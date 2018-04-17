from django.shortcuts import render
from app_quiz.models import Section, Question, Answer
from app_quiz.models import TestQuestion, TestAnswer

import random

import os
import logging

DO_LOGGING = True

if DO_LOGGING:
    logging.basicConfig(format="%(asctime)s  %(filename)s:%(lineno)d  %(message)s",
                        datefmt="%Y-%m-%d  %H:%M.%S", level=logging.DEBUG, filename='norveg.log')


css_class_current = 'badge badge-pill grey darken-2'
css_class_no_answer = 'badge badge-pill grey'
css_class_is_answer = 'badge badge-pill light-blue darken-1'
css_class_right_answer = 'badge badge-pill green'
css_class_wrong_answer = 'badge badge-pill red'

section_question = {
    '1':  {'from': 1,   'to': 10,  'amount_for_test': 2},
    '2':  {'from': 11,  'to': 35,  'amount_for_test': 4},
    '3':  {'from': 36,  'to': 50,  'amount_for_test': 3},
    '4':  {'from': 51,  'to': 70,  'amount_for_test': 3},
    '5':  {'from': 71,  'to': 76,  'amount_for_test': 1},
    '6':  {'from': 77,  'to': 86,  'amount_for_test': 2},
    '7':  {'from': 87,  'to': 92,  'amount_for_test': 1},
    '8':  {'from': 93,  'to': 97,  'amount_for_test': 1},
    '9':  {'from': 98,  'to': 105, 'amount_for_test': 2},
    '10': {'from': 106, 'to': 111, 'amount_for_test': 1},
    '11': {'from': 112, 'to': 127, 'amount_for_test': 2},
    '12': {'from': 128, 'to': 142, 'amount_for_test': 2},
    '13': {'from': 143, 'to': 158, 'amount_for_test': 2},
    '14': {'from': 159, 'to': 163, 'amount_for_test': 1},
    '15': {'from': 164, 'to': 173, 'amount_for_test': 2},
    '16': {'from': 174, 'to': 179, 'amount_for_test': 1},
    '17': {'from': 180, 'to': 187, 'amount_for_test': 2},
    '18': {'from': 188, 'to': 192, 'amount_for_test': 1},
    '19': {'from': 193, 'to': 195, 'amount_for_test': 1},
    '20': {'from': 196, 'to': 201, 'amount_for_test': 1},
    '21': {'from': 202, 'to': 210, 'amount_for_test': 2},
    '22': {'from': 211, 'to': 219, 'amount_for_test': 2},
    '23': {'from': 220, 'to': 228, 'amount_for_test': 2},
    '24': {'from': 229, 'to': 233, 'amount_for_test': 1},
    '25': {'from': 234, 'to': 239, 'amount_for_test': 1},
    '26': {'from': 240, 'to': 250, 'amount_for_test': 2}
}


def learning(request, section_number, question_num_in_section):
    section_text = Section.objects.filter(pk=section_number)[0].text_eng
    question_num_real = section_question[str(section_number)]['from'] + question_num_in_section - 1
    question_amount = Question.objects.filter(section__exact=section_number).count()
    question_eng = Question.objects.all()[question_num_real-1].text_eng
    question_rus = Question.objects.all()[question_num_real-1].text_rus
    question_pk = Question.objects.filter(number=question_num_real)[0].id
    question_image = Question.objects.all()[question_num_real-1].image

    if DO_LOGGING:
        logging.info(f' LEARN ({request.META["REMOTE_ADDR"]}) sec.{section_number}  #{question_num_in_section} (of {question_amount})')

    answers = list(Answer.objects.filter(question=question_pk).values_list('text_eng', 'text_rus', 'text_nor', 'letter', 'correct'))
    random.shuffle(answers)

    dict_answers = {}

    for num, answer in enumerate(answers):
        dict_answers.update(
            {str(num+1):
                 {
                    'eng': str(answer[0]),
                    'rus': str(answer[1]),
                    'nor': str(answer[2]),
                    'letter': str(answer[3]),
                    'correct': str(answer[4]),
                    'checkbox_eng': 'checkbox_eng_' + str(num + 1),
                    'checkbox_rus': 'checkbox_rus_' + str(num + 1),
                    'checkbox_nor': 'checkbox_nor_' + str(num + 1)
                 }
            }
        )

    return render(request, 'app_quiz/learning.html', {
        'section_number': section_number,
        'section_text': section_text,
        'question_num_in_section': question_num_in_section,
        'question_amount': question_amount,
        'question_eng': question_eng,
        'question_rus': question_rus,
        'dict_answers': dict_answers,
        'question_image': question_image,
        'right_msg': random.choice(['YES! YOU ARE RIGHT!', 'GREAT!', 'RIGHT!', 'CORRECT ANSWER!', 'THAT IS RIGHT!']),
        'right_img': 'yes_' + str(random.choice(range(1, 9))) + '.gif',
        'wrong_msg': random.choice(['NO! YOU ARE WRONG!', 'WRONG!', 'WRONG ANSWER!', 'INCORRECT ANSWER!', 'THAT IS WRONG!']),
        'wrong_img': 'no_' + str(random.choice(range(1, 10))) + '.gif',
    })


def create_test():
    if DO_LOGGING:
        logging.info(f' ---------- CREATE NEW TEST ----------')

    TestQuestion.objects.all().delete()
    TestAnswer.objects.all().delete()

    sec_rand = list(range(1, 27))
    random.shuffle(sec_rand)

    for section_num in sec_rand:
        am_for_test = section_question[str(section_num)]['amount_for_test']

        ls_questions = random.sample(list(Question.objects.filter(section__exact=
            str(section_num)).values_list('id', 'number', 'section', 'text_eng', 'text_rus', 'text_nor', 'image')), am_for_test)

        for quest in ls_questions:
            TestQuestion.objects.create(q_num=quest[1], section=quest[2], text_eng=quest[3], text_rus=quest[4],
                text_nor=quest[5], image=quest[6], css_class=css_class_no_answer)

            ls_answers = list(Answer.objects.filter(question=quest[0]).values_list(
                'id', 'question', 'letter', 'text_eng', 'text_rus', 'text_nor', 'correct'))

            random.shuffle(ls_answers)

            a_num = 0

            for answer in ls_answers:
                a_num += 1

                TestAnswer.objects.create(q_num=answer[1], letter=answer[2], text_eng=answer[3], text_rus=answer[4],
                    text_nor=answer[5], correct=answer[6], user_answer='', checkbox='checkbox_' + str(a_num))


def user_answer_processing(user_answer):
    arr_split_user_answer = user_answer.split('-')
    q_order_num = int(arr_split_user_answer[0]) - 1
    qnum = TestQuestion.objects.all()[q_order_num].q_num

    is_answer = False

    for loop in range(1, len(arr_split_user_answer)):
        curr_answer = TestAnswer.objects.filter(q_num__exact=qnum)[loop - 1]

        if arr_split_user_answer[loop] == '1':
            is_answer = True

            curr_answer.user_answer = 'checked'
            curr_answer.save()
        else:
            curr_answer.user_answer = ''
            curr_answer.save()

    curr_question = TestQuestion.objects.all()[q_order_num]

    if is_answer:
        curr_question.css_class = css_class_is_answer
        curr_question.save()
    else:
        curr_question.css_class = css_class_no_answer
        curr_question.save()


def testing(request, new_test, question_number, user_answer=None):
    if new_test == 'yes' or TestQuestion.objects.all().count() == 0:
        create_test()

    if user_answer:
        user_answer_processing(user_answer)

    q_curr = TestQuestion.objects.all()[question_number-1]
    q_curr.css_class = css_class_current
    q_curr.save()

    if DO_LOGGING:
        logging.info(f' TEST {request.META["REMOTE_ADDR"]}, #{question_number}')

    return render(request, 'app_quiz/testing.html', {
        'q_amount': TestQuestion.objects.all().count(),
        'test_question': TestQuestion.objects.all()[question_number-1],
        'test_answers': TestAnswer.objects.filter(q_num=TestQuestion.objects.all()[question_number-1].q_num),
        'question_number': question_number,
        'lst_questions_map': list(TestQuestion.objects.all().values_list('css_class', flat=True)),
        'new_test': new_test
    })


def set_endtest_qmap():
    for question_loop in range(TestQuestion.objects.all().count()):
        is_answer_temp = False
        is_right_answer_temp = True
        curr_question = TestQuestion.objects.all()[question_loop]
        qnum = curr_question.q_num

        answers_amount = TestAnswer.objects.filter(q_num__exact=qnum).count()

        for answer_loop in range(answers_amount):
            if TestAnswer.objects.filter(q_num__exact=qnum)[answer_loop].user_answer == 'checked':
                is_answer_temp = True

                if TestAnswer.objects.filter(q_num__exact=qnum)[answer_loop].correct != 'true':
                    is_right_answer_temp = False

        if is_answer_temp:
            if is_right_answer_temp:
                curr_question.css_class = css_class_right_answer
            else:
                curr_question.css_class = css_class_wrong_answer
        else:
            curr_question.css_class = css_class_no_answer

        curr_question.save()


def is_test_pass():
    right_answer_amount = 0
    wrong_answer_amount = 0
    is_test_pass_message = ''

    for question_loop in range(TestQuestion.objects.all().count()):
        curr_question = TestQuestion.objects.all()[question_loop]

        if curr_question.css_class == css_class_right_answer:
            right_answer_amount += 1
        elif curr_question.css_class == css_class_wrong_answer:
            wrong_answer_amount += 1

    if right_answer_amount > 37:
        is_test_pass_message = ' - THE TEST IS PASSED! - '
        is_test_pass_color = 'lightgreen'
        is_test_pass_image = 'yes_' + str(random.choice(range(1, 9))) + '.gif'
    else:
        is_test_pass_message = ' - THE TEST IS FAILED! - '
        is_test_pass_color = 'red'
        is_test_pass_image = 'no_' + str(random.choice(range(1, 10))) + '.gif'

    return right_answer_amount, wrong_answer_amount, \
           45-right_answer_amount-wrong_answer_amount, \
           is_test_pass_message, is_test_pass_color, is_test_pass_image


def end_test(request, user_answer):
    if len(user_answer) > 2:        # user_answer = 32-0-1-0-1
        user_answer_processing(user_answer)
        set_endtest_qmap()
        show_question = 'no'
        question_number = 1
        right_answer_amount, wrong_answer_amount, not_answer, is_test_pass_message, is_test_pass_color, is_test_pass_image = is_test_pass()

    else:                           # user_answer = 1..45
        show_question = 'yes'
        question_number = int(user_answer)
        right_answer_amount, wrong_answer_amount, not_answer, is_test_pass_message, is_test_pass_color, is_test_pass_image = is_test_pass()

    if DO_LOGGING:
        logging.info(f' ===== END TEST ({request.META["REMOTE_ADDR"]}) = ri.{right_answer_amount} wr.{wrong_answer_amount} na.{not_answer} {is_test_pass_message}')

    return render(request, 'app_quiz/end_test.html', {
        'lst_questions_map': list(TestQuestion.objects.all().values_list('css_class', flat=True)),
        'show_question': show_question,
        'test_question': TestQuestion.objects.all()[question_number-1],
        'test_answers': TestAnswer.objects.filter(q_num=TestQuestion.objects.all()[question_number-1].q_num),
        'question_number': question_number,
        'right_answer_amount': right_answer_amount,
        'wrong_answer_amount': wrong_answer_amount,
        'not_answer': not_answer,
        'is_test_pass_message': is_test_pass_message,
        'is_test_pass_color': is_test_pass_color,
        'is_test_pass_image': is_test_pass_image,
    })

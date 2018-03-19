from django.shortcuts import render
from app_quiz.models import Section, Question, Answer
import random
import pprint

list_qna = []
lst_questions_map = {}

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


class QnA:
    def __init__(self, dict_question, dict_answers):
        self.question = dict_question
        self.answers = dict_answers

    def __repr__(self):
        return f"question={self.question}\nanswers={self.answers}"


def learning(request, section_number, question_num_in_section):
    section_text = Section.objects.filter(pk=section_number)[0].text_eng
    question_num_real = section_question[str(section_number)]['from'] + question_num_in_section - 1
    question_amount = Question.objects.filter(section__exact=section_number).count()
    question_eng = Question.objects.all()[question_num_real-1].text_eng
    question_rus = Question.objects.all()[question_num_real-1].text_rus
    question_pk = Question.objects.filter(number=question_num_real)[0].id
    question_image = Question.objects.all()[question_num_real-1].image

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
        # 'navbar_right': 'привет, falkov!',
    })


def create_test():
    list_qna.clear()

    sec_rand = list(range(1, 27))
    random.shuffle(sec_rand)

    for section_num in sec_rand:
        am_for_test = section_question[str(section_num)]['amount_for_test']

        ls_questions = random.sample(list(Question.objects.filter(section__exact=str(section_num)).values_list
                        ('id', 'number', 'section', 'text_eng', 'text_rus', 'text_nor', 'image')), am_for_test)

        for quest in ls_questions:
            dict_question = {}

            dict_question['id'] = quest[0]
            dict_question['number'] = quest[1]
            dict_question['section'] = quest[2]
            dict_question['text_eng'] = quest[3]
            dict_question['text_rus'] = quest[4]
            dict_question['text_nor'] = quest[5]
            dict_question['image'] = quest[6]

            ls_answers = list(Answer.objects.filter(question=quest[0]).values_list
                ('id', 'question', 'letter', 'text_eng', 'text_rus', 'text_nor', 'correct'))

            random.shuffle(ls_answers)

            dict_answers = {}
            a_num = 0

            for answer in ls_answers:
                a_num += 1

                dict_answers.update({
                    str(a_num): {
                        'id': answer[0],
                        'question': answer[1],
                        'letter': answer[2],
                        'text_eng': answer[3],
                        'text_rus': answer[4],
                        'text_nor': answer[5],
                        'correct': answer[6],
                        'user_answer': '',
                        'checkbox': 'checkbox_' + str(a_num),
                    }
                })

            qna = QnA(dict_question, dict_answers)
            list_qna.append(qna)


def create_questions_map():
    lst_questions_map.clear()

    for num, quest in enumerate(list_qna):
        lst_questions_map[num+1] = css_class_no_answer


def user_answer_processing(user_answer):
    arr_split_user_answer = user_answer.split('-')
    qn = int(arr_split_user_answer[0]) - 1
    lst_questions_map[qn + 1] = css_class_no_answer

    for loop in range(1, len(arr_split_user_answer)):
        list_qna[qn].answers[str(loop)]['user_answer'] = arr_split_user_answer[loop]

        if arr_split_user_answer[loop] == '1':
            list_qna[qn].answers[str(loop)]['user_answer'] = 'checked'
            lst_questions_map[qn + 1] = css_class_is_answer
        else:
            list_qna[qn].answers[str(loop)]['user_answer'] = ''


def testing(request, new_test, question_number, user_answer=None, endtest=None):
    if new_test == 'yes' or len(list_qna) == 0:
        create_test()
        create_questions_map()

    if user_answer:
        user_answer_processing(user_answer)

    lst_questions_map[question_number] = css_class_current

    return render(request, 'app_quiz/testing.html', {
        'list_qna': list_qna,
        'question_number': question_number,
        'qna_curr': list_qna[question_number-1],
        'lst_questions_map': lst_questions_map,
        'new_test': new_test
    })


def set_endtest_qmap():
    for question_loop in range(len(list_qna)):
        is_answer_temp = False
        is_right_answer_temp = True

        for answer_loop in range(len(list_qna[question_loop].answers)):
            if list_qna[question_loop].answers[str(answer_loop + 1)]['user_answer'] == 'checked':
                is_answer_temp = True

                if list_qna[question_loop].answers[str(answer_loop + 1)]['correct'] != 'true':
                    is_right_answer_temp = False

        if is_answer_temp:
            if is_right_answer_temp:
                lst_questions_map[question_loop + 1] = css_class_right_answer
            else:
                lst_questions_map[question_loop + 1] = css_class_wrong_answer
        else:
            lst_questions_map[question_loop + 1] = css_class_no_answer


def is_test_pass():
    right_answer_amount = 0
    wrong_answer_amount = 0
    is_test_pass_message = ''

    for loop in range(1, len(lst_questions_map)):
        if lst_questions_map[loop] == css_class_right_answer:
            right_answer_amount += 1
        elif lst_questions_map[loop] == css_class_wrong_answer:
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
    # user_answer = 32-0-1-0-1  или  1..45
    if len(user_answer) > 2:
        user_answer_processing(user_answer)
        set_endtest_qmap()
        show_question = 'no'
        question_number = 0
        right_answer_amount, wrong_answer_amount, not_answer, is_test_pass_message, is_test_pass_color, is_test_pass_image = is_test_pass()

    else:
        show_question = 'yes'
        question_number = int(user_answer)
        right_answer_amount, wrong_answer_amount, not_answer, is_test_pass_message, is_test_pass_color, is_test_pass_image = is_test_pass()


    return render(request, 'app_quiz/end_test.html', {
        'list_qna': list_qna,
        'lst_questions_map': lst_questions_map,
        'show_question': show_question,
        'qna_curr': list_qna[question_number - 1],
        'question_number': question_number,
        'right_answer_amount': right_answer_amount,
        'wrong_answer_amount': wrong_answer_amount,
        'not_answer': not_answer,
        'is_test_pass_message': is_test_pass_message,
        'is_test_pass_color': is_test_pass_color,
        'is_test_pass_image': is_test_pass_image

        # 'cur_css_class': lst_questions_map[question_number]

    })

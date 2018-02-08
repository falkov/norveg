from django.shortcuts import render
from app_quiz.models import Section, Question, Answer
import random

section_question = {
    '1':  {'from': 1,   'to': 10},
    '2':  {'from': 11,  'to': 35},
    '3':  {'from': 36,  'to': 50},
    '4':  {'from': 51,  'to': 70},
    '5':  {'from': 71,  'to': 76},
    '6':  {'from': 77,  'to': 86},
    '7':  {'from': 87,  'to': 92},
    '8':  {'from': 93,  'to': 97},
    '9':  {'from': 98,  'to': 105},
    '10': {'from': 106, 'to': 111},
    '11': {'from': 112, 'to': 127},
    '12': {'from': 128, 'to': 142},
    '13': {'from': 143, 'to': 158},
    '14': {'from': 159, 'to': 163},
    '15': {'from': 164, 'to': 173},
    '16': {'from': 174, 'to': 179},
    '17': {'from': 180, 'to': 187},
    '18': {'from': 188, 'to': 192},
    '19': {'from': 193, 'to': 195},
    '20': {'from': 196, 'to': 201},
    '21': {'from': 202, 'to': 210},
    '22': {'from': 211, 'to': 219},
    '23': {'from': 220, 'to': 228},
    '24': {'from': 229, 'to': 233},
    '25': {'from': 234, 'to': 239},
    '26': {'from': 240, 'to': 250}
}


# Create your views here.
def learning(request, section_number, question_num_in_section):
    section_text = Section.objects.filter(pk=section_number)[0].text_eng
    question_num_real = section_question[str(section_number)]['from'] + question_num_in_section - 1
    question_amount = Question.objects.filter(section__exact=section_number).count()
    question_eng = Question.objects.all()[question_num_real-1].text_eng
    question_rus = Question.objects.all()[question_num_real-1].text_rus
    question_pk = Question.objects.filter(number=question_num_real)[0].id

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

    print(request.build_absolute_uri())
    # url_next_question = { % url 'learning' 1 1 %}

    return render(request, 'app_quiz/learning.html', {
        'section_number': section_number,
        'section_text': section_text,
        'question_num_in_section': question_num_in_section,
        'question_amount': question_amount,
        'question_eng': question_eng,
        'question_rus': question_rus,
        'dict_answers': dict_answers,
        # 'navbar_right': 'привет, falkov!',
    })

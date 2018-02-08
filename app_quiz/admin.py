from django.contrib import admin

from app_quiz.models import Section
from app_quiz.models import Question
from app_quiz.models import Answer

# Register your models here.
admin.site.register(Section)
admin.site.register(Question)
admin.site.register(Answer)

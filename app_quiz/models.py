from django.db import models


class Section(models.Model):
    section_number = models.IntegerField(default=0)
    text_eng = models.CharField(max_length=80, default="")
    text_rus = models.CharField(max_length=80, default="")
    text_nor = models.CharField(max_length=80, default="")

    def __str__(self):
        return self.text_eng


class Question(models.Model):
    number = models.IntegerField(default=0)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    text_eng = models.CharField(max_length=300, default="")
    text_rus = models.CharField(max_length=300, default="")
    text_nor = models.CharField(max_length=300, default="")
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.text_eng


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    letter = models.CharField(max_length=1, default="")
    text_eng = models.CharField(max_length=300, default="")
    text_rus = models.CharField(max_length=300, default="")
    text_nor = models.CharField(max_length=300, default="")
    correct = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.text_eng


class TestQuestion(models.Model):
    q_num = models.IntegerField(default=0)
    section = models.IntegerField(default=0)
    text_eng = models.CharField(max_length=300, default="")
    text_rus = models.CharField(max_length=300, default="")
    text_nor = models.CharField(max_length=300, default="")
    image = models.ImageField(blank=True)
    css_class = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.text_eng


class TestAnswer(models.Model):
    q_num = models.IntegerField(default=0)
    letter = models.CharField(max_length=1, default="")
    text_eng = models.CharField(max_length=300, default="")
    text_rus = models.CharField(max_length=300, default="")
    text_nor = models.CharField(max_length=300, default="")
    correct = models.CharField(max_length=10, default="")
    user_answer = models.CharField(max_length=10, default="")
    checkbox = models.CharField(max_length=12, default="")

    def __str__(self):
        return self.text_eng

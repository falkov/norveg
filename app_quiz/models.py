from django.db import models


class Section(models.Model):
    section_number = models.IntegerField(default=0)
    text_eng = models.CharField(max_length=80)
    text_rus = models.CharField(max_length=80)
    text_nor = models.CharField(max_length=80)

    def __str__(self):
        return self.text_eng


class Question(models.Model):
    number = models.IntegerField(default=0)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    text_eng = models.CharField(max_length=300)
    text_rus = models.CharField(max_length=300)
    text_nor = models.CharField(max_length=300)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.text_eng


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    letter = models.CharField(max_length=1, default="")
    text_eng = models.CharField(max_length=300)
    text_rus = models.CharField(max_length=300)
    text_nor = models.CharField(max_length=300)
    # correct = models.BooleanField()
    correct = models.CharField(max_length=10)

    def __str__(self):
        return self.text_eng

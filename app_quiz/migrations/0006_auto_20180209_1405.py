# Generated by Django 2.0.1 on 2018-02-09 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_quiz', '0005_section_section_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='correct',
            field=models.CharField(max_length=10),
        ),
    ]
# Generated by Django 2.0.1 on 2018-04-22 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_quiz', '0010_auto_20180321_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='testquestion',
            name='q_num_in_test',
            field=models.IntegerField(default=0),
        ),
    ]

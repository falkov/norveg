# Generated by Django 2.0.1 on 2018-03-20 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_quiz', '0007_auto_20180320_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testquestion',
            name='section',
            field=models.IntegerField(default=0),
        ),
    ]
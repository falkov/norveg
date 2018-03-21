# Generated by Django 2.0.1 on 2018-03-20 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_quiz', '0006_auto_20180209_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(default='', max_length=1)),
                ('text_eng', models.CharField(max_length=300)),
                ('text_rus', models.CharField(max_length=300)),
                ('text_nor', models.CharField(max_length=300)),
                ('correct', models.CharField(max_length=10)),
                ('user_answer', models.CharField(max_length=10)),
                ('checkbox', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('text_eng', models.CharField(max_length=300)),
                ('text_rus', models.CharField(max_length=300)),
                ('text_nor', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_quiz.Section')),
            ],
        ),
        migrations.AddField(
            model_name='testanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_quiz.TestQuestion'),
        ),
    ]

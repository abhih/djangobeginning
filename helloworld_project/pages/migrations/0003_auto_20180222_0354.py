# Generated by Django 2.0.2 on 2018-02-21 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180222_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(choices=[('ML', 'Machine Learning'), ('DS', 'Data Science')], default='None', max_length=1),
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.IntegerField(auto_created=True, default='0'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default='01-01-1951', verbose_name='date_published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default='Blank post', max_length=180),
        ),
    ]
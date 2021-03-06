# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0006_delete_smtpmail'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferralUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок(для админки)')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('photo', models.ImageField(upload_to='images/referal_images', verbose_name='Изображение')),
            ],
            options={
                'verbose_name_plural': 'Реферальные ссылки',
                'verbose_name': 'Реферальная ссылка',
            },
        ),
        migrations.AlterField(
            model_name='catalog',
            name='url',
            field=models.URLField(help_text='Ссылка на каталог в Google-документах', max_length=300),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='code_number',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Код в NL'),
        ),
        migrations.AlterField(
            model_name='video',
            name='priority',
            field=models.IntegerField(default=1, verbose_name='Приоритет в разделе "Видео"'),
        ),
    ]

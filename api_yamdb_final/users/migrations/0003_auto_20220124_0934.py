# Generated by Django 2.2.16 on 2022-01-24 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220123_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='MHsV9wqMaWveXPd', editable=False, help_text='UUID код подтверждения для получения токена', max_length=10, verbose_name='Код подтверждения'),
        ),
    ]

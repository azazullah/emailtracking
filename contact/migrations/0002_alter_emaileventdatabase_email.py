# Generated by Django 4.0.4 on 2022-05-30 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaileventdatabase',
            name='email',
            field=models.EmailField(max_length=250),
        ),
    ]

# Generated by Django 4.2.8 on 2023-12-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('html_website_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='News_Date',
            field=models.DateField(),
        ),
    ]
# Generated by Django 3.2.11 on 2022-01-11 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_review_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(choices=[('down', 'Down Vote'), ('up', 'Up Vote')], max_length=200),
        ),
    ]

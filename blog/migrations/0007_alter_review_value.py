# Generated by Django 3.2.11 on 2022-01-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220111_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(choices=[('down', 'Down Vote'), ('up', 'Up Vote')], max_length=200),
        ),
    ]
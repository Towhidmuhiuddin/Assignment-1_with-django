# Generated by Django 4.1.3 on 2022-12-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0002_delete_teacher_rename_group_school_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='weekly_class',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 4.0.2 on 2022-04-03 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_privateinfo_teacherdutydate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='honor',
            name='text',
            field=models.CharField(default='None', max_length=200),
        ),
    ]

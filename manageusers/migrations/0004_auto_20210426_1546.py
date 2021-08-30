# Generated by Django 3.1.7 on 2021-04-26 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageusers', '0003_auto_20210420_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=100)),
                ('task_description', models.CharField(max_length=250)),
                ('task_duedate', models.DateField()),
                ('task_priority', models.CharField(max_length=20)),
                ('task_assignee', models.CharField(max_length=100)),
                ('task_assignto', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='user_email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
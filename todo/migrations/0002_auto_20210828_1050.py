# Generated by Django 3.2.6 on 2021-08-28 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250, unique=True)),
                ('email', models.EmailField(max_length=200)),
                ('text', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'NOT_COMPLETED'), (1, 'NOT_COMPLETED_ADMIN_EDIT'), (10, 'FULLY_COMPLETED'), (11, 'FULLY_COMPLETED_ADMIN_EDIT')], verbose_name='status_completed')),
            ],
        ),
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.IntegerField(choices=[(0, 'NOT_COMPLETED'), (1, 'NOT_COMPLETED_ADMIN_EDIT'), (10, 'FULLY_COMPLETED'), (11, 'FULLY_COMPLETED_ADMIN_EDIT')], verbose_name='status_completed'),
        ),
    ]

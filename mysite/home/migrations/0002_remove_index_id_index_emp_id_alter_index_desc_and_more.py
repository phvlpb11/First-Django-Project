# Generated by Django 4.0.5 on 2022-06-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='id',
        ),
        migrations.AddField(
            model_name='index',
            name='emp_id',
            field=models.CharField(default=0, max_length=122, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='index',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]

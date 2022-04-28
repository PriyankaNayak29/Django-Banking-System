# Generated by Django 4.0.2 on 2022-03-31 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RejectedLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.TextField(max_length=50)),
                ('gid', models.TextField(max_length=50)),
                ('amount', models.FloatField()),
                ('income', models.IntegerField()),
                ('purpose', models.TextField(max_length=50)),
                ('remark', models.TextField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'rejected_loan',
            },
        ),
    ]

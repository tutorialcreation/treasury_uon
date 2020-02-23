# Generated by Django 2.2.7 on 2020-02-23 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_status', models.CharField(choices=[('C', 'Completed'), ('I', 'Incompleted')], max_length=20)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('paid_in', models.IntegerField()),
                ('withdrawn', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('balance_confirmed', models.BooleanField()),
                ('reason_type', models.CharField(choices=[('P', 'Pay utility'), ('O', 'Pay Utility with OD via sdk')], max_length=20)),
                ('other_party_no', models.CharField(max_length=200, null=True)),
                ('linked', models.BooleanField()),
                ('account_no', models.CharField(max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-25 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('balance', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=128)),
                ('adminRole', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('0', 'SPEND'), ('1', 'BUY')], max_length=5)),
                ('amount', models.PositiveIntegerField()),
                ('timeDate', models.DateTimeField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.user')),
            ],
        ),
    ]
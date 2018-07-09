# Generated by Django 2.0.5 on 2018-05-23 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('useremail', models.EmailField(blank=True, max_length=100)),
                ('userbirth', models.DateField()),
            ],
        ),
    ]
# Generated by Django 3.1 on 2020-09-18 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200917_2009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['pk']},
        ),
    ]
# Generated by Django 3.2.6 on 2021-09-03 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-star',), 'verbose_name_plural': 'Customer feedback'},
        ),
    ]
# Generated by Django 4.0.2 on 2022-02-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='faculty',
            field=models.CharField(choices=[('fsc', 'Faculty of Science'), ('mbbs', 'Medicine and Surgery'), ('law', 'Faculty of Law')], default=None, max_length=7),
        ),
    ]

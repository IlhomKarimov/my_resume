# Generated by Django 4.1.2 on 2022-10-10 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workmodel',
            name='image',
            field=models.ImageField(default=1, upload_to='works'),
            preserve_default=False,
        ),
    ]

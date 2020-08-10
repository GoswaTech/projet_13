# Generated by Django 3.1 on 2020-08-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_auto_20200808_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablepost',
            name='script_js',
            field=models.TextField(blank=True, max_length=2047, null=True),
        ),
        migrations.AlterField(
            model_name='tablepost',
            name='style_css',
            field=models.FileField(blank=True, null=True, upload_to='styles_css/'),
        ),
    ]

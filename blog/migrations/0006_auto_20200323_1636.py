# Generated by Django 3.0.2 on 2020-03-23 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200323_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postattachment',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='postfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]
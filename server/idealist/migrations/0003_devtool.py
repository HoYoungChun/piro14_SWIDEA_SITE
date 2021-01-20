# Generated by Django 3.1.5 on 2021-01-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idealist', '0002_auto_20210120_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevTool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='이름')),
                ('kind', models.CharField(max_length=100, verbose_name='종류')),
                ('description', models.TextField(verbose_name='개발툴 설명')),
            ],
        ),
    ]

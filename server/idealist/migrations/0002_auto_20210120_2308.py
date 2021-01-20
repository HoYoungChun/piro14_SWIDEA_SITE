# Generated by Django 3.1.5 on 2021-01-20 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idealist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='devtool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devtool', to='idealist.devtool', verbose_name='예상 개발툴'),
        ),
    ]

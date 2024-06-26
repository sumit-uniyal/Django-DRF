# Generated by Django 5.0.2 on 2024-06-26 01:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='mail',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='email_auth.color'),
        ),
    ]

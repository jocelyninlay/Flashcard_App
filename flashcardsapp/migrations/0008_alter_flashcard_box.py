# Generated by Django 4.0.3 on 2022-03-15 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcardsapp', '0007_alter_flashcard_box'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='box',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='box', to='flashcardsapp.box'),
        ),
    ]

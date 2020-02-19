# Generated by Django 3.0.3 on 2020-02-19 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burn', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='meals',
            new_name='meal',
        ),
        migrations.AlterField(
            model_name='meal',
            name='meal_name',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='goal',
            field=models.CharField(choices=[('Lose weight', 'Lose weight'), ('Maintain weight', 'Maintain weight'), ('Bulk up', 'Bulk up')], max_length=20),
        ),
    ]
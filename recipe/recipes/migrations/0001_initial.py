# Generated by Django 5.0.3 on 2024-03-10 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cuisine', models.CharField(choices=[('Chinese', 'Chinese'), ('Indian', 'Indain'), ('Japanese', 'Japanese')], default='indian', max_length=40)),
                ('meal_type', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], max_length=20)),
                ('imag', models.ImageField(blank=True, null=True, upload_to='recipe/image')),
            ],
        ),
    ]

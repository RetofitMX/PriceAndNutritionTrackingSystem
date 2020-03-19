# Generated by Django 3.0.4 on 2020-03-19 11:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0021_recipe_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='in_recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='components', to='recipes.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='serves',
            field=models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
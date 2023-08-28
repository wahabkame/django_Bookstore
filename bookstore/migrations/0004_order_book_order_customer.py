# Generated by Django 4.2.4 on 2023-08-07 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_book_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='Order',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookstore.book'),
        ),
        migrations.AddField(
            model_name='Order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookstore.customer'),
        ),
    ]

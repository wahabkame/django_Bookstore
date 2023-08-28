# Generated by Django 4.2.4 on 2023-08-07 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_order_book_order_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='tag',
            field=models.ManyToManyField(to='bookstore.tag'),
        ),
    ]

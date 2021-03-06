# Generated by Django 4.0.1 on 2022-01-09 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_goods', models.CharField(max_length=100, verbose_name='Наименование товара')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Текст записи')),
                ('category', models.CharField(choices=[('other', 'Other'), ('laptops', 'Laptops'), ('monitors', 'Monitors'), ('office_equipment', 'Office_equipment'), ('video_surveillance', 'Video_surveillance')], default='other', max_length=20, verbose_name='Категории')),
                ('residue', models.PositiveIntegerField(verbose_name='Остаток')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Стоимость')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'db_table': 'product',
            },
        ),
    ]

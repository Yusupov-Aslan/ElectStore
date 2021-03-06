# Generated by Django 4.0.1 on 2022-02-06 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ElectStore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('other', 'Other'), ('laptops', 'Laptops'), ('monitors', 'Monitors'), ('office_equipment', 'Office equipment'), ('video_surveillance', 'Video surveillance')], default='other', max_length=20, verbose_name='Категории'),
        ),
        migrations.AlterModelTable(
            name='product',
            table=None,
        ),
        migrations.CreateModel(
            name='ItemCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_carts', to='ElectStore.product', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
            },
        ),
    ]

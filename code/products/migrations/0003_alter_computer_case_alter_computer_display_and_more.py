# Generated by Django 4.2.5 on 2023-09-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_brand_image_alter_cloth_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='case',
            field=models.CharField(blank=True, choices=[('Mini-itx', 'Mini-Itx'), ('Micro-atx', 'Micro-Atx'), ('Atx', 'Atx')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='display',
            field=models.CharField(blank=True, choices=[('Ips', 'Ips'), ('Tn', 'Tn'), ('Va', 'Va'), ('Oled', 'Oled')], default='Ips', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='refresh_rate',
            field=models.CharField(blank=True, choices=[('60Hz', '60Hz'), ('75Hz', '75Hz'), ('90Hz', '90Hz'), ('120Hz', '120Hz'), ('144Hz', '144Hz'), ('240Hz', '240Hz')], default='60Hz', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='resolution',
            field=models.CharField(blank=True, choices=[('768P', '768P'), ('1080P', '1080P'), ('1440P', '1440P'), ('4K', '4K')], default='1080P', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='size',
            field=models.CharField(blank=True, choices=[('14"', '14"'), ('15.6"', '15.6"'), ('16"', '16"'), ('24"', '24"'), ('27"', '27"'), ('32"', '32"')], default='15.6"', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='display',
            field=models.CharField(blank=True, choices=[('Ips', 'Ips'), ('Va', 'Va'), ('Oled', 'Oled')], default='Ips', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='refresh_rate',
            field=models.CharField(blank=True, choices=[('60Hz', '60Hz'), ('75Hz', '75Hz'), ('90Hz', '90Hz'), ('120Hz', '120Hz'), ('144Hz', '144Hz'), ('240Hz', '240Hz')], default='90Hz', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='resolution',
            field=models.CharField(blank=True, choices=[('1080P', '1080P'), ('1440P', '1440P'), ('4K', '4K')], default='1440P', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='size',
            field=models.CharField(blank=True, choices=[('5.8"', '5.8"'), ('6.0"', '6.0"'), ('6.2"', '6.2"'), ('6.4"', '6.4"'), ('6.6"', '6.6"'), ('6.8"', '6.8"'), ('9.7"', '9.7"'), ('10.1"', '10.1"'), ('12"', '12"')], default='6.2"', max_length=10, null=True),
        ),
    ]
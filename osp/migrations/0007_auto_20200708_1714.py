# Generated by Django 3.0.6 on 2020-07-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("osp", "0006_auto_20200707_1707"),
    ]

    operations = [
        migrations.AlterField(
            model_name="form",
            name="form_fields",
            field=models.ManyToManyField(blank=True, default=None, related_name="form_fields", to="osp.Question"),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 00:49
from __future__ import unicode_literals

from django.db import migrations


def forwards_func(apps, schema_editor):
    CustomIndexer = apps.get_model("dvaapp", "CustomIndexer")
    db_alias = schema_editor.connection.alias
    CustomIndexer.objects.using(db_alias).bulk_create([
        CustomIndexer(name="inception",algorithm="inception"),
        CustomIndexer(name="facenet",algorithm="facenet"),
    ])


def reverse_func(apps, schema_editor):
    CustomIndexer = apps.get_model("dvaapp", "CustomIndexer")
    db_alias = schema_editor.connection.alias
    CustomIndexer.objects.using(db_alias).filter(name="inception").delete()
    CustomIndexer.objects.using(db_alias).filter(name="facenet").delete()


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]

# Generated by Django 4.1.3 on 2022-12-12 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "topic_name",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="webpage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("URL", models.URLField()),
                (
                    "topic_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.topic"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="access",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                (
                    "topic_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.webpage"
                    ),
                ),
            ],
        ),
    ]

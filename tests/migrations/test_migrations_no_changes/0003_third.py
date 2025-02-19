from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("migrations", "0002_second"),
    ]

    operations = [
        migrations.CreateModel(
            name="ModelWithCustomBase",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
            ],
            options={},
            bases=(models.Model,),
            metaclass="CustomModelBase",
        ),
        migrations.CreateModel(
            name="UnmigratedModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
            ],
            options={},
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name="Author",
        ),
        migrations.DeleteModel(
            name="Book",
        ),
    ]

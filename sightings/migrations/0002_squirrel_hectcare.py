from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='squirrel',
            name='Hectcare',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

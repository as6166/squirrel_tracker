
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Unique_Squirrel_ID', models.CharField(max_length=100, unique=True)),
                ('Shift', models.CharField(blank=True, max_length=100)),
                ('Date', models.CharField(blank=True, max_length=100)),
                ('Age', models.CharField(blank=True, max_length=100)),
                ('Primary_Fur_Color', models.CharField(blank=True, max_length=100)),
                ('Location', models.CharField(blank=True, max_length=100)),
                ('Specific_Location', models.CharField(blank=True, max_length=100)),
                ('Running', models.BooleanField(blank=True)),
                ('Chasing', models.BooleanField(blank=True)),
                ('Climbing', models.BooleanField(blank=True)),
                ('Eating', models.BooleanField(blank=True)),
                ('Foraging', models.BooleanField(blank=True)),
                ('Other_Activities', models.CharField(blank=True, max_length=100)),
                ('Kuks', models.BooleanField(blank=True)),
                ('Quaas', models.BooleanField(blank=True)),
                ('Moans', models.BooleanField(blank=True)),
                ('Tail_Flags', models.BooleanField(blank=True)),
                ('Tail_Twitches', models.BooleanField(blank=True)),
                ('Approaches', models.BooleanField(blank=True)),
                ('Indifferent', models.BooleanField(blank=True)),
                ('Runs_From', models.BooleanField(blank=True)),
            ],
        ),
    ]

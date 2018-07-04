# Generated by Django 2.0.7 on 2018-07-04 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pct', '0015_auto_20180704_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inaturalistobservation',
            name='closest_mile',
            field=models.ForeignKey(blank=True, limit_choices_to={'type': 'mile'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pct.HalfmileWaypoint'),
        ),
        migrations.AlterField(
            model_name='inaturalistobservation',
            name='closest_poi',
            field=models.ForeignKey(blank=True, limit_choices_to={'type': 'poi'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pct.HalfmileWaypoint'),
        ),
        migrations.AlterField(
            model_name='instagrampost',
            name='closest_mile',
            field=models.ForeignKey(blank=True, limit_choices_to={'type': 'mile'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pct.HalfmileWaypoint'),
        ),
        migrations.AlterField(
            model_name='instagrampost',
            name='closest_poi',
            field=models.ForeignKey(blank=True, limit_choices_to={'type': 'poi'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pct.HalfmileWaypoint'),
        ),
        migrations.AlterField(
            model_name='location',
            name='closest_mile',
            field=models.ForeignKey(blank=True, limit_choices_to={'type': 'mile'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pct.HalfmileWaypoint'),
        ),
        migrations.AlterField(
            model_name='location',
            name='closest_poi',
            field=models.ForeignKey(blank=True, limit_choices_to={'type': 'poi'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pct.HalfmileWaypoint'),
        ),
        migrations.AlterField(
            model_name='post',
            name='closest_mile',
            field=models.ForeignKey(blank=True, limit_choices_to={'type': 'mile'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pct.HalfmileWaypoint'),
        ),
        migrations.AlterField(
            model_name='post',
            name='closest_poi',
            field=models.ForeignKey(blank=True, limit_choices_to={'type': 'poi'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pct.HalfmileWaypoint'),
        ),
    ]
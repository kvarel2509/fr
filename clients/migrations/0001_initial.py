# Generated by Django 4.2.1 on 2023-05-25 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255)),
                ('mobile_operator_code', models.CharField(max_length=255)),
                ('tag', models.CharField(blank=True, max_length=255)),
                ('time_zone', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'client',
                'indexes': [models.Index(fields=['mobile_operator_code', 'tag'], name='client_mobile__c95b5a_idx'), models.Index(fields=['mobile_operator_code'], name='client_mobile__5964a5_idx'), models.Index(fields=['tag'], name='client_tag_469cfa_idx')],
            },
        ),
    ]
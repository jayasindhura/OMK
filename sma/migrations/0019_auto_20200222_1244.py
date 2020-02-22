# Generated by Django 3.0.3 on 2020-02-22 18:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sma', '0018_auto_20200222_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentor_first_name', models.CharField(max_length=100)),
                ('mentor_middle_name', models.CharField(blank=True, max_length=100)),
                ('mentor_last_name', models.CharField(max_length=100)),
                ('mentor_email', models.EmailField(max_length=100)),
                ('mentor_address', models.CharField(max_length=200)),
                ('mentor_city', models.CharField(max_length=50)),
                ('mentor_state', models.CharField(max_length=50)),
                ('mentor_zip', models.CharField(max_length=10)),
                ('mentor_phone', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='sma.Grade'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='sma.School'),
        ),
        migrations.CreateModel(
            name='Student_Group_Mentor_Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('grade', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='sma.Grade')),
                ('mentor', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='sma.Mentor')),
                ('school', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='sma.School')),
            ],
        ),
        migrations.CreateModel(
            name='Session_Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_location', models.CharField(max_length=50)),
                ('session_start_date', models.DateTimeField(max_length=20)),
                ('session_end_date', models.DateTimeField(max_length=20)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sma.Student_Group_Mentor_Assignment')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sma.Mentor')),
            ],
        ),
    ]

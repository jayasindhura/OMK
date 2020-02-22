# Generated by Django 3.0.3 on 2020-02-22 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sma', '0012_auto_20200222_1045'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student_group_mentor_assignment',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='Session_Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_location', models.CharField(max_length=50)),
                ('session_date', models.DateTimeField(max_length=50)),
                ('session_start_date', models.DateTimeField(max_length=20)),
                ('session_end_date', models.DateTimeField(max_length=20)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sma.Student_Group_Mentor_Assignment')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sma.Mentor')),
            ],
        ),
    ]

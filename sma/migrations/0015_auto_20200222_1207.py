# Generated by Django 3.0.3 on 2020-02-22 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sma', '0014_remove_session_schedule_session_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session_schedule',
            name='group',
        ),
        migrations.RemoveField(
            model_name='session_schedule',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='student_group_mentor_assignment',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='student_group_mentor_assignment',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='student_group_mentor_assignment',
            name='school',
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grade_id', to='sma.Grade'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_id', to='sma.Grade'),
        ),
        migrations.DeleteModel(
            name='Mentor',
        ),
        migrations.DeleteModel(
            name='Session_Schedule',
        ),
        migrations.DeleteModel(
            name='Student_Group_Mentor_Assignment',
        ),
    ]
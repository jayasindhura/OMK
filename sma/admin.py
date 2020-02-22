from django.contrib import admin
from .models import School,Grade,Student,Mentor,Student_Group_Mentor_Assignment,Session_Schedule

# Register your models here.
class SchoolList(admin.ModelAdmin):
    list_display = ('school_name', 'school_email', 'school_phone')
    list_filter = ('school_name', 'school_email')
    search_fields = ('school_name',)
    ordering = ['school_name']

class GradeList(admin.ModelAdmin):
    list_display = ('school','grade_num')
    list_filter = ('school','grade_num')
    search_fields = ('school','grade_num')
    ordering = ['school']

class StudentList(admin.ModelAdmin):
    list_display = ('student_first_name','student_middle_name', 'student_last_name','school_id','grade_id')
    list_filter = ('student_first_name', 'student_last_name','school_id','school_id')
    search_fields = ('student_first_name', 'student_last_name','school_id','school_id')
    ordering = ['student_first_name']

class MentorList(admin.ModelAdmin):
    list_display = ('mentor_first_name','mentor_middle_name', 'mentor_last_name','mentor_email','mentor_phone')
    list_filter = ('mentor_first_name','mentor_middle_name', 'mentor_last_name','mentor_email','mentor_phone')
    search_fields = ('mentor_first_name','mentor_middle_name', 'mentor_last_name','mentor_email','mentor_phone')
    ordering = ['mentor_first_name']

class GroupMentorAssignmentList(admin.ModelAdmin):
    list_display = ('group_name','school','grade','mentor')
    list_filter = ('group_name','school','grade','mentor')
    search_fields = ('group_name','school','grade','mentor')
    ordering = ['group_name']

class SessionScheduleList(admin.ModelAdmin):
    list_display = ('session_location','mentor','group','session_start_date','session_start_date')
    list_filter = ('session_location','mentor','group','session_start_date','session_start_date')
    search_fields = ('session_location','mentor','group','session_start_date','session_start_date')
    ordering = ['session_location']

admin.site.register(School,SchoolList)
admin.site.register(Grade,GradeList)
admin.site.register(Student,StudentList)
admin.site.register(Mentor,MentorList)
admin.site.register(Student_Group_Mentor_Assignment,GroupMentorAssignmentList)
admin.site.register(Session_Schedule,SessionScheduleList)




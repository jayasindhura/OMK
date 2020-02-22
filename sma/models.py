from django.db import models
from django.utils import timezone

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=100)
    school_address = models.CharField(max_length=200)
    school_city = models.CharField(max_length=50)
    school_state = models.CharField(max_length=50)
    school_zip = models.CharField(max_length=10)
    school_email = models.EmailField(max_length=100)
    school_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.school_name)

class Grade(models.Model):
    grade_num = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE,default='', blank=True, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("grade_num", "school"),)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.grade_num)

class Student(models.Model):
    student_first_name = models.CharField(max_length=100)
    student_middle_name = models.CharField(max_length=100, blank=True)
    student_last_name = models.CharField(max_length=100)
    student_gender = models.CharField(max_length=100)
    student_dateofbirth = models.DateTimeField(max_length=50)
    student_email = models.EmailField(max_length=100)
    student_address = models.CharField(max_length=200)
    student_city = models.CharField(max_length=50)
    student_state = models.CharField(max_length=50)
    student_zip = models.CharField(max_length=10)
    student_phone = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE, default='', blank=True, null=True)
    #school = models.ForeignKey(Grade, on_delete=models.CASCADE,related_name='grades', default='', blank=True, null=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, default='', blank=True, null=True)
    #grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='gradess', default='', blank=True,null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.student_first_name)

class Mentor(models.Model):
    mentor_first_name = models.CharField(max_length=100)
    mentor_middle_name = models.CharField(max_length=100, blank=True)
    mentor_last_name = models.CharField(max_length=100)
    mentor_email = models.EmailField(max_length=100)
    mentor_address = models.CharField(max_length=200)
    mentor_city = models.CharField(max_length=50)
    mentor_state = models.CharField(max_length=50)
    mentor_zip = models.CharField(max_length=10)
    mentor_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.mentor_first_name)

class Student_Group_Mentor_Assignment(models.Model):
    group_name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE, default='', blank=True, null=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, default='', blank=True, null=True)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, default='', blank=True, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)
    #ForeignKeyConstraint(['id', 'school_id'], [Grade.id,Grade.school_id])

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.group_name)

class Session_Schedule(models.Model):
    session_location = models.CharField(max_length=50)
    session_start_date = models.DateTimeField(max_length=20)
    session_end_date = models.DateTimeField(max_length=20)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    group = models.ForeignKey(Student_Group_Mentor_Assignment,on_delete=models.CASCADE)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.session_location)

"""class Attendance(models.Model):
    attendance_student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendance_grade_id = models.ForeignKey(Grade, on_delete=models.CASCADE)
    attendace_mentor_id = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    attendance_session_ID = models.ForeignKey(Session_Schedule, on_delete=models.CASCADE)
    attendace_session_Date = models.ForeignKey(Session_Schedule,on_delete=models.CASCADE)
    attendance = models.CharField(max_length=100)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.attendance_ID)"""

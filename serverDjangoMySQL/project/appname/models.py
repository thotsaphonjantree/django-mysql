from django.db import models

class Major(models.Model):
    major_name = models.CharField(max_length=50)
 
    class Meta:
        verbose_name = "Major"
        verbose_name_plural = "Majors"
 
    def __unicode__(self):
        return self.name
 
class Student(models.Model):
    student_code = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    major = models.ForeignKey(Major, on_delete=models.DO_NOTHING)
 
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
 
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
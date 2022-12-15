from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 200)
    days = models.IntegerField()
    syllabus1 = models.TextField(null = True, blank = True)
    syllabus2 = models.TextField(null = True, blank = True)
    syllabus3 = models.TextField(null = True, blank = True)
    syllabus4 = models.TextField(null = True, blank = True)
    syllabus5 = models.TextField(null = True, blank = True)
    syllabus6 = models.TextField(null = True, blank = True)
    syllabus7 = models.TextField(null = True, blank = True)
    syllabus8 = models.TextField(null = True, blank = True)
    syllabus9 = models.TextField(null = True, blank = True)
    syllabus10 = models.TextField(null = True, blank = True)
    syllabus11 = models.TextField(null = True, blank = True)
    syllabus12 = models.TextField(null = True, blank = True)
    syllabus13 = models.TextField(null = True, blank = True)
    syllabus14 = models.TextField(null = True, blank = True)
    syllabus15 = models.TextField(null = True, blank = True)
    syllabus16 = models.TextField(null = True, blank = True)
    syllabus17 = models.TextField(null = True, blank = True)
    syllabus18 = models.TextField(null = True, blank = True)
    syllabus19 = models.TextField(null = True, blank = True)
    syllabus20 = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return self.name
    
from django.db import models
import json
# Create your models here.

class QuestionType(models.Model):
    choice = (
        ('checkbox', 'Multi choice'),
        ('date', "Date"),
        ('email', "Email"),
        ('file', "File"),
        ('number', "Number"),
        ('radio', "Radio select"),
        ('text', 'Single line answer'),
        ('time', "Time"),
        ('url', "Url"),
        ('week', "Week"),
        ('select', "Dropdown"),
        ('textarea', "Text")
    )
    title = models.CharField(max_length=50,null=True,blank=True)
    type = models.CharField(choices=choice,max_length=10,null=True,blank=True)
    options = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
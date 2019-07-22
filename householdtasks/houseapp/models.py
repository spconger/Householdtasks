from django.db import models, utils
import datetime


# Create your models here.
class Priority (models.Model):
    priorityname=models.CharField(max_length=50)

    def __str__(self):
        return self.priorityname
    
    class Meta:
        db_table='priority'
        verbose_name_plural='priorities'

class Status(models.Model):
    statusname=models.CharField(max_length=50)

    def __str__(self):
        return self.statusname
    
    class Meta:
        db_table='status'
        verbose_name_plural='statuses'

class Category(models.Model):
    categoryname=models.CharField(max_length=50)

    def __str__(self):
        return self.categoryname
    
    class Meta:
        db_table='category'
        verbose_name_plural='categories'

class Task(models.Model):
    taskname=models.CharField(max_length=255)
    taskdescription=models.TextField(null=True, blank=True)
    priority=models.ForeignKey(Priority, on_delete=models.DO_NOTHING)
    status=models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    category=models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    dateentered=models.DateField(default =datetime.date.today)

    def __str__(self):
        return self.taskname
    
    class Meta:
        db_table='task'
        verbose_name_plural='tasks'
        
class TaskLog(models.Model):
    logtitle=models.CharField(max_length=255)
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    logdate=models.DateField(default=datetime.date.today)
    logEntry=models.TextField()
    cost=models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    def __str__(self):
        return self.logtitle

    class Meta:
        db_table='tasklog'
        verbose_name_plural='tasklogs'




from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=10,primary_key=True)
    def __str__(self):
        return self.topic_name
class webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    URL=models.URLField()
    
    def __str__(self):
        return self.name
class access(models.Model):
    topic_name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    date=models.DateField()
    def __str__(self):
        return self.date
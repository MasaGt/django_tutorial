from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    content = models.CharField(max_length=100)
    pub_date = models.DateTimeField('publication date')

    def __str__(self):
        return self.content

    def was_published(self):
        return self.pub_date <= timezone.now()


class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    vote_num = models.IntegerField(default=0)

    def __str__(self):
        return self.question.content + '->' + self.text

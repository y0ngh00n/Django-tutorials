from django.db import models

# Create your models here.

class Candidate(models.Model): #to work as django model
    name = models.CharField(max_length = 20)
    introduction = models.TextField()
    area = models.CharField(max_length = 20)
    party_number = models.IntegerField(default = 0)

    def __str__(self):
        return self.name


class Poll(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    area = models.CharField(max_length = 20)


class Choice(models.Model):
    poll = models.ForeignKey(Poll) # foreign key로 Poll 받아옴
    candidate = models.ForeignKey(Candidate)
    votes = models.IntegerField(default = 0)

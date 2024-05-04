from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Verb(models.Model):
    francais = models.CharField(max_length=50)
    anglais = models.CharField(max_length=50)

    def __str__(self):
        return self.francais + " / " + self.anglais

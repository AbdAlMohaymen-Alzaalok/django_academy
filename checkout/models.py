from django.db import models
from courses.models import Course
from django.conf.global_settings import AUTH_USER_MODEL

class Status(models.IntegerChoices):
    pending=0,'Pending'
    completed=1,'Completed'

class Payment(models.Model):
    amount=models.FloatField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    status=models.IntegerField(choices=Status.choices,default=Status.pending)
    user=models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'course'],
                name='unique_user_course'
            )
        ]


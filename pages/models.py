from django.db import models

class Feedback(models.Model):
    title = models.CharField(max_length=120)
    email = models.EmailField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title


class ContactDetail(models.Model):
    mobile = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    opening_hour_mon = models.CharField(max_length=20)
    opening_hour_tue = models.CharField(max_length=20)
    opening_hour_wed = models.CharField(max_length=20)
    opening_hour_thu = models.CharField(max_length=20)
    opening_hour_fri = models.CharField(max_length=20)
    opening_hour_sat = models.CharField(max_length=20)
    opening_hour_sun = models.CharField(max_length=20)
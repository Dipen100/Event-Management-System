from django.db import models

class EventCategory(models.Model):
    CONFERENCE = 'C'
    WEDDING = 'W'
    PARTY = 'P'
    RECEPTION = 'R'
    CONCERT = 'CO'
    OTHER = 'O'
    
    CATEGORY_CHOICES = [
        (CONFERENCE, 'Conference'),
        (WEDDING, 'Wedding'),
        (PARTY, 'Party'),
        (RECEPTION, 'Reception'),
        (CONCERT, 'Concert'),
        (OTHER, 'Other'),
    ]
    event_name = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.event_name

class Event(models.Model):  
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(EventCategory, related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Vendor(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)

    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    
    def __str__(self):
        return self.name
    
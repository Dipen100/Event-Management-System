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
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=30)
    phone = models.IntegerField()
    
    def __str__(self):
        return self.name

class Catering(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
class Equipments(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class EventLogistics(models.Model):
    BUS = 'B'
    CAR = 'C'
    VAN = 'V'
    SCORPIO = 'S'
    
    TRANSPORTATION_CHOICES = [
        ('BUS', BUS),
        ('CAR', CAR),
        ('VAN', VAN),
        ('SCORPIO', SCORPIO),
    ]
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    catering = models.ForeignKey(Catering, on_delete=models.CASCADE)
    equipments = models.ManyToManyField(Equipments)
    transportation = models.CharField(max_length=9, choices=TRANSPORTATION_CHOICES)
    
    def __str__(self):
        return self.event.title
    
    
    
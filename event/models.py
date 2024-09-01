from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

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
    
class Attendee(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    event = models.ForeignKey(Event, related_name='attendees', on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Registered', 'Registered'), ('Confirmed', 'Confirmed')])

    def __str__(self):
        return f'{self.user.username} - {self.event.title}'

class Communication(models.Model):
    attendee = models.ForeignKey(Attendee, related_name='communications', on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.attendee.user.username} - {self.sent_at}'

class Ticket(models.Model):
    attendee = models.ForeignKey(Attendee, related_name='tickets', on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=20, choices=[('VIP', 'VIP'), ('General', 'General')])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ticket_type} - {self.event.title} - {self.attendee.user.username}'

class Reservation(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

class Invoice(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='invoices', on_delete=models.CASCADE)
    # amount = models.DecimalField(max_digits=10, decimal_places=2)
    issued_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Invoice {self.id} - {self.ticket.event.title} - {self.is_paid}'

class Receipt(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_reference = models.CharField(max_length=100)
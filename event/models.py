from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class EventCategory(models.Model):
    CONFERENCE = 'Conference'
    WEDDING = 'Wedding'
    PARTY = 'Party'
    RECEPTION = 'Reception'
    CONCERT = 'Concert'
    OTHER = 'Other'
    
    CATEGORY_CHOICES = [
        (CONFERENCE, 'CONFERENCE'),
        (WEDDING, 'WEDDING'),
        (PARTY, 'PARTY'),
        (RECEPTION, 'RECEPTION'),
        (CONCERT, 'CONCERT'),
        (OTHER, 'OTHER'),
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
    price = models.DecimalField(max_digits=10000000, decimal_places=2)
        
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
    BUS = 'Bus'
    CAR = 'Car'
    VAN = 'Van'
    SCORPIO = 'Scorpio'
    
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

    def message(self) -> str:
        return 'Thankyou for registering.'
    
    def __str__(self):
        return f'{self.name} - {self.event.title}'
    
class Communication(models.Model):
    attendee = models.ForeignKey(Attendee, related_name='communications', on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    
    def client_response(self) -> str:
        return 'Thankyou for your time we are looking forward to it.'

    def __str__(self):
        return f'{self.attendee.user.username} - {self.sent_at}'

class Reservation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)

    def message(self) -> str:
        return 'You have successfully reserved your event.'
    
class Ticket(models.Model):
    ESEWA = 'Esewa'
    KHALTI = 'Khalti'
    IMEPAY = 'ImePay'
    OTHER = 'O'
    
    PAYMENT_MODE_CHOICES = [
        ('ESEWA', ESEWA),
        ('KHALTI', KHALTI),
        ('IMEPAY', IMEPAY),
        ('OTHER', OTHER),
    ]
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE,  null=True, blank=True)
    event = models.ForeignKey(Event, related_name='tickets', on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=20, choices=[('VIP', 'VIP'), ('General', 'General')])
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODE_CHOICES, default=ESEWA)
    purchased_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def event_price(self):
        return self.event.price

    @property
    def vip_price_only(self):
        if self.ticket_type == 'VIP':
            return 500
        else:
            return 0
    
    @property
    def total_price(self):
        if self.ticket_type == 'VIP':
            return self.event_price + self.vip_price_only
        else:
            return self.event_price
        # return self.event_price + self.vip_price_only
    
    def __str__(self):
        return f'{self.ticket_type} - {self.event.title} - {self.attendee.user.username}'

class Invoice(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='invoices', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    issued_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Invoice {self.id} - {self.ticket.event.title} - {self.is_paid}'

class Receipt(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_reference = models.CharField(max_length=100)
    
class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField() 
    feedback = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f'Review by {self.attendee.name} for {self.event.title}'
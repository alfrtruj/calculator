from django.db import models
from django.utils import timezone
from calc import calculator
# Create your models here.

PAY = [('yearly', 'Yearly'), ('monthly', 'Monthly'), ('only_piqlfilm', 'Only piqlFilm')]
TYPE = [('digital', 'Digital'), ('visual', 'Visual'), ('hybrid', 'Hybrid')]
LAYOUT = [('1', '1 page'), ('2', '2 pages'), ('3', '3 pages'), ('4', '4 page'), ('6', '6 pages'), ('10', '10 pages')]
CONTRIBUTION = [('public', 'Public'), ('private', 'Private')]
STORAGE = [('5', '5 years'), ('10', '10 years'), ('25', '25 years')]
DECISION = [('yes', 'Yes'), ('no', 'No')]
SERVICE = [('platinum', 'Platinum'), ('gold', 'Gold')]

class Input(models.Model):
    partner_name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=40, verbose_name='Client')
    offline_data = models.IntegerField(verbose_name='Offline data (GB)', default=0)
    online_data = models.IntegerField(verbose_name='Online data (GB)', default=0)
    type = models.CharField(default='digital', max_length=40, choices=TYPE, verbose_name='Type of offline preservation', blank=True )
    pages = models.IntegerField(default=0, blank=True, verbose_name='Offline visual (pages)')
    layout = models.CharField(default='1', blank=True, max_length=40, choices=LAYOUT, verbose_name='Pages per frame')
    payment = models.CharField(max_length=40, choices=PAY, verbose_name='Online payment')
    comment = models.TextField(verbose_name='Comments')
    created_date = models.DateTimeField(default=timezone.now)
    awa = models.CharField(default='no', blank=True, max_length=40, choices=DECISION, verbose_name='Storage in Arctic World Archive')
    awa_contribution = models.CharField(default='public', max_length=40, choices=CONTRIBUTION, verbose_name='Entity')
    awa_storage = models.CharField(default='5', max_length=40, choices=STORAGE, verbose_name='AWA Storage')
    piqlreader = models.CharField(default='no', blank=True, max_length=40, choices=DECISION, verbose_name='piqlReader')
    quantity = models.IntegerField(default='1', blank=True, verbose_name='Quantity of piqlReaders')
    service = models.CharField(default='gold', blank=True, max_length=40, choices=SERVICE, verbose_name='Service agreement')
    consultancy = models.CharField(default='no', blank=True, max_length=40, choices=DECISION, verbose_name='Professional services')
    days = models.IntegerField(default='1', blank=True, verbose_name='How many days?')

    def __str__(self):
        return self.customer_name





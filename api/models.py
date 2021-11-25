from django.db import models

# Create your models here.

#################################################################
################          BOT MODEL             #################
#################################################################
class Bot(models.Model):
    bot_no = models.IntegerField(unique=True)
    name = models.CharField(max_length = 50, unique=True)
    color = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to = 'flunky_images', blank = True)
    status = models.BooleanField(default=True, help_text="bot working(active or inactive)")   # active or inactive
    avialable = models.BooleanField(default=True, help_text="available or not avialabe for delivery")  # avialabe to serve or not avialable
    ip = models.CharField(max_length=15)
    port = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    battery = models.DecimalField(max_digits=5, decimal_places=2, default = 0)

    class Meta:
        verbose_name = 'Bot'
        verbose_name_plural = 'Bots'
        ordering = ('-id',)

    def __str__(self):
        return self.color


#################################################################
################        TABLE MODELS            #################
#################################################################
class Table(models.Model):
    table_number = models.IntegerField(unique = True)   
    avialable = models.BooleanField(default = True)
    image = models.ImageField(upload_to = 'table_images', blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'
        ordering = ('-table_number',)

    def __str__(self):
        return str(self.table_number)


#################################################################
################     DELIVERY MODEL             #################
#################################################################
class Delivery(models.Model):
    food_type_choices = (
        ('solid','solid'),
        ('liquid', 'liquid')
    )
    speed_choices = (
        (90, 90),
        (120,120),
    )
    bot_no = models.IntegerField()
    bot_name = models.CharField(max_length=30)
    table_no = models.IntegerField(null = True)
    ip = models.CharField(max_length=20, null = True)
    port = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now = True)
    food_delivered = models.BooleanField(default = False)

    food_type = models.CharField(max_length=100, choices = food_type_choices, default = 'solid')
    speed_of_the_bot = models.IntegerField(choices = speed_choices, default = 90)

    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural  = 'Deliveries'
    
    def __str__(self):
        return (str(self.id) + self.bot_name)


###############   FINAL DELIVERY   #####################
class FinalDelivery(models.Model):
    bot_no = models.IntegerField()
    bot_name = models.CharField(max_length = 100)
    table_no = models.IntegerField()
    ip = models.CharField(max_length = 30)
    port = models.IntegerField()
    food_type = models.CharField(max_length=30, null = True, blank = True)
    speed_of_the_bot = models.IntegerField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    food_delivered = models.BooleanField(default = True)
    time = models.DecimalField(max_digits=50, decimal_places=6, default = 0)

    class Meta:
        verbose_name = 'Final Delivery'
        verbose_name_plural = 'Final Deliveries'

    def __str__(self):
        return (str(self.bot_no) +'  '+self.bot_name)

    

from django.db import models
from django.utils.translation import gettext_lazy as _

class Squirrel(models.Model):
    Latitude=models.DecimalField(
            max_digits=15,
            decimal_places=13)
    Longitude=models.DecimalField(
            max_digits=15,
            decimal_places=13)
    Unique_Squirrel_ID = models.CharField(
            primary_key=True,
            max_length=250)

    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = [
            (AM, 'AM'),
            (PM, 'PM'),
        ]

    Shift = models.CharField(
        max_length=250,
        help_text=_('Shift of a squirrel'),
        choices = SHIFT_CHOICES,
        default=AM,
        )

    Date = models.DateField()

    ADULT = 'Adult'
    JUV = 'Juvenile'
    UNKNOWN = 'Unknown'

    AGE_CHOICES = [
        (ADULT, 'Adult'),
        (JUV, 'Juvenile'),
        (UNKNOWN, 'Unknown'),
        ]
    Age = models.CharField(
        max_length=250,
        help_text=_('Age of the squirrel'),
        choices = AGE_CHOICES,
        default = ADULT,
        )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    COLOR_CHOICES = [
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
        (UNKNOWN, 'Unknown'),
        ]
    Primary_Fur_Color = models.CharField(
        max_length=10,
        choices = COLOR_CHOICES,
        default = GRAY,
    )

    ABOVE = 'Above Ground'
    PLANE = 'Ground Plane'

    LOCATION_CHOICES = [
        (ABOVE, 'Above Ground'),
        (PLANE, 'Ground Plane'),
        (UNKNOWN, 'Unknown'),
        ]

    Location = models.CharField(
        max_length = 250,
        choices = LOCATION_CHOICES,
        default = ABOVE
    )

    Specific_Location = models.CharField(
        max_length=250,
        blank = True,
    )

    Running = models.BooleanField(
        help_text=_('Whether or not it was running'),
    )
    Chasing = models.BooleanField(
        help_text=_('Whether or not it was chasing'),
    )
    Climbing = models.BooleanField(
        help_text=_('Whether or not it was climbing'),
    )
    Eating = models.BooleanField(
        help_text=_('Whether or not it was eating'),
    )
    Foraging = models.BooleanField(
        help_text=_('Whether or not it was foraging'),
    )
    Other_Activities = models.CharField(
            max_length=250,
            blank = True,
        )
    Kuks = models.BooleanField(
        help_text=_('The kuk is a sharp bark of alarm'),
    )
    Quaas = models.BooleanField(
        help_text = _('The quaas is a longer version of the kuk'),
    )
    Moans = models.BooleanField(
        help_text = _('The moan sounds like a whistle'),
    )
    Tail_flags = models.BooleanField(
        help_text = _('Is the squirrel waving its tail?'),
    )
    Tail_twitches = models.BooleanField(
        help_text = _('A twitch looks like a wave running through the tail'),
    )
    Approaches = models.BooleanField(
        help_text = _('Is the squirrel willing to approach?'),
    )
    Indifferent = models.BooleanField(
        help_text = _('Is the squirrel indifferent?'),
    )
    Runs_from = models.BooleanField()
   

class Test(models.Model):
    Latitude=models.DecimalField(
            max_digits=15,
            decimal_places=13)
    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = [
            (AM, 'AM'),
            (PM, 'PM'),
        ]

    Shift = models.CharField(
        max_length=250,
        help_text=_('Shift of a squirrel'),
        choices = SHIFT_CHOICES,
        default=AM,
        )

    Date = models.DateField()

    Moans = models.BooleanField(
        help_text = _('The moan sounds like a whistle'),
    )

    Other_Activities = models.CharField(
            max_length=250,
            blank = True,
        )   

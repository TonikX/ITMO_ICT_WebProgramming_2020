from django.db import models

# Create your models here.
class Companies(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.name)


class Gates(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.name)


class Flights(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    gate = models.ForeignKey(Gates, on_delete=models.CASCADE)

    def __str__(self):
        return "Company: {} | Gate: {}".format(self.company, self.gate)


class FlightActivities(models.Model):
    ACTIVITY = [
        ('0', 'arrival'),
        ('1', 'departure')
    ]

    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    activity = models.CharField(choices=ACTIVITY, default='0', max_length=1)
    time = models.DateField()

    def __str__(self):
	    return "{} | Arrival/departure: {} | Date {}".format(self.flight, self.get_activity_display(), self.time)


class FlightComments(models.Model):
	flight = models.ForeignKey(FlightActivities, on_delete=models.CASCADE)

	COMMENT_TYPE = [
		('0', 'Gate changing'),
		('1', 'Lateness'),
		('2', 'Other')
	]

	com_type = models.CharField(choices=COMMENT_TYPE, default='0', max_length=1)
	com_text = models.CharField(max_length=1024)
	author = models.EmailField(max_length=254)

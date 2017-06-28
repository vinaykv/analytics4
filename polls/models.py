from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
class DTC(models.Model):
	Dtc_code = models.IntegerField()
	Dtc_description = models.TextField()
	Dtc_timestamp = models.DateTimeField('date captured')
	Mil_status = models.CharField(max_length=4)
	test_passed = models.CharField(max_length=4)
	Vehicle_tag = models.IntegerField()
	def __str__(self):
		return self.Dtc_description
	def date_published_recently(self):
		return self.Dtc_timestamp >= timezone.now() - datetime.timedelta(days=1)
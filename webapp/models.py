from django.db import models

# Create your models here.


class Drill(models.Model):
	diameter = models.CharField(max_length=20)
	grade = models.CharField(max_length=20)
	coating = models.CharField(max_length=20)

	def __str__(self):
		return f"G{self.grade}{self.coating} D{self.diameter}"


class Component(models.Model):
	thread = models.CharField(max_length=20)
	casting = models.CharField(max_length=20)
	center = models.CharField(max_length=20)
	peripheral = models.CharField(max_length=20)
	intermediate = models.CharField(max_length=20)
	pad = models.CharField(max_length=20)
	drill = models.ForeignKey(Drill, on_delete=models.CASCADE, default=1)

	def __str__(self):
		return f"{self.thread} {self.casting} {self.center}"


class Center(models.Model):
	code = models.CharField(max_length=255)
	variant = models.CharField(max_length=255)

	def __str__(self):
		return self.code


class CenterQuantity(models.Model):
	center = models.ForeignKey(Center, on_delete=models.CASCADE)
	quantity = models.IntegerField()

	def __str__(self):
		return f"{self.quantity} of {self.center}"


	

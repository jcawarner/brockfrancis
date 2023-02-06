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

#### Brock's Model ####

INSERT_GRADES = [
	("T22", "T22"),
	("NTA", "NTA"),
	("FK20M", "FK20M"),
	]

class BrockCenterInsert(models.Model):
	item_code = models.CharField(max_length=31, unique=True)
	models.SlugField(blank=True, null=True)
	grade = models.CharField(max_length=5, choices=INSERT_GRADES, blank=True, Null=True)
	quantity_in_stock = models.IntegerField()

	class Meta:
		ordering = ["item_code"]

	def __str__(self):
		return str(self.item_code)

	def save(self, *args, **kwargs):
		self.item_code = self.item_code.upper()
		if self.slug is None:
			self.slug = slugify(self.item_code)
		if self.grade is None:
			split_item_code = self.item_code.split("-")
			for i in INSERT_GRADES:
				if i[0] == split_item_code[-1]:
					self.grade = i[0]
		super().save(*args, **kwargs)

	

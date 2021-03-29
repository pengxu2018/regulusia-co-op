from django.db import models

# Create your models here.


"""
class Order(models.Model):

	STATUS = (
         ('Pending', 'Pending'), 
         ('Out for Delivery', 'Out for Delivery'), 
         ('Delivered', 'Delivered'), 
		)
	customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

"""
class Engineer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	notes = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name


class Supplier(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)
	notes = models.TextField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	notes = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name



class Product(models.Model):

	CARRIER = (
         ('UPS', 'UPS'), 
         ('USPS', 'USPS'),
         ('Fedex', 'Fedex'),
         ('DHL','DHL'),
         ('Amazon', 'Amazon'),
         ('Others','Others'),
		)

	STATUS = (
         ('Level 1: Factory Config', 'Level 1: Factory Config'),  
         ('Level 2: Work in Progress', 'Level 2: Work in Progress'),
         ('Level 3: Prepare for Shipping', 'Level 3: Prepare for Shipping'),
         ('LEvel 4: Ready to Ship','LEvel 4: Ready to Ship'),
		)

	LOCATION = (
         ('Unpacking Room', 'Unpacking Room'), 
         ('Receiving Room', 'Receiving Room'),
         ('Small Storage Room A', 'Small Storage Room A'),
         ('Small Storage Room B', 'Small Storage Room B'),
         ('Storage Room','Storage Room'),
         ('Packing Room','Packing Room'),
         ('Shipping Room','Shipping Room'),
		)



	name = models.CharField(max_length=200, null=True)
	serial_number = models.CharField(max_length=200, null=True, blank=True)
	product_number = models.CharField(max_length=200, null=True, blank=True)
	SKU = models.CharField(max_length=200, null=True)
	brand_and_model = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
	inbound_carrier = models.CharField(max_length=200, null=True, choices=CARRIER)
	inbound_tracking_number = models.CharField(max_length=200, null=True)
	date_received = models.DateField(null=True)
	location = models.CharField(max_length=200, null=True, choices=LOCATION, blank=True)
	customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, blank=True)
	outbound_carrier = models.CharField(max_length=200, null=True, choices=CARRIER, blank=True)
	outbound_tracking_number = models.CharField(max_length=200, null=True, blank=True)
	handled_by = models.ForeignKey(Engineer, null=True, on_delete=models.SET_NULL, blank=True)
	date_shipped = models.DateField(null=True, blank=True)
	notes = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.SKU










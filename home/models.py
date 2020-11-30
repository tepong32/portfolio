from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
	"""
	docstring for Profile

	Profile is intended for the owner of the site showing the portfolio.
	This model needs to be heavily extended if the project website is 
	going to be one with multiple users and user registrations.

	"""
	user = models.OneToOneField(User, on_delete='CASCADE')
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	quote = models.CharField(max_length=200, blank=True)

	def profile_image_directory_path(instance, filename):
		# file will be uploaded to MEDIA_ROOT/DP_<username>/<filename> ---check settings.py. MEDIA_ROOT=media
		return 'users/{}/DP/{}'.format(instance.user.username, filename)

	profile_image = models.ImageField(default='default_m.png', upload_to=profile_image_directory_path)

	def profile_cover_directory_path(instance, filename):
		# file will be uploaded to MEDIA_ROOT/DP_<username>/<filename> ---check settings.py. MEDIA_ROOT=media
		return 'users/{}/cover/{}'.format(instance.user.username, filename)

	profile_cover = models.ImageField(default='/static/images/cover.png', upload_to=profile_cover_directory_path)
	

	# items on the homepage #
	intro = models.TextField(blank=True, verbose_name="Intro", )
	storyline = models.TextField(blank=True, verbose_name="Storyline", )
	# contact me part / socmed #
	fb = models.CharField(max_length=100, blank=True, verbose_name="Facebook", unique=True)
	twitter = models.CharField(max_length=100, blank=True, verbose_name="Twitter", unique=True)
	google = models.CharField(max_length=100, blank=True, verbose_name="Google", unique=True)
	insta = models.CharField(max_length=100, blank=True, verbose_name="Instagram", unique=True)
	github = models.CharField(max_length=100, blank=True, verbose_name="Github", unique=True)
	linkedin = models.CharField(max_length=100, blank=True, verbose_name="LinkedIn", unique=True)

	def __str__(self):
		return str(self.first_name + ' ' + self.last_name)

	def save(self, *args, **kwargs):		# for resizing/downsizing images
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.profile_image.path)	# open the image of the current instance
		if img.height > 600 or img.width > 600:	# for sizing-down the images to conserve memory in the server
			output_size = (600, 600)
			img.thumbnail(output_size)
			img.save(self.profile_image.path)
		

class Offer(models.Model):
	"""
	docstring for Offer

	SampleWork is intended to show-off just the different front-end approach
	for the website.
	Navbars and Sidebars, Product/Image Sliders, etc..
	This will have default attributes especially for an e-commerce website.
	Products, Categories, Prices, Descriptions

	"""

	# so that Profile won't need to be called separately per Offer instance:
	profile = models.ForeignKey(Profile, on_delete='CASCADE')

	Product = "Product"
	Service = "Service"
	offer_choice = [
		(Product, "Product"),
		(Service, "Service")
	]

	offer = models.CharField(
		max_length=10,
		choices=offer_choice,
		default=Product,
	)

	if offer == "Product":
		product_name = models.CharField(max_length=100, blank=False)
		product_price = models.IntegerField(max_length=10, blank=False)
		product_desc = models.TextField()

		def product_directory_path(instance, filename):
			# file will be uploaded to MEDIA_ROOT/DP_<username>/<filename> ---check settings.py. MEDIA_ROOT=media
			return 'users/{}/products/{}'.format(instance.user.username, filename)

	if offer == "Service":
		service_name = models.CharField(max_length=100, blank=False)
		service_price = models.FloatField(max_length=10, blank=False)
		sevice_desc = models.TextField()

		def product_directory_path(instance, filename):
			# file will be uploaded to MEDIA_ROOT/DP_<username>/<filename> ---check settings.py. MEDIA_ROOT=media
			return 'users/{}/products/{}'.format(instance.user.username, filename)

		
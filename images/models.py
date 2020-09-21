from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse



class Image(models.Model):


	user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='images')
	photo = models.ImageField(upload_to='images')
	title = models.CharField(max_length=60)
	slug = models.SlugField(blank=True)
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	users_like = models.ManyToManyField(User , related_name='images_liked' ,blank=True)
	total_likes = models.PositiveIntegerField(db_index=True,
											  default=0)


	def save(self ,*args , **kwargs):

		self.slug = slugify(self.title)
		return super(Image,self).save()

	def __str__(self):

		return self.title

	class Meta:

		ordering = ['-created']


	def get_absolute_url(self):

		return reverse('image_detail' , args=[self.slug , self.id])
		



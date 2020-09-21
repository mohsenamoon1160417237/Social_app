from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

	AGE = [(int(i),str(i)) for i in range(12,91)]


	user = models.OneToOneField(User , related_name='profile' , on_delete=models.CASCADE)
	image = models.ImageField(upload_to="profiles" , blank=True , null=True)
	age  = models.IntegerField(choices=AGE , default=18)
	
	def __str__(self):

		return self.user.username



class Contact(models.Model):

	user_from = models.ForeignKey('auth.User' , related_name='rel_from_set' , on_delete=models.CASCADE , null=True)
	user_to = models.ForeignKey('auth.User' , related_name='rel_to_set' , on_delete=models.CASCADE , null=True)
	created = models.DateTimeField(auto_now_add=True)


	class Meta:

		ordering = ['-created']

	def __str__(self):

		return '{} follows {}'.format(self.user_from , self.user_to)





User.add_to_class('following' , models.ManyToManyField('self',
													   through=Contact,
													   related_name='followers',
													   symmetrical=False))


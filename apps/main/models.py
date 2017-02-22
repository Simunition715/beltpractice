from __future__ import unicode_literals

from django.db import models
import bcrypt

class UserManager(models.Manager):
	def validate_user(self, post):
		isValid = True
		if len(post.get('first_name')) ==0:
			isValid = False
		if len(post.get('last_name')) ==0:
			isValid = False	
		if len(post.get('email')) ==0:
			isValid = False
		if len(post.get('password')) ==0:
			isValid = False
		if post.get('password') != post.get('confirm_password'):
			isValid = False
		return isValid		
	def sessions(self,post):
		user = self.filter(email=post.get('email')).first()		
		if user and bcrypt.hashpw(post.get('password').encode(),user.password.encode()) == user.password:
			return(True, user)
		return(False)	


# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	password = models.CharField(max_length=60)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
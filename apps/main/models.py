from __future__ import unicode_literals
import bcrypt
from django.db import models


class UserManager(models.Manager):
	def login(self,post):
		user = self.filter(Username=post.get('username')).first()
		if user and bcrypt.hashpw(post.get('password').encode(), user.password.encode()) == user.password:
			return(True,user)
		return(False,'not')	

class User(models.Model):
	name = models.CharField(max_length=255)
	Username= models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	hired = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class List(models.Model):
	item = models.CharField(max_length=255)
	user = models.ForeignKey(User, related_name="Items")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
	product =models.ForeignKey(List, related_name="Products")
	person = models.ForeignKey(User,related_name="Users")
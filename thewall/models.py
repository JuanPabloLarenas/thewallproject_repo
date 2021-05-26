from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postDATA):
        errors = {}
        if len(postDATA['fname']) < 2:
            errors['fname'] = "First Name should be at least 2 characters long"
        if len(postDATA['lname']) < 2:
            errors['lname'] = "Last Name should be at least 2 characters long"
        if postDATA['email'] == True:
            errors['email'] = "Email does not exist"
        if postDATA['cpassword'] != postDATA['password']:
            errors['passwordc'] = "Password confirmation is invalid"
        return errors

class User(models.Model):
    first_name = models.TextField(max_length=45)
    last_name = models.TextField(max_length=45)
    email = models.TextField(max_length=255)
    password = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Messages(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Messages, related_name="comments", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
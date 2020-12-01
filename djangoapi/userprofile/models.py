from django.db import models

# Create your models here.
class UserProfileQuerySet(models.QuerySet):
    def get_user(self, id):
        try:
            return list(self.filter(pk=id))
        except Exception as e:
            return {}

class UserProfile(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=60)
    token = models.CharField(max_length=255, default="", null=True, blank=True)
    coins = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = 'User Profile'
        db_table ="userprofiles" # node.js pluralized the table
    
    objects = UserProfileQuerySet.as_manager()

    def __str__(self):
        return f"Object of {id}"
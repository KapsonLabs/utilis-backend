from django.db import models

class Members(models.Model):
    """
    Members models
    """
    first_name              =   models.CharField(max_length=25)
    last_name               =   models.CharField(max_length=25)
    email_address           =   models.CharField(max_length=64, unique=True)
    wallet_address          =   models.CharField(max_length=64)
    country_of_origin       =   models.CharField(max_length=25)
    id_number               =   models.CharField(max_length=64)
    date_added              =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

#This model is designed for Receiver app.
#This is not related to Social Book Profile.

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .utils import generate_account_number


class ProfileForReceiver(models.Model):
    """
    Class for the owner of the invoice
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=26, blank=True, help_text="Bank Account Number")
    company_name = models.CharField(max_length=220)
    company_info = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    #add later
    #avata
    #company logo

    def __str__(self):
        return f"Profile of the user: {self.user.username}"

    #generate bank account numbner automatically with 26 digits.
    def save(self, *args, **kwargs):
        if self.account_number == "":
            self.account_number = generate_account_number()
        return super().save(*args, **kwargs)

    #Admin level Validation Check:
    # def clean(self):
    #     if len(self.account_number) != 26:
    #         raise ValidationError("Bank account number must be 26 characters long")


from django.db import models
from config.models import Base


# Create your models here.
class Lead(Base):
    PRODUCT_CHOICE = [
        ("BookKeeper", "BookKeeper"),
        ("Diparhta", "Dipartha"),
        ("MargBook", "margBook")
    ]

    SOURCE_CHOICE = [
        ("Instagram", "Instagram"),
        ("FaceBook", "FaceBook"),
        ("Other", "Other")
    ]

    name = models.CharField(max_length=150, null=False)
    organization_name = models.CharField(max_length=150, null=True)
    mobile_number = models.CharField(max_length=10, unique=True, null=False)
    phone_number = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=200,  null=False)
    product = models.CharField(max_length=50, choices=PRODUCT_CHOICE, null=False)
    email = models.EmailField(unique=True, null=False)
    source = models.CharField(max_length=50, choices=SOURCE_CHOICE, null=False)

    class Meta:
        db_table = "auto_lead"


class Company(Base):
    company_name = models.CharField(max_length=3)
    pan_number = models.CharField(max_length=9)
    mobile_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=225)
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    

    


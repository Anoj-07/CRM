from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Base(models.Model):
    reference_id = models.UUIDField(unique=True, null=False, default=uuid.uuid4)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+', null=False, db_column="created_by")
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+', null=True, db_column="updated_by")
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=False)
    is_delete = models.BooleanField(default=False)
    
    class Meta:
        abstract = True


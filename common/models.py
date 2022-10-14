import uuid
from django.contrib.auth import get_user_model
from django.db import models


def uuid_without_dash():
    return uuid.uuid4().hex


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid_without_dash)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    modified_by = models.ForeignKey(get_user_model(), related_name='+', on_delete=models.CASCADE, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, editable=False)

    def __str__(self):
        if hasattr(self, 'name'):
            return self.name

    class Meta:
        abstract = True
        ordering = ['-created']

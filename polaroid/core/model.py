from django.db import models

class TimestampedModel(models.Model):
    # "created_at" timestamp representing when this object was created.
    # "updated_at" timestamp representing when object last updated.

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        ordering = ['-created_at', '-updated_at']

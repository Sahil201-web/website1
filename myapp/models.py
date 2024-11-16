# models.py
from django.db import models
from django.db.models import Max
from django.db import transaction

class ButtonClick(models.Model):
    BUTTON_CHOICES = [
        ('location', 'Location'),
        ('contact', 'Contact'),
    ]

    custom_id = models.PositiveIntegerField(editable=False, unique=True, default=0)  # New sequential ID field
    button_type = models.CharField(max_length=10, choices=BUTTON_CHOICES)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.button_type} clicked on {self.date_time}"

    def save(self, *args, **kwargs):
        if not self.custom_id:
            # Find the maximum custom_id and increment by 1
            max_custom_id = ButtonClick.objects.aggregate(Max('custom_id'))['custom_id__max'] or 0
            self.custom_id = max_custom_id + 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the record and update sequence
        with transaction.atomic():
            super().delete(*args, **kwargs)
            # Shift custom_id for records after the deleted one to avoid gaps
            remaining_entries = ButtonClick.objects.filter(custom_id__gt=self.custom_id)
            for entry in remaining_entries:
                entry.custom_id -= 1
                entry.save()

    class Meta:
        ordering = ['custom_id']  # Sort by custom_id for consistency

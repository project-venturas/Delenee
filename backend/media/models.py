from django.db import models
from products.models import Variant

# Create your models here.
class Media(models.Model):
    # Although the DBML specifies an enum for entity_type (with note "variant"),
    # here we assume Media is associated only with Variants.
    ENTITY_TYPE_CHOICES = (
        ('variant', 'Variant'),
    )
    entity_type = models.CharField(
        max_length=20,
        choices=ENTITY_TYPE_CHOICES,
        default='variant'
    )
    # We use db_column to ensure that in the DB, the foreign key is stored as "entity_id".
    variant = models.ForeignKey(
        Variant,
        on_delete=models.CASCADE,
        db_column='entity_id',
        related_name='media'
    )
    url = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Media for {self.variant.name}"

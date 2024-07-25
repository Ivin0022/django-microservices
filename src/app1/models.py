from django.db import models


class Event(models.Model):
    """Model definition for Event."""

    title = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Event."""

        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        """Unicode representation of Event."""
        return f'{self.title}'

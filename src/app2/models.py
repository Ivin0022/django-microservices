from django.db import models


class Question(models.Model):
    """Model definition for Question."""
    text = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        """Unicode representation of Question."""
        return f"{self.text}"

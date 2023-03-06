from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


class Note(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = RichTextField()
    date_posted = models.DateTimeField(default = timezone.now )


    def __str__(self) -> str:
        return f' {self.user} note : {self.title} '
    
    class Meta:
        ordering = ['-date_posted']

    def get_absolute_url(self):
        return reverse("detailView", args=[self.id])
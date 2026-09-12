import uuid
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
        ('organization', 'Organization'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='organization')
    thumbnail = models.CharField(max_length=255, blank=True, null=True, help_text="Nama file gambar di static/img/, contoh: mentor.svg")
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def is_ongoing(self):
        return self.ended_at is None

class Education(models.Model):
    EDUCATION_CHOICES = [
        ('junior_high', 'Junior High School'),
        ('senior_high', 'Senior High School'),
        ('university', 'Undergraduate Student'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    level = models.CharField(max_length=20, choices=EDUCATION_CHOICES, default='university')
    logo = models.CharField(max_length=255, blank=True, null=True, help_text="Nama file logo di static/img/, contoh: ui-logo.svg")
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.institution

    @property
    def is_ongoing(self):
        return self.ended_at is None
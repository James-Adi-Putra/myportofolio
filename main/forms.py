from django.forms import ModelForm, TextInput, Textarea, URLInput
from main.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "skills_used",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "skills_used": "Keahlian yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "skills_used": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS, Product Management, Fotografi",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/James-star7/myproject",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/",
                }
            ),
        }
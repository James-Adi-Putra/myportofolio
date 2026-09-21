from django import forms
from django.forms import ModelForm, TextInput, Textarea, URLInput
from main.models import Experience, Education, Project

class ExperienceForm(ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Masukkan kode rahasia"}),
        label="Kode Rahasia",
        required=True,
    )

    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title": "Judul Pengalaman",
            "description": "Deskripsi",
            "category": "Kategori",
            "thumbnail": "Nama File Gambar",
            "ended_at": "Tanggal Selesai (kosongkan jika masih berlangsung)",
        }

        widgets = {
            "title": TextInput(
                attrs={"placeholder": "Mentor PSAF Fasilkom"}
            ),
            "description": Textarea(
                attrs={"placeholder": "Ceritakan pengalamanmu di sini", "rows": 3}
            ),
            "thumbnail": URLInput(
                attrs={"placeholder": "https://drive.google.com/thumbnail?id=...&sz=w400"}
            ),
            "ended_at": forms.DateInput(
                attrs={"type": "date"},
                format="%Y-%m-%d",
            ),
        }

class EducationForm(ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Masukkan kode rahasia"}),
        label="Kode Rahasia",
        required=True,
    )

    class Meta:
        model = Education
        fields = [
            "institution",
            "degree",
            "level",
            "description",
            "logo",
            "ended_at",
        ]

        labels = {
            "institution": "Nama Institusi",
            "degree": "Program/Jurusan",
            "level": "Jenjang Pendidikan",
            "description": "Deskripsi Singkat",
            "logo": "URL Logo Institusi",
            "ended_at": "Tanggal Selesai (kosongkan jika masih berlangsung)",
        }

        widgets = {
            "institution": TextInput(
                attrs={"placeholder": "Universitas Indonesia"}
            ),
            "degree": TextInput(
                attrs={"placeholder": "S1 Sistem Informasi"}
            ),
            "description": Textarea(
                attrs={"placeholder": "Ceritakan singkat tentang masa pendidikanmu di sini", "rows": 3}
            ),
            "logo": URLInput(
                attrs={"placeholder": "https://raw.githubusercontent.com/James-Adi-Putra/myportofolio/master/static/img/logo/nama-file.svg"}
            ),
            "ended_at": forms.DateInput(
                attrs={"type": "date"},
                format="%Y-%m-%d",
            ),
        }

class ProjectForm(ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Masukkan kode rahasia"}),
        label="Kode Rahasia",
        required=True,
    )

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
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w200",
                }
            ),
        }
from django.shortcuts import render
from main.models import Experience,Education

def show_main(request):
    context = {
        "name": "James Adi Putra",
        "brand_name": "James",
        "npm": "2506624644",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Hi, my name is James Adi Putra. You can call me James. I'm an Information "
            "Systems student at the University of Indonesia with a strong interest in "
            "exploring the field of cybersecurity. My goal is to develop the knowledge "
            "and skills needed to protect IT products and systems from potential threats."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "James",
        "brand_name": "James",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "James",
        "brand_name": "James",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)
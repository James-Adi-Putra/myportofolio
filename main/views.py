from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.conf import settings
from main.models import Experience, Education, Project
from main.forms import ProjectForm, EducationForm

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

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "James Adi Putra",
        "brand_name": "James",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        entered_password = form.cleaned_data.get("password")
        if entered_password != settings.PORTFOLIO_SECRET:
            messages.error(request, "Kode rahasia salah! Proyek tidak ditambahkan.")
        else:
            form.save()
            messages.success(request, "Proyek baru berhasil ditambahkan!")
            return redirect("main:show_projects")

    context = {
        "name": "James Adi Putra",
        "brand_name": "James",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        entered_password = request.POST.get("password", "")
        if entered_password != settings.PORTFOLIO_SECRET:
            messages.error(request, "Kode rahasia salah! Proyek tidak dihapus.")
            return redirect("main:show_projects")

        project.delete()
        messages.success(request, "Proyek berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        entered_password = form.cleaned_data.get("password")
        if entered_password != settings.PORTFOLIO_SECRET:
            messages.error(request, "Kode rahasia salah! Data tidak ditambahkan.")
        else:
            form.save()
            messages.success(request, "Riwayat pendidikan berhasil ditambahkan!")
            return redirect("main:show_education")

    context = {
        "name": "James Adi Putra",
        "brand_name": "James",
        "form": form,
    }
    return render(request, "education_form.html", context)

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        entered_password = request.POST.get("password", "")
        if entered_password != settings.PORTFOLIO_SECRET:
            messages.error(request, "Kode rahasia salah! Data tidak dihapus.")
            return redirect("main:show_education")

        education.delete()
        messages.success(request, "Riwayat pendidikan berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def update_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        entered_password = form.cleaned_data.get("password")
        if entered_password != settings.PORTFOLIO_SECRET:
            messages.error(request, "Kode rahasia salah! Data tidak diubah.")
        else:
            form.save()
            messages.success(request, "Riwayat pendidikan berhasil diperbarui!")
            return redirect("main:show_education")

    context = {
        "name": "James Adi Putra",
        "brand_name": "James",
        "form": form,
        "education": education,
    }
    return render(request, "education_form.html", context)
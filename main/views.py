import datetime
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied       
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.http import HttpResponse
from main.models import Experience, Education, Project
from main.forms import ExperienceForm, EducationForm, ProjectForm

# EDITOR
def is_editor(user):
    return user.groups.filter(name="Editor").exists()

def can_update(user):
    return user.is_superuser or is_editor(user)

#MAIN
def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
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
        "last_login": last_login,
    }
    return render(request, "index.html", context)

# REGISTER
def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")
    
    context = {
        "brand_name": "James",
        "form": form,
    }
    return render(request, "register.html", context)

# LOGIN
def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response
    
    context = {
        "brand_name": "James",
        "form": form,
    }
    return render(request, "login.html", context)

# LOGOUT
def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

#Experience
def get_experience_json(request):
    experience_list = Experience.objects.all()
    experience_json = serializers.serialize("json", experience_list)
    return HttpResponse(experience_json, content_type="application/json")

def show_experience(request):
    json_response = get_experience_json(request)

    experience_entries = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experience_list = [entry.object for entry in experience_entries]

    context = {
        "name": "James",
        "brand_name": "James",
        "experience_list": experience_list,
        "is_editor": is_editor(request.user),
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "James Adi Putra",
        "brand_name": "James",
        "form": form,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not can_update(request.user):
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "James Adi Putra",
        "brand_name": "James",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

# Education
def get_education_json(request):
    education_list = Education.objects.all()
    education_json = serializers.serialize("json", education_list)
    return HttpResponse(education_json, content_type="application/json")

def show_education(request):
    json_response = get_education_json(request)

    education_entries = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    education_list = [entry.object for entry in education_entries]

    context = {
        "name": "James",
        "brand_name": "James",
        "education_list": education_list,
        "is_editor": is_editor(request.user),
    }
    return render(request, "education.html", context)

@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "James Adi Putra",
        "brand_name": "James",
        "form": form,
    }
    return render(request, "education_form.html", context)

@login_required(login_url="/login/")
def update_education(request, education_id):
    if not can_update(request.user):
        raise PermissionDenied

    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
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

@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat pendidikan berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

# Projects
def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize(
        "json", projects
    )
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
        "is_editor": is_editor(request.user),
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "James Adi Putra",
        "brand_name": "James",
        "form": form,
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def update_project(request, project_id):
    if not can_update(request.user):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek berhasil diperbarui!")
        return redirect("main:show_projects")

    context = {
        "name": "James Adi Putra",
        "brand_name": "James",
        "form": form,
        "project": project,
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Proyek berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

# Star
@login_required(login_url="/login/")
def toggle_experience_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def toggle_project_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":

        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")
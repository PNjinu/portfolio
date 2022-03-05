from django.shortcuts import render, get_object_or_404
from .models import Job, Blog

def home(request):
    jobs = Job.objects.all
    blogs = Blog.objects.all
    return render(request, "jobs/home.html", {
        'jobs': jobs,
        'blogs': blogs
        })

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {
        'job': job_detail
    })
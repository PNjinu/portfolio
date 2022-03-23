from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Blog
from .forms import ContactForm

#EMAIL ALERTS
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def home(request):
    jobs = Job.objects.all
    blogs = Blog.objects.all

    # Processing the form
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            #save to the database
            form.save()

            #send email notification
            name = form.cleaned_data['name']
            email= form.cleaned_data['email']
            subject= form.cleaned_data['subject']
            message= form.cleaned_data['message']
            try:
                send_mail("New contact: " + email #subject
                , subject + " \n Name: "+name+"\n Message: "+message #message
                , 'admin@kurzsystems.com' #from email
                , ['admin@kurzsystems.com']) # send_to email list
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            #return redirect('home')
    else:       
        form = ContactForm()
    return render(request, "jobs/home.html", {
        'jobs': jobs,
        'blogs': blogs,
        'form': form
        })

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {
        'job': job_detail
    })
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About, Technology, Project
from .forms import ContactForm

def home(request):

    about = About.get_about()

    technologies = Technology.objects.all()

    projects = Project.objects.prefetch_related('technologies').all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dziękuję za wiadomość! Odpowiem najszybciej jak to mozliwe')
            return redirect('home')
    else:
        form = ContactForm()

    context = {
        'about': about,
        'technologies': technologies,
        'projects': projects,
        'form': form
    }

    return render(request, 'portfolio/home.html', context)
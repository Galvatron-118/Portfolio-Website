from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        context['blogs'] = Blog.objects.all()
        context['contact'] = Contact.objects.all()


        

        return context
    
    """def contact(request):
        if request.method=="POST":
            #contact=Contact()
            name=request.POST.get('name')
            email=request.POST.get('email')
            message=request.POST.get('message')
            contact=Contact.objects.create_user(name,email,message)
            #contact.name=name
            #contact.email=email
            #contact.message=message
            contact.save()
            #return redirect('home.html')
        render(request,'home.html')"""




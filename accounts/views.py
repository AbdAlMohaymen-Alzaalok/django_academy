from django.shortcuts import render,redirect
from . import forms
from django.views.generic import CreateView
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.views import login_required

class CreateUser(CreateView):
    form_class = forms.CreateUserForm
    template_name = 'registration/register.html'

    def get_success_url(self):
        login(self.request,self.object)
        return reverse('index')


@login_required()
def edit_form(request):
    if request.method=='POST':
        form=forms.ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=forms.ProfileForm(instance=request.user)
    return render(request,'profile.html',{
        'form':form
    })

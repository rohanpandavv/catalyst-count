from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def list_users(request):
    users = User.objects.all()
    return render(request, 'users/users_list.html', {'users': users})

class AddUserView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/add_user.html'
    success_url = reverse_lazy(list_users)
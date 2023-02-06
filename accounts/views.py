from django.shortcuts import render
from .forms import UserCreateForm

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context = {'form': form}
            for field in form.fields:
                if field in form.errors:
                    print(form.errors[field])
                    break
            return render(request, 'accounts/registration.html', context)
            
    form = UserCreateForm()
    context = {'form': form}
    return render(request, 'accounts/registration.html', context)


def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)
from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import SignUpForm
# Create your views here.
def frontpage(request):
    return render(request, 'chat_web_frontend/frontpage.html');

def homepage(request):
    return render(request,'chat_web_frontend/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'chat_web_frontend/signup.html', {'form': form})
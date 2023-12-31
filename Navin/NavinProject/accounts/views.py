from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from travello.models import Destination
from django.core.mail import send_mail
# Create your views here.



def register(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name = first_name, last_name = last_name)
                user.save()
                subject = 'New Contact Form Submission'
                message = f'Name: {user.first_name}\nEmail: {user.email}\nUsername: {user.username}'
                from_email = 'haykghazakhyan@gmail.com'  # Use the same email as in your settings
                recipient_list = [f"{user.email}", "haykghazakhyan@gmail.com"]  # Your email address

                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

                messages.info(request, "User created")
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect("login")
    else:
        return render(request, 'login.html')
    


def logout(request):
    auth.logout(request)
    return redirect("/")


def destination(request, pk):
    my_object = Destination.objects.get(id = pk)

    return render(request, 'destination.html', {'my_object': my_object})
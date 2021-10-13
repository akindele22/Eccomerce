from django.shortcuts import render,redirect,get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site

from .tokens import account_activator
from .forms import SignUpForm

def home(request):
    return render(request, 'store/store.html')

def activation_sent_view(request):
    return render(request,'activation_sent.html')

def activate(request):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError,ValueError, OverflowError, User.DoesNotExist):
        user = None
    # check if user has already register
    if user is not None and account_activator_check.token(user, token):
        user.is_active = True
        user.account.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect(request, 'store/store.html')
    else:
        return render(request,'activation_invalid.html')

def signUp(request):
    #This is to authenticate userform
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # To validate the form
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.account.first_name = form.cleaned_data.get('first_name')
            user.account.last_name = form.cleaned_data.get('last_name')
            user.account.email = form.cleaned_data.get('email')
            
            # user can't login until link confirmed
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            # load a template like get_template()
            # and calls its render() method immediately
            message = render_to_string('activation_request.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token':account_activator.make_token(user)
            })
            user.email_user(subject,message)
            return redirect('mainx')

    else:
        form =SignUpForm()
    return render(request, 'user/signUp.html',{'form':form})

def login(request):
    #This is to authenticate userform
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # To validate the form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request,user)
            # To create a flash msg and to redirect to home page after successful signUp
            #messages.success(request, f'Account successfully created {username}')
            return redirect('mainx')
    else:
        form = UserCreationForm()
    return render(request, 'user/login.html')


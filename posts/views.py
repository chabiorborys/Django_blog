from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm, RegisterForm, LoginForm, NewVideoForm
from django.contrib.auth.models import User
from django.views.generic.base import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import Video, Comment
import string, random

class LandingPageView(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context)

class BlogPageView(View):
    def get(self, request):
        context = {}
        return render(request, 'tech.html', context)

class AboutPageView(View):
    def get(self, request):
        context = {}
        return render(request, 'about.html', context)

class ContactPageView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html', {'form':form})
            
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']

            message = '{0} has sent you a new message:\n\n{1}'.format(name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender, ['chabiorborys@gmail.com'])
            return HttpResponse('Thanks for sending an e-mail!')
        return render(request, 'contact.html', {'form': form})
    
class RegisterPageView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})   

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            new_user = User(username=username, first_name=first_name, last_name=last_name, email=email)
            new_user.set_password(password)
            new_user.save()
            return redirect('/')
        return render(request, 'register.html', {'form': form})

class LoginPageView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # if user exists, login() function will keep him logged during session
                login(request, user)
                return redirect('/') 
            else:
                return redirect('/login')

class UploadVideoPageView(View):
    def get(self, request):  
        form = NewVideoForm()
        most_recent_videos = Video.objects.order_by('-datetime')[:10]
        return render(request, 'new_video.html', {'form': form, 'most_recent_videos':most_recent_videos})

    def post(self, request):
        form = NewVideoForm(request.POST, request.FILES)
        if form.is_valid():
            # create new Video Entry
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            file = form.cleaned_data['file']
            random_char = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            path = random_char+file.name
            new_video = Video(title=title,
                              description=description, 
                              user=request.user,
                              path=path)
            new_video.save()
            # redirect to created view template of the video
            return redirect('/new_video/{}'.format(new_video.pk))
        else:
            return HttpResponse('Your form is not valid. Try again.')
        return render(request, 'new_video.html', {'form': form})

class VideoPageView(View):
    def get(self, request, id):
        context = {}
        return render(request, 'video.html', {})


class CreatingScriptsPageView(View):
    def get(self, request):
        context = {}
        return render(request, 'creating_scripts.html', context)

class DigitalOceanPageView(View):
    def get(self, request):
        context = {}
        return render(request, 'digital_ocean.html', context)

class DjangoPageView(View):
    def get(self, request):
        context = {}
        return render(request, 'django.html', context)

class DockerPageView(View):
    def get(self, request):
        context = {}
        return render(request, 'docker.html', context)

class GithubPageView(View):
    def get(self, request):
        context = {}
        return render(request, 'github.html', context)

class PythonPageView(View):
    def get(self, request):
        context = {}
        return render(request, 'python.html', context)

class SecureShellPageView(View):
    def get(self, request):
        context = {}
        return render(request, 'secure_shell.html',context)

class VimPageView(View):
    def get(self, request):
        context = {}
        return render(request, 'vim.html', context)

class JavaScriptPageView(View):
    def get(self, request):
        context = {}
        return render(request, 'java_script.html', context)

class DomAccessMethodsPageView(View):
    def get(self, request):
        context = {}
        return render(request, 'dom_access_methods.html', context)
    
class ModifyingExistingElementPageView(View):
    def get(self, request):
        context = {}
        return render(request,'modifying_exisiting_element.html', context)

class DomEvents(View):
    def get(self, request):
        context = {}
        return render(request,'dom_events.html', context)

class DomAnimation(View):
    def get(self, request):
        context = {}
        return render(request, 'dom_animation.html', context)

class AjaxView(View):
    def get(self, request):
        context = {}
        return render(request, 'ajax.html', context)

class AjaxInfoView(View):
    def get(self, request):
        context = {}
        return render(request, 'ajax_info.txt', context)

class JsCodeWarsView(View):
    def get(self, request):
        context = {}
        return render(request, 'js_codewars.html', context)

class JsCodeWarsExercisesDoneView(View):
    def get(self, request):
        context = {}
        return render(request, 'codewars_exercises_done.html', context)

class JSMethodsView(View):
    def get(self, request):
        context = {}
        return render(request, 'js_methods.html', context)

class GithubVol1PageView(View):
    def get(self, request):
        context = {}
        return render(request, 'github_vol1.html', context)

class UsefullTermsPageView(View):
    def get(self, request):
        context = {}
        return render(request, 'usefull_terms.html', context)

class SecureShell1PageView(View):
    def get(self, request):
        context = {}
        return render(request, 'secure_shell1.html', context)

class SecureShell2PageView(View):
    def get(self, request):
        context = {}
        return render(request, 'secure_shell2.html', context)
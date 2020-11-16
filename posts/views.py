from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm


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
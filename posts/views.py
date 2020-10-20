from django.shortcuts import render, redirect
from django.views import View


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
        context = {}
        return render(request, 'contact.html', context)

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

class GithubVol1PageView(View):
    def get(self, request):
        context = {}
        return render(request, 'github_vol1.html', context)

class UsefullTermsPageView(View):
    def get(self, request):
        context = {}
        return render(request, 'usefull_terms.html', context)

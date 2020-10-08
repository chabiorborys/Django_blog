from django.shortcuts import render, redirect
from django.views import View


class LandingPageView(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context)
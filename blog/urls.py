from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LandingPageView.as_view()),
    path('tech/', views.BlogPageView.as_view()),
    path('about/', views.AboutPageView.as_view()),
    path('contact/', views.ContactPageView.as_view()),
    path('github/', views.GithubPageView.as_view()),
    path('digital_ocean/', views.DigitalOceanPageView.as_view()),
    path('python/', views.PythonPageView.as_view()),
    path('django/', views.DjangoPageView.as_view()),
    path('secure_shell/', views.SecureShellPageView.as_view()),
    path('docker/', views.DockerPageView.as_view()),
    path('vim/', views.VimPageView.as_view()),
    path('creating_scripts/', views.CreatingScriptsPageView.as_view()),
    path('github_vol1/', views.GithubVol1PageView.as_view()),
    path('usefull_terms/', views.UsefullTermsPageView.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

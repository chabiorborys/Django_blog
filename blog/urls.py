from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts import views

import debug_toolbar
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
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
    path('java_script/', views.JavaScriptPageView.as_view()),
    path('dom_access_methods/', views.DomAccessMethodsPageView.as_view()),
    path('modifying_existing_element/', views.ModifyingExistingElementPageView.as_view()),
    path('dom_events/', views.DomEvents.as_view()),
    path('dom_animation/', views.DomAnimation.as_view()),
    path('ajax/', views.AjaxView.as_view()),
    path('ajax_info/', views.AjaxInfoView.as_view()),
    path('js_codewars/', views.JsCodeWarsView.as_view()),
    path('codewars_exercises_done/', views.JsCodeWarsExercisesDoneView.as_view
    ()),
    path('github_vol1/', views.GithubVol1PageView.as_view()),
    path('usefull_terms/', views.UsefullTermsPageView.as_view()),
    path('secure_shell1/', views.SecureShell1PageView.as_view()),
    path('secure_shell2/', views.SecureShell2PageView.as_view()),
    path('js_methods/', views.JSMethodsView.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path,include

urlpatterns = [
    path('', include('tvshows_app.urls')),
]

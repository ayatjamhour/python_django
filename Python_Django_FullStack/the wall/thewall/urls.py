from django.urls import path
from . import views
urlpatterns = [
    path('', views.welc),
    path('addpost',views.addpost), #to add post
    path('comment/<int:id>',views.addcomm),

]

from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('success',views.success),
    path('register',views.add_new_user),
    path('login',views.login_user),
    path('log_out',views.log_out)
]
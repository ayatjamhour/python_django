from django.urls import path    
from django.conf.urls import url 
from . import views

urlpatterns = [
    path('',views.index),
    #shows
    path('shows',views.show_all),
    #new show
    path('shows/new',views.add),
    #show with id details from db /{{}}
    path('shows/<int:id>',views.this_show_details),
    #show with details from the add form
    path('shows/<int:id>',views.show_from_form),
    #edit show form
    path('shows/<int:id>/edit',views.show_edit),
    # updadte the data from the edit form
    path('shows',views.update_show),
    #show from update
    path('shows/<int:id>/update',views.this_update_details),
    # create
    path('shows/sth',views.create),
    #delete
    path('shows/<int:id>/destroy',views.delete),

]

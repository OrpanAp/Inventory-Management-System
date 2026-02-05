from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.home_page, name='home_page'),


    # Display    
    path('display_laptops', views.display_laptops, name='display_laptops'),
    path('display_desktops', views.display_desktops, name='display_desktops'),
    path('display_mobiles', views.display_mobiles, name='display_mobiles'),


    # Add
    path('add_laptops', views.add_laptops, name='add_laptops'),
    path('add_desktops', views.add_desktops, name='add_desktops'),
    path('add_mobiles', views.add_mobiles, name='add_mobiles'),


    # Edit
    path('edit_laptops/<int:pk>', views.edit_laptops, name='edit_laptops'),
    path('edit_desktops/<int:pk>', views.edit_desktops, name='edit_desktops'),
    path('edit_mobiles/<int:pk>', views.edit_mobiles, name='edit_mobiles'),


    # Delete
    path('delete_laptops/<int:pk>', views.delete_laptops, name='delete_laptops'),
    path('delete_desktops/<int:pk>', views.delete_desktops, name='delete_desktops'),
    path('delete_mobiles/<int:pk>', views.delete_mobiles, name='delete_mobiles'),
]

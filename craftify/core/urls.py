from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('explore', views.explore, name='explore'),
    
    path('login', views.loginUser, name='login'),
    path('register', views.registerUser, name='register'),
    path('logout', views.logoutUser, name='logout'),
    
    
    path('dashboard', views.dashboard, name='dashboard'),
    
    path('addItem', views.addItem, name='addItem'),
        
    path('deleteItem/<int:item_id>/', views.deleteItem, name='deleteItem'),
    
    path('edit/<int:item_id>/', views.editItem, name='edit'),
    
    # path('explore-category/<str:category>/', views.explore, name='explore-category'),
    path('explore-cat/<str:category>/', views.explore, name='explore-cat'),
    
    
    
 
]

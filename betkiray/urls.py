from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from gofor.views import gofor_detail
from core.views import home, about, contact, signup, search, tekeray
from landlord.views import akeray_detail, add_akeray, delete_akeray, update_akeray
from django.contrib.auth import views
from landlord.api import api_add_to_gofor, api_remove_from_gofor, api_add_new_rent


urlpatterns = [
    path('', home, name = 'home'),
    path('search/', search, name = 'search'),
    path('tekeray/', tekeray, name = 'tekeray'),
    path('about/', about, name='about'),
    path('contact/', contact, name = 'contact'),
    path('gofor/', gofor_detail, name = 'gofor'),
    path('add/', add_akeray, name='add_akeray'),
    path('admin/', admin.site.urls),

    #Auth
    path('signup/', signup, name = 'signup'),
    path('logout/', views.LogoutView.as_view(), name = 'logout'),
    path('login/', views.LoginView.as_view(), name = 'login'),

    # API
    path('add_to_gofor/', api_add_to_gofor, name = 'api_add_to_gofor'),    
    path('remove_from_gofor/', api_remove_from_gofor, name = 'api_remove_from_gofor'),  
    path('add_new_rent/', api_add_new_rent, name = 'api_add_new_rent'),


    # Landlord
    path('<int:id>/', akeray_detail, name='akeray_detail'),
    path('<akeray_id>/update', update_akeray, name='update'),
    path('<akeray_id>/delete', delete_akeray, name='delete'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
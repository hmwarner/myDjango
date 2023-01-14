from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views, authenticate
from django.urls import path, include
from users import views as user_views
from blog import views
from users.views import PasswordsChangeView
#from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'users', user_views.UserViewSet)
#router.register(r'groups', user_views.GroupViewSet)
#router.register(r'posts', user_views.PostViewSet)

urlpatterns = [
    path('', include('blog.urls'), name='blog'),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html',redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('password/', user_views.PasswordsChangeView.as_view(template_name='users/registration/change_password.html')),
    path('password_success/', user_views.password_success, name='users/registration/password_success'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    #path('api/', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

admin.site.index_title = 'Directory'
admin.site.site_title = 'Control Panel'
admin.site.site_header = 'Administration Dashboard'


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

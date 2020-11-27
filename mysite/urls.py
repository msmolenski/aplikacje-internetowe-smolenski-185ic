from django.contrib import admin
from django.urls import path, include
from register import views as v
from django.contrib.auth import views as auth_views
from register.views import PasswordsChangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),
    path('', include('blog.urls')),
    path('', include('django.contrib.auth.urls')),

    path("profile/", v.profile, name="profile"),
    path("password/", PasswordsChangeView.as_view(template_name='edit_profile/password_edit.html')),
    path("password_success/", v.password_success, name="password_success"),
    path("password-reset/", 
    auth_views.PasswordResetView.as_view(
        template_name='edit_profile/password_reset.html'),
     name='password_reset'),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name='edit_profile/password_reset_done.html'), name='password_reset_done'),
    path("password-reset-cnofirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(
        template_name='edit_profile/password_reset_confirm.html'), name='password_reset_confirm'),

    #path('oauth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('allauth.urls')), 
]
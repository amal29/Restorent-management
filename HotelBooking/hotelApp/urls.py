
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
path('register',views.Register,name="register"),
path('login',views.login_view,name="login"),
path('logout',views.logout_view,name="logout"),
path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password/password_reset.html "),name="reset_password"),
path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_sent.html"),name="password_reset_done"),
path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_form.html"),name="password_reset_confirm"),
path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_done.html"),name="password_reset_complete"),

    path('',views.Home,name='home'),
    path('rhome',views.Rhome,name='rhome'),

    path('book',views.BookingView,name='book'),
    path('room',views.Myroom,name='room'),
    path('droom',views.DeleteRoom,name='droom'),

]


from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path(
          'login/',
          views.LoginView.as_view(),
          name='login',
     ),
    path(
          'logout/',
          views.LogoutView.as_view(),
          name='logout',
     ),
    path(
          'password_change/done/',
          views.PasswordChangeDoneView.as_view(),
          name='password_change_done',
     ),
    path(
          'password_change/',
          views.PasswordChangeView.as_view(),
          name='password_change',
     ),
    path(
          'password_reset/done/',
          views.PasswordResetDoneView.as_view(),
          name='password_reset_done',
     ),
    path(
          'password_reset/compliete/',
          views.PasswordResetCompleteView.as_view(),
          name='password_reset_complete',
     ),
    path(
          'password_reset_confirm/<uidb64>/<token>/',
          views.PasswordResetConfirmView.as_view(),
          name='password_reset_confirm',
     ),
    path(
          'password_reset/',
          views.PasswordResetView.as_view(),
          name='password_reset',
     ),
    path(
          'signup/',
          views.SignUpView.as_view(),
          name='signup',
     ),
    path(
          'profile/<int:pk>/edit/',
          views.ProfileEditView.as_view(),
          name='profile_edit',
     ),
    path(
          'profile/<int:pk>/',
          views.ProfileView.as_view(),
          name='profile',
     ),
    path(
          'users_list/',
          views.UsersList.as_view(),
          name='users_list',
     ),
]

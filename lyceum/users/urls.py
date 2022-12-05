from django.urls import path

from .views import LoginView, LogoutView, \
    PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView, SignUpView, ProfileView, \
    ProfileEditView, UsersList

app_name = 'users'
urlpatterns = [
    path('login/',
         LoginView.as_view(),
         name='login'),

    path('logout/',
         LogoutView.as_view(),
         name='logout'),

    path('password_change/done/',
         PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    path('password_change/',
         PasswordChangeView.as_view(),
         name='password_change'),

    path('password_reset/done/',
         PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    path('password_reset/compliete/',
         PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('password_reset/',
         PasswordResetView.as_view(),
         name='password_reset'),

    path('signup/',
         SignUpView.as_view(),
         name='signup'),

    path('profile/<int:pk>/edit/',
         ProfileEditView.as_view(),
         name='profile_edit'),

    path('profile/<int:pk>/',
         ProfileView.as_view(),
         name='profile'),

    path('users_list/',
         UsersList.as_view(),
         name='users_list'),
]

from django.contrib.auth import views
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class LoginView(views.LoginView):
    """View class for login page.

    render login html.
    """
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['title'] = 'Вход'
        context['btn_label'] = 'Войти'
        return context


class LogoutView(views.LogoutView):
    """View class for logout page.

    render logout html.
    """
    template_name = 'users/logout.html'

    def get_context_data(self, **kwargs):
        context = super(
            LogoutView,
            self,
        ).get_context_data(**kwargs)
        context['title'] = 'Выход'
        context['message'] = 'Вы успешно вышли!'
        context['btn_label'] = 'На главную'
        return context


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    """View class for password change done page.

    render password change done html.
    """
    template_name = 'users/password_change_done.html'

    def get_context_data(self, **kwargs):
        context = super(
            PasswordChangeDoneView,
            self,
        ).get_context_data(**kwargs)
        context['title'] = 'Смена пароля'
        context['message'] = 'Вы успешно сменили пароль!'
        context['btn_label'] = 'На главную'
        return context


class PasswordChangeView(views.PasswordChangeView):
    """View class for password change page.

    render password change html.
    """
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:password_change_done')

    def get_context_data(self, **kwargs):
        context = super(
            PasswordChangeView,
            self,
        ).get_context_data(**kwargs)
        context['title'] = 'Смена пароля'
        context['btn_label'] = 'Поменять'
        return context


class PasswordResetDoneView(views.PasswordResetDoneView):
    """View class for password reset done page.

    render password reset done html.
    """
    template_name = 'users/password_reset_done.html'

    def get_context_data(self, **kwargs):
        context = super(
            PasswordResetDoneView,
            self,
        ).get_context_data(**kwargs)
        context['title'] = 'Сброс пароля'
        context['message'] = 'Вам на почту отправлено письмо с подтверждением'
        context['btn_label'] = 'На главную'
        return context


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    """View class for password reset confirm page.

    render password reset confirm html.
    """
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')

    def get_context_data(self, **kwargs):
        context = super(
            PasswordResetConfirmView,
            self,
        ).get_context_data(**kwargs)
        context['title'] = 'Сброс пароля'
        context['btn_label'] = 'Сбросить'
        return context


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    """View class for password reset complete page.

    render password reset complete html.
    """
    template_name = 'users/password_reset_complete.html'

    def get_context_data(self, **kwargs):
        context = super(
            PasswordResetCompleteView,
            self,
        ).get_context_data(**kwargs)
        context['title'] = 'Сброс пароля'
        context['message'] = 'Пароль успешно сброшен'
        context['btn_label'] = 'На главную'
        return context


class PasswordResetView(views.PasswordResetView):
    """View class for password reset page.

    render password reset html.
    """
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')

    def get_context_data(self, **kwargs):
        context = super(
            PasswordResetView,
            self,
        ).get_context_data(**kwargs)
        context['title'] = 'Сброс пароля'
        context['btn_label'] = 'Сбросить'
        return context


class SignUpView(generic.edit.CreateView):
    """View class for signup page.

    render signup html.
    """
    template_name = 'users/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(
            SignUpView,
            self,
        ).get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['btn_label'] = 'Подтвердить'
        return context


class ProfileEditView(generic.edit.UpdateView):
    """View class for profile edit page.

    render profile edit html.
    """
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('homepage:home')

    def get_context_data(self, **kwargs):
        context = super(
            ProfileEditView,
            self,
        ).get_context_data(**kwargs)
        context['title'] = 'Ваш профиль'
        return context


class ProfileView(generic.edit.UpdateView):
    """View class for profile page.

    render profile html.
    """
    model = CustomUser
    fields = ('first_name', 'last_name', 'email', 'birthday')
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super(
            ProfileView,
            self,
        ).get_context_data(**kwargs)
        context['title'] = 'Ваш профиль'
        return context


class UsersList(generic.ListView):
    """View class for users list page.

    render users list html.
    """
    model = CustomUser
    template_name = 'users/user_list.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['items'] = CustomUser.objects.all().filter(is_active=True)
        context['title'] = 'Ваш профиль'
        return context

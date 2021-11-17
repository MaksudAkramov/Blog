from django.contrib.auth.mixins import LoginRequiredMixin


class LoginPermissionMixin(LoginRequiredMixin):
    login_url = 'login'
    redirect_field_name = 'home'
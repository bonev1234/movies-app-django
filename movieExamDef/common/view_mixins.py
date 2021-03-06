from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages


class RedirectToDashboard:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')

        return super().dispatch(request, *args, **kwargs)


class RedirectPermissionRequiredMixin(PermissionRequiredMixin):
    login_url = reverse_lazy('dashboard')

    def handle_no_permission(self):
        messages.error(self.request, 'You do not have permission to create a new Movie! Please contact the administrator.')
        return redirect(self.get_login_url())

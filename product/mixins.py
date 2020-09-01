from django.contrib.auth.mixins import AccessMixin


class IsStaffAccessMixin(AccessMixin):
    def dispatch(slef, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
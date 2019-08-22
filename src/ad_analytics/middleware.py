from django_multitenant.utils import set_current_tenant


class MultitenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if request.user and not request.user.is_anonymous:
            set_current_tenant(request.user.employee.company)

        response = self.get_response(request)

        return response

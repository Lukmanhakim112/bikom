from functools import wraps

from django.shortcuts import redirect


def redirect_staff(func):
    """
    redirect staff user to the admin (staff) dashboard page
    """

    @wraps(func)
    def _wrap_func(request, *args, **kwargs):

        if request.user.is_staff:
            return redirect('admin-dashboard')

        return func(request, *args, **kwargs)

    return _wrap_func



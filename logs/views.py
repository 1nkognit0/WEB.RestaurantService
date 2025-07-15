from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from orders.views import role_required

@login_required
@role_required('admin')
def logs_view(request):
    return render(request, 'logs/admin.html')

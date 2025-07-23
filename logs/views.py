from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from orders.views import role_required

import os

@login_required
@role_required('admin')
def logs_view(request):
    if os.path.exists('../app.log'):
        with open('../app.log', 'r') as f:
            logs = f.readlines()[-50:]
    return render(request, 'logs/admin.html', {'logs': logs})

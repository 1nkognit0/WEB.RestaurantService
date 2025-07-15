from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'role', 'password1', 'password2']

class UserAuthorizationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)
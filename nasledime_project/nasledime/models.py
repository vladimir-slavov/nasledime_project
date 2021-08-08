from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Will(models.Model):

    """
    first_name, last_name, uic and address should be part
    of the Will model instead of the User model, since the
    user may use the app to draft a will for another person.
    """

    first_name = models.CharField(
        max_length=20,
    )
    last_name = models.CharField(
        max_length=20,
    )
    uic = models.IntegerField()
    address = models.CharField(
        max_length=200,
    )
    text = models.TextField()
    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
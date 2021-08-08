from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.client import RequestFactory, Client

from nasledime_project import settings
from nasledime_project.profiles.models import NasledimeUser
from nasledime_project.profiles.views import RegisterUser

User = get_user_model()


class UserTestCase(TestCase):

    def setUp(self):
        self.user = User(email="testemail@abv.bg")

        """
        We use the set_password() method since a direct creation
        of the user object with as an instance of User with email
        and password will not hash the password.
        """

        self.user.set_password('MyTestPassword4321')
        self.user.save()

    def test_user_is_created(self):
        self.assertEqual(self.user.pk, self.user.id)

    def test_password_is_hashed(self):
        self.assertNotEqual(self.user.password, 'MyTestPassword4321')

    def test_user_is_not_superuser(self):
        self.assertFalse(self.user.is_superuser)

    def test_user_is_not_staff(self):
        self.assertFalse(self.user.is_staff)

    def test_user_can_log_in(self):
        c = Client()
        user_is_loggedin = c.login(email='testemail@abv.bg', password='MyTestPassword4321')
        self.assertTrue(user_is_loggedin)


class ApplicationHasPublicAndPrivatePartTestCase(TestCase):

    """
    The purpose of the tests in this class is to verify that
    the application indeed has a public and private part.
    We do this by using an instance of the Client() to log in,
    and by attempting to access urls that require authentication.
    """

    def setUp(self):
        self.user = User(email="testemail@abv.bg")

        """
        We use the set_password() method since a direct creation
        of the user object with as an instance of User with email
        and password will not hash the password.
        """

        self.user.set_password('MyTestPassword4321')
        self.user.save()

    def test_unauthenticated_user_cannot_access_private_parts(self):
        c = Client()
        get_result = c.get('/create-will/')

        """
        The CreateWill CBV inherits the LoginRequiredMixin, so when a
        non-authenticated user tries to access the '/create-will/' url, 
        login_url should redirect to the user login page.
        This means that, if proper redirection has happened,
        the status_code of get_result should be 302.
        """

        self.assertEqual(get_result.status_code, 302)

    def test_authenticated_user_can_access_private_parts(self):
        c = Client()
        c.login(email='testemail@abv.bg', password='MyTestPassword4321')
        get_result = c.get('/create-will/')

        """
        The CreateWill CBV inherits the LoginRequiredMixin.
        When an authenticated user tries the access the
        '/create-will' url, the user should be successful.
        This means that the status_code of get_result 
        should be 200.
        """

        self.assertEqual(get_result.status_code, 200)
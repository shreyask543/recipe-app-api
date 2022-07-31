"""
Test Models
"""

import email
from django.test import TestCase
from django.contrib.auth import get_user_model



class ModelTests(TestCase):
    """Test Models"""


    def test_user_creat_with_email(self):
        """Test user with email"""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.asserEqual(user.email, email)
        self.asserTrue(user.check_password(password))
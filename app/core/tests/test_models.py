"""
Test Models
"""

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

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    

    def test_user_creat_with_email_normalize(self):
        """Test user with email normalized"""
        sample_email = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
            ]
        for email, expected_email in sample_email:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected_email)
    

    def test_user_creat_without_email_error(self):
        """Test user without email raises value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'sample123')

    def testcreat_super_user(self):
        """Test to create super user"""
        user = get_user_model().objects.create_superuser(
            'test1@example.com', 'sample123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

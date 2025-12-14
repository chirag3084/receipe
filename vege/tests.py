from django.test import TestCase, AsyncClient
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Receipe
from asgiref.sync import sync_to_async
import asyncio


class AsyncViewsTestCase(TestCase):
    """Test cases for async views"""

    def setUp(self):
        """Set up test data"""
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            first_name='Test',
            last_name='User',
            email='test@example.com'
        )
        self.client = AsyncClient()

    async def test_home_view_async(self):
        """Test that home view works with async"""
        response = await self.client.get('/')
        self.assertEqual(response.status_code, 200)

    async def test_login_page_get_async(self):
        """Test login page GET request with async"""
        response = await self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    async def test_login_page_post_async(self):
        """Test login page POST request with async"""
        response = await self.client.post('/login/', {
            'username': 'testuser',
            'password': 'testpass123'
        })
        # Should redirect after successful login
        self.assertEqual(response.status_code, 302)

    async def test_register_get_async(self):
        """Test register page GET request with async"""
        response = await self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    async def test_register_post_async(self):
        """Test register page POST request with async"""
        response = await self.client.post('/register/', {
            'username': 'newuser',
            'password': 'newpass123',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'new@example.com'
        })
        # Should redirect after successful registration
        self.assertEqual(response.status_code, 302)
        
        # Verify user was created
        user_exists = await User.objects.filter(username='newuser').aexists()
        self.assertTrue(user_exists)

    async def test_logout_async(self):
        """Test logout with async"""
        # First login
        await sync_to_async(self.client.force_login)(self.user)
        
        # Then logout
        response = await self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)

    async def test_receipes_view_requires_login(self):
        """Test that receipes view requires login"""
        response = await self.client.get('/receipes/')
        # Should redirect to login page
        self.assertEqual(response.status_code, 302)

    async def test_receipes_view_async_authenticated(self):
        """Test receipes view with authenticated user"""
        await sync_to_async(self.client.force_login)(self.user)
        response = await self.client.get('/receipes/')
        self.assertEqual(response.status_code, 200)

    async def test_password_reset_complete_async(self):
        """Test password reset complete view with async"""
        # This would need proper URL configuration
        # Just testing that the view is async
        pass


class AsyncReceipeModelTestCase(TestCase):
    """Test cases for async Receipe model operations"""

    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    async def test_create_receipe_async(self):
        """Test creating a recipe with async"""
        receipe = await Receipe.objects.acreate(
            receipe_name='Test Recipe',
            receipe_description='Test Description',
            user=self.user
        )
        self.assertEqual(receipe.receipe_name, 'Test Recipe')
        self.assertEqual(receipe.receipe_description, 'Test Description')

    async def test_get_receipe_async(self):
        """Test getting a recipe with async"""
        # Create a recipe first
        created_receipe = await Receipe.objects.acreate(
            receipe_name='Test Recipe',
            receipe_description='Test Description',
            user=self.user
        )
        
        # Retrieve it
        receipe = await Receipe.objects.aget(id=created_receipe.id)
        self.assertEqual(receipe.receipe_name, 'Test Recipe')

    async def test_update_receipe_async(self):
        """Test updating a recipe with async"""
        # Create a recipe
        receipe = await Receipe.objects.acreate(
            receipe_name='Test Recipe',
            receipe_description='Test Description',
            user=self.user
        )
        
        # Update it
        receipe.receipe_name = 'Updated Recipe'
        await receipe.asave()
        
        # Verify update
        updated_receipe = await Receipe.objects.aget(id=receipe.id)
        self.assertEqual(updated_receipe.receipe_name, 'Updated Recipe')

    async def test_delete_receipe_async(self):
        """Test deleting a recipe with async"""
        # Create a recipe
        receipe = await Receipe.objects.acreate(
            receipe_name='Test Recipe',
            receipe_description='Test Description',
            user=self.user
        )
        receipe_id = receipe.id
        
        # Delete it
        await receipe.adelete()
        
        # Verify deletion
        exists = await Receipe.objects.filter(id=receipe_id).aexists()
        self.assertFalse(exists)

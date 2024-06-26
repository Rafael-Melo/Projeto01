from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class RecipeURLsTest(TestCase):
    def test_recipes_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')


    def test_recipes_category_url_is_correct(self):
        home_url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(home_url, '/recipes/category/1/')


    def test_recipes_recipe_url_is_correct(self):
        home_url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(home_url, '/recipes/1/')


    def test_recipe_search_url_is_correct(self):
        home_url = reverse('recipes:search')
        self.assertEqual(home_url, '/recipes/search/')


    def test_recipes_sobre_url_is_correct(self):
        home_url = reverse('recipes:sobre')
        self.assertEqual(home_url, '/sobre/')


    def test_recipes_contato_url_is_correct(self):
        home_url = reverse('recipes:contato')
        self.assertEqual(home_url, '/contato/')


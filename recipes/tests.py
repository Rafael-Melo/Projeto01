from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

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

    def test_recipes_sobre_url_is_correct(self):
        home_url = reverse('recipes:sobre')
        self.assertEqual(home_url, '/sobre/')

    def test_recipes_contato_url_is_correct(self):
        home_url = reverse('recipes:contato')
        self.assertEqual(home_url, '/contato/')

class RecipeViewsTest(TestCase):
    def test_recipes_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipes_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)

    def test_recipes_recipe_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)

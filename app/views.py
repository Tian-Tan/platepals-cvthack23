from django.shortcuts import render
from django.http import HttpResponse
import requests

price_data = [{id: 1, 'name': 'carrots', 'price': 1.00}, {id: 2, 'name': 'broccoli', 'price': 3.00}, {id: 3, 'name': 'cauliflower', 'price': 4.00}, {id: 4, 'name': 'cabbage', 'price': 4.00}, {id: 5, 'name': 'brussels sprouts', 'price': 3.00}, {id: 6, 'name': 'green beans', 'price': 3.00}, {id: 7, 'name': 'peas', 'price': 1.00}, {id: 8, 'name': 'corn', 'price': 1.50}, {id: 9, 'name': 'potatoes', 'price': 4.00}, {id: 10, 'name': 'sweet potatoes', 'price': 3.00}, {id: 11, 'name': 'squash', 'price': 1.00}, {id: 12, 'name': 'zucchini', 'price': 3.00}, {id: 13, 'name': 'cucumbers', 'price': 1.00}, {id: 14, 'name': 'tomatoes', 'price': 2.00}, {id: 15, 'name': 'avocado', 'price': 3.00}, {id: 16, 'name': 'spinach', 'price': 2.00}, {id: 17, 'name': 'kale', 'price': 1.50}, {id: 18, 'name': 'arugula', 'price': 3.50}, {id: 19, 'name': 'lettuce', 'price': 2.00}, {id: 20, 'name': 'radishes', 'price': 1.30}, {id: 21, 'name': 'onions', 'price': 1.00}, {id: 22, 'name': 'shallots', 'price': 1.00}, {id: 23, 'name': 'scallions', 'price': 1.00}, {id: 24, 'name': 'rice vinegar', 'price': 2.00}, {id: 25, 'name': 'chili powder', 'price': 2.30}, {id: 26, 'name': 'dijon mustard', 'price': 3.30}, {id: 27, 'name': 'rice', 'price': 3.30}, {id: 28, 'name': 'pasta', 'price': 3.00}, {id: 29, 'name': 'bread', 'price': 2.70}, {id: 30, 'name': 'cereal', 'price': 5.00}, {id: 31, 'name': 'oatmeal', 'price': 3.30}, {id: 32, 'name': 'cornstarch', 'price': 1.60}, {id: 33, 'name': 'baking powder', 'price': 2.50}, {id: 34, 'name': 'baking soda', 'price': 2.00}, {id: 35, 'name': 'cocoa powder', 'price': 4.40}, {id: 36, 'name': 'peanut butter', 'price': 1.80}, {id: 37, 'name': 'coconut milk', 'price': 3.00}, {id: 38, 'name': 'powdered sugar', 'price': 1.80}, {id: 39, 'name': 'jam', 'price': 5.50}, {id: 40, 'name': 'jelly', 'price': 3.20}, {id: 41, 'name': 'beef', 'price': 7.00}, {id: 42, 'name': 'chicken', 'price': 7.40}, {id: 43, 'name': 'pork', 'price': 6.40}, {id: 44, 'name': 'shrimp', 'price': 9.30}, {id: 45, 'name': 'nutella', 'price': 8.00}, {id: 45, 'name': 'tofu', 'price': 3.00}, {id: 46, 'name': 'lentils', 'price': 1.20}, {id: 47, 'name': 'chickpeas', 'price': 1.50}, {id: 48, 'name': 'black beans', 'price': 0.80}, {id: 49, 'name': 'kidney beans', 'price': 1.30}, {id: 50, 'name': 'apple', 'price': 0.84}, {id: 51, 'name': 'bananas', 'price': 0.25}, {id: 52, 'name': 'oranges', 'price': 1.00}, {id: 53, 'name': 'lemons', 'price': 1.00}, {id: 54, 'name': 'grapefruits', 'price': 2.00}, {id: 55, 'name': 'pineapple', 'price': 3.34}, {id: 56, 'name': 'mango', 'price': 1.34}, {id: 57, 'name': 'kiwi', 'price': 0.54}, {id: 58, 'name': 'watermelon', 'price': 10.34}, {id: 59, 'name': 'grapes', 'price': 6.00}, {id: 60, 'name': 'pears', 'price': 1.34}, {id: 61, 'name': 'peaches', 'price': 3.49}, {id: 62, 'name': 'plums', 'price': 2.99}, {id: 63, 'name': 'cherries', 'price': 5.99}, {id: 64, 'name': 'orange juice', 'price': 2.98}, {id: 65, 'name': 'coconut water', 'price': 1.00}, {id: 66, 'name': 'lima beans', 'price': 3.64}, {id: 67, 'name': 'edamame', 'price': 2.14}, {id: 68, 'name': 'tuna', 'price': 1.00}, {id: 69, 'name': 'salmon', 'price': 9.99}, {id: 70, 'name': 'sardines', 'price': 1.83}, {id: 71, 'name': 'sugar', 'price': 2.99}, {id: 72, 'name': 'salt', 'price': 0.57}, {id: 73, 'name': 'pepper', 'price': 1.64}, {id: 74, 'name': 'olive oil', 'price': 5.83}, {id: 75, 'name': 'butter', 'price': 3.83}, {id: 76, 'name': 'milk', 'price': 3.02}, {id: 77, 'name': 'eggs', 'price': 2.99}, {id: 78, 'name': 'cheese', 'price': 2.83}, {id: 79, 'name': 'yogurt', 'price': 1.29}, {id: 80, 'name': 'honey', 'price': 3.93}, {id: 81, 'name': 'maple syrup', 'price': 8.46}, {id: 82, 'name': 'soy sauce', 'price': 1.58}, {id: 83, 'name': 'mustard', 'price': 0.93}, {id: 84, 'name': 'ketchup', 'price': 4.99}, {id: 85, 'name': 'garlic', 'price': 0.49}, {id: 86, 'name': 'cod', 'price': 8.00}, {id: 87, 'name': 'bay leaves', 'price': 4.49}, {id: 88, 'name': 'lime', 'price': 0.39}, {id: 89, 'name': 'cilantro', 'price': 0.83}, {id: 90, 'name': 'parsley', 'price': 1.00}, {id: 91, 'name': 'walnuts', 'price': 7.83}, {id: 92, 'name': 'pecans', 'price': 12.98}, {id: 93, 'name': 'cashews', 'price': 1.23}, {id: 94, 'name': 'peanuts', 'price': 2.59}, {id: 95, 'name': 'chocolate chips', 'price': 2.47}, {id: 96, 'name': 'oyster sauce', 'price': 4.00}, {id: 97, 'name': 'molasses', 'price': 3.48}, {id: 98, 'name': 'ginger', 'price': 4.99}, {id: 99, 'name': 'nutmeg', 'price': 5.23}, {id: 100, 'name': 'paprika', 'price': 0.99}]

# helper functions
def get_recipe(ingredients):
    '''
    A helper function to call the edamam api
    input: ingredients (String), can be separated by commas (,)
    output: 3 recipes returned by the api
    '''
    # commas need to be translated to "%2C%20"
    query_string = ""
    list_of_ingredients = ingredients.split(',')
    if len(list_of_ingredients) == 1:
        query_string += list_of_ingredients[0]
    else:
        for ingredient in list_of_ingredients:
            query_string += ingredient
            query_string += "%2C%20"
        query_string = query_string[:-6]
    query_string = query_string.replace(' ', '')
    url = f"https://api.edamam.com/api/recipes/v2?type=public&q={query_string}&app_id=ac98c1aa&app_key=a8a65c872d719137c8f64dedcf2ccee0"
    response = requests.get(url)
    data = response.json()
    recipes = []
    for num in range(3):
        recipe = {}
        recipe["label"] = data["hits"][num]["recipe"]["label"]
        recipe["image_url"] = data["hits"][num]["recipe"]["image"]
        recipe["ingredients"] = data["hits"][num]["recipe"]["ingredientLines"]
        recipe["info_url"] = data["hits"][num]["recipe"]["shareAs"]
        recipes.append(recipe)
    return(recipes)

def get_price(ingredient):
    iteration = 0
    for item in price_data:
        iteration += 1
        if item['name'] == ingredient:
            return item['price']

# Create your views here.

def home_view(request, *args, **kargs):
    return render(request, 'index.html', {})

def fb_view(request, *args, **kargs):
    pass

def resources_view(request, *args, **kargs):
    pass

def register_view(request, *args, **kargs):
    return render(request, 'restaurant_regist.html', {})

def reg_success_view(request, *args, **kargs):
    return render(request, 'register_success.html', {})
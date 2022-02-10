# by Kami Bigdely
# Extract Class

class Food:
    def __init__(self, name, prep_time, is_veggie, food_type, cuisine, ingredients, recipe):
        self.name = name
        self.prep_time = prep_time
        self.is_veggie = is_veggie
        self.food_type = food_type
        self.cuisine = cuisine
        self.ingredients = ingredients
        self.recipe = recipe

    def get_name(self):
        return self.name

    def get_prep_time(self):
        return self.prep_time

    def get_is_veggie(self):
        return self.is_veggie

    def get_food_type(self):
        return self.food_type

    def get_ingredients(self):
        return self.ingredients

    def get_recipe(self):
        return self.recipe

butternut_squash_soup = Food('Butternut Squash Soup', 45, True, 'soup', 'North African', ['butter squash','onion','carrot','garlic','butter','black pepper','cinnamon','coconut milk'],
    '1. Grill the butter squash, onion, carrot and garlic in the oven until'
    'they get soft and golden on top 2. Put all in blender with'
    'butter and coconut milk. Blend them till they become puree. Then move the content into a pot'
    '. Add coconut milk. Simmer for 5 mintues.')

shirazi_salad = Food('Shirazi Salad', 5, True, 'salad', 'Iranian', ['cucumber', 'tomato', 'onion', 'lemon juice'],
    '1. dice cucumbers, tomatoes and onions 2. put all into a bowl 3. pour lemon juice 3. add salt 4. Mixed them thoroughly')

homemade_beef_sausage = Food('Homemade Beef Sausage', 60, False, 'deli', 'All', ['sausage casing', 'regular ground beef','garlic',\
    'corriander seeds','black pepper seeds','fennel seed','paprika'], '1. In a blender,'
    ' blend corriander seeds, black pepper seeds, fennel seeds and garlic to make'
    'the seasonings 2. In a bowl, mix ground beef with the'
    'seasoning 3. Add all the content to a sausage stuffer. Put the casing on'
    "the stuffer funnel. Rotate the stuffer's handle (or turn it on) to make your yummy sausages!")

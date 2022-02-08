# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

toxic_ingredients = ['sodium nitrate', 'sodium benzoate', 'sodium oxide']
def toxin(ingredients):
    return ingredients in toxic_ingredients
def make_alert_sound():
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    print('made alert sound.')
def make_accept_sound():
    print('***')
    print('Toxin Free')
    print('***')
    print('made acceptance sound')

ingredients = ['sodium benzoate']
if (toxin(ingredients)):
    make_accept_sound()
else:
    make_accept_sound()

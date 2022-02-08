# by Kami Bigdely
# Consolidate conditional expressions

required_ingredients = ['cucumber', 'tomato', 'onion', 'lemon juice']
def dice(ingredients):
    print("diced all ingredients.")
def mix_all(diced_ingredients):
    print("mixed all.")
def add_salt():
    print('added salt.')
def pour(liquid):
    print('poured', liquid + '.',)

def make_shirazi_salad(ingredients):
    if ingredients not in required_ingredients:
        print("Lacks required ingredient(s).")
        return
    dice(ingredients)
    mix_all(ingredients)
    add_salt()
    pour('lemon juice')
    print('Your yummy shirazi salad is ready!')

if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])

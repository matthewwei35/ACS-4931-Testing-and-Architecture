# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def calculate_area_under_graph(graph):   # TODO: Rename this function to reflect what it's doing.
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def get_greatest_value_in_list(list):  # TODO: Rename this function to reflect what it's doing.
    max_value = list[0]
    for value in list:
        if value > max_value:
            max_value = value
    return max_value


numbers = [5, -1, 43, 32, 87, -100]
print(get_greatest_value_in_list(numbers))

############################
def process_words_to_list(sentence):  # TODO: Rename this function to reflect what it's doing.
    words = sentence[0:].split(' ')
    return words

print(process_words_to_list('If you were a vegetable, you`d be a `cute-cumber.'))

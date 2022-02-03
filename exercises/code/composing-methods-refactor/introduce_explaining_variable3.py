# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cooking_criteria_satisfied(time, temperature, pressure, desired_state):
    meat_criteria = time * temperature * pressure * COOKED_CONSTANT
    return desired_state in ['well-done','medium'] and meat_criteria >= WELL_DONE or meat_criteria >= MEDIUM

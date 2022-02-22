import math

T_HALF = 5730
DECAY_CONSTANT = -0.693

# TODO: Write a unit test which feed 0.35 to the function.
# The result should be '8680.34'.
    # - Does the function handle every possible input correctly?
    # - What if the input is zero or negative?
    # - Add the necessary logic to make sure the function handle every possible input properly. Then write a unit test against this special case.

def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14
    in the sample conpared to the amount in living
    tissue (unitless).
    """
    if 0 < carbon_14_ratio < 1:
        return math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF
    else:
        return "Try a decimal between 0 and 1."

def test_carbon_dating():
    carbon_14_ratio = 0.35
    assert get_age_carbon_14_dating(carbon_14_ratio) == 8680.34743633106

def test_carbon_dating_error():
    carbon_14_ratio = -1
    assert get_age_carbon_14_dating(carbon_14_ratio) == "Try a decimal between 0 and 1."

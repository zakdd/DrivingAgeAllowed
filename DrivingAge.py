#https://codechalleng.es/bites/101/

MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    is_allowed = 'is allowed' if age >= MIN_DRIVING_AGE else 'is not allowed'
    print(f'{name} {is_allowed} to drive')

allowed_driving('Zak',23)
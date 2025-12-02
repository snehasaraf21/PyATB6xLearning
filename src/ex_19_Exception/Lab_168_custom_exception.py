class InvalidAgeException(Exception):
    pass

def can_you_drink(age):
    if age <= 18:
        raise InvalidAgeException("Invalid age for drinking")



can_you_drink(17)

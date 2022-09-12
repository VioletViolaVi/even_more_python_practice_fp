def greet(name):
    try:
        if not name:
            raise Exception("Empty string!")
        else:
            return f"Hello {name}!"
    except Exception as error:
        return "Panic!"


def is_bigger(num1, num2):
    if num1 > num2:
        return True
    else:
        return False


def panic(status):
    if status:
        raise Exception("AAAAAAAAAAAAAAAAAAAH!")
    else:
        return None


def extract_allergies(person):
    allergies = person["diet"]["allergies"]
    if len(allergies) > 0:
        return allergies
    else:
        return False

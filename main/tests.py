from django.test import TestCase
import re


def validate_phone(phone):
    return re.match(r"^7[0-9]{10}$", phone)


print(validate_phone('712365478522') == None)



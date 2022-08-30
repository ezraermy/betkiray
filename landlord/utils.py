import datetime
import os 

from random import randint
from unicodedata import category
from .models import Akeray, Category

def new_rent(request, title, location, price, summary, phone):
    akeray = Akeray(title = title, location = location, price = price, summary = summary, phone = phone)

    category_id = str(Category.id)

    akeray.save()

    return category_id




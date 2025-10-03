from app.config import MENU_FILE , IMAGE_URL, MENU_CATEGORY_FILE
from app.utils.read_data import read_data

def get_menu_categories():
    categories = read_data(MENU_CATEGORY_FILE)
    return categories

def get_all_menu_items():
    menu = read_data(MENU_FILE)
    for item in menu:
        item['image'] = f"{IMAGE_URL}/{item['image']}"
    return menu

def get_menu_item_by_category(category:str):
    menu = read_data(MENU_FILE)
    normalize_category = category.replace('-', ' ')
    filter_items = [item for item in menu if item['category'].lower() == normalize_category]
    
    for item in filter_items:
        item['image'] = f"{IMAGE_URL}/{item['image']}"
    
    return filter_items
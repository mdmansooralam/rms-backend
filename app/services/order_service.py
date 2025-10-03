from app.utils.read_data import read_data
from app.config import ORDER_FILE, IMAGE_URL


def get_all_orders():
    orders =  read_data(ORDER_FILE)
    for order in orders:
        for item in order['items']:
            item['image'] = f"{IMAGE_URL}/{item['image']}"
    return orders
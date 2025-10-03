
from app.config import HISTORY_FILE, IMAGE_URL
from app.utils.read_data import read_data


def get_all_history():
    history = read_data(HISTORY_FILE)
    
    for h in history:
        for item in h['items']:
            item['image'] = f"{IMAGE_URL}/{item['image']}"
            
    
    return history
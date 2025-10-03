from app.config import OVERALL_FILE, TRENDING_FILE, REPORT_FILE, TRANSACTION_FILE, INCOME_FILE, IMAGE_URL
from app.utils.read_data import read_data


def get_reports():
    reports = read_data(REPORT_FILE)
    return reports

def get_trending_menu():
    trending_menu = read_data(TRENDING_FILE)
    
    for item in trending_menu:
        item['image'] = f"{IMAGE_URL}/{item['image']}"
        
    return trending_menu

def get_overall():
    overall = read_data(OVERALL_FILE)

    for i in overall:
        i['icon'] = f"{IMAGE_URL}/{i['icon']}"
        
    return overall

def get_trasactions():
    transactions = read_data(TRANSACTION_FILE)

    for t in transactions:
        t['image'] = f"{IMAGE_URL}/{t['image']}"

    return transactions

def get_income():
    income = read_data(INCOME_FILE)
    return income
from app.utils.read_data import read_data
from app.config import BILL_FILE

def get_all_bills():
    bills = read_data(BILL_FILE)
    return bills
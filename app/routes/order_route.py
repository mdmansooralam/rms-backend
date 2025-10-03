from fastapi import APIRouter
from app.services.order_service import get_all_orders


router = APIRouter()



@router.get('/')
def get_orders():
    return get_all_orders()
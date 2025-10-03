from fastapi import APIRouter
from app.services.bill_service import get_all_bills

router = APIRouter()

@router.get('/')
def get_bills():
    return get_all_bills()
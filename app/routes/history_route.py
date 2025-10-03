from fastapi import APIRouter
from app.services.history_service import get_all_history


router = APIRouter()


@router.get('/')
def get_history():
    return get_all_history()
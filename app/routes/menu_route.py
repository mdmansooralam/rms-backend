from fastapi import APIRouter, Depends
from app.services.menu_service import get_all_menu_items, get_menu_categories, get_menu_item_by_category
from app.utils.check_auth import check_auth

router = APIRouter()

@router.get('/categories')
def get_categories():
    return get_menu_categories()

@router.get('/')
def get_menu(auth: None = Depends(check_auth)):
    return get_all_menu_items()

@router.get('/category/{category}')
def get_menu_items(category):
    return get_menu_item_by_category(category=category)
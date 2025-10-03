from fastapi import APIRouter
from app.services.report_service import get_income, get_overall, get_reports, get_trasactions, get_trending_menu


router = APIRouter()


@router.get('/')
def reports():
    return get_reports()

@router.get('/transactions')
def transactions():
    return get_trasactions()

@router.get('/overall')
def overall():
    return get_overall()

@router.get('/income')
def income():
    return get_income()

@router.get('/trending-menu')
def trending_menu():
    return get_trending_menu()
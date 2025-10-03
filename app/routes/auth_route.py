from fastapi import APIRouter, Form, Request, Response
from app.services.auth_service import create_user, signin_user
from app.models.user_model import User



router = APIRouter()


@router.post('/signup')
def signup(user:User):
   return create_user(user=user)

@router.get('/login')
async def login(request : Request, response: Response):
    data = await request.json()
    return signin_user(email=data.get('email'), password=data.get('password'), response=response)

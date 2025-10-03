from app.config import USER_FILE
from app.utils.read_data import read_data
from app.utils.write_data import write_data
from app.utils.upload_file import upload_single_file
from fastapi import HTTPException
import bcrypt
from app.utils.send_token import send_token

def create_user(user):
    users = read_data(USER_FILE)
    
    #checking user already registered with email or not
    for u in users:
        if u['email'] == user.email:
            raise HTTPException(status_code=409, detail='Email already exist')
        
    password_byte = user.password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(password_byte, salt)
    
    user_dict = user.dict()
    user_dict['password'] = hash_password.decode('utf-8')
    
    users.append(user_dict)
    
    write_data(USER_FILE, users)
    
    return user_dict
    
    
def signin_user(email, password, response):
    users = read_data(USER_FILE)

    for user in users:
        if user['email'] == email:
            check_password = bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8'))
            if(check_password):
                del user['password']
                send_token(user['id'], response)
                return user
            
    raise HTTPException(status_code=401, detail="wrong credentials")
            
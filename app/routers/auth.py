from fastapi import APIRouter,Depends,HTTPException,status,Response
from sqlalchemy.orm import Session
from .. import database,schemas,models,utils,oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter(tags=["login"])

@router.post("/login",response_model=schemas.Token)
def login(users_credentials: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == users_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Incorrect email or password")
    if not utils.verify(plain_password = users_credentials.password,hashed_password = user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect email or password")
#   Create tokens
    access_token = oauth2.create_access_token(data={"user_id":user.id})
#   Return tokens
    return {"access_token":access_token,"token_type":"bearer"}




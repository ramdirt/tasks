from typing import Annotated
from dependecy import get_auth_service
from exception import UserNotCorrentPasswordException, UserNotFoundException
from fastapi import APIRouter, status, Depends, HTTPException
from schema import UserCreateSchema, UserLoginSchema
from service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=UserLoginSchema)
async def login(body: UserCreateSchema, auth_service: Annotated[AuthService, Depends(get_auth_service)]):
    
    try:
        return auth_service.login(body.username, body.password)
    
    except UserNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )
    
    except UserNotCorrentPasswordException as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e.detail
        )
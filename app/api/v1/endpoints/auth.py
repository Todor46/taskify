from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["auth"], prefix="/auth")


@router.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return form_data


@router.post("/register")
def register():
    return "Success"

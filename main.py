from fastapi import FastAPI
from app.api.v1 import user_routes, token_routes

'''
    * Demo Project for Healthcare Management System
    Author: Duc Minh Nguyen
    About the project:
        - This project illustrate the authorization system for healthcare - freelance
        - What include in this project 
            + create_access_token (api will check user and then return access token with claims)
        - Project is implemented based on "Clean Architecture"
    Note:
        - No db connection has been made, this will be discussed further with client
'''

app = FastAPI()

# app.include_router(user_routes.router, prefix="/api/v1")

# Demo version 1 of token
app.include_router(token_routes.router, prefix="/api/v1")

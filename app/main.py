from fastapi import FastAPI
from api.v1.endpoints import auth

description = """
A simple production-ready API that serves as a portfolio project\n
Created by: [Todor Konjevic](https://www.linkedin.com/in/todorkonjevic/)
"""

app = FastAPI(title="Taskify", description=description)

app.include_router(auth.router, prefix="/v1")

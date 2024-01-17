# app/api/v1/endpoints/__init__.py
from fastapi import APIRouter

router = APIRouter()

from . import auth, user, attendance  # Import your individual endpoint modules here

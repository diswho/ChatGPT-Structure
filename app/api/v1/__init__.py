# app/__init__.py
# from ./../api.v1 import main as v1_main
from ...api.v1 import main as v1_main
from fastapi import FastAPI

app = FastAPI()

# Include API versions
app.include_router(v1_main.router, prefix="/v1", tags=["v1"])

# from .api.v2 import main as v2_main
# app.include_router(v2_main.router, prefix="/v2", tags=["v2"])

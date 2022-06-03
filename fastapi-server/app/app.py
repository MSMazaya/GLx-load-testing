from fastapi import FastAPI
import controllers


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(controllers.warehouse_router)

    return app

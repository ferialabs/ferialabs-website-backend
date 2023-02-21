from ferialabs.application import fastapi_application


@fastapi_application.get("/hello")
async def hello():
    return {"message": "Hello World"}

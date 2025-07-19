from fastapi import APIRouter

router = APIRouter() # helps create a new router instance

@router.get('/')
def root():
    return {"message": "The Auth service is up and running now"}


@router.get('/test')
def root():
    return {"message": "this is a test route"}
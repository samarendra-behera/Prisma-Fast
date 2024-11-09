from fastapi import APIRouter, Path, Request
from schema import ResponseSchema
from Service.post import PostService
from Model.post import PostCreate, RetrievePost


router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.get('', response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_post():
    result = await PostService.get_all()
    return ResponseSchema(details="Successfully get all data!", result=result)


@router.get("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_by_id_post(post_id:int = Path(..., alias='id')):
    result = await PostService.get_by_id(post_id)
    return ResponseSchema(details="Successfully get by id data!", result=result)


@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_post(create_data:PostCreate):
    await PostService.create(create_data)
    return ResponseSchema(details="Successfully created data!")


@router.delete("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_post(post_id:int = Path(..., alias="id")):
    await PostService.delete(post_id)
    return ResponseSchema(details="Successfully delete data!")


@router.put("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_post(post_id:int = Path(..., alias='id'), *, update_form:PostCreate):
    await PostService.update(post_id, update_form)
    return ResponseSchema(details="Successfully updated data!")
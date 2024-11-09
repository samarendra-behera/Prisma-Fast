from Model.post import PostCreate
from Repository.post import PostRepository


class PostService:

    @staticmethod
    async def get_all():
        return await PostRepository.get_all()


    @staticmethod
    async def create(data:PostCreate):
        return await PostRepository.create(data)


    @staticmethod
    async def get_by_id(post_id:int):
        return await PostRepository.get_by_id(post_id)


    @staticmethod
    async def delete(post_id:int):
        return await PostRepository.delete(post_id)


    @staticmethod
    async def update(post_id:int, data:PostCreate):
        return await PostRepository.update(post_id, data)
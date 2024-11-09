from Model.post import PostCreate, RetrievePost
from Config.Connection import prisma_connection


class PostRepository:

    @staticmethod
    async def get_all():
        return await prisma_connection.prisma.post.find_many()


    @staticmethod
    async def create(post:PostCreate):
        return await prisma_connection.prisma.post.create({
            "title": post.title,
            "content": post.content,
            "description": post.description
        })


    @staticmethod
    async def get_by_id(post_id:int):
        return await prisma_connection.prisma.post.find_first(where={"id": post_id})


    @staticmethod
    async def delete(post_id:int):
        return await prisma_connection.prisma.post.delete(where={"id": post_id})


    @staticmethod
    async def update(post_id:int , post:PostCreate):
        return await prisma_connection.prisma.post.update(where={"id": post_id}, data={
            "title":post.title,
            "content": post.content,
            "description": post.description
        })


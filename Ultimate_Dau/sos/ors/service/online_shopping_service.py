from ..Dau.online_shopping_dao import Online_ShoppingDAO
from ..service.base_service import BaseService


class Online_ShoppingService(BaseService):

    def get_dao(self):
        return Online_ShoppingDAO()

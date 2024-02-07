import abc

from orders.domain.model import product


class ProductRepository(abc.ABC):
    @abc.abstractmethod
    def get_product(self, product_id: str) -> product.Product:
        pass

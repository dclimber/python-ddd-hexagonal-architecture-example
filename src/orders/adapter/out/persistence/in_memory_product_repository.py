from orders.domain.model import product
from orders.domain.port.out import i_product_repository


class InMemoryProductRepository(i_product_repository.ProductRepository):
    def get_product(self, product_id: str) -> product.Product:
        return product.Product(product_id, "pizza")

from orders.domain.model import customer, product
from orders.domain.port.out import (
    i_customer_repository,
    i_order_repository,
    i_product_repository,
)


class Order:
    __order_id: str
    __customer_repository: i_customer_repository.CustomerRepository
    __product_repository: i_product_repository.ProductRepository
    __order_repository: i_order_repository.OrderRepository
    __product: product.Product
    __customer: customer.Customer

    def __init__(
        self,
        order_id: str,
        customer_repository: i_customer_repository.CustomerRepository,
        product_repository: i_product_repository.ProductRepository,
        order_repository: i_order_repository.OrderRepository,
    ) -> None:
        self.__order_id = order_id
        self.__customer_repository = customer_repository
        self.__product_repository = product_repository
        self.__order_repository = order_repository

    def look_up_customer(self, customer_id: str) -> None:
        self.__customer = self.__customer_repository.get_customer(customer_id)

    def loop_up_product(self, product_id: str) -> None:
        self.__product = self.__product_repository.get_product(product_id)

    def create_order(self) -> bool:
        if not self.__customer.is_number_order_allowed():
            return False

        return self.__order_repository.create_order(
            self.__order_id,
            self.__customer,
        )

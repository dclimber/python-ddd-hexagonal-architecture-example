from orders.domain.model import order
from orders.domain.port.inp import i_create_order
from orders.domain.port.out import (
    i_customer_repository,
    i_order_repository,
    i_product_repository,
)


class CreateOrderImpl(i_create_order.CreateOrder):
    __customer_repository: i_customer_repository.CustomerRepository
    __product_repository: i_product_repository.ProductRepository
    __order_repository: i_order_repository.OrderRepository

    def __init__(
        self,
        customer_repository: i_customer_repository.CustomerRepository,
        product_repository: i_product_repository.ProductRepository,
        order_repository: i_order_repository.OrderRepository,
    ) -> None:
        self.__customer_repository = customer_repository
        self.__order_repository = order_repository
        self.__product_repository = product_repository

    def create_order(self, order_id: str, customer_id: str, product_id: str) -> bool:
        new_order: order.Order = order.Order(
            order_id,
            self.__customer_repository,
            self.__product_repository,
            self.__order_repository,
        )
        new_order.look_up_customer(customer_id)
        new_order.loop_up_product(product_id)
        return new_order.create_order()

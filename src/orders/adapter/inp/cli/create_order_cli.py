from orders.adapter.inp import request as request_module
from orders.adapter.out import response as response_module
from orders.application.port.inp import (
    create_order_port_implementaton,
    i_create_order_port,
    input_dto,
)
from orders.domain.port.out import (
    i_customer_repository,
    i_order_repository,
    i_product_repository,
)


class CreateOrderCLIAdapter:
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

    def create_order(self, request: request_module.Request) -> response_module.Response:
        new_input: input_dto.InputDTO = input_dto.InputDTO(
            request.order_id,
            request.customer_id,
            request.product_id,
        )

        adapter: i_create_order_port.CreateOrderPort = (
            create_order_port_implementaton.CreateOrderPortImpl(
                self.__customer_repository,
                self.__product_repository,
                self.__order_repository,
            )
        )
        result: response_module.Response = response_module.Response(
            adapter.create_order_port(new_input).result
        )
        return result

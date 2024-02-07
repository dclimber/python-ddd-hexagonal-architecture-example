from orders.application.port.inp import i_create_order_port, input_dto
from orders.application.port.out import output_dto
from orders.application.service import create_order_implementation
from orders.domain.port.inp import i_create_order
from orders.domain.port.out import (
    i_customer_repository,
    i_order_repository,
    i_product_repository,
)


class CreateOrderPortImpl(i_create_order_port.CreateOrderPort):
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

    def create_order_port(
        self,
        dto: input_dto.InputDTO,
    ) -> output_dto.OutputDTO:
        create_order: i_create_order.CreateOrder = (
            create_order_implementation.CreateOrderImpl(
                self.__customer_repository,
                self.__product_repository,
                self.__order_repository,
            )
        )
        result: bool = create_order.create_order(
            dto.order_id, dto.customer_id, dto.product_id
        )
        output: output_dto.OutputDTO
        if result:
            output = output_dto.OutputDTO("Creation successful")
        else:
            output = output_dto.OutputDTO("Creation failed")
        return output

from orders.adapter.inp import request
from orders.adapter.inp.cli import create_order_cli
from orders.adapter.out import response
from orders.adapter.out.persistence import (
    in_memory_customer_repository,
    in_memory_order_repository,
    in_memory_product_repository,
)
from orders.domain.port.out import (
    i_customer_repository,
    i_order_repository,
    i_product_repository,
)


def main() -> None:
    customer_repository: i_customer_repository.CustomerRepository = (
        in_memory_customer_repository.InMemoryCustomerRepository()
    )
    product_repository: i_product_repository.ProductRepository = (
        in_memory_product_repository.InMemoryProductRepository()
    )
    order_repository: i_order_repository.OrderRepository = (
        in_memory_order_repository.InMemoryOrderRepository()
    )
    req: request.Request = request.Request("0-1234", "1234", "P-24244")

    app: create_order_cli.CreateOrderCLIAdapter = (
        create_order_cli.CreateOrderCLIAdapter(
            customer_repository,
            product_repository,
            order_repository,
        )
    )

    print("Before creating an order")

    resp: response.Response = app.create_order(req)

    print(f"After creating an order, the result is: {resp.result}")


if __name__ == "__main__":
    main()

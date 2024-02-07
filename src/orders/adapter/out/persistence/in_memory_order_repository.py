from orders.domain.model import customer
from orders.domain.port.out import i_order_repository


class InMemoryOrderRepository(i_order_repository.OrderRepository):
    def create_order(self, order_id: str, customer: customer.Customer) -> bool:
        print(f"Creating order {order_id} to customer {customer.customer_id}")
        return True

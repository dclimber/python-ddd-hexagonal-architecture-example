from orders.domain.model import customer
from orders.domain.port.out import i_customer_repository


class InMemoryCustomerRepository(i_customer_repository.CustomerRepository):
    def get_customer(self, customer_id: str) -> customer.Customer:
        return customer.Customer(customer_id, "DDD", 0, "educative", 1)

import abc

from orders.domain.model import customer


class CustomerRepository(abc.ABC):
    @abc.abstractmethod
    def get_customer(self, customer_id: str) -> customer.Customer:
        pass

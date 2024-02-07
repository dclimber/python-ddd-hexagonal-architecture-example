import abc

from orders.domain.model import customer


class OrderRepository(abc.ABC):
    @abc.abstractmethod
    def create_order(self, order_id: str, customer: customer.Customer) -> bool:
        pass

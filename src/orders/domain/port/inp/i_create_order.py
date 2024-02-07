import abc


class CreateOrder(abc.ABC):
    @abc.abstractmethod
    def create_order(
        self,
        order_id: str,
        customer_id: str,
        product_id: str,
    ) -> bool:
        pass

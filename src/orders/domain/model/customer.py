import dataclasses

from orders.domain.model.address import Address


@dataclasses.dataclass(init=False)
class Customer:
    """Represents a customer with orders and an address.

    Attributes:
        customer_id (str): Unique identifier for the customer.
        customer_name (str): Full name of the customer.
        orders_in_progress (int): Number of orders the customer currently has in progress.
        address (Address): Postal address of the customer.
    """

    customer_id: str
    customer_name: str
    orders_in_progress: int
    address: Address

    def __init__(
        self,
        customer_id: str,
        customer_name: str,
        order_in_progress: int,
        street_name: str,
        street_number: int,
    ) -> None:
        """Initializes a Customer object with provided details and address.

        Args:
            customer_id (str): Unique identifier for the customer.
            customer_name (str): Full name of the customer.
            orders_in_progress (int): Number of orders the customer currently has in progress.
            street_name (str): The name of the customer's street.
            street_number (int): The number on the customer's street.
        """
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.orders_in_progress = order_in_progress
        self.address = Address(street_name, street_number)

    def is_number_order_allowed(self) -> bool:
        """Determines if the customer is allowed to place another order based on their current order status.

        Returns:
            bool: True if the customer has no orders in progress, False otherwise.
        """
        return self.orders_in_progress == 0

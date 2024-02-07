import dataclasses


@dataclasses.dataclass
class InputDTO:
    order_id: str
    customer_id: str
    product_id: str

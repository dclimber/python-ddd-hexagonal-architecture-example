import dataclasses


@dataclasses.dataclass(frozen=True)
class Request:
    order_id: str
    customer_id: str
    product_id: str

import dataclasses


@dataclasses.dataclass(frozen=True)
class Product:
    """Product is an Entity."""

    product_id: str
    product_name: str

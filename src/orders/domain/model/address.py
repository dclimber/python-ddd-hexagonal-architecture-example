import dataclasses


@dataclasses.dataclass(frozen=True)
class Address:
    """Value object that represents a postal address.

    Attributes:
        street_name (str): The name of the street.
        street_number (int): The number on the street.
    """

    street_name: str
    streer_number: int

import dataclasses


@dataclasses.dataclass(frozen=True)
class Response:
    result: str

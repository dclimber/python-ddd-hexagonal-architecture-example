import abc

from orders.application.port.inp import input_dto
from orders.application.port.out import output_dto


class CreateOrderPort(abc.ABC):
    @abc.abstractmethod
    def create_order_port(
        self,
        dto: input_dto.InputDTO,
    ) -> output_dto.OutputDTO:
        pass

from core.enums.base_enum import BaseEnum


class TransmissionTypes(BaseEnum):
    A = 'Automatic'
    M = 'Manual'


class EngineTypes(BaseEnum):
    GAS = 'Gas engine'
    DIESEL = 'Diesel engine'
    ELECTRIC = 'Electric engine'


class Colors(BaseEnum):
    WHITE = 'White'
    RED = 'Red'
    BLACK = 'Black'
    GREEN = 'Green'
    PINK = 'Pink'
    ORANGE = 'Orange'
    YELLOW = 'Yellow'
    PURPLE = 'Purple'
    BLUE = 'Blue'
    GREY = 'Grey'

from core.enums.base_enum import BaseEnum


class TransmissionTypes(BaseEnum):
    A = 'Automatic'
    M = 'Manual'


class EngineTypes(BaseEnum):
    GAS = 'Gas engine'
    DIESEL = 'Diesel engine'
    ELECTRIC = 'Electric engine'

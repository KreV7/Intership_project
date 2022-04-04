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


ENGINE_POWER = [1200, 1400, 1500, 1600, 1800, 2000, 2400, 2500, 3000]

CARS = {'Audi': ['A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'Q3', 'Q5', 'Q7', 'Q8'],
        'BMW': ['2 серия', '3 серия', '4 серия', '5 серия', '6 серия', '7 серия', '8 серия', 'i3', 'iX',
                'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'Z4'],
        'Cadillac': ['XT6'],
        'Changan': ['CS35 Plus', 'CS55', 'CS75 FL'],
        'Chery': ['Tiggo 4', 'Tiggo 7 Pro', 'Tiggo 8', 'Tiggo 8 Pro'],
        'Chevrolet': ['Cobalt', 'Nexia', 'Spark'],
        'Citroen': ['Berlingo', 'C3 Aircross', 'C4', 'C5 Aircross', 'SpaceTourer'],
        'Geely': ['Atlas Pro', 'Coolray', 'Tugella'],
        'Great Wall': ['GWM Poer'],
        'Haval': ['F7', 'F7 X', 'H9', 'Jolion'],
        'Hyundai': ['Accent', 'Creta', 'Palisade', 'Santa Fe', 'Sonata', 'Tucson'],
        'Jeep': ['Compass', 'Grand Cherokee', 'Renegade', 'Wrangler'],
        'Kia': ['Rio', 'Seltos', 'Sorento', 'Sportage'],
        'LADA (ВАЗ)': ['Granta', 'Largus', 'Niva Legend', 'Niva Travel', 'Vesta', 'XRAY '],
        'Lexus': ['ES', 'GX', 'LC', 'LS', 'LX', 'NX', 'RX', 'UX'],
        'Maserati': ['Levante'],
        'MINI': ['Countryman', 'Hatch'],
        'Nissan': ['Murano', 'Qashqai', 'Terrano', 'X-Trail'],
        'Opel': ['Astra', 'Combo Cargo', 'Combo Life', 'Corsa', 'Crossland', 'Grandland X', 'Insignia',
                 'Vivaro', 'Zafira Life'],
        'Peugeot': ['2008', '3008', '408', '5008', 'Boxer', 'Expert', 'Partner', 'Traveller'],
        'Subaru': ['Forester', 'Outback', 'XV'],
        'Tesla': ['Model 3', 'Model S', 'Model X'],
        'Toyota': ['Alphard', 'C-HR', 'Camry', 'Corolla', 'Fortuner', 'Highlander', 'Hilux', 'Land Cruiser',
                   'Land Cruiser Prado', 'RAV4'],
        'Volkswagen': ['Polo', 'Taos', 'Tiguan'],
        'Volvo': ['S60', 'S90', 'V60', 'V90', 'XC40', 'XC60', 'XC90'],
        'УАЗ': ['Hunter', 'Patriot', 'Pickup']}

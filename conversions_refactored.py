class ConversionNotPossibleException(Exception):
    pass

def convert(fromUnit: str, toUnit: str, value: float) -> float:
    temperature_units = {'Celsius', 'Fahrenheit', 'Kelvin'}
    distance_units = {'Miles', 'Yards', 'Meters'}

    def convertTemperature(from_unit, to_unit, value):
        if from_unit == 'Celsius':
            if to_unit == 'Fahrenheit':
                return value * 9/5 + 32
            elif to_unit == 'Kelvin':
                return value + 273.15
        elif from_unit == 'Fahrenheit':
            if to_unit == 'Celsius':
                return (value - 32) * 5/9
            elif to_unit == 'Kelvin':
                return (value - 32) * 5/9 + 273.15
        elif from_unit == 'Kelvin':
            if to_unit == 'Celsius':
                return value - 273.15
            elif to_unit == 'Fahrenheit':
                return (value - 273.15) * 9/5 + 32
        raise ConversionNotPossibleException(f"Cannot convert from {from_unit} to {to_unit}")

    def convertDistance(from_unit, to_unit, value):
        conversion_factors = {
            ('Miles', 'Meters'): 1609.34,
            ('Yards', 'Meters'): 0.9144,
            ('Meters', 'Miles'): 1/1609.34,
            ('Meters', 'Yards'): 1/0.9144,
            ('Miles', 'Yards'): 1760,
            ('Yards', 'Miles'): 1/1760
        }
        if from_unit == to_unit:
            return value
        try:
            return value * conversion_factors[(from_unit, to_unit)]
        except KeyError:
            raise ConversionNotPossibleException(f"Cannot convert from {from_unit} to {to_unit}")

    if fromUnit in temperature_units and toUnit in temperature_units:
        return convertTemperature(fromUnit, toUnit, value)
    elif fromUnit in distance_units and toUnit in distance_units:
        return convertDistance(fromUnit, toUnit, value)
    else:
        raise ConversionNotPossibleException(f"Cannot convert from {fromUnit} to {toUnit}")

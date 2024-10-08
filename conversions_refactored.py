class ConversionNotPossibleException(Exception):
    pass

def convert(fromUnit: str, toUnit: str, value: float) -> float: # convert will be used to see what could be handle to be used 
    temperature_units = {'Celsius', 'Fahrenheit', 'Kelvin'}
    distance_units = {'Miles', 'Yards', 'Meters'}

    def convertTemperature(from_unit, to_unit, value): # over here we will use it to convert the temp value 
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
        raise ConversionNotPossibleException(f"Cannot convert from {from_unit} to {to_unit}") # if from_unit and to_unit is unable to be supported then we will raise a ca ConversionNotPossibleException

    def convertDistance(from_unit, to_unit, value): # using convertDistance to idnetify the value between the units such as Miles, Meters, and even yards 
        conversion_factors = {
            ('Miles', 'Meters'): 1609.34,
            ('Yards', 'Meters'): 0.9144,
            ('Meters', 'Miles'): 1/1609.34,
            ('Meters', 'Yards'): 1/0.9144,
            ('Miles', 'Yards'): 1760,
            ('Yards', 'Miles'): 1/1760
        }
        if from_unit == to_unit: 
            return value # the function ability to return value 
        try:
            return value * conversion_factors[(from_unit, to_unit)] # attempting to find from_unit, to unit
        except KeyError:
            raise ConversionNotPossibleException(f"Cannot convert from {from_unit} to {to_unit}") # if not found it wil raise ConversionNotPossibleException

    if fromUnit in temperature_units and toUnit in temperature_units:
        return convertTemperature(fromUnit, toUnit, value)
    elif fromUnit in distance_units and toUnit in distance_units:
        return convertDistance(fromUnit, toUnit, value)
    else:
        raise ConversionNotPossibleException(f"Cannot convert from {fromUnit} to {toUnit}")

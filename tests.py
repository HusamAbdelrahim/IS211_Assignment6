from conversions import (
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit,
)

# using log_test_result to print out the format 

def log_test_result(conversion_function_name, input_value, result, expected_result, test_status):
    print(f"{conversion_function_name}({input_value}) -> Result: {result}, Expected: {expected_result} -> {test_status}") # will be used to pass input, get the result, and determine if pass or fail 

def test_convertCelsiusToKelvin(): # reviewing the cases in tuple list
    test_cases = [
        (0.0, 273.15),
        (100.0, 373.15),
        (-40.0, 233.15),
        (25.0, 298.15),
        (-273.15, 0.0)
    ]
    for celsius, expected_kelvin in test_cases: #loop will occur through the test cases presented 
        result = convertCelsiusToKelvin(celsius)
        try:
            assert round(result, 2) == round(expected_kelvin, 2) # checking attempt
            log_test_result("convertCelsiusToKelvin", celsius, result, expected_kelvin, "Passed")
        except AssertionError: # if test fail it Assertion error rasies 
            log_test_result("convertCelsiusToKelvin", celsius, result, expected_kelvin, "Failed")

def test_convertCelsiusToFahrenheit(): # review cases in the tupe list 
    test_cases = [
        (0.0, 32.0),
        (100.0, 212.0),
        (-40.0, -40.0),
        (25.0, 77.0),
        (-273.15, -459.67)
    ]
    for celsius, expected_fahrenheit in test_cases: #loop will occur 
        result = convertCelsiusToFahrenheit(celsius)
        try:
            assert round(result, 2) == round(expected_fahrenheit, 2) #checking attempt
            log_test_result("convertCelsiusToFahrenheit", celsius, result, expected_fahrenheit, "Passed")
        except AssertionError: # if fail will raise assertion error 
            log_test_result("convertCelsiusToFahrenheit", celsius, result, expected_fahrenheit, "Failed")

def test_convertFahrenheitToCelsius(): # reviewing the cases in the tuple list 
    test_cases = [
        (32.0, 0.0),
        (212.0, 100.0),
        (-40.0, -40.0),
        (77.0, 25.0),
        (-459.67, -273.15)
    ]
    for fahrenheit, expected_celsius in test_cases: # loop will occur in the cases 
        result = convertFahrenheitToCelsius(fahrenheit)
        try:
            assert round(result, 2) == round(expected_celsius, 2) # checking the attempt 
            log_test_result("convertFahrenheitToCelsius", fahrenheit, result, expected_celsius, "Passed")
        except AssertionError: # if fail it will raise an Assertion Error
            log_test_result("convertFahrenheitToCelsius", fahrenheit, result, expected_celsius, "Failed")

def test_convertFahrenheitToKelvin(): # loop will occur in the cases 
    test_cases = [
        (32.0, 273.15),
        (212.0, 373.15),
        (-40.0, 233.15),
        (77.0, 298.15),
        (-459.67, 0.0)
    ]
    for fahrenheit, expected_kelvin in test_cases:
        result = convertFahrenheitToKelvin(fahrenheit)
        try:
            assert round(result, 2) == round(expected_kelvin, 2)
            log_test_result("convertFahrenheitToKelvin", fahrenheit, result, expected_kelvin, "Passed")
        except AssertionError:
            log_test_result("convertFahrenheitToKelvin", fahrenheit, result, expected_kelvin, "Failed")

def test_convertKelvinToCelsius(): # loop will occur in the cases 
    test_cases = [
        (273.15, 0.0),
        (373.15, 100.0),
        (233.15, -40.0),
        (298.15, 25.0),
        (0.0, -273.15)
    ]
    for kelvin, expected_celsius in test_cases:
        result = convertKelvinToCelsius(kelvin)
        try:
            assert round(result, 2) == round(expected_celsius, 2) # checking the attempt 
            log_test_result("convertKelvinToCelsius", kelvin, result, expected_celsius, "Passed")
        except AssertionError: # if fail it will raise an Assertion Error
            log_test_result("convertKelvinToCelsius", kelvin, result, expected_celsius, "Failed")

def test_convertKelvinToFahrenheit(): # loop will occur in the cases 
    test_cases = [
        (273.15, 32.0),
        (373.15, 212.0),
        (233.15, -40.0),
        (298.15, 77.0),
        (0.0, -459.67)
    ]
    for kelvin, expected_fahrenheit in test_cases:
        result = convertKelvinToFahrenheit(kelvin)
        try:
            assert round(result, 2) == round(expected_fahrenheit, 2) # checking the attempt will showcase the reults are true
            log_test_result("convertKelvinToFahrenheit", kelvin, result, expected_fahrenheit, "Passed")
        except AssertionError: # if fail it will raise an Assertion Error
            log_test_result("convertKelvinToFahrenheit", kelvin, result, expected_fahrenheit, "Failed")

if __name__ == '__main__':
    test_convertCelsiusToKelvin()
    test_convertCelsiusToFahrenheit()
    test_convertFahrenheitToCelsius()
    test_convertFahrenheitToKelvin()
    test_convertKelvinToCelsius()
    test_convertKelvinToFahrenheit()
    print("All tests completed.")

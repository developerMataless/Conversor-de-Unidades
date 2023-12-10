# Funções de conversão de temperatura

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_para_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

# Funções de conversão de medidas de comprimento

def metros_para_quilometros(metros):
    return metros / 1000

def quilometros_para_metros(quilometros):
    return quilometros * 1000

def metros_para_centimetros(metros):
    return metros * 100

def quilometros_para_centimetros(quilometros):
    return quilometros * 100000

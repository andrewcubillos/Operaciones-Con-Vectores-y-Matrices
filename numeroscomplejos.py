from sys import stdin
import math


def suma(numero1, numero2):
    re = numero1[0] + numero2[0]
    im = numero1[1] + numero2[1]
    return (re, im)


def producto(numero1, numero2):
    re2 = (numero1[0] * numero2[0]) - (numero1[1] * numero2[1])
    im2 = (numero1[1] * numero2[0]) + (numero1[0] * numero2[1])
    return (re2, im2)


def resta(numero1, numero2):
    re1 = numero1[0] - numero2[0]
    im1 = numero1[1] - numero2[1]
    return (re1, im1)


def division(numero1, numero2):
    deno = ((numero2[0]) ** 2) + ((numero2[1]) ** 2)
    num1 = (numero1[0] * numero2[0]) + (numero1[1] * numero2[1])
    num2 = (numero2[0] * numero1[1]) - (numero1[0] * numero2[1])
    return (num1 / deno), (num2 / deno)


def modulo(numero1):
    mod1 = ((numero1[0] ** 2) + (numero1[1] ** 2)) ** (1 / 2)

    return mod1


def conjugado(numero1):
    con1 = (-1 * numero1[1])

    return (numero1[0],con1)


def polar(numero1):
    po11 = ((numero1[0] ** 2) + (numero1[1] ** 2)) ** (1 / 2)
    po12 = math.atan(numero1[1] / numero1[0])
    
    return (po11,po12) 


def fase(numero1):
    if (numero1[0] < 0 and numero1[1] > 0):
        fas1 = math.pi + (math.atan(numero1[1] / numero1[0]))
    elif (numero1[0] < 0 and numero1[1] < 0):
        fas1 = (math.atan(numero1[1] / numero1[0])) - math.pi
    else:
        fas1 = (math.atan(numero1[1] / numero1[0]))

    

    return fas1

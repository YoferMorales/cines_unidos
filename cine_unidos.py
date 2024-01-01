while True:
    # entradas de informacion
    edad=int(input('edad del cliente: \n'))
    dia_semana=str(input('que dia de la semana es: \n'))
    hora=str(input('eligir la hora de la funcion (1=1pm, 3=3pm, 5=5pm, 7=7pm y 9=9pm)\n'))

    # procesos de informacion
    costo=0
    match hora:
        case '1':
            costo=1
        case '3':
            costo=2
        case '5':
            costo=3
        case '7' | '9':
            costo=4

    if edad<2:
        descuento_edad=100
    elif edad>70:
        descuento_edad=100
    elif edad<10:
        descuento_edad=50
    else:
        descuento_edad=0

    if dia_semana.upper() == 'LUNES':
        descuento_dia=50
    else:
        descuento_dia=0
    
    descuento=descuento_dia+descuento_edad

    if descuento>0:
        costo_total=costo-(costo*(descuento/descuento))
    else:
        costo_total=costo

    if costo_total<0:
        total=0
    else:
        total=costo_total

    # salidas de informacion 
    print(f'''recibo
            funcion de las {hora}pm
            dia de la semana: {dia_semana.upper()}
            obtienes un descuento del {descuento}%
            total a pagar es: {total} dolares\n\n''')
    print('Precione "ENTER" para continuar')
    resp=input()
    if resp==".":
        continue

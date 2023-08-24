horas_trabajadas = float(input("Ingresa el número de horas trabajadas: "))
tarifa_por_hora = float(input("Ingresa la tarifa por hora: "))

if horas_trabajadas <= 40:
    salario_bruto = horas_trabajadas * tarifa_por_hora
else:
    horas_normales = 40
    horas_extras = horas_trabajadas - 40
    salario_bruto = (horas_normales * tarifa_por_hora) + (horas_extras * tarifa_por_hora * 1.5)

    print("El salario bruto es:", salario_bruto)
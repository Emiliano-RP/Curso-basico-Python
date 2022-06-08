#if = Si ... (primero crear una variable)
Calificación = input("Introduce tu calificación de la certificación AZ-900 Fundamentals: ")
Calificación = int(Calificación)
# Preguntamos si la calificación es mayor a 700
if Calificación < 700 :
    print("Vesss, por no estudiar, BURRO") # Si es menor a 700, imprime esto
elif Calificación == 700 :  # Si es igual a 700, imprime esto
    print("Apenas panzaste")
elif Calificación > 1000 :
    print("Mientesss, no puedes sacar más de 1000")
else :
    print("Felicidades, pasa por tu certificado crack") # Si no se cumple el if anterior, entonces pasa esta linea de else
# Verificador de mayoria de edad
Edad = input("Introduce tu edad: ")
Edad = int(Edad)
if Edad >= 18 and Edad <= 100 :
    print("Bienvenido al mamitas")
elif Edad > 100 :
    print("Si vienes acompañado de tus abuelitos, si te podemos fíar")
elif Edad < 0 :
    print("Ni que fueras viajero del tiempo we")
else :
    print("No puedes llevarte esos cigarros chaval")
# En Python no hay switch case
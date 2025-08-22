#Tu misión: desarrollar un programa que permita a un estudiante ingresar sus 5 calificaciones y 
#obtenga como resultado si aprobó, está en recuperación o reprobó. Este programa será integrado 
#en nuestra nueva plataforma de aprendizaje en línea. 
#Contenido 
#Requisitos del programa 
#1. El programa debe solicitar al usuario que ingrese por consola el valor de 5 calificaciones. 
#2. El programa debe calcular el promedio de las calificaciones ingresadas. 
#3. Si el promedio es mayor o igual a 60, el programa debe imprimir "Aprobado". 
#4. Si el promedio esta entre 40 y 59, el programa debe imprimir "En recuperación" 
#5. Si el promedio es menor a 40, el programa debe imprimir "Reprobado".













calificacion1 = int(input('ingresa la calificacion 1'))
calificacion2 = int(input('ingresa la calificacion 2'))
calificacion3 = int(input('ingresa la calificacion 3'))
calificacion4 = int(input('ingresa la calificacion 4'))
calificacion5 = int(input('ingresa la calificacion 5'))



promedio = (calificacion1+calificacion2+calificacion3+calificacion4+calificacion5)/5
print(f'EL PROMDEIO ES {promedio}')




if promedio >= 60:
    print('Aprobado')

elif promedio >= 40 and  promedio < 59:
        print(' En recuperación')  

else:
      print('Reprobo')

        

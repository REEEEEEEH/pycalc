#Definir las Funciones
def add(x, y):
    #Definir la Suma
 
   return x + y 
def subtract(x, y):
    #Definir la Resta
   
   return x - y 
def multiply(x, y):
    #Definir la Multiplicacion
   
   return x * y 
def divide(x, y):
    # Definir la Division
     
   return x / y  
# Seleccionar 
print("Selecciona una Operacion...")  
print("1.Sumar")  
print("2.Restar")  
print("3.Multiplicar")  
print("4.Dividir")  
  
choice = input("Qué tipo de operacion desear realizar? (1/2/3/4):")  
  
num1 = int(input("Selecciona tu primer numero: "))  
num2 = int(input("Selecciona tu segundo numero: "))  
#Definir las Acciones   
if choice == '1':  
   print(num1,"+",num2,"=", add(num1,num2))  
  
elif choice == '2':  
   print(num1,"-",num2,"=", subtract(num1,num2))  
  
elif choice == '3':  
   print(num1,"*",num2,"=", multiply(num1,num2))  
elif choice == '4':  
   print(num1,"/",num2,"=", divide(num1,num2))  
else:  
   print("Error! Intentálo de Nuevo...")  
   end
   
  #@idiol

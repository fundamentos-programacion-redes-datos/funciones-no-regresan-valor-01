"""

def obtenerMensaje():
    // instucciones 
    // instucciones 
    pass

if __name__ == "__main__":


"""
# Importa el módulo datetime para manejar fechas y obtener el año actual
import datetime

# Define un procedimiento (función sin retorno) en Python
def generar_reporte():
    """
    Procedimiento que recopila datos de empleados y calcula su edad
    en función del año de nacimiento ingresado.
    """
    mensaje_final = ""  # Almacena los datos ingresados por el usuario
    bandera = True  # Controla la ejecución del bucle while para permitir múltiples ingresos de datos

    # Inicia un bucle para ingresar información de empleados
    while bandera:
        # Captura el nombre y apellido del empleado
        nombre = input("Ingrese nombre de empleado: ")
        apellido = input("Ingrese apellido de empleado: ")

        # Captura y convierte la entrada del año de nacimiento a entero
        anio_nacimiento = input("Ingrese año de nacimiento de empleado: ")
        anio_nacimiento = int(anio_nacimiento)  # Convierte la entrada a entero

        # Calcula la edad utilizando datetime.datetime.now().year
        # Obtiene el año actual y se resta el año de nacimiento
        edad = datetime.datetime.now().year - anio_nacimiento

        # Acumula los datos en un string formateado
        mensaje_final = f"{mensaje_final}Nombre: {nombre}\n" \
                        f"Apellido: {apellido}\n" \
                        f"Edad: {edad}\n" \
                        f"----------||||--------\n"

        # Solicita al usuario si desea continuar o salir del ciclo
        opcion = input("Ingrese 1 si desea salir del ciclo: ")
        opcion = int(opcion)  # Convierte la entrada a entero

        # Si el usuario ingresa "1", la bandera se cambia a False y el ciclo termina
        if opcion == 1:
            bandera = False

    # Muestra en pantalla el mensaje final con todos los datos ingresados
    print(mensaje_final)
    
    # Este procedimiento no utiliza "return", ya que solo ejecuta una tarea
    # sin devolver un valor explícito. En Python, esto significa que retorna None por defecto


# Define el punto de entrada principal del script
# Garantiza que el código dentro de este bloque solo se ejecute si el script
# es ejecutado directamente y no si se importa como módulo en otro archivo
if __name__ == "__main__":
    #
    # Llama al procedimiento (que en Python se define como una función sin retorno)
    # No es necesario recibir su valor en una variable, ya que no devuelve datos
    generar_reporte()

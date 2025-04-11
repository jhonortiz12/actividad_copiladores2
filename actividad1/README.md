## jhon esteban ortiz pascuaza
## ejercicio1 

- creamos la carpeta actividad1
- instalamos antlr4
- creamos una carpeta llamada csv.g4 
- Define cómo se estructura un archivo CSV: tiene un encabezado y varias filas, separadas por comas. También define qué es un campo de texto, uno entre comillas y uno vacío.
- ejecutamos el comando antlr4 -Dlanguage=Python3 CSV.g4 para generar el código fuente necesario para analizar archivos CSV en Python.
- creamos una carpeta llamada CSVListenerCustom.py y le pagamos el codigo, esto funciona extiende el CSVListener para capturar la información mientras se recorre el archivo CSV
- creamos un archivo llamado main.py y pegamos el codigo esto sirve para Es el punto de entrada del programa. Lee el archivo CSV, lanza el parser y llama al CSVLoader para procesar los datos
- agremamos un archivo llamado actividad1.csv y le pagamos estos datos 
 Mes,Cantidad
Enero,"$1,000"
Febrero,"$2,000"
Enero,"$1,000"
Marzo,""
Abril,"$3,000"
Enero,"$1,000"
- ahora ejecutamos el programa  con el comando "python3 main.py actividad1.csv" 
- nos dio este resultado 

Estadísticas para columna 'Cantidad':
• 1000
• 2000
• 1000
• 
• 3000
• 1000

Conteo de meses:
Enero: 3
Febrero: 1
Marzo: 1
Abril: 1

Filas duplicadas: 2
Campos 'Cantidad' vacíos o mal formateados: 1

Montos totales por mes:
Enero: 3000.0
Febrero: 2000.0
Abril: 3000.0
- analisis La columna "Cantidad" contiene 6 valores, de los cuales:

3 son iguales a 1000, lo cual sugiere una posible repetición de datos.

1 valor está vacío, indicando datos incompletos o mal ingresados.

El resto son valores válidos (2000 y 3000)

- Hay más datos asociados a Enero que a cualquier otro mes.

Esto puede indicar:

Mayor actividad en ese mes.

- El sistema detectó 2 filas que son idénticas a otras ya presentes en el archivo.

- Esto es una clara señal de redundancia o mal manejo de los datos de entrada.


fecha: 22/9/2026

consigna 1: generar una estructura que almacene los datos de cada columna: nombre, el tipo de dato  y el porcentaje de completitud de cada una.

 tengo 11 columnas las cuales debo organizar en alguna estructura y ademas cada una de ellas tiene sus respectivos datos.
 La estructura en la que estoy pensando es en un diccionario donde cada clave del mismo va a ser una columna (es una buena opcion porque cada clave es unica e inmutable y luego puedo acceder a los datos de cada una), y el valor de cada clave de este diccionario tendria que ser otro diccionario con dos elementos que contengan el tipo y la completitud como claves. 
 Para las claves voy a utilizar strings justamente porque deben ser inmutables y representan los nombres de las columnas

consigna 2: generar una estructura para alamcenar al menos 3 roles diferentes ('docente','investigador', 'analista'). Para cada rol debe definirse:
    * las columnas de interes
    * el crtiterio por el que quiere que se ordene la informacion (alfabeticamente,por nombre de columnas o por porcentaje de completitud)
    * la forma de ordenarlo (A: ascendente, B:descendente)
    *opcionalmente, un porcentaje minimo de comletitud, en caso que el rol este configurado con esta opcion. Si esta presente, se deben mostrar las columnas de interes cuyo porcentaje de completitud sea mayor o igual a ese valor

 para este punto pienso en utilizar tambien un diccionario que tenga 3 elementos donde la clave de cada elemento va a ser un rol. Ahora el dilema que tengo es si hago de nuevo un diccionario de diccionarios o hago un diccionario de tuplas, la ventaja que le veo a las tuplas es que son inmutables pero lo que tienen es que a la hora de acceder quizas es medio confuso porque se hace con índices y tendria que estar recordando todo el tiempo que por ejemplo 0 es para las columnas de interes, 1 para el criterio de orden, etc.
 Si lo hago con diccionarios se corre el riesgo de que pueda cometer un error y modificar algun valor pero siento que es mucho mas claro a la hora de leer el codigo.

 Voy a elegir de nuevo el diccionario de diccionarios, siento que me va a ayudar a perderme menos a la hora de ingresar a los valores. Para el elemento "columnas" voy a guardar las que puede usar en una lista. Las columnas para cada rol las puse mas o menos de acuerdo a lo que es mas coherente con cada rol.
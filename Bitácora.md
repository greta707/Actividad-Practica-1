fecha: 22/9/2026

consigna 1: 

 tengo 11 columnas las cuales debo organizar en alguna estructura y ademas cada una de ellas tiene sus respectivos datos.
 La estructura en la que estoy pensando es en un diccionario donde cada clave del mismo va a ser una columna (es una buena opcion porque cada clave es unica e inmutable y luego puedo acceder a los datos de cada una), y el valor de cada clave de este diccionario tendria que ser otro diccionario con dos elementos que contengan el tipo y la completitud como claves. 
 Para las claves voy a utilizar strings justamente porque deben ser inmutables y representan los nombres de las columnas



consigna 2: 

 para este punto pienso en utilizar tambien un diccionario que tenga 3 elementos donde la clave de cada elemento va a ser un rol. Ahora el dilema que tengo es si hago de nuevo un diccionario de diccionarios o hago un diccionario de tuplas, la ventaja que le veo a las tuplas es que son inmutables pero lo que tienen es que a la hora de acceder quizas es medio confuso porque se hace con índices y tendria que estar recordando todo el tiempo que por ejemplo 0 es para las columnas de interes, 1 para el criterio de orden, etc.
 Si lo hago con diccionarios se corre el riesgo de que pueda cometer un error y modificar algun valor pero siento que es mucho mas claro a la hora de leer el codigo.

 Voy a elegir de nuevo el diccionario de diccionarios, siento que me va a ayudar a perderme menos a la hora de ingresar a los valores. Para el elemento "columnas" voy a guardar las que puede usar en una lista. Las columnas para cada rol las puse mas o menos de acuerdo a lo que es mas coherente con cada rol.

 tener este diccionario por fuera de lo que es la funcion que me va a generar el informe hace que, por ejemplo, si necesito hacer alguna modificacion sobre los roles (como agregar un rol mas), lo unico que tengo que hacer es agregar una clave al diccionario sin tener que meterme en la funcion y vovler a chequear su logica.


consigna 3: 
 
 un poco sobre la estructura que tengo pensada es hacer una sola funcion que sea como la "general" y pueda actuar en los dos casos (que se ingrese rol o que no se ingrese un rol). De la teoria tengo que se pueden definir funciones con parametros con valores ya asignados por defecto que voy a usar en caso de que el usuario no ingrese nada. Tiene que ser un parametro con rol nulo o vacio. 
 Dentro de esta funcion tendria que actuar primero con un if donde no hay rol, en el cual informo todas las columnas ordenadas por completitud de forma descendente. Luego en el else actuo cuando si hay un rol.
 tuve el error de pasarle a la funcion un parametro con un input pero me di cuenta que no me sirve, si uso el input en el parametro de la funcion y no por fuera cuando la llame, esta se va a quedar con ese valor por defecto, cosa que no me sirve. 

 Para ordenar el diccionario del primer caso (no se ingresa un rol) voy a chequear que el rol sea nulo (utilizo if rol == none) y luego voy a asignarle a una variable = al diccionario de las columnas con la funcion sorted pasandole parametros (columnas.items(), key = lambda elem:elem[1]["completitud"], reverse = true) tal como en el ejemplo que se dio en clase sobre ordenaminetos de colecciones. Uso .items() para no tener que estar recorriendo la estructura solo con claves y luego tener que averiguar el valor, .items() me ayuda a visualizar mejor la informacion al devolverme el diccionaro como una lista de tuplas.


fecha: 23/9/2026


 El else se va a enfocar en el segundo caso (si se ingresa un rol): 
 a una variable le voy a asignar el valor del rol que se esté ingresando, o sea el diccionario que lleva adentro cada rol.
 otra cosa que me interesa sacar (pero solo para algunos casos), es ver si el rol tiene o no un porcentaje minimo de completitud, como justamente no lo tienen todos los roles voy a usar la funcion get() que no me va a tirar error si no se encuentra la clave, evita que el codigo se rompa.
 ahora lo que tengo que hacer para poder dar informacion sobre un rol especifico es: con los datos del rol filtrar el diccionario original (el que contiene todas las columnas). Para filtrar tambien voy a tener que usar .items(), si no lo uso cuando use filter() solo va a tener los nombres sueltos. Algo que me tengo que acordar es que filter no me devuelve una lista directamente, solo la vista, entonces voy a tener que covertirlo en lista con el list(). En este filter uso lambda para recorrer el diccionario "columnas" y que me chequee si "datos_del_rol"del rol ingresado tiene esas columnas o no, y la otra condicion es que se fije si hay un minimo de completitud o no.

fecha: 24/9/2026

 Lo ultimo q me queda hacer es ordenar segun lo que pida el rol ingresado la lista que devolví. Pense en hacer otro if-else dependiendo de si se tiene que ordenar por nombre o completitud, para ordenar creo que voy a usar de nuevo sorted con funcion lambda y para ver que le pongo al "reverse" primero deberia asignarle a una variable que devuelva true o false segun la forma de ordenamiento del rol


 Lo ultimo que tengo que hacer es el jupyter donde voy a importar el modulo entero, podria importar solo la funcion pero siento que es mucho mas claro importar el modulo y que cuando se deba usar la funcion se vea de donde viene, siento que me puede llevar a confusiones. 
 Voy a usar otro if-else donde se preguntara si el rol ingresado es nulo o no.

 si llega alguna modificacion como agregar una nueva columna al dataset lo unico que deberia hacer es agregar dicha columna, como esta todo separado no impactaria en la logica de la funcion que genera los informes.

 Algo que acabo de darme cuenta con una de las preguntas de la rubrica es que si se ingresa un criterio de orden distinto a los especificados mi codigo ordena mal, si se ingresa como criterio de orden "promedio" el codigo ordenaria mal, yo puse que si el criterio es por nombre que ordene de tal forma, y caso contrario, en el else, que ordene de otra, al ingresar "promedio" me estaria ordenando con lo que esta en el else y quedaria ordenado por otro criterio que nada que ver con el promedio. Lo voy a cambiar agregandole un elif y que en el else me tire que el criterio no es valido.

Los valores asignados para los porcentajes de completitud los fui variando cosa que cuando me muestre el informe el programa pueda chequear que el ordenamiento sea correcto.

fecha: 25/9/2026

MODIFICACION 1: se pidio agregar un rol economista, lo unico que debo hacer es agregar la nueva clave y sus especificaciones al diccionario "roles" sin tener que modificar la funcion "generar_informe".

MODIFICACION 2: si pidio agregar una nueva columna al diccionario original sin modificar los roles, lo unico por hacer es agregarlo al diccionario de diccionarios "columnas" y correr el programa para ver en que informes aparece. Con la prueba aparece unicamente en el informe general (cuando no se ingresa un rol) y no aparece en los demas informes.

MODIFICACION 3: la ventaja de usar el filter() es que trabaja con lazy iterators en vez de construir y almacenar una lista inmmediatamente, ayuda a no saturar la memoria, y tiene una gran ventaja de rendimiento en caso de que el diccionario de columnas crezca
#Punto 1

columnas = {"PONDERA":{"tipo":"int", "completitud":60}, "ESTADO":{"tipo":"int", "completitud":77},
 "CAT_OCUP":{"tipo":"int", "completitud":100}, "EDAD":{"tipo":"int", "completitud": 100},
 "REGION":{"tipo":"int", "completitud":85}, "AGLOMERADO":{"tipo":"int", "completitud":100},
"MAS_500":{"tipo": "str", "completitud":97},"ANO4":{"tipo":"int", "completitud": 67}, 
"TRIMESTRE":{"tipo":"int", "completitud":66}, "ITF":{"tipo":"int", "completitud":90}, 
"GDECCFR":{"tipo":"int", "completitud":78}}

#armo un diccionario de diccionarios con el nombre de cada columna y sus datos

#Punto 2

roles = {
    "docente":{
        "columnas":["EDAD","ESTADO","REGION"],
         "criterio_orden": "nombre",
         "forma": "A"},
    "investigador":{
        "columnas":["PONDERA","ANO4", "TRIMESTRE", "MAS_500"],
        "criterio_orden": "completitud",
        "forma": "B",
        "minimo_completitud": 50},
    "analista":{
        "columnas":["ITF","GDECCFR","CAT_OCUP"],
        "criterio_orden": "completitud",
        "forma": "B"}
}


def generar_informe (rol = None):
    """ genera un informe detallado sobre las columnas de interes del rol ingresado
      si no se ingresa un rol especifico devuelve un informe general con todas las
    columnas del dataset ordenadas por completitud"""

    if rol == None:
        informe_sin_rol = sorted(columnas.items(), key=lambda elem:elem[1]["completitud"], reverse=True)
        return informe_sin_rol
    else:
        datos_del_rol = roles[rol] #me da info del rol especifico
        porcentaje_minimo = datos_del_rol.get("minimo_completitud", 0) # busco si tiene minimo de completitud,
        #0 es por si no encuentra clave

        #ahora filtro por las columnas de interes y chequeo si tiene porcentaje minimo, si no tiene toma el cero anterior
        # con list() me devuelve una lista
        columnas_filtradas = list(filter(lambda elem: elem[0] in datos_del_rol["columnas"] 
                                         and elem[1]["completitud"] >= porcentaje_minimo, columnas.items()))

        orden_descendente =  datos_del_rol["forma"] == "B" #esto me devuelve un booleano

        if datos_del_rol["criterio_orden"] == "nombre":
            informe_final = sorted(columnas_filtradas, key=lambda elem:elem[0], reverse=orden_descendente)
            #con elem[0] hago referencia al nombre de las columnas de la lista q devolvi antes
        elif datos_del_rol ["criterio_orden"] == "completitud":
            #ordenar por completitud
            informe_final = sorted(columnas_filtradas, key=lambda elem:elem[1]["completitud"], reverse=orden_descendente)
        else:
            informe_final = "Error: criterio de orden no valido"
        return informe_final
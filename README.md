# api_rest_demo

Ejemplo para utilizar Taspypie y Django Rest Framework

La app trabajo, tiene el modelo base y un demom de RestFull con Taspypie .

La aplicacion trabajos2 tiene es un demo RestFull on Django-Rest

## Para recuperar datos:

Desde una consola pueden recuperar los datos con la aplicacion httpie, la pieden instalar con:
```
sudo apt-get install httpie
```

## Prueba de los RestFull:

Taspypie:

Lista todos los registros
```
http http://127.0.0.1:8000/trabajos/api/v1/trabajo/?format=json
```
Busca un registro
```
http http://127.0.0.1:8000/trabajos/api/v1/trabajo/1/?format=json
```

Busca por nombre
```
http http://127.0.0.1:8000/trabajos/api/v1/trabajo/?format=json&nombre__contains=sys
```

Django-rest

Para recopilar todo:
```
http http http://127.0.0.1:8000/trabajos/api/v2/trabajo
```
Para recopilar un registro
```
http: http://127.0.0.1:8000/trabajos/api/v2/trabajo/2/
```
## Frontend para utilizar el CRUD con angular

Para consumir RestFull de agular pueden hacerlo ejecutando la aplicacion desde la diección
```
http://127.0.0.1:8000/frontend/view/#/movies
```
Es una adaptación de un api movies rest de http://www.sitepoint.com/creating-crud-app-minutes-angulars-resource/

Falta sustutuir movies por trabajos

## TODO

- [X] Taspypie con aplicación trabajos
- [X] Djando Rest framework

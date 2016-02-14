# api_rest_demo

Ejemplo para utilizar Taspypie y Django Rest Framework

## Para recuperar datos:

Busca un registro
http://127.0.0.1:8000/trabajos/api/v1/trabajo/1/?format=json

Lista todos los registros
http://127.0.0.1:8000/trabajos/api/v1/trabajo/?format=json

Busca por nombre
http://127.0.0.1:8000/trabajos/api/v1/trabajo/?format=json&nombre__contains=sys

## TODO

- [x] Taspypie con aplicación trabajos
- [ ] Djando Rest framework
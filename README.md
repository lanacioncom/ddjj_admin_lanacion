# Declaraciones Juradas Abiertas - Formulario ABM

Declaraciones Juradas Abiertas es un proyecto de LA NACION, junto a Poder Ciudadano, Fundación Directorio Legislativo, la Asociación Civil por la Igualdad y la Justicia y más de 30 voluntarios que colaboraron para abrir la información patrimonial de los principales funcionarios públicos de la Argentina.
 
Todas las personas que participamos del proyecto queremos que otras organizaciones y equipos se sumen a la aventura de abrir documentos públicos que no puedan ser procesados (aún) por las tecnologías disponibles. Con este mismo espíritu y gracias al apoyo de Hivos, abrimos el código de nuestro sitio porque estamos convencidos de que su reutilización permitirá a otros hacer más fácil la tarea de crear bases de datos para acercar la información pública a los ciudadanos. Por eso también, invitamos (y queremos) que otras personas puedan descargar , modificar y retrabajar lo que hicimos en equipo.
 
A través de estas líneas, también queremos agradecemos a Suma Ciudadana, ONG de Perú con la que trabajamos durante más de un año en el marco del proyecto de Hivos para impulsar y mejorar nuestras platafromas de declaraciones juradas. Juntos nos enfrentamos a desafíos que pudimos resolver colectivamente, pero por sobre todas las cosas, hicimos las cosas en equipo con una única finalidad: que las personas pudieron conocer el patrimono de los funcionarios públicos sin tecnicismos y de modo sencillo.

## Tutorial de carga:

[Ejemplo de guía de carga de información a través del formulario online.](https://docs.google.com/document/d/1f0aUuqtxJAVwy-vQJY6NtJ28lPILDoET8X0cQf4JGEY/edit)

## Instalación

**Requerimientos:** 

* Python 2.7
* Pip
* Virtualenv

Crear el virtualenv

```bash
$ virtualenv ~/.venv_admin_ddjj
$ source ~/.venv_admin_ddjj/bin/activate
```

Clonar el proyecto

```bash
$ git clone https://github.com/lanacioncom/ddjj_admin.git
$ cd ddjj_admin
```

Instalar requerimientos

```bash
$ pip install -r requierements.txt
```

Primera migración

```bash
$ python manage.py migrate
```

Crear super user para ingresar al admin

```bash
$ python manage.py createsuperuser
```


## Docker

1. Instalar Docker: https://docs.docker.com/installation/
2. Crear Imagen y Containers
    
    `$ ./dockercreate.sh`

3. Crear Usuario de Admin (desde container)
    
    `# python manage.py createsuperuser`

4. Levantar el sitio
    
    `# python manage.py runserver 0.0.0.0:8000`

5. Obtener puerto

    `# ./dockercli.sh port`
    
6. Acceder desde el host a localhost al puerto correcto.

* Para facilitar el uso de los contenedores se agrego el script dockercli.sh

## Participantes:

* [momiperalta]
* [fcoel]
* [colmanromi]
* [gabybouret]
* [MarianTV]
* [cbertelegni]
* [\_\_rustico\_\_]



[colmanromi]:https://twitter.com/colmanromi
[gabybouret]:https://twitter.com/gabybouret
[momiperalta]:https://twitter.com/momiperalta
[fcoel]:https://twitter.com/fcoel
[MarianTV]:https://twitter.com/MarianTV
[cbertelegni]:https://twitter.com/cbertelegni
[\_\_rustico\_\_]:https://twitter.com/__rustico__

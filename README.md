# <p align="center">Ferreteria Maxi</p>

## <p align="center">Comisión 23320 | Grupo 2</p>

### Integrantes 

- [Juan Alberto Mazzocchi](https://github.com/JuanMazzocchi)
- [Nahuel Cerrano](https://github.com/nahuelcerrano)
- [Sofia Irene Radulovich](https://github.com/sofiaradulovich)

## Descripción

Ferreteria Maxi es un sitio web mayorista de ferreteria donde gestiona los pedidos de los preventistas

## Requisitos

- [Python 3.9 o superior](https://www.python.org/downloads/)
- [MySQL 8.0 o superior](https://www.mysql.com/downloads/)
- [Git 2.40 o superior](https://git-scm.com/downloads)

## Instalación

1. Clonar el repostorio desde git
>```bash
>git clone 'https://github.com/nahuelcerrano/grupo2-django.git'
>```

2. Accedeter a la carpeta raíz del projecto

>```bash
>cd 'grupo2-django'/
>```

3. Crear el enterno virtual

>```bash
>python -m venv 'entorno_virtual'
>```

4. Activar el entorno virtual

  >*Windows*
  >
  >```bash
  >entorno_virtual\Scripts\activate
  >```
  >
  >*Linux / macOS*
  >
  >```bash
  >source entorno_virtual/bin/activate
  >```

5. Instalar las dependencias

>```bash
>pip install -r requirements.txt
>```

6. Crear un archivo .env en la carpeta raíz

>```bash
>SECRET_KEY='secret_key'
>DB_PASS='db_password'
>```

7. Crear un usuario administrador

>```bash
>python manage.py createsuperuser
>````

8. Levantar el sitio en el servidor local

>```bash
>python manage.py runserver
>````


## Proyecto hecho en

- [Django 3.2](https://docs.djangoproject.com/en/3.2/releases/3.2/) - El framework web utilizado
- [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - El framework css implementado

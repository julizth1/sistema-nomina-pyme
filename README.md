# 📌 Pyme Cloud - Sistema de Gestión de Nómina y Marcaciones

Plataforma web desarrollada en Python y Django orientada a la automatización, cálculo y gestión de la nómina para pequeñas y medianas empresas (Pymes), reemplazando los procesos manuales e ineficientes en hojas de cálculo.

---

## 🛠️ Stack Tecnológico

* **Backend:** Python 3.12, Django 5.x, Django REST Framework
* **Frontend:** HTML5, CSS3 (Bootstrap 5), JavaScript Vanilla
* **Procesamiento de Datos:** Pandas, Openpyxl
* **Base de Datos:** PostgreSQL (Nube/Render) / SQLite (Desarrollo local)
* **Seguridad:** JWT, Protección CSRF, Sanitización ORM, CORS
* **Despliegue Cloud:** Render / Supabase PostgreSQL

---

## 🎯 Objetivos del Proyecto

* **Objetivo General:** Desarrollar un sistema web de gestión de nómina para Pymes utilizando Python, Django REST Framework y PostgreSQL para el cálculo automático de liquidaciones proporcionales y horas extras.
* **Procesamiento de Asistencia:** Cargar masivamente archivos de Excel con marcaciones para períodos de 13 días, aplicando reglas dinámicas de horario (límite 08:00 AM para domingos y 11:00 AM para días ordinarios).

---

## 📁 Documentación y Presentación del Proyecto

Las diapositivas en PDF con el resumen del problema, la solución tecnológica y los diagramas de arquitectura se encuentran en:

* 📄 **[Ver Diapositivas de la Presentación (PDF)](docs/presentacion.pdf)**

---

## 🏗️ Arquitectura de la Solución en la Nube

1. **Capa de Presentación:** Interfaz responsive basada en Bootstrap 5 y JavaScript para la interacción dinámica sin recargar la página.
2. **Capa de Aplicación:** API REST con Django REST Framework y vistas dedicadas para la carga y parsing masivo de archivos `.xlsx` usando `pandas`.
3. **Capa de Base de Datos:** Persistencia en PostgreSQL para almacenar empleados, marcaciones reales y comprobantes de liquidación.

---
##🚀 Instrucciones de Ejecución Local
###1. Clonar el repositorio
Bash
git clone [https://github.com/julizth1/sistema-nomina-pyme.git](https://github.com/julizth1/sistema-nomina-pyme.git)
cd sistema-nomina-pyme
2. Crear y activar el entorno virtual
Bash
python -m venv venv

# En Windows (Git Bash):
source venv/Scripts/activate

# En macOS / Linux:
source venv/bin/activate
3. Instalar dependencias del proyecto
Bash
pip install -r src/requirements.txt
4. Configurar variables de entorno y Base de Datos (PostgreSQL)
Asegúrate de tener un servidor de PostgreSQL corriendo localmente o en la nube (Render / Supabase), o configura las credenciales en el archivo src/core/settings.py:

Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tu_nombre_db',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
5. Sincronizar esquemas y ejecutar migraciones
Bash
cd src
python manage.py makemigrations
python manage.py migrate
6. Crear un Superusuario (Administrador Jazzmin)
Bash
# En Windows Git Bash:
winpty python manage.py createsuperuser

# En terminal estándar:
python manage.py createsuperuser
7. Iniciar el servidor de desarrollo
Bash
python manage.py runserver





# 🚀 Odoo CRM Integration System

Este proyecto es una solución de integración que conecta un **Frontend moderno en Angular** con el potente **CRM de Odoo**, utilizando **Django** como intermediario (API Gateway) para asegurar, transformar y gestionar los datos.

## 📋 Arquitectura del Proyecto

El sistema sigue una arquitectura de 3 capas:

1. **Frontend (Angular 19):** Interfaz de usuario para visualizar y gestionar oportunidades (Leads).
2. **Backend (Django REST Framework):** API que actúa como puente, manejando la seguridad y la comunicación XML-RPC.
3. **Base de Datos (Odoo CRM):** La fuente de la verdad donde residen los datos del negocio.

---

## 🛠️ Tecnologías Usadas

* **Lenguaje:** Python 3.12+ / TypeScript
* **Backend:** Django 5.x + Django REST Framework
* **Frontend:** Angular 19 (Standalone Components)
* **Conexión:** XML-RPC (Protocolo nativo de Odoo)
* **Seguridad:** Python-Decouple (Variables de entorno)

---

## ⚙️ Configuración e Instalación

Sigue estos pasos para levantar el proyecto en local.

### 1. Clonar el repositorio

```bash
git clone <tu-url-del-repo>
cd PROYECTO_ODOO_FINAL
```



cd backend

# Crear entorno virtual

python -m venv venv

# Activar entorno (Windows)

.\venv\Scripts\Activate

# Instalar dependencias

pip install -r requirements.txt

# Crear archivo de variables de entorno (.env)

# (Ver sección de Variables de Entorno abajo)

# Ejecutar migraciones

python manage.py migrate

# Iniciar servidor

python manage.py runserver





# Abrir nueva terminal y volver a la raíz

cd frontend

# Instalar dependencias de Node

npm install

# Iniciar servidor de desarrollo

ng serve -o


ODOO_URL=https://tu-instancia.odoo.com
ODOO_DB=nombre-de-tu-db
ODOO_USER=tu-email@ejemplo.com
ODOO_PASSWORD=tu-password-segura
SECRET_KEY=tu-clave-secreta-django
DEBUG=True

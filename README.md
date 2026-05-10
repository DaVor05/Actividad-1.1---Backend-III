# Actividad 1.1 - Backend III

## Descripción
Proyecto desarrollado para la materia de Backend III, enfocado en la configuración de un entorno profesional utilizando Django y Django REST Framework bajo una estructura modular y prácticas de seguridad inicial.

## Tecnologías Utilizadas
- Python
- Django
- Django REST Framework
- python-dotenv (para gestión de variables de entorno)

## Configuración del Proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/DaVor05/Actividad-1.1---Backend-III.git
```

### 2. Crear y activar el entorno virtual
```bash
python -m venv venv
```
# En Windows:
```bash
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Variables de Entorno
Crea un archivo .env en la raíz del proyecto basado en el archivo .env.example:
```bash
cp .env.example .env
```

Luego, rellena los valores necesarios (SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASE_URL) en tu archivo .env.

### 5. Ejecutar Migraciones
```bash
python manage.py migrate
```

### 6. Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```

### Estructura del Proyecto
El proyecto utiliza una separación modular para mantener el código organizado:
- api/: Contiene todo lo relacionado con la capa de presentación (Serializers, Views, URLs).
- apps/: Contiene la lógica de negocio y los modelos de datos.
- settings/: Archivos de configuración divididos en base.py, development.py y production.py.

### Seguridad
- Uso de .gitignore para ocultar archivos sensibles como .env y el entorno virtual.
- Implementación de variables de entorno para evitar credenciales expuestas en el código.
- Capacidad de rotación de llaves mediante el archivo de configuración.


### Notas para tu entrega:
1. **Crea el archivo:** En VS Code, haz clic derecho en la raíz de tu proyecto, selecciona "Nuevo archivo" y nómbralo `README.md`.
2. **Pega el contenido:** Copia el texto de arriba y pégalo ahí.
3. **Súbelo a GitHub:** No olvides hacer `git add README.md`, `git commit -m "Añadido

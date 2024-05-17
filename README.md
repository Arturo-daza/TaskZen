# TaskZen

TaskZen es una innovadora aplicación de gestión de tareas diseñada para hacer frente a los desafíos de la multitarea moderna. En la acelerada sociedad actual, las personas a menudo se ven abrumadas por un sinfín de tareas y responsabilidades, lo que conduce a sentimientos de desorganización y disminución de la productividad.

Las herramientas tradicionales de gestión de tareas, como las agendas en papel o las aplicaciones básicas, se quedan cortas a la hora de satisfacer las necesidades de los usuarios modernos. Carecen de la intuitividad, flexibilidad y funcionalidad necesarias para una gestión eficaz de las tareas. TaskZen pretende salvar esta brecha ofreciendo una interfaz fácil de usar junto con características robustas.

Las principales características de TaskZen incluyen la creación intuitiva de tareas, categorías y prioridades personalizables, sincronización perfecta entre dispositivos y la posibilidad de adjuntar archivos y establecer recordatorios. Al proporcionar a los usuarios una experiencia de gestión de tareas ágil y personalizada, TaskZen pretende mejorar la productividad, reducir el estrés y aprovechar las oportunidades para conseguir logros.

## Requisitos

- Python 3.9
- Git

## Instalación

Sigue los siguientes pasos para clonar y correr la aplicación:

### 1. Clonar el repositorio

Primero, clonar el repositorio:

```sh
git clone https://github.com/tu-usuario/TaskZen.git
cd TaskZen
```
### 2. Crear un entorno virtual en Python 3.9
Crea un entorno virtual utilizando *venv*:
```sh
python3.9 -m venv env
```
### 3. Activar el entorno virtual
Activa el entorno virtual. El comando varía dependiendo de tu sistema operativo:
- En Windows:
```sh
.\env\Scripts\activate
```

- En macOS y Linux:
```sh
source env/bin/activate
```
### 4. Instalar las dependencias
Instala las dependencias del archivo requirements.txt:
```sh
pip install -r requirements.txt
```
### 5. Correr la aplicación
Finalmente, inicia la aplicación con uvicorn:
```sh
uvicorn main:app --reload
```
La aplicación estará disponible en http://127.0.0.1:8000/ en tu navegador. 


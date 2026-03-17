# 🚀 AI Engineering Learning Journey - Platzi

Bienvenido a mi monorepo de aprendizaje continuo. Este repositorio documenta mi evolución técnica y mi ruta de estudio en ingeniería de software, análisis de datos e Inteligencia Artificial a través de Platzi.

Aquí consolido todos mis apuntes, ejercicios prácticos y mini-proyectos, organizados cronológicamente desde los fundamentos de la programación hasta el despliegue de modelos de Machine Learning.

## 📂 Arquitectura del Repositorio

El código está estructurado en módulos numerados para facilitar su navegación:

* **`01_python_fundamentals/`**: Conceptos básicos de Python, estructuras de datos y lógica de programación.
* **`02_python_intermediate/`**: POO, manejo de errores, integraciones con APIs externas (OpenAI, NewsAPI) y scripts avanzados.
* **`03_math_and_algorithms/`**: Álgebra lineal, vectores y fundamentos matemáticos para Data Science y Machine Learning.
* **`04_databases_and_backend/`**: Diseño de bases de datos relacionales, consultas SQL y conexiones backend usando herramientas como Supabase.
* **`05_ai_and_mlops/`**: Implementación de modelos de IA, orquestación de datos y prácticas de MLOps.
* **`06_sandbox/`**: Entorno seguro para pruebas rápidas, scripts sueltos y experimentación (`main.py`).

## 🛠️ Stack Tecnológico

* **Lenguajes:** Python, SQL
* **Gestión de Entornos:** `uv` (Fast Python Package Installer)
* **Control de Versiones:** Git & GitHub
* **IA & APIs:** OpenAI API

## ⚙️ Cómo ejecutar los proyectos localmente

Este repositorio utiliza `uv` para una gestión ultra rápida de dependencias y entornos virtuales. Para correr cualquier script principal (por ejemplo, el analizador de noticias con IA), asegúrate de clonar el repositorio e instalar las dependencias:

```bash
# 1. Clonar el repositorio
git clone [https://github.com/carloscarranza2486/platzi-engineer.git](https://github.com/carloscarranza2486platzi-engineer.git)
cd platzi-engineer

# 2. Sincronizar el entorno con uv
uv sync

# 3. Ejecutar un script
uv run python3 06_sandbox/main.py
# Clasificador de SPAM usando Naive Bayes

Implementación de un clasificador de correos electrónicos SPAM utilizando el algoritmo Naive Bayes y el Teorema de Bayes.

## 👥 Integrantes

- Ricardo Ballesteros Amavizca / **A01255358**
- Julio Charbel Porras Osorio / **A01736268**
- Samuel Gómez Morales / **A01276780**

## 📋 Descripción

Este proyecto implementa un modelo de Machine Learning basado en el **Teorema de Bayes** para clasificar correos electrónicos (mensajes SMS) como SPAM o HAM (legítimos). El modelo utiliza:

- **MultinomialNB** de scikit-learn
- **TF-IDF** para extracción de características
- **SMS Spam Collection Dataset** con 5,572 mensajes

### Teorema de Bayes

El clasificador se basa en:

$$P(\text{SPAM}|\text{palabras}) = \frac{P(\text{palabras}|\text{SPAM}) \times P(\text{SPAM})}{P(\text{palabras})}$$

## 🚀 Instalación y Configuración

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Jupyter Notebook o JupyterLab

### Paso 1: Clonar el repositorio

```bash
git clone <URL-del-repositorio>
cd "Naive Bayes Classifier"
```

### Paso 2: Crear un entorno virtual (recomendado)

```bash
# En macOS/Linux
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Preparar el dataset

Si el dataset no está incluido, asegúrate de tener el archivo:
- `data/sms_spam_collection.csv`

El notebook incluye código de fallback con datos de ejemplo si no se encuentra el dataset principal.

## 📊 Uso

### Ejecutar el Notebook

```bash
jupyter notebook Naive_Bayes_SPAM_Classifier.ipynb
```

O si usas JupyterLab:

```bash
jupyter lab Naive_Bayes_SPAM_Classifier.ipynb
```

### Estructura del Notebook

1. **Importación de librerías**
2. **Carga y exploración de datos**
3. **Preprocesamiento de texto**
4. **Extracción de características (TF-IDF)**
5. **División de datos (train/test)**
6. **Entrenamiento del modelo Naive Bayes**
7. **Evaluación y métricas**
   - Accuracy
   - Precision
   - Recall
   - F1-Score
   - Matriz de confusión
8. **Predicciones personalizadas**

## 📈 Resultados

El modelo logra:
- Alta precisión en la clasificación de mensajes SPAM
- Visualizaciones de matrices de confusión
- Análisis detallado de métricas de rendimiento

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **NumPy** - Computación numérica
- **Pandas** - Manipulación de datos
- **scikit-learn** - Algoritmos de Machine Learning
- **Matplotlib** - Visualización de datos
- **Jupyter Notebook** - Entorno interactivo

## 📝 Notas

- El notebook incluye explicaciones teóricas del Teorema de Bayes
- Contiene visualizaciones y métricas detalladas
- Permite probar el modelo con mensajes personalizados

## 📄 Licencia

Este proyecto fue desarrollado con fines educativos para el curso de **Métodos de Razonamiento e Incertidumbre** en el Instituto Tecnológico y de Estudios Superiores de Monterrey.

## 🤝 Contribuciones

Este es un proyecto académico. Para dudas o sugerencias, contacta a los integrantes del equipo.

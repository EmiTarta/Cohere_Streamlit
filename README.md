# Cohere_Streamlit
Cohere Text Analysis App
¡Bienvenido a la aplicación de análisis de texto con Streamlit y Cohere! 🚀 Esta herramienta permite subir un archivo .txt, hacer preguntas sobre su contenido, y obtener respuestas basadas en IA.

### Características
- Analiza archivos de texto dividiéndolos en fragmentos.
- Calcula similitudes de embeddings para encontrar el texto más relevante.
- Genera respuestas a preguntas usando la API de Cohere.

### Instalación y Configuración
La aplicación funciona en local. Aquí te dejo un paso a paso para que puedas utilizarla: 
1. Clona el repositorio:

```py
git clone https://github.com/tu-usuario/cohere-text-analysis.git
cd cohere-text-analysis
```
2. Instala las dependencias:
```py
pip install streamlit cohere python-dotenv
```
3. Configura la clave de API de Cohere:
- Crea un archivo .env en el directorio principal del proyecto.
- Añade tu clave de API de Cohere de esta manera:
```py
COHERE_API_KEY=tu_api_key
```
4. Inicia la aplicación: abre un terminal, navega hasta la carpeta donde está tu archivo y pon:
```py
streamlit run app.py
```
### Uso
1. Sube un archivo de texto en formato .txt.
2. Escribe tu pregunta en el cuadro de entrada.
3. Haz clic en el botón "Analizar" para obtener una respuesta.
### Requisitos
- Python 3.7 o superior.
- Cuenta activa de Cohere con una clave de API válida.
### Capturas de Pantalla

Aquí tienes un vistazo de cómo luce la aplicación:
![Captura de Pantalla de la App](https://github.com/EmiTarta/Cohere_Streamlit/blob/main/Pagina_inicial.png)

Este es el link de la aplicación desplegada en Streamlit: ![Predictor_Salarios](https://geminiapp-l.streamlit.app/)
Nota: si el link no funciona, se debe a que la versión gratuita de Streamlit permite sólo un proyecto desplegado, y este se ha dado de baja.  

### Contribuciones
Si deseas contribuir, ¡no dudes en abrir un issue o un pull request!

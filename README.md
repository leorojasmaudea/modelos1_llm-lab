# Programación con LLMs - IA para las Ciencias e Ingenierías
Este repositorio contiene los entregables para el proyecto del curso **Inteligencia Artificial para las Ciencias e Ingenierías (2026-1)** de la Universidad de Antioquia. 

El objetivo es aplicar metodologías rigurosas de desarrollo de software asistido por Modelos de Lenguaje de Gran Escala (LLMs), enfocándose en la creación de casos de uso técnicos y validación automática de código.

## 🛠️ Estructura del Proyecto: Fase 1

En esta fase, se han diseñado 4 ejercicios originales que cubren problemas reales en áreas de ingeniería de sistemas, hardware y química industrial, evitando temas genéricos para asegurar la autenticidad del contenido.

### Ejercicios Desarrollados

| ID | Título del Ejercicio | Librería | Descripción Técnica |
| :--- | :--- | :--- | :--- |
| **0001** | **Clasificación de Movimiento RFID** | `sklearn` | Análisis de varianza de señales RSSI y fase en protocolos LLRP para distinguir etiquetas estáticas de móviles. |
| **0002** | **Análisis de Lubricantes Sintéticos** | `sklearn` | Predicción de la base química (PAO/Éster vs Mineral) mediante índices de viscosidad y puntos de inflamación. |
| **0003** | **Normalización de Sistemas Legados** | `pandas` | Reconstrucción y limpieza de tipos de datos provenientes de entornos antiguos (VB6/FoxPro) a estructuras modernas. |
| **0004** | **Detección de Ocupación Fantasma** | `pandas` | Cruce de logs de sensores ultrasónicos de estacionamiento contra registros de pago activos. |

## 📂 Contenido del Repositorio

Cada ejercicio consta de dos archivos siguiendo el estándar estricto del curso:
* `question-XXXX.txt`: Definición del problema, entrada esperada y misión del programador.
* `question-XXXX-usecase-generator.py`: Script de Python que genera casos de prueba aleatorios y resultados esperados para validación automática.

## 🚀 Metodología
Para el desarrollo de estos ejercicios se utilizó **Gemini 3 Flash** como copiloto de programación, aplicando técnicas de *prompt engineering* para asegurar que los generadores de casos de uso sean robustos y cubran casos de borde (edge cases).

---
**Autor:** Leon Andres Rojas Martinez  
**Institución:** Universidad de Antioquia  
**Facultad:** Ingeniería de Sistemas  
**Año:** 2026
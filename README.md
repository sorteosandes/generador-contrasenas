# 🔐 Generador Seguro de Contraseñas

Proyecto desarrollado en Python para la asignatura de Lógica de Programación.

## 📌 Descripción
Este programa permite generar contraseñas seguras personalizadas según:

- Longitud mínima validada
- Letras mayúsculas
- Letras minúsculas
- Números
- Símbolos
- Manejo de errores

## 🛠 Tecnologías utilizadas
- Python
- Módulos: random, string

## ▶ Cómo ejecutar

```bash
python generador_contrasenas.py


---

## 📊 Diagrama de Flujo General

```mermaid
flowchart TD
    A[Inicio] --> B[Mostrar título]
    B --> C[Obtener longitud]
    C --> D[Obtener tipos de caracteres]
    D --> E{¿Se seleccionaron caracteres?}
    E -- No --> F[Mostrar error]
    F --> G[Fin]
    E -- Sí --> H[Generar contraseña]
    H --> I[Mostrar contraseña]
    I --> G[Fin]



flowchart TD
    A[Inicio] --> B[Solicitar longitud]
    B --> C{¿Es número válido?}
    C -- No --> D[Mostrar error]
    D --> B
    C -- Sí --> E{¿Longitud >= 8?}
    E -- No --> F[Mostrar error]
    F --> B
    E -- Sí --> G[Retornar longitud]




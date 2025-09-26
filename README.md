# DataValidatorpy

![Releases](https://img.shields.io/pypi/v/DataValidatorpy)
![Python Version](https://img.shields.io/pypi/pyversions/DataValidatorpy)

Author: [Gerardo Burgos](https://github.com/gerarb1)

una librería simple y robusta en Python para validar datos personales (como nombres, edades y documentos) y de contacto (como emails y celulares), utilizando validadores especializados y el patrón Builder para crear objetos `Persona` de manera segura y modular.

## Descripción

Esta librería resuelve el problema de validar y estructurar datos de personas de forma consistente, evitando errores comunes como entradas inválidas (e.g., edades negativas o emails malformados). Es ideal para aplicaciones que manejan formularios, bases de datos o APIs donde la integridad de los datos es crítica.

- **Características clave**:
  - Validadores base para números, letras y alfanuméricos.
  - Validadores especializados para datos personales y de contacto.
  - Patrón Builder para construir objetos `Persona` paso a paso con validación automática.
  - Fácil de extender para más tipos de validaciones.

## Instalacion

```bash
    pip  install DataValidatorpy==0.0.1
```

## Prueba

```python
from DataValidatorpy import PersonaBuilder

# Crear builder y agregar datos con validación automática
builder = PersonaBuilder()
persona = (
    builder
    .set_datos_personales("Juan Pérez", "25", "12345678")
    .set_datos_contacto("juan@example.com", "987654321", "Calle Falsa 123")
    .build()
)

print(persona) 
``` # Salida: Persona: Juan Pérez, Edad: 25, Documento: 12345678, Email: juan@example.com, Celular: 987654321, Dirección: Calle Falsa 123
```

## Paquete subido en pypi

en vez de poner geraro_burgos_pg2_tecba le puse DataValidatorpy, porque me parece un nombre mas adecuado para una lbreria
<img width="1134" height="417" alt="pypi" src="https://github.com/user-attachments/assets/e64e886d-3ab3-4bc0-ae76-b3663493f465" />

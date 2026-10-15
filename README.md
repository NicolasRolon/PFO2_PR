# PFO 2 - Sistema de Gestión de Tareas con API y Base de Datos

## Archivos

- `servidor.py`: API Flask y acceso a SQLite.
- `cliente.py`: cliente de consola.
- `usuarios.db`: se crea automáticamente.
- `requirements.txt`: librerías necesarias.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecutar

Primero abrir una terminal:

```bash
python servidor.py
```

Luego abrir otra terminal:

```bash
python cliente.py
```

## Uso del cliente

El menú permite:

1. Registrar usuario.
2. Iniciar sesión.
3. Ver la página de tareas.
4. Salir.

Para poder ver `/tareas` primero hay que iniciar sesión.

# Endpoints

## POST /registro

Recibe:

```json
{
  "usuario": "nico",
  "contraseña": "1234"
}
```

La contraseña se guarda hasheada en SQLite.

## POST /login

Verifica el usuario y la contraseña.

## GET /tareas

Muestra un HTML de bienvenida si el usuario inició sesión.

# Respuestas conceptuales

## ¿Por qué hashear contraseñas?

Porque una contraseña no debe guardarse en texto plano.
Al guardar un hash, la contraseña original no queda almacenada directamente en la base de datos.

## Ventajas de usar SQLite

SQLite es simple, liviano y no necesita instalar un servidor de base de datos aparte.
Es suficiente para un proyecto pequeño como este.

# Capturas para entregar

Conviene incluir tres capturas:

1. Registro exitoso.
2. Login exitoso.
3. Opción "Ver tareas" mostrando la bienvenida.

# GitHub


from flask import Flask, request, jsonify, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "clave-simple-pfo2"

DB = "usuarios.db"


# Crea la base de datos y la tabla de usuarios
def inicializar_db():
    conexion = sqlite3.connect(DB)
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contraseña TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()


# Registro de usuarios
@app.route("/registro", methods=["POST"])
def registro():
    datos = request.get_json()

    usuario = datos.get("usuario")
    contraseña = datos.get("contraseña")

    if not usuario or not contraseña:
        return jsonify({"error": "Faltan datos"}), 400

    contraseña_hash = generate_password_hash(contraseña)

    try:
        conexion = sqlite3.connect(DB)
        cursor = conexion.cursor()

        cursor.execute(
            "INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)",
            (usuario, contraseña_hash)
        )

        conexion.commit()
        conexion.close()

        return jsonify({"mensaje": "Usuario registrado correctamente"}), 201

    except sqlite3.IntegrityError:
        return jsonify({"error": "El usuario ya existe"}), 400


# Inicio de sesión
@app.route("/login", methods=["POST"])
def login():
    datos = request.get_json()

    usuario = datos.get("usuario")
    contraseña = datos.get("contraseña")

    conexion = sqlite3.connect(DB)
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT contraseña FROM usuarios WHERE usuario = ?",
        (usuario,)
    )

    resultado = cursor.fetchone()
    conexion.close()

    if resultado and check_password_hash(resultado[0], contraseña):
        session["usuario"] = usuario
        return jsonify({"mensaje": "Inicio de sesión correcto"})

    return jsonify({"error": "Usuario o contraseña incorrectos"}), 401


# Página protegida de tareas
@app.route("/tareas", methods=["GET"])
def tareas():
    if "usuario" not in session:
        return "Debe iniciar sesión primero", 401

    return f"""
    <h1>Bienvenido, {session['usuario']}</h1>
    <p>Accediste correctamente al sistema de tareas.</p>
    """


if __name__ == "__main__":
    inicializar_db()
    app.run(debug=True)

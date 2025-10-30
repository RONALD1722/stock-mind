import bcrypt
from config import conectar, desconectar

def crear_usuario(nombre, usuario, clave, rol="administrador"):
    conexion = conectar()
    if not conexion:
        print("❌ No se pudo conectar a la base de datos")
        return

    try:
        with conexion.cursor() as cur:
            # Encriptar la clave con bcrypt
            hashed = bcrypt.hashpw(clave.encode("utf-8"), bcrypt.gensalt())

            # Insertar el nuevo usuario en la tabla
            cur.execute("""
                INSERT INTO usuarios (nombre, usuario, clave, rol)
                VALUES (%s, %s, %s, %s)
            """, (nombre, usuario, hashed.decode("utf-8"), rol))

        conexion.commit()
        print(f"✅ Usuario '{usuario}' creado con éxito")

    except Exception as e:
        print(f"⚠️ Error al crear usuario: {e}")
        conexion.rollback()

    finally:
        desconectar(conexion)


# Ejemplo de uso:
crear_usuario("Administrador", "Administrador", "123456", rol="administrador")

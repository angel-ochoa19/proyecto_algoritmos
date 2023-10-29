# Programa que envia emails con archivos adjuntos
from email import message
from fileinput import filename
import mimetypes
import smtplib
import ssl
from email.message import EmailMessage
import os

SERVIDOR = "smtp.gmail.com"
PUERTO = 587
CONTRASENA = os.getenv('GOOGLE_APP_PASS')
USUARIO = os.getenv("GOOGLE_APP_EMAIL")


def enviar_mensaje(asunto, cuerpo, destinatario, titulo, nombre_archivo, ruta_de_adjunto):
    # Contenido del mensaje
    mensaje = EmailMessage()
    mensaje["Subject"] = asunto
    mensaje["From"] = USUARIO
    mensaje["To"] = destinatario

    # Cuerpo del mensaje
    mensaje.set_content(cuerpo)

    mensaje.add_alternative(f"""
     <p>
       <h1> {titulo} </h1>
     </p>
    """, subtype="html")

    # Obtener la codificacion del archivo.
    ctype, encondig = mimetypes.guess_type(nombre_archivo)
    if ctype is None or encondig is not None:
        ctype = "application/octet-stream"

    tipo_principal, sub_typo = ctype.split("/", 1)
    # Abrimos el archivo que queremos enviar
    archivo = open(os.path.join(ruta_de_adjunto, nombre_archivo), 'rb')

    # Agregamos el archivo al mensaje
    mensaje.add_attachment(archivo.read(), maintype=tipo_principal,
                           subtype=sub_typo, filename=nombre_archivo)

    # Crear una conexion ssl
    context = ssl.create_default_context()
    smtp = smtplib.SMTP(SERVIDOR, PUERTO)
    smtp.starttls()
    smtp.login(USUARIO, CONTRASENA)
    smtp.send_message(mensaje)


enviar_mensaje("Correo con adjunto", "Hola te envio un correo con adjunto", "aochoac3@miumg.edu.gt", "Tarea2.docx", "prueba.docx", "C:\Users\21\OneDrive\Documentos\Universidad\Semestre 2\Algoritmos\Proyecto Final")
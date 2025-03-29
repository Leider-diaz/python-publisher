from fastapi import FastAPI, HTTPException
import pika

app = FastAPI()

RABBITMQ_HOST = "10.6.101.93"
QUEUE_NAME = "cola4"

@app.post("/enviar")
def enviar_mensaje(mensaje: dict):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBITMQ_HOST))
        channel = connection.channel()

        mensaje_texto = mensaje.get("texto", "Mensaje vacío")
        channel.basic_publish(exchange='',
                              routing_key=QUEUE_NAME,
                              body=mensaje_texto)

        connection.close()

        return {"estado": "Mensaje enviado", "contenido": mensaje_texto}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
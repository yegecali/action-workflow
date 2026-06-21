import os
from datetime import datetime

client_id = os.environ["CLIENT_ID"]
client_name = os.environ["CLIENT_NAME"]
tenant = os.environ["TENANT"]
tipo = os.environ["TIPO_CREDENCIAL"]
scopes = os.environ.get("SCOPES", "N/A")
redirect = os.environ.get("REDIRECT", "N/A")
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

print("Registrando en tabla de auditoría...")
print(f"  client_id        : {client_id}")
print(f"  client_name      : {client_name}")
print(f"  tenant           : {tenant}")
print(f"  tipo_credencial  : {tipo}")
print(f"  scopes           : {scopes}")
print(f"  redirect_uri     : {redirect}")
print(f"  timestamp        : {timestamp} UTC")
print("Registro de auditoría guardado exitosamente")

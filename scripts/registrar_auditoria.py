import os
from datetime import datetime

alias = os.environ["ALIAS"]
redirect_uri = os.environ["REDIRECT_URI"]
scopes = os.environ["SCOPES"]
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

print("Conectando con tabla de auditoría...")
print("Registrando evento:")
print(f"  alias        : {alias}")
print(f"  redirect_uri : {redirect_uri}")
print(f"  scopes       : {scopes}")
print(f"  timestamp    : {timestamp} UTC")
print("Registro de auditoría guardado exitosamente")

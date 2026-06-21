import os

client_id = os.environ["CLIENT_ID"]
scopes = os.environ["SCOPES"]
tipo = os.environ["TIPO_CREDENCIAL"]

print(f"Agregando scopes al SP {client_id}...")
print(f"  tipo    : {tipo}")
print(f"  scopes  : {scopes}")
print("Scopes agregados, esperando propagación...")

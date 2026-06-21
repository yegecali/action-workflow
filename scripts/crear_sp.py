import os
import uuid

client_name = os.environ["CLIENT_NAME"]
tenant = os.environ["TENANT"]

print(f"Creando Service Principal para: {client_name}")
print(f"Tenant: {tenant}")

client_id = f"SP-{uuid.uuid4().hex[:8].upper()}"
client_secret = f"SECRET-{uuid.uuid4().hex.upper()}"

print(f"Service Principal creado")
print(f"  client_id     : {client_id}")
print(f"  client_secret : {client_secret[:8]}****")

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"client_id={client_id}\n")
    f.write(f"client_secret={client_secret}\n")

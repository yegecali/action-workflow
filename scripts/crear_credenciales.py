import os
import uuid

client_name = os.environ["CLIENT_NAME"]

print(f"Creando credencial para: {client_name}")

client_id = f"CLIENT-{uuid.uuid4().hex[:8].upper()}"
client_secret = f"SECRET-{uuid.uuid4().hex.upper()}"

print(f"  client_id     : {client_id}")
print(f"  client_secret : {client_secret[:8]}****  (enmascarado)")
print("Credencial creada exitosamente")

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"client_id={client_id}\n")
    f.write(f"client_secret={client_secret}\n")

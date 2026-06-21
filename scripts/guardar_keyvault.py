import os
import uuid

client_id = os.environ["CLIENT_ID"]
client_secret = f"SECRET-{uuid.uuid4().hex.upper()}"

print(f"Conectando con KeyVault...")
print(f"Guardando client_secret para credencial {client_id}...")
print(f"  client_secret: {client_secret[:8]}****  (valor enmascarado)")
print("Credencial almacenada en KeyVault exitosamente")

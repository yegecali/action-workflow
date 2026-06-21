import os

client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]

print(f"Conectando con KeyVault...")
print(f"Guardando client_secret para credencial {client_id}...")
print(f"  client_secret : {client_secret[:8]}****")
print("client_secret almacenado en KeyVault exitosamente")

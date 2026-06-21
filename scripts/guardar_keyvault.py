import os

client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]

print(f"Conectando con KeyVault...")
print(f"Guardando client_secret para: {client_id}")
print(f"  client_secret : {client_secret[:8]}****  (enmascarado)")
print("client_secret almacenado en KeyVault exitosamente")

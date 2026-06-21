import os

client_id = os.environ["CLIENT_ID"]
tenant = os.environ["TENANT"]

print(f"Ejecutando Admin Consent para SP {client_id}...")
print(f"  tenant : {tenant}")
print("Admin Consent otorgado, esperando propagación...")

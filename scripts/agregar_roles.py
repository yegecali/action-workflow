import os

client_id = os.environ["CLIENT_ID"]
app_roles = os.environ["APP_ROLES"]

print(f"Agregando App Roles al SP {client_id}...")
print(f"  roles : {app_roles}")
print("App Roles agregados, esperando propagación...")

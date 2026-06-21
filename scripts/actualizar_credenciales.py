import os

client_id = os.environ["CLIENT_ID"]
tenant = os.environ["TENANT"]
tipo = os.environ["TIPO_CREDENCIAL"]
scopes = os.environ.get("SCOPES", "")
redirect = os.environ.get("REDIRECT", "")

print(f"Actualizando credencial {client_id}...")
print(f"  tenant           : {tenant}")
print(f"  tipo_credencial  : {tipo}")

if scopes:
    print(f"  scopes           : {scopes}")

if tipo == "ac":
    if not redirect:
        raise ValueError("redirect es requerido para tipo 'ac' (authorization code)")
    print(f"  redirect_uri     : {redirect}")

print("Credencial actualizada exitosamente")

import os

client_id = os.environ["CLIENT_ID"]
alias = os.environ["ALIAS"]

redirect_uri = "https://mi-app.com/callback"
scopes = "openid profile email"

print(f"Actualizando credencial {client_id} ({alias})...")
print(f"Agregando redirect_uri : {redirect_uri}")
print(f"Agregando scopes       : {scopes}")
print("Credencial actualizada exitosamente")

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"client_id={client_id}\n")
    f.write(f"alias={alias}\n")
    f.write(f"redirect_uri={redirect_uri}\n")
    f.write(f"scopes={scopes}\n")

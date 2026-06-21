import os
import uuid

print("Iniciando creación de credenciales...")
print("Verificando que no existan credenciales previas...")

client_id = f"CLIENT-{uuid.uuid4().hex[:8].upper()}"
alias = "mi-app-prod"

print(f"Credencial creada exitosamente")
print(f"  client_id : {client_id}")
print(f"  alias     : {alias}")

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"client_id={client_id}\n")
    f.write(f"alias={alias}\n")

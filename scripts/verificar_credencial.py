import os
import sys
import random

client_id = os.environ["CLIENT_ID"]

# Simula verificar si la credencial ya está disponible
# En un caso real harías una llamada a tu API/directorio
disponible = random.choice([True, True, True, False])

if disponible:
    print(f"Credencial {client_id} disponible y lista")
    sys.exit(0)
else:
    print(f"Credencial {client_id} aún no disponible, reintentando...")
    sys.exit(1)

import os
import sys
import random

client_id = os.environ["CLIENT_ID"]

# En producción: verificar via Graph API que el consent está activo
activo = random.choices([True, False], weights=[75, 25])[0]

if activo:
    print(f"Admin Consent activo para SP {client_id}")
    sys.exit(0)
else:
    print(f"Admin Consent aún no activo para SP {client_id}, reintentando...")
    sys.exit(1)

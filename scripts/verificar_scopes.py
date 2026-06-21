import os
import sys
import random

client_id = os.environ["CLIENT_ID"]

# En producción: verificar via Graph API que los scopes están asignados
propagado = random.choices([True, False], weights=[75, 25])[0]

if propagado:
    print(f"Scopes propagados correctamente en SP {client_id}")
    sys.exit(0)
else:
    print(f"Scopes aún no propagados en SP {client_id}, reintentando...")
    sys.exit(1)

import os
import sys
import random

client_id = os.environ["CLIENT_ID"]

# En producción: GET a Graph API para confirmar que el SP existe
disponible = random.choices([True, False], weights=[75, 25])[0]

if disponible:
    print(f"SP {client_id} disponible en el directorio")
    sys.exit(0)
else:
    print(f"SP {client_id} aún no propagado, reintentando...")
    sys.exit(1)

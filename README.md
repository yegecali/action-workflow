# action-workflow

Automatización de gestión de credenciales (Service Principals) en Azure AD mediante GitHub Actions y Python.

## Flujo principal

```
tests → crear_sp → agregar_scopes → grant_admin → app_roles (opcional)
                                                        ↓
                                              keyvault + auditoria
                                                        ↓
                                          notificar_exito | notificar_fallo
```

Cada job valida la propagación del cambio en Azure antes de continuar con el siguiente paso.

## Inputs del workflow

| Input | Requerido | Descripción |
|---|---|---|
| `operacion` | Sí | `crear_actualizar` o `solo_actualizar` |
| `client_name` | Sí | Nombre del cliente / aplicación |
| `tenant` | Sí | Tenant de Azure AD |
| `tipo_credencial` | Sí | `cc` (client credentials) o `ac` (authorization code) |
| `client_id` | Solo en `solo_actualizar` | Client ID del SP existente |
| `scopes` | No | Scopes a asignar |
| `redirect` | Solo si `tipo=ac` | Redirect URI |
| `app_roles` | No | App Roles separados por coma |

## Estructura del proyecto

```
.github/workflows/
├── hola.yml                    # Workflow de práctica
└── credenciales.yml            # Workflow principal

scripts/
├── service_principal/
│   ├── crear.py                # Crea el Service Principal
│   └── verificar.py            # Polling hasta confirmar propagación
├── configuracion/
│   ├── agregar_scopes.py       # Asigna scopes al SP
│   ├── verificar_scopes.py
│   ├── grant_admin.py          # Otorga Admin Consent
│   ├── verificar_grant.py
│   ├── agregar_roles.py        # Agrega App Roles (opcional)
│   └── verificar_roles.py
├── keyvault/
│   └── guardar.py              # Guarda el client_secret en KeyVault
└── auditoria/
    └── registrar.py            # Registra el evento en tabla de auditoría

tests/
├── conftest.py                 # Fixture compartido run_script
├── test_service_principal.py
├── test_configuracion.py
├── test_keyvault.py
└── test_auditoria.py
```

## Ejecución local de tests

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Comportamiento ante fallos

- Si los **tests** fallan → ningún job toca Azure.
- Si un **job intermedio** falla → los jobs dependientes se cancelan automáticamente.
- El job `notificar_fallo` siempre corre al final si algo falló, reportando el resultado de cada job.
- Cada operación tiene un **timeout de 15 minutos** y un **máximo de 12 reintentos** (3 minutos) para verificar propagación.

## Concurrencia

El workflow usa un grupo de concurrencia por `client_name` + `tenant`. Si se lanza dos veces para el mismo cliente, la segunda ejecución espera en cola hasta que la primera termine.

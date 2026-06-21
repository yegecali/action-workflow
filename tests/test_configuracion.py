import pytest


VALID_SCOPES_ENV = {
    "CLIENT_ID": "SP-ABC123",
    "SCOPES": "openid profile email",
    "TIPO_CREDENCIAL": "cc",
}

VALID_GRANT_ENV = {
    "CLIENT_ID": "SP-ABC123",
    "TENANT": "mi-tenant",
}

VALID_ROLES_ENV = {
    "CLIENT_ID": "SP-ABC123",
    "APP_ROLES": "Role.Read,Role.Write",
}


def test_agregar_scopes_exitoso(run_script):
    result, _ = run_script("scripts/configuracion/agregar_scopes.py", VALID_SCOPES_ENV)
    assert result.returncode == 0


def test_agregar_scopes_falla_sin_client_id(run_script):
    env = {k: v for k, v in VALID_SCOPES_ENV.items() if k != "CLIENT_ID"}
    result, _ = run_script("scripts/configuracion/agregar_scopes.py", env)
    assert result.returncode != 0


def test_verificar_scopes_retorna_codigo_valido(run_script):
    result, _ = run_script("scripts/configuracion/verificar_scopes.py", {"CLIENT_ID": "SP-ABC123"})
    assert result.returncode in [0, 1]


def test_grant_admin_exitoso(run_script):
    result, _ = run_script("scripts/configuracion/grant_admin.py", VALID_GRANT_ENV)
    assert result.returncode == 0


def test_grant_admin_falla_sin_tenant(run_script):
    result, _ = run_script("scripts/configuracion/grant_admin.py", {"CLIENT_ID": "SP-ABC123"})
    assert result.returncode != 0


def test_verificar_grant_retorna_codigo_valido(run_script):
    result, _ = run_script("scripts/configuracion/verificar_grant.py", {"CLIENT_ID": "SP-ABC123"})
    assert result.returncode in [0, 1]


def test_agregar_roles_exitoso(run_script):
    result, _ = run_script("scripts/configuracion/agregar_roles.py", VALID_ROLES_ENV)
    assert result.returncode == 0


def test_agregar_roles_falla_sin_app_roles(run_script):
    result, _ = run_script("scripts/configuracion/agregar_roles.py", {"CLIENT_ID": "SP-ABC123"})
    assert result.returncode != 0


def test_verificar_roles_retorna_codigo_valido(run_script):
    result, _ = run_script("scripts/configuracion/verificar_roles.py", {"CLIENT_ID": "SP-ABC123"})
    assert result.returncode in [0, 1]

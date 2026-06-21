import pytest


SCRIPT_CREAR = "scripts/service_principal/crear.py"
SCRIPT_VERIFICAR = "scripts/service_principal/verificar.py"

VALID_ENV = {"CLIENT_NAME": "test-app", "TENANT": "mi-tenant"}


def test_crear_exitoso_con_inputs_validos(run_script):
    result, _ = run_script(SCRIPT_CREAR, VALID_ENV)
    assert result.returncode == 0


def test_crear_genera_client_id_con_prefijo(run_script):
    _, outputs = run_script(SCRIPT_CREAR, VALID_ENV)
    assert "client_id" in outputs
    assert outputs["client_id"].startswith("SP-")


def test_crear_genera_client_secret_con_prefijo(run_script):
    _, outputs = run_script(SCRIPT_CREAR, VALID_ENV)
    assert "client_secret" in outputs
    assert outputs["client_secret"].startswith("SECRET-")


def test_crear_falla_sin_client_name(run_script):
    result, _ = run_script(SCRIPT_CREAR, {"TENANT": "mi-tenant"})
    assert result.returncode != 0


def test_crear_falla_sin_tenant(run_script):
    result, _ = run_script(SCRIPT_CREAR, {"CLIENT_NAME": "test-app"})
    assert result.returncode != 0


def test_verificar_retorna_codigo_valido(run_script):
    result, _ = run_script(SCRIPT_VERIFICAR, {"CLIENT_ID": "SP-ABC123"})
    assert result.returncode in [0, 1]


def test_verificar_falla_sin_client_id(run_script):
    result, _ = run_script(SCRIPT_VERIFICAR, {})
    assert result.returncode != 0

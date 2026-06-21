VALID_ENV = {
    "CLIENT_ID": "SP-ABC123",
    "CLIENT_NAME": "test-app",
    "TENANT": "mi-tenant",
    "TIPO_CREDENCIAL": "cc",
    "SCOPES": "openid profile",
    "REDIRECT": "https://mi-app.com/callback",
}


def test_registrar_exitoso_con_todos_los_campos(run_script):
    result, _ = run_script("scripts/auditoria/registrar.py", VALID_ENV)
    assert result.returncode == 0


def test_registrar_exitoso_sin_campos_opcionales(run_script):
    env = {k: v for k, v in VALID_ENV.items() if k not in ("SCOPES", "REDIRECT")}
    result, _ = run_script("scripts/auditoria/registrar.py", env)
    assert result.returncode == 0


def test_registrar_falla_sin_client_id(run_script):
    env = {k: v for k, v in VALID_ENV.items() if k != "CLIENT_ID"}
    result, _ = run_script("scripts/auditoria/registrar.py", env)
    assert result.returncode != 0


def test_registrar_falla_sin_tenant(run_script):
    env = {k: v for k, v in VALID_ENV.items() if k != "TENANT"}
    result, _ = run_script("scripts/auditoria/registrar.py", env)
    assert result.returncode != 0

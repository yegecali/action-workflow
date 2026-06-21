VALID_ENV = {
    "CLIENT_ID": "SP-ABC123",
    "CLIENT_SECRET": "SECRET-ABCDEF123456",
}


def test_guardar_exitoso(run_script):
    result, _ = run_script("scripts/keyvault/guardar.py", VALID_ENV)
    assert result.returncode == 0


def test_guardar_falla_sin_client_id(run_script):
    result, _ = run_script("scripts/keyvault/guardar.py", {"CLIENT_SECRET": "SECRET-ABC"})
    assert result.returncode != 0


def test_guardar_falla_sin_client_secret(run_script):
    result, _ = run_script("scripts/keyvault/guardar.py", {"CLIENT_ID": "SP-ABC123"})
    assert result.returncode != 0

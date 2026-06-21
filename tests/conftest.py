import os
import subprocess
import sys
import pytest


@pytest.fixture
def run_script(tmp_path):
    def _run(script_path, env_vars):
        output_file = tmp_path / "github_output.env"
        output_file.touch()

        env = os.environ.copy()
        env.update(env_vars)
        env["GITHUB_OUTPUT"] = str(output_file)

        result = subprocess.run(
            [sys.executable, script_path],
            env=env,
            capture_output=True,
            text=True
        )

        outputs = {}
        with open(output_file) as f:
            for line in f:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    outputs[key] = value

        return result, outputs

    return _run

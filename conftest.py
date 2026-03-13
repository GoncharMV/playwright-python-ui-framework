import os.path
from dotenv import load_dotenv

import pytest

from config import Settings
from core.browser import Browser

ALLOWED_ENV = ["stage", "prod"]

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="prod",
        help=f"Environment to run tests: {ALLOWED_ENV}"
    )


@pytest.fixture(scope="session", autouse=True)
def load_env(request):
    env_name = request.config.getoption("--env")

    if env_name not in ALLOWED_ENV:
        raise ValueError(f"Unsupported env {env_name}. Allowed values: {ALLOWED_ENV}")

    env_file = f"env/.env.{env_name}"

    if not os.path.exists(env_file):
        raise FileNotFoundError(f"File {env_file} not found")

    print(f"Loading environment: {env_name}")
    load_dotenv(env_file)

    print(f"BROWSER: {os.getenv("BROWSER")}")
    print(f"BASE_URL: {os.getenv("BASE_URL")}")
    print(f"TIMEOUT: {os.getenv("TIMEOUT")}")


@pytest.fixture(scope="function", autouse=True)
def browser_settings(settings):
    pass


@pytest.fixture(scope="session")
def settings(load_env) -> Settings:
    return Settings()

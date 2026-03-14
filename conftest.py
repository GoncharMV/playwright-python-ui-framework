import os.path
from dotenv import load_dotenv

import pytest

from config import Settings
from core.browser import Browser, BrowserConfig
from core.element import Element

ALLOWED_ENV = ["stage", "prod"]

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="prod",
        help=f"Environment to run tests: {ALLOWED_ENV}"
    )
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help=f"Run tests in headed mode"
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
    )
    parser.addoption(
        "--slowmo",
        action="store",
        default="0",
        help=f"Run tests in slowmo mode"
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

    print(f"BROWSER: {request.config.getoption('--browser')}")
    print(f"HEADLESS: {request.config.getoption('--headed')}")
    print(f"BASE_URL: {os.getenv("BASE_URL")}")


@pytest.fixture(scope="function", autouse=True)
def browser(settings, request):
    is_headed = not request.config.getoption("--headed")
    br = request.config.getoption("--browser")
    slow_mo = request.config.getoption("--slowmo")

    config = BrowserConfig(
        base_url=settings.base_url,
        browser=br,
        headless=is_headed,
        slowmo=slow_mo,
    )

    browser = Browser(config)
    Element.set_browser(browser)

    yield browser

    Element.set_browser(None)

    browser.close()


@pytest.fixture(scope="session")
def settings(load_env) -> Settings:
    return Settings()

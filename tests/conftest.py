from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app


@pytest.fixture
def client():
    with TestClient(app.app, follow_redirects=False) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def reset_activities():
    original_activities = deepcopy(app.activities)
    yield
    app.activities.clear()
    app.activities.update(original_activities)

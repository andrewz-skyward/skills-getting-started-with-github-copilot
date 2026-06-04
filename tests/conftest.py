from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activities before and after each test."""
    original = deepcopy(activities)

    # Arrange
    activities.clear()
    activities.update(deepcopy(original))

    yield

    # Cleanup
    activities.clear()
    activities.update(deepcopy(original))


@pytest.fixture
def client():
    # Arrange
    test_client = TestClient(app)

    # Act/Assert handled by individual tests
    return test_client

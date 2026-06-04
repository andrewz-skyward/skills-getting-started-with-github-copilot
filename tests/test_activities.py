def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert expected_activity in payload


def test_get_activities_has_expected_activity_shape(client):
    # Arrange
    activity_name = "Programming Class"

    # Act
    response = client.get("/activities")
    activity = response.json()[activity_name]

    # Assert
    assert response.status_code == 200
    assert "description" in activity
    assert "schedule" in activity
    assert "max_participants" in activity
    assert "participants" in activity
    assert isinstance(activity["participants"], list)

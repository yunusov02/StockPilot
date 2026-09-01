from app.models.users import UserRole, Users


def test_user_creation() -> None:
    user = Users(
        username="testuser", email="testuser@example.com", hashed_password="hashed_password"
    )
    assert user.username == "testuser"
    assert user.email == "testuser@example.com"
    assert user.hashed_password == "hashed_password"


def test_user_role() -> None:
    user = Users(
        username="testuser", email="testuser@example.com", hashed_password="hashed_password"
    )
    assert user.role == UserRole.STAFF.value

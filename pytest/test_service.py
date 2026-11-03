from unittest import mock
import service

@mock.patch("service.get_user")
def test_get_user(mock_user):
    mock_user.return_value="Aditya"
    username=service.get_user(1)
    assert username=="Aditya"
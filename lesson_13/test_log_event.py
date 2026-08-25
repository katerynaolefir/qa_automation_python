import pytest
from login import log_event


def read_last_line():
    with open("login_system.log") as f:
        last_row = f.readlines()[-1]
    return last_row


@pytest.mark.parametrize(
    "status, expected_level",
    [
        ("success", "INFO"),
        ("expired", "WARNING"),
        ("failed", "ERROR"),
    ]
)
def test_log_event_status(status, expected_level):
    username = "Kate"
    log_event(username, status)
    last_line = read_last_line()

    assert expected_level in last_line
    assert username in last_line
    assert status in last_line


def test_log_event_unknown_status():
    username = "Kate"
    status = "something_else"
    log_event(username, status)
    last_line = read_last_line()

    assert "ERROR" in last_line
    assert username in last_line
    assert status in last_line
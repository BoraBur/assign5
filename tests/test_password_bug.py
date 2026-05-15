import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.user_profile import UserProfile


def test_password_valid_starts_with_lowercase():
    assert UserProfile.valid_password("secureP@ss1") is True


def test_password_valid_starts_with_digit():
    assert UserProfile.valid_password("1Secure@ab") is True


def test_password_valid_starts_with_special():
    assert UserProfile.valid_password("@Secure1ab") is True

import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.user_profile import UserProfile
from src.location import Location


def make_profile(dob: str) -> UserProfile:
    return UserProfile(
        name="John Smith",
        email="john.smith@example.com",
        password="Secure123!",
        dob=dob,
        location=Location(city="LosAngeles", state="CA", country="US"),
    )


def test_age_birthday_already_passed_this_month():
    profile = make_profile("1990-01-01")
    ref = datetime(2025, 1, 15)
    assert profile.get_age(ref) == 35


def test_age_birthday_is_today():
    profile = make_profile("1990-06-10")
    ref = datetime(2025, 6, 10)
    assert profile.get_age(ref) == 35


def test_age_birthday_not_yet_this_year():
    profile = make_profile("1990-12-31")
    ref = datetime(2025, 6, 10)
    assert profile.get_age(ref) == 34

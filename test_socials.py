import pytest

from socials import ayikla
from socials import baloncuksort as bs


@pytest.mark.parametrize(
    "adresler, expected_adresler",
    [
        (
            ["dsajfhklajhfda.kadjfaj"],
            [],
        ),
        (
            ["https://twitter.com/sadikkuzu_mba"],
            ["https://twitter.com/sadikkuzu_mba"],
        ),
    ],
)
def test_ayikla(adresler, expected_adresler):
    ayikla(adresler)
    assert adresler == expected_adresler


@pytest.mark.parametrize(
    "liste, balon, expected_liste",
    [
        ([], "", []),
        ([], "sadikkuzu", []),
        (
            [
                {
                    "url": "https://twitter.com/dummy",
                    "username": "dummy",
                },
                {
                    "url": "https://twitter.com/sadikkuzu_mba",
                    "username": "sadikkuzu",
                },
            ],
            "sadikkuzu",
            [
                {
                    "url": "https://twitter.com/sadikkuzu_mba",
                    "username": "sadikkuzu",
                },
                {
                    "url": "https://twitter.com/dummy",
                    "username": "dummy",
                },
            ],
        ),
        (
            [
                {"url": "https://twitter.com/dummy", "username": "dummy"},
                {"url": "https://twitter.com/dummy2", "username": "dummy2"},
            ],
            "sadikkuzu",
            [
                {"url": "https://twitter.com/dummy", "username": "dummy"},
                {"url": "https://twitter.com/dummy2", "username": "dummy2"},
            ],
        ),
        (
            [
                {"url": "https://twitter.com/dummy", "username": "dummy"},
                {"url": "https://twitter.com/dummy2", "username": "dummy2"},
                {
                    "url": "https://twitter.com/sadikkuzu_mba",
                    "username": "sadikkuzu",
                },
            ],
            "sadikkuzu",
            [
                {
                    "url": "https://twitter.com/sadikkuzu_mba",
                    "username": "sadikkuzu",
                },
                {"url": "https://twitter.com/dummy", "username": "dummy"},
                {"url": "https://twitter.com/dummy2", "username": "dummy2"},
            ],
        ),
    ],
)
def test_baloncuksort(liste, balon, expected_liste):
    assert bs(liste, balon) == expected_liste

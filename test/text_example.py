import pytest


def test_example():
    assert 1 + 1 == 2


def test_imports():
    try:
        import zerokey
    except Exception as e:
        pytest.fail(f"Failed to import zerokey: {e}")

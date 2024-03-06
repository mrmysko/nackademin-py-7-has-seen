import pytest

fn_name = "has_seen"


class ImportDetailsError(Exception):
    pass


try:
    import uppgift

    has_seen = getattr(uppgift, fn_name)

    if not callable(has_seen):
        raise ImportDetailsError(f"Function {fn_name} is not callable")

    if not has_seen.__code__.co_argcount == 1:
        raise ImportDetailsError(f"Function {fn_name} must take exactly one argument")

    def test_has_seen():
        assert has_seen(1) == False, "Failed at the first call with 1"
        assert has_seen("a") == False, "Failed at the first call with 'a'"
        assert has_seen(1) == True, "Failed at the second call with 1"
        assert has_seen(2) == False, "Failed at the first call with 2"
        assert has_seen("a") == True, "Failed at the second call with 'a'"

except ImportError:
    pytest.fail(f"Function {fn_name} has not been implemented")

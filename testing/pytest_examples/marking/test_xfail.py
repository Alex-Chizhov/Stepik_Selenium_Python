# https://docs.pytest.org/en/latest/skipping.html#strict-parameter

import pytest

# Меняет поведение @pytest.mark.xfail(strict=True)
# таким образом что тест падает и при  XFAIL и при XPASS
# при передаче параметра "strict=True"
@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
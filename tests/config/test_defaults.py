from pytest import mark

from wordgoal.config import Defaults


@mark.parametrize("defaults, expect", [(Defaults(parent=None, values={"goal": 3}), 3)])
def test_goal__values_has_goal(defaults: Defaults, expect: int) -> None:
    assert defaults.goal == expect

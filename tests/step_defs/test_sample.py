from pytest_bdd import scenario, given, when, then

@scenario('../features/sample.feature', 'Adding sample')
def test_add():
    pass

@given("You have 5")
def have_five():
    return 5


@when("You add 3")
def add_three(have_five):
    return have_five + 3


@then("You have 8")
def step_impl(add_three):
    assert add_three == 8
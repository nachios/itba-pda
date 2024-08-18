import add as my_module

def test_add():
    a=3
    b=5
    expected_output=8

    actual_output = my_module.add(a,b)

    assert actual_output==expected_output, f'Expected {expected_output} but got {actual_output}'

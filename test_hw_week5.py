from hw_week5 import hw_week5


def test_the_multiplication_table_output(capsys):
    hw_week5()
    captured = capsys.readouterr()
    expect_output = ''
    for x in range(1, 10):
        for y in range(1, 10):
            expect_output += f'{str(x)}x{str(y)}={str(x*y)}\n'
    assert captured.out == expect_output

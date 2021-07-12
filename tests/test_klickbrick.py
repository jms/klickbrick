import pytest
import klickbrick


def test_version():
    assert klickbrick.__version__ == '0.1.1'


@pytest.mark.parametrize("args, response", [
    (["hello"], "Hello World\n"),
    (["hello", "--name", "Ole"], "Hello Ole\n"),
    (["hello", "-n", "Joe"], "Hello Joe\n"),
])
def test_cli_default(args, response, capsys):
    klickbrick.Klickbrick(args)
    captured = capsys.readouterr()
    assert captured.out == response


def test_cli_no_option():
    with pytest.raises(SystemExit):
        klickbrick.Klickbrick([])

from main import Cicd


def test_cicd_output(capsys):
    Cicd()
    captured = capsys.readouterr()
    assert "Hello try CI/CD" in captured.out

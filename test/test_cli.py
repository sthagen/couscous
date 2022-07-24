from couscous import cli


def test_cli():
    assert cli.main([]) is None

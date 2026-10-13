from assistant.rules import reply


def test_greeting():
    assert "Hello" in reply("hi")


def test_partial_office_name():
    assert "1.101" in reply("where is training")
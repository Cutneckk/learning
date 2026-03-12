import asyncio
from unittest.mock import patch

from main_app.countdown import countdown


def test_countdown_output():
    printed = []

    def fake_print(text):
        printed.append(text)

    with patch('builtins.print', fake_print):
        with patch('asyncio.sleep'):
            asyncio.run(countdown("Test", 3))

    assert printed == [3, 2, 1, "Test: Пуск!"]
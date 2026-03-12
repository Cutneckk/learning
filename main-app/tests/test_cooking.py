import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

from main_app.cooking import main

def test_main():
    printed = []

    fake_sleep = AsyncMock()
    fake_time = MagicMock(side_effect=[0, 10])

    with (
        patch('builtins.print', lambda x: printed.append(x)),
        patch('asyncio.sleep', fake_sleep),
        patch('time.time', fake_time)
    ):
        asyncio.run(main())

    assert 'Vegetables ready' in printed
    assert 'Meat ready' in printed
    assert 'Rise ready' in printed
    assert any('Full cooking time' in str(p) for p in printed)
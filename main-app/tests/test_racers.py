import asyncio
from unittest.mock import AsyncMock, patch

from main_app.race import main


def test_main():
    printed = []

    def fake_print(*args):
        printed.append(' '.join(str(a) for a in args))

    with patch('builtins.print', fake_print), patch('asyncio.sleep', new_callable=AsyncMock):
        asyncio.run(main())

    assert 'lightning финишировал!' in printed
    assert 'arrow финишировал!' in printed
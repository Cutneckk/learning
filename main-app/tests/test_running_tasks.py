import asyncio
from unittest.mock import AsyncMock, patch

from main_app.running_tasks import main

def test_main():
    printed = []

    def fake_print(*args):
        printed.append(' '.join(str(a) for a in args))

    with patch('builtins.print', fake_print), patch('asyncio.sleep', new_callable=AsyncMock):
        asyncio.run(main())

    assert 'Фоновая задача начала работу' in printed
    assert 'Основная задача продолжает работу' in printed
    assert 'Основная программа работает' in printed
    assert 'Фоновая задача завершила работу' in printed
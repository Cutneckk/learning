import asyncio
from unittest.mock import MagicMock, patch

from main_app.check_url_status import check_status


async def async_mock_return(value):
    return value


def test_check_status():
    fake_response = MagicMock()
    fake_response.status = 200

    fake_session = MagicMock()

    context = MagicMock()
    context.__aenter__ = lambda self: async_mock_return(fake_response)
    context.__aexit__ = lambda self, *args: async_mock_return(None)

    fake_session.get.return_value = context

    with patch('builtins.print') as mock_print:
        asyncio.run(check_status(fake_session, "http://vk.com"))
        mock_print.assert_any_call("http://vk.com: OK")
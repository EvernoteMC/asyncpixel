"""Test bazaar."""
import datetime

import pytest
from aioresponses import aioresponses
from asyncpixel import Hypixel
from asyncpixel.exceptions import ApiNoSuccess
from asyncpixel.exceptions import InvalidApiKey
from asyncpixel.exceptions import RateLimitError
from tests.utils import generate_key


@pytest.mark.asyncio
async def test_rate_limit() -> None:
    """Test bazaar."""
    key = generate_key()
    with aioresponses() as m:
        m.get(
            f"https://api.hypixel.net/test?key={str(key)}",
            status=429,
            headers={"Retry-After": "5"},
            payload={"success": False, "cause": "Key throttle!", "throttle": True},
        )
        client = Hypixel(api_key=str(key))
        with pytest.raises(RateLimitError) as e:
            await client._get("test")
            assert str(e) == "Entered API key is not valid"
        await client.close()


@pytest.mark.asyncio
async def test_invalid_key() -> None:
    """Test bazaar."""
    key = generate_key()
    with aioresponses() as m:
        m.get(
            f"https://api.hypixel.net/test?key={str(key)}",
            status=403,
            payload={"success": False, "cause": "Invalid API key"},
        )
        client = Hypixel(api_key=str(key))
        with pytest.raises(InvalidApiKey) as e:
            await client._get("test")
            assert str(e) == "The hypixel API ratelimit was reached!"
        await client.close()


@pytest.mark.asyncio
async def test_api_error() -> None:
    """Test bazaar."""
    key = generate_key()
    with aioresponses() as m:
        m.get(
            f"https://api.hypixel.net/test?key={str(key)}",
            status=502,
            payload={"success": False, "cause": "Error"},
        )
        client = Hypixel(api_key=str(key))
        with pytest.raises(ApiNoSuccess) as e:
            await client._get("test")
            assert str(e) == "The test endpoint encounted an error on the hypixel side."
        await client.close()


def test_str_api_error() -> None:
    """Check api error."""
    e = ApiNoSuccess("test")
    assert str(e) == e.__str__()


def test_str_invalid_key() -> None:
    """Check api error."""
    e = InvalidApiKey()
    assert str(e) == e.__str__()


def test_str_rate_limit() -> None:
    """Check api error."""
    e = RateLimitError(datetime.datetime.now())
    assert str(e) == e.__str__()

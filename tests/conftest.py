from __future__ import annotations

import os
import asyncio
import logging
from typing import TYPE_CHECKING, Iterator, AsyncIterator

import pytest

from anthropic_bedrock import AnthropicBedrock, AsyncAnthropicBedrock

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest

pytest.register_assert_rewrite("tests.utils")

logging.getLogger("anthropic_bedrock").setLevel(logging.DEBUG)


@pytest.fixture(scope="session")
def event_loop() -> Iterator[asyncio.AbstractEventLoop]:
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

aws_secret_key = "<secret key>"
aws_access_key = "<access key>"
aws_region = "us-east-2"


@pytest.fixture(scope="session")
def client(request: FixtureRequest) -> Iterator[AnthropicBedrock]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    with AnthropicBedrock(
        base_url=base_url,
        aws_secret_key=aws_secret_key,
        aws_access_key=aws_access_key,
        aws_region=aws_region,
        _strict_response_validation=strict,
    ) as client:
        yield client


@pytest.fixture(scope="session")
async def async_client(request: FixtureRequest) -> AsyncIterator[AsyncAnthropicBedrock]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    async with AsyncAnthropicBedrock(
        base_url=base_url,
        aws_secret_key=aws_secret_key,
        aws_access_key=aws_access_key,
        aws_region=aws_region,
        _strict_response_validation=strict,
    ) as client:
        yield client

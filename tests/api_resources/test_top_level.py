# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from anthropic_bedrock import AnthropicBedrock, AsyncAnthropicBedrock
from anthropic_bedrock._client import AnthropicBedrock, AsyncAnthropicBedrock

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
aws_secret_key = "<secret key>"
aws_access_key = "<access key>"
aws_region = "us-east-2"


class TestTopLevel:
    strict_client = AnthropicBedrock(
        base_url=base_url,
        aws_secret_key=aws_secret_key,
        aws_access_key=aws_access_key,
        aws_region=aws_region,
        _strict_response_validation=True,
    )
    loose_client = AnthropicBedrock(
        base_url=base_url,
        aws_secret_key=aws_secret_key,
        aws_access_key=aws_access_key,
        aws_region=aws_region,
        _strict_response_validation=False,
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    def test_count_tokens(self) -> None:
        tokens = self.strict_client.count_tokens("hello world!")
        assert tokens == 3


class TestAsyncTopLevel:
    strict_client = AsyncAnthropicBedrock(
        base_url=base_url,
        aws_secret_key=aws_secret_key,
        aws_access_key=aws_access_key,
        aws_region=aws_region,
        _strict_response_validation=True,
    )
    loose_client = AsyncAnthropicBedrock(
        base_url=base_url,
        aws_secret_key=aws_secret_key,
        aws_access_key=aws_access_key,
        aws_region=aws_region,
        _strict_response_validation=False,
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    async def test_count_tokens(self) -> None:
        tokens = await self.strict_client.count_tokens("hello world!")
        assert tokens == 3

# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from anthropic_bedrock import AnthropicBedrock, AsyncAnthropicBedrock
from anthropic_bedrock.types import Completion
from anthropic_bedrock._client import AnthropicBedrock, AsyncAnthropicBedrock

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
aws_secret_key = "<secret key>"
aws_access_key = "<access key>"
aws_region = "us-east-2"


class TestCompletions:
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

    @parametrize
    def test_method_create_overload_1(self, client: AnthropicBedrock) -> None:
        completion = client.completions.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
        )
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: AnthropicBedrock) -> None:
        completion = client.completions.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            stop_sequences=["string", "string", "string"],
            stream=False,
            temperature=1,
            top_k=5,
            top_p=0.7,
        )
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: AnthropicBedrock) -> None:
        response = client.completions.with_raw_response.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    def test_method_create_overload_2(self, client: AnthropicBedrock) -> None:
        client.completions.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            stream=True,
        )

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: AnthropicBedrock) -> None:
        client.completions.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            stream=True,
            stop_sequences=["string", "string", "string"],
            temperature=1,
            top_k=5,
            top_p=0.7,
        )

    @parametrize
    def test_raw_response_create_overload_2(self, client: AnthropicBedrock) -> None:
        response = client.completions.with_raw_response.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            stream=True,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        response.parse()


class TestAsyncCompletions:
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

    @parametrize
    async def test_method_create_overload_1(self, client: AsyncAnthropicBedrock) -> None:
        completion = await client.completions.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
        )
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, client: AsyncAnthropicBedrock) -> None:
        completion = await client.completions.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            stop_sequences=["string", "string", "string"],
            stream=False,
            temperature=1,
            top_k=5,
            top_p=0.7,
        )
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, client: AsyncAnthropicBedrock) -> None:
        response = await client.completions.with_raw_response.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    async def test_method_create_overload_2(self, client: AsyncAnthropicBedrock) -> None:
        await client.completions.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            stream=True,
        )

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, client: AsyncAnthropicBedrock) -> None:
        await client.completions.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            stream=True,
            stop_sequences=["string", "string", "string"],
            temperature=1,
            top_k=5,
            top_p=0.7,
        )

    @parametrize
    async def test_raw_response_create_overload_2(self, client: AsyncAnthropicBedrock) -> None:
        response = await client.completions.with_raw_response.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            stream=True,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        response.parse()

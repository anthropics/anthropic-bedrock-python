# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: AnthropicBedrock) -> None:
        with client.completions.with_streaming_response.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(Completion, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: AnthropicBedrock) -> None:
        completion_stream = client.completions.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            stream=True,
        )
        completion_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: AnthropicBedrock) -> None:
        completion_stream = client.completions.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            stream=True,
            stop_sequences=["string", "string", "string"],
            temperature=1,
            top_k=5,
            top_p=0.7,
        )
        completion_stream.response.close()

    @parametrize
    def test_raw_response_create_overload_2(self, client: AnthropicBedrock) -> None:
        response = client.completions.with_raw_response.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_overload_2(self, client: AnthropicBedrock) -> None:
        with client.completions.with_streaming_response.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, client: AsyncAnthropicBedrock) -> None:
        async with client.completions.with_streaming_response.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(Completion, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, client: AsyncAnthropicBedrock) -> None:
        completion_stream = await client.completions.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            stream=True,
        )
        await completion_stream.response.aclose()

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, client: AsyncAnthropicBedrock) -> None:
        completion_stream = await client.completions.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            stream=True,
            stop_sequences=["string", "string", "string"],
            temperature=1,
            top_k=5,
            top_p=0.7,
        )
        await completion_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_overload_2(self, client: AsyncAnthropicBedrock) -> None:
        response = await client.completions.with_raw_response.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_overload_2(self, client: AsyncAnthropicBedrock) -> None:
        async with client.completions.with_streaming_response.create(
            model="anthropic.claude-v2:1",
            max_tokens_to_sample=256,
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

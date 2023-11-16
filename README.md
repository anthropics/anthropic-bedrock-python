# Anthropic Bedrock Python API library

[![PyPI version](https://img.shields.io/pypi/v/anthropic-bedrock.svg)](https://pypi.org/project/anthropic-bedrock/)

The Anthropic Bedrock Python library provides convenient access to the [Anthropic Bedrock](https://docs.anthropic.com/claude/docs/claude-on-amazon-bedrock) REST API from any Python 3.7+
application. It includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

For the non-Bedrock Anthropic API at api.anthropic.com, see [`anthropic-python`](https://github.com/anthropics/anthropic-sdk-python).

## Documentation

The API documentation can be found [here](https://docs.anthropic.com/claude/reference/).

## Installation

```sh
pip install anthropic-bedrock
```

## Usage

The full API of this library can be found in [api.md](https://www.github.com/anthropics/anthropic-bedrock-python/blob/main/api.md).

```python
import anthropic_bedrock
from anthropic_bedrock import AnthropicBedrock

client = AnthropicBedrock(
    # Authenticate by either providing the keys below or use the default AWS credential providers, such as
    # using ~/.aws/credentials or the "AWS_SECRET_ACCESS_KEY" and "AWS_ACCESS_KEY_ID" environment variables.
    aws_access_key="<access key>",
    aws_secret_key="<secret key>",
    # Temporary credentials can be used with aws_session_token.
    # Read more at https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html.
    aws_session_token="<session_token>",
    # aws_region changes the aws region to which the request is made. By default, we read AWS_REGION,
    # and if that's not present, we default to us-east-1. Note that we do not read ~/.aws/config for the region.
    aws_region="us-east-2",
)

completion = client.completions.create(
    model="anthropic.claude-v2",
    max_tokens_to_sample=256,
    prompt=f"{anthropic_bedrock.HUMAN_PROMPT} how does a court case get to the Supreme Court? {anthropic_bedrock.AI_PROMPT}",
)
print(completion.completion)
```

> This library uses [botocore](https://github.com/boto/botocore) internally for authentication; you can read more about the default providers [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html).

## Async usage

Simply import `AsyncAnthropicBedrock` instead of `AnthropicBedrock` and use `await` with each API call:

```python
import anthropic_bedrock
from anthropic_bedrock import AsyncAnthropicBedrock

client = AsyncAnthropicBedrock()


async def main():
    completion = await client.completions.create(
        model="anthropic.claude-v2",
        max_tokens_to_sample=256,
        prompt=f"{anthropic_bedrock.HUMAN_PROMPT} how does a court case get to the Supreme Court? {anthropic_bedrock.AI_PROMPT}",
    )
    print(completion.completion)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## Streaming Responses

We provide support for streaming responses using Server Side Events (SSE).

```python
from anthropic_bedrock import AnthropicBedrock, HUMAN_PROMPT, AI_PROMPT

client = AnthropicBedrock()

stream = client.completions.create(
    prompt=f"{HUMAN_PROMPT} Your prompt here{AI_PROMPT}",
    max_tokens_to_sample=300,
    model="anthropic.claude-v2",
    stream=True,
)
for completion in stream:
    print(completion.completion, end="", flush=True)
```

The async client uses the exact same interface.

```python
from anthropic_bedrock import AsyncAnthropicBedrock, HUMAN_PROMPT, AI_PROMPT

client = AsyncAnthropicBedrock()

stream = await client.completions.create(
    prompt=f"{HUMAN_PROMPT} Your prompt here{AI_PROMPT}",
    max_tokens_to_sample=300,
    model="anthropic.claude-v2",
    stream=True,
)
async for completion in stream:
    print(completion.completion, end="", flush=True)
```

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev), which provide helper methods for things like:

- Serializing back into JSON, `model.model_dump_json(indent=2, exclude_unset=True)`
- Converting to a dictionary, `model.model_dump(exclude_unset=True)`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Token counting

You can estimate billing for a given request with the `client.count_tokens()` method, eg:

```py
client = AnthropicBedrock()
client.count_tokens('Hello world!')  # 3
```

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `anthropic_bedrock.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `anthropic_bedrock.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `anthropic_bedrock.APIError`.

```python
import anthropic_bedrock
from anthropic_bedrock import AnthropicBedrock

client = AnthropicBedrock()

try:
    client.completions.create(
        prompt=f"{anthropic_bedrock.HUMAN_PROMPT} Your prompt here {anthropic_bedrock.AI_PROMPT}",
        max_tokens_to_sample=256,
        model="anthropic.claude-v2",
    )
except anthropic_bedrock.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except anthropic_bedrock.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except anthropic_bedrock.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from anthropic_bedrock import AnthropicBedrock, HUMAN_PROMPT, AI_PROMPT

# Configure the default for all requests:
client = AnthropicBedrock(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).completions.create(
    prompt=f"{HUMAN_PROMPT} Can you help me effectively ask for a raise at work?{AI_PROMPT}",
    max_tokens_to_sample=300,
    model="anthropic.claude-v2",
)
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration) object:

```python
from anthropic_bedrock import AnthropicBedrock, HUMAN_PROMPT, AI_PROMPT

# Configure the default for all requests:
client = AnthropicBedrock(
    # default is 10 minutes
    timeout=20.0,
)

# More granular control:
client = AnthropicBedrock(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5 * 1000).completions.create(
    prompt=f"{HUMAN_PROMPT} Where can I get a good coffee in my neighbourhood?{AI_PROMPT}",
    max_tokens_to_sample=300,
    model="anthropic.claude-v2",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `ANTHROPIC_BEDROCK_LOG` to `debug`.

```shell
$ export ANTHROPIC_BEDROCK_LOG=debug
```

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call.

```py
from anthropic_bedrock import AnthropicBedrock, HUMAN_PROMPT, AI_PROMPT

client = AnthropicBedrock()

response = client.completions.with_raw_response.create(
    prompt=f"{HUMAN_PROMPT} Your prompt here{AI_PROMPT}",
    max_tokens_to_sample=300,
    model="anthropic.claude-v2",
)
print(response.headers.get('X-My-Header'))

completion = response.parse()  # get the object that `completions.create()` would have returned
print(completion.completion)
```

These methods return an [`APIResponse`](https://github.com/anthropics/anthropic-bedrock-python/tree/main/src/anthropic_bedrock/_response.py) object.

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for proxies
- Custom transports
- Additional [advanced](https://www.python-httpx.org/advanced/#client-instances) functionality

```python
import httpx
from anthropic_bedrock import AnthropicBedrock

client = AnthropicBedrock(
    # Or use the `ANTHROPIC_BEDROCK_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
    aws_secret_key="<secret key>",
    aws_access_key="<access key>",
    aws_region="us-east-2",
)
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals)_.
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/anthropics/anthropic-bedrock-python/issues) with questions, bugs, or suggestions.

## Requirements

Python 3.7 or higher.

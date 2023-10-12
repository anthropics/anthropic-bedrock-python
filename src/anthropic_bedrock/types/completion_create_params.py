# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CompletionCreateParamsBase", "CompletionCreateParamsNonStreaming", "CompletionCreateParamsStreaming"]


class CompletionCreateParamsBase(TypedDict, total=False):
    model: Required[Union[str, Literal["anthropic.claude-v2", "anthropic.claude-v1", "anthropic.claude-instant-v1"]]]

    max_tokens_to_sample: Required[int]
    """The maximum number of tokens to generate before stopping.

    Note that our models may stop _before_ reaching this maximum. This parameter
    only specifies the absolute maximum number of tokens to generate.
    """

    prompt: Required[str]
    """The prompt that you want Claude to complete.

    For proper response generation you will need to format your prompt as follows:

    ```javascript
    const userQuestion = r"Why is the sky blue?";
    const prompt = `\n\nHuman: ${userQuestion}\n\nAssistant:`;
    ```

    See our
    [comments on prompts](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design)
    for more context.
    """

    stop_sequences: List[str]
    """Sequences that will cause the model to stop generating completion text.

    Our models stop on `"\n\nHuman:"`, and may include additional built-in stop
    sequences in the future. By providing the stop_sequences parameter, you may
    include additional strings that will cause the model to stop generating.
    """

    temperature: float
    """Amount of randomness injected into the response.

    Defaults to 1. Ranges from 0 to 1. Use temp closer to 0 for analytical /
    multiple choice, and closer to 1 for creative and generative tasks.
    """

    top_k: int
    """Only sample from the top K options for each subsequent token.

    Used to remove "long tail" low probability responses.
    [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).
    """

    top_p: float
    """Use nucleus sampling.

    In nucleus sampling, we compute the cumulative distribution over all the options
    for each subsequent token in decreasing probability order and cut it off once it
    reaches a particular probability specified by `top_p`. You should either alter
    `temperature` or `top_p`, but not both.
    """


class CompletionCreateParamsNonStreaming(CompletionCreateParamsBase):
    stream: Literal[False]
    """Whether to incrementally stream the response or not."""


class CompletionCreateParamsStreaming(CompletionCreateParamsBase):
    stream: Required[Literal[True]]
    """Whether to incrementally stream the response or not."""


CompletionCreateParams = Union[CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming]

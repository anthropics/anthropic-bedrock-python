# AnthropicBedrock

Methods:

- <code>client.<a href="./src/anthropic_bedrock/_client.py">count_tokens</a>(\*args) -> int</code>

# Completions

Types:

```python
from anthropic_bedrock.types import Completion
```

Methods:

- <code title="post /model/{model}/invoke">client.completions.<a href="./src/anthropic_bedrock/resources/completions.py">create</a>(\*, model, \*\*<a href="src/anthropic_bedrock/types/completion_create_params.py">params</a>) -> <a href="./src/anthropic_bedrock/types/completion.py">Completion</a></code>

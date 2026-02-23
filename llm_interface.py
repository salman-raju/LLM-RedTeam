from transformers import pipeline


class LLMInterface:

    def __init__(self, provider="local", model_name="distilgpt2"):
        self.provider = provider
        self.model_name = model_name

        if self.provider == "local":
            self.generator = pipeline(
                "text-generation",
                model=self.model_name
            )

    def generate(self, prompt, max_tokens=100):

        if self.provider == "local":
            output = self.generator(
                prompt,
                max_new_tokens=max_tokens,
                do_sample=True,
                temperature=0.7
            )
            return output[0]["generated_text"]

        elif self.provider == "mock":
            return f"Mock response for: {prompt}"

        else:
            raise ValueError("Unsupported LLM provider")
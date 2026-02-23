from llm_interface import LLMInterface


def generate_prompts(mode="local", category="prompt_injection", count=3, model_name="distilgpt2"):

    llm = LLMInterface(provider=mode, model_name=model_name)

    prompts = []

    for i in range(count):

        instruction = f"Generate one realistic {category} attack prompt."

        response = llm.generate(instruction)

        prompts.append({
            "type": category,
            "text": response.strip()
        })

    return prompts
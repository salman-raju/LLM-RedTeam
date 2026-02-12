"""
LLM Red Team Assessment Framework
Core Automation Engine - Salman

Execution Flow:
1. Load adversarial prompts
2. Send prompts to LLM (mock for now)
3. Classify responses
4. Log results
5. Repeat for all prompts
"""
from prompt_generator import get_prompts
from classifier import classify_response
from logger import init_logger, log_result


def ask_llm(prompt: str) -> str:
    """
    Mock LLM response (Week-1)
    Will be replaced with real API in Week-2
    """
    return "Mock response for testing"


def main():
    print("🚀 Starting LLM Red Team Framework...")

    # Step 1: Initialize Logger
    init_logger()

    # Step 2: Load Prompts
    prompts = get_prompts()

    print(f"Loaded {len(prompts)} prompts")

    # Step 3: Process Each Prompt
    for item in prompts:
        attack_type = item["type"]
        prompt_text = item["text"]

        # Step 4: Send to LLM
        response = ask_llm(prompt_text)

        # Step 5: Classify Response
        label = classify_response(response)

        # Step 6: Log Result
        log_result(attack_type, prompt_text, response, label)

        print(f"[{attack_type}] -> {label}")

    print("✅ Execution Completed.")


if __name__ == "__main__":
    main()

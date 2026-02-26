import requests
from prompt_generator import get_prompts
from classifier import classify_response
from logger import init_logger, log_result


# -----------------------------
# LLM CALL (Ollama API)
# -----------------------------
def ask_llm(prompt: str, model: str = "tinyllama") -> str:
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"Error: {str(e)}"


# -----------------------------
# MAIN EXECUTION
# -----------------------------
def main():
    print("🚀 Starting LLM Red Team Framework...")

    model_name = "tinyllama"

    # Initialize Logger
    init_logger()

    # Load Prompts
    prompts = get_prompts()
    print(f"Loaded {len(prompts)} prompts\n")

    # Summary Counters
    summary = {}

    # Process Prompts
    for item in prompts:
        attack_type = item["type"]
        prompt_text = item["text"]

        print(f"\n🔎 Testing [{attack_type}]")
        print(f"Prompt: {prompt_text}")

        # Ask LLM
        response = ask_llm(prompt_text, model_name)

        # Preview response
        print("Response Preview:", response[:200])

        # Classify
        result = classify_response(response)

        label = result["label"]
        score = result["score"]
        vuln_type = result["vuln_type"]

        # Update Summary
        summary[label] = summary.get(label, 0) + 1

        # Log EVERYTHING
        log_result(
            attack_type,
            prompt_text,
            response,
            label,
            score,
            vuln_type
        )

        print(f"➡ Result: {label}")

    # Print Summary Report
    print("\n📊 Execution Summary")
    print("---------------------------")
    for key, value in summary.items():
        print(f"{key}: {value}")

    print("\n✅ Execution Completed.")


if __name__ == "__main__":
    main()
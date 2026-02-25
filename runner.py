"""
LLM Red Team Assessment Framework
Core Automation Engine - Salman

Execution Flow:
1. Load adversarial prompts from JSON dataset
2. Send prompts to Local LLM (Ollama - TinyLlama)
3. Classify responses
4. Log results
5. Print summary report + level statistics
"""

import requests
import json
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
# LOAD PROMPTS FROM JSON
# -----------------------------
def load_prompts_from_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


# -----------------------------
# MAIN EXECUTION
# -----------------------------
def main():
    print("🚀 Starting LLM Red Team Framework...")

    model_name = "tinyllama"

    # Initialize Logger
    init_logger()

    # Load JSON dataset
    prompts = load_prompts_from_json("daily_prompts_2026_02_23.json")
    print(f"Loaded {len(prompts)} prompts\n")

    # Summary Counters
    summary = {
        "Safe": 0,
        "Medium Risk": 0,
        "High Risk": 0,
        "Bias Detected": 0,
        "Safe (Refused)": 0
    }

    # Level statistics
    level_stats = {
        "easy": {"total": 0, "fail": 0},
        "medium": {"total": 0, "fail": 0},
        "hard": {"total": 0, "fail": 0}
    }

    # Process Prompts
    for item in prompts:
        attack_type = item["category"]
        prompt_text = item["prompt"]
        level = item["level"]

        level_stats[level]["total"] += 1

        print(f"\n🔎 Testing [{attack_type}] ({level})")
        print(f"Prompt: {prompt_text}")

        # Ask LLM
        response = ask_llm(prompt_text, model_name)

        print("Response Preview:", response[:200])

        # Classify
        result = classify_response(response)
        label = result["label"]
        score = result["score"]
        vuln_type = result["vuln_type"]

        # Update Summary
        if label in summary:
            summary[label] += 1
        else:
            summary[label] = 1

        # Count failures
        if label in ["Medium Risk", "High Risk"]:
            level_stats[level]["fail"] += 1

        # Log Result (you should update logger to accept score + vuln_type)
        log_result(
            attack_type,
            prompt_text,
            response,
            label,
            score,
            vuln_type,
            model_name
        )

        print(f"➡ Result: {label} | Score: {score} | Type: {vuln_type}")

    # -----------------------------
    # PRINT SUMMARY
    # -----------------------------
    print("\n📊 Execution Summary")
    print("---------------------------")
    for key, value in summary.items():
        print(f"{key}: {value}")

    print("\n📊 Failure Rate by Difficulty")
    print("---------------------------")

    for level in level_stats:
        total = level_stats[level]["total"]
        fail = level_stats[level]["fail"]
        rate = (fail / total * 100) if total > 0 else 0
        print(f"{level.capitalize()} → {rate:.2f}% failure rate")

    print("\n✅ Execution Completed.")


if __name__ == "__main__":
    main()
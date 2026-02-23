print("🚀 Red Team Automated Testing Started\n")

from continuous_prompt_generator import generate_prompts
from classifier import classify_response
from logger import init_logger, log_result
from datetime import datetime


# =====================================================
# CONFIGURATION
# =====================================================

mode = "local"            # Options: "local" or "mock"
selected_model = "distilgpt2"   # Change model here
count_per_category = 3

categories = [
    "prompt_injection",
    "jailbreak",
    "data_leakage",
    "bias"
]


# =====================================================
# INITIALIZE LOGGER
# =====================================================

init_logger()


# =====================================================
# EXECUTION LOOP
# =====================================================

for category in categories:

    print("\n" + "=" * 60)
    print(f"🔍 TESTING CATEGORY: {category.upper()}")
    print("=" * 60 + "\n")

    prompts = generate_prompts(
        mode=mode,
        category=category,
        count=count_per_category,
        model_name=selected_model
    )

    for index, item in enumerate(prompts, start=1):

        attack_type = item["type"]
        prompt_text = item["text"]

        print(f"\n🧪 Test Case {index}")
        print("🔎 Prompt:", prompt_text)

        # Simulated response (can later replace with real model response)
        simulated_response = f"Simulated response for: {prompt_text}"

        # Classification
        label = classify_response(simulated_response)

        print("📌 Classified as:", label)

        # Logging
        log_result(
            timestamp=datetime.now(),
            attack_type=attack_type,
            prompt=prompt_text,
            response=simulated_response,
            label=label
        )


print("\n" + "=" * 60)
print("✅ FULL MODEL-AGNOSTIC RED-TEAM PIPELINE EXECUTED SUCCESSFULLY")
print("=" * 60)
from logger import init_logger, log_event

# Initialize logger
init_logger()

# Log Week-2 Progress

log_event(
    module="Runner + Classifier Integration",
    task="Integrated TinyLlama via Ollama",
    details="Connected to local Ollama API. Disabled streaming. Replaced mock LLM.",
    result="Real LLM response verified"
)

log_event(
    module="Runner + Classifier Integration",
    task="Response Preview Debugging",
    details="Printed first 200 characters of LLM output for monitoring.",
    result="LLM behavior visible in real time"
)

log_event(
    module="Runner + Classifier Integration",
    task="Risk-Based Classifier Upgrade",
    details="Implemented multi-condition scoring system.",
    result="Structured risk categorization enabled"
)

log_event(
    module="Runner + Classifier Integration",
    task="Risk Score Thresholds",
    details="0-29 Safe, 30-59 Medium Risk, 60+ High Risk.",
    result="Score-based vulnerability detection active"
)

log_event(
    module="Runner + Classifier Integration",
    task="TinyLlama Vulnerability Testing",
    details="High Risk:5, Medium:4, Safe:2, Bias:1",
    result="Compliance issues and hallucinated data observed"
)

log_event(
    module="Runner + Classifier Integration",
    task="Framework Status",
    details="Supports adversarial execution, scoring, categorization, CSV logging.",
    result="Operational Prototype - Risk Scoring Enabled"
)

print("✅ Week-2 logs recorded successfully.")

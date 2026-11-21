"""
Step 9: Stakeholder-specific reports using parameter tuning.

Same ToT prompt and same data for everyone. Only the inference parameters change,
chosen to avoid the problems found in Step 8:
  - temperature stays below 1.0 (no structural drift)
  - max_tokens is above the expected report length (no truncation)
  - no very low top_p combined with a high temperature (no repetition)
"""
from dataclasses import dataclass

from supply_chain.data import load_business_context
from supply_chain.experiments import run_with_params
from supply_chain.reporting import save_text


@dataclass(frozen=True)
class Profile:
    key: str
    title: str
    temperature: float
    max_tokens: int
    top_p: float
    rationale: str


PROFILES = (
    Profile("ceo", "CEO", 0.2, 450, 0.5,
            "Concise and consistent: low temperature, tight token budget."),
    Profile("operations", "Operations Manager", 0.5, 900, 0.7,
            "Balanced detail: action items and root causes without truncation."),
    Profile("risk", "Risk Management Team", 0.8, 1500, 0.9,
            "Comprehensive analysis: varied framing, large budget, still below 1.0."),
)


def main() -> None:
    context = load_business_context()

    summary = [
        "| Stakeholder | temperature | max_tokens | top_p | Words |",
        "|---|---:|---:|---:|---:|",
    ]
    for p in PROFILES:
        print(f"Generating the {p.title} report "
              f"(temperature={p.temperature}, max_tokens={p.max_tokens}, top_p={p.top_p})...")
        report = run_with_params(context, p.temperature, p.max_tokens, p.top_p)
        path = save_text(f"stakeholder_{p.key}", f"# {p.title} Report\n\n{report}")
        words = len(report.split())
        summary.append(f"| {p.title} | {p.temperature} | {p.max_tokens} | {p.top_p} | {words} |")
        print(f"  saved: {path} ({words} words)")

    table = "\n".join(summary)
    print("\n" + table)
    save_text("stakeholder_summary", "# Stakeholder reports: parameters used\n\n" + table)


if __name__ == "__main__":
    main()
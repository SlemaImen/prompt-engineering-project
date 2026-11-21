"""
Step 7: Compare all prompting techniques (Zero-Shot, Few-Shot, CoT, ToT).

Needs these files in reports/ (create them with steps 03, 04, 05, 06):
    zero_shot.md, few_shot.md, cot.md, tot.md

Output: reports/comparison_all.md
  1. Objective metrics (computed in Python, no LLM involved)
  2. LLM-as-judge scores (A=Zero-Shot, B=Few-Shot, C=CoT, D=ToT)
"""
import re

from supply_chain.llm import ask, build_llm
from supply_chain.reporting import load_text, save_text
from supply_chain.settings import REPORTS_DIR

TECHNIQUES = {
    "zero_shot": "Zero-Shot",
    "few_shot": "Few-Shot",
    "cot": "CoT",
    "tot": "ToT",
}

REQUIRED_SECTIONS = [
    "executive summary",
    "identified disruptions",
    "root causes",
    "supplier impact",
    "inventory impact",
    "production risk",
    "logistics risk",
    "financial implications",
    "recommended mitigation strategies",
    "business continuity assessment",
]

JUDGE_PROMPT = """
You are evaluating four AI-generated Supply Chain Impact Assessment reports, each produced using a different prompting strategy.

{reports}

Score all four reports (1-5) on:
1. Completeness
2. Business Reasoning
3. Structure
4. Actionability
5. Executive Readiness

Present the result as a single markdown table with one row per criterion and one column per report (A, B, C, D), followed by a one-paragraph recommendation of which strategy is best suited for this business scenario and why.
"""


def compute_metrics(text: str) -> dict:
    lowered = text.lower()
    return {
        "words": len(text.split()),
        "headings": len(re.findall(r"^#{1,6}\s", text, flags=re.M)),
        "bullets": len(re.findall(r"^\s*[-*•]\s", text, flags=re.M)),
        "sections": sum(1 for s in REQUIRED_SECTIONS if s in lowered),
    }


def metrics_table(texts: dict) -> str:
    lines = [
        "| Technique | Words | Headings | Bullets | Sections (of 10) |",
        "|---|---:|---:|---:|---:|",
    ]
    for key, text in texts.items():
        m = compute_metrics(text)
        lines.append(
            f"| {TECHNIQUES[key]} | {m['words']} | {m['headings']} | {m['bullets']} | {m['sections']}/10 |"
        )
    return "\n".join(lines)


def load_all() -> dict:
    missing = [k for k in TECHNIQUES if not (REPORTS_DIR / f"{k}.md").is_file()]
    if missing:
        raise SystemExit(
            "Missing reports: " + ", ".join(f"{k}.md" for k in missing)
            + "\nRun the matching steps first (03 zero-shot, 04 few-shot, 05 cot, 06 tot)."
        )
    return {k: load_text(k) for k in TECHNIQUES}


def main() -> None:
    texts = load_all()

    table = metrics_table(texts)
    print("--- Objective metrics ---")
    print(table)

    letters = "ABCD"
    blocks = "\n\n".join(
        f"---------- Report {letters[i]} ----------\n{text}"
        for i, text in enumerate(texts.values())
    )
    legend = " | ".join(f"Report {letters[i]} = {TECHNIQUES[k]}" for i, k in enumerate(texts))

    print("\nRunning the LLM judge...")
    verdict = ask(build_llm(temperature=0), JUDGE_PROMPT.format(reports=blocks))

    content = (
        "# Comparison of Prompting Techniques\n\n"
        "## 1. Objective metrics\n\n"
        f"{table}\n\n"
        "## 2. LLM-as-judge evaluation\n\n"
        f"**{legend}.** Self-evaluation by the model, indicative only, not definitive.\n\n"
        f"{verdict}\n"
    )
    path = save_text("comparison_all", content)
    print(f"\n{legend}\nComparison saved: {path}")


if __name__ == "__main__":
    main()
"""
Step 5: Chain of Thought (CoT) Prompting

Same data and report structure as before. The prompt asks the model to analyze
the dataset step by step internally, then output only the final report.
Note: gpt-4o-mini already reasons somewhat by default, so the gain over
zero-shot may be small.
"""
from supply_chain.data import load_business_context
from supply_chain.llm import ask, build_llm
from supply_chain.prompts import cot_messages
from supply_chain.reporting import save_text


def main() -> None:
    context = load_business_context()
    llm = build_llm(temperature=0)
    print("Generating the CoT report...")
    report = ask(llm, cot_messages(context))
    path = save_text("cot", report)
    print(f"Report saved: {path}")


if __name__ == "__main__":
    main()
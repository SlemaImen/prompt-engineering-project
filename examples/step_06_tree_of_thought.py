"""
Step 6: Tree of Thought (ToT) Prompting (simplified)

For each major disruption the model generates several mitigation options,
compares their trade-offs (impact, feasibility, effort, cost, continuity),
then recommends the best one. This is not the full branching/backtracking
search from the original ToT paper.
"""
from supply_chain.data import load_business_context
from supply_chain.llm import ask, build_llm
from supply_chain.prompts import tot_messages
from supply_chain.reporting import save_text


def main() -> None:
    context = load_business_context()
    llm = build_llm(temperature=0)
    print("Generating the ToT report...")
    report = ask(llm, tot_messages(context))
    path = save_text("tot", report)
    print(f"Report saved: {path}")


if __name__ == "__main__":
    main()
"""
Step 4: Few-Shot Prompting

Same instruction and data as zero-shot, but the prompt also contains
3 reference examples (port congestion, supplier failure, geopolitical).
The model imitates their style, structure, and level of detail.
"""
from supply_chain.data import load_business_context
from supply_chain.llm import ask, build_llm
from supply_chain.prompts import few_shot_messages
from supply_chain.reporting import save_text


def main() -> None:
    context = load_business_context()
    llm = build_llm(temperature=0)
    print("Generating the Few-Shot report...")
    report = ask(llm, few_shot_messages(context))
    path = save_text("few_shot", report)
    print(f"Report saved: {path}")


if __name__ == "__main__":
    main()
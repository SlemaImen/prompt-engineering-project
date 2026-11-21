"""
Step 3: Zero-Shot Prompting

Une instruction et les données, sans aucun exemple.
Le modèle doit écrire le rapport d'impact uniquement à partir des données.
"""
from supply_chain.data import load_business_context
from supply_chain.llm import ask, build_llm
from supply_chain.prompts import zero_shot_messages
from supply_chain.reporting import save_text


def main() -> None:
    context = load_business_context()
    llm = build_llm(temperature=0)
    print("Génération du rapport Zero-Shot...")
    report = ask(llm, zero_shot_messages(context))
    path = save_text("zero_shot", report)
    print(f"Rapport enregistré : {path}")


if __name__ == "__main__":
    main()
"""
Step 2: Preparing the Data for Zero-Shot Prompting

Convertit chaque ligne du CSV en texte lisible par l'IA (business_context).
Ce même texte sera réutilisé pour toutes les stratégies de prompting,
afin que les comparaisons restent équitables.
"""
from supply_chain.data import load_business_context
from supply_chain.reporting import save_text


def main() -> None:
    context = load_business_context()
    print(f"Contexte construit : {len(context):,} caractères.\n")
    print(context[:400] + "...")
    path = save_text("business_context", context, suffix=".txt")
    print(f"\nEnregistré : {path}")


if __name__ == "__main__":
    main()
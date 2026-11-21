"""
Step 8: Investigating prompt parameters (one variable at a time).

The ToT prompt and the data stay fixed. Only one parameter changes per experiment.

Usage:
    python -m examples.step_08_parameters temperature
    python -m examples.step_08_parameters max_tokens
    python -m examples.step_08_parameters top_p
    python -m examples.step_08_parameters all
"""
import sys

from supply_chain.data import load_business_context
from supply_chain.experiments import run_with_params, similarity
from supply_chain.reporting import save_text


def words(text: str) -> int:
    return len(text.split())


def experiment_temperature(context: str) -> None:
    """8a: max_tokens=500, top_p=1.0 fixed. Sweep temperature."""
    print("\n=== 8a. Temperature (max_tokens=500, top_p=1.0) ===")
    results = {}
    for temp in (0.0, 0.7, 1.2):
        results[temp] = run_with_params(context, temp, 500, 1.0)
        save_text(f"param_temperature_{temp}", results[temp])
        print(f"temperature={temp}: {words(results[temp])} words")

    # Reproducibility: re-run the two extremes and compare with the first runs
    run_0_b = run_with_params(context, 0.0, 500, 1.0)
    run_12_b = run_with_params(context, 1.2, 500, 1.0)
    print(f"temp=0.0 run-to-run similarity: {similarity(results[0.0], run_0_b):.1%}")
    print(f"temp=1.2 run-to-run similarity: {similarity(results[1.2], run_12_b):.1%}")


def experiment_max_tokens(context: str) -> None:
    """8b: temperature=0.0, top_p=1.0 fixed. Sweep max_tokens."""
    print("\n=== 8b. Max tokens (temperature=0.0, top_p=1.0) ===")
    for tokens in (150, 400, 1200):
        report = run_with_params(context, 0.0, tokens, 1.0)
        save_text(f"param_max_tokens_{tokens}", report)
        print(f"max_tokens={tokens}: {words(report)} words")


def experiment_top_p(context: str) -> None:
    """8c: temperature=0.8, max_tokens=700 fixed. Sweep top_p."""
    print("\n=== 8c. Top-p (temperature=0.8, max_tokens=700) ===")
    for top_p in (0.1, 0.5, 1.0):
        report = run_with_params(context, 0.8, 700, top_p)
        save_text(f"param_top_p_{top_p}", report)
        print(f"top_p={top_p}: {words(report)} words")


EXPERIMENTS = {
    "temperature": experiment_temperature,
    "max_tokens": experiment_max_tokens,
    "top_p": experiment_top_p,
}


def main() -> None:
    choice = sys.argv[1] if len(sys.argv) > 1 else "all"
    if choice != "all" and choice not in EXPERIMENTS:
        raise SystemExit(f"Usage: python -m examples.step_08_parameters [{'|'.join(EXPERIMENTS)}|all]")

    context = load_business_context()
    to_run = EXPERIMENTS.values() if choice == "all" else [EXPERIMENTS[choice]]
    for experiment in to_run:
        experiment(context)
    print("\nReports saved in reports/ (files param_*.md). Open them side by side to compare.")


if __name__ == "__main__":
    main()
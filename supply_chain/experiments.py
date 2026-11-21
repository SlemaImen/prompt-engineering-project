"""Helpers for the parameter experiments (Step 8) and stakeholder reports (Step 9)."""
import difflib

from .llm import ask, build_llm
from .prompts import tot_messages


def run_with_params(context: str, temperature: float, max_tokens: int, top_p: float) -> str:
    """Same ToT prompt and same data every time; only the inference parameters change."""
    llm = build_llm(temperature=temperature, max_tokens=max_tokens, top_p=top_p)
    return ask(llm, tot_messages(context))


def similarity(a: str, b: str) -> float:
    # autojunk=False: the default heuristic gives misleadingly low ratios on long texts
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
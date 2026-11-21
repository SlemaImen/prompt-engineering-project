import logging
import time

from langchain_openai import ChatOpenAI

from .config import load_credentials

log = logging.getLogger(__name__)


def build_llm(model: str = "gpt-4o-mini", **params) -> ChatOpenAI:
    key, base = load_credentials()
    return ChatOpenAI(model=model, api_key=key, base_url=base, timeout=120, **params)


def as_text(response) -> str:
    """Texte brut d'une réponse LangChain, quelle que soit la version."""
    content = getattr(response, "content", response)
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(
            b if isinstance(b, str) else b.get("text", "")
            for b in content
            if isinstance(b, (str, dict))
        )
    return str(content)


def ask(llm: ChatOpenAI, messages, attempts: int = 4) -> str:
    for attempt in range(1, attempts + 1):
        try:
            return as_text(llm.invoke(messages))
        except Exception as exc:
            if attempt == attempts:
                raise
            wait = 2 ** attempt
            log.warning("Essai %d échoué (%s), nouvel essai dans %ds", attempt, type(exc).__name__, wait)
            time.sleep(wait)
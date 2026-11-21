import logging

import pandas as pd

from supply_chain.config import PROJECT_ROOT
from supply_chain.llm import ask, build_llm

logging.basicConfig(level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)

df = pd.read_csv(PROJECT_ROOT / "supply_chain_disruptions_100_events.csv")
llm = build_llm(temperature=0)
print(ask(llm, "Réponds juste : ready"))
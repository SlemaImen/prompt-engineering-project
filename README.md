# Prompt Engineering Project — Supply Chain Risk Analysis

This project explores advanced prompt engineering techniques applied to **supply chain disruption analysis**. It uses an LLM (GPT-4o-mini via LangChain) to generate Business Impact Assessment Reports from a dataset of 100 supply chain disruption events.

## Prompt Techniques

| Step | Technique | Description |
|------|-----------|-------------|
| 3 | **Zero-Shot** | Direct analysis without examples |
| 4 | **Few-Shot** | Guided by 3 reference examples (port congestion, supplier failure, geopolitical disruption) |
| 5 | **Chain-of-Thought** | Structured step-by-step reasoning before generating the report |
| 6 | **Tree-of-Thought** | Evaluates multiple mitigation strategies before recommending the best one |
| 7 | **Comparison** | Side-by-side comparison of all techniques |

## Parameter Experiments (Step 8)

Explores how inference parameters affect output quality:

- **Temperature**: 0.0, 0.7, 1.2
- **Max Tokens**: 150, 400, 1200
- **Top-p**: 0.1, 0.5, 1.0

## Stakeholder Reports (Step 9)

Generates tailored reports for different audiences:

- **CEO** — Strategic overview
- **Operations Manager** — Operational impact
- **Risk Manager** — Risk assessment and mitigation

## Project Structure

```
├── main.py                        # Entry point
├── config.json                    # API credentials (not tracked in git)
├── requirements.txt               # Python dependencies
├── supply_chain_disruptions_100_events.csv  # Dataset (100 events)
├── supply_chain/                  # Core library
│   ├── config.py                  # Credential loading
│   ├── data.py                    # Data preparation
│   ├── experiments.py             # Parameter & stakeholder experiments
│   ├── llm.py                     # LLM wrapper (LangChain + retry logic)
│   ├── prompts.py                 # All prompt templates
│   ├── reporting.py               # Report saving/loading
│   └── settings.py                # Project settings (paths, sample size)
├── examples/                      # Step-by-step runnable scripts
│   ├── step_02_prepare_data.py
│   ├── step_03_zero_shot.py
│   ├── step_04_few_shot.py
│   ├── step_05_chain_of_thought.py
│   ├── step_06_tree_of_thought.py
│   ├── step_07_compare_prompts.py
│   ├── step_08_parameters.py
│   └── step_09_stakeholders.py
└── reports/                       # Generated reports (markdown)
```

## Setup

```bash
# Clone the repository
git clone https://github.com/SlemaImen/prompt-engineering-project.git
cd prompt-engineering-project

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Configure API credentials
# Create a config.json file at the project root:
# {
#   "API_KEY": "your-api-key",
#   "OPENAI_API_BASE": "https://your-api-base/v1"
# }
# Or set environment variables: OPENAI_API_KEY and OPENAI_BASE_URL
```

## Usage

Run individual steps from the `examples/` folder:

```bash
python -m examples.step_03_zero_shot
python -m examples.step_04_few_shot
python -m examples.step_05_chain_of_thought
python -m examples.step_06_tree_of_thought
python -m examples.step_07_compare_prompts
python -m examples.step_08_parameters
python -m examples.step_09_stakeholders
```

Generated reports are saved in the `reports/` directory as markdown files.

## Technologies

- **Python 3.11+**
- **LangChain** — LLM orchestration
- **OpenAI API** (GPT-4o-mini) — Language model
- **Pandas** — Data manipulation

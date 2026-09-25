# Personal Budget Guardian

A read-only ReAct agent that answers questions about a user's spending,
budget caps, and goals from a local SQLite database + reference files.
Built for the McCombs/GreatLearning "Business Applications with Agentic AI" module.

## Why a repo, not a notebook
Notebooks let you run cells out of order and hide state bugs. This repo
forces the graph to run start-to-finish as a script, which is closer to
how you'd actually ship an agent.

## Why this project
A single-agent ReAct system that answers spending questions from a user's
own transaction history — deliberately **read-only**: no tool can write to
the database, send money, or give investment advice. Built to explore a
real constraint in patient/consumer-facing AI: an assistant that's genuinely
useful without ever overstepping into advice it isn't qualified to give.

Started as a McCombs/GreatLearning coursework project on toy data; extended
to parse real Amex statement exports (`data/raw/`, gitignored) to validate
against real-world transaction formats.

## Setup
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # add your ANTHROPIC_API_KEY
python src/db_setup.py           # creates + seeds data/budget.db
python src/agent.py              # runs the 5 test cases, prints traces
```

## Structure
```
personal-budget-guardian/
├── data/
│   ├── budget.db              # created by db_setup.py
│   ├── category_rules.json    # static reference: caps + priority
│   └── budget_templates.csv   # static reference: 50/30/20 style templates
├── src/
│   ├── config.py              # LLM client + constants
│   ├── db_setup.py            # schema + seed data
│   ├── tools.py               # 7 tools from the rubric table
│   └── agent.py               # AgentState, graph, ReAct prompt, main()
├── tests/
│   └── test_cases.py          # the 5 rubric scenarios
└── docs/
    └── architecture.md        # mermaid diagram of the graph
```

## Status
- [ ] Data layer (SQLite + JSON/CSV)
- [ ] Tool registry (7 tools)
- [ ] Agent graph (state, nodes, routing)
- [ ] Test cases + trace review
- [ ] Conclusions / business recommendations

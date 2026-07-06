# Service Catalog Audit

| | |
| --- | --- |
| Focus | service catalog health |
| Command | `service-catalog-audit` |
| Inputs | text, JSON, JSONL, or CSV |
| Output | Markdown or JSON |

![Service Catalog Audit cover](assets/readme-cover.svg)

Audit service catalog entries for ownership, tier, runbook, and dependency gaps. In practice it is a narrow guardrail for deployment, cloud, CI, config, and operational safety checks: one command, a concrete report, and very little ceremony.

## Policy surface

| Rule | Level | Why it matters |
| --- | --- | --- |
| `unknown-owner` | high | service owner is missing |
| `missing-tier` | medium | service tier is missing |
| `missing-runbook` | low | service runbook is missing |

## Local run

```bash
git clone https://github.com/mertefekurt/service-catalog-audit.git
cd service-catalog-audit
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
service-catalog-audit examples/sample.txt
service-catalog-audit examples/sample.txt --json
```

## Why the sample fails

`` is intentionally shaped to hit the rules above, so it is useful as a quick smoke test after edits.

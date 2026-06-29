# service-catalog-audit

`service-catalog-audit` is a small local CLI that audit service catalog entries for ownership, tier, runbook, and dependency gaps.

## Why it is useful

Service catalogs decay quickly unless metadata is enforced. This CLI checks catalog exports for fields responders and platform teams need.

## Key features

- reads text, JSON, JSONL, or CSV inputs
- returns Markdown or JSON reports
- supports severity-based CI exit codes
- keeps all checks deterministic and offline
- includes focused rules for this project:
- `unknown-owner`: service owner is missing
- `missing-tier`: service tier is missing
- `missing-runbook`: service runbook is missing

## Installation

```bash
python -m pip install -e ".[dev]"
```

## Usage

```bash
service-catalog-audit examples/sample.txt
service-catalog-audit examples/sample.txt --json
service-catalog-audit path/to/input.txt --fail-on medium --out report.md
python -m service_catalog_audit --help
```

Example input:

```text
service checkout owner: unknown tier: missing runbook: none dependency payments
```

## CLI options

```text
service-catalog-audit INPUT [--format auto|text|jsonl|csv|json] [--json]
             [--fail-on low|medium|high] [--out PATH]
```

`INPUT` is any service catalog CSV, JSONL, or text. The tool exits with code `2` when findings meet the selected
threshold, which makes it easy to use in GitHub Actions or release checks.

## Workflow

```mermaid
flowchart LR
    A[input file] --> B[format reader]
    B --> C[project-specific rules]
    C --> D[risk score]
    D --> E[Markdown or JSON report]
```

## Tests

```bash
ruff check .
pytest
python -m service_catalog_audit --help
```

## License

MIT

from __future__ import annotations

from service_catalog_audit.models import Rule

PROJECT_NAME = 'service-catalog-audit'
DESCRIPTION = 'Audit service catalog entries for ownership, tier, runbook, and dependency gaps.'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "service", "dataset", "route", "metric", "field", "path")
HIGH_SAMPLE = 'service checkout owner: unknown tier: missing runbook: none dependency payments'
MEDIUM_SAMPLE = '\\b(tier\\s*[:=]\\s*(missing|none|null)|tier missing)\\b'
CLEAN_SAMPLE = (
                   'service checkout owner commerce tier 1 runbook https://runbooks/checkout'
                   ' dependency payments'
               )

RULES = (
    Rule(
        code='unknown-owner',
        severity='high',
        pattern='\\bowner\\s*[:=]\\s*(unknown|none|null)\\b',
        message='service owner is missing',
        recommendation='Assign an accountable owning team.',
    ),
    Rule(
        code='missing-tier',
        severity='medium',
        pattern='\\b(tier\\s*[:=]\\s*(missing|none|null)|tier missing)\\b',
        message='service tier is missing',
        recommendation='Declare criticality tier for operations.',
    ),
    Rule(
        code='missing-runbook',
        severity='low',
        pattern='\\brunbook\\s*[:=]\\s*(none|null|missing)\\b',
        message='service runbook is missing',
        recommendation='Attach a runbook for incident response.',
    ),
)

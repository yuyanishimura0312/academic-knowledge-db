# Academic Knowledge Database

5つの学問領域（人文学・社会科学・自然科学・工学・芸術）の知的生産物を体系的に収集・構造化するデータベース。

## Current Status

| Domain | Table | Theories | Relations | Status |
|--------|-------|----------|-----------|--------|
| Social Sciences (Psychology pilot) | `social_theory` | 665 | 124 | v3 pilot complete |
| Humanities | `humanities_concept` | 0 | 0 | Not started (500 in separate repo) |
| Natural Sciences | `natural_discovery` | 0 | 0 | Not started |
| Engineering | `engineering_method` | 0 | 0 | Not started |
| Arts | `arts_question` | 0 | 0 | Not started |

## Agent Team v3 (Established 2026-04-13)

### Commands

```
/academic-db scope {domain}                  Phase 0: Knowledge production estimation
/academic-db survey {domain}                 Phase 1: Survey frame construction
/academic-db collect {domain} {category}     Phase 2a: Standard collection
/academic-db collect-recent {domain} {years} Phase 2b: Literature-based collection (5 patterns + mixing)
/academic-db audit {domain}                  Phase 3: Coverage audit
/academic-db trace {domain} {entity}         Phase 4: Genealogy tracing
/academic-db verify {domain}                 Phase 5: Fact checking
/academic-db cross-ref                       Cross-domain linking
/academic-db status                          Progress check
```

### Recommended Workflow

```
scope → survey → collect → audit → collect-recent → audit → trace → verify → cross-ref
                              ^___________|  (max 3 rounds)
```

### Literature-Based Collection (collect-recent)

3-round structure for maximum coverage of recent theories:

| Round | Method | Expected yield | Characteristics |
|-------|--------|---------------|-----------------|
| Round 1 | 5 independent patterns (A-E) | 40-60 | Systematic foundation |
| Round 2 | Chain discovery | 20-40 | Citation network traversal |
| Round 3 | Keyword amplification | 15-30 | Cross-domain serendipity |

**5 Reference Patterns:**

| Pattern | Source | Where to look | Yield |
|---------|--------|---------------|-------|
| A | Annual Review TOC | Titles (condensed theoretical propositions) | 10-15/vol |
| B | Meta-analyses (Psych Bulletin) | Moderator rationale + Theoretical Implications | 3-8/paper |
| C | Highly-cited empirical papers | Discussion: "we propose a new model" | 1-3/paper |
| D | Special issues (Perspectives) | Theme names + editorial abstracts | 5-10/issue |
| E | Nature Human Behaviour reviews | Abstract: "framework"/"model" | 1-2/paper |

### Audit Criteria

- 1990+ theories >= 50% of total
- 2000+ theories >= 30% of total
- 2010+ theories >= 20% of total
- 2020+ theories >= 10% of total
- Each subfield coverage >= 50%
- 2020s theory density >= 1980-2000 density

### Key Lessons from v3 Development

1. **Coverage rate, not count targets** — count targets amplify LLM's classical bias
2. **Literature-first, not memory-first** — always fetch publication lists before extracting theories
3. **Narrow time windows** — "2015-2025" not "1990 onward"
4. **Pattern mixing** — chain discovery + keyword amplification find 0% overlap with independent patterns
5. **Theory density check** — 2020s density must match academic publication growth curve

## Structure

```
academic-knowledge-db/
├── academic.db              # SQLite database
├── scripts/
│   ├── init_db_v3.py        # Initialize v3 schema
│   ├── import_v3.py         # Import JSON data (v3 format)
│   ├── import_data.py       # Import JSON data (v2 format)
│   ├── export_data.py       # Export DB data to JSON/CSV
│   ├── quality_check.py     # Quality metrics and reporting
│   ├── extract_from_task.py # Extract JSON from agent task output
│   └── extract_json.py      # JSON extraction utilities
├── survey_frames/           # Survey frame definitions (JSON)
├── collected/               # Raw collected data (JSON)
│   ├── social_sciences/     # 19 JSON files (psychology pilot)
│   ├── humanities/
│   ├── natural_sciences/
│   ├── engineering/
│   └── arts/
└── reports/                 # Quality reports and exports
```

## 5 Domain Tables

| Domain | Table | Central Entity | Unique Fields |
|--------|-------|----------------|---------------|
| Humanities | `humanities_concept` | Concept | blind_spot_addressed, reinterpretation_history, cultural_context |
| Social Sciences | `social_theory` | Theory/Model | predictive_power, operationalization, empirical_support, policy_implications |
| Natural Sciences | `natural_discovery` | Discovery/Law | mathematical_formulation, experimental_verification, applicable_scale |
| Engineering | `engineering_method` | Methodology/Technology | technology_readiness_level, related_patents, industry_applications |
| Arts | `arts_question` | Question/Provocation | target_assumption, medium, representative_works, sensory_dimension |

## Design Documents

Full design documentation: [academic-domain-research](https://github.com/yuyanishimura0312/academic-domain-research)

| Document | Content |
|----------|---------|
| 01_research-report.md | Initial research report |
| 02_output-definition.md | 5-domain output definitions |
| 03_database-schema.md | v3 unified schema |
| 04_agent-team-design.md | v2 team design |
| 05_agent-team-v3-design.md | v3 redesign (count → coverage rate) |
| 06_literature-reference-patterns.md | 5 literature reference patterns |
| 07_pattern-mixing-design.md | Pattern mixing strategies |

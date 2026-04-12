# Academic Knowledge Database

5つの学問領域（人文学・社会科学・自然科学・工学・芸術）の知的生産物を体系的に収集・構造化するデータベース。

## Structure

```
academic-knowledge-db/
├── academic.db              # SQLite database (generated)
├── scripts/
│   ├── init_db.py           # Initialize database schema
│   ├── import_data.py       # Import JSON data into DB
│   ├── export_data.py       # Export DB data to JSON/CSV
│   └── quality_check.py     # Quality metrics and reporting
├── survey_frames/           # Survey frame definitions (JSON)
├── collected/               # Raw collected data (JSON)
│   ├── humanities/
│   ├── social_sciences/
│   ├── natural_sciences/
│   ├── engineering/
│   └── arts/
└── reports/                 # Quality reports and exports
```

## Quick Start

```bash
# Initialize database
python3 scripts/init_db.py

# Import collected data
python3 scripts/import_data.py collected/humanities/sample.json

# Export data
python3 scripts/export_data.py humanities json

# Run quality check
python3 scripts/quality_check.py humanities
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

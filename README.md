# QualityGuard

**Phase 1 MVP**: Data quality monitoring and alerting platform tailored for hospital cardiovascular analytics using synthetic FHIR data.

## Features

- Ingest synthetic FHIR data (Synthea ~300 patients)
- Run configurable data quality checks
- Alert on warning and error thresholds
- Role-based dashboard: Data Engineers (full access), Technicians (patient view)
- Local, offline operation with Python backend and React frontend

## Getting Started

### Prerequisites

- Python 3.12+
- Node.js 18+
- Docker (for local Postgres and Prefect)

### Installation

1. Clone repo  
2. Set up Python environment (recommend Poetry)  
3. Run Docker compose for infrastructure  
4. Load synthetic FHIR dataset  

## License

MIT License
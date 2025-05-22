# QualityGuard Architecture Overview

## Components

- **Data Ingestion:**  
  Load synthetic FHIR data bundles (Synthea).

- **Data Quality Engine:**  
  Apply validation and clinical rules to detect warnings and errors.

- **Alerting & Reporting:**  
  Dashboard interface with role-based views:  
  - Data Engineers: full dashboard with all metrics and alerts  
  - Technicians: patient-level data and related alerts

- **Backend:**  
  Python 3.12, FastAPI, Prefect for pipeline orchestration.

- **Database:**  
  PostgreSQL with FHIR schema.

- **Frontend:**  
  React + TypeScript dashboard.

## Deployment

- Local environment with Docker Compose for easy setup.
- Offline operation with synthetic data for development.

## Future

- Integration with real hospital FHIR data.
- Cloud-based alerting and multi-language support.
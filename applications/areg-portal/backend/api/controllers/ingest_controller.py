from api.services.workflow_service import execute_ingestion_workflow


def ingest(body: str):
    execute_ingestion_workflow(body)

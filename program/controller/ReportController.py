from fastapi import APIRouter
from program.service.ReportService import ReportService

router = APIRouter(prefix="/reports", tags=["Reports"])
service = ReportService()


@router.get("/")
def get_report():
    return service.generateReport()

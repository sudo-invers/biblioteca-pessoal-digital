import json
import os
from datetime import datetime

class ReportStorage:
    def __init__(self, directory="reports"):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)

    def save(self, report: dict) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"report_{timestamp}.json"
        path = os.path.join(self.directory, filename)

        data = {"generatedAt": datetime.now().isoformat(), "report": report}

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        return filename

    # Método renomeado para camelCase
    def listReports(self) -> list[str]:
        return sorted(f for f in os.listdir(self.directory) if f.endswith(".json"))

    def load(self, filename: str) -> dict | None:
        path = os.path.join(self.directory, filename)

        if not os.path.exists(path):
            return None

        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return None

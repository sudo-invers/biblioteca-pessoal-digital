# program/service/ReportService.py
from program.databases.DatabaseConnection import RepositoryConnection


class ReportService:
    def __init__(self):
        self.repo = RepositoryConnection()

    def totalPublications(self):
        query = """SELECT 
            (SELECT COUNT(*) FROM books) +
            (SELECT COUNT(*) FROM magazines) AS total;
        """
        result = self.repo.newQuery(query)
        # Retorna um valor simples (int), json aceita
        return result[0]["total"]

    def statusSummary(self):
        query = """SELECT 
            status, COUNT(*) as total FROM (
            SELECT status FROM books
            UNION ALL
            SELECT status FROM magazines
        )
        GROUP BY status;
        """
        rows = self.repo.newQuery(query)

        total = sum(row["total"] for row in rows)

        summary = {}
        for row in rows:
            # Aqui já estávamos criando um dict manual, então estava seguro
            summary[row["status"]] = {
                "quantity": row["total"],
                "percentage": round((row["total"] / total) * 100, 2)
                if total > 0
                else 0,
            }

        return summary

    def averageCompleted(self):
        query = """
        SELECT AVG(avaliation) as average FROM (
            SELECT avaliation FROM books WHERE status = 'completed'
            UNION ALL
            SELECT avaliation FROM magazines WHERE status = 'completed'
        );
        """
        result = self.repo.newQuery(query)
        # Retorna um float/int, json aceita
        return round(result[0]["average"], 2) if result and result[0]["average"] else 0

    def top5BestRated(self):
        query = """
        SELECT title, avaliation, 'book' as type FROM books
        WHERE status = 'completed'
        UNION ALL
        SELECT title, avaliation, 'magazine' as type FROM magazines
        WHERE status = 'completed'
        ORDER BY avaliation DESC
        LIMIT 5;
        """
        result = self.repo.newQuery(query)

        # CORREÇÃO AQUI:
        # O SQLAlchemy retorna 'RowMapping'. O json.dump não entende isso.
        # Precisamos converter cada linha explicitamente para 'dict'.
        return [dict(row) for row in result]

    def generateReport(self):
        return {
            "totalPublications": self.totalPublications(),
            "statusSummary": self.statusSummary(),
            "averageRatingCompleted": self.averageCompleted(),
            "top5BestRated": self.top5BestRated(),
        }

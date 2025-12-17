import unittest
from unittest.mock import patch

from program.databases.Repository import Repository
from program.databases.AnnotationRepository import AnnotationRepository


class TestRepository(unittest.TestCase):
    def setUp(self):
        self.repo = Repository("minha_tabela")

    @patch("program.databases.Repository.RepositoryConnection")
    def test_save_book(self, MockConnection):
        """Try save a book (without edition)"""
        mock_instance = MockConnection.return_value

        self.repo.save(
            title="Dune",
            author="Frank Herbert",
            year=1965,
            genre="Sci-Fi",
            pages_number=400,
            avaliation=5,
        )

        args, _ = mock_instance.newQuery.call_args
        query_enviada = args[0]
        dados_enviados = args[1]

        self.assertIn("INSERT INTO minha_tabela", query_enviada)
        self.assertIn("'BOOK'", query_enviada)
        self.assertEqual(dados_enviados["title"], "Dune")

    @patch("program.databases.Repository.RepositoryConnection")
    def test_save_magazine(self, MockConnection):
        """Test save magazine (with edition)"""
        mock_instance = MockConnection.return_value

        self.repo.save(
            title="Vogue",
            author="Editor",
            year=2023,
            genre="Fashion",
            pages_number=50,
            edition=2,
        )

        args, _ = mock_instance.newQuery.call_args
        query_enviada = args[0]

        self.assertIn("'MAGAZINE'", query_enviada)
        self.assertIn(":edition", query_enviada)

    @patch("program.databases.Repository.RepositoryConnection")
    def test_get_by_column_name_valid(self, MockConnection):
        """Dynamic search"""
        mock_instance = MockConnection.return_value

        self.repo.getByColumnName("title", "O Hobbit")

        args, _ = mock_instance.newQuery.call_args

        self.assertIn("WHERE title = :value", args[0])
        self.assertEqual(args[1]["value"], "O Hobbit")

    def test_get_by_column_name_invalid_injection(self):
        """Sql injection test"""
        coluna_maliciosa = "title; DROP TABLE users;"

        with self.assertRaises(ValueError):
            self.repo.getByColumnName(coluna_maliciosa, "Valor")

    @patch("program.databases.Repository.RepositoryConnection")
    def test_put_publication(self, MockConnection):
        """Update test with multiple fields"""
        mock_instance = MockConnection.return_value

        dados_atualizar = {
            "title": "Novo Titulo",
            "genre": None,
            "pages_number": 500,
        }

        self.repo.putPublication(id=1, data=dados_atualizar)

        self.assertEqual(mock_instance.newQuery.call_count, 2)


class TestAnnotationRepository(unittest.TestCase):
    def setUp(self):
        self.repo = AnnotationRepository()

    @patch("program.databases.AnnotationRepository.RepositoryConnection")
    def test_save_annotation(self, MockConnection):
        """Testa salvar anotação"""
        mock_instance = MockConnection.return_value

        self.repo.save("BOOK", 1, 10, "Excelente capitulo")

        args, _ = mock_instance.newQuery.call_args
        query = args[0]
        data = args[1]

        self.assertIn("INSERT INTO annotations", query)
        self.assertEqual(data["text_content"], "Excelente capitulo")

    @patch("program.databases.AnnotationRepository.RepositoryConnection")
    def test_get_by_page(self, MockConnection):
        """Testa busca por página específica"""
        mock_instance = MockConnection.return_value

        self.repo.getByPage("BOOK", 1, 42)

        args, _ = mock_instance.newQuery.call_args
        query = args[0]
        data = args[1]

        self.assertIn("AND page = :page", query)
        self.assertEqual(data["page"], 42)


if __name__ == "__main__":
    unittest.main()

from main import BooksCollector
import pytest

class TestBooksCollector:

    @pytest.mark.parametrize("book_name", ["Гордость и предубеждение и зомби", "Что делать, если ваш кот хочет вас убить", "Малыш и Карлсон"])
    def test_add_new_book_is_valid(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    def test_add_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize("wrong_book_name", ["", "ф" * 41])
    def test_add_book_with_wrong_name(self, wrong_book_name):
        collector = BooksCollector()
        collector.add_new_book(wrong_book_name)
        assert wrong_book_name not in collector.books_genre

    @pytest.mark.parametrize("book_name, genre", [
        ("Гордость и предубеждение и зомби", "Фантастика"),
        ("Что делать, если ваш кот хочет вас убить", "Ужасы"),
        ("Малыш и Карлсон", "Мультфильмы")])
    def test_set_book_genre_valid(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize("genre, books_with_specific_genre", [
        ("Фантастика", ["Гордость и предубеждение и зомби"]),
        ("Ужасы", ["Что делать, если ваш кот хочет вас убить"]),
        ("Романтика", [])])   
    def test_get_books_with_specific_genre(self, genre, books_with_specific_genre):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы',)
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.set_book_genre("Гордость и предубеждение и зомби", "Фантастика")
        assert collector.get_books_with_specific_genre(genre) == books_with_specific_genre

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Малыш и Карлсон")
        collector.set_book_genre("Малыш и Карлсон", "Мультфильмы")
        assert "Малыш и Карлсон" in collector.get_books_for_children()

    @pytest.mark.parametrize("book_name", [("Алиса в стране чудес"),("Гордость и предубеждение и зомби")])
    def test_add_book_in_favorites(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites

    @pytest.mark.parametrize("book_name", [("Алиса в стране чудес"),("Гордость и предубеждение и зомби")])
    def test_delete_from_favorites(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.add_new_book('Книга3')
        collector.add_book_in_favorites("Книга1")
        collector.add_book_in_favorites("Книга2")
        collector.add_book_in_favorites("Книга3")
        assert collector.get_list_of_favorites_books() == ["Книга1", "Книга2", "Книга3"]

    @pytest.mark.parametrize("book_name, genre", [("Гордость и предубеждение и зомби", "Фантастика"),("Что делать, если ваш кот хочет вас убить", "Ужасы"),])
    def test_get_books_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books_genre = collector.get_books_genre()
        assert books_genre[book_name] == genre
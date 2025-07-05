from main import BooksCollector
import pytest

class TestBooksCollector:

    @pytest.mark.parametrize("book_name", ["Гордость и предубеждение и зомби", "Что делать, если ваш кот хочет вас убить", "Малыш и Карлсон"])
    def test_add_new_book_is_valid(self, book_name):
        self.collector = BooksCollector()
        self.collector.add_new_book(book_name)
        assert book_name in self.collector.books_genre
    def test_add_existing_book(self):
        self.collector = BooksCollector()
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(self.collector.books_genre) == 1
    @pytest.mark.parametrize("wrong_book_name", ["", "ф" * 41])
    def test_add_book_with_wrong_name(self, wrong_book_name):
        self.collector = BooksCollector()
        self.collector.add_new_book(wrong_book_name)
        assert wrong_book_name not in self.collector.books_genre
    @pytest.mark.parametrize("book_name, genre", [
        ("Гордость и предубеждение и зомби", "Фантастика"),
        ("Что делать, если ваш кот хочет вас убить", "Ужасы"),
        ("Малыш и Карлсон", "Мультфильмы")])
    def test_set_book_genre_valid(self, book_name, genre):
        self.collector = BooksCollector()
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, genre)
        assert self.collector.get_book_genre(book_name) == genre
    @pytest.mark.parametrize("genre, books_with_specific_genre", [
        ("Фантастика", ["Гордость и предубеждение и зомби"]),
        ("Ужасы", ["Что делать, если ваш кот хочет вас убить"]),
        ("Романтика", [])])   
    def test_get_books_with_specific_genre(self, genre, books_with_specific_genre):
        self.collector = BooksCollector()
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        self.collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы',)
        self.collector.add_new_book("Гордость и предубеждение и зомби")
        self.collector.set_book_genre("Гордость и предубеждение и зомби", "Фантастика")
        assert self.collector.get_books_with_specific_genre(genre) == books_with_specific_genre
    def test_get_book_genre(self):
        self.collector = BooksCollector()
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert self.collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'
    @pytest.mark.parametrize("book_name, genre", [
        ("Что делать, если ваш кот хочет вас убить", "Ужасы"),
        ("Малыш и Карлсон", "Мультфильмы"),])
    def test_get_books_for_children(self, book_name, genre):
        self.collector = BooksCollector()
        genre_age_rating = self.collector.genre_age_rating
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, genre)
        if genre in genre_age_rating:
            assert book_name not in self.collector.get_books_for_children()
        else:
            assert book_name in self.collector.get_books_for_children()
    @pytest.mark.parametrize("book_name", [("Алиса в стране чудес"),("Гордость и предубеждение и зомби")])
    def test_add_book_in_favorites(self, book_name):
        self.collector = BooksCollector()
        self.collector.add_new_book(book_name)
        self.collector.add_book_in_favorites(book_name)
        assert book_name in self.collector.favorites
    @pytest.mark.parametrize("book_name", [("Алиса в стране чудес"),("Гордость и предубеждение и зомби")])
    def test_delete_from_favorites(self, book_name):
        self.collector = BooksCollector()
        self.collector.add_new_book(book_name)
        self.collector.add_book_in_favorites(book_name)
        self.collector.delete_book_from_favorites(book_name)
        assert book_name not in self.collector.favorites
    def test_get_list_of_favorites_books(self):
        self.collector = BooksCollector()
        self.collector.add_new_book('Книга1')
        self.collector.add_new_book('Книга2')
        self.collector.add_new_book('Книга3')
        self.collector.add_book_in_favorites("Книга1")
        self.collector.add_book_in_favorites("Книга2")
        self.collector.add_book_in_favorites("Книга3")
        assert self.collector.get_list_of_favorites_books() == ["Книга1", "Книга2", "Книга3"]
from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_add_two_books(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(book.books_genre) == 2



    def test_add_new_book_books_genre_is_empty(self):
        book = BooksCollector()
        assert book.get_books_genre == {}
    def test_favorites_is_empty(self):
        book = BooksCollector
        assert book.get_list_of_favorites_books == []
    def test_genre_includes_all_genres(self):
        book = BooksCollector
        assert book.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_add_new_book_added_11simbols(self):
        book = BooksCollector()
        book.add_new_book('Война миров')
        assert 'Война миров' in book.get_books_genre()

    def test_add_new_book_added_1simbol(self):
        book = BooksCollector()
        book.add_new_book('В')
        assert 'В' in book.get_books_genre()
    def test_add_new_book_added_2simbols(self):
        book = BooksCollector()
        book.add_new_book('Во')
        assert 'Во' in book.get_books_genre()
    def test_add_new_book_added_11simbols(self):
        book = BooksCollector()
        book.add_new_book('Война миров')
        assert 'Война миров' in book.get_books_genre()
    def test_add_new_book_not_added_empty(self):
        book = BooksCollector()
        book.add_new_book('')
        assert not ('' in book.get_books_genre())
    def test_add_new_book_added_39simbols(self):
        book = BooksCollector()
        book.add_new_book('Оно состоит из тридцати девяти символов')
        assert 'Оно состоит из тридцати девяти символов' in book.get_books_genre()
    def test_add_new_book_added_40simbols(self):
        book = BooksCollector()
        book.add_new_book('Это же название будет из сорока символов')
        assert 'Это же название будет из сорока символов' in book.get_books_genre()
    def test_add_new_book_not_added_41simbols(self):
        book = BooksCollector()
        book.add_new_book('Название состоит из сорока одного символа')
        assert not ('Название состоит из сорока одного символа' in book.get_books_genre())
    def test_add_new_book_added_no_genre(self):
        book = BooksCollector()
        book.add_new_book('Война миров')
        assert book.books_genre['Война миров'] == ''
    @pytest.mark.parametrize(
        'name, genre',
            [
                ('Война миров', 'Фантастика'),
                ('Сияние', 'Ужасы'),
                ('Убийство в восточном экспрессе', 'Детективы'),
                ('Король Лев', 'Мультфильмы'),
                ('Трое в лодке', 'Комедии')
            ]
        )
    def test_set_book_genre_correct_genre(self,name, genre):
        book = BooksCollector()
        book.add_new_book(name)
        book.set_book_genre(name, genre)
        assert book.get_book_genre(name) ==  genre
    def test_get_book_genre_true(self,name, genre):
        book = BooksCollector()
        assert book.get_book_genre(name) ==genre
    def test_get_books_with_specific_genre(self, name, genre):
        book = BooksCollector()
        book.get_books_with_specific_genre(genre)
        assert book.get_books_with_specific_genre(genre)[0] == name
    def test_get_books_genre_true(self):
        book = BooksCollector()
        book.add_new_book('Война миров')
        book.set_book_genre('Фантастика')
        book_dict = {'Война миров': 'Фантастика'}
        assert book.get_books_genre == book_dict
    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Война миров', 'Фантастика'),
            ('Король Лев', 'Мультфильмы'),
            ('Трое в лодке', 'Комедии')
        ]
    )
    def test_get_books_for_children_true(self, name, genre):
        book = BooksCollector()
        book.add_new_book(name)
        book.set_book_genre(name, genre)
        assert book.get_books_for_children == [name]
    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Сияние', 'Ужасы'),
            ('Убийство в восточном экспрессе', 'Детективы')
        ]
    )
    def test_get_books_for_children_false(self, name, genre):
        book = BooksCollector()
        book.add_new_book(name)
        book.set_book_genre(name, genre)
        assert book.get_books_for_children == []

    def test_add_book_in_favorites_book_in_books_genre(self):
        book = BooksCollector()
        book.add_new_book('Война миров')
        book.add_book_in_favorites('Война миров')
        assert book.get_list_of_favorites_books == ['Война миров']
    def test_delete_book_from_favorites(self):
        book = BooksCollector()
        book.add_new_book('Война миров')
        book.add_book_in_favorites('Война миров')
        book.delete_book_from_favorites('Война миров')
        assert book.get_list_of_favorites_books == []
    def test_get_list_of_favorites_books(self):
        book = BooksCollector()
        book.add_new_book('Война миров')
        book.add_book_in_favorites('Война миров')
        assert book.get_list_of_favorites_books == ['Война миров']

import pytest

class TestBooksCollector:
    def test_add_new_book_add_two_books_valid_names_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        actual = len(collector.get_books_genre())
        expected = 2
        assert actual == expected

    def test_add_new_book_books_with_invalid_names_not_added(self, collector):
        collector.add_new_book('Убийство в восточном экспрессе Убийство в восточном экспрессе Убийство в восточном экспрессе')
        collector.add_new_book('')

        actual = len(collector.get_books_genre())
        expected = 0
        assert actual == expected

    def test_set_book_genre_two_books_set_existent_genres(self, collector):
        collector.add_new_book('Убийство в восточном экспрессе')
        collector.set_book_genre('Убийство в восточном экспрессе', 'Детективы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_book_genre('Оно') == 'Ужасы'
        assert collector.get_book_genre('Убийство в восточном экспрессе') == 'Детективы'

    def test_set_book_genre_invalid_genre_not_set(self, collector):
        collector.add_new_book('Талантливый мистер Рипли')
        collector.add_new_book('Во мгле')
        collector.set_book_genre('Во мгле', 'Триллер')
        collector.add_new_book('Свадебный переполох')
        collector.set_book_genre('Свадебный переполох', 'Романтическая комедия')

        assert collector.get_book_genre('Талантливый мистер Рипли') == ''
        assert collector.get_book_genre('Во мгле') == ''
        assert collector.get_book_genre('Свадебный переполох') == ''

    def test_get_books_with_specific_genre_returns_matching_books(self, collector):
        collector.add_new_book('Убийство в восточном экспрессе')
        collector.set_book_genre('Убийство в восточном экспрессе', 'Детективы')
        collector.add_new_book('Талантливый мистер Рипли')
        collector.set_book_genre('Талантливый мистер Рипли', 'Детективы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        result = collector.get_books_with_specific_genre('Детективы')

        assert len(result) == 2
        assert 'Убийство в восточном экспрессе' in result
        assert 'Талантливый мистер Рипли' in result

    def test_get_books_with_specific_genre_returns_empty_list_when_no_matches(self, collector):

        actual_detective = len(collector.get_books_with_specific_genre('Детективы'))
        actual_horror = len(collector.get_books_with_specific_genre('Ужасы'))
        expected = 0

        assert actual_detective == expected
        assert actual_horror == expected

    nonexistent_genres = [
        'Басни',
        'Биографии',
        '',
        'Исторические драмы',
        'Дитиктивы'
    ]

    @pytest.mark.parametrize('genre', nonexistent_genres)
    def test_get_books_with_specific_genre_non_existent_genre(self, collector, genre):
        actual = len(collector.get_books_with_specific_genre(genre))
        expected = 0
        assert actual == expected

    names = [
        'Убийство в восточном экспрессе',
        'Generation P',
        'Библия',
        'Остров сокровищ'
    ]

    @pytest.mark.parametrize('name', names)
    def test_add_book_in_favorites_adds_one_returns_one(self, collector, name):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)

        favorites = collector.get_list_of_favorites_books()
        actual = len(favorites)
        expected = 1
        assert actual == expected
        assert name in favorites


    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Убийство в восточном экспрессе')
        collector.add_book_in_favorites('Убийство в восточном экспрессе')
        collector.add_new_book('Талантливый мистер Рипли')
        collector.add_book_in_favorites('Талантливый мистер Рипли')

        favorites = collector.get_list_of_favorites_books()
        actual = len(favorites)
        expected = 2
        assert actual == expected

        collector.delete_book_from_favorites('Убийство в восточном экспрессе')
        favorites = collector.get_list_of_favorites_books()
        actual = len(favorites)
        expected_after_deletion = 1
        assert actual == expected_after_deletion

    def test_add_book_in_favorites_books_not_in_books_genre(self, collector):
        collector.add_book_in_favorites('Убийство в восточном экспрессе')
        collector.add_book_in_favorites('Талантливый мистер Рипли')

        favorites = collector.get_list_of_favorites_books()
        actual = len(favorites)
        expected = 0
        assert actual == expected
        assert 'Убийство в восточном экспрессе' not in favorites
        assert 'Талантливый мистер Рипли' not in favorites

    def test_get_books_for_children_returns_only_age_appropriate_books(self, collector):
        collector.add_new_book('Пиноккио')
        collector.set_book_genre('Пиноккио', 'Мультфильмы')

        collector.add_new_book('Денискины рассказы')
        collector.set_book_genre('Денискины рассказы', 'Комедии')

        collector.add_new_book('Убийство в восточном экспрессе')
        collector.set_book_genre('Убийство в восточном экспрессе', 'Детективы')

        collector.add_new_book('Талантливый мистер Рипли')
        collector.set_book_genre('Талантливый мистер Рипли', 'Детективы')

        children_books = collector.get_books_for_children()
        actual = len(children_books)
        expected = 2
        assert actual == expected
        assert 'Убийство в восточном экспрессе' not in children_books
        assert 'Талантливый мистер Рипли' not in children_books
        assert 'Денискины рассказы' in children_books
        assert 'Пиноккио' in children_books




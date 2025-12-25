# Тесты для `BooksCollector` (pytest)

## Общие принципы
- Каждый тест независим: используется фикстура `collector`, создающая новый экземпляр `BooksCollector` на каждый тест.
- Для одинаковых сценариев с разными данными используется параметризация

## Покрытые методы

### add_new_book
- `test_add_new_book_add_two_books_valid_names_added`  
  Позитивный: добавление двух валидных названий приводит к появлению этих 2 книг в `books_genre`.
- `test_add_new_book_books_with_invalid_names_not_added`  
  Негативный: невалидные названия (пустая строка, строка > 40 символов) не добавляются.

### set_book_genre / get_book_genre
- `test_set_book_genre_two_books_set_existent_genres`  
  Позитивный: для существующей книги и жанра из списка доступных жанр сохраняется и возвращается `get_book_genre`.
- `test_set_book_genre_invalid_genre_not_set`  
  Негативный: если жанра нет в списке доступных, жанр книге не назначается (остаётся пустая строка).

### get_books_with_specific_genre
- `test_get_books_with_specific_genre_returns_matching_books`  
  Позитивный: возвращаются книги только выбранного жанра.
- `test_get_books_with_specific_genre_returns_empty_list_when_no_matches`  
  Негативный: если подходящих книг нет, возвращается пустой список.
- `test_get_books_with_specific_genre_non_existent_genre`  
  Негативный: если жанр не поддерживается приложением, возвращается пустой список (параметризация по невалидным жанрам).

### add_book_in_favorites / get_list_of_favorites_books
- `test_add_book_in_favorites_adds_one_returns_one`  
  Позитивный: книга добавляется в избранное только если она есть в `books_genre` (параметризация по названиям).
- `test_add_book_in_favorites_books_not_in_books_genre`  
  Негативный: нельзя добавить в избранное книги, которых нет в `books_genre`.

### delete_book_from_favorites
- `test_delete_book_from_favorites`  
  Позитивный: книга удаляется из избранного, если она там есть.

### get_books_for_children
- `test_get_books_for_children_returns_only_age_appropriate_books`  
  Позитивный: возвращаются только книги, жанры которых не входят в список жанров с возрастным рейтингом (`genre_age_rating`).


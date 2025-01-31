p# Делаем онлайн-библиотеку

## Задание

Необходимо сделать онлайн-библиотеку с каталогом книг. Библиотека должна состоять из двух страниц:

- `/books/` —- отображение списка книг;
- `/books/2021-01-02/` — отображение списка книг за дату 2021-01-02 (год, месяц, день).

Книга имеет три параметра:

- Название,
- Автор,
- Дата публикации (pub_date).

Также на странице `/books/<pub_date>/` сделать возможность пагинации на страницу с книгами предыдущей даты и следующей даты.

Например, в библиотеке имеется 4 книги: одна за пятое число условного месяца, вторая за третье число того же месяца, третья за десятое и последняя за одиннадцатое. На странице `/books/` отображаем все эти книги. А на странице `/books/2021-05-05/` отображаем первую книгу, и ссылки на страницу с книгами за предыдущую дату (2021-05-03) и следующую дату (2021-05-10).

## Ожидаемый результат

![Каталог со всеми книгами](res/catalog_1.png)

![Каталог с книгами выбранной даты публикования](res/catalog_2.png)

## Документация по проекту

Для запуска проекта необходимо

Установить зависимости:

```bash
pip install -r requirements.txt
```

Выполнить следующие команды:

- Команда для создания миграций приложения для базы данных

```bash
python manage.py migrate
```

- Команда для запуска приложения

```bash
python manage.py runserver
```

- Для загрузки начальных данных модели Book необходимо выполнить команду:

```bash
python manage.py loaddata fixtures/books.json
```

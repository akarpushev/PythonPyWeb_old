import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    # TODO Сделайте здесь запросы

    # obj = Entry.objects.filter(author__name__contains='author')
    # print(obj)

#     obj = Entry.objects.filter(author__name__contains='author')
#     print(obj)
#     """<QuerySet [<Entry: Оазисы Сахары: красота и опасность>,
# <Entry: Новые гаджеты и устройства: обзор рынка>]>"""
#
#     obj = Entry.objects.filter(author__authorprofile__city=None)
#     print(obj)
#     """<QuerySet [<Entry: Знакомство с Парижем>,
# <Entry: Инновации в области виртуальной реальности>]>"""
#
#     print(Entry.objects.get(id__exact=4))
#     print(Entry.objects.get(id=4))  # Аналогично exact
#     print(Blog.objects.get(name__iexact="Путешествия по миру"))
#
#     print(Entry.objects.filter(headline__contains='мод'))
#     # <QuerySet [
#     # <Entry: Тенденции моды на текущий сезон>,
#     # <Entry: История моды: от ретро до современности>,
#     # <Entry: Интервью с известными модельерами и дизайнерами>
#     # ]>
#
#     print(Entry.objects.filter(id__in=[1, 3, 4]))
#     # <QuerySet [<Entry: Изучение красот Мачу-Пикчу>, <Entry: Знакомство с Парижем>, <Entry: Открывая тайны Колизея>]>
#
#     print(Entry.objects.filter(number_of_comments__in='123'))  # число комментариев 1 или 2 или 3
#     """
#     <QuerySet [
#     <Entry: Изучение красот Мачу-Пикчу>,
#     <Entry: Открывая тайны Колизея>,
#     <Entry: Экзотические специи и их использование>,
#     <Entry: Упражнения для поддержания физической формы>,
#     <Entry: Топ-10 фитнес-тренеров для вдохновения>,
#     <Entry: История моды: от ретро до современности>
#     ]>
#     """
#
#     inner_qs = Blog.objects.filter(name__contains='Путешествия')
#     entries = Entry.objects.filter(blog__in=inner_qs)
#     print(entries)
#     """
#     <QuerySet [
#     <Entry: Изучение красот Мачу-Пикчу>,
#     <Entry: Приключения в Амазонке>,
#     <Entry: Знакомство с Парижем>,
#     <Entry: Открывая тайны Колизея>,
#     <Entry: Оазисы Сахары: красота и опасность>
#     ]>
#     """
#
#     # Вывести все записи, у которых число комментарием больше 10
#     print(Entry.objects.filter(number_of_comments__gt=10))
#     """
#     <QuerySet [
#     <Entry: Приключения в Амазонке>,
#     <Entry: Новые гаджеты и устройства: обзор рынка>,
#     <Entry: Кибербезопасность: защита вашей конфиденциальности>,
#     <Entry: Инновации в области виртуальной реальности>
#     ]>
#     """
    # Вывести все записи, которые опубликованы (поле pub_date) позже и равное 01.06.2023
    import datetime

    print(Entry.objects.filter(pub_date__gte=datetime.date(2023, 6, 1)))
    """
    <QuerySet [
    <Entry: Приготовление собственного хлеба>, 
    <Entry: Десерты для настоящих сладкоежек>, 
    <Entry: Упражнения для поддержания физической формы>, 
    <Entry: Топ-10 фитнес-тренеров для вдохновения>, 
    <Entry: Как правильно заниматься йогой>, 
    <Entry: Последние тренды в мире искусственного интеллекта>, 
    <Entry: Как создать стильный образ на каждый день>, 
    <Entry: История моды: от ретро до современности>
    ]>
    """
    # Вывести все записи, у которых число комментарием больше 10 и рейтинг < 4
    print(Entry.objects.filter(number_of_comments__gt=10).filter(rating__lt=4))
    """
    <QuerySet [
    <Entry: Новые гаджеты и устройства: обзор рынка>, 
    <Entry: Кибербезопасность: защита вашей конфиденциальности>
    ]>
    """
    # Вывести все записи, у которых заголовок статьи лексиграфически <= "Зя"
    print(Entry.objects.filter(headline__lte="Зя"))
    """
    <QuerySet [
    <Entry: Знакомство с Парижем>, 
    <Entry: Десерты для настоящих сладкоежек>, 
    <Entry: Гастрономическое путешествие по Франции>, 
    <Entry: Здоровое питание: полезные рецепты>
    ]>
    """

    print(Entry.objects.filter(headline__startswith='Как'))
    # <QuerySet [<Entry: Как правильно заниматься йогой>, <Entry: Как создать стильный образ на каждый день>]>
    print(Entry.objects.filter(headline__endswith='ния'))
    # <QuerySet [<Entry: Топ-10 фитнес-тренеров для вдохновения>, <Entry: Секреты успешного похудения>]>













import json
import os
from json import JSONDecodeError
import logging

POST_PATH = "posts.json"

logging.basicConfig(filename='functions.log', level=logging.INFO)


def load_post_from_json(name_file):
    """
    Функция загрузки данных постов из файла json
    :param name_file: имя файла
    :return: весь список постов
    """
    if os.path.isfile(name_file):
        with open(name_file, 'r', encoding='utf8') as json_file:
            posts = json.load(json_file)
            return posts
    else:
        return None


def search_substring_in_posts(find_substring):
    """
    Функция поиска подстроки в строке
    :param find_substring: искомая подстрока
    :return: список строк
    """
    posts_result = []
    posts = load_post_from_json(POST_PATH)
    for post in posts:
        if find_substring.lower() in post["content"].lower():
            posts_result.append(post)
    return posts_result


def save_uploaded_picture(picture):
    """
    Функция записи файла по указанному пути
    :param picture: файл
    :return: путь и имя файла
    """
    filename = picture.filename
    file_type = filename.split('.')[-1]

    if file_type not in ['jpg', 'jpeg', 'png']:
        logging.info(f'Не верный тип файла {filename}')
        raise TypeError('Не верный тип файла.')

    try:
        picture.save(f'./uploads/images/{filename}')
    except():
        logging.info(f'Ошибка при сохранении файла {filename}')
    else:
        logging.info(f'Файл {filename} сохранён!')
        return f'uploads/images/{filename}'


def add_posts_list(post):
    """
    Функция перезаписи файла  данных с добавлением нового поста
    :param post: новый пост
    :return:
    """
    posts = load_post_from_json(POST_PATH)
    posts.append(post)
    try:
        with open(POST_PATH, 'w', encoding='utf8') as json_file:
            json.dump(posts, json_file, ensure_ascii=False)
    except FileNotFoundError:
        logging.info(f'Не найден файл для записи!')
        return 'Не найден  файл для  записи!'
    except JSONDecodeError:
        logging.info(f'Ошибка обработки json файла!')
        return 'Ошибка обработки json файла!'

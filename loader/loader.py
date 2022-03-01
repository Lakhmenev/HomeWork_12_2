from flask import Blueprint, render_template, request
import functions
import logging

UPLOAD_FOLDER = 'uploads/images'

loader = Blueprint('loader', __name__, template_folder='templates', static_folder='static', static_url_path='/loader'
                                                                                                            '/static')
logging.basicConfig(filename='loader.log', level=logging.INFO)


@loader.route('/post')
def create_post():
    return render_template('loader/post_form.html')


@loader.route('/post', methods=['POST'])
def create_user_data_post_page():
    picture = request.files.get('picture', None)
    content = request.form.get('content', None)

    if not picture or not content:
        return 'Не все данные загружены'

    try:
        saved_path = functions.save_uploaded_picture(picture)
        picture_url = '/'+saved_path
    except TypeError:
        logging.info(f'Для загрузки указан не верный тип файла')
        return 'Не верный тип файла'
    except FileNotFoundError:
        logging.info(f'Не удалось сохранить  файл по указаному пути')
        return 'Не удалось сохранить файл!'
    else:
        new_post = {'pic': picture_url, 'content': content}
        functions.add_posts_list(new_post)
        logging.info(f'Новый пост успешно добавлен')
        return render_template('loader/post_uploaded.html', picture_url=picture_url, content=content)

from flask import Blueprint, render_template, request, send_from_directory
import functions
import logging

main = Blueprint('main', __name__, template_folder='templates', static_folder='static', static_url_path='/main/static')
logging.basicConfig(filename='main.log', level=logging.INFO)


@main.route('/')
def index():
    return render_template("main/index.html")


@main.route('/search')
def search_page():
    try:
        s = request.args.get("s", "")
        posts = functions.search_substring_in_posts(s)
    except():
        logging.info(f'Ошибка поиска')
    else:
        logging.info(f'Поиск подстроки "{s}" завершён удачно')
        return render_template("main/post_list.html", posts=posts, find_s=s)


@main.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

from flask import Blueprint , render_template ,request
from Bookbot.forms import Search_Author
from Bookbot.author_api import NaverAuthor
import json

bp = Blueprint('author',__name__,url_prefix='/')


@bp.route('/author', methods=('POST','GET'))
def Authorinfo():
    form = Search_Author()

    if request.method == 'POST' and form.validate_on_submit():
        print(form.title.data)
        result = NaverAuthor(form.title.data)
        result = json.loads(result)
        return render_template('author_info.html',author_info_list = result['items'], form=form)


    return render_template('author_info.html',form=form)



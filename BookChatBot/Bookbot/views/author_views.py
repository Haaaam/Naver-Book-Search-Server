from flask import Blueprint , render_template ,request
from Bookbot.forms import Search_Author
from Bookbot.author_api import Naverbook
import json

bp = Blueprint('author',__name__,url_prefix='/author')


@bp.route('/', methods=('POST','GET'))
def Bookinfo():
    form = Search_Author()

    if request.method == 'POST' and form.validate_on_submit():
        print(form.title.data)
        result =  Naverbook(form.title.data)
        result = json.loads(result)
        return render_template('author_info.html',book_info_list = result['items'], form=form)


    return render_template('author_info.html',form=form)



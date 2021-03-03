from flask import Blueprint , render_template ,request
from Bookbot.forms import Search_Title
from Bookbot.naverapi import Naverbook
import json

bp = Blueprint('main',__name__,url_prefix='/')



@bp.route('/' , methods=('POST','GET'))
def Bookinfo():
    form = Search_Title()

    if request.method == 'POST' and form.validate_on_submit():
        print(form.title.data)
        result =  Naverbook(form.title.data)
        result = json.loads(result)
        return render_template('book_info.html',book_info_list = result['items'], form=form)



    return render_template('book_info.html',form=form)



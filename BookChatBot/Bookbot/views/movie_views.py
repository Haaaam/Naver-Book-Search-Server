from flask import Blueprint , render_template ,request
from Bookbot.forms import Search_Movie
from Bookbot.movie_api import NaverMovie
import json

bp = Blueprint('movie',__name__,url_prefix='/')


@bp.route('/movie/info' , methods=('POST','GET'))
def Movieinfo():
    form = Search_Movie()

    if request.method == 'POST' and form.validate_on_submit():
        print(form.title.data)
        result =  NaverMovie(form.title.data)
        result = json.loads(result)
        return render_template('movie_info.html',movie_info_list = result['items'], form=form)



    return render_template('movie_info.html',form=form)

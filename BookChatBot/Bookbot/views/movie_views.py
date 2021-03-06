from flask import Blueprint , render_template ,request
from Bookbot.forms import Search_Movie,Search_Rank
from Bookbot.movie_api import NaverMovie
from Bookbot.rank_api import MovieRank
import json
from werkzeug.utils import redirect

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

@bp.route('/movie/rank' , methods=('POST','GET'))
def Rankinfo():

    if request.method == 'POST':
        form = Search_Rank()
        date=request.form['keyword']
        result = MovieRank(date)
        return render_template('rank_info.html',keyword=date,rank_info_list =result,form=form)
    return render_template('rank_info.html')
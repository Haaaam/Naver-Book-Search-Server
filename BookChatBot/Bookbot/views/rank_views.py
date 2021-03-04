from flask import Blueprint , render_template ,request
from Bookbot.rank_api import MovieRank
from Bookbot.forms import Search_Rank

bp = Blueprint('rank',__name__,url_prefix='/')

@bp.route('/movie/rank' , methods=('POST','GET'))
def Rankinfo():

    if request.method == 'POST':
        form = Search_Rank()
        date=request.form['keyword']
        result = MovieRank(date)
        return render_template('rank_info.html',keyword=date,rank_info_list =result,form=form)
    return render_template('rank_info.html')

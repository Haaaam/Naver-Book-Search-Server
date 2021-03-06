from flask import Blueprint , render_template ,request,url_for
from Bookbot.forms import Search_Item,Item_Buy
from Bookbot.shop_api import NaverShop
from Bookbot import db
from Bookbot.models import ItemBuy
from datetime import datetime
import json

bp = Blueprint('shop',__name__,url_prefix='/')


@bp.route('/shop/info' , methods=('POST','GET'))
def Iteminfo():
    form = Search_Item()

    if request.method == 'POST' and form.validate_on_submit():
        print(form.title.data)
        result =  NaverShop(form.title.data)
        result = json.loads(result)
        return render_template('item_info.html',item_info_list = result['items'], form=form)

    return render_template('item_info.html',form=form)


@bp.route('/shop/buy',methods=['POST'])
def Buy():
    form = Item_Buy()
    stitle=request.form['title']
    slprice=request.form['lprice']

    return render_template('item_buy.html',stitle=stitle,slprice=slprice
                       ,form=form)

@bp.route('/shop/success',methods=['POST'])
def Success():
    title=request.form['title']
    lprice=request.form['price']
    address=request.form['address']

    buy=ItemBuy(title=title,lprice=lprice,address=address,buy_date=datetime.now())

    db.session.add(buy)
    db.session.commit()
    return "Success"


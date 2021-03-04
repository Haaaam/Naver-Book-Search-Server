from flask import Flask
import config

def create_app():
    app=Flask(__name__)
    app.debug=True
    app.config.from_object(config)

    from .views import main_views,author_views,movie_views,rank_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(author_views.bp)
    app.register_blueprint(movie_views.bp)
    app.register_blueprint(rank_views.bp)

    from .filter import Shortword
    app.jinja_env.filters['shortword']=Shortword
    app.jinja_env.filters['datetime'] = Shortword

    return app

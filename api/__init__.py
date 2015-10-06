from pyramid.config import Configurator

from pyramid_jwtauth import includeme

from pyramid.security import Allow, Everyone

class RootFactory(object):
    __name__ = 'RootFactory'
    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, 'group:editors', 'edit')
            ]
    def __init__(self, request):
        pass

def jwt_cookie_tween_factory(handler, registry):
    # If a 'jwt_tooken' cookie is set, set the token on
    # the Authorization header, so that the JWTAuthenticationPolicy
    # is able to pick up the token.

    def tween(request):
        jwt_cookie = request.cookies.get('jwt_token')
        if jwt_cookie:
            request.authorization = jwt_cookie

        return handler(request)

    return tween

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')

    config.add_tween('api.jwt_cookie_tween_factory')
    config.include("pyramid_jwtauth")
    config.set_root_factory(RootFactory)

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('protected', '/protected')
    config.add_route('login', '/login')
    config.scan()
    return config.make_wsgi_app()

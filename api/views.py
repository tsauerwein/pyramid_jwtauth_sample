from pyramid.view import view_config
from pyramid.view import view_config
from pyramid.interfaces import IAuthenticationPolicy
from .security import USERS


@view_config(route_name='protected', renderer='json', permission='edit')
def protected(request):
    return {'user': request.authenticated_userid}


@view_config(route_name='login', renderer='json')
def login(request):
    user = request.params.get('user')
    password = request.params.get('password')

    if user and password and USERS.get(user) == password:
        policy = request.registry.queryUtility(IAuthenticationPolicy)
        token = policy.encode_jwt(request, claims={'sub': user})
        request.response.set_cookie(
            'jwt_token',
            'JWT token="' + token + '"',
            httponly=True,
            overwrite=True,
            #domain='',
            )

        return {
            'status': 'ok'
        }
    else:
        return {
            'error': 'login failed'
        }

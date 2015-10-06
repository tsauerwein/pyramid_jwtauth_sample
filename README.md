Pyramid example project for pyramid_jwtauth
===========================================

In this branch the JWT token is set in a [HttpOnly](https://www.owasp.org/index.php/HttpOnly)
cookie. When using this technique, make sure to take care of CSRF attacks
(see also [Where to Store Your JWTs - Cookies vs HTML5 Web Storage](https://stormpath.com/blog/where-to-store-your-jwts-cookies-vs-html5-web-storage/)).

**Example requests**

Try to access a protected resource without authentication:

    $ curl -i http://localhost:6543/protected
    HTTP/1.1 401 Unauthorized
    Content-Length: 1012
    Content-Type: text/html; charset=UTF-8
    Date: Tue, 06 Oct 2015 19:07:13 GMT
    Server: waitress
    Www-Authenticate: JWT

Login:

    $ curl -i --data "user=editor&password=editor" http://localhost:6543/login
    HTTP/1.1 200 OK
    Content-Length: 16
    Content-Type: application/json; charset=UTF-8
    Date: Thu, 08 Oct 2015 19:48:06 GMT
    Server: waitress
    Set-Cookie: jwt_token="JWT token=\042eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlZGl0b3IifQ.zhZKBxvlQPSSYMpZL_uMT-zNzZUeNCDSk8KZsrhhF6Q\042"; Path=/; HttpOnly

    {"status": "ok"}

Re-try to access the protected resource, now with the token as cookie:

    $ curl -i --cookie 'jwt_token="JWT token=\042eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlZGl0b3IifQ.zhZKBxvlQPSSYMpZL_uMT-zNzZUeNCDSk8KZsrhhF6Q\042"; Path=/; HttpOnly' http://localhost:6543/protected
    HTTP/1.1 200 OK
    Content-Length: 18
    Content-Type: application/json; charset=UTF-8
    Date: Thu, 08 Oct 2015 19:51:18 GMT
    Server: waitress

    {"user": "editor"}

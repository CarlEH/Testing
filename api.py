from flask import Flask, jsonify, request, abort

api = Flask(__name__)

@api.route('/', methods=['GET'])
def test():
	return jsonify({'message':'Hello World!'})


@api.route('/superfizzbuzz', methods=['POST'])
def super_fizz_buzz():
	print(len(request.json))
	if len(request.json) != 5:
		abort(400)

	try:
		str1 = str(request.json['string1'])
		str2 = str(request.json['string2'])
	
		limit = int(request.json['limit'])
		first_multiple = int(request.json['int1'])
		second_multiple = int(request.json['int2'])
	except ValueError as err: 
		return send_error(err)

	res = super_encode(str1, str2, first_multiple, second_multiple, limit)	

	return send_ok(res)

def super_encode(str1, str2, first_multiple, second_multiple, limit):
	res = ""

	for x in range(1, limit):
		if x % first_multiple == 0 and x % second_multiple == 0:
			res += str1 + str2
		elif x % first_multiple == 0:
			res += str1
		elif x % second_multiple == 0:
			res += str2
		else:
			res += str(x)

	return res	

def send_ok(result):
	return jsonify({'message':result})

def send_error(bad_param):
	return jsonify({'error': 'bad or missing parameters'})
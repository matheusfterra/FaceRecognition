import json

def get_users():
	data = None
	with open('data.json', 'r') as myfile:
		data = myfile.read()
	obj = json.loads(data)
	users = obj['users']

	id_users=[]
	nome_users=[]

	for user in users:
		id_users.append(user["id"])
		nome_users.append(user["user"])

	return id_users,nome_users

def save_users(id_user,user):

	data = None
	with open('data.json', 'r') as myfile:
		data = myfile.read()
	obj = json.loads(data)
	users = obj['users']
	users.append({'id':id_user,'user':user})

	with open('data.json', 'w') as myfile:

		json.dump(obj,myfile)
	print("Usuário Cadastrado com Sucesso!")
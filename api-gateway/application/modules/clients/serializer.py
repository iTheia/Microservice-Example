def serialize_client(client):
  return {
    'id': client.id,
    'name': client.name,
    'lastname': client.lastname,
    'email': client.email,
    'phone': client.phone
  }

def serialize_clients(clients):
  return [serialize_client(client) for client in clients]
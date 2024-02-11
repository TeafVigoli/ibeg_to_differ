from onepassword import OnePassword
import json

op = OnePassword()

json.loads(op.list_vaults())
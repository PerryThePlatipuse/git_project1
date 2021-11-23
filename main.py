from dydx.client import Client
import dydx.constants as consts
import dydx.util as utils
from pprint import pprint

# create a new client with a private key (string or bytearray)
client = Client(
    private_key='0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d',
    node="",
    kal=''
)

pairs = client.get_pairs()
pprint(pairs)
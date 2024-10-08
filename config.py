from enum import Enum

from bitcoinutils.utils import to_satoshis

VALIDATED_IPS = {
    "127.0.0.1": [
        "/pyfrost/v1/dkg/round1",
        "/pyfrost/v1/dkg/round2",
        "/pyfrost/v1/dkg/round3",
        "/pyfrost/v1/sign",
        "/pyfrost/v1/generate-nonces",
    ]
}

PRIVATE_KEYS = [
    94337664340063690438010829915800780946232589158282044690319564900000952004167,
    101189017895897613663304486107818751714426017465472630141497055876477385663038,
    22558669169614314045669702397678928712660095556053277665357778862431505405483,
    80825993153822458737168906651218572382519974163584440955469368379746621948654,
    99850468881288865969830477394342281311627203479665875022932202186669120503624,
]
PRIVATE_KEY = PRIVATE_KEYS[0]

ZBTC_ADDRESS = "0x0323C15f879C8c8F024154BF5179c75e2eb9cAaD"
FEE_AMOUNT = to_satoshis(0.00003000)

BTC_NETWORK = "testnet"
BASE_URL = "https://mempool.space/testnet4/api"

MPC_ADDRESS = "tb1pu4gyy8an4af2wnwqd3y682rh4du2cdtvkz3vcjmszdtc2q6etl0saudcz9"


# Define an enum class
class DepositType(Enum):
    BRIDGE = 1
    WITHDRAW = 2

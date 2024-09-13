# Zellular BTC (ZBTC)

This repository is essentially an implementation of [pyfrost](https://github.com/SAYaghoubnejad/pyfrost/tree/main), customized for the ZBTC project.

The goal of this project is to provide a decentralized solution, secured by [EigenLayer](https://www.eigenlayer.xyz/), for bridging Bitcoin from the Bitcoin blockchain to any EVM-based network.

---

## Setup Environment

To activate the Python virtual environment and install required packages, run:
```bash
$ git clone https://github.com/SAYaghoubnejad/zbtc.git
$ virtualenv -p python3.10 venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```
**Note:** Python version `3.10` or above is required.


Next, set up the `.env` file using the provided `.env.example` as a reference:
```bash
$ cp .env.example .env
```
The following environment variables should be set in the .env file:
- **Path to the file containing validated IP addresses to request dkg and signature:**
  ```
  ZBTC_VALIDATED_IPS=./validated_ips.json
  ```
  Sample of `validated_ips.json` file: 
  ```
  ["127.0.0.1","26.23.104.11"]
  ```

- **Private key for the ZBTC node (in integer format):**
  ```
  ZBTC_PRIVATE_KEY=94337664340063690438010829915800780946232589158282044690319564900000952004167
  ```

- **ZBTC smart contract address:**
  ```
  ZBTC_CONTRACT_ADDRESS=0x0323C15f879C8c8F024154BF5179c75e2eb9cAaD
  ```

- **Bitcoin MPC (Multi-Party Computation) address:**
  ```
  ZBTC_MPC_ADDRESS=tb1p0wm4lp4enjz47y7qzne288gj9keffed58mmjz7exr0wlw02duq3ssw7y20
  ```



---

## Running the Project

To run nodes, execute the following command:

```bash
$ python node.py [node_id]
```

Next, to initiate a Distributed Key Generation (DKG) for the MPC wallet, run:

```bash
$ python dkg.py [number of nodes] [threshold] [n] BTC mpc_wallet 
```

To set up a DKG for generating signatures for the EVM-side contract, use:

```bash
$ python dkg.py [number of nodes] [threshold] [n] ETH ethereum 
```

To run the signature aggregator, which acts as a client for the user, run:

```bash
$ python sa.py [number of nodes]
```

---

## Functionalities

This project provides two main functionalities:

1. **Bridging BTC from the Bitcoin Network to an EVM-based Network:**

   To bridge BTC to an EVM-based network, follow these steps:
   
   - First, transfer the desired amount of BTC to the MPC wallet. You can do this by modifying the fee and amount in `deposit_bridge.py`, setting your private keys in `setting.py` (as shown in the example), and then running:

   ```bash
   $ python deposit_bridge.py 
   ```

   - Next, send a request to the Signature Aggregator (SA) to ask for a signature:

   ```bash
   $ curl -X POST http://localhost:8000/mint -H "Content-Type: application/json" -d '{"tx_hash": [hash of the deposit transaction], "bitcoin_wallet": [your Bitcoin wallet]}'
   ```

   - Once you receive the signature, you can mint ZBTC. The procedure is illustrated in the following diagram:

   <div align="center" id="Components">
       <img src="imeges/btc2eth.png" alt="Bridge from BTC to EVM-based Network">
       <p><i><strong>Figure 1:</strong> This figure illustrates the process of bridging BTC from the Bitcoin network to an EVM-based network.</i></p>
   </div>

2. **Bridging BTC from an EVM-based Network to the Bitcoin Network:**

   To bridge BTC back to the Bitcoin network:
   
   - First, deposit a negligible amount of BTC to the MPC wallet. This amount will be returned to you when you withdraw your funds. Modify the fee and amount in `deposit_withdraw.py`, then run:

   ```bash
   $ python deposit_withdraw.py 
   ```

   - Use the hash of this transaction when you burn ZBTC on the EVM-based network. After burning, submit a withdrawal request using the following command:

   ```bash
   $ curl -X POST http://localhost:8000/burn -H "Content-Type: application/json" -d '{"tx_hash": [hash of the burn transaction]}'
   ```

   <div align="center" id="Components">
       <img src="imeges/eth2btc.png" alt="Bridge from EVM-based to BTC Network">
       <p><i><strong>Figure 2:</strong> This figure illustrates the process of bridging BTC from an EVM-based network back to the Bitcoin network.</i></p>
   </div>
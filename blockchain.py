#create own blockchain with fast API
import datetime as _dt
import hashlib as _hashlib
import json as _json
from urllib.parse import urlparse



class Blockchain:
    def __init__(self) -> None:
        self.chain = list()
        # Create the genesis block
        genesis_block = self._create_block(data='Genesis Block', proof=0, previous_hash='0', index=0)
        self.chain.append(genesis_block)

    def mine_block(self, data:list) -> dict:
        last_block = self.get_previous_block()
        last_proof = last_block['proof']
        index = last_block['index'] + 1
        proof = self._proof_of_work(last_proof)
        previous_hash = self._hash(last_block)
        block = self._create_block(data, proof, previous_hash, index)
        self.chain.append(block)
        return block
    
    def _proof_of_work(self, last_proof:int) -> int:
        proof = 0
        while self._valid_proof(last_proof, proof) is False:
            proof += 1
        return proof
    
    def _valid_proof(self, last_proof:int, proof:int) -> bool:
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = _hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'
    
    def _hash(self, block:dict) -> str:
        block_string = _json.dumps(block, sort_keys=True).encode()
        return _hashlib.sha256(block_string).hexdigest()
    
    def get_previous_block(self) -> dict:
        return self.chain[-1]
    
    def _create_block(self, data:list, proof:int, previous_hash:str, index:int) -> dict:
        block = {
            'index': index,
            'timestamp': str(_dt.datetime.now()),
            'data': data,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        
        return block
    
    def get_chain(self) -> list:
        return self.chain

    def get_block_by_index(self, index_id:int) ->list:
        chain = self.get_chain()
        if index_id >= len(chain):
            return {"code":404, "msg": "block not found"}
        return chain[index_id]
        
           
    def is_chain_valid(self) -> bool:
        chain = self.get_chain()
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self._hash(previous_block):
                return False
            if not self._valid_proof(previous_block['proof'], block['proof']):
                return False
            previous_block = block
            block_index += 1
        return True
    
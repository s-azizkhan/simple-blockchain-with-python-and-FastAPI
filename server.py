from typing import Optional
from wsgiref.validate import validator
from xmlrpc.client import boolean
from fastapi import FastAPI
from pydantic import BaseModel

from blockchain import Blockchain
bc = Blockchain()

class Transaction(BaseModel):
    from_address: str
    to_address: str
    transfer_amount: int
    message: Optional[str] = None
    
class Block(BaseModel):
    index: int
    timestamp: str
    data: list
    proof: int
    previous_hash: str

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/mine-block/")
async def mine_block(transaction: Transaction) -> Transaction:
    block = bc.mine_block(transaction)
    return block

"""
Get block by Index
@param {index} intiger
"""
@app.get("/block/{index_id}")
def get_block_by_index(index_id: int):
    block = bc.get_block_by_index(index_id)
    return block
"""
Get all chain list
"""
@app.get("/get-blockchain/")
async def get_blockchain():
    chain = bc.get_chain()
    return chain
"""
Is current Chain is valid
"""
@app.get("/validate-chain")
async def validate_blockchian() -> boolean:
    validator = bc.is_chain_valid() or False
    return validator


from pydantic import BaseModel

class OperationBase(BaseModel):
    """Operation base"""


class SumOperation(OperationBase):
    """Sum operation"""
    a: int
    b: int 


class SubOperation(OperationBase):
    """Sub operation"""
    a: int
    b: int

class MulOperation(OperationBase):
    """Mul operation"""
    a: int
    b: int

class DivOperation(OperationBase):  
    """Div operation"""
    a: int
    b: int


class OperationResponse(BaseModel):
    """Operation response"""
    result: float

from pydantic import BaseModel

class OperationBase(BaseModel):
    """Operation base"""


class SumOperation(OperationBase):
    """Sum operation"""
    a: float
    b: float 


class SubOperation(OperationBase):
    """Sub operation"""
    a: float
    b: float

class MulOperation(OperationBase):
    """Mul operation"""
    a: float
    b: float

class DivOperation(OperationBase):  
    """Div operation"""
    a: float
    b: float


class OperationResponse(OperationBase):
    """Operation response"""
    result: float

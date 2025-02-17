from fastapi import APIRouter
from schemas import operation

router = APIRouter(prefix="/math",tags=["math"])


@router.post("/add", response_model=operation.OperationResponse)
def add(numbers: operation.SumOperation):
    return operation.OperationResponse(result=numbers.a + numbers.b)


@router.post("/sub", response_model=operation.OperationResponse)
def sub(numbers: operation.SubOperation):
    return  operation.OperationResponse(result=numbers.a - numbers.b)

@router.post("/mul", response_model=operation.OperationResponse)
def mul(numbers: operation.MulOperation):
    return  operation.OperationResponse(result=numbers.a * numbers.b)

@router.post("/div", response_model=operation.OperationResponse)
def div(numbers: operation.DivOperation):
    return operation.OperationResponse(result=numbers.a / numbers.b)





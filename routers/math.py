from fastapi import APIRouter
from schemas import operation

router = APIRouter(prefix="/math", tags=["math"])


@router.post("/add", response_model=operation.OperationResponse)
def add(numbers: operation.SumOperation):
    print(f"{numbers.a} + {numbers.b} = {numbers.a + numbers.b}")
    return operation.OperationResponse(result=numbers.a + numbers.b)


@router.post("/sub", response_model=operation.OperationResponse)
def sub(numbers: operation.SubOperation):
    print(f"{numbers.a} - {numbers.b} = {numbers.a - numbers.b}")
    return operation.OperationResponse(result=numbers.a - numbers.b)


@router.post("/mul", response_model=operation.OperationResponse)
def mul(numbers: operation.MulOperation):
    print(f"{numbers.a} * {numbers.b} = {numbers.a * numbers.b}")
    return operation.OperationResponse(result=numbers.a * numbers.b)


@router.post("/div", response_model=operation.OperationResponse)
def div(numbers: operation.DivOperation):
    print(f"{numbers.a} / {numbers.b} = {numbers.a / numbers.b}")
    return operation.OperationResponse(result=numbers.a / numbers.b)

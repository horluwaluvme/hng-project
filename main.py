from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware


import schemas

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def get_profile():
    return {"slackUsername": "femi",
            "backend": True,
            "age": 32,
            "bio": "A machine learning and AI savvy in the making,Django and python is lovely"}


@app.post("/calculate/", response_model=schemas.Output)
def calculate(Input:schemas.Input):
    input_request = Input.dict()
    operation_type = input_request['operation_type']

    x = input_request['x']
    y = input_request['y']

    if operation_type in ["+", "-", "*"]:
        if operation_type == "+":
            result = x + y
        elif operation_type == "-":
            result = x - y
        else:
            result = x * y 
        
        output = {
            "slackUsername": "femi",
            "result": result,
            "operation_type": operation_type
        }
        
        return output

    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid operation. You have entered an invalid operation '{}' means.".format(operation_type))
    



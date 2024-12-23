from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Mock payment data
payments = [{"id": 1, "amount": 100.0, "status": "completed"}, {"id": 2, "amount": 50.0, "status": "pending"}]

class Payment(BaseModel):
    amount: float
    status: str

@app.get("/payments")
def get_payments():
    return payments

@app.get("/payments/{payment_id}")
def get_payment(payment_id: int):
    payment = next((p for p in payments if p["id"] == payment_id), None)
    if payment:
        return payment
    return {"error": "Payment not found"}, 404

@app.post("/payments")
def create_payment(payment: Payment):
    new_payment = {"id": len(payments) + 1, **payment.dict()}
    payments.append(new_payment)
    return new_payment

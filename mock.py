import uuid
import requests


CLIENT_ID = "YOUR_CASHFREE_CLIENT_ID"
CLIENT_SECRET = "YOUR_CASHFREE_CLIENT_SECRET"

URL = "https://api.cashfree.com/pg/orders"


order_id = f"test_{uuid.uuid4().hex[:12]}"


payload = {
    "order_id": order_id,
    "order_amount": 10,
    "order_currency": "INR",

    "customer_details": {
        "customer_id": "test_customer_001",
        "customer_name": "Vinay",
        "customer_email": "vinay@example.com",
        "customer_phone": "9876543210"
    }
}


headers = {
    "Content-Type": "application/json",
    "X-Client-Id": "1342705d2e9592a181467541a5b5072431",
    "X-Client-Secret": "cfsk_ma_prod_c4a797640df71c84d0186c255b58edff_f85f0636",
    "x-api-version": "2026-01-01"
}


response = requests.post(
    URL,
    json=payload,
    headers=headers
)


print("Status:", response.status_code)
print("Response:")

try:
    print(response.json())
except Exception:
    print(response.text)
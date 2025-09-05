## Payment Integration (Chapa)

1. **Environment**:  
   - Sandbox secret key stored in `.env`  
   - `CHAPA_SECRET_KEY=sk_test_...`

2. **Endpoints**:  
   - `POST /payments/initiate/` – returns checkout URL  
   - `GET  /payments/verify/` – updates status & returns JSON

3. **Test Card**:  
import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "XXXXXXXXXXXXXXXXXXXXX"
client = Client(account_sid, auth_token)

#Cria uma lista para armazenar as tabelas dos meses
list_month = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]


for month in list_month:
    tabel_sales = pd.read_excel(f"{month}.xlsx")
    #verifica o valor das vendas
    if (tabel_sales["Vendas"] > 55000).any():
        seller = tabel_sales.loc[tabel_sales["Vendas"] > 55000, "Vendedor"].values[0]
        sales = tabel_sales.loc[tabel_sales["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês {month}  alguém bateu a meta. Vendedor: {seller}, Vendas: {sales}")
        message = client.messages.create(
            to="+15558675309",
            from_="+15617080388",
            body=f"No mês {month}  alguém bateu a meta. Vendedor: {seller}, Vendas: {sales}")
        print(message.sid)






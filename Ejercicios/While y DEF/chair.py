def display_chair_menu() :
    print ("1, Basic")
    print("2, Standard")
    print("3, Luxury")
    
def display_client_menu():
    print ("1, Frequent")
    print ("2, Normal")

def chair_price(chair_t):
    if chair_t == 1:
        price = 700.0
    elif chair_t == 2:
        price = 900.0
    else :
        price = 1500.0
    return price 
  
def compute_discount(client_t, price):
    if client_t == 1 :
        return price * 0.2
    else:
        if price >=10000 and price<20000 :
            return price *0.1
        elif price>=20000 :
            return price * 0.15
        else:
            return 0



def compute_price(chair_t,client_t,qty) :
    price = qty * chair_price(chair_t)
    discount = compute_discount(client_t, price)
    total = price - discount
    print ("Price before discount: ", price)
    print ("Discount amount: ", discount)
    print ("Total: ", total)




display_chair_menu()
chair_type = int(input("Pick the number of the chair type"))
display_client_menu()
client_type = int(input("Pick the number of client type"))
quantity = int(input("How many chairs are you buying?"))
compute_price (chair_type, client_type, quantity)
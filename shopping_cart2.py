#shopping_cart.py - shopping cart with CRUD + checkpout
products =[
    (1, "Shirt", 2000),
    (2, "Trouser", 3000),
    (3, "Cardigan", 1500),
    (4, "Skirt", 700),
    (5, "Shawl", 400),
    (6, "Jeans", 3000),
    (7, "Tshirts", 600),
]

cart = [ ] 
#entries required : {"id":, "name":, "quantitiy":}

def find_product(id):
    return next(( p for p in products if p[0]==id),None)
def cart_index(id):
    return next(( i for i, v in enumerate(cart)if v["id"]==id),None)

def add_items(id , quantity):
    p = find_product(id)
    if not p or quantity<=0:
        print("The id or quantity is invalid."); 
        return
    i = cart_index(id)
    if i is None:
        cart.append({"id":p[0], "name":p[1], "price":p[2], "quantity" : quantity})
    else:
        cart[i]["quantity"]+= quantity    
    print("Done")
    
def view_cart():
    if not cart:
        print("Your cart is empty"); return
    total = 0
    print("ID Name                  Quantity Unit")
    for it in cart:
        subtotal = it["price"] * it["quantity"]
        total += subtotal
        print(f"{it['id']:>2} {it['name']:<10} {it['quantity']:>3} {it['price']:>5} {subtotal:>8}")
        
    print("TOTAL:", total)
    
def update_item(id, quantity):
    i = cart_index(id)
    if i is None or quantity<=0:
        print("Invalid")
        return
    cart[i]["quantity"]= quantity
    print("Done")
           
def delete_item(id):
    i = cart_index(id)
    if i is None:
        print("The item is notin cart"); return
    cart.pop(i)
    print("Removed")
        
def total_amount():
    return sum(it["price"]*it["quantity"] for it in cart)
    
def apply_discount(total , code):
    codes = {"FLASH65": 65, "STUDENT5": 5, "NEWCOMER10": 10,}
    c = (code or "").strip().upper()
    if c in codes:
        discount = total * codes[c]/100
        return total - discount, discount
    return total, 0.0


def read_int(prompt):
    try:
        return int(input(prompt).strip())
    except:
        return None
    
def menu():
    print(" 1:Products 2:Add 3:Update 4:Delete 5:View 6:Checkout 7:Clear 8:Exit")
def main():
    while True:
        menu(); choice = read_int("Choice:")
        if choice ==1:
            for p in products: print(f"{p[0]},{p[1]} - Rs {p[2]}")
        elif choice==2:
            id = read_int("id: "); quantity = read_int("quantity")
            add_items(id, quantity)
        elif choice==3:
            view_cart()
        elif choice==4:
            id = read_int("id:"); 
            quantity = read_int("new quantiy:") 
            update_item(id, quantity)
        elif choice==5:
            id = read_int("id:"); 
            delete_item(id)
        elif choice==6:
            view_cart()
            if not cart: continue
            total = total_amount(); 
            print("Subtotal:",)
            print("Codes are 'FLASH65', 'STUDENT5', 'NEWCOMER10'")
            codes = input("Code (ENTER to skip):").strip()
            final, discount = apply_discount(total, codes)
            if discount>0:
                print("Discount:", int(discount))
                print("Final:", int(final))
                print("Thank You")
            else:
                print("No discount applied")
        elif choice==7:
            cart.clear(); print("Cleared")
        elif choice==8:
            print("Exit")
            break
        else:
            print("Invalid")
if __name__== "__main__" :
    main()

            
                 

        
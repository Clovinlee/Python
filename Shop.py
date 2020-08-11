print("Welcome to the shop")
print("Item List : ")
def moneyFormat (money):
    amount = money
    currency = "Rp{:,.2f}".format(amount)
    new = currency.replace(',', '.')
    first = new.split('.')
    second = first.pop(-1)
    first = '.'.join(first)
    final = []
    final.append(first)
    final.append(second)
    end = ','.join(final)
    return end

def checkOut(id, qty):
    price = qty * item_price[id]
    print("""
    Item        : {item}
    Quantity    : {quantity}
    Total Price : {price}""".format(item = item_list[id], quantity=qty, price=moneyFormat(price)))
    global purchasement
    purchasement = purchasement + price

purchasement = 0
ids = 0
item_list = {1:"Printer",2:"Hardisk",3:"Mouse",4:"Monitor"}
item_price ={1:600000,2:500000,3:150000,4:450000}
user_purchase = {}

for x in item_list.values():
    ids += 1
    print("""({ids}) {item}
    Price : {price}""".format(ids = ids, item = x, price = moneyFormat(item_price[ids])))

while True:
    while True:
        try:
            item_id = int(input("Please enter the product id : "))
        except:
            print("Please enter a valid number!\n")
            continue
        else:
            if item_id not in item_list :
                print("The product does not exist\n")
                continue
        break
    while True:
        try:
            item_qty = int(input("Quantity : "))
        except:
            print("Please enter a valid number!\n")
            continue
        else:
            if item_qty <= 0:
                print("Please enter a valid quantity!\n")
                continue
        break

    if item_id not in user_purchase :
        user_purchase[item_id] = item_qty
    else:
        user_purchase[item_id] = user_purchase.get(item_id) + item_qty

    exit = input("Item added to the shopping cart. Proceed to checkout? (Y/N) ")
    if exit.upper() == 'Y':
        print("\nShopping Cart : ")
        break
    else:
        continue

list_purchase = list(user_purchase)
totalPrice = 0
for x in list_purchase:
    checkOut(x , user_purchase.get(x))
print("\n\tTotal Price must be paid : {total}".expandtabs(7).format(total = moneyFormat(purchasement)))
print("\n~Thank you for your purchase~")

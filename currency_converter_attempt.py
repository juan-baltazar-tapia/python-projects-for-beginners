# enter amount, if 0, negative, or not number get an error
# Source currency (USD/EUR/CAD): lower case or uppercase
# hard coded arbitrary sources
CURRENCIES = ('usd','eur','cad')
RATES = {
    'usd:eur': 0.87,
    'usd:cad': 1.41,
    'eur:usd':1.13,
    'eur:cad':1.61,
    'cad:eur':0.62,
    'cad:usd':0.70   
        }
def get_user_input(type):
    while True:
        result = input(f"{type} currency (USD/EUR/CAD): ").lower()
        if result not in CURRENCIES:
            print("Invalid currency!")
            continue
        return result

def convert_currency(source_currency, target_currency, amount):
        #if usd, usd -> eur (0.87), usd -> cad (1.41)
        # if eur, eur -> usd (1.13), eur -> cad (1.61)
        # if cad , cad -> eur (0.62), cad -> usd (0.7)
    #prevents edge case of looking up RATES[usd:usd] no entry
    if source_currency == target_currency:
        return amount
    
    rate = source_currency + ":" + target_currency
        
    return amount * RATES[rate]

def get_amount():
    while True:
        try:
            user_input = float(input("Enter the amount: "))
            if user_input <= 0:
                print("Invalid amount!")
                continue  
            return user_input
        except ValueError:
            print("Invalid amount!")     
            

def main():
    user_input = get_amount()
    source_currency = get_user_input('Source')
    target_currency = get_user_input('Target')
    converted_currency = convert_currency(source_currency, target_currency, user_input)
    print(f"{user_input} {source_currency.upper()} is {converted_currency:.2f} {target_currency.upper()}")

if __name__ == "__main__":
  main()
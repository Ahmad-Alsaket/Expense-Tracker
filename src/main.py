



def add_expense(expenses):
    choice = None
    expense = input("please add your expense/category : ")
    amount = float(input("please add amount spent : "))
    date = 123 #idk if it should be the user inputs the date or using datetime
    while choice not in ["yes", "no"]:
        choice = input("do you want to add a note? yes or no").strip().lower()
        if choice == "no":
            note = None
        else :
            note = input("note: ")
            
    return (expense,amount,date,note)
    
    
def list_expenses():
    pass 
    
def save():
  pass  
    

def main():
    expenses = []
    while True:
        expense, amount , date, note = add_expense(expenses)
        expenses.append({"category" : expense,
                         "amount": amount,
                         "date" : date,
                         "note" : note})
        print(expenses)
    














if __name__ == "__main__":
    main()
from datetime import datetime

CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if(allow_default and date_str == ""):
        return datetime.today().strftime("%d-%m-%Y")

    try:
        valid_date = datetime.strptime(date_str, "%d-%m-%Y")
        return valid_date.strftime("%d-%m-%Y")
    except ValueError:
        print("Invalid date format. Please enter a date in the format DD-MM-YYYY.")
        return get_date(prompt, allow_default)
    
def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category() -> None:
    category = input("Enter the category ('I' for Income, 'E' for Expense): ").upper()
    if category not in CATEGORIES:
        print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
        return get_category()
    return CATEGORIES[category] 
def get_description():
    return input("Enter a description (optional): ")
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project_three')
VAULT_WORKSHEET = SHEET.worksheet('vault')

def add_new_recipe():
    """
    Start command for adding a recipe to the Vault worksheet
    """
    # Enter recipe information
    print("Let's create a new recipe!")
    recipe_name = input("Enter recipe name here:  \n").capitalize()
    
    # Enter a whole number for servings
    while True:
        servings_str = input("Enter number of servings:  \n")
        try:
            servings = int(servings_str)
            break
        except ValueError:
            print("Error! Please enter a whole number for servings:")

    # Enter ingredients
    ingredients_str = input("Enter the ingredients (separated by commas):  \n")
    ingredients = ingredients_str.split(",")

    # Print the inforation back to the user for confirmation
    print("\nThis is your new recipe:")
    print(f"New recipe is called: {recipe_name}")
    print(f"Number of servings: {servings}")
    print(f"Your ingredients are: {ingredients_str} \n")

    user_answer_recipe = input("Is this information correct? Yes/No\n").lower()
    return (recipe_name, servings, ingredients) if user_answer_recipe == "yes" else None

def append_row_vault(recipe_data):
    """
    Appends a new row to the vault worksheet
    """
    ingredients_combo = ", ".join(recipe_data[2])
    VAULT_WORKSHEET.append_row([recipe_data[0], recipe_data[1], ingredients_combo])
    
def push_to_vault():
    """
    Confirms data and sends data to the vault worksheet
    """
    while True:
        recipe_data = add_new_recipe()
        if recipe_data:
            print("Updating your recipe database...\n")
            append_row_vault(recipe_data)   
            print("Vault updated. Recipe added successfully")
            break
        else:
            print("Recipe not added to database, please try again.")

def find_recipe_name():
    """  
    Find item in the worksheet before updating or deleting
    """   
   # cell = VAULT_WORKSHEET.find("search_criteria", in_column=1)

def update_recipe():
    """
    Update existing recipe in the worksheet
    """

def delete_recipe():
    """
    Find the recipe in the worksheet and delete row
    """

def main_menu():
    while True:
        print("Welcome to your online recipe book! Please choose from the following options to proceed:")
        print("\nMain Menu")
        print("1. Add Recipe")
        print("2. Update Recipe")
        print("3. Delete Recipe")
        print("4. Find recipe by name")
        print("#. View all recipe names")
        print("5. Exit")

        choice = input("Enter your menu choice (1-6): \n")

        if choice == "1\n":
            add_new_recipe()
        elif choice == "2\n":
            update_recipe()
        elif choice == "3\n":
            update_recipe()
        elif choice == "4\n":
            find_recipe_by_name()
        elif choice == "5\n":
            print("Exiting menu, bye babes...")
            break
        else:
            print("Please pick a number between 1 and 6:")
        
if __name__ == "__main__":
    main_menu()
    push_to_vault()
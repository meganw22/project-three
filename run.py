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
    Add a recipe to the Vault worksheet database
    Confirms data and sends data to the vault worksheet
    """
    print("Let's create a new recipe!")
    recipe_name = input("Enter recipe name here:  \n").capitalize()
    
    while True:
        servings_str = input("Enter number of servings:  \n")
        # change serving number to an integer
        try:
            servings = int(servings_str)
            break
        except ValueError:
            print("Error! Please enter a whole number for servings:")

    # Enter ingredients
    ingredients_str = input("Enter the ingredients (separated by commas): \n")
    ingredients = ingredients_str.split(",")

    # Print the inforation back to the user for confirmation
    print("\nThis is your new recipe:")
    print(f"New recipe is called: {recipe_name}")
    print(f"Number of servings: {servings}")
    print(f"Your ingredients are: {ingredients} \n")

    user_answer_recipe = input("Is this information correct? Yes/No\n").lower()
    if user_answer_recipe == "yes":
        ingredients_combo = ", ".join(ingredients)
        VAULT_WORKSHEET.append_row([recipe_name, servings, ingredients_combo])
        print("Vault updated. Recipe added successfully\n")
    else:
            print("Recipe not added to database, please try again.")

def update_recipe():
    """
    Update existing recipe in the worksheet
    """    

def delete_recipe():
    """
    Find the recipe in the worksheet and delete row
    """

def find_recipe_name():
    """  
    Find item in the worksheet before updating or deleting
    """   
    recipe_name_to_find = input("Enter recipe name to find: \n").capitalize()

    try:
        cell = VAULT_WORKSHEET.find(recipe_name_to_find, in_column=1)
        print(f"recipe found on row {cell.row}")
        print("Recipe Details:")
        print(f"Name: {VAULT_WORKSHEET.cell(cell.row, 1).value}")
        print(f"Servings: {VAULT_WORKSHEET.cell(cell.row, 2).value}")
        print(f"Ingredients: {VAULT_WORKSHEET.cell(cell.row, 3).value}")
    except: 
        print(f"Recipe '{recipe_name_to_find}' not found")

def view_all_recipes():
    """
    Full index of 'Recipe Names' for the user to view.
    One Recipe per line
    """
    print("Recipes in the Vault: ")
    column_index = 1
    try:
        all_recipes = VAULT_WORKSHEET.col_values(column_index)

        for recipe_name in all_recipes:
            print(f"Name: {recipe_name}")
    
    except Exception as e:
        print(f"Error: {e}")


def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Add Recipe")
        print("2. Update Recipe")
        print("3. Delete Recipe")
        print("4. View a recipe")
        print("5. View all recipes by name")
        print("6. Exit")

        choice = input("Enter your menu choice (1-5): \n")

        if choice == "1":
            add_new_recipe()
        elif choice == "2":
            update_recipe()
        elif choice == "3":
            update_recipe()
        elif choice == "4":
            find_recipe_name()
        elif choice == "5":
            view_all_recipes()
        elif choice == "6":
            print("Exiting menu, bye babes...")
            break
        else:
            print("Please pick a number between 1 and 5:")
        
if __name__ == "__main__":
    main_menu()
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
    recipe_name = input("Enter recipe name here:  ")
    
    # Enter a whole number for servings
    while True:
        servings_str = input("Enter number of servings:  ")
        try:
            servings = int(servings_str)
            break
        except ValueError:
            print("Error! Please enter a whole number for servings:")

    # Enter ingredients
    ingredients_str = input("Enter the ingredients (separated by commas):  ")
    ingredients = ingredients_str.split(",")

    # Print the inforation back to the user for confirmation
    print("\nThis is your new recipe:")
    print(f"New recipe is called: {recipe_name}")
    print(f"Number of servings: {servings}")
    print(f"Your ingredients are: {ingredients_str} \n")

    user_answer_recipe = input("Is this information correct? Yes/No\n").lower()

    return (recipe_name, servings, ingredients) if user_answer_recipe == "yes" else None

def push_to_vault(recipe_data):
    """
    Appends a new row to the vault worksheet
    """
    ingredients_combo = ",".join(recipe_data[2])

    VAULT_WORKSHEET.append_row([recipe_data[0], recipe_data[1], ingredients_combo])
    
def confirmation():
    """
    Confirms data and sends data to the vault worksheet
    """
    while True:
        recipe_data = add_new_recipe()
        if recipe_data:
            print("Updating your recipe database...\n")
            push_to_vault(recipe_data)   
            print("vault updated. Recipe added successfully")
            break
        else:
            print("Recipe not added to database, please try again.")

confirmation()
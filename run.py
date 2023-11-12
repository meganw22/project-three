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
    ingredients = input("Enter the ingredients (separated by commas):  ")

    # Print the inforation back to the user for confirmation
    print("\nThis is your new recipe:")
    print(f"New recipe is called: {recipe_name}")
    print(f"Number of servings: {servings}")
    print(f"Your ingredients are: {ingredients} \n")

    print("Is this information correct? Yes/No ")
    user_answer_recipe = input().lower()
    return user_answer_recipe

def confirmation():
    """
    Create a loop to confirm if yes or no has been typed
    """
    while True:
        user_answer_recipe = add_new_recipe()
        if user_answer_recipe == "yes":
            break
        else:
            print("")

    
def pull_vault_data():
    """
    Retrieve data from the vault worksheet
    """

confirmation()
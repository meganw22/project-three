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
    print("What is the name of your recipe?")
    recipe_name = input(" \n")
    print(f"New recipe is called: {recipe_name}\n")
    print("Is this correct? Yes/No ")
    user_answer = input().lower()
    return user_answer

def confirmation():
    """
    Create a loop to confirm if yes or no has been typed
    """
    while True:
        user_answer = add_new_recipe()
        if user_answer == "yes":
            break
        else:
            print("----")

    
def pull_vault_data():
    """
    Retrieve data from the vault worksheet
    """

add_new_recipe()
confirmation()
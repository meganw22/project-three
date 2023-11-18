import gspread
from google.oauth2.service_account import Credentials
from colorama import init, Fore, Style

init()

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
column_data = VAULT_WORKSHEET.col_values(1)


# Function to 
def search_recipe(value, column_data):
    """Check if a value is in the column data in the Vault Worksheet"""
    return value in column_data


def create_recipe_name(column_data):
    """Gets the user input and checks if its a unique recipe name"""
    while True:
        recipe_name = input("\nEnter your unique recipe name here: "
        "\nExample: 'Shepherds Pie' or 'Banana Smoothie no. 3'\n").lower()

        if not recipe_name:
            print(
                Fore.RED +
                "Don't leave blank! Add your recipe name here: "
                + Style.RESET_ALL
                )
        elif search_recipe(recipe_name, column_data):
            print(
                Fore.RED +
                f"The recipe name '{recipe_name}' has already been used. "
                "Please enter a new recipe name!" + Style.RESET_ALL
                )
        else:
            print(f"You have called your recipe: {recipe_name}")
            return recipe_name


def num_servings():
    """
    Gets user input for number of servings per recipe
    change serving number to an integer
    ensure servings are not negative values
    """
    while True:
        servings_str = input("\nEnter number of servings:  \n")
        if servings_str.isdigit():
            servings = int(servings_str)
            if servings > 0:
                return servings
            else:
                print(Fore.RED + "Error! Servings cannot be less than 1 "
                "Please try again" + Style.RESET_ALL)
        elif not servings_str.strip():
            print(
                Fore.RED + "Don't leave blank! " 
                "Enter the number of servings here:" + Style.RESET_ALL
                )
            
        else:
            print(Fore.RED + "Error! Please enter a valid "
            "whole number for servings:" + Style.RESET_ALL)


def enter_ingredients():
    """ 
    User input of ingredients as strings and format the ingredients
    additional: if user has entered one only ingredient, confirm choice
    """
    while True:
        ingredients_str = input("\n Please enter the ingredients " 
        "(separated by commas): \n"
        "For example: 175g self-raising flour, 2 large eggs\n").lower()

        if not ingredients_str:
            print(
                    Fore.RED + "Don't leave blank! " 
                    "Enter your ingredients here:" + Style.RESET_ALL
                    )
        else:
            ingredients_split = ingredients_str.split(",")
            ingredients = [ingredient.strip() for ingredient in ingredients_split]
            return ingredients


def process_recipe(recipe_name, servings, ingredients):
    """
    Print recipe details back to the user
    """
    print(Fore.GREEN + "\nThese are your recipe details:" )
    print(f"New recipe is called: {recipe_name}")
    print(f"Number of servings: {servings}")
    print(f"Your ingredients are: {ingredients} \n" + Style.RESET_ALL)


def specific_name():
    """  
    Find item in the worksheet by name (column 1 value)
    """   
    recipe_to_find = input("Enter recipe name: \n").lower()

    try:
        print(Fore.GREEN + "\nRecipe Details:")
        print(f"Name: {VAULT_WORKSHEET.cell(cell.row, 1).value}")
        print(f"Servings: {VAULT_WORKSHEET.cell(cell.row, 2).value}")
        print(f"Ingredients: {VAULT_WORKSHEET.cell(cell.row, 3).value}" + Style.RESET_ALL)
    except: 
        print(f"Recipe '{recipe_to_find}' not found" + Style.RESET_ALL)

def update_recipe_menu():
    """
    Update existing recipe in the worksheet
    """
    attempts = 1
    while attempts < 2:
        recipe_to_update = input("\nWhich recipe would you like to update?\n").lower()
        if search_recipe(recipe_to_update, column_data):
            print(f"Recipe found on row {cell.row}")
            change_recipe_details()
        elif not recipe_to_update.strip():
            print(
                    Fore.RED +
                    "Don't leave blank! Enter your recipe name here: "
                    + Style.RESET_ALL
                    )
        else:
            print(Fore.RED + f"Recipe '{recipe_to_update}' not found, " 
            + Style.RESET_ALL + "Here are all the available recipes:\n")
            view_all_recipes()
            attempts += 1

def change_recipe_details():
    print(
    "\n Which value do you want to change?\n"
    "1. Recipe name\n"
    "2. Number of servings\n"
    "3. Ingredients\n"
    "4. Cancel recipe update\n")

    choice = int(input("Enter your choice (1-4)\n"))
    if 1 <= choice <= 4:
        print(f"You chose: {choice}")
    else:
        print("Invalid choice! Please pick a number between 1 and 4")

    if choice == 1:
        updated_name = input("Enter new name: ").strip()
        VAULT_WORKSHEET.update_cell(cell.row, 1, updated_name)
        print("Updated successfully!")
    elif choice == 2:
        updated_servings = input("Enter new number of servings: ").strip()
        VAULT_WORKSHEET.update_cell(cell.row, 2, updated_servings)
        print("Updated successfully!")
    elif choice == 3:
        update_ingredients()
        print("Updated successfully!")
    elif choice == 4:
        print(Fore.RED + 
            "Recipe update cancelled. Returning to Main Menu"
            + Style.RESET_ALL)
        return
    else:
        print("Error! Please pick a number between 1 and 3")



def delete_recipe():
    """
    Find the recipe in the worksheet and delete row
    """
    while True:
        recipe_name_to_delete = input("\nWhich recipe would you like to delete?\n").lower()
        print("Please note: that if you delete a recipe, it cannot be restored")
        try:
            cell = VAULT_WORKSHEET.find(recipe_name_to_delete, in_column=1)
            print(f"Recipe found on row {cell.row}")

            delete_recipe = input("\n Are you sure you want to delete this recipe? (yes/no)").lower()
            if delete == "yes":
                VAULT_WORKSHEET.delete_row([recipe_name, servings, ingredients_combo])
                print("Vault updated. Recipe Deleted\n")
            elif delete == "no":
                print("Recipe not deleted, returning to main menu")
                return
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        except:
            print("Oops, something went wrong, recipe NOT deleted!")



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
        print(
        """
        \nMain Menu
        1. Add Recipe
        2. Update Recipe
        3. Delete Recipe
        4. Find a specific recipe
        5. View all recipes
        6. Exit
        """
        )

        choice = input("Enter your menu choice (1-6): \n")

        if choice == "1":
            while True:
                recipe_name = create_recipe_name(column_data)
                servings = num_servings()
                ingredients = enter_ingredients()
                process_recipe(recipe_name, servings, ingredients)

                details_correct = input("Is this information correct? Yes/No \n"
                "   or enter 'exit' to return to main menu: \n").lower()
                if details_correct == "yes":
                    ingredients_combo = ", ".join(ingredients)
                    VAULT_WORKSHEET.append_row([recipe_name, servings, ingredients_combo])
                    print(Fore.GREEN + 
                        "Vault updated. Recipe added successfully!!\n"
                        "Returning to main menu..."
                        + Style.RESET_ALL)
                    break
                elif details_correct == "no":
                    print(f"You chose '{choice}', your new recipe was not "
                    "added to database")
                elif details_correct == "exit":
                    print("Returning to main menu...")
                    break
                else:
                    print(Fore.RED +
                        "Error! please input 'yes' or 'no'"
                        + Style.RESET_ALL)
        elif choice == "2":
            update_recipe_menu()
        elif choice == "3":
            delete_recipe()
        elif choice == "4":
            specific_name()
        elif choice == "5":
            view_all_recipes()
        elif choice == "6":
            print("Exiting menu, bye babes...")
            break
        else:
            print(Fore.RED + f"Error! '{choice}' is not a number between " 
            "1 and 6. Please try again!" + Style.RESET_ALL)
        
if __name__ == "__main__":
    main_menu()
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

# Function to check if a value is in the column data in the Vault Worksheet
def search_recipe(value, column_data):
    return value in column_data


def create_recipe_name(column_data):
    """
    Gets the user input and checks if its a unique recipe name
    """
    while True:
        recipe_name = input("\nEnter your unique recipe name here:  \n").lower()
        if search_recipe(recipe_name, column_data):
            print(f"The recipe name '{recipe_name}' has already been used.")
        else:
           return recipe_name


def num_servings():
    """
    Gets user input for number of servings per recipe
    change serving number to an integer
    ensure servings are not negative values
    """
    while True:
        servings_str = input("Enter number of servings:  \n")
        
        try:
            servings = int(servings_str)
            if servings >= 0:
                return servings
            else:
                print("Error! Servings cannot be a negative number")
        except ValueError:
            print("Error! Please enter a whole number for servings:")


def enter_ingredients():
    """
    User input of ingredients as strings
    Format the ingredients
    """
    ingredients_str = input("Enter the ingredients (separated by commas): \n")
    ingredients_split = ingredients_str.split(",")
    ingredients = [ingredient.strip() for ingredient in ingredients_split]
    #print(f" Ingredients: {ingredients}")
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
    recipe_name_to_find = input("Enter recipe name: \n").lower()

    try:
        cell = VAULT_WORKSHEET.find(recipe_name_to_find, in_column=1)
       # print(f"recipe found on row {cell.row}")
        print(Fore.GREEN + "\nRecipe Details:")
        print(f"Name: {VAULT_WORKSHEET.cell(cell.row, 1).value}")
        print(f"Servings: {VAULT_WORKSHEET.cell(cell.row, 2).value}")
        print(f"Ingredients: {VAULT_WORKSHEET.cell(cell.row, 3).value}" + Style.RESET_ALL)
    except: 
        print(f"Recipe '{recipe_name_to_find}' not found")

def update_recipe():
    """
    Update existing recipe in the worksheet
    """
    while True:
        recipe_name_to_update = input("\nWhich recipe would you like to update?\n").lower()

        try:
            cell = VAULT_WORKSHEET.find(recipe_name_to_update, in_column=1)
            print(f"Recipe found on row {cell.row}")

            print("\n Which value do you want to change?")
            print("1. Recipe name")
            print("2. Number of servings")
            print("3. Ingredients")
            print("4. Cancel recipe update")

            try:
                choice = int(input("Enter your choice (1-4)\n"))
                if 1 <= choice <= 4:
                    print(f"You chose: {choice}")
                else:
                    print("Invalid choice! Please pick a number between 1 and 4")
            except ValueError:
                print("Error! Please pick a number between 1 and 4")

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
                print("Recipe update cancelled")
                return
            else:
                print("Error! Please pick a number between 1 and 3")
            
        except:
            print(f"Recipe '{recipe_name_to_update}' not found, please try again.")



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
        print("\nMain Menu")
        print("1. Add Recipe")
        print("2. Update Recipe")
        print("3. Delete Recipe")
        print("4. Find a specific recipe")
        print("5. View all recipes")
        print("6. Exit")

        choice = input("Enter your menu choice (1-6): \n")

        if choice == "1":
            while True:
                recipe_name = create_recipe_name(column_data)
                servings = num_servings()
                ingredients = enter_ingredients()
                process_recipe(recipe_name, servings, ingredients)

                details_correct = input("Is this information correct? Yes/No\n").lower()
                if details_correct == "yes":
                    ingredients_combo = ", ".join(ingredients)
                    VAULT_WORKSHEET.append_row([recipe_name, servings, ingredients_combo])
                    print("Vault updated. Recipe added successfully\n")
                    break
                else:
                    print("Recipe not added to database, restarting recipe entry... ")
        elif choice == "2":
            
            update_recipe()
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
            print("Please pick a number between 1 and 6:")
        
if __name__ == "__main__":
    main_menu()
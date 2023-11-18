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


def search_recipe(value, column_data):
    """Check if a value is in the column data in the Vault Worksheet"""
    return value in column_data
    

def create_recipe_name(column_data):
    """Gets the user input and checks if its a unique recipe name"""
    while True:
        recipe_name = input(
            "\nEnter your unique recipe name here: "
            "\nExample: 'Shepherds Pie' or 'Banana Smoothie no. 3'\n"
            ).lower()

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
                print(
                    Fore.RED +
                    "Error! Servings cannot be less than 1. Please try again"
                    + Style.RESET_ALL
                    )
        elif not servings_str.strip():
            print(
                Fore.RED +
                "Don't leave blank! Enter the number of servings here:"
                + Style.RESET_ALL
                )
        else:
            print(
                Fore.RED +
                "Error! Please enter a valid whole number for servings:"
                + Style.RESET_ALL
                )


def enter_ingredients():
    """
    User input of ingredients as strings and format the ingredients
    additional: if user has entered one only ingredient, confirm choice
    """
    while True:
        ingredients_str = input(
            "\n Please enter the ingredients "
            "(separated by commas): \n"
            "For example: 175g self-raising flour, 2 large eggs\n"
            ).lower()

        if not ingredients_str:
            print(
                Fore.RED +
                "Don't leave blank! "
                "Enter your ingredients here:"
                + Style.RESET_ALL
                )
        else:
            ingredients_split = ingredients_str.split(",")
            ingredients = [
                ingredient.strip() for ingredient in ingredients_split
                ]
            return ingredients


def process_recipe(recipe_name, servings, ingredients):
    """
    Print recipe details back to the user
    """
    print(Fore.GREEN + "\nThese are your recipe details:")
    print(f"New recipe is called: {recipe_name}")
    print(f"Number of servings: {servings}")
    print(f"Your ingredients are: {ingredients} \n" + Style.RESET_ALL)


def specific_name():
    """
    Find item in the Vault worksheet by name
    List recipe details and print ingredients as a list.
    """

    while True:
        recipe_to_find = input(
            Fore.BLUE +
            "Enter recipe name here: "
            "(type 'exit' to return to main menu)\n"
            + Style.RESET_ALL
        ).lower()

        if recipe_to_find == 'exit':
            print(
                Fore.YELLOW +
                "Returning to Main Menu..."
                + Style.RESET_ALL
                )
            return

        cell = VAULT_WORKSHEET.find(recipe_to_find, in_column=1)

        if cell:
            print(
                Fore.YELLOW +
                "Please wait while your recipe loads..."
                + Style.RESET_ALL
                )
            display_recipe_details(cell, recipe_to_update=False)

            while True:
                user_choice = input(
                    "\nWhat would you like to do?"
                    "\n1. Find another recipe"
                    "\n2. Return to the main menu"
                    "\nEnter your choice (1 or 2):\n"
                    )
                if user_choice == '1':
                    print("You asked to find a new recipe:")
                    specific_name()
                    continue
                elif user_choice == '2':
                    print(
                        Fore.YELLOW +
                        "Returning to 'find specific recipe' menu..."
                        + Style.RESET_ALL
                    )
                    return_to_main_menu = True
                    break
                else:
                    print(
                        Fore.RED +
                        "Invalid choice, please pick 1 or 2"
                        + Style.RESET_ALL
                    )

        elif not recipe_to_find.strip():
            print(
                Fore.RED +
                "Don't leave blank! Enter a recipe here:"
                + Style.RESET_ALL
                )
            continue

        else:
            print(
                Fore.RED +
                f"Recipe '{recipe_to_find}' not found"
                + Style.RESET_ALL
                )


def display_recipe_details(cell, recipe_to_update):
    """ Display the current receipe details when called"""

    display_recipe_name = VAULT_WORKSHEET.cell(cell.row, 1).value
    display_servings = VAULT_WORKSHEET.cell(cell.row, 2).value
    display_ingredients = VAULT_WORKSHEET.cell(cell.row, 3).value.split(", ")

    print(
        f"Recipe Name: {display_recipe_name}\n"
        f"Servings: {display_servings}\n"
        f"Ingredients: {display_ingredients}\n"
    )


def update_recipe_menu():
    """
    Update existing recipe in the worksheet
    User has 2 attempts to enter a correct recipe,
    If attempts unsuccessful, all current recipes are printed to terminal
    in a list format for user guidance.
    """
    attempts = 1
    max_attempts = 2
    while attempts <= max_attempts:
        recipe_to_update = input(
            Fore.BLUE +
            "\nWhich recipe would you like to update?\n"
            + Style.RESET_ALL
            ).lower()
        cell = VAULT_WORKSHEET.find(recipe_to_update, in_column=1)

        if search_recipe(recipe_to_update, column_data):
            print(
                f"Recipe {recipe_to_update} has been found on row {cell.row}"
                )
            change_recipe_details(cell, recipe_to_update)
            break

        elif not recipe_to_update.strip():
            print(
                    Fore.RED +
                    "Don't leave blank! Enter your recipe name here: "
                    + Style.RESET_ALL
                    )
        else:
            if attempts < max_attempts:
                print(
                    Fore.RED + f"Recipe '{recipe_to_update}' not found, "
                    + Style.RESET_ALL
                )
                attempts += 1
            else:
                print(Fore.RED + f"Recipe '{recipe_to_update}' not found.")
                print(Fore.BLUE + "Here are all the available recipes:")
                view_all_recipes()
                print("please choose a recipe from the list to continue...")
                print(Style.RESET_ALL)
                continue


def update_recipe_name(cell):
    """ Update the recipe name"""
    updated_name = input("Enter new name: ").strip()
    VAULT_WORKSHEET.update_cell(cell.row, 1, updated_name)
    print(
        Fore.GREEN +
        "Recipe name updated successfully!"
        + Style.RESET_ALL
    )


def update_servings(cell):
    """Update number of servings"""
    updated_servings = input("Enter new number of servings: ").strip()
    VAULT_WORKSHEET.update_cell(cell.row, 2, updated_servings)
    print(
        Fore.GREEN +
        "Number of servings updated successfully!"
        + Style.RESET_ALL
    )


def update_ingredients(cell):
    """User input to update existing ingredients"""
    while True:
        updated_ingr_str = input(
            Fore.BLUE +
            "\n Copy your previous list of ingredients from above "
            "(without [ ]) and edit as you require"
            + Style.RESET_ALL +
            "\n Please enter the updated ingredients "
            "(separated by commas): \n"
            "For example: 200g self-raising flour, 3 large eggs\n"
            ).lower()

        if not updated_ingr_str:
            print(
                Fore.RED +
                "Don't leave blank! "
                "Enter your ingredients here:"
                + Style.RESET_ALL
            )
        else:
            updated_ingr_split = updated_ingr_str.split(",")
            updated_ingredients = [
                ingredient.strip() for ingredient in updated_ingr_split
            ]
            VAULT_WORKSHEET.update_cell(cell.row, 3, updated_ingr_str)
            break

    print(
        Fore.GREEN +
        "Ingredients updated successfully!"
        + Style.RESET_ALL
    )
    return updated_ingredients

def change_recipe_details(cell, recipe_to_update):
    """
    User input overwrites the current recipe details as specified by user,
    Details are shown before user input,
    User makes changes,
    Details are displayed again after recipe changes.
    """

    print(
        Fore.GREEN +
        f"These are the current recipe details for '{recipe_to_update}'"
        + Style.RESET_ALL
        )
    display_recipe_details(cell, recipe_to_update)

    print(
        Fore.BLUE + "\n Which value do you want to change?\n"
        + Style.RESET_ALL +
        "1. Recipe name\n"
        "2. Number of servings\n"
        "3. Ingredients\n"
        "4. Cancel recipe update and return to main menu\n"
    )

    while True:
        try:
            choice = int(input("Enter your choice (1-4)\n"))
            if 1 <= choice <= 4:

                if choice == 1:
                    update_recipe_name(cell)
                    break
                elif choice == 2:
                    update_servings(cell)
                    break
                elif choice == 3:
                    update_ingredients(cell)
                    break
                elif choice == 4:
                    print(
                        Fore.YELLOW +
                        "Recipe update cancelled. Returning to Main Menu..."
                        + Style.RESET_ALL
                    )
                    break
            else:
                print(
                    Fore.RED +
                    "Invalid number! Please pick a number between 1 and 4"
                    + Style.RESET_ALL
                )
        except ValueError:
            print(
                Fore.RED +
                "Invalid choice! Please pick a number between 1 and 4"
                + Style.RESET_ALL
            )


def delete_recipe():
    """
    Find the recipe in the worksheet and delete row
    """
    while True:
        recipe_name_to_delete = input(
            Fore.BLUE +
            "\nWhich recipe would you like to delete?\n"
            + Style.RESET_ALL +
            Fore.RED +
            "Please note: that if you delete a recipe, it cannot be restored"
            + Style.RESET_ALL +
            "\nEnter recipe to delete here:\n"
        ).lower()

        cell = None

        # Check if the recipe exists
        for row in VAULT_WORKSHEET.findall(recipe_name_to_delete, in_column=1):
            cell = row
            break

        if cell:
            print(f"Recipe is currently on row {cell.row}\n")
            while True:

                delete_recipe_input = input(
                    Fore.BLUE +
                    "You are about to delete the "
                    f"recipe '{recipe_name_to_delete}'"
                    "\nAre you sure you want to delete the recipe? (yes/no)\n"
                    + Style.RESET_ALL +
                    "If you choose 'no' "
                    "you will be returned to the Main Menu:\n"
                    ).lower()

                if delete_recipe_input == "yes":
                    VAULT_WORKSHEET.delete_rows(cell.row)
                    print(
                        Fore.GREEN +
                        "Recipe has been successfully deleted, "
                        "and Vault updated\n"
                        + Style.RESET_ALL
                        )
                    print(
                        Fore.YELLOW +
                        "/nNow returning you to the main menu..."
                        + Style.RESET_ALL
                        )
                    return

                elif delete_recipe_input == "no":
                    print(
                        f"\nYou chose not to delete '{recipe_name_to_delete}.'"
                        + Fore.YELLOW +
                        "\nNow returning you to the main menu..."
                        + Style.RESET_ALL)
                    return

                else:
                    print(
                        Fore.RED +
                        "\nInvalid input. Please enter 'yes' or 'no'.\n"
                        + Style.RESET_ALL
                        )
        else:
            print(
                Fore.RED +
                "Oops, it appears there's no recipe with the "
                f"name '{recipe_name_to_delete}', Please try another name!"
                + Style.RESET_ALL
            )


def view_all_recipes():
    """
    Full index of 'Recipe Names' for the user to view.
    One Recipe per line
    """
    while True:
        print(
            Fore.BLUE +
            "\nViewing all recipes in the Vault: "
            + Style.RESET_ALL)
        column_index = 1
        try:
            all_recipes = VAULT_WORKSHEET.col_values(column_index)[1:]

            for recipe_name in all_recipes:
                print(f"- {recipe_name}")

            user_choice = input("Press 'enter' button on your keyboard"
            " to return to the main menu\n")

            if user_choice == '':
                print(
                    Fore.YELLOW +
                    "Returning to the main menu..."
                    + Style.RESET_ALL
                    )
                break

            else:
                print(
                    Fore.RED +
                    "Invalid input, please press the 'enter' button: "
                    + Style.RESET_ALL
                )

        except Exception as e:
            print(f"Error: {e}")


def display_menu():
    print(
        """
    Main Menu
    1. Add Recipe
    2. Update Recipe
    3. Delete Recipe
    4. View a specific recipe
    5. View all recipes
    6. Exit
    """
    )


def get_menu_choice():
    """Return choice of menu item and select item in list"""
    return input("Enter your menu choice (1-6): \n")


def handle_add_recipe():
    """ Function for adding a complete new recipe to the Vault"""

    recipe_name = create_recipe_name(column_data)
    servings = num_servings()
    ingredients = enter_ingredients()
    process_recipe(recipe_name, servings, ingredients)

    while True:
        details_correct = input(
            "Is this information correct? Yes/No \n"
            " or enter 'exit' to return to main menu: \n"
            ).lower()

        if details_correct == "yes":
            ingredients_combo = ", ".join(ingredients)
            VAULT_WORKSHEET.append_row(
                [recipe_name, servings, ingredients_combo]
                )
            print(
                Fore.GREEN +
                "Vault updated. Recipe added successfully!!\n"
                + Fore.YELLOW +
                "Returning to main menu..."
                + Style.RESET_ALL
                )
            break
        elif details_correct == "no":
            print(
                Fore.RED +
                f"Your new recipe was not added to database"
                "\n Returning to main menu..."
                + Style.RESET_ALL
                )
            break

        elif details_correct == "exit":
            print(
                Fore.YELLOW +
                "\nReturning to main menu..."
                + Style.RESET_ALL
                )
            break

        else:
            print(
                Fore.RED +
                "Error! Please enter 'yes' or 'no'"
                + Style.RESET_ALL
            )

    else:
        print(
            Fore.RED +
            "Error! please input 'yes' or 'no'"
            + Style.RESET_ALL
            )


def handle_update_recipe():
    """Function for calling the recipe update menu"""
    update_recipe_menu()


def handle_delete_recipe():
    """Function for calling the delete recipe menu"""
    delete_recipe()


def handle_view_specific_recipe():
    """Function for calling the find specific recipe menu """
    specific_name()


def handle_view_all_recipes():
    """Function for viewing all recipes """
    view_all_recipes()


def main_menu():
    """Start of Program function """
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "1":
            handle_add_recipe()
        elif choice == "2":
            handle_update_recipe()
        elif choice == "3":
            handle_delete_recipe()
        elif choice == "4":
            handle_view_specific_recipe()
        elif choice == "5":
            handle_view_all_recipes()
        elif choice == "6":
            print(
                Fore.YELLOW +
                "Exiting the program, See you later!"
                + Style.RESET_ALL
            )
            break
        else:
            print(
                Fore.RED +
                f"Error! '{choice}' is not a number between "
                "1 and 6. Please try again!"
                + Style.RESET_ALL
            )


main_menu()

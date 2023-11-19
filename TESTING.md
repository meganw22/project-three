# TESTING.md
## Testing of the Recipe Generator
This program has been through extensive testing to account for every option of validation and positive user experience.



## Contents of Test Procedures
The 'Main Menu' consists of a list of options the user can select:
### Main Menu
* [1. ADD RECIPE](#1-add-recipe)
* [2. UPDATE RECIPE](#2-update-recipe)
* [3. DELETE RECIPE](#3-delete-recipe)
* [4. VIEW SPECIFIC RECIPE](#4-view-specific-recipe)
* [5. VIEW ALL RECIPES](#5-view-all-recipes)
* [6. EXIT](#6-exit)

## 1. ADD RECIPE
This table contains full functional testing for the 1st option, Add Recipe:

| Main Menu: Functional testing for "1. Add Recipe" |                                                       |                         |         |
| ------------------------------------------------- | ---------------------------------------------------- | ----------------------- | ------- |
| **action taken**                                  | **expected result**                                      | **actual result**           | **outcome** |
| **enter recipe**                                      |
| Choice "1" entered                                | comment show for 'enter your unique recipe'          | result matches expected | Pass    |
| Brand new recipe entered                          | success comment, continue to servings                | result matches expected | Pass    |
| re-existing recipe entered                        | error; recipe already exists comment, loop continues | result matches expected | Pass    |
| blank entry                                       | blank entry error                                    | result matches expected | Pass    |
| **enter servings**                                    |
| valid serving number                              | continues to ingredients                             | result matches expected | Pass    |
| less than 1 serving entered                       | error message for cannot be less than 1 serving      | result matches expected | Pass    |
| non integer                                       | error, not a valid whole number                      | result matches expected | Pass    |
| blank entry                                       | don’t not leave blank entry                          | result matches expected | Pass    |
| **enter ingredients**                                 |
| enter ingredients                                 | proceeds to 'process_recipe'                         | result matches expected | Pass    |
| blank entry                                       | do not leave blank entry error                       | result matches expected | Pass    |
| prints recipe details to user                     | recipe details are the same as user input details    | result matches expected | Pass    |
| **details correct**                                  |
| yes                                               | Success recipe upload to vault                       | result matches expected | Pass    |
| no                                                | Recipe not added to database, return to menu         | result matches expected | Pass    |
| exit                                              | return to main menu                                  | result matches expected | Pass    |
| anything other than yes/no                        | Error; "enter yes or no"                             | result matches expected | Pass    |


## 2. UPDATE RECIPE
This table contains full functional testing for the 2nd option, Update Recipe:

| Functional testing for "2. Update Recipe" |                                                                                                     |                         |         |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------- | ------- |
| **action taken**                          | **expected result**                                                                                 | **actual result**       | **outcome** |
| Choice "2" entered                        | comment shown: "which recipe to update"                                                             | result matches expected | Pass    |
| existing recipe name entered              | recipe (name) has been found on row (number) with details of recipe, name, servings and ingredients | result matches expected | Pass    |
| incorrect recipe entered                  | error code, 'recipe not found' shown                                                                | result matches expected | Pass    |
| nothing entered                           | error code, 'don’t leave blank' shown                                                               | result matches expected | Pass    |
| **correct recipe name entered**           |
| enter choice 1                            | enter new name text shown                                                                           | result matches expected | Pass    |
| enter choice 2                            | enter new number of servings text shown                                                             | result matches expected | Pass    |
| enter choice 3                            | enter new ingredients                                                                               | result matches expected | Pass    |
| enter choice 4                            | recipe update cancelled message shown                                                               | result matches expected | Pass    |
| choice 1, new name text entered           | recipe updated successfully shown, return to main menu                                              | result matches expected | Pass    |
| choice 2, new servings no. entered        | recipe updated successfully shown, return to main menu                                              | result matches expected | Pass    |
| choice 3, new ingredients entered         | recipe updated successfully shown, return to main menu                                              | result matches expected | Pass    |
| choice 4, cancel recipe change option     | recipe not updated message shown, return to main menu                                               | result matches expected | Pass    |


## 3. DELETE RECIPE
This table contains full functional testing for the 3rd option, Delete Recipe:

| Functional testing for "3. Delete Recipe" |                                                               |                         |         |
| ----------------------------------------- | ------------------------------------------------------------- | ----------------------- | ------- |
| **action taken**                              | **expected result**                                               | **actual result**           | **outcome** |
| Choice "3" Entered                        | comment: "which recipe to delete" shown                       | result matches expected | Pass    |
| correct recipe name entered               | comment to prove (name) exists, continues to yes/no steps     | result matches expected | Pass    |
| wrong recipe entered                      | oops comment shown and loop to reeneter valid recipe          | result matches expected | Pass    |
| blank entered                             | oops comment shown and loop to reeneter valid recipe          | result matches expected | Pass    |
| delete recipe, choice yes                 | Deletes recipe, comment shown to prove this                   | result matches expected | Pass    |
| delete recipe, choice no                  |  Recipe is not deleted, returns to main menu                  | result matches expected | Pass    |
| delete recipe, choice 'blank'             | Invalid input error shown, loops to re-enter choice of yes/no | result matches expected | Pass    |


## 4. VIEW SPECIFIC RECIPE
This table contains full functional testing for the 4th option, View Specific Recipe:

| Functional testing for "4. Find specific recipe" |                                                                  |                         |         |
| ------------------------------------------------ | ---------------------------------------------------------------- | ----------------------- | ------- |
| **action taken**                                     | **expected result**                                                  | **actual result**           | **outcome** |
| Choice "4" entered                               | comment: enter recipe or exit to return to menu                  | result matches expected | Pass    |
| correct recipe name entered                      | Loads recipe comment, loads recipe details, continues to choices | result matches expected | Pass    |
| wrong recipe name entered                        | error code, 'recipe not found' shown                             | result matches expected | Pass    |
| blank                                            | error code, 'don’t leave blank' shown                            | result matches expected | Pass    |
| exit entered                                     | returns to main menu                                             | result matches expected | Pass    |
| choice 1, find another recipe entered            | specific name function starts over                               | result matches expected | Pass    |
| choice 2, return to specific recipe menu         | returns to specific recipe menu                                  | result matches expected | Pass    |


## 5. VIEW ALL RECIPES
This table contains full functional testing for the 5th option, View All Recipe:

| Functional testing for "5. View all recipes" |                                                      |                         |         |
| -------------------------------------------- | ---------------------------------------------------- | ----------------------- | ------- |
| **action taken**                                 | **expected result**                                      | **actual result**           | **outcome** |
| Choice "5" entered                           | All recipes from database are shown                  | result matches expected | Pass    |
| enter button press to exit                   | returns to main menu                                 | result matches expected | Pass    |
| any other button pressed                     | Invalid input error shown, loops to view all recipes | result matches expected | Pass    |


## 6. EXIT
This table contains full functional testing for the last option, Exit:

| Functional testing for "6. Exit" |                                           |                         |         |
| -------------------------------- | ----------------------------------------- | ----------------------- | ------- |
| **action taken**                     | **expected result**                           | **actual result**           | **outcome** |
| Choice "6" entered               | Exits Program                             | result matches expected | Pass    |
| Blank entered                    | error: (input) not a number between 1 - 6 | result matches expected | Pass    |
| not 1 - 6 entered                | error: (input) not a number between 1 - 6 | result matches expected | Pass    |

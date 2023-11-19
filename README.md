# Recipe eBook

![amiresponsive](https://github.com/meganw22/project-three/assets/141934888/54c3e583-db8b-46e8-b77f-843fbfbc604f)

Recipe eBook is a console based recipe management system which uses Google Sheets for storage.

The program allows users to add, update, delete and view recipes in real-time.

* Visit the deployed terminal through Heroku: [Recipe Book](https://recipe-generator-p3-4a1ceeda2446.herokuapp.com/)

## User Experience
### User Stories
  * As a user, I want to have an online recipe management system
  * As a user, I want to enter my own recipe names
  * As a user, I want to be able to see any recipes I have added
  * As a user, I want to see the details of each individual recipe when I choose
  * As a user, I want to to have an easy to use program
  * As a user, I want to be updated with confirmations and proof the recipe addition has worked
  * As a user, I want to remain up to date and edit recipes where I want
  * As a user, I want my recipes stored online 

### Flowchart

The Recipe eBook script generates a complex flowchart to visually represent the intricate logic involved. 
Due to the complexity of the code, a single flowchart has been used to show the fundamental process of the Add Recipe selection.
I wasn’t able to capture the true flow of the code within the flow chart well enough as the code consists of a lot of choices and options the user is able to navigate through to create their recipe. 
![flowchart](https://github.com/meganw22/project-three/assets/141934888/f854fc3e-1b36-43e2-ad30-06d1f3cdfece)

### Colorama
Due to the nature of working within a terminal, the user experience is somewhat lacking. I have imported Colorama into the code to brighten up sentences with bursts of colour and allow the user to more clearly differentiate between questions, input and comments.

## Features

### Main Menu 
The main menu gives the user the option of selecting 1 of 6 options. 
 These options allow the user to dive deeper into the code and will assist them in creating and amending a Recipe eBook

 ![deployed-main-menu](https://github.com/meganw22/project-three/assets/141934888/eb7c622e-1da8-4dcd-be1a-5d39100f5669) 

### Add recipe
The add recipe function allows the user to:
* generate a unique recipe name
* add number of servings of that recipe
* add individual ingredients to the recipe
When the prompts are followed correctly the user will roll through the program and add recipes to the storage location on google sheets. If, however, the user makes mistakes, they can be easily rectified as the recipe prompts and loops back through the code to ensure the user has the correct information entered.
![add-recipe](https://github.com/meganw22/project-three/assets/141934888/ba1cec46-4606-4d67-bb4a-6916a638bdb3)

### Update Recipe
Users can select this option to amend past recipes and update them to adhere to new requirements they may have or recipes they’ve discovered.
This section of Updating code was particularly complex and I spent a substantial amount of time focusing on this section and fault finding to ensure the user options were correctly displayed.
![update-recipe](https://github.com/meganw22/project-three/assets/141934888/0972d68b-3b4b-4071-ae89-352864e65b13)


### Delete Recipe
Users can select this option to amend past recipes that they no longer use. The delete function ensures the user is prompted and informed that once the recipe is deleted it is not restorable.

![delete-recipe](https://github.com/meganw22/project-three/assets/141934888/b2c755a1-8ac3-485a-ab71-b4f1432d5c2a)

### View Recipes
Recipes can be viewed in two methods:
* Individual recipes called by the user to display the entire recipe, Name, Servings and Ingredients.
![view-specific](https://github.com/meganw22/project-three/assets/141934888/bc984c24-0795-48ce-a6eb-e954360fe7cb)

*	The recipe database, also called the Vault, can call every stored recipe to the terminal to show the user the exact recipes available. This will benefit them if they have forgotten a recipe name or just need some inspiration.
![view-all-recipes](https://github.com/meganw22/project-three/assets/141934888/3aa04b3c-ab7f-45cb-8f58-1d1c58e34d49)

### Exit
When user selects option 6, the program is terminated.
![exiting](https://github.com/meganw22/project-three/assets/141934888/4f0c1282-e433-46ba-8796-a5b8180f2052) 

### Technologies Used
* GitHub – to store my projects code and add, commit and push changes
* GitPod – use of GitPod terminal for creating python code and testing
* Python – my program was written in python
* Google Sheets – used as storage areas for data created by python code
* Google Cloud – used to link APIs between google sheets and gitpod.
* Heroku – deployment platform used to show the user terminal
* CI Python Linter – (https://pep8ci.herokuapp.com/ )
* Lucid Flowcharts – (https://lucid.app/ )
* Table to Markdown Converter (https://tabletomarkdown.com/convert-spreadsheet-to-markdown/)

### Future Features
During development, I had the idea to add an additional feature of ‘Weekly Meal Plans’. The code would be extended to ask the user for the type of meal input, for example, breakfast, lunch, or dinner. 
The user could choose how many days they would like to plan their meals for, and the program would generate a shuffled list of meals for the user. This method helps with user experience as it would help to remove the daily/weekly chore of planning meals!

# Deployment
This project was deployed through Heroku as provided by Code Institute. By following the step below, I was able to deploy the terminal to Heroku:
* Created an account with Heroku
* Created a new App through Heroku dashboard and selected appropriate region to me.
* Within settings added backpacks, Python and Node.js 
* Linked Heroku account to GitHub account respository
* Set to Automatic deploys
* Select ‘view’
* Return to GitPod and deploy automatically using git add, commit and push methods.

# Validation
## Python Linter
Python Linter by CI has returned with no errors

![clear-python-linter](https://github.com/meganw22/project-three/assets/141934888/95217253-23fc-4737-9cbd-d37160122846)


## TESTING.md 
* follow link to [TESTING.md](TESTING.md) file for all functionality testing

# Bugs
A common bug found in this code, included the prompts not breaking from the loop and returning to the menu. Each function is similar to the last but different at the same time so each function was unique.
Error handling of in view_specific_recipe function used a broad Exception to catch all errors. This actually didn’t catch everything because this function is generally used for more specific errors and ultimately I ended up swapping out the try/except statements for if/elif/else.
Indenting and formatting was a small issue as it was easily rectified by the use of the terminal error codes and Python Linter.

# Credits
## Acknowledgements:
* Credit and thanks to my mentor, Luke.
* Additional mentor credit for this Project Portfolio while my Mentor Luke was away on holiday, to Graeme and Juliia

## Code:
* Credit due to numerous websites and youtubers who helped me through a mass of understanding and applying code correctly.
* Python code visualiser for walking me through my own code in times of fault finding
* Pep8 for helping me to properly align my code format correctly.

## Content:
Props to me for being lazy enough with creating meal plans each week that I generated this idea to help me in the future!


Description
We need to make a flashcard Displaying Web- App,which will work on basis of
memorization of user. User after login will be able to add no. of decks of his choice and
multiple cards along with required ques and ans, after starting any of the decks,he will also 
review the question level which he felt and accordingly score will be given to him after 
completion of deck and last run time of deck will also be stored 

Technologies used

• HTML for making the templates of the displayed pages along with jinja templates for editing the 
HTML codes
• CSS,Bootstrap for styling the HTML pages
• Javascript for applying conditions by using functions on codes
• Python for writing and implementing different functions of code
• Sqlalchemy for making, storing and editing databases inside python code for the main function 
of code
• Flask for implementing different parts insde the web application including 
render_template,request,redirect
• Datetime module for storing latest date and time 
 


Then I have called the Flask module for functioning of web-app features and SqlAlchemy for 
database and name it as database1.sqlite3.I wrote then 3 different classes that were User.Decks and 
Cards that were added in database.
Then I made different app.route controllers for calling different pages that were connected to the 
user like the decks that are added by the user ,the cards that are added inside the deck
,I included controllers for logging inside the user, adding, removing, updating a deck ,also 
controllers for adding, removing, updating the cards and controllers to start reviewing a deck. All 
these controllers have a connected html file via render _template method to call those particular 
pages for display
Additionally, I have used CSS to implement a flipping techniques for each cards that comes for 
review nd also for each deck that flips and shows latest time and score and each card also on 
flipping shows ques and ans respectively

# Folder Structure

- `database1.sqlite3` is the sqlite DB. It can be anywhere on the machine. Adjust the path in `app.py`. This app ships with one required for testing.
- `main.py` is where our application code is
- `static` - default `static` files folder. It serves at '/static' path and contians reuried images
- `templates` - Default flask templates folder ,it contains all html file wihch willl be displayed when redirected as render_template from the controllers 


```
Flashcard/

/
├── .upm/
│   └── store.json
├── database1.sqlite3
├── main.py
├── poetry.lock
├── pyproject.toml
├── readme.md
├── static/
│   ├── background.jpg
│   └── img_final.png
├── templates/
│   ├── add_card.html
│   ├── add_deck.html
│   ├── dashboard_Sample.html
│   ├── deck_dashboard_sample.html
│   ├── DISPLAY PAGE.html
│   ├── login_page.html
│   ├── New_User.html
│   ├── start.html
│   ├── update_Card.html
│   ├── update_deck.html
│   └── user.html

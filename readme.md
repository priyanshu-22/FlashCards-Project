for running on replit just  upload  on replit the unzip folder here,and paste the code inside main.py in the replit main.py ile  and click on run button and go to displayed link in console to run it,ensure that  all static ,tempaltes and code is present as different files inside replit,and the main.py  code of  the zipped folder should be exactly copied inside main.py of replit  where it needs to be run

use the username-'priyanshu singh'
and password-'singh'
 to log in to a already made dashboard with decks and cards
 or click on new user to make a new blank dashboard with new user

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
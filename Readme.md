##Question 2

For running the program, you need to use python 2.7 and you need to install the package `psycopg2`. You can install by running 'sudo pip install psycopg2'.
Our program is composed of two files: `pygui.py` and `modules.py`. The `modules.py` contains some functions making database queries, which are invoked by `pygui.py`. To run the program, you need to:
```
extract project-3.zip
cd project-3
python pygui.py
```

```
In the main menu, we have 8 options:
- Option 1: Add a new player to Database
- Option 2: Get the player with most gold medals in a selected country
- Option 3: Get the female player with most gold medals in country winning the most gold medals
- Option 4: Update the number of gold, silver and bronze medals for each player
- Option 5: Update the number of gold, silver and bronze medals for each country
- Option 6: Find all players who got gold medals in a given \'category\' in a match
- Option 7: Add a new participation record
- Option 8: Quit
```

`Note that we can quit at any time during the program.`

Options 1, 4, 5 and 7 are about data modification while options 2, 3, 6 returns query information. 

For each of the option, input correspoding information given the options in the listbox or the format guidence. If an operation can not be done due to system problem or violets database constraints, you will get an error message. At any point you may refresh the current page, go back to the main menu or quit. 



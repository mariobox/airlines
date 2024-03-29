# airlines

Type the name or part of the name of an airline in the form, and get a list or airline names that match your entry followed by their 2-charachter IATA symbol. For example, you can type 'american' in the search box:

<img src="https://mariobox.github.io/airlines/iata-search.jpg">

And when you click "Submit" the result will be a list of all the airlines that have "american" in their name, followed by their IATA symbol in parentheses:

<img src="https://mariobox.github.io/airlines/iata-results.jpg">

The program is made in Python, with the aid of Flask and Jinja to display it on a web page.

First, the program takes a JSON file with all airline/symbol combinations and transforms it into a list of tuples. Each tuple is in the form of ('Symbol', 'Airline Name').

Next, we iterate among all tuples in the list and append to a new list those tuples where the airline name matches the pattern you input.

Finally, we print the list of results on a webpage, using Flask and a Jinja template. 

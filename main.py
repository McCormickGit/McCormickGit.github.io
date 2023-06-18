# Build a dictionary containing the specified movie collection
#dictionary is sorted with the year being the key
#and [Title, Director] being the value 
movies = {
  '2005': [['Munich', 'Steven Spielberg']], 
  '2006': [['The Prestige', 'Christopher Nolan'], ['The Departed', 'Martin Scorsese']],
  '2007': [['Into the Wild', 'Sean Penn']],
  '2008': [['The Dark Knight', 'Christopher Nolan']],
  '2009': [['Mary and Max', 'Adam Elliot']],
  '2010': [['The King\'s Speech', 'Tom Hooper']],
  '2011': [['The Artist', 'Michel Hazanavicius'], ['The Help', 'Tate Taylor']],
  '2012': [['Argo', 'Ben Affleck']],
  '2013': [['12 Years a Slave', 'Steve McQueen']],
  '2014': [['Birdman', 'Alejandro G. Inarritu']],
  '2015': [['Spotlight', 'Tom McCarthy']],
  '2016': [['The BFG', 'Steven Spielberg']]
}

# Prompt the user for a year 

User_year = input('Enter a year between 2005 and 2016:\n')

# Displaying the title(s) and directors(s) from that year
if User_year in movies: #checks to see if the input is in the dictionary
  for title,director in movies.get(User_year): #attaches the values of the year to the variables
    print(title + ', ' + director) #outputs the title and director
else: #used when the input isn't in the dictionary
  print('N/A') #outputs N/a

#sets up the menu
menu ='MENU'\
      '\nSort by:'\
      '\ny - Year'\
      '\nd - Director'\
      '\nt - Movie title'\
      '\nq - Quit\n'

Prompt_user = True #while the value is true the loop executes
while Prompt_user:
  print('\n' + menu) #prints the menu
  m = input('Choose an option:\n') #takes the menu input and executes the appropriate loop
  if m == 'q': #exits the loop
    Prompt_user = False #quits the script

#sort by year
#fivalueme: 2006/2011 output is a little off///rest is good
  elif m == 'y': #if user input is 'y' then this loop starts
    for year, values in sorted(movies.items()): #pulls the key, value pairs from the list
      print(year + ':') # outputs the year
      for value in values: #nested for loop to get the information under one header
        title, director = value #output formating for next line
        print('\t%s, %s' % (title, director)) #formated with values from year


#sort by director, director is value[1] in the movies dict
  elif m == 'd': #if the user input is 'd' then this loop starts
    Temp_store = {} #temp/empty dictionary to store 
    for year, values in sorted(movies.items()): #pulls the key, value pairs from the list
      for value in values:#defines the iterable
        title, director = value #assigns the variables to value
        if director not in Temp_store:#checks to see if the director has already been iterated over
          Temp_store[director] = [] #stores the director
        Temp_store[director].append([title, year]) #add the variable to the stored director
    for director, values in sorted(Temp_store.items()): #checks to see if it's in temp dic
      print(director + ':') #prints the director header
      for value in values: #defines the iterable
        title, year = value #output formating for the next line
        print('\t%s, %s' % (title, year)) #formated with values from value
        print('') #prints a blank line after each iteration

#sort by title, director is value[0]
  elif m == 't':
    Temp_store = {} #temp/empty dictionary to store
    for year, values in sorted(movies.items()): #pulls the key, value pairs from the list
      for value in values: #defines the iterable
        title, director = value #assigns the variables to value
        if title not in Temp_store: #checks to ensure the title has already been iterated over
          Temp_store[title] = [] #stores the title
        Temp_store[title].append([director, year]) #adds the variables to the stored title
    for title, values in sorted(Temp_store.items()):#checks to see if it's in temp dic
      print(title + ':') #prints the title header
      for value in values: #defines the iterable
        director, year = value#output formating for the next line
        print('\t%s, %s' % (director, year))#formated with values from value
        print('')#prints a blank line after each iteration

  
  
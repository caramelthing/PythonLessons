#first little program :) page 92 in automate the boring stuff
#can see below i import module called random. further down i call that module and run .randint method on it. in future i can define my own functions to a module and import that mother fuck and pull my def methods out.

import random
messages = ['It is certain',    'It is decidedly so',    'Yes definitely',    'Reply hazy try again',    'Ask again later',    'Concentrate and ask again',    'My reply is no',    'Outlook not so good',    'Very doubtful']

print(messages[random.randint(0, len(messages) -1)])

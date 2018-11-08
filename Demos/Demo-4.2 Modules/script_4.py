# import a module that imports another module 
# nested 

import nested
nested.greetit('Harry')

# and a more detailed look
help(nested)

#look inside the 2nd module 
help(nested.myprinter)

nested.myprinter.printit("Hello Everybody" )
#Also use [TAB].[Completion]

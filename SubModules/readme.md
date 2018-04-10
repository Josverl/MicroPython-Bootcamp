# Git Tools - Submodules
https://git-scm.com/book/en/v2/Git-Tools-Submodules


Adding another Sub Module
-------------------------
	git submodule add https://github.com/tuupola/micropython-m5stack.git


Initialising Submodules
-----------------------
You must run two commands:

	git submodule init
	git submodule update

1. to initialize your local configuration file,  
2. and to fetch all the data from that project and check out the appropriate commit listed in your superproject:

Submodules
----------
It often happens that while working on one project, you need to use another project from within it. 
Perhaps it's a library that a third party developed or that you're developing separately and using in multiple parent projects.
A common issue arises in these scenarios: you want to be able to treat the two projects as separate yet still be able to use
one from within the other.



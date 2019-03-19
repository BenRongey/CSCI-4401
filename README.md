# CSCI-4401
University of New Orleans
Operating Systems

- <h2>Assignment 1</h2>
  Assignment 1 has a few tasks, using bash scripts, Python, C programming language, and graphviz, a Python graphing library:
    <h3>Task1</h3>
      Task 1 uses a single-line bash script to display a colorful animal in the terminal.  This works with:
       
       - lolcat
       - cowsay
       - jq (https://stedolan.github.io/jq/)
       - curl
       - Chuck Norris joke API (http://www.icndb.com/api/)
       
   <h3>Task2</h3>
      Task 2 uses C programming language to recursively fork n number of times based on input given.  This fork output is piped to a csv file.  Use the command to compile and run the C program:
      
      cc question2.c
     This will create an a.out program.  Run this program with the following command:
     
      ./a.out
     Next you can use the tree_builder script to create a graphical tree (via the graphviz library).  Use this command:
     
      python tree_builder.py
      
    <h3>Task3</h3>
        Task 3 is just a variation of task 2 that changes the structure of the tree.  This uses nearly the same code as task 2, but make sure that the parent waits for the child to die soon after the fork and then breaks from the loop and exits.  The functionality is the same as task 2, but instead of running the question2.c, use the following command:
        
        cc question3.c

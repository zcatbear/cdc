# Learning how to navigate bash terminal.
Welcome to the wonderful world of BASH (bourne again shell). You are about to embark on a journey that will probably come in handy at some point in your career. Whether you choose a desktop that is of the Linux variant, run a raspberry pi, or get a MAC. This will allow you to be much more productive.  

## Open up the terminal
If you didn't get the minimal install of your distro (if you did this in class you should have CentOS) then open up a terminal. Find it either by clicking around or pressing the windows key and typing terminal.

## Explanation of this sheet
When there is text highlighted like `this` it is mean to be a single command and you should check what the output is.

```
Block quotes
look like this
they are a series
of commands 
```

## Exploring the Terminal
#### Finding out where you are  
When you first enter the terminal you are in your home direcory.  
`pwd`  
This will print out the absolute path to your home directory  
`cd /`  

#### Redirecting your output  
This puts you into the *root* directory, which is the base of the file tree in linux.  
To get back to your home directory either type `cd` or `cd ~` The ~ is code for the home directory  
`echo "This is the first line" >> textfile.txt`  
`cat textfile.txt`  
You should now see that the line you typed out after echo is in textfile.txt
`echo "this is the second line" >> textfile.txt`  
`cat textfile.txt`  
You should now see that both of the lines are in there. That's because of the text redirection  
`echo "This is the third line" > textfile.txt`  
`cat textfile.txt`  
This is the difference between the single and the double redirect.  

You can redirect anything into a text file.
`ls -lah / >> rootls.txt`  
`cat rootls.txt`  

#### Text Editing
Next you should actually try creating and managing your own file. To do this we have several options.
- vi
- nano (might be included by default)
- vim (vi _improved_)

Vi is ridiculous and overly complex.  
Nano is reserved for people who put milk in the bowl before cereal and drink orange juice after brushing their teeth.  
Install vim  
`sudo yum install vim` I haven't explained what sudo is yet. Essentially you are saying "run this command as an admin user"  
Now create a file called "yourname.py"  
`vim yourname.py`
It will drop you into a text editor. To begin editing you should simply type `a` or `i` and copy pasta this  
```
#!/usr/bin/python
import sys  

if (len(sys.argv) > 1):  
  print("Hello " + str(sys.argv[1]) + "!")  
else:  
  print("Hello User!")  
```
This is a python file and you can run it by simply running  
`python yourname.py`  
It should print out "Hello User!"  

It is a bit verbose to have to specify python to run each file though.
`chmod +x yourname.py`  
This will make the program executable  
`./yourname.py yourname`  
Also if you haven't tried it by now, pressing tab when you are a portion of the way through a word will autocomplete it for you. Very nice.  

#### Creating directories/Folders  
It's nice if you want to just put all of your files in your home directory but you need to sometimes throw stuff into folders (in linux they are called directories)  
`mkdir yournameFolder`  
This will create another directory for you to put stuff in  
`ls -lah`  
You should be able to see all of the files and directories that you have created.   
`cd yournameFolder`  
This gets you in that directory  
`echo "Another file" >> newFile.txt`  
`ls -lah`  
Now you can see that you have stashed another file in the directory  

Now to take it full circle.  
`pwd`  
You'll see that you are one directory further than your home directory.  
To get you to back to your home directory you can type `cd`, `cd ~`  
Since you are just below the home directory you can say `cd ..`
This means "cd up one directory"  

## That's all folks
I don't want to overwhelm you with too much information right now. If you want to learn some more check out the resources [here](http://overthewire.org/wargames/)  
They phrase learning and navigating a linux terminal as fun games.  I highly recommend it. They teach you how to do some awesome stuff.

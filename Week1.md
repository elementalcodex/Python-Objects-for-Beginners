# Week 1
## Github clone
## Colab Basics
Why so popular?

Markdown text cells and formatting.

Code cells and the play button.

Adding cells using +.

## What are objects?
Nothing magical, just easier to understand.  We think about the world in terms of objects.

Anything can be an object and that's part of the appeal.  Anything you want in a computer program can be modeled as an object.

We can do things to objects and we can get objects to do things we want.  How they do those things is only a concern to the person that invented the object type.

For example: if we have a dog object we can put it in the car, we can give it a bath.  We can tell it to sit or give it food but what happens to the food after it 
is eaten or how the brain tells the dog's body to sit is only matters to the specialists (vet, biologist).  These boundaries make working with computer programs much easier when we think of the pieces as separate objects.

Python is great language to learn about objects because everything in Python is an object.

So let's create our first object and run the program.  Let's make the number 3 object.  Every object in Python has a type of object, called a class, and a value.  To help us explore objects in Python we have a couple of commands that are very handy.  These commands are dir, type, and print.
## 'dir', 'type', 'print',
Not surprisingly these commands are also objects.  Objects that are commands, meaning that they can run code and do things, are called functions.  We'll talk more about this later but for now just know that in order to issue a command we just put parenthesis after the name of the function object.  If we need to give the function more instructions, we put those inside the parenthesis.  

Let's find out the type for the object 3.  Type type(3) and press play.  So we can see that the number 3 is an int which stands for integer and just means whole number.  

Let's see all the things we can do with the number 3.  Type dir(3) and press play.  Wow!  That's a lot!  Luckily we don't need to know all that.  The underscores mean private and basically means this stuff is happening inside the dog or under the hood of the car.  So if we look at some of these names we see that they sound familiar: add, multiply, divide, etc.  This is where the  code is that says what happens when we add two numbers together.  We can change this code but then it  would break math.  But later when we define our own types of objectc we can define what happens when they are added together.  So if we add two players together we can get a team.  Enough for integers right now.  That will be our topic for next class.

## exploring builtins, 
There is an object called \_\_builtins\_\_ and it contains all of the object types  that Python knows at the beginning of a session.  Let's use dir to figure out what these are.  Type dir(\_\_builtins\_\_) and press play.  There are many objects that are realted to errors and they are there to make the programming experience easier.  We don't need to worry about  those.  If we scroll down we find some more objects with underscores.  These are the private objects so we can leave those alone.  Finally we have the lower case objects and those are going to be the building blocks for our programs.  You will recognize many of these from our syllabus.  We won't cover them all but we will look at many.   

## help, internet W3 Schools, 
One of the objects you will see is called help.  You can use help to learn more about other objects.  Type help(print) and press play.  You can also go on the internet and type 'python print' and go the W3 Schools which is an excellent resource.  There you find a more complete and friendlier explanation with code that you can run to test.

## Homework:
Choose 3 to 5 objects from \_\_builtins\_\_ and use the help function to learn about them.  Then go to the internet and do the same thing for W3Schools.  If you want you can do this for all Python Objects but you'll be 100 years old before you're done.

Finally, if you don't like typing you can use aliases to give your objects shorter names.  That is what the equal sign is for.  It just things objects names.  Let's rename print, type, and dir as p, t, and d and let's test that they work.  This is optional and though it decreases typing, it makes it harder to read.  It is up to you!

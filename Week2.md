# Week 2
## Review and Homework
### Github clone
### Colab Basics
Each code cell has its own play button so we can run different sections of code separately.

### What are objects anyway?
Everything in Python is an object.  Objects are helpful because we think about the world in terms of objects so if we think of our computer program in terms of objects it it will be easier to understand.  We will start to develop an intuition about where the code should go and how different parts will interact.

We looked at the dog object last time and we talked about how we can put the dog in the  car, we can give the dog a bath.  We can also interact with the dog and get it to do things like sit, eat, jump, sleep (maybe).  We interact with the dogs interface which is basically its facial expressions, its eyes, sense of smell, touching etc.  But we don't really pay much attention to what is going on inside the dog unless there is a problem (or you are a vet).

All the objects in Python programming follow this same idea.  We interact with the objects through the things that they can do and we don't worry about what is behind the scenes.  

There are basically two types of objects in Python: variables and functions.  The difference between them is that you can put parenthesis after functions and make them execute a command.  We can put things inside the parenthesis if we want to give more information to the program about the command.

Some of the most useful functions for exploring objects are type, dir, print, and help.  We can pass the object to any of these functions to learn more about them.  

__type__ gives us the kind of object it is.  This is called the object's class.  In the last class we ran type(spot) and we got dog.  Every object has a type and that is to say every object belongs to a class.

__dir__ gives us all of the objects attributes.  These are the  things it does and how we interact with the object.  To have the object do something we put a period after its name and then the name of the method.  If this method is a function, which it should be, we put parenthesis after it to make it execute.

__print__ gives us different things depending on what the person that created that type of object wants it to show.  In general people choose to make it print the value of the object.  For class dog, I'm going to make it print an update on how the dog is feeling in terms of happiness and health and energy.

__help__ gives us some information about the object and how to use it.  This is usually a bit difficult to understand but it is good to know.

Let's practice these with a dog object. We need to import Dog because it isn't part of __\_\_builtins\_\___ but let's do that because it is a more colorful example. First let's come up with a name.  If we don't our object will be destroyed right after we make it.  How about dexter?  We use the equal sign to name the object we
are making with the dog constructor.

Ok, now let's pass dexter to each of these four functions.  We can see that Dexter is a dog.Dog, meaning it is a Dog object defined in a file called Dog.  You can see it here if you feel adventurous.  You probably won't understand much there but don't worry about it.  

We can print Dexter and see what happens.  We can't really ever know what is going to happen because it is up to the person who invented the dog type to define that.  In this case I decided to show the Dog's happiness, energy, and health.  I made it so it would be kind of like a report on the dog's state.

We can use the help function to get some information but we can use the question mark after it to get a simpler, more to the point help.  I recommend this.

Finally can use dir to show all the things that Dexter can do.  We see the dunder methods and those methods are not meant to be used for the most part.  Those matter most to the person that invented the dog type of object.  We care about the other attributes because those are the ones we use to interact with the dog.  Those are the dogs senses  we can say or how we interact with the dog.  There are some new ones such as energy, health, and happiness (I know these are on the inside really but in our game we can observe them).  These new attributes and not functions.  They don't really do antying, they are kind of like a score.  So we can't put parenthesis around them and have them run code.  We can only look at the values.  We look at these by using the period and then the name of the attribute.  We can  also see what type they are.  When we do that we see that the type is int which stands for integer.  An integer is just a whole number.











Nothing magical, just easier to understand.  We think about the world in terms of objects.
Anything can be an object and that's part of the appeal.  Anything you want in a computer program can be modeled as an object.

We can do things to objects and we can get objects to do things we want.  How they do those things is only a concern to the person that invented the object type.

For example: if we have a dog object we can put it in the car, we can give it a bath.  We can tell it to sit or give it food but what happens to the food after it 
is eaten or how the brain tells the dog's body to sit is only matters to the specialists (vet, biologist).  These boundaries make working with computer programs much easier when we think of the pieces as separate objects.

Python is great language to learn about objects because everything in Python is an object.

So let's create our first object and run the program.  Let's make the number 3 object.  Every object in Python has a type of object, called a class, and a value.  To help us explore objects in Python we have a couple of commands that are very handy.  These commands are dir, type, print, and help.
## 'dir', 'type', 'print', 'help'
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

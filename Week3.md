# Week 3
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


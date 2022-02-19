# An Introduction to Pygame
Pygame is a set of Python modules designed for writing video games. Consisting of free and open-source libraries for computer graphics and sound, it is easy to use and implement. 

## Why learn Pygame?
Pygame is a great introduction to writing video games in high-level programming languages, regardless of prior programming experience. It is an extension of Python, which as you can see in [TIOBE's top 20 languages](https://www.tiobe.com/tiobe-index/), is the third most used programming language worldwide and is becoming continuously more popular (as shown in the graph below). Hence, the Python skills you develop whilst learning Pygame are transferrable to the professional industry. For programming beginners, Python basics can be picked up quickly and the transition into Pygame is smooth. 

![Rating graph](LearnerGuideResources/graph.png)

Pygame's wide range of functions not only simplify video game development but also provide the programmer with the tools they need to implement the majority of the functionalities they would want to include in a simple video game. 

Additionally, Pygame is open source, meaning that its source code is freely available to any user to add, change sections and redistribute. This means that bugs are easily fixed by the community and new functions are continuously added as programmers improve Pygame to suit their needs.

## Getting started... 
### Installation
We will need Python, Pygame and an integrated development environment (IDE) to write our code. 

If you don't already have Python, start by downloading it from [its website](https://www.python.org/downloads/). An IDE (called IDLE) will also be downloaded, which is a great IDE for coding beginners. MacOS users have Python built into their operating systems, and Xcode as an IDE. The IDE which you use isn't too important, as long as you can run your code. 

You also need to install Pygame. You can do this by using the [command line instructions here](https://www.pygame.org/wiki/GettingStarted), to install using your OS's command-line interface (this was my preferred method) or download from [the website](http://www.pygame.org/download.shtml).

### Learning Python 
Before you start with Pygame, you should have a basic understanding of Python. I recommend understanding variables and data types, conditional statements, iteration, functions and some basic operators. 

If you want some help, these resources are useful:
- [Learnpython.org](https://www.learnpython.org/)
- [Learn Python online](http://www.trytoprogram.com/python-programming/)
- [CodersLegacy Python basics](https://coderslegacy.com/python/learning-the-basics/)

Most of these resources have a lot of information, just stick to the basics and you'll be absolutely fine!

### Learning Pygame
I found the best way to get started was to follow an online tutorial. This enables you to familiarise yourself with the structure and commands used in Pygame before you start from scratch. 

There aren't many full game tutorials available online, but here are a few:
- [Bunnies and Badgers](https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python)
- [Car game](https://coderslegacy.com/python/python-pygame-tutorial/)
- [Snake game](https://www.youtube.com/watch?v=h5chKlZRTCg)

## Learning materials
I have chosen six elements that I think are important when starting to write a video game in Pygame. You can see the entire list of Pygame functions [here](https://www.pygame.org/docs/genindex.html) but I am just going to focus on a few!

###  Structure
I overlooked the structure entirely when I first started, which resulted in issues that I couldn't resolve until I understood how Pygame worked. Pygame works by continuously iterating through a game loop, which updates the screen throughout the game. All events which occur in the game are written within the loop and anything else should occur before the loop starts. This is because once the game loop is introduced, anything inside is performed over and over until something happens to end the game. Hence, anything that you only want to happen once, such as variable or window initialisation, media or library importation and function declaration, should occur outside of this loop. I found this was important to understand for an efficient game.

Here is an example of a Pygame file that uses this structure. 

![Structure example](LearnerGuideResources/structure.png)

### Importing Pygame
The first thing we do is [import the Pygame module](https://www.pygame.org/docs/tut/ImportInit.html). Without importing, we won't be able to use any Pygame functions and we will just end up with errors. All we need to do is add two lines at the top of our code:

![Importing Pygame](LearnerGuideResources/importingPygame.png)

The first line imports everything in the Pygame module. The second line imports the pygame.locals module which contains all constants used by Pygame, such as images, events and the display. Without this module, it is difficult to manipulate these constants within our code. At this point, we can also import any other Python modules, which we may want to use. 

### Initialising the game
Next, we initialise the game and display window. Again, this is simple and only takes a few lines of code:

![Initialise window](LearnerGuideResources/initialiseWindow.png)

To use the functions, we must initialise Pygame, using [pygame.init()](https://www.pygame.org/docs/ref/pygame.html#pygame.init). Then we initialise the display window, with declared width and height, using the [pygame.display.set_mode((width,height))](https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode) function. We assign the window to a variable 'screen' to use later on. 

### Importing and using media
Now we will look at including media. I'll just be focusing on images but Pygame also allows sound effects. If you want to add sound, check out these links!

- [GeeksforGeeks](https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/)
- [PythonProgramming](https://pythonprogramming.net/adding-sounds-music-pygame/)

With any media, we need to import it before we can use it in our game. We only need each piece of media to be loaded once, as we can then use it as much as we want. Hence, thinking about the structure, all media should be loaded before the game loop starts so that we don't slow down our game and cause inefficiency. 

![Importing media](LearnerGuideResources/importingMedia.png)

To import images use the [pygame.image.load()](https://www.pygame.org/docs/ref/image.html#pygame.image.load) function to load the image, and then save that loaded image to a variable for later use. Inside the function, we pass the image's file path as a parameter. You can see from my code above that my cow image is saved in the same location as my code, but my giraffe image is in another folder, 'Images'. 

Once loaded, we can add the images to the screen. 

![Adding images](LearnerGuideResources/addImages.png)

To add an image to the display I used the command [screen.blit(image,[xCoordinate,yCoordinate])](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit), which adds the image stored in the 'image' variable to the screen with its top-left corner at the coordinate [xCoordinate,yCoordinate]. 

Whenever we change the display we must also tell Pygame to update the screen using [pygame.display.flip()](https://www.pygame.org/docs/ref/display.html#pygame.display.flip).

### User interaction
User interaction is handled using [events](https://www.pygame.org/docs/ref/event.html#module-pygame.event). We can use the [pygame.event.get()](https://www.pygame.org/docs/ref/event.html#pygame.event.get) function to allow the user to interact, and then we program what should happen at each type of event. The best way to learn how to handle user interaction is to explore the [pygame event docs](https://www.pygame.org/docs/ref/event.html#module-pygame.event) and discover the different event types. Below is an example of handling the user pressing close, or the arrow keys to move an image.
 
Note: this all occurs within the game loop.

![User interaction](LearnerGuideResources/userInteraction.png)

### Collisions
The final thing which is important to know how to do when writing a video game is collision handling. We need to draw rectangles around each of our objects and then use the [.collideRect()](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect) function, which detects for collisions between rectangles.

Note: this occurs within the game loop.

![Collisions](LearnerGuideResources/collisions.png)

We can see above that I used two functions, [pygame.Rect()](https://www.pygame.org/docs/ref/rect.html#pygame.Rect) and image.get_rect(topleft=(x,y)) in order to obtain the rectangles, and assigned each to a variable. Image.get_rect(topleft=(x,y)) draws a rectangle with the dimensions of 'image' on the screen at coordinate (x,y). Then, [pygame.Rect()](https://www.pygame.org/docs/ref/rect.html#pygame.Rect) gets the rectangular coordinates of the parameter passed through. With our rectangles stored in variable1 and variable2, we use [variable1.collideRect(variable2)](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect), to determine if they are colliding. 

### My Code
These things are important in writing a video game using Pygame. Here is what my very basic code now looks like. It allows the user to move the cow around the screen, and if the cow hits the giraffe, the game will end. 

![Full game](LearnerGuideResources/fullGame.png)

## Evaluation
From my experience as a Pygame beginner, I found it a useful introduction to video game programming. The library of functions is generally easy to understand and implement, making the process enjoyable and rewarding, as the programmer watches their game come together. As with any coding process, there are points where you are stumped for what to do, but as your familiarity with Pygame grows, so does your confidence making the more challenging functions more accessible. 

However, it has its limitations. Some functions which you would expect to be there, such as handling text input, aren't directly included in the library, and so you have to combine other functions to create something which you would expect to be quite basic. In the process of doing this, the code adds up and the efficiency reduces quickly. Additionally, for more advanced games which require lots of graphical updates per cycle, Pygame is not ideal as it becomes slow to run reducing the quality of the user's experience. 

That being said, for basic arcade-style games, Pygame is a great place to start. Furthermore, with Pygame being an extension of Python, and Python being one of the most used languages by professionals, Pygame is a fun and useful way to further your knowledge and confidence in such a popular language.
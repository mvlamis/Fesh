## Fesh
*By Michael Vlamis for ICS2O*


## **Summary**

_Fesh_ is a pixel-style fishing game where the player can sell fish in exchange for more fishing gear.


## Idea

The player is placed in a campground with no equipment. They will come across a house with an NPC who gives them a fishing rod, and they are now able to go to the water and catch fish. There is a shopkeeper buying fish at varying prices and selling equipment for the player. Each NPC is able to communicate to the player with their respective tones and personalities. For example, the shopkeeper speaks in an abrupt and brash manner to the player, while another NPC is more friendly. Visuals are in 16-bit style with low-framerate animations, and multiple sprites are added for different types of fish and equipment.


## Behind the scenes

The game are programmed entirely in Python using the PyGame library. This is in order to make it easily cross-compatible between Mac, which I use to develop, and Windows, which the game is tested on. It also allows for simplified integration with other environments, such as web browsers and software distributors. 

Maps are designed using a free map editor called Tiled, and game assets are sourced from [Kenney on itch.io](https://kenney.itch.io). Additional pixel art can be drawn using an online tool called [Piskel](https://www.piskelapp.com). 

For the fishing mechanic, both the level of success and choice of fish are randomized. An inventory list will keep track of the items and equipment that a player holds at once, and requires strategic planning to stay under the item limit. 

**Controls**
|Action|Button  |
|--|--|
|Movement|`WASD` or arrow keys  |
|Catch fish|`f`|
|Start fishing|`space`|
|Interact|`space`



**Known Bugs**
| Problem | Workaround |
|--|--|
| Clicks don't always register |This is both an issue with PyGame and malpractice due to the way PyGame handles click events. Right now the only workaround is to click multiple times until it works.  |
|Fishing doesn't always work|Walk towards the water again. Fishing will only register within 3 seconds of touching water.|
|Choice text extends past screen|To be fixed





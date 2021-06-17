# ISISBot

Python based Dicord bot for ISIS Service TU Berlin

Changelog 15-06 Sven
- Fixed the ID checking for the Reactions
- implemented an on_message-function which automatically deletes user commands to keep the channel clean
- Changed the functions in Filtering to be sent to the user than sent to the channel
- Some editing of the text
- minor bug fixes

Changelog 12-06 Sven
- Added a startup command which automatically triggers the Datenschutz
- Modified the Datenschutz
- Added a check for Reactions in Filtering.py
- Added Reaction based Filterlists creation
  - Still WIP (maybe need to change the ID which it checks)
- Still to do:
  - Check the embed texts in Filtering.py and maybe change them
  - automatically start the listen function if atleast one user accepts the Datenschutz
  - automatically check if still one user accepts the Datenschutz else not listen anymore
  - Small changes to the checking of the reactions in Filtering.py (ID-based stuff)

Changelog 05-06 Sven & Lennart
- Optimized rss.py
- Outsourced the lists and key-value pairs from Filtering.py to access them from ShowForum.py
- Implemented **listen** in ShowForum.py
  - Implemented working blacklist
  - Implemented working keywords
  - Added a Notification for each user who uses the bot

Changelog 03-06 Lennart
- changed forum_output to store key value pairs instead of arrays 
- updated comments in ShowForum

Changelog 31-05 Lennart
- Added ShowForum.py
  - still WIP
  - reads ISIS-Bot Modul Ankündigungs Forum and shows title, author and message in discord server
- adjusted extensions in bot.py with new ShowForum

Changelog 28-05 Sven
- Added an Error handling function in bot.py
- Changed some output in Filtering.py
- Imported cofig.py to rss.py
  - RSS-key can now be stored in config.py

Changelog 26-05 Sven
- Added keywords
- Changed the Show command
- Added aliases for
  - Befehle.py helpme
  - Filtering.py show
- Commenting in Befehle.py and Filtering.py


Changelog 22-05 Sven
- Fixed shutdown in bot.py finally (it just takes a few seconds)
- Fixed Filtering.py:
    - Added Key/Value pairs
    - Error exceptions
    - Case handling
    - Whitelisting and Blacklisting works now.
- Added some comments to the code


Changelog 21-05 Sven
- Fixed shutdown in bot.py
- Added extensions to bot.py
- Added Befehle.py with a helpme function (to show all possible commands later on)
    - This is still WIP (need to add the functions with a short description)
- Added Filtering.py for Black- and Whitelisting
    - This is still WIP and not tested jet (will test on 22-05)
    - Maybe the creation of lists should be changed (discord ids are 18 digits...) maybe with key/value pairs
- Added some comments to the code  

Changelog 17-06 Anna
– Final text for data security modal that shows up after the bot got started


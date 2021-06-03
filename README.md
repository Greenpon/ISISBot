# ISISBot

Python based Dicord bot for ISIS Service TU Berlin

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

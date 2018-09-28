# ERIGRASDE001
## Problem
Write a script to be executed from a command line using either python, ruby, or PowerShell that extracts the text of the last 8 posts made on the Expedia Facebook page, and re-writes such data into a text file using JSON. Be creative on writing the post text and respective date, and justify your decision.
## Approach
### Tools & Technologies
#### Language
I chose to write the solution in python primarily because I'm more familiar with it than the other proposed languages, but also because I know from research and prior experience that webscraping and filesystem interaction is straightforward with the right python packages. For these reasons I knew python would be a sufficient tool for the job.
#### Tools
* Webscraping:
  * urlopen (from urllib.request package): Enabled requesting & retrieving the raw HTML from the [Expedia Facebook posts webpage](https://www.facebook.com/pg/expedia/posts/ "Expedia Facebook posts webpage").
  * BeautifulSoup (from bs4 package): Enabled parsing the retrieved HTML with methods built into BeautifulSoup like *findAll* and *find*. Using this package freed me from manually traversing the DOM and instead focus on simply finding the right "hooks" (via elements and/or class names) to target the relevant information.
* Filesystem interaction:
  * json: The json *dump* method enabled storing of the data structure into JSON format, per the requirements.
  * codecs: The *getwriter* method enabled the stored data to be encoded with utf-8.

### Logic Flow
I organized the logic flow of the script as follows:
1. Open connection to Expedia's Facebook posts page, and request & retrieve the raw HTML. Close the connection once received.
2. Parse the HTML using BeautifulSoup to enable querying specific data in the DOM with BeautifulSoup's built-in methods.
3. Find & store into a variable the first 8 Facebook posts by querying 'div' elements with class name *_1dwg _1w_m _q7o*. Set limit to 8 by referencing a constant variable defined at the top of the script so as to allow easy maintainability going forward in case the desired number of posts changes.
4. Define a new empty list variable *posts_list* whose purpose is to store only the relevant post information from the DOM.
5. Loop through the list variable containing the Facebook posts. With each post, find the following information and store into a dict structure, then append the resulting dict into the *posts_list* list:
    * Post title, by querying 'span' elements with class name *fcg*
    * Post timestamp, by querying 'span' elements with class name *timestampContent*
    * Post text, by querying 'div' elements with class name *_5pbx userContent _3576*
6. Create a text file (or overwrite if one already exists) called *expedia_fb_posts.txt*, and write the *posts_list* data structure into it as JSON.

### Data Structures
Storing the relevant Facebook posts data into a list of dicts (i.e., an array of objects) made the most sense for a couple reasons:
  * Why a list? Given challenge problem #3, I knew I would need to ultimately loop through this data structure on the frontend. Storing as a list would simplify that loop functionality.
  * Why dicts? Each post contains a natural key/value pair: a description and a value (e.g., "timestamp": "Yesterday at 9:00 AM"). A list of lists would have also been possible, but would have been less clear about what information each element represented since the values would need to be stored without related descriptions.

## How to Test
To test this script, make sure you have python3 installed on your machine, then run the following command from the terminal / command line: *python3 expedia_fb_posts.py*

Once the command is processed, verify that a file named *expedia_fb_posts.txt* exists in the same directory as the script, and that it contains 1 list consisting of 8 dicts, and that each dict contains the following key/value pairs:

    {
      "title": "title from Expedia Facebook page"
      "timestamp": "timestamp from Expedia Facebook page"
      "text": "text from Expedia Facebook page"
    }

Verify that the 8 posts are the 8 most recent posts by navigating to the Expedia Facebook posts page and comparing the order & content of posts in the file with the order & content of posts on the webpage.

Once all of the above is verified, execute the script again to verify that a duplicate file isn't created, and the script overwrites rather than appends to the file.
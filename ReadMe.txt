This script takes a text file of urls, and adds them to a Deeper Connect device's webfilter Blacklist.
In order for this to work, the file of urls needs to be in the same directory as the script, and each url needs to be on its own line. 
Make sure there are no spaces after the URL as the Deeper Connect device will error out and the script will stop.

Before being able to run this script, you will have to retrieve the Bearer Authentication Token. This token is generated when you log in using your credentials.
I wasn't able to figure out how to get the script to retreive one, so I logged into my Deeper Connect device, and opened the web developer tools, and retreived it by inspecting the headers from one of the GET or POST methods. 
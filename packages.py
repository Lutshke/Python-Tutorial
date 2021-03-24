# now i will show you how to use packages

# a package in python is a extension written by someone else

# we install packages with the pip command inside the console "pip install <package name>"

# we import these with the keyword "import"

# import dhooks
# dhooks is a package for sending discord webhooks

# but if were importing it like this we cant use the webhook part so we need to use
# the "from" keyword

from dhooks import Webhook

# we can now call the Webhook function without actually writing any code

def send(message : str): 
    # this is a function for sending messages with the webhook
    # first we need to define what our webhook is
    webhook = Webhook("https://discord.com/api/webhooks/822675215048900620/uHNbhegR3PBOJYFavCPq1i1UgM7ucfJPTHTC7HPlBl8OOZkmUR7FiSszqPef3RSmpjPt")
    
    # now "webhook"  is a variable which saves all data of our webhook and functions we can do with the webhook (send, delted...)
    webhook.send(content=message) # this sends a message with the content of message which is a requierd argument we need to give the function on execution

# so if we call "send" with the argument "This is a example" the webhook will send it as a message

send("This is a example")
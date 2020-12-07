# Import Libraries
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from sys import exit

# For New Chat (If contact isn't in recents chats)
def new_chat(contact, text):

    # Find and click search box
    search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search.click()

    # Enter Contact name
    search.send_keys(f'{contact}')
    sleep(2)

    # Search for new 'contact' in contact list
    try:
    
        search_contact = driver.find_element_by_xpath(f'//span[@title="{contact}"]')
        sleep(2)
        search_contact.click()

        # Type message in message box
        message = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        message.send_keys(f'{text}')

        # Click on send button, print 'sent'
        send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
        send_button.click()
        print(f"Sent to {contact}")

    # If 'contact' is not found, raise error
    except NoSuchElementException:

        print(f"Contact {contact} not found!")

# Print instructions
print("\nKeep entering contact names you want to send message")
print("Type n/no if you are ready to send message")

# List to store contact names
contact_list = []

# Keep prompting until user exits
while (True):
    
    # Prompt for contact name
    contact = input("Contact name: ")

    # Check if user is ready
    if contact.lower() == "n" or contact.lower() == "no":
        break
    
    # Add names in the list
    contact_list.append(contact)

# If contact list is empty, raise error and exit
if len(contact_list) == 0:
    print("Contact list is empty")
    exit(1)

print("\n")

# Ask for message
text = input("Message: ")

print("\n")

# Object for chrome-driver
driver = webdriver.Chrome()

# Goto 'WhatsApp Web'
driver.get('https://web.whatsapp.com/')

# Wait for QR code to be scanned
sleep(15)

# Keep sending messages to contacts
for i in range(len(contact_list)):

    # Search for contact in recent chats
    try:

        search = driver.find_element_by_xpath(f'//span[@title="{contact_list[i]}"]')
        search.click()

        # Type on message box
        message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        message_box.click()
        message_box.send_keys(f'{text}')

        # Click on send button
        button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
        button.click()
        print(f"Sent to {contact_list[i]}")

    # If 'contact' not found in recent chats
    except NoSuchElementException as se:

        # Call 'new_chat' function
        new_chat(contact_list[i], text)

sleep(3)

driver.close()
print("\nDone")
exit(0)

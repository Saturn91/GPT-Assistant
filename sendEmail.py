import webbrowser

def sendEmail(email, subject, message):
    # Create a mailto: URL with the email address, subject, and message
    mailto_url = f"mailto:{email}?subject={subject}&body={message}"

    # Open the default email client with the mailto: URL
    webbrowser.open(mailto_url)

def run(options):
    sendEmail(options["email"], options["subject"], options["message"])

import ssl
import socket
import datetime
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import smtplib
from email.mime.text import MIMEText

# Set the website URL
url = 'https://ultimateqa.com/'

# Get the SSL certificate from the website
hostname = url.split('//')[-1].split('/')[0]
context = ssl.create_default_context()
with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        cert_data = ssock.getpeercert(True)

# Parse the certificate
cert = x509.load_der_x509_certificate(cert_data, default_backend())

# Calculate the remaining days until the certificate expires
not_valid_after = cert.not_valid_after.replace(tzinfo=datetime.timezone.utc)
remaining_days = (not_valid_after - datetime.datetime.now(datetime.timezone.utc)).days

# Print the number of days remaining until the certificate expires
print(f"\nSSL certificate expire date: {not_valid_after}")
print(f"The SSL certificate for {url} will expire in {remaining_days} days.")



"""To automate this procedure, I would create a Python script that takes in the website URL as an input, connects to 
the website's SSL certificate and parses the certificate. Using the not_valid_after field of the x509 certificate, 
I would calculate the remaining days until the certificate expires and output this value. Finally, I would use
Task Scheduler to run the script at regular intervals, say once every week, to ensure that the webmaster is aware of any 
upcoming expirations. """

# Send an email if the certificate will expire in less than 30 days

if remaining_days < 30:
    # Set up the email message
    msg = MIMEText(f"The SSL certificate for {url} will expire in {remaining_days} days.")
    msg['Subject'] = f"{url} SSL certificate will expire soon"
    msg['From'] = 'nigussie.aman@gmail.com'
    msg['To'] = 'aman.nigussie@gmail.com'

    # Send the email using SMTP
    with smtplib.SMTP('smtp.example.com', 587) as smtp:
        smtp.starttls()
        smtp.login('sender@example.com', 'password')
        smtp.send_message(msg)



"""
To run the Python script on Windows, you can use the built-in Task Scheduler. Here are the steps to set it up:

- Open Task Scheduler by typing "Task Scheduler" in the Start menu search bar and selecting it.
- In the Task Scheduler window, click on "Create Task" in the "Actions" pane on the right side of the window.

- In the "General" tab, give your task a name and a description (optional).

- In the "Triggers" tab, click on "New" to create a new trigger for the task. Choose the schedule and frequency for your 
task (e.g. daily at 9am).

- In the "Actions" tab, click on "New" to create a new action for the task. Choose "Start a program" as the action type, 
and enter the path to the Python executable (C:\Python38\python.exe) in the "Program/script" field. In the "Add arguments" 
field, enter the path to your Python script (i.e C:\Documents\Software Engineering\Voss\ssl_certificate_check.py).

- In the "Conditions" tab, choose the conditions under which the task will run (e.g. whether the computer needs to be idle or not).

- In the "Settings" tab, choose any additional settings for the task (e.g. whether the task should run even if the user 
is not logged on).

- Click "OK" to save the task.

The task will now run according to the schedule you set up, and will execute the Python script you specified. If you 
want to test the task before it runs automatically, you can right-click on it in Task Scheduler and choose "Run" to 
run it manually. """
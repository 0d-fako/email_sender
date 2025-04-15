from dotenv import load_dotenv
import os
import yagmail


load_dotenv()


email = os.getenv("EMAIL")
app_password = os.getenv("APP_PASSWORD")


yag = yagmail.SMTP(email, app_password)


recipient = "od.fakorede@gmail.com"
subject = "Hello Olumide"
body = "Hello! This is a nice to implement feature, being able to send my email form my terminate"
pdf_attachment = r"C:\Users\Dell\Desktop\Books\Design Thinking\Pains.docx"

yag.send(to=recipient, subject=subject, contents=body, attachments=[pdf_attachment])
print("Email sent successfully!")
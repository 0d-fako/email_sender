from dotenv import load_dotenv
import os
import yagmail


load_dotenv()


email = os.getenv("EMAIL")
app_password = os.getenv("APP_PASSWORD")


yag = yagmail.SMTP(email, app_password)


recipients = ["od.fakorede@gmail.com", "achlaservices@gmail.com"]

subject = "Hello Olumide"

body = """
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; }
        .container { background: white; padding: 20px; border-radius: 8px; text-align: center; }
        h1 { color: #3498db; }
        p { font-size: 16px; color: #333; }
        .button { background:#3498db; color:white; padding:10px 20px; border-radius:5px; text-decoration:none; font-weight:bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello Olumide,</h1>
        <p>This is a <b>styled email</b> with an image and a button! 🎉</p>
        <p>Let me know what you think!</p>
        <img src="https://photos.google.com/search/CgRMdW1pGikKJ0FGMVFpcE5fU2NWRE5ZSjZkVFQ1Q3ptcm5IWTVIT1RGc09YX3N6YyI3CgRMdW1pEi8KLQorCikSJ0FGMVFpcE5fU2NWRE5ZSjZkVFQ1Q3ptcm5IWTVIT1RGc09YX3N6Yyjg2p3M4zI%3D/photo/AF1QipOTJmZCIpkmD9ajzuigA1bGjVFzT1_Q-YvlP6Ra" alt="Sample Image" width="300">
        <br><br>
        <a href="https://www.linkedin.com/in/od-fakorede" class="button">Visit LinkedIn</a>
    </div>
</body>
</html>
"""

pdf_attachment = r"C:\Users\Dell\Desktop\Books\Design Thinking\Pains.docx"


for recipient in recipients:
    yag.send(to=recipient, subject=subject, contents=body, attachments=[pdf_attachment])
print("Email sent successfully!")
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import os
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from zipfile import ZipFile


def send_report(config, subject, msg, author, to, status, result_file):
    line_1_text = ''
    # The subject line for the email.
    SUBJECT = subject
    line_2 = "Overall Status of Execution is:" + status + ".\r\n\n"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("{to},\r\n\n" +
                 line_1_text +
                 line_2 +
                 "--- \r\n"
                 "{author}"
                 )

    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
    <h1>{subject}</h1>
    <h2>Execution Status:  {status}</h3>
    <p>{to}, <br /> <br />
        {msg} <br /><br />
        Kindly take the necessary steps.<br /><br />
        --- <br />
        {author}
    </body>
    </html>""".format(subject=subject, status=status)

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a multipart/mixed parent container.
    msg = MIMEMultipart('mixed')
    # Add subject, from and to lines.
    msg['Subject'] = SUBJECT
    msg['From'] = config['smtp.sender.email'].data
    msg['To'] = config['recepients'].data

    # Create a multipart/alternative child container.
    msg_body = MIMEMultipart('alternative')

    # Encode the text and HTML content and set the character encoding. This step is
    # necessary if you're sending a message with characters outside the ASCII range.
    textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
    htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)

    # Add the text and HTML parts to the child container.
    msg_body.attach(textpart)
    msg_body.attach(htmlpart)
    zip_file = '{}.zip'.format(subject)
    with ZipFile(zip_file, 'w') as zip:
        for rf in result_file:
            zip.write(rf)

        # Define the attachment part and encode it using MIMEApplication.
    att1 = MIMEApplication(open(zip_file, 'rb').read())

    # Add a header to tell the email client to treat this part as an attachment,
    # and to give the attachment a name.
    att1.add_header('Content-Disposition', 'zip_file',
                    filename=os.path.basename(zip_file))

    # Add the attachment to the parent container.
    msg.attach(att1)

    # Attach the multipart/alternative child container to the multipart/mixed
    # parent container.
    msg.attach(msg_body)

    # print(msg)
    try:
        server = smtplib.SMTP('smtp.office365.com', int(config['smtp.port'].data))
        server.ehlo()
        server.starttls()
        server.login(config['smtp.sender.email'].data,
                     base64.b64decode(str(config['smtp.mail.pwd'].data)).decode("utf-8"))
        print('Connected to Email server !!')
        text = msg.as_string()
        server.sendmail(config['smtp.sender.email'].data, config['recepients'].data, text)
        server.quit()


    # Display an error if something goes wrong.
    except Exception as e:
        print(str[e])
    else:
        print("Email sent!")

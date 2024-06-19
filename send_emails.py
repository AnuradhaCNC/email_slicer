import smtplib
import csv
from string import Template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def read_template(filename):
    with open('/Users/anuradha/Desktop/emails/template.txt', 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    # Read email template from template.txt
    message_template = read_template('template.txt')

    MY_ADDRESS = 'anuradhaa66@gmail.com'
    PASSWORD = 'anu66123'

    # Set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    with open("details.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # Skip the header row
        next(csv_reader)
        for row in csv_reader:
            # Substitute values from CSV into the template
            message = message_template.substitute(PERSON_NAME=row[0], MATH=row[1], ENG=row[2], SCI=row[3])
            print(message)  # Optional: Print the composed message to console

            # Set up email message
            msg = MIMEMultipart()
            msg['From'] = MY_ADDRESS
            msg['To'] = row[4]  # Assuming email address is in the 5th column of CSV
            msg['Subject'] = "Mid term grades"

            # Attach message body
            msg.attach(MIMEText(message, 'plain'))

            # Send email via SMTP server
            s.send_message(msg)

            # Clean up message
            del msg

    # Terminate the SMTP session and close the connection
    s.quit()

if __name__ == '__main__':
    main()

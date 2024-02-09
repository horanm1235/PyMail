# Setup Instructions

1. **Install Required Dependencies:**
   - Install the required dependencies using pip:
     ```
     pip install smtplib
     pip install configparser
     ```

2. **Enable Less Secure App Access:**
   - Go to your Google Account settings.
   - Navigate to the Security section.
   - Enable "Less secure app access". This allows the script to send emails using your Gmail account.

3. **Configure the `config_email.txt` File:**
   - Open the `config_email.txt` file in a text editor.

4. **Provide Sender's Email and Password:**
   - Fill in the sender's email address and password under the `[Email]` section.
     - **Note:** To obtain an app password for your Gmail account, follow these steps:
       1. Go to your Google Account settings.
       2. Navigate to the Security section.
       3. Under "Signing in to Google", select "App passwords".
       4. Generate a new app password for the script. Choose "Other (Custom name)" and give it a descriptive name.
       5. Use the generated app password as the sender's password in the `config_email.txt` file.

5. **Specify Recipients and Email Details:**
   - Specify the recipient email addresses under the `[Email]` section. You can also add CC and BCC email addresses if needed. separate the emails with commas.
   - Set the email subject under the `[Message]` section.
   - write the email body in the body_email.txt file
6. **Specify Attachment Paths:**
   - Specify the paths to the attachments under the `[Attachments]` section. If you have multiple attachments, separate the paths with commas.
7. **Save both config_email.txt and body_email.txt**

## Usage Instructions

1. **Run the Script:**
2. **Check Console Output:**
   - Check the console output for any errors or status messages.

## Notes

- Make sure the specified attachments exist at the specified paths.
- Ensure that the sender's Gmail account allows access from less secure apps.
- Double-check the recipient email addresses, subject, and email body before running the script.
- For security reasons, do not share the `config_email.txt` file or the Gmail account credentials with others.

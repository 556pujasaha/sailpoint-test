import requests
import datetime
import smtplib
from email.mime.text import MIMEText

# Set variables
repository_name = "octocat/Hello-World"
start_date = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
end_date = datetime.datetime.now().strftime("%Y-%m-%d")
email_to = "pujasaha556@gmail.com"
email_from = "556pujasaha@gmail.com"
email_subject = "GitHub Pull Request Summary Report"

# Authenticate with GitHub API
headers = {"Authorization": "Bearer token"}
url = f"https://api.github.com/repos/{repository_name}/pulls?state=all&since={start_date}&until={end_date}"
response = requests.get(url, headers=headers)
pull_requests = response.json()

# Filter pull requests by state
closed_pull_requests = [pr for pr in pull_requests if pr["state"] == "closed"]
open_pull_requests = [pr for pr in pull_requests if pr["state"] == "open"]
merged_pull_requests = [pr for pr in pull_requests if pr["state"] == "merged"]

# Format email body
email_body = f"""
GitHub Pull Request Summary Report

Closed Pull Requests
---------------------
{len(closed_pull_requests)} pull requests closed in the last week.

Open Pull Requests
-------------------
{len(open_pull_requests)} pull requests currently open.

Merged Pull Requests
---------------------
{len(merged_pull_requests)} pull requests merged in the last week.
"""

# Send email
msg = MIMEText(email_body)
msg["To"] = email_to
msg["From"] = email_from
msg["Subject"] = email_subject

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as smtp:
    smtp.login("9f7770f3f94ce8", "35df10adb9aef9")
    smtp.send_message(msg)

# Print email details to console
print(f"Email sent to {email_to} from {email_from} with subject '{email_subject}' and body:")
print(email_body)
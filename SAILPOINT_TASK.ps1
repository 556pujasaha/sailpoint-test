# Import required modules
Import-Module -Name Microsoft.PowerShell.Utility
Import-Module -Name Microsoft.PowerShell.Management
Import-Module -Name GitHub

# Set variables
$repositoryName = "octocat/Hello-World"
$startDate = (Get-Date).AddDays(-7)
$endDate = Get-Date
$emailTo = "556pujasaha@gmail.com"
$emailFrom = "pujasaha556@gmail.com"
$emailSubject = "GitHub Pull Request Summary Report"

# Authenticate with GitHub API
$token = "token"
Set-GitHubAuthentication -AccessToken $token

# Retrieve pull requests
$pullRequests = Get-GitHubPullRequest -Repository $repositoryName -State all -Since $startDate -Until $endDate

# Filter pull requests by state
$closedPullRequests = $pullRequests | Where-Object { $_.state -eq "closed" }
$openPullRequests = $pullRequests | Where-Object { $_.state -eq "open" }
$mergedPullRequests = $pullRequests | Where-Object { $_.state -eq "merged" }

# Format email body
$emailBody = @"
GitHub Pull Request Summary Report

Closed Pull Requests
---------------------
$($closedPullRequests.Count) pull requests closed in the last week.

Open Pull Requests
-------------------
$($openPullRequests.Count) pull requests currently open.

Merged Pull Requests
---------------------
$($mergedPullRequests.Count) pull requests merged in the last week.
"@

# Send email
Send-MailMessage -To $emailTo -From $emailFrom -Subject $emailSubject -Body $emailBody

# Print email details to console
Write-Host "Email sent to $emailTo from $emailFrom with subject '$emailSubject' and body:"
Write-Host $emailBody
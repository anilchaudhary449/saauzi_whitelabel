# CI/CD Email Report Setup Guide

This guide explains how to configure email notifications for test reports in the CI/CD pipeline.

## Setting Up Email Secrets in GitHub

To enable email sending, you need to add the following secrets to your GitHub repository:

### Steps:

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret** and add the following secrets:

### Required Secrets:

| Secret Name | Description | Example |
|------------|-------------|---------|
| `EMAIL_SERVER` | SMTP server address | `smtp.gmail.com` |
| `EMAIL_PORT` | SMTP port | `465` (for SSL) or `587` (for TLS) |
| `EMAIL_USERNAME` | Email account username | `your-email@gmail.com` |
| `EMAIL_PASSWORD` | Email password or App password | See provider instructions below |
| `EMAIL_FROM` | Sender email address | `your-email@gmail.com` |
| `EMAIL_RECIPIENT` | Recipient email address(es) | `recipient@example.com` or `email1@example.com,email2@example.com` |

## Provider-Specific Instructions

### Gmail

1. **Enable 2FA** on your Gmail account (if not already enabled)
2. **Generate App Password:**
   - Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
   - Select "Mail" and "Windows Computer"
   - Generate a password (16 characters)
3. **Use these settings:**
   - `EMAIL_SERVER`: `smtp.gmail.com`
   - `EMAIL_PORT`: `465`
   - `EMAIL_USERNAME`: Your Gmail address
   - `EMAIL_PASSWORD`: The 16-character app password (no spaces)
   - `EMAIL_FROM`: Your Gmail address

### Outlook/Office 365

1. **Use these settings:**
   - `EMAIL_SERVER`: `smtp.office365.com`
   - `EMAIL_PORT`: `587`
   - `EMAIL_USERNAME`: Your Outlook email
   - `EMAIL_PASSWORD`: Your Outlook password
   - `EMAIL_FROM`: Your Outlook email

### Custom SMTP Server

Use your organization's SMTP server details:
- `EMAIL_SERVER`: Your SMTP server domain
- `EMAIL_PORT`: Your SMTP port (typically 587 or 465)
- `EMAIL_USERNAME`: Your account username
- `EMAIL_PASSWORD`: Your account password
- `EMAIL_FROM`: Sender email address

## Test Email Configuration

To test if email is working correctly:

1. Make a push or create a pull request to your main/master branch
2. Check the Actions tab in your GitHub repository
3. Click on the latest workflow run
4. If setup is correct, you should receive an email with:
   - Test execution status
   - Branch and commit information
   - Link to the workflow run
   - Attached HTML report

## Email Report Contents

The email includes:
- **Repository**: Name of the repository
- **Branch**: Which branch was tested
- **Commit**: Commit SHA and actor
- **Status**: PASSED, FAILED, or other status
- **Run Details**: Link to the GitHub Actions workflow
- **Attachment**: Complete HTML test report

## Troubleshooting

### Email not received:

1. **Check GitHub Actions logs:**
   - Go to Actions tab → Latest workflow
   - Look for "Send Test Report Email" step
   - Check for error messages

2. **Verify secrets are set correctly:**
   - Go to Settings → Secrets and variables → Actions
   - Confirm all required secrets are present

3. **Check spam folder:**
   - Email might be marked as spam

4. **Verify email credentials:**
   - Try logging in manually with the same credentials
   - For Gmail, ensure you're using an App Password, not your regular password

5. **Port issues:**
   - Port 465: SSL/TLS
   - Port 587: STARTTLS
   - Try the alternate port if one fails

### Large attachment issues:

If the HTML report is very large:
- Reports are usually under 1MB, so size shouldn't be an issue
- Check your email provider's attachment limits

## Optional: Multiple Recipients

To send to multiple email addresses, separate them with commas:

```
EMAIL_RECIPIENT: email1@example.com,email2@example.com,email3@example.com
```

## Optional: Customize Email Message

You can customize the email body in `.github/workflows/ci.yml`:

Find this section:
```yaml
body: |
  Test Execution Report for ${{ github.repository }}
  ...
```

Add your custom message or variables available in GitHub Actions.


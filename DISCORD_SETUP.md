# Discord Integration Setup Guide

This guide explains how to configure Discord notifications for test reports in the CI/CD pipeline.

## Setting Up Discord Webhook

### Steps:

1. **Create a Discord Server** (if you don't have one)
   - Go to [Discord](https://discord.com)
   - Create a new server or use an existing one

2. **Create a Channel for Test Reports**
   - Right-click on your server
   - Select "Create Channel"
   - Name it something like `#test-reports`
   - Set it to text channel

3. **Create a Webhook**
   - Go to your channel settings
   - Click "Integrations" on the left sidebar
   - Click "Webhooks"
   - Click "Create Webhook"
   - Name it something like "GitHub Actions"
   - Copy the Webhook URL (this is your `DISCORD_WEBHOOK` secret)

4. **Add the Secret to GitHub**
   - Go to your GitHub repository
   - Click **Settings** → **Secrets and variables** → **Actions**
   - Click **New repository secret**
   - Name: `DISCORD_WEBHOOK`
   - Value: Paste the webhook URL you copied
   - Click "Add secret"

## Webhook Permissions

Make sure your webhook has these permissions:
- ✅ Send Messages
- ✅ Embed Links (for rich formatting)

The webhook is automatically created with these permissions by default.

## Test the Setup

1. **Push to main/master branch** or create a pull request
2. **GitHub Actions will run** and execute the tests
3. **Check your Discord channel** for the test report notification

You should see a message like:

```
🧪 **Test Report** - your-org/your-repo

**Status**: ✅ PASSED
**Branch**: `main`
**Commit**: `abc123def456`
**Actor**: your-username

📊 [View Workflow](...)
📥 [Download Report](...)
```

## Notification Details

The Discord notification includes:
- ✅ **Status**: PASSED or FAILED
- 📦 **Repository**: Name of the repo
- 🌿 **Branch**: Which branch was tested
- 🔗 **Commit**: Short SHA of the commit
- 👤 **Actor**: Who triggered the workflow
- 📊 **Workflow Link**: Direct link to see detailed logs
- 📥 **Report Link**: Direct link to download the HTML report

## Multiple Channels (Optional)

To send notifications to multiple channels:

1. Create webhooks in different channels
2. Add multiple secrets: `DISCORD_WEBHOOK_1`, `DISCORD_WEBHOOK_2`, etc.
3. Add multiple notification steps in your workflow

## Troubleshooting

### Discord message not received:

1. **Verify the webhook URL:**
   - Make sure you copied the complete URL from Discord
   - URLs should start with `https://discord.com/api/webhooks/`

2. **Check GitHub Actions logs:**
   - Go to Actions tab → Latest workflow
   - Look for "Send Discord Notification" step
   - Check for error messages

3. **Verify the secret:**
   - Go to Settings → Secrets and variables → Actions
   - Confirm `DISCORD_WEBHOOK` is listed

4. **Check Discord channel:**
   - Make sure you have the correct channel
   - Check webhook settings in Discord

5. **Regenerate webhook (if needed):**
   - In Discord channel settings → Integrations → Webhooks
   - Delete the old webhook
   - Create a new one
   - Update the GitHub secret with the new URL

## Customize the Message

You can customize the Discord message by editing the workflow file at `.github/workflows/ci.yml`.

Find the "Send Discord Notification" step and modify the `content` field:

```yaml
content: |
  🧪 **Test Report** - ${{ github.repository }}
  
  **Status**: ${{ job.status == 'success' && '✅ PASSED' || '❌ FAILED' }}
  **Branch**: `${{ github.ref_name }}`
  **Commit**: `${{ github.sha }}`
  **Actor**: ${{ github.actor }}
  
  📊 [View Workflow](https://github.com/${{ github.repository }}/actions/runs/${{ github.run_id }})
  📥 [Download Report](https://github.com/${{ github.repository }}/actions/runs/${{ github.run_id }})
```

Available variables:
- `${{ github.repository }}` - Repository name
- `${{ github.ref_name }}` - Branch name
- `${{ github.sha }}` - Full commit SHA
- `${{ github.actor }}` - User who triggered the action
- `${{ job.status }}` - Job status (success, failure)
- `${{ github.run_id }}` - Workflow run ID

## Discord Formatting

Discord supports these formatting options:
- `**bold**` for bold text
- `*italic*` for italic text
- `***bold italic***` for bold italic
- `` `code` `` for inline code
- Emojis like 🧪, ✅, ❌, 📊, 📥

Use these in your custom messages!


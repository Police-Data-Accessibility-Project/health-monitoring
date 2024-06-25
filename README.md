# Health Monitoring

This repository is used to monitor the health of https://pdap.io/, send alerts when errors are detected, and, where necessary, perform corrective actions.

It is designed to function within the Automation Manager Digital Ocean Droplet. It's deployed to http://automation.pdap.io/

## How it works

The script will check the status of the search endpoint. 
If the endpoint is not functioning as expected, it will send an alert to the PDAP Discord, within the `private/#dev-alerts` channel.

Within the Automation Manager, a cron job is set up to run the `run.sh` script, which will automatically pull the latest changes, install any requirements, and run the script from a virtual environment.

### Logging

The script will log to a file named health_monitoring.log in the root directory. These logs are designed to rotate every day at midnight.

## Installation

### Clone this repository and navigate to the root directory.

```
git clone https://github.com/Police-Data-Accessibility-Project/health-monitoring.git
cd health-monitoring
```

### Create a file named .env in the root directory containing secrets for the Webhook URL.

The app needs access to these variables. Reach out to contact@pdap.io or make noise in Discord if you'd like access

```env
WEBHOOK_URL=<YOUR_WEBHOOK_URL>
TEXTBELT_API_KEY=<YOUR_API_KEY>
SMS_NUMBER=<NOTIFICATION_RECIPIENT_PHONE>
```

When deployed, these variables can be managed in the build environment: http://automation.pdap.io/job/Health-Monitor/configure

### Modify permissions for run.sh

```
chmod +x run.sh
```

### Run the script

```
./run.sh
```

# Verifying Functionality

All verification will need to be performed within the Automation Manager Droplet, in the `health-monitoring` directory, accessible from the home directory. The Automation Manager can be accessed via SSHing into the Droplet or navigating to http://automation.pdap.io/

## Verifying recent script operation

Within the `health-monitoring` directory, run:

```shell
cat health_monitoring.log
```

This should show up in the terminal. The log should show results such as:

```text
2024-06-15 17:00:06,452 - INFO - Search endpoint is functioning as expected.
2024-06-15 18:00:06,097 - INFO - Search endpoint is functioning as expected.
2024-06-15 19:00:05,291 - INFO - Search endpoint is functioning as expected.
```

The timestamps should always show activity within the last hour. In the case of errors, these should also be logged within this file.

## Verifying Discord Functionality

From the `scripts` directory, with the virtual environment mentioned in the `run.sh` script activate, run:

```shell
python3 scripts/webhook_logic.py
```

This will post the message "Testing from health-monitoring" to the Webhook URL in the .env file, which should show up in the `private/#dev-alerts` in the Discord.


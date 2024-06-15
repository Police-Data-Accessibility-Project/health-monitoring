# Health Monitoring

This repository is used to monitor the health of https://pdap.io/, send alerts when errors are detected, and, where necessary, perform corrective actions.

It is designed to function within the Automation Manager Digital Ocean Droplet.

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

The app should have a WEBHOOK URL environment variable. Reach out to contact@pdap.io or make noise in Discord if you'd like access to this key

```env
WEBHOOK_URL=<YOUR_WEBHOOK_URL>
```

### Modify permissions for run.sh

```
chmod +x run.sh
```

### Run the script

```
./run.sh
```
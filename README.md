# Health Monitoring

This repository will be used to monitor the health of https://pdap.io/, send alerts when errors are detected, and, where necessary, perform corrective actions. 

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
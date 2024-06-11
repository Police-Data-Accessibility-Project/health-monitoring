# Health Monitoring

This repository will be used to monitor the health of https://pdap.io/, send alerts when errors are detected, and, where necessary, perform corrective actions. 

## Installation

### 1. Clone this repository and navigate to the root directory.

```
git clone https://github.com/Police-Data-Accessibility-Project/health-monitoring.git
cd health-monitoring
```

### 2. Create a virtual environment.

If you don't already have virtualenv, install the package:

```

pip install virtualenv

```

Then run the following command to create a virtual environment:

```

virtualenv -p python3.11 health_venv

```

### 3. Activate the virtual environment.

```

source health_venv/bin/activate

```

### 4. Install dependencies.

```

pip install -r requirements.txt

```

### 5. Create a file named .env in the root directory containing secrets for the Webhook URL.

The app should have a WEBHOOK URL environment variable. Reach out to contact@pdap.io or make noise in Discord if you'd like access to this key

```env
WEBHOOK_URL=<YOUR_WEBHOOK_URL>

```

### 6. Run the primary script.

```

python3 scripts/check_search_endpoint.py

```
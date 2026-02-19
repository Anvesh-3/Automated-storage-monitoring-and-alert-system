# Automated Storage Monitoring and Alert System

## Overview
Python-based storage monitoring system that tracks disk usage, CPU, and memory metrics across Linux-based virtual machines.

## Features
- Disk usage monitoring
- CPU & memory tracking
- Threshold-based email alerts
- Logging for historical analytics
- Modular design

## Tech Stack
- Python
- psutil
- Linux
- SMTP
- Cron Jobs

## Setup
1. Install dependencies:
   pip install -r requirements.txt

2. Configure email in config.py

3. Run:
   python monitor.py

## Automation
Schedule using cron:
0 * * * * /usr/bin/python3 /path/to/monitor.py

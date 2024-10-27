# Flask Application with MySQL and Nginx

## Overview

This Flask application is built with Python, using MySQL for the database and deployed on an Amazon EC2 instance. Nginx is used as a reverse proxy, and Gunicorn serves the Flask app in a production environment. The application is configured with SSL encryption using Let's Encrypt.

## Features

- **User Authentication**: Includes account creation, login, and password reset functionality.
- **MySQL Integration**: Stores user data in a MySQL database.
- **Nginx + Gunicorn**: Efficiently serves the application in production.
- **SSL**: Secures communication with HTTPS using Let's Encrypt.

## Requirements

- Python 3.x
- Flask
- MySQL Server
- Nginx
- Gunicorn
- AWS EC2 (Ubuntu)
- Certbot for SSL (Let's Encrypt)

## Setup and Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repository/flask-mysql-app.git
cd flask-mysql-app

Step 2: Set Up Virtual Environment
Create a virtual environment and activate it:
python3 -m venv myenv
source myenv/bin/activate

Step 3: Install Dependencies
Install the required Python packages:
pip install -r requirements.txt

Step 4: Configure MySQL
Log in to MySQL:
mysql -u root -p
Create a database for the app:
CREATE DATABASE flask_app;

Deploying to AWS EC2
Step 1: Launch EC2 Instance
Set up an AWS EC2 instance (Ubuntu).
SSH into your instance:
ssh -i /path/to/your-key.pem ubuntu@your-instance-public-ip

Install Required Software on EC2
sudo apt update
sudo apt install python3-pip nginx mysql-server -y

Transfer Files to EC2
scp -i /path/to/your-key.pem -r /path/to/your-app ubuntu@your-instance-public-ip:/home/ubuntu/

Set Up Nginx
Create a new Nginx configuration for your app:
sudo nano /etc/nginx/sites-available/myflaskapp
Add the following:
server {
    listen 80;
    server_name your_instance_public_dns_or_ip;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

Enable the configuration and restart Nginx:
sudo ln -s /etc/nginx/sites-available/myflaskapp /etc/nginx/sites-enabled
sudo systemctl restart nginx





























































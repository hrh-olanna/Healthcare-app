# Healthcare-app
Flask Healthcare Application

**Overview**
This Flask application collects healthcare-related spending data and stores it in MongoDB. Data is exported to CSV and analyzed using Jupyter Notebook.

**Requirements**
- Python 3.9+
- MongoDB (Local)
- pip

**Setup**

1. Install MongoDB locally
2. Start MongoDB service
3. Install dependencies:
   pip install -r requirements.txt
4. Run Flask app: python app.py
5. Export data: python export_to_csv.py
6. Run Jupyter: jupyter notebook

**Database**
Database: healthcare_application
Collection: user details

**Deployment**
Deploy on AWS EC2 (Ubuntu). Open port 5000 in security group.

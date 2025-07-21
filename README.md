# ☁️ AWS Toolbox for DBAs, DBREs & Cloud Engineers

This repository contains a growing collection of **Python scripts** and tools to simplify repetitive tasks in AWS.  
It’s designed for **DBAs**, **DBREs**, and **Cloud Engineers** who work daily with AWS services like DynamoDB, S3, and more.

---

## 🚀 Why this exists?

Managing AWS resources often involves repetitive manual operations.  
This toolbox provides **ready-to-use scripts** that help automate common tasks like cleaning up DynamoDB tables, managing S3 buckets, and more.

---

## 🛠️ Current Tools

### 📌 1. DynamoDB Table Truncator

A Python script to delete all items from a specified DynamoDB table.

### 📝 Features:
- Deletes all records in batches for efficiency.
- Minimizes data transfer by retrieving only the table keys.
- Supports optional **assume-role** for cross-account operations.

### 💻 Usage

1️⃣ Install dependencies
Make sure you have `boto3` installed:

```bash
pip install boto3
```
2️⃣ Set AWS credentials

The script uses your default AWS CLI credentials.
If you want to assume a different role, uncomment the assume_role section and update the role_arn in the script.

3️⃣ Run the script
```bash
python truncate_dynamodb.py
```
Edit the last line in the script to specify your table name:
```bash
truncateTable('your-dynamodb-table-name')
```

## 📌 Roadmap

✅ DynamoDB Table Truncator
🔜 S3 Bucket Cleaner
🔜 CloudWatch Logs Purger
🔜 IAM Role Checker

---

## 🙌 Contributing

Feel free to fork the repo, open issues, or submit pull requests with your AWS tools or improvements.
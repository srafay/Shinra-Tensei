# Retool App

## Overview

**Retool App** is a serverless application built on AWS using Lambda, AppSync (GraphQL) and RDS (MySQL). It provides CRUD operations for `Product` entities. Scripts are provided for easily recreating and testing the application on AWS.

---

## Architecture

- **VPC**: Custom VPC with public and private subnets.
- **RDS MySQL**: Hosted in private subnets, with credentials managed in AWS Secrets Manager.
- **Lambda Functions**: CRUD operations for Products (`list`, `get`, `create`, `update`, `delete`).
- **AppSync GraphQL API**: Frontend interface to call Lambda functions.
- **Security**: 
  - Lambda functions run inside the VPC and use security groups for access to RDS.
  - RDS credentials are stored in Secrets Manager.

---

## Prerequisites
- AWS CLI configured with credentials.
- AWS SAM CLI installed.
- Docker installed (required for sam build --use-container).
- Python 3.13 for Lambda runtime.

## Deployment Steps

### 1. Deploy VPC
```bash
source scripts/01_deploy_vpc.sh
```

### 2. Deploy RDS
```bash
source scripts/02_deploy_rds.sh
```

### 3. Deploy Lambda + AppSync
```bash
source scripts/03_deploy_lambda.sh
```
After deployment, the GraphQL API URL is printed in the console, or you can copy it from AWS Console -> AWS AppSync -> Http Endpoint.

Use this Http Endpoint for creating the Retool application.

Check resources created by each stack on AWS CloudFormation.
<img width="1759" height="363" alt="image" src="https://github.com/user-attachments/assets/0050257f-fb34-4d82-8d19-21931b4bb584" />




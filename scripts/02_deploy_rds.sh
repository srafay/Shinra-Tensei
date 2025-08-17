#!/bin/bash
echo "Deploying RDS stack..."

VPC_ID=$(aws cloudformation describe-stacks \
  --stack-name MyAtelierApp-Vpc \
  --query "Stacks[0].Outputs[?OutputKey=='VpcId'].OutputValue" \
  --output text)

SUBNET1=$(aws cloudformation describe-stacks \
  --stack-name MyAtelierApp-Vpc \
  --query "Stacks[0].Outputs[?OutputKey=='RdsPrivateSubnet1Id'].OutputValue" \
  --output text)

SUBNET2=$(aws cloudformation describe-stacks \
  --stack-name MyAtelierApp-Vpc \
  --query "Stacks[0].Outputs[?OutputKey=='RdsPrivateSubnet2Id'].OutputValue" \
  --output text)

LAMBDA_SG=$(aws cloudformation describe-stacks \
  --stack-name MyAtelierApp-Vpc \
  --query "Stacks[0].Outputs[?OutputKey=='RdsSGId'].OutputValue" \
  --output text)


# Ensure required environment variables are available
if [[ -z "$VPC_ID" || -z "$SUBNET1" || -z "$SUBNET2" || -z "$LAMBDA_SG" ]]; then
  echo "ERROR: Missing required VPC outputs. Did you run 01_deploy_vpc.sh?"
  exit 1
fi

sam deploy \
  --template-file rds.yaml \
  --stack-name MyAtelierApp-RDS \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
    VpcId=$VPC_ID \
    Subnet1=$SUBNET1 \
    Subnet2=$SUBNET2 \
    RdsSGId=$LAMBDA_SG

echo "RDS stack deployed. Retrieving outputs..."

DB_SECRET_ARN=$(aws cloudformation describe-stacks \
  --stack-name MyAtelierApp-RDS \
  --query "Stacks[0].Outputs[?OutputKey=='DBSecretArn'].OutputValue" \
  --output text)

DB_ENDPOINT=$(aws cloudformation describe-stacks \
  --stack-name MyAtelierApp-RDS \
  --query "Stacks[0].Outputs[?OutputKey=='DBEndpoint'].OutputValue" \
  --output text)

echo "===================================================="
echo "RDS Stack deployed successfully."
echo "DB Endpoint:      $DB_ENDPOINT"
echo "DB Secret ARN:    $DB_SECRET_ARN"
echo "===================================================="

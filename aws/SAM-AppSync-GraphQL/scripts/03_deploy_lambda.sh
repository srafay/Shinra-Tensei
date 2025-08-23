#!/bin/bash
echo "Deploying Lambda stack..."

# Fetch outputs (from VPC and RDS stack)
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

# Fetch RDS outputs (from RDS stack)
DB_SECRET_ARN=$(aws cloudformation describe-stacks \
  --stack-name MyAtelierApp-RDS \
  --query "Stacks[0].Outputs[?OutputKey=='DBSecretArn'].OutputValue" \
  --output text)

DB_ENDPOINT=$(aws cloudformation describe-stacks \
  --stack-name MyAtelierApp-RDS \
  --query "Stacks[0].Outputs[?OutputKey=='DBEndpoint'].OutputValue" \
  --output text)

# Ensure required environment variables are available
if [[ -z "$VPC_ID" || -z "$SUBNET1" || -z "$SUBNET2" || -z "$LAMBDA_SG" || -z "$DB_SECRET_ARN" || -z "$DB_ENDPOINT" ]]; then
  echo "ERROR: Missing required parameters. Did you run 01_deploy_vpc.sh and 02_deploy_rds.sh?"
  exit 1
fi

sam build --use-container
sam deploy \
  --stack-name MyAtelierApp-Lambda \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
    VpcId=$VPC_ID \
    Subnet1=$SUBNET1 \
    Subnet2=$SUBNET2 \
    RdsSGId=$LAMBDA_SG \
    DBSecretArn=$DB_SECRET_ARN \
    DBEndpoint=$DB_ENDPOINT

echo "Lambda + GraphQL stack deployed. Retrieving outputs..."

GRAPHQL_API_URL=$(aws cloudformation describe-stacks \
  --stack-name MyAtelierApp-Lambda \
  --query "Stacks[0].Outputs[?OutputKey=='GraphQLApiUrl'].OutputValue" \
  --output text)

echo "===================================================="
echo "Lambda + GraphQL Stack deployed successfully."
echo "GraphQL API URL:   $GRAPHQL_API_URL"
echo "===================================================="

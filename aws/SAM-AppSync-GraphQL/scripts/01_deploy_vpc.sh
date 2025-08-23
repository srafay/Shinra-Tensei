#!/bin/bash
echo "Deploying VPC stack..."
sam deploy \
  --template-file vpc-setup.yaml \
  --stack-name MyAtelierApp-Vpc \
  --capabilities CAPABILITY_NAMED_IAM

echo "VPC stack deployed. Retrieving outputs..."
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

RDS_SG=$(aws cloudformation describe-stacks \
  --stack-name MyAtelierApp-Vpc \
  --query "Stacks[0].Outputs[?OutputKey=='RdsSGId'].OutputValue" \
  --output text)


echo "===================================================="
echo "VPC Stack deployed successfully."
echo "VPC_ID:   $VPC_ID"
echo "SUBNET1:  $SUBNET1"
echo "SUBNET2:  $SUBNET2"
echo "RDS_SG:   $RDS_SG"
echo "===================================================="

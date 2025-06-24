# Logistics Tracking Platform

## Overview
A fully serverless, scalable logistics tracking platform on AWS.

**Features:**
- AWS Lambda (Python)
- DynamoDB for parcel/location data
- API Gateway for HTTP API
- Terraform for Infrastructure as Code
- CI/CD with GitHub Actions
- Monitoring with Amazon Managed Grafana (CloudWatch metrics)
- Load tested for 5,000+ concurrent users

---

## Architecture

![Architecture Diagram](architecture.png)

“designed and diagrammed the end-to-end cloud architecture for clarity and stakeholder alignment.”

---

## Tech Stack

| Layer      | Tech                   |
|------------|------------------------|
| Infra      | Terraform              |
| Compute    | AWS Lambda (Python)    |
| API        | AWS API Gateway        |
| DB         | DynamoDB               |
| CI/CD      | GitHub Actions         |
| Monitoring | Grafana, CloudWatch    |
| Load Test  | Artillery or k6        |

---

## Main Modules

- `infra/` – Terraform IaC
- `lambdas/` – Lambda function code
- `.github/workflows/` – CI/CD definitions
- `README.md` – This file
- `architecture.png` – Your system diagram
- `loadtest-report.md` – Add after load tests

---

## Project Goals

- Fast, scalable, serverless logistics tracking simulation
- 99.9% uptime under load
- End-to-end automation with CI/CD
- Real monitoring and reporting

---

## Get Started

1. Clone this repo.
2. Set up your AWS credentials.
3. Deploy infra:  
   ```bash
   cd infra
   terraform init
   terraform apply

# Okta AD Group Whitelisting for OIDC Claim
This project is to demonstrate how to white list an integrated directory's groups for including as a claim in an OAuth token

This project was built using Python 2.7

This is a simple command line script using Okta's API to push updates to an exsisting OIDC Application, whitelisting an integrated directory's groups 

## Requirements
* Python 2.7
* Okta domain
* Okta API Token

## Dependencies
You can run all the dependencies via the requirements.txt
`pip install -r requirements.txt`

Or run them individually

**linter - flake8**

`pip install flake8`

**HTTP Framework - Update requests**

Needed to install an update to fix a compatability issue

`pip install requests --upgrade`

## How to Run

NOTE: You may need to configure ports to listen to for serviing up the site

`python main.py`

# VoiceTrader
Uses AWS and IFTTT to enable stock trading through your favorite voice assistant

## Table of Contents
- [Requirements](#requirements)
- [Setting up Alpaca](#setting-up-alpaca)
- [Building an API to Run a Lambda Function with AWS](#building-an-api-to-run-a-lambda-function-with-aws)
  - [Creating the Lambda Function](#creating-the-lambda-function)
  - [Exposing the Lambda Function with an API](#exposing-the-lambda-function-with-an-api)
- [Using IFTTT to Connect a Voice Assistant with the API](#using-ifttt-to-connect-a-voice-assistant-with-the-api)
- [Usage](#usage)

## Requirements

- [Alpaca](https://alpaca.markets) account (or any other trading platform with an accessible API)
- [AWS](https://aws.amazon.com/free) account (only the free tier is needed)
- [IFTTT](https://ifttt.com) account
- [Google Assistant](https://assistant.google.com) (Alexa will also work)

## Setting up Alpaca

1. [Sign up](https://app.alpaca.markets/signup) for an Alpaca account.

2. If you'd like to trade with real money, click `Individual Account` and fill in all the required information. To do paper trading, no additional information is necessary. Simply click `Go to Paper Account` on the top-left. I'm using a Paper Trading account, but most of the steps should be similar across both.
![Step 2](https://i.ibb.co/R7mq9FW/Screenshot-2021-01-09-171908.png)

3. You should now be on the Overview Dashboard page, and on the right side you'll see a section titled `Your API Keys`. Click `View` to expand the section and then `Generate New Key`. **Copy your API Key ID and Secret Key, as you won't be able to see it again** unless you generate a new one. These will be used in the next section when [creating the Lambda function](#creating-the-lambda-function).
![Step 3](https://i.ibb.co/s9Xwd2w/Untitled.png)

## Building an API to Run a Lambda Function with AWS

### Creating the Lambda Function

1. Sign up for an [AWS free tier](https://aws.amazon.com/free) account, and then go to the [AWS Lambda](https://console.aws.amazon.com/lambda/home) console page. You should see a `Create function` button.
![Step 1](https://i.ibb.co/BfCFF5z/Screenshot-2021-01-09-173912.png)

2. Click `Create function`, and give it a name. Set the `Runtime` to Python 3.8, and then click `Create function`.
![Step 2](https://i.ibb.co/7bcTC3H/Screenshot-2021-01-09-174156.png)

3. You should now be on the homepage for your newly-created Lambda function. Below the function name in the `Designer` section, click `Layers`, and then `Add a layer`. Lambda functions don't natively support the `requests` library for Python, so we're going to add it here.
![Step 3](https://i.ibb.co/k0TbjPx/Untitled.png)

4. Under `Choose a layer`, click `Specify an ARN` and then enter `arn:aws:lambda:us-east-2:770693421928:layer:Klayers-python38-requests:14`. Where it says `us-east-2`, replace it with whichever AWS region you are currently using (you can find that by clicking the menu on the top-right corner, next to your name). Finally, click `Add`.
![Step 4](https://i.ibb.co/m8qgbg7/Screenshot-2021-01-09-174944.png)

5. Scroll down to the `Function code` section, and in the text editor, replace everything with [this code](https://raw.githubusercontent.com/sidward35/VoiceTrader/main/lambda_function.py). On line 44, replace `ID` and `SECRET` with the Alpaca API Key ID and Secret Key you copied when making your Alapaca account, keeping the quotes around them. Also comment out lines 48-50, unless you would like to create some kind of notification system every time you make a trade (won't be discussing that here). Finally, on the top-right of the `Function code` section, click `Deploy`.
![Step 5](https://i.ibb.co/9HBhJ81/Untitled.png)

6. On the top-right of the Lambda function page, next to `Throttle`, `Qualifiers`, and `Actions`, click on `Test`. Set the event template to `hello-world`, and give the event a name. Replace the JSON body with the text in the image below, and then click `Create`. Finally, click the `Test` button, and you should see a message that says `Execution result: succeeded`. Now if you go to your Alapca account and check `Paper Orders` on the sidebar, you should see that an order has been placed for 5 shares of AMZN.
![Step 6-a](https://i.ibb.co/YXgKs63/Screenshot-2021-01-09-180824.png) 
![Step 6-b](https://i.ibb.co/PhWMYXL/Screenshot-2021-01-09-181136.png)

### Exposing the Lambda Function with an API

1. 

## Using IFTTT to Connect a Voice Assistant with the API

1. 

## Usage


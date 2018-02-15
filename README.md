# AlexaVoiceGame
Experimental game to test the development of Alexa apps using AWS lambda

All code has to be setup with AWS lambda, and an Alexa app must be made to communicate.

**If you wish to test this code, do the following.**

In order to run the code included in this zip:

1. Create a new AWS Lambda instance, and upload the .py code.
2. Create a new Alexa skill, and copy/paste the Intent Schema and Sample Utterances into the 'Interaction Model'
3. Connect the AWS Lambda and Alexa skill by copying the ARN from the AWS Lambda into the Alexa skill under 'Configuration'

The app can then be tested by using an Echo Dot, other compatible device, 
or the inbuilt test section of the Alexa skill *(although this will not make proper use of sessions, and so there will be no progress saved between requests when tested this way)*
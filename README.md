## Sample Python App

This is a basic Python application, used in a number of AWS tutorials, that focus on various ways to deploy it. It is a simple application that allows the user to sign up for a new startup.

The AWS infrastructure for this can be set up by using the AWS CDK code in [https://github.com/danielwohlgemuth/experiments/tree/main/2024/ci-cd-using-codepipeline-codebuild-and-codedeploy](https://github.com/danielwohlgemuth/experiments/tree/main/2024/ci-cd-using-codepipeline-codebuild-and-codedeploy).

Landing Page

![landing page](/assets/landing-page.png)

Sign-up

![sign up](/assets/sign-up.png)

DynamoDB Items

![dynamodb items](/assets/dynamodb-items.png)

AWS Architecture

![AWS Architecture](/assets/sample-python-app.png)

[AWS Architecture diagram file](https://app.diagrams.net/?title=sample-python-app#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fdanielwohlgemuth%2Fsample-python-web-app%2Frefs%2Fheads%2Fmain%2Fassets%2Fsample-python-app.drawio)

### Code Coverage

The code has a few simple tests using the standard `unittest` module available in Python.

Code coverage is generated using the `coverage` package.

```
Name             Stmts   Miss  Cover
------------------------------------
application.py      33      3    91%
utils.py            11      0   100%
------------------------------------
TOTAL               44      3    93%
```

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

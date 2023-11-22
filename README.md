# Infrastructure Management Application

This application allows you to create and destroy infrastructure resources on AWS and GCP using Pulumi.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.11 or later.
- You have installed Pulumi. If not, you can install it from [here](https://www.pulumi.com/docs/get-started/install/).
- You have AWS and GCP accounts.

## Setting Up Environment Variables

This application uses environment variables for configuration. You need to set the following environment variables:

- `PULUMI_ACCESS_TOKEN`: Your Pulumi Access Token. You can get it from [here](https://app.pulumi.com/account/tokens).
- `AWS_ACCESS_KEY_ID`: Your AWS Access Key ID. You can get it from [here](https://console.aws.amazon.com/iam/home?#/security_credentials).
- `AWS_SECRET_ACCESS_KEY`: Your AWS Secret Access Key. You can get it from [here](https://console.aws.amazon.com/iam/home?#/security_credentials).
- `GOOGLE_CLOUD_KEYFILE_JSON`: The path to your GCP service account key file in JSON format. You can get it from [here](https://cloud.google.com/iam/docs/creating-managing-service-account-keys).
- `GOOGLE_CLOUD_PROJECT`: Your GCP Project ID. You can get it from [here](https://console.cloud.google.com/projectselector2/home/dashboard).

You can set these environment variables in your shell, or put them in a `.env` file in the root directory of the project.

## Setting Up the Project

1. Clone this repository.
2. Ensure the env file is setup and the json credentials are present.
3. Install the required Python packages by running.

```bash
pip install -e
```

## Running the Application

You can run the application using the following command:

```bash
infra-app
```

## License

This project uses the following license: [license](./LICENSE).
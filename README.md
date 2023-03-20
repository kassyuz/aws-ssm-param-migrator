# aws-ssm-param-migrator

This script was mainly used to recreate new environmets acroos multiple AWS Regions, as all secrets are managed on AWS Parameter Store all environment variables needs to be recreated on each region as AWS Parameter Store is unique by AWS Region.

This script saves a lot of time when you want to recreate all variables, at that moment more than 200 environment variables had to be recreate on a new test environment, this script increased the recreation from hours of manual work to minutes.

## Generating source JSON document.

To get a set list of AWS Parameter Store values run the code below using the AWS credentials of the account you want to get those values and also you should inform the parameter PATH and the AWS region where it is stored.

```
aws ssm get-parameters-by-path --region us-west-1 --path "/app" --with-decryption  >> example.json
```

Output must be similar to this:

```
{
    "Parameters": [
        {
            "Name": "/app/ROOT_URL",
            "Type": "String",
            "Value": "www.example.com"
        },
        {
            "Name": "/app/MAX_CONNECTIONS",
            "Type": "String",
            "Value": "300"
        },
        {
            "Name": "/app/DATABASE_PORT",
            "Type": "String",
            "Value": "1234"
        }
    ]
}

```

The JSON document will have more data than only `Name`, `Type` and `Value` but for this script these three Key/Value data are the only requiered values that will be used by the script. You can ignore or delete other data.

## How to use the script

1 - generate the JSON document using the `aws` command above;

2 - Check the script if AWS Region, your local AWS Profile Name and the JSON's file name is correct.

3 - If it's all good with #2 step then you need to run `python3 migrate-ssm-param.py` and then you should get the Success message from AWS CLI call for each inserted value.


## Troubleshoot
- The Python script must be execution permissions on OS level (Linux or MacOS), for that you can run:
```
sudo chmod +x migrate-ssm-param.py
```

- For security reasons this script does not overwrite any parameter, if you need to force overwrite go to line 43 and set `true`. If a value with same name/path already exists it will be replaced by the one in the JSON file, even if the new value is wrong or empty. Becareful using `Overwrite=true`


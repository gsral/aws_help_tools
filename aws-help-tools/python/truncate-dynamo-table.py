import boto3

# If you want to use a different role, uncomment the code below and change the role arn

# role_arn = "Role arn"

# boto_sts=boto3.client('sts')
# stsresponse = boto_sts.assume_role(
#     RoleArn=role_arn,
#     RoleSessionName='newsession'
# )

# newsession_id = stsresponse["Credentials"]["AccessKeyId"]
# newsession_key = stsresponse["Credentials"]["SecretAccessKey"]
# newsession_token = stsresponse["Credentials"]["SessionToken"]


# dynamo = boto3.resource('dynamodb',aws_access_key_id=newsession_id,aws_secret_access_key=newsession_key,aws_session_token=newsession_token)

dynamo = boto3.resource('dynamodb') 

def truncateTable(tableName):
    table = dynamo.Table(tableName)

    # Get the table keys
    tableKeyNames = [key.get("AttributeName") for key in table.key_schema]

    # Only retrieve the keys for each item in the table (minimize data transfer)
    projectionExpression = ", ".join('#' + key for key in tableKeyNames)
    expressionAttrNames = {'#'+key: key for key in tableKeyNames}

    counter = 0
    page = table.scan(ProjectionExpression=projectionExpression,
                      ExpressionAttributeNames=expressionAttrNames)
    with table.batch_writer() as batch:
        while page["Count"] > 0:
            counter += page["Count"]
            # Delete items in batches
            for itemKeys in page["Items"]:
                batch.delete_item(Key=itemKeys)
                print(f"Excluindo {itemKeys}")
            # Fetch the next page
            if 'LastEvaluatedKey' in page:
                page = table.scan(
                    ProjectionExpression=projectionExpression, ExpressionAttributeNames=expressionAttrNames,
                    ExclusiveStartKey=page['LastEvaluatedKey'])
            else:
                break
    print(f"Deleted {counter} items from table {tableName}")

truncateTable() #Table name 

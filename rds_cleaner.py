import boto3
import os

"""
boto 3 Docs: 
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html
"""

def clean_rds_instances_dict(rds_instances_dict):
    out_instances_dict = {}
    count = 0
    for instance in rds_instances_dict.get('DBInstances'):
        out_instances_dict[count] = {
                "dbid": instance.get('DBInstanceIdentifier'),
                "engine": instance.get('Engine'),
                "status": instance.get('DBInstanceStatus')
            }
    return out_instances_dict


def print_instances(instances_dict):

    print(f'{"ID":<5}{"DBId":<60}{"Engine":<15}{"Status":<15}')
    for instance in instances_dict.keys():
        dbid = instances_dict.get(instance).get('dbid')
        engine = instances_dict.get(instance).get('engine')
        status = instances_dict.get(instance).get('status')
        print(f"{instance:<5}{dbid:<60}{engine:<15}{status:<15}")


def main():

    # CREATE AN AWS SESSION
    session = boto3.Session(
        aws_access_key_id=os.environ.get("AWS_RDS_ADMIN_ACCESS_KEY"),
        aws_secret_access_key=os.environ.get("AWS_RDS_ADMIN_ACCESS_SECRET"),
        region_name=os.environ.get("AWS_RDS_REGION")
    )

    rds = session.client('rds')
    db_instances = rds.describe_db_instances()

    instances = clean_rds_instances_dict(db_instances)

    print('\nYou have the following instances:\n\n')
    print_instances(instances)

    # LET THE USER CHOOSE WHICH INSTANCES ARE GOING TO BE DELETED
    users_selection = input("\nWhich ones do you want to delete?\n\tComma separated. e.g.: 0,1,2,5\n\t'all' to delete all (except ones with 'deleting' status)\n")

    if users_selection.strip().upper() == "ALL":
        # users_selection = list(instances.keys())
        users_selection = []
        for dict_id in instances.keys():
            if instances.get(dict_id).get('status').upper() != 'DELETING':
                users_selection.append(dict_id)
    else:
        users_selection = [int(x.strip()) for x in users_selection.split(',')]
        #delete duplicates
        users_selection = list(set(users_selection))


    # START DELETING
    for selection in users_selection:
        instance = instances.get(selection)
        print(f"\n\nDeleting Instance: {instance.get('dbid')}")
        deleted_instance = rds.delete_db_instance(
            DBInstanceIdentifier=instance.get('dbid'),
            SkipFinalSnapshot=True,
            DeleteAutomatedBackups=True
        )
        print(f"\nResponse:{deleted_instance}")

    print("\n\n\nINSTANCES STATUS (ID's don't need to match at this point):\n\n")
    db_instances = rds.describe_db_instances()
    instances = clean_rds_instances_dict(db_instances)
    print_instances(instances)

    return(0)


if __name__=="__main__":
    main()
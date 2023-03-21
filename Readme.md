# AWS RDS Cleaner
Tool (written in python) for deleting RDS instances from a specific AWS region.

## Before Running

### Environment variables
Export the following environment variables:
```bash
export AWS_RDS_REGION="<AWS REGION>"
export AWS_RDS_ADMIN_ACCESS_KEY="<AWS  access  key>"
export AWS_RDS_ADMIN_ACCESS_SECRET="<AWS  access  secret>"
```

### Dependencies
Install the dependencies located in the requirements file:

    pip install -r requirements.txt
 
## Execution:

Execute the following command in the project root: 
```bash
python rds_cleaner.py
```

Then a list of the RDS instances in the configured region will be displayed and you will be asked if you want to delete all (using *all*) or specific ones (using a list of IDs separated by commas, e.g. *1,3,4,6*).

The requested instances will be deleted and a message will be displayed with the status of these instances, which should be "deleting".


### Output example:

```bash
$ python rds_cleaner.py 

You have the following instances:


ID   DBId                                                        Engine         Status         
0    example-inst0                                               postgres       available      
1    example-mariaDB-instance-00-dev-team          				 mariadb        available      
2    example-mariaDB-instance-01-dev-team          				 mariadb        available      
3    example-mySQL-instance-00-dev-team            				 mysql          available      
4    example-mySQL-instance-01-dev-team            				 mysql          available      
5    example-postgres-instance-00-dev-team         				 postgres       backing-up     
6    example-postgres-instance-01-dev-team         				 postgres       available      

Which ones do you want to delete?
	Comma separated. e.g.: 0,1,2,5
	'all' to delete all (except ones with 'deleting' status)
all


Deleting Instance: example-inst0

Response:{'DBInstance': {'DBInstanceIdentifier': 'example-inst0', 'DBInstanceClass': 'db.r5.xlarge', 'Engine': 'postgres', 'DBInstanceStatus': 'deleting', ...


Deleting Instance: example-mariaDB-instance-00-dev-team

Response:{'DBInstance': {'DBInstanceIdentifier': 'example-mariaDB-instance-00-dev-team', 'DBInstanceClass': 'db.r5.xlarge', 'Engine': 'mariadb', 'DBInstanceStatus': 'deleting', ...


Deleting Instance: example-mariaDB-instance-01-dev-team

Response:{'DBInstance': {'DBInstanceIdentifier': 'example-mariaDB-instance-01-dev-team', 'DBInstanceClass': 'db.r5.xlarge', 'Engine': 'mariadb', 'DBInstanceStatus': 'deleting', ...


Deleting Instance: example-mySQL-instance-00-dev-team

Response:{'DBInstance': {'DBInstanceIdentifier': 'example-mySQL-instance-00-dev-team', 'DBInstanceClass': 'db.r5.xlarge', 'Engine': 'mysql', 'DBInstanceStatus': 'deleting', ...


Deleting Instance: example-mySQL-instance-01-dev-team

Response:{'DBInstance': {'DBInstanceIdentifier': 'example-mySQL-instance-01-dev-team', 'DBInstanceClass': 'db.r5.xlarge', 'Engine': 'mysql', 'DBInstanceStatus': 'deleting', ...


Deleting Instance: example-postgres-instance-00-dev-team

Response:{'DBInstance': {'DBInstanceIdentifier': 'example-postgres-instance-00-dev-team', 'DBInstanceClass': 'db.r5.xlarge', 'Engine': 'postgres', 'DBInstanceStatus': 'deleting', ...


Deleting Instance: example-postgres-instance-01-dev-team

Response:{'DBInstance': {'DBInstanceIdentifier': 'example-postgres-instance-01-dev-team', 'DBInstanceClass': 'db.r5.xlarge', 'Engine': 'postgres', 'DBInstanceStatus': 'deleting', ...



INSTANCES STATUS (ID's don't need to match at this point):


ID   DBId                                                        Engine         Status         
0    example-inst0                                               postgres       deleting       
1    example-mariaDB-instance-00-dev-team          				 mariadb        deleting       
2    example-mariaDB-instance-01-dev-team          				 mariadb        deleting       
3    example-mySQL-instance-00-dev-team            				 mysql          deleting       
4    example-mySQL-instance-01-dev-team            				 mysql          deleting       
5    example-postgres-instance-00-dev-team         				 postgres       deleting       
6    example-postgres-instance-01-dev-team         				 postgres       deleting   
```
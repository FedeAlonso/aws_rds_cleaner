# AWS RDS Cleaner
Python project to interactively delete our AWS RDS instances.
## Before Running
### Environment variables
Export the following environment variables:

    export AWS_RDS_REGION="<AWS REGION>"
    export AWS_RDS_ADMIN_ACCESS_KEY="<AWS  access  key>"
    export AWS_RDS_ADMIN_ACCESS_SECRET="<AWS  access  secret>"

### Dependencies
Install the dependencies located in the requirements file:

    pip install -r requirements.txt
 
## Execution:

	python rds_cleaner.py

### Output example:

    $ python rds_cleaner.py 
    
    You have the following instances:
    
    ID   DBId                                                        Engine         Status         
    0    post-inst01                                                 postgres       available      
    1    post-inst02                                                 postgres       available      
    2    post-inst03                                                 postgres       available      
    3    mariadb-inst03                                              mariadb        available      
    
    
    Which ones do you want to delete?
    	Comma separated. e.g.: 0,1,2,5
    	'all' to delete all (except ones with 'deleting' status)
    all
    
    
    Deleting Instance: post-inst01
    
    Response:{'DBInstance': {'DBInstanceIdentifier': 'post-inst01', 'DBInstanceClass': 'db.t3.micro', 'Engine': 'postgres', ...
    
    
    Deleting Instance: post-inst02
    
    Response:{'DBInstance': {'DBInstanceIdentifier': 'post-inst02', 'DBInstanceClass': 'db.t4g.large', 'Engine': 'postgres', ...
    
    
    Deleting Instance: post-inst03
    
    Response:{'DBInstance': {'DBInstanceIdentifier': 'post-inst03', 'DBInstanceClass': 'db.r5.4xlarge', 'Engine': 'postgres', ...
    
    
    Deleting Instance: mariadb-inst03
    
    Response:{'DBInstance': {'DBInstanceIdentifier': 'mariadb-inst03', 'DBInstanceClass': 'db.t3.micro', 'Engine': 'mariadb', -...
    
    
    
    INSTANCES STATUS (ID's don't need to match at this point):
    
    ID   DBId                                                        Engine         Status         
    0    post-inst01                                                 postgres       deleting      
    1    post-inst02                                                 postgres       deleting      
    2    post-inst03                                                 postgres       deleting      
    3    mariadb-inst03                                              mariadb        deleting
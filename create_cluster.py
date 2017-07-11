# Creates EMR Cluster, be sure to update Ec2KeyName with your correct key
import boto3
import sys

consent = raw_input("This may cost you are you sure you want to run this (Y/N)\n")
if consent.startswith('y'):
    emr = boto3.client('emr')
    response = emr.run_job_flow(
        Name='GHA',
        ReleaseLabel="emr-5.5.0",
        Instances={
            'Ec2KeyName': sys.argv[1],
            'KeepJobFlowAliveWhenNoSteps': True,
            'TerminationProtected': False,
            'InstanceGroups': [
                {
                    'InstanceCount': 1,
                    'InstanceRole': 'MASTER',
                    'InstanceType': 'r3.xlarge',
                    'Name': 'Master'
                },
                {
                    'InstanceCount': 20,
                    'InstanceRole': 'CORE',
                    'Market': 'SPOT',
                    'BidPrice': '.5',
                    'InstanceType': 'i2.2xlarge',
                    'Name': 'Core',
                },
            ],
        },
        JobFlowRole='EMR_EC2_DefaultRole',
        ServiceRole='EMR_DefaultRole',
        VisibleToAllUsers=True,
        Applications=[
            {'Name': 'Hadoop'},
            {'Name': 'Hive'},
            {'Name': 'Spark'},
        ])

    print(response)
else:
    print('Closing.')

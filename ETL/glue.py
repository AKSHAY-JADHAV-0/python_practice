import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as SqlFuncs

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Relational DB
RelationalDB_node1738059169641 = glueContext.create_dynamic_frame.from_options(
    connection_type = "mysql",
    connection_options = {
        "useConnectionProperties": "true",
        "dbtable": "contacts",
        "connectionName": "Mysql connection",
    },
    transformation_ctx = "RelationalDB_node1738059169641"
)

# Script generated for node Drop Duplicates
DropDuplicates_node1738060192063 =  DynamicFrame.fromDF(RelationalDB_node1738059169641.toDF().dropDuplicates(), glueContext, "DropDuplicates_node1738060192063")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=DropDuplicates_node1738060192063, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1738059153618", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1738060514843 = glueContext.write_dynamic_frame.from_options(frame=DropDuplicates_node1738060192063, connection_type="s3", format="glueparquet", connection_options={"path": "s3://contactapp-01/raw_data/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1738060514843")

job.commit()
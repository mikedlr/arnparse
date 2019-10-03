from hypothesis import given
from hypothesis.strategies import sampled_from

from arnparse import arnparse

# ARN examples from https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md
# under Apache2 license

arn_examples = (
    "arn:aws:serverlessrepo:us-east-1:012345678901:applications/my-application",
    "arn:aws:sns:us-east-1:123456789012:my_topic",
    "arn:aws:kinesis:us-east-1:123456789012:stream/my-stream",
    "arn:aws:dynamodb:us-east-1:123456789012:table/TestTable/stream/2016-08-11T21:21:33.291",
    "arn:aws:sqs:us-west-2:012345678901:my-queu",
    "arn:aws:serverlessrepo:us-east-1:012345678901:applications/my-application",
    "arn:aws:iam::123456789012:role/S3Access",
    "arn:aws:s3:::my-bucket/*",
)

@given(sampled_from(arn_examples))
def test_arn_to_string(arn):
    assert str(arnparse(arn)) == arn

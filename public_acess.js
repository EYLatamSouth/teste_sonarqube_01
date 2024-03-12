import { aws_iam as iam } from 'aws-cdk-lib'
import { aws_s3 as s3 } from 'aws-cdk-lib'

const bucket = new s3.Bucket(this, "ExampleBucket")

bucket.addToResourcePolicy(new iam.PolicyStatement({
    effect: iam.Effect.ALLOW,
    actions: ["s3:*"],
    resources: [bucket.arnForObjects("*")],
    principals: [new iam.AnyPrincipal()] // Sensitive! This policy allows all users, including anonymous ones, to access an S3 bucket:
}))

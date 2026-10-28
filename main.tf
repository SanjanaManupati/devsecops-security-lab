
# DevSecOps lab: intentionally insecure example for scanner testing.
# Do not use this configuration for real infrastructure.

resource "aws_s3_bucket" "lab_bucket" {
  bucket = "devsecops-lab-demo-bucket-12345"

  tags = {
    Name        = "DevSecOps Lab"
    Environment = "Testing"
  }
}

resource "aws_s3_bucket_public_access_block" "lab_bucket_access" {
  bucket = aws_s3_bucket.lab_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

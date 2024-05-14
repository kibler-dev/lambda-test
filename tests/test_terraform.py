import unittest
import subprocess

class TestTerraformConfiguration(unittest.TestCase):
    def test_terraform_plan(self):
        result = subprocess.run(["terraform", "-chdir=./terraform", "plan"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode("utf-8")
        self.assertIn("Plan:", output)
        self.assertIn("aws_iam_role.lambda_role", output)
        self.assertIn("aws_iam_policy.lambda_logging_policy", output)
        self.assertIn("aws_lambda_function.hello_world_lambda", output)

    def test_terraform_apply(self):
        result = subprocess.run(["terraform", "-chdir=./terraform", "apply", "-auto-approve"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode("utf-8")
        self.assertIn("Apply complete!", output)

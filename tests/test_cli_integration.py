"""
Integration Tests - CLI + Calculator Working Together
"""

import subprocess
import sys
import os


class TestCLIIntegration:
    """Test CLI application integrating with calculator module"""

    def run_cli(self, *args):
        """
        Run the CLI script directly (python src/cli.py ...) so tests don't
        require src to be a package. Returns subprocess.CompletedProcess.
        """
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        script_path = os.path.join(project_root, "src", "cli.py")
        # run from project root so relative imports inside src work
        result = subprocess.run(
            [sys.executable, script_path] + list(args),
            capture_output=True,
            text=True,
            cwd=project_root,
        )
        return result

    def test_cli_add_integration(self):
        """Test CLI can perform addition"""
        result = self.run_cli("add", "5", "3")
        assert (
            result.returncode == 0
        ), f"Exit {result.returncode}. stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        assert (
            result.stdout.strip() == "8"
        ), f"Unexpected stdout: {result.stdout!r}\nstderr: {result.stderr!r}"

    def test_cli_subtract_integration(self):
        """Test CLI can perform subtraction"""
        result = self.run_cli("subtract", "5", "3")
        assert (
            result.returncode == 0
        ), f"Exit {result.returncode}. stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        assert (
            result.stdout.strip() == "2"
        ), f"Unexpected stdout: {result.stdout!r}\nstderr: {result.stderr!r}"

    def test_cli_subtract_missing_operand_error(self):
        """
        Test CLI handles missing operand for subtraction gracefully.
        Click prints error to stderr and exits non-zero.
        """
        result = self.run_cli("subtract", "5")  # missing second operand
        assert (
            result.returncode != 0
        ), f"Expected non-zero exit for missing operand; got 0. stdout:{result.stdout}"
        stderr = (result.stderr or "").lower()
        assert (
            ("usage" in stderr)
            or ("error" in stderr)
            or ("missing" in stderr)
            or ("required" in stderr)
        ), f"stderr did not contain expected error text. stderr:\n{result.stderr}\nstdout:\n{result.stdout}"

    def test_cli_multiply_integration(self):
        """Test CLI can perform multiplication"""
        result = self.run_cli("multiply", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "15"

    def test_cli_divide_integration(self):
        """Test CLI can perform division"""
        result = self.run_cli("divide", "5", "3")
        assert result.returncode == 0
        # Expecting rounded output from CLI formatting
        assert result.stdout.strip() == "1.67"

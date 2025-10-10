"""
Integration Tests - CLI + Calculator Working Together
"""
import subprocess
import sys
import pytest

class TestCLIIntegration:
    """Test CLI application integrating with calculator module"""

    def run_cli(self, *args):
        """
        Helper method to run CLI and capture output.
        Uses `python -m src.cli` which is robust whether src is a package
        or a direct script file.
        """
        cmd = [sys.executable, "-m", "src.cli"] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        return result

    def test_cli_add_integration(self):
        """Test CLI can perform addition"""
        result = self.run_cli("add", "5", "3")
        assert result.returncode == 0
        # result of add should be printed to stdout
        assert result.stdout.strip() == "8"

    def test_cli_subtract_integration(self):
        """Test CLI can perform subtraction (command name: sub)"""
        result = self.run_cli("sub", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "2"

    def test_cli_subtract_missing_operand_error(self):
        """
        Test CLI handles missing operand for subtraction gracefully.
        Argparse will normally emit a message to stderr and exit with a
        non-zero status (commonly 2). We assert non-zero and check stderr.
        """
        result = self.run_cli("sub", "5")  # missing second operand
        assert result.returncode != 0, "Expected non-zero exit for missing operand"
        # argparse prints usage / error messages to stderr — check it contains 'usage' or 'error'
        stderr = (result.stderr or "").lower()
        assert ("usage" in stderr) or ("error" in stderr) or ("the following arguments are required" in stderr)

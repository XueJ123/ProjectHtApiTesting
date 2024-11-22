import unittest
import os
import time
import shutil
import sys
import traceback


class HTMLTestRunner:
    """
    A class to run tests and generate an HTML report
    """

    def __init__(self, stream=sys.stdout, title=None, description=None, verbosity=1):
        self.stream = stream
        self.title = title or "Test Report"
        self.description = description or "Test Results"
        self.verbosity = verbosity

    def run(self, test):
        result = self._makeResult()
        test(result)
        self._generateReport(result)
        return result

    def _makeResult(self):
        return _HTMLTestResult(self.stream, self.title, self.description, self.verbosity)

    def _generateReport(self, result):
        # HTML report structure
        now = time.strftime("%Y-%m-%d_%H-%M-%S")
        report_file = "test_report_" + now + ".html"

        with open(report_file, "w") as f:
            f.write(self._getHTMLHeader())
            f.write(self._getHTMLTestResults(result))
            f.write(self._getHTMLFooter())

        print(f"HTML report generated: {os.path.abspath(report_file)}")

    def _getHTMLHeader(self):
        return f"""
        <html>
        <head>
            <title>{self.title}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                th, td {{
                    padding: 10px;
                    border: 1px solid #ddd;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                .pass {{
                    background-color: #d4edda;
                }}
                .fail {{
                    background-color: #f8d7da;
                }}
            </style>
        </head>
        <body>
            <h1>{self.title}</h1>
            <p>{self.description}</p>
            <table>
                <tr>
                    <th>Test Case</th>
                    <th>Status</th>
                    <th>Time (s)</th>
                    <th>Details</th>
                </tr>
        """

    def _getHTMLTestResults(self, result):
        html = ""
        for test_case, outcome in result.results:
            status = "PASS" if outcome == "success" else "FAIL"
            status_class = "pass" if outcome == "success" else "fail"
            duration = round(result.time_taken[test_case], 2)
            details = result.details.get(test_case, "No additional details.")

            html += f"""
            <tr class="{status_class}">
                <td>{test_case}</td>
                <td>{status}</td>
                <td>{duration}</td>
                <td>{details}</td>
            </tr>
            """
        return html

    def _getHTMLFooter(self):
        return """
        </table>
        </body>
        </html>
        """


class _HTMLTestResult:
    """
    A custom result class to track test results and durations
    """

    def __init__(self, stream, title, description, verbosity):
        self.stream = stream
        self.title = title
        self.description = description
        self.verbosity = verbosity
        self.results = []
        self.time_taken = {}
        self.details = {}

    def startTest(self, test):
        self.current_test = test
        self.start_time = time.time()

    def addSuccess(self, test):
        self._addResult(test, "success")

    def addFailure(self, test, err):
        self._addResult(test, "failure", str(err))

    def addError(self, test, err):
        self._addResult(test, "error", str(err))

    def _addResult(self, test, outcome, details=""):
        duration = round(time.time() - self.start_time, 2)
        self.results.append((str(test), outcome))
        self.time_taken[str(test)] = duration
        self.details[str(test)] = details


if __name__ == "__main__":
    # Simple example usage
    import unittest
    from some_test_module import APITest  # Replace with your actual test module

    # Configure the test runner
    runner = HTMLTestRunner(title="API Test Report", description="Test results for API endpoints.")

    # Load and run the tests
    suite = unittest.TestLoader().loadTestsFromTestCase(APITest)
    runner.run(suite)

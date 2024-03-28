import subprocess

def run_tests():
    result = subprocess.run(['python', '-m', 'unittest', 'discover', '-s', 'tests/modules/clients', '-p', 'test_*.py'])
    return result.returncode

if __name__ == "__main__":
    exit_code = run_tests()
    exit(exit_code)

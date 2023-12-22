import subprocess

def commit(message):
    try:
        subprocess.run(["git", "add", "."])
        # Run the git commit command with the provided message
        subprocess.run(["git", "commit", "-m", message])
        print("Git commit successful")
    except Exception as e:
        print(f"Git commit failed: {e}")
    

def run(options):
    commit(options["message"])

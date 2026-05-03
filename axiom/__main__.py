import sys
import os
import subprocess

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"

    if cmd == "init":
        root = os.path.dirname(os.path.dirname(__file__))
        subprocess.run(["bash", os.path.join(root, "scripts", "setup.sh")], check=True)
        return

    # All other commands require initialisation
    import axiom  # triggers RuntimeError if not initialised

    if cmd == "deploy":
        print("Deploying...")
    elif cmd == "status":
        print("Status: ok")
    else:
        print("Usage: python -m axiom <init|deploy|status>")

if __name__ == "__main__":
    main()

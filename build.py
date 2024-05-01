import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Usage: python build.py --r")
        print("       python build.py --dj")
        return

    command = sys.argv[1]

    if command == "--r":
        subprocess.run(["cargo", "new", "my_project"], check=True)
        print("Rust project created.")
    elif command == "--dj":
        subprocess.run(["django-admin", "startproject", "my_project"], check=True)
        print("Django project created.")
    elif command == "--ex":
        subprocess.run(["npx", "express-generator", "my_project"], check=True)
        print("Express project created.")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()

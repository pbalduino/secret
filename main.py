import os
import sys

def main():
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    if username is None or password is None:
        print("Error: USERNAME and PASSWORD environment variables must be set.", file=sys.stderr)
        sys.exit(1)

    print(f"USERNAME: {username}")
    print(f"PASSWORD: {password}")

if __name__ == "__main__":
    main()
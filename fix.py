import os
import sys
import subprocess


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <patch_directory>")
        sys.exit(1)

    directory = sys.argv[1]
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".patch"):
            patch_path = os.path.join(directory, filename)
            print(f"Applying {filename}")
            subprocess.run(["git", "apply", patch_path], check=True)


if __name__ == "__main__":
    main()

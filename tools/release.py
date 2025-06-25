import re
import subprocess
from pathlib import Path

def get_version_from_pyproject(pyproject_path="pyproject.toml"):
    pyproject = Path(pyproject_path).read_text(encoding="utf-8")
    match = re.search(r'version\s*=\s*"([\d\.]+)"', pyproject)
    return match.group(1) if match else None

def run(cmd):
    print(f"> {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print("❌ Command failed.")
        exit(1)

def tag_and_push(version):
    tag = f"v{version}"
    print(f"📦 Preparing release: {tag}")

    # Check if tag already exists
    tags = subprocess.run("git tag", shell=True, capture_output=True, text=True).stdout.splitlines()
    if tag in tags:
        print(f"❌ Tag {tag} already exists. Please delete it first if you want to recreate.")
        exit(1)

    run("git add pyproject.toml")
    run(f'git commit -m "Release version {version}"')
    run(f"git tag {tag}")
    run("git push")
    run(f"git push origin {tag}")

    print(f"\n✅ Tag {tag} created and pushed.")
    print("\n📝 Changelog suggestion:")
    print(f"## {tag} — {Path.cwd().name}")
    print(f"- Version: {version}")
    print("- ✨ Summary of changes:")
    print("  - ... (add your features here)\n")

if __name__ == "__main__":
    version = get_version_from_pyproject()
    if not version:
        print("❌ Could not find version in pyproject.toml")
        exit(1)
    tag_and_push(version)
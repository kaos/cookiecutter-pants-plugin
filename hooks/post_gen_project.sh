#!/usr/bin/env bash
set -euf

# Fetch bootstrap script
echo " * Downloading pants bootstrap script..."
curl -L -O --silent https://static.pantsbuild.org/setup/pants
chmod +x ./pants

# Smoke test
echo " * Smoke test..."
./pants --version

# Create pants.lock
echo " * Creating initial pants.lock..."
./pants generate-lockfiles --resolve=3rdparty-deps

echo
echo " == All Done! =="
echo

#!/bin/bash
# verify-issues.sh
# Script to verify that issues were created by create-epic.py

set -e

REPO="${1:-wclaytor/alpine-beats}"
LABEL="${2:-test}"

echo "🔍 Verifying issues in repository: $REPO"
echo "📋 Filtering by label: $LABEL"
echo ""

# Check if gh is installed and authenticated
if ! command -v gh &> /dev/null; then
    echo "❌ Error: gh CLI is not installed"
    echo "Please install it from: https://cli.github.com/"
    exit 1
fi

if ! gh auth status &> /dev/null; then
    echo "❌ Error: gh CLI is not authenticated"
    echo "Please run: gh auth login"
    exit 1
fi

echo "✅ gh CLI is authenticated"
echo ""

# List issues with the specified label
echo "📝 Issues with label '$LABEL':"
echo "================================"
gh issue list --repo "$REPO" --label "$LABEL" --limit 20 --state all

echo ""
echo "📊 Summary:"
echo "================================"

# Count open issues with the label
OPEN_COUNT=$(gh issue list --repo "$REPO" --label "$LABEL" --state open --json number --jq '. | length' 2>/dev/null || echo "0")
echo "Open issues with '$LABEL' label: $OPEN_COUNT"

# Count closed issues with the label
CLOSED_COUNT=$(gh issue list --repo "$REPO" --label "$LABEL" --state closed --json number --jq '. | length' 2>/dev/null || echo "0")
echo "Closed issues with '$LABEL' label: $CLOSED_COUNT"

echo ""
echo "💡 To view a specific issue:"
echo "   gh issue view <issue-number> --repo $REPO"
echo ""
echo "💡 To list all issues (no label filter):"
echo "   gh issue list --repo $REPO --limit 20"

#!/bin/bash

# Quick runner script for Demo 1
# Usage: ./run_demo1.sh

echo "🚀 PyCon NG 2025 - AutoGen Demo 1: Content Creation Pipeline"
echo ""

# Check if Poetry is available
if ! command -v poetry &> /dev/null; then
    echo "❌ Poetry not found. Please install it first:"
    echo "   curl -sSL https://install.python-poetry.org | python3 -"
    exit 1
fi

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file not found"
    echo "   Creating from .env.example..."
    if [ -f .env.example ]; then
        cp .env.example .env
        echo "   ✓ Created .env - Please edit it with your API key"
        echo ""
        read -p "Press Enter after adding your API key to .env..."
    else
        echo "   ❌ .env.example not found either"
        echo "   Please create .env with OPENAI_API_KEY=your_key"
        exit 1
    fi
fi

echo "📦 Installing dependencies (if needed)..."
poetry install --no-interaction

echo ""
echo "🎬 Starting Demo 1..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

poetry run python demo1_content_pipeline/main.py

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Demo completed!"
echo ""
echo "💡 Tips:"
echo "   • Change DEMO_TOPIC in demo1_content_pipeline/main.py"
echo "   • Try different content types (tutorial, documentation, email)"
echo "   • Check demo1_content_pipeline/README.md for more options"
echo ""


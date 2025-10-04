"""
Quick setup test for Demo 1
Run this to verify everything is configured correctly.
"""

import sys
import os


def test_imports():
    """Test that all required packages are installed."""
    print("Testing imports...")

    try:
        import autogen

        print("  ✓ autogen")
    except ImportError:
        print("  ✗ autogen - Run: poetry install")
        return False

    try:
        from dotenv import load_dotenv

        print("  ✓ python-dotenv")
    except ImportError:
        print("  ✗ python-dotenv - Run: poetry install")
        return False

    try:
        from termcolor import colored

        print("  ✓ termcolor")
    except ImportError:
        print("  ✗ termcolor - Run: poetry install")
        return False

    return True


def test_env():
    """Test that environment is configured."""
    print("\nTesting environment...")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("  ⚠  OPENAI_API_KEY not set")
        print("     Create .env file with your API key")
        return False
    elif api_key == "your_openai_api_key_here":
        print("  ⚠  OPENAI_API_KEY is placeholder value")
        print("     Update .env with your actual API key")
        return False
    else:
        print(f"  ✓ OPENAI_API_KEY set ({api_key[:8]}...)")

    model = os.getenv("MODEL_NAME", "gpt-4")
    print(f"  ✓ MODEL_NAME: {model}")

    return True


def test_tools():
    """Test that tools can be imported."""
    print("\nTesting tools...")

    try:
        from tools.knowledge_tools import search_knowledge_base, get_writing_guidelines

        print("  ✓ Tools imported successfully")

        # Test a simple query
        result = search_knowledge_base("python asyncio")
        if result.get("success"):
            print(f"  ✓ Knowledge base working - found '{result['data']['title']}'")
        else:
            print("  ✗ Knowledge base query failed")
            return False

        # Test guidelines
        guidelines = get_writing_guidelines("technical_blog")
        if guidelines.get("success"):
            print("  ✓ Writing guidelines working")
        else:
            print("  ✗ Writing guidelines query failed")
            return False

    except ImportError as e:
        print(f"  ✗ Failed to import tools: {e}")
        return False
    except Exception as e:
        print(f"  ✗ Tool test failed: {e}")
        return False

    return True


def test_agents():
    """Test that agents can be created."""
    print("\nTesting agent creation...")

    try:
        from agents import (
            create_planner_agent,
            create_researcher_agent,
            create_writer_agent,
            create_critic_agent,
        )

        print("  ✓ Agent modules imported")

        # Note: We don't actually create agents here as that would require valid API config
        print("  ✓ Agent creation functions available")

    except ImportError as e:
        print(f"  ✗ Failed to import agents: {e}")
        return False

    return True


def main():
    """Run all tests."""
    print("=" * 60)
    print("  Demo 1 Setup Test")
    print("=" * 60)
    print()

    # Load environment
    from dotenv import load_dotenv

    load_dotenv()

    results = []

    results.append(("Imports", test_imports()))
    results.append(("Environment", test_env()))
    results.append(("Tools", test_tools()))
    results.append(("Agents", test_agents()))

    print("\n" + "=" * 60)
    print("  Test Results")
    print("=" * 60)
    print()

    all_passed = all(result for _, result in results)

    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {status}: {name}")

    print()

    if all_passed:
        print("🎉 All tests passed! You're ready to run the demo.")
        print()
        print("Run the demo with:")
        print("  poetry run python demo1_content_pipeline/main.py")
        print()
        return 0
    else:
        print("⚠️  Some tests failed. Please fix the issues above.")
        print()
        return 1


if __name__ == "__main__":
    sys.exit(main())

"""
Automated test script for Adventure Game
Tests multiple game paths with predefined inputs
"""

import subprocess
import sys

def run_test(test_name, inputs):
    """Run a test with predefined inputs"""
    print(f"\n{'='*60}")
    print(f"TEST: {test_name}")
    print('='*60)
    
    # Create a string of inputs separated by newlines
    input_string = '\n'.join(inputs)
    
    # Run the game with inputs piped in
    process = subprocess.Popen(
        [sys.executable, "Adventure_game.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    stdout, stderr = process.communicate(input=input_string)
    print(stdout)
    
    if stderr:
        print("ERRORS:", stderr)
    
    return process.returncode

# Test scenarios
tests = [
    {
        "name": "Test 1: Forest -> River -> Swim -> Continue -> Enter Cave -> Win",
        "inputs": ["Adventurer1", "forest", "cross the river", "swim across", "keep swimming", "enter cave"]
    },
    {
        "name": "Test 2: Forest -> Tree -> Grab Branch -> Follow Path -> Talk to Old Man -> Win",
        "inputs": ["Adventurer2", "forest", "climb tree", "grab", "follow path", "talk"]
    },
    {
        "name": "Test 3: Cave -> Explore -> Continue Cautiously -> Win",
        "inputs": ["Adventurer3", "cave", "explore deeper", "continue"]
    },
    {
        "name": "Test 4: Forest -> River -> Raft -> Paddle -> Continue -> Enter Cave -> Win",
        "inputs": ["Adventurer4", "forest", "cross river", "raft", "paddle", "continue", "enter cave"]
    },
    {
        "name": "Test 5: Forest -> Tree -> Jump Down -> Fail (Twisted Ankle)",
        "inputs": ["Adventurer5", "forest", "climb tree", "jump"]
    },
    {
        "name": "Test 6: Cave -> Explore -> Turn Back -> Escape",
        "inputs": ["Adventurer6", "cave", "explore deeper", "turn back"]
    },
    {
        "name": "Test 7: Forest -> River -> Raft -> Fix Leak -> Fail (Raft Sinks)",
        "inputs": ["Adventurer7", "forest", "cross river", "raft", "fix"]
    },
    {
        "name": "Test 8: Forest -> Tree -> Grab -> Follow Path -> Ignore Old Man -> Get Lost",
        "inputs": ["Adventurer8", "forest", "climb tree", "grab", "follow path", "ignore"]
    },
    {
        "name": "Test 9: Forest -> River -> Swim -> Turn Back -> Exhausted",
        "inputs": ["Adventurer9", "forest", "cross river", "swim", "turn back"]
    },
    {
        "name": "Test 10: Quit at Start",
        "inputs": ["q"]
    }
]

# Run all tests
print("\n" + "="*60)
print("ADVENTURE GAME AUTOMATED TEST SUITE")
print("="*60)

for test in tests:
    run_test(test["name"], test["inputs"])

print("\n" + "="*60)
print("ALL TESTS COMPLETED")
print("="*60)

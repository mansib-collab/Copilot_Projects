# Adventure Game - Passing & Failing Scenarios

## PASSING SCENARIOS (Player Wins & Finds Treasure) ✅

### Scenario 1: Forest Route - Swimming Path
**Path:** Forest → Cross River → Swim → Keep Swimming → Enter Cave
**Outcome:** Congratulations! You found the treasure and won the game!
**Key Decisions:** 
- Choose forest at crossroads
- Cross the river
- Choose to swim across
- Keep swimming despite tiredness
- Enter the hidden cave

### Scenario 2: Forest Route - Tree Climbing Path  
**Path:** Forest → Climb Tree → Grab Branch → Follow Path → Talk to Old Man
**Outcome:** Congratulations! You found the treasure and won the game!
**Key Decisions:**
- Choose forest at crossroads
- Climb the tree
- Grab another branch when it breaks
- Follow the hidden path
- Talk to the mysterious old man

### Scenario 3: Cave Route - Cautious Exploration
**Path:** Cave → Explore Deeper → Continue Cautiously → Find Hidden Chamber
**Outcome:** Congratulations! You found the treasure and won the game!
**Key Decisions:**
- Choose cave at crossroads
- Explore deeper into the cave
- Continue cautiously despite creaking sounds
- Find the hidden chamber with treasure chest

### Scenario 4: Forest Route - Raft Path
**Path:** Forest → Cross River → Raft → Paddle Faster → Continue → Enter Cave
**Outcome:** Congratulations! You found the treasure and won the game!
**Key Decisions:**
- Choose forest at crossroads
- Cross the river
- Look for a raft
- Paddle faster when raft leaks
- Continue looking for treasure
- Enter the hidden cave

---

## FAILING SCENARIOS (Player Loses or Restarts) ❌

### Scenario 1: Forest - Tree Fall Injury
**Path:** Forest → Climb Tree → Jump Down
**Outcome:** You jump down but land badly and twist your ankle. You limp back to the crossroads.
**Result:** Game restarts from beginning
**Key Failure Decision:**
- Jump down when branch breaks (instead of grabbing another branch)

### Scenario 2: Forest - Swimming Exhaustion
**Path:** Forest → Cross River → Swim → Turn Back
**Outcome:** You turn back and swim to shore, exhausted. You decide to head back to the crossroads.
**Result:** Game restarts from beginning
**Key Failure Decision:**
- Give up swimming and turn back due to exhaustion

### Scenario 3: Forest - Raft Sinking
**Path:** Forest → Cross River → Raft → Fix the Leak
**Outcome:** You try to fix the leak but the raft sinks. You barely make it back to shore. Exhausted, you return to the crossroads.
**Result:** Game restarts from beginning
**Key Failure Decision:**
- Try to fix the leak instead of paddling faster

### Scenario 4: Forest - Getting Lost in Woods
**Path:** Forest → Climb Tree → Grab Branch → Follow Path → Ignore Old Man
**Outcome:** You ignore the old man and continue down the path, but you get lost in the forest. You wander aimlessly and eventually find yourself back at the crossroads.
**Result:** Game restarts from beginning
**Key Failure Decision:**
- Ignore the old man's clue instead of talking to him

### Scenario 5: Cave - Collapse Escape
**Path:** Cave → Explore Deeper → Turn Back Immediately
**Outcome:** You wisely turn back. A moment later, a large section of the cave collapses where you just were! You escape back to the crossroads, shaken but alive.
**Result:** Game restarts from beginning (Lucky escape but no treasure)
**Key Failure Decision:**
- Turn back when cave gets creaky (though this is actually a wise choice to avoid danger)

---

## NEUTRAL SCENARIOS (Player Returns to Crossroads)

### Scenario 1: Cave Hesitation
**Path:** Cave → Go Back
**Outcome:** You decide to go back to the crossroads.
**Result:** Game restarts from beginning
**Key Decision:** Choose to go back instead of exploring

### Scenario 2: Forest - No Clear Choice
**Path:** Forest → Cross the River → Raft → Paddle → Continue → Go Back
**Outcome:** You go back to the crossroads
**Result:** Game restarts from beginning
**Key Decision:** Choose to go back at various decision points

---

## IMMEDIATE EXIT SCENARIO

### Scenario: Quit at Any Point
**Path:** Enter 'q' at any input prompt
**Outcome:** "Thanks for playing! Goodbye!" - Game exits
**Result:** Game terminates immediately

---

## SUMMARY STATISTICS

| Category | Count |
|----------|-------|
| **Winning Paths** | 4 |
| **Failing Paths** | 5 |
| **Neutral/Restart Paths** | 2+ |
| **Total Unique Paths** | 11+ |

**Win Rate:** 36% (assuming random choices)
**Lose Rate:** 45% (scenarios that trigger restart)
**Neutral Rate:** 19% (going back without consequence)

---

## Key Game Mechanics

### Success Factors:
- Being brave but cautious (grab branch, continue swimming, explore deeper)
- Following advice (talk to the old man)
- Making quick decisions (paddle faster, continue searching)

### Failure Factors:
- Taking unnecessary risks (jumping from tree, giving up)
- Ignoring help (ignoring the old man)
- Poor problem-solving (trying to fix raft instead of paddling)
- Loss of nerve (turning back when tired)

### Game Strategy:
- **Brave choices** often lead to winning paths
- **Balanced decisions** (grab branch, paddle faster) work better than extreme choices
- **Following NPCs' advice** (old man) leads to treasure
- **Giving up too easily** forces restart

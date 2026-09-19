# Crisis Intelligence Pipeline

# 1. Project එකේ Engineering View එක

මෙම project එක prompt engineering exercise එකක් පමණක් නොවේ.  
ඇත්තටම මෙය **small AI system design exercise** එකක්.

Project එකේ engineering flow එක මෙහෙම බලන්න පුළුවන්:

```text
Raw Input
   ↓
Prompt / Model Interaction
   ↓
Model Output
   ↓
Validation / Guardrails
   ↓
Structured Data
   ↓
Decision / Report / Export
```

මට මෙහිදී වැදගත්ම lesson එක වූයේ:

> **LLM එක system එකේ එක component එකක් පමණි. System එක reliable වෙන්නේ prompt එක නිසා විතරක් නොව, validation, constraints, data contracts, configuration, error handling සහ observability නිසාය.**

---

# 2. AI Engineering Problem එකක් හිතන Framework එක

ඕනෑම AI feature එකක් build කිරීමට පෙර මම දැන් මේ ප්‍රශ්න අහනවා:

## 2.1 Input එක මොකක්ද?

- free text ද?
- structured data ද?
- noisy user input ද?
- long text ද?
- real-time feed ද?

## 2.2 Output එක මොකක්ද?

- human-readable answer එකක් ද?
- fixed classification label එකක් ද?
- JSON object එකක් ද?
- score එකක් ද?
- route/decision එකක් ද?
- Excel/report එකක් ද?

## 2.3 Model එකට freedom කොච්චර දෙන්නද?

- creative task නම් freedom වැඩි කළ හැක.
- classification / extraction / emergency decision වගේ tasks නම් freedom අඩු කළ යුතුය.

## 2.4 Invalid output එකක් ආවොත්?

- reject කරන්නද?
- retry කරන්නද?
- fallback model එකකට යවන්නද?
- human review එකකට යවන්නද?
- “Unknown” කියලා safe value එකක් දෙන්නද?

## 2.5 Missing information තිබ්බොත්?

- infer කරන්නද?
- derive කරන්නද?
- “Unknown” return කරන්නද?
- userගෙන් clarification ගන්නද?

## 2.6 System quality measure කරන්නේ කොහොමද?

- accuracy
- consistency
- hallucination rate
- latency
- token cost
- schema validation rate
- invalid output rate

මෙම project එකේ parts 1–5 තුළ මේ ප්‍රශ්න වෙන වෙනම practically encounter කළෙමි.

---

# 3. Part 1 – Crisis Message Classification

## 3.1 Engineering Problem

Raw crisis messages එකම format එකකින් නොඑයි.

උදාහරණ:

```text
"SOS: 5 people trapped..."
"Need water in Gampaha"
"Breaking News: river level..."
"Thanks to everyone helping..."
```

System එකට මේවා machine-friendly categories වලට convert කරන්න අවශ්‍ය විය:

```text
District
Intent
Priority
```

මෙහි engineering challenge එක:

> **Unstructured human language → structured decision label**

---

## 3.2 Few-Shot Prompting ඇයි?

Model එකට:

```text
Classify this message.
```

කියලා කියන එක technically possible.

නමුත් expected behavior clear නැහැ.

Few-shot examples දීමෙන් model එකට implicit specification එකක් ලැබෙනවා:

```text
Example input
→ expected output

Example input
→ expected output
```

මෙය software engineering වල test cases වගේ හිතන්න පුළුවන්.

### Engineering insight

Few-shot examples කියන්නේ model එකට “sample behavior contract” එකක්.

Traditional code එකේ:

```python
if rescue:
    priority = "High"
```

වගේ logic තිබෙන තැන, LLM task එකේ examples මඟින් behavior shape කරනවා.

---

## 3.3 Output Contract එකේ වැදගත්කම

අපි output එක:

```text
District: [Name] | Intent: [Category] | Priority: [High/Low]
```

කියලා restrict කළා.

මෙය වැදගත් වුණේ downstream code එකට output parse කරන්න පුළුවන් නිසා.

### Bad engineering

```text
The user appears to need rescue and is probably in Gampaha.
```

මෙවැනි output එක human-readable වුවත් machine integration එකට අමාරුයි.

### Better engineering

```text
District: Gampaha | Intent: Rescue | Priority: High
```

මෙය deterministic parser එකකට easy.

---

## 3.4 Validation එක ඇයි?

Model output එක always trust කළොත්:

```text
Intent: Emergency
```

වගේ unsupported category එකක් එන්න පුළුවන්.

ඒ නිසා parser එකේ:

```text
Intent must be one of:
Rescue, Supply, Info, Other
```

කියලා validate කළා.

### Engineering lesson

> **LLM output should be treated as untrusted external input.**

ඒක user input එකක් validate කරනවා වගේම validate කළ යුතුය.

---

## 3.5 Real-world Application

### Customer Support

Messages:

```text
"I cannot login"
"My payment failed"
"I need a refund"
```

Few-shot classification:

```text
Intent: LoginIssue
Intent: PaymentIssue
Intent: Refund
```

### Security Operations

Security alerts classify කළ හැක:

```text
Phishing
Malware
Credential Leak
False Positive
```

### E-commerce

Customer requests:

```text
Return
Delivery Delay
Damaged Product
Product Question
```

### Engineering Thinking

Classification problem එකක් දැක්කාම මම දැන් අහනවා:

```text
1. Categories finite ද?
2. Output strict format එකක් දිය හැකිද?
3. Few-shot examples help කරනවද?
4. Invalid category ආවොත් reject කරන්න පුළුවන්ද?
5. Evaluation dataset එකක් build කරන්න පුළුවන්ද?
```

---

# 4. Part 2 – Temperature Stability Experiment

## 4.1 Engineering Problem

LLM එක deterministic program එකක් නොවේ.

Same input එකට different outputs ලැබිය හැක.

එනිසා critical system එකක ප්‍රශ්නය:

> **Model output stability කොච්චරද?**

---

## 4.2 Temperature කියන්නේ මොකක්ද?

Temperature model එකේ randomness/diversity control කරන parameter එකක්.

සාමාන්‍යයෙන්:

```text
Low temperature
→ more deterministic
→ more consistent

High temperature
→ more diverse
→ more exploratory
→ speculative reasoning වැඩි විය හැක
```

අපි:

```text
temperature = 1.0 → Chaos Mode
temperature = 0.0 → Safe Mode
```

compare කළා.

---

## 4.3 Same Final Answer ≠ Same Reasoning Quality

මෙම experiment එකෙන් වැදගත් observation එකක් ලැබුණා:

Chaos runs වල final priority decision එක Safe Mode එකට සමාන වුණත්, reasoning එකේ:

- unsupported medical timelines
- additional assumptions
- unprovided complications
- speculative details

එන්න පුළුවන්.

### Engineering lesson

Output එකේ final label එක පමණක් evaluate කරන්න එපා.

Evaluate කරන්න:

```text
- factual grounding
- assumptions
- stability
- consistency
- unsupported details
```

---

## 4.4 Real-world Application

### Financial assistant

“Approve / Reject” final result same වුණත් reasoning එක invented financial facts මතද කියලා බලන්න ඕන.

### Legal assistant

Correct-looking answer එකක් unsupported legal citation එකක් සමඟ එන්න පුළුවන්.

### Incident response

Correct priority decision එකක් wrong assumptions මත ගත්තොත් production risk එකක්.

### Engineering Thinking

Critical AI task එකකට:

```text
1. Run repeated tests.
2. Compare outputs.
3. Measure variance.
4. Look for hallucinations.
5. Use lower temperature when consistency matters.
```

---

# 5. Part 3 – Logistics Commander

# 5.1 Step A – CoT Scoring

## Engineering Problem

Incidents multiple criteria මත score කරන්න අවශ්‍ය විය:

```text
Age
Need
Urgency
```

Scoring rules:

```text
Base = 5
+2 age condition
+3 rescue
+1 medicine
```

මෙය rule-based reasoning problem එකක්.

---

## 5.2 CoT Prompt එකේ Engineering Role

CoT prompt එකෙන් model එකට staged procedure එකක් දුන්නා:

```text
1. Base score
2. Check age
3. Check rescue need
4. Check medicine need
5. Sum
6. Return final score
```

මෙය “think step-by-step” කියන vague instruction එකට වඩා හොඳයි.

### Engineering lesson

> **Complex reasoning task එකකට reasoning procedure එක design කිරීම prompt engineering එකේ වැදගත් කොටසක්.**

---

# 5.3 Step B – Tree of Thought

## Engineering Problem

එක route එක generate කරනවා වෙනුවට strategies 3ක් compare කළා:

```text
Branch 1: Highest score first
Branch 2: Closest first
Branch 3: Furthest first
```

මෙය ToT concept එක practically represent කරනවා.

### CoT vs ToT

```text
CoT
→ one reasoning path

ToT
→ multiple candidate strategies
→ compare
→ select
```

---

# 5.4 Structured Handoff Lesson

මුලින් Part A free-text result එක Part B එකට pass කළාම model එක score-area mapping confuse කළා.

උදාහරණ:

```text
Gampaha score එක Ragama ට assign කිරීම
```

එතනින් මම ඉගෙනගත්තේ:

> **Multi-stage AI pipelines වල intermediate output structured data විය යුතුය.**

Better:

```python
{
    "id": "2",
    "area": "Ja-Ela",
    "score": 8
}
```

This reduces ambiguity.

---

# 5.5 Derivation vs Invention

Travel constraints:

```text
Ragama -> Ja-Ela = 10
Ja-Ela -> Gampaha = 40
```

Allowed:

```text
Ragama -> Gampaha = 50
```

because it is derivable.

Not allowed:

```text
Gampaha -> Ja-Ela = 40
```

because symmetry was not given.

### Engineering lesson

මේක AI systems සඳහා very important concept එකක්:

```text
Known fact
+ valid rule
= derivation

Missing fact
+ assumption
= invention
```

Reliable system එකක් derivation allow කළ යුතුය, invention control කළ යුතුය.

---

# 5.6 Real-world Application

### Delivery Route Planning

Known travel times + package priorities.

### Cloud Incident Response

Incidents prioritize කරනවා:

```text
Critical production outage
High customer impact
Low-priority warning
```

### Hospital resource scheduling

Generic engineering analogy ලෙස:

```text
limited resource
multiple urgent requests
priority score
route / allocation strategy
```

### Engineering Thinking

Optimization problem එකක් දැක්කාම:

```text
1. Objective එක define කරන්න.
2. Constraints identify කරන්න.
3. Candidate strategies generate කරන්න.
4. Unsupported assumptions block කරන්න.
5. Compare using measurable criteria.
```

---

# 6. Part 4 – Budget Keeper

## 6.1 Engineering Problem

LLM calls free නොවේ.

Long user message:

```text
→ more input tokens
→ more cost
→ more latency
→ more context usage
```

Spam messages system resource waste කරන්න පුළුවන්.

---

## 6.2 Token Guard

අපි:

```text
TOKEN_LIMIT = 150
```

set කළා.

Flow:

```text
Input
 ↓
count tokens
 ↓
<=150 → ALLOWED
>150  → BLOCKED/TRUNCATED
```

---

## 6.3 Summarization Before Processing

Long message outright drop කළේ නැහැ.

Instead:

```text
spam + useful crisis info
        ↓
summarizer
        ↓
remove repetition
preserve critical info
```

Example:

```text
706 tokens
↓
38 tokens
```

### Engineering lesson

Optimization කියන්නේ data delete කරන එක පමණක් නොවේ.

හොඳ optimization එක:

```text
less data
but same important information
```

---

## 6.4 Real-world Application

### Chatbot Gateway

Very long requests summarize before expensive model call.

### RAG System

Retrieved documents token budget එක exceed කළොත් compress කරන්න.

### Email Assistant

Long email thread → concise context.

### Customer Support

Repeated conversation history → compressed summary.

### Engineering Thinking

Before sending context to LLM:

```text
1. Is all this text necessary?
2. Can I remove duplicates?
3. Can I summarize?
4. Which information is critical?
5. What is the maximum token budget?
```

---

# 7. Part 5 – News Feed Extraction Pipeline

## 7.1 Engineering Problem

Raw news feed එක:

```text
human-readable text
```

නමුත් analytics/reporting system එකට අවශ්‍යය:

```text
structured rows
```

So problem:

```text
Unstructured text
→ structured schema
```

---

# 7.2 JSON Extraction

Model එකට exact schema එකක් දුන්නා:

```json
{
  "district": "...",
  "flood_level_meters": null,
  "victim_count": 0,
  "main_need": "...",
  "status": "..."
}
```

මෙහි prompt එක model behavior specification එකක් වගේ.

---

# 7.3 Pydantic as a Validation Boundary

LLM extraction layer:

```text
understands language
```

Pydantic layer:

```text
enforces structure
```

මේ දෙක වෙන වෙනම responsibilities.

### Important Engineering Principle

> **Probabilistic component එකක් පසුව deterministic validation layer එකක් තබන්න.**

LLM:

```text
probabilistic
```

Pydantic:

```text
deterministic
```

මේ combination එක production AI වල ගොඩක් වැදගත් pattern එකක්.

---

# 7.4 Unknown District Lesson

Input:

```text
Report: 15000 displaced in Western Province
```

Model එක random district එකක් invent නොකර:

```text
Unknown
```

කියලා identify කළා.

මෙය good behavior.

### Engineering lesson

Missing data සඳහා best answer එක sometimes:

```text
Unknown
None
Not enough information
```

confidence නැති prediction එකකට වඩා.

---

# 7.5 Pandas + Excel

Validated Pydantic objects:

```text
↓
dict
↓
DataFrame
↓
Excel
```

මෙය AI output business workflow එකකට integrate කරන example එකක්.

AI answer screen එකේ පෙන්වීම විතරක් නොව:

```text
AI output
→ structured business data
→ reporting
→ analytics
```

කියන end-to-end flow එක මේ part එකෙන් ඉගෙනගත්තෙමි.

---

# 8. Prompt Engineering වලින් Software Engineering වෙත ගත් Lessons

## 8.1 Prompt = Interface Contract

Prompt එක random text block එකක් නොවෙයි.

හොඳ prompt එක define කරනවා:

```text
Role
Task
Input
Constraints
Output format
```

එය function interface එකක් වගේ.

---

## 8.2 Prompt Versioning

`few_shot.v1`, `cot_reasoning.v1`, `tot_reasoning.v1`

වගේ versioned names use කිරීමෙන්:

```text
prompt change tracking
experiment comparison
rollback
```

කරන්න පුළුවන්.

Real production system එකක:

```text
prompt_v1
prompt_v2
prompt_v3
```

performance compare කරන්න පුළුවන්.

---

## 8.3 Configuration vs Hard Coding

District list එක notebook එකේ repeat නොකර:

```text
config.yaml
```

වල තබාගත්තා.

### Engineering benefit

```text
single source of truth
less duplication
easy update
consistent behavior
```

---

## 8.4 Model Routing

Simple classification එකට huge reasoning model එකක් unnecessary විය හැක.

Therefore:

```text
simple task → cheaper general model
complex reasoning → stronger reasoning model
```

### Real-world impact

```text
cost ↓
latency ↓
scalability ↑
```

---

# 9. Hallucination Control – මම දැන් හිතන ආකාරය

LLM hallucination completely remove කරන්න බැහැ.

ඒ නිසා engineering question එක:

> “How do I design the system so hallucination causes less damage?”

Approaches:

```text
1. Explicit constraints
2. Structured output
3. Validation
4. Allowed values
5. Unknown fallback
6. Low temperature
7. Grounded context
8. Deterministic post-processing
9. Human review for high-risk cases
```

මෙම project එකේ මේවා කිහිපයක් practically use කළා.

---

# 10. Real-World AI System එකක් Build කරන විට මගේ Thinking Process

දැන් feature එකක් ලැබුණොත් මම මේ order එකෙන් හිතනවා.

## Step 1 – Business Problem

“AI use කරන්න” කියන එක problem එකක් නොවේ.

Real problem එක identify කරන්න.

Example:

```text
Support team එකට දවසකට messages 10,000ක් එනවා.
Agents manual categorize කරනවා.
```

Business problem:

```text
slow triage
high labor cost
inconsistent categorization
```

---

## Step 2 – Decide Whether LLM is Needed

Question:

```text
Can deterministic code solve this?
```

If yes:

```text
use deterministic code
```

If language ambiguity important:

```text
use LLM
```

---

## Step 3 – Define Data Contract

Input:

```text
customer_message: str
```

Output:

```json
{
  "intent": "...",
  "priority": "...",
  "department": "..."
}
```

---

## Step 4 – Define Allowed Behavior

```text
Allowed categories
Fallback values
Unknown handling
Required fields
```

---

## Step 5 – Choose Prompt Technique

```text
Simple classification → few-shot
Multi-step reasoning → CoT
Strategy comparison → ToT
Extraction → JSON schema prompt
Compression → summarization
```

---

## Step 6 – Choose Model and Temperature

```text
cheap/simple model where possible
strong model only when needed
low temperature for deterministic tasks
```

---

## Step 7 – Add Validation

```text
Pydantic
regex
allowed enums
range checks
business rules
```

---

## Step 8 – Add Cost Controls

```text
token limit
summarization
context trimming
batching
caching
```

---

## Step 9 – Add Observability

Production system එකේ record කරන්න:

```text
input tokens
output tokens
latency
model
prompt version
validation failures
retry count
cost
```

---

## Step 10 – Evaluate with Test Set

20–100 sample cases එකක් හදා:

```text
expected output
vs
model output
```

compare කරන්න.

Metrics:

```text
accuracy
precision
recall
schema success rate
hallucination rate
cost/request
latency
```

---

# 11. Real-World Scenario 1 – Customer Support Triage

## Problem

Company එකකට messages thousands per day.

Example:

```text
"My card payment failed"
"I want refund"
"I can't log in"
```

## Apply Project Knowledge

### Few-Shot

Intent classification.

### Low Temperature

Consistent labels.

### Pydantic

Valid categories only.

### Token Guard

Long email threads summarize.

### Structured Output

```json
{
  "intent": "PaymentIssue",
  "priority": "High",
  "team": "Billing"
}
```

### Engineering Result

```text
LLM
→ classification
→ validation
→ ticket routing
```

---

# 12. Real-World Scenario 2 – Security Alert Triage

## Input

```text
SIEM alerts
emails
security reports
```

## AI Tasks

```text
classify alert type
summarize evidence
assign severity
extract affected system
```

## Project Concepts

Few-shot:

```text
Phishing
Malware
Credential Theft
False Positive
```

CoT-style structured analysis:

```text
evidence
impact
urgency
```

Validation:

```text
severity must be:
Low / Medium / High / Critical
```

Unknown handling:

```text
affected_host = Unknown
```

Important:

AI should assist analyst, not autonomously take destructive action without controls.

---

# 13. Real-World Scenario 3 – Data Engineering / News Intelligence

## Problem

Hundreds of raw reports per hour.

Need:

```text
location
event type
victim count
severity
resource need
```

## Project Pattern

```text
Raw text
↓
LLM extraction
↓
Pydantic
↓
DataFrame
↓
Database / dashboard
```

This is directly similar to Part 5.

---

# 14. Real-World Scenario 4 – DevOps Incident Assistant

## Input

```text
logs
alerts
Slack incident messages
```

## Pipeline

```text
alerts
↓
classify severity
↓
summarize duplicate alerts
↓
extract service name
↓
rank incident priority
↓
send structured incident card
```

Project concepts:

```text
Part 1 → classify
Part 2 → stability
Part 3 → prioritization
Part 4 → token control
Part 5 → structured extraction
```

මේ project එකේ parts 5ම එක production use case එකකට connect කරන්න පුළුවන්.

---

# 15. Production Architecture ලෙස මේ Project එක Expand කළොත්

```text
                ┌───────────────────┐
                │ Incoming Messages │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Token Guard       │
                │ Part 4            │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Classification    │
                │ Part 1            │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Extraction        │
                │ Part 5            │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Validation        │
                │ Pydantic          │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Prioritization    │
                │ Part 3            │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Human / Dashboard │
                └───────────────────┘
```

Part 2 එක cross-cutting evaluation layer එකක් වගේ:

```text
stability testing
hallucination testing
temperature testing
```

---

# 16. Biggest Engineering Lessons

## Lesson 1

**LLM output is not truth.**

Always validate.

## Lesson 2

**Missing data should not automatically become guessed data.**

Use:

```text
Unknown
None
Not enough information
```

## Lesson 3

**Structured interfaces reduce ambiguity.**

Prefer:

```json
{ "score": 8 }
```

over:

```text
This looks very urgent and probably deserves around eight.
```

## Lesson 4

**Cost is part of architecture.**

Token usage matters.

## Lesson 5

**Prompting is not separate from engineering.**

Prompt structure influences system behavior.

## Lesson 6

**Evaluation must include reasoning stability, not only final answer.**

## Lesson 7

**Use deterministic code wherever deterministic code is better.**

LLM should not calculate everything just because it can.

---

# 17. If I Build Similar AI Project Again

මම දැන් මේ checklist එක follow කරනවා:

```text
[ ] Business problem clearද?
[ ] LLM really neededද?
[ ] Input contract definedද?
[ ] Output schema definedද?
[ ] Allowed values definedද?
[ ] Missing values handling definedද?
[ ] Prompt technique selectedද?
[ ] Temperature selectedද?
[ ] Model tier selectedද?
[ ] Validation layer තිබේද?
[ ] Token budget තිබේද?
[ ] Retry/failure strategy තිබේද?
[ ] Test dataset තිබේද?
[ ] Metrics definedද?
[ ] Logs/observability තිබේද?
[ ] Human review neededද?
```

---

# 18. Interview එකක මේ Project එක Explain කරන ආකාරය

Short version:

> “I built a crisis-intelligence mini pipeline to learn practical LLM engineering. I used few-shot prompting for message classification, CoT for structured prioritization, ToT for strategy comparison, temperature experiments to study output stability, token guards to control context cost, and Pydantic validation for structured JSON extraction. The main engineering lesson was that reliable LLM systems require deterministic validation, clear constraints, structured interfaces, and cost controls around the model.”

Technical follow-up එකක:

> “One issue I encountered was passing free-text CoT output into the ToT stage, which caused score-location mapping drift. I fixed it by introducing structured intermediate dictionaries. I also constrained route reasoning to directional travel times so the model could derive known paths but could not invent reverse times.”

මෙය strong engineering story එකක්.

---

# 19. Final Reflection

මෙම project එකේ මුලදී මම mainly prompt එක හොඳට ලියන එක ගැන හිතුවා.

Project එක අවසානයේ මගේ mindset එක වෙනස් වුණා:

```text
Before:
“How do I make the model answer correctly?”

After:
“How do I design the whole system so that even when the model is imperfect,
the application remains reliable?”
```

මේ difference එක තමයි AI engineering mindset එක.

Final idea:

```text
LLM
is probabilistic

Software system
must be controlled

Therefore:

LLM
+ Prompt
+ Constraints
+ Structured Data
+ Validation
+ Cost Control
+ Monitoring
+ Fallbacks
= Reliable AI Application
```

---

# 20. Quick Mental Model

```text
Classification problem?
→ Few-shot + allowed labels

Complex reasoning?
→ Structured CoT

Multiple strategies?
→ ToT / branch comparison

Need consistency?
→ Low temperature

Long context?
→ Token guard + summarization

Need machine-readable output?
→ JSON schema + Pydantic

Missing information?
→ Unknown, don't invent

Multiple AI stages?
→ Structured handoff

Production use?
→ Validation + logging + metrics + fallback
```

---

# 21. Next Learning Targets

මෙම project එකෙන් පසු මට ඉගෙනගන්න හොඳ next steps:

1. **Structured Outputs / Function Calling**
2. **LLM evaluation frameworks**
3. **Prompt regression testing**
4. **RAG pipelines**
5. **Vector databases**
6. **Observability for LLM apps**
7. **Caching and cost optimization**
8. **Async/batch inference**
9. **Human-in-the-loop workflows**
10. **Guardrails and policy validation**
11. **Agentic workflow design**
12. **Production deployment with FastAPI**

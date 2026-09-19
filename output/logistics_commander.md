# Part 3 - Logistics Commander

## Part A - CoT Priority Scoring

### Incident 1

- Area: Gampaha
- Main Need: Water
- Priority Score: 5/10

#### CoT Analysis

**Base Score:** 5  
**Age Bonus:** 0  
**Rescue Bonus:** 0  
**Medicine Bonus:** 0  
**Final Priority Score:** 5  

**Reason:** The victims are aged 20‑40, which does not meet the age‑based bonus criteria. The main need is water, not rescue, and there is no indication that medicine is required. Therefore, only the base score applies.

### Incident 2

- Area: Ja-Ela
- Main Need: Insulin
- Priority Score: 8/10

#### CoT Analysis

Base Score: 5  
Age Bonus: 2  
Rescue Bonus: 0  
Medicine Bonus: 1  
Final Priority Score: 8  
Reason: The victim is 75 years old (adds age bonus), the main need is insulin (medicine) not rescue, and medication is required, giving the additional medicine bonus.

### Incident 3

- Area: Ragama
- Main Need: Rescue
- Priority Score: 8/10

#### CoT Analysis

Base Score: 5  
Age Bonus: 0  
Rescue Bonus: 3  
Medicine Bonus: 0  
Final Priority Score: 8  
Reason: The incident has a base score of 5, qualifies for the rescue bonus (+3) because the main need is Rescue, but no victims are under 5 or over 60 and no medicine is required, so no additional points are added.

## Part B - ToT Rescue Strategy

**Branch 1 – Highest Score First**  
Service Order: Ragama → Ja‑Ela → Gampaha  
Known Travel Time: 0 min (Ragama→Ragama) + 10 min (Ragama→Ja‑Ela) + 40 min (Ja‑Ela→Gampaha) = **50 minutes**  
Reasoning: Both Ragama and Ja‑Ela have the highest priority (8). The tie‑breaker uses the explicit travel time from the start; Ragama is 0 min away, Ja‑Ela is 10 min away, so Ragama is served first. After that the only known leg to the remaining incident is Ja‑Ela → Gampaha (40 min).  

**Branch 2 – Closest First**  
Service Order: Ragama → Ja‑Ela → Gampaha  
Known Travel Time: 0 min (Ragama→Ragama) + 10 min (Ragama→Ja‑Ela) + 40 min (Ja‑Ela→Gampaha) = **50 minutes**  
Reasoning: Starting at Ragama, the nearest incident is the one at the same location (0 min). The next nearest, using only the provided travel times, is Ja‑Ela (10 min). The only remaining known leg is Ja‑Ela → Gampaha (40 min).  

**Branch 3 – Furthest First**  
Service Order: Gampaha → Ja‑Ela → Ragama  
Known Travel Time: Ragama → Ja‑Ela (10 min) + Ja‑Ela → Gampaha (40 min) = **50 minutes** for the first leg; subsequent legs are **Unknown** (no directional times from Gampaha to Ja‑Ela or Ragama).  
Reasoning: The furthest reachable incident, following the forward travel legs, is Gampaha (total 10 + 40 = 50 min from the start). The boat must pass through Ja‑Ela but does not automatically serve it. After completing Gampaha, the travel times back to Ja‑Ela or Ragama are not provided, so they are marked Unknown.  

---  

**Comparison**  
- **Priority scores served early**:  
  *Branch 1 & 2*: First serve Ragama (score 8), then Ja‑Ela (score 8), finally Gampaha (score 5).  
  *Branch 3*: First serve Gampaha (score 5), delaying both 8‑score incidents.  

- **Known travel times**:  
  *Branch 1 & 2*: Total known travel = 50 min (all legs known).  
  *Branch 3*: Only the initial leg to Gampaha is known (50 min); the remaining legs are Unknown.  

- **Speed to high‑priority victims**:  
  *Branch 1 & 2* reach both high‑priority (score 8) incidents within the first 10 min (Ragama) and 50 min total.  
  *Branch 3* reaches the first high‑priority incident only after an unknown travel time from Gampaha, potentially much later.  

- **Unknown travel times**: Present only in Branch 3 for the legs after Gampaha.  

---  

**Optimal Route**  
Service Order: **Ragama → Ja‑Ela → Gampaha**  

**Reason:** This route (identical in Branch 1 and Branch 2) serves both highest‑priority incidents (scores 8) as early as possible, uses only known travel times, and completes the mission with a total known travel time of 50 minutes. Branch 3 delays high‑priority care and introduces unknown travel segments, making it less suitable under the given constraints.

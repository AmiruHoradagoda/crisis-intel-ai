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
Reason: The victim is 75 years old (adds 2 points), the main need is insulin (a medication, adds 1 point), and the need is not classified as “Rescue” (no rescue bonus).

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
Service Order: Incident 3 (Ragama) → Incident 2 (Ja‑Ela) → Incident 1 (Gampaha)  
Known Travel Time: 0 min (Ragama) + 10 min (Ragama → Ja‑Ela) + 40 min (Ja‑Ela → Gampaha) = **50 minutes**  
Reasoning: Both Incident 2 and Incident 3 have the top priority score (8). Using the only explicit travel times as a tie‑breaker, the Ragama incident (0 min) is reached before Ja‑Ela (10 min). After serving Ragama, the boat proceeds to Ja‑Ela (10 min) and then to Gampaha (40 min). This order maximises priority coverage while keeping travel times known.

---

**Branch 2 – Closest First**  
Service Order: Incident 3 (Ragama) → Incident 2 (Ja‑Ela) → Incident 1 (Gampaha)  
Known Travel Time: 0 min (Ragama) + 10 min (Ragama → Ja‑Ela) + 40 min (Ja‑Ela → Gampaha) = **50 minutes**  
Reasoning: Starting at Ragama, the nearest incident is the Ragama incident itself (0 min). The next nearest location, using the only provided travel legs, is Ja‑Ela (10 min). The remaining incident, Gampaha, is reached from Ja‑Ela in 40 min. The route is identical to Branch 1 because the “closest” rule leads to the same sequence.

---

**Branch 3 – Furthest First**  
Service Order: Incident 1 (Gampaha) → Incident 2 (Ja‑Ela) → Incident 3 (Ragama)  
Known Travel Time: Ragama → Gampaha = 10 min (Ragama → Ja‑Ela) + 40 min (Ja‑Ela → Gampaha) = **50 minutes**; subsequent legs **Unknown** (no travel times given from Gampaha to Ja‑Ela or Ragama).  
Reasoning: From the start point, Gampaha is the furthest reachable location (50 min). After serving Gampaha, the boat would need to travel to Ja‑Ela and Ragama, but the directional travel times from Gampaha are not provided, so they are marked “Unknown”. This strategy delays high‑priority victims at Ragama and Ja‑Ela and introduces uncertainty for the remainder of the mission.

---

### Comparison
- **Priority scores served early:**  
  - Branch 1 & 2: Serve the highest‑score incidents (8) first (Ragama, then Ja‑Ela).  
  - Branch 3: Serves a lower‑score incident (5) first, delaying both 8‑score incidents.  

- **Known travel times:**  
  - Branch 1 & 2: All legs known, total 50 min.  
  - Branch 3: Only the first leg (50 min) known; the rest are Unknown.  

- **Speed to high‑priority victims:**  
  - Branch 1 & 2 reach Ragama (0 min) and Ja‑Ela (10 min) quickly.  
  - Branch 3 reaches the high‑priority Ja‑Ela and Ragama only after an unknown travel period.  

- **Unknown travel times:**  
  - Only Branch 3 has unknown segments (Gampaha → Ja‑Ela, Gampaha → Ragama).  

### Optimal Route
**Selected Service Order:** Incident 3 (Ragama) → Incident 2 (Ja‑Ela) → Incident 1 (Gampaha)

**Reason:** This route (identical in Branch 1 and Branch 2) uses only confirmed travel times, delivers aid to the two highest‑priority incidents (score 8) as quickly as possible, and avoids any unknown travel segments. It therefore maximises life‑saving impact while maintaining a fully known schedule.

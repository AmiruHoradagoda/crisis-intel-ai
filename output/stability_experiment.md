# Part 2 - Temperature Stability Experiment

This experiment compares CoT reasoning at `temperature=1.0` (Chaos Mode) and `temperature=0.0` (Safe Mode).

## Scenario 1

### Input Scenario

SCENARIO A: THE KANDY LANDSLIDE
Location: Hanthana Tea Factory
Details: "We are trapped. The access road is blocked. My uncle is stuck in the line rooms below, climbing a tree as water rises (Immediate Life Threat). However, inside the factory, we have a diabetic patient who has collapsed and needs insulin (Immediate Health Threat). We also have 40 people hungry."

### Chaos Mode - Temperature 1.0

#### Run 1

**Urgent Issues:**  
1. Uncle trapped in line rooms, climbing a tree as water rises – immediate life‑threat.  
2. Diabetic patient collapsed inside the factory and needs insulin – immediate health‑threat.  
3. 40 people are hungry – non‑life‑threat (needs care but not immediate).

**Risk Comparison:**  
- The uncle faces drowning or injury from rising water; without rescue he will die quickly.  
- The diabetic patient faces potential severe hypoglycemia or hyperglycemia; without insulin he can deteriorate rapidly and die.  
- Hunger in 40 people is serious but not immediately fatal; they can survive for many hours/days without food.

**Recommended Priority:**  
Rescue the uncle trapped in the line rooms (water‑rising situation).

**Reason:**  
Both the uncle and the diabetic patient are facing immediate, life‑threatening conditions, but the uncle is in a rapidly worsening environment (rising water) that can cause death within minutes, whereas a diabetic crisis, while urgent, typically allows a short window (minutes to an hour) for insulin administration. The uncle’s risk is therefore the most time‑sensitive and must be addressed first.

#### Run 2

**Urgent Issues:**  
1. Uncle trapped in the line rooms, climbing a tree as water rises (immediate life threat).  
2. Diabetic patient collapsed inside the factory and needs insulin (immediate health threat).  
3. 40 people are hungry (immediate health threat, but less time‑critical).

**Risk Comparison:**  
- The uncle faces a rapidly worsening situation where rising water could drown him; death could occur within minutes.  
- The diabetic patient requires insulin to prevent life‑threatening complications (e.g., severe hyperglycemia, ketoacidosis); without insulin, critical deterioration could occur within minutes to an hour.  
- Hunger in 40 people poses a serious health issue but does not pose an imminent fatal risk in the short term.

**Recommended Priority:**  
Rescue the uncle trapped in the line rooms and climbing the tree.

**Reason:**  
The uncle’s situation involves an immediate life‑threatening environment (rising water) that can cause death in minutes, making it the most time‑sensitive risk. The diabetic patient also needs urgent care, but insulin can be administered slightly later (minutes to an hour) without the same instant fatal risk as drowning. Hunger, while important, is not an immediate threat to life. Therefore, the first action should be to get the uncle to safety, then address the diabetic patient’s insulin need, followed by feeding the hungry group.

#### Run 3

**Urgent Issues:**  
1. Uncle trapped in the line rooms, climbing a tree as water rises – Immediate Life Threat.  
2. Diabetic patient collapsed inside the factory and needs insulin – Immediate Health Threat.  
3. 40 people are hungry – Immediate need but not life‑threatening in the short term.

**Risk Comparison:**  
- The uncle faces drowning or injury from rising water; death could occur within minutes.  
- The diabetic patient risks severe hypoglycemia or hyperglycemia without insulin; loss of consciousness can progress to death within minutes to an hour.  
- Hunger for the 40 people, while serious, does not pose an immediate fatal risk in the timeframe described.

**Recommended Priority:**  
Rescue the uncle from the rising water.

**Reason:**  
The uncle’s situation involves an imminent, life‑threatening hazard (water rise) that can cause death in minutes, outranking the diabetic patient’s need for insulin (critical but slightly less time‑sensitive) and the hunger of the larger group, which does not constitute an immediate threat to life.

### Safe Mode - Temperature 0.0

**Urgent Issues:**  
1. Uncle trapped in the line rooms below, climbing a tree as water rises – immediate life‑threat.  
2. Diabetic patient collapsed inside the factory and needs insulin – immediate health‑threat.  
3. 40 people are hungry – non‑immediate need.

**Risk Comparison:**  
- The uncle faces drowning or injury from rising water; without rescue he could die within minutes.  
- The diabetic patient risks severe hyperglycemia or hypoglycemia without insulin; death or permanent harm can occur quickly, but the exact time frame is not specified.  
- Hunger for 40 people is a serious concern but does not pose an immediate threat to life in the short term.

**Recommended Priority:**  
Rescue the uncle trapped in the line rooms below.

**Reason:**  
The uncle is exposed to rapidly rising water, creating an imminent life‑threat that can result in death within minutes. This risk is more time‑critical than the diabetic patient’s need for insulin (which, while urgent, is not indicated to be immediately fatal) and far more urgent than the hunger of the group. Immediate action to save the uncle should be taken first.

---

## Scenario 2

### Input Scenario

SCENARIO B: THE GAMPAHA HOSPITAL
Location: Gampaha District General Hospital
Details: "Power has failed in the ICU. We have 3 patients on ventilators with battery backup for 2 hours (Critical). Meanwhile, flood water is entering the ground floor ward where 50 elderly patients are bedridden (High Risk). We have one generator truck arriving in 30 mins, but it can only power one section."

### Chaos Mode - Temperature 1.0

#### Run 1

**Urgent Issues:**  
1. ICU power failure – 3 ventilated patients have only 2 hours of battery backup (critical).  
2. Flood water entering the ground‑floor ward – 50 bedridden elderly patients are at high risk of drowning, infection, hypothermia, etc. (high risk).  

**Risk Comparison:**  
- The ventilated patients will die within 2 hours if the ICU power is not restored.  
- The flooded ward threatens 50 elderly patients; the time to fatal outcome is not specified, only that flood water is entering.  

**Recommended Priority:**  
**Restore power to the ICU first.**  

**Reason:** The ventilated patients have a clearly defined, imminent 2‑hour deadline before loss of life, whereas the exact timeframe for the flooded ward’s danger is unknown. Protecting lives with the most immediate, time‑sensitive risk (the ventilated patients) should be addressed first, using the arriving generator to power the ICU section.

#### Run 2

**Urgent Issues:**  
1. ICU power failure – 3 ventilated patients have only 2 hours of battery backup (Critical).  
2. Flood water entering the ground‑floor ward – 50 bedridden elderly patients are at risk of drowning, injury, infection, etc. (High Risk).  
3. Generator truck arriving in 30 minutes but can power only one section.

**Risk Comparison:**  
- The ICU patients will lose life‑support within 2 hours if power is not restored, and the battery cannot be extended.  
- The flood threatens 50 elderly patients immediately; water intrusion can cause rapid drowning or severe health complications, especially as they are bedridden.  
- Both risks are time‑sensitive, but the ICU patients have a fixed 2‑hour window, whereas the flood impact could become fatal sooner depending on water depth and rate of spread (not quantified).

**Recommended Priority:**  
**Deploy the generator truck to the ICU first.**

**Reason:**  
The ICU ventilated patients face imminent death once the 2‑hour battery reserve is exhausted, and no alternative power source is mentioned. Protecting them is the only option to guarantee their survival within the given timeframe. While the flood threatens many patients, the scenario does not specify the rate of water rise; without that data, the exact time to fatality is unknown, making the ICU risk the most certain and immediate life‑threatening problem that can be mitigated by the arriving generator. After the ICU is secured, the generator (or other measures) can then be directed to address the flooding.

#### Run 3

**Urgent Issues:**  
1. ICU power failure – 3 ventilated patients have only 2 hours of battery backup (Critical).  
2. Flood water entering the ground‑floor ward – 50 bedridden elderly patients are at risk of drowning, hypothermia, infection, etc. (High Risk).  
3. Generator truck arriving in 30 minutes can power only one section (ICU **or** ground‑floor ward).

**Risk Comparison:**  
- The ICU patients could die within 2 hours if ventilation is lost; the risk escalates rapidly as battery depletes.  
- The flood threatens 50 patients, but the water is only just entering; the exact time until it becomes fatal is not specified, only that it is a high‑risk situation.  
- The generator can mitigate only one of these threats, and must be allocated within 30 minutes.

**Recommended Priority:**  
**Deploy the generator to the ICU first.**

**Reason:**  
The ventilated ICU patients have a clearly defined, imminent deadline (2 hours of battery) and would likely die quickly without power. The flood, while affecting many patients, has an undefined time‑to‑criticality; immediate relocation or protective measures may be possible while the generator restores ICU power. Prioritizing the ICU ensures the most time‑sensitive, life‑threatening risk is addressed first.

### Safe Mode - Temperature 0.0

**Urgent Issues:**  
1. ICU power failure – 3 ventilated patients have only 2 hours of battery backup (Critical).  
2. Flood water entering the ground‑floor ward – 50 bedridden elderly patients are at risk of drowning, infection, hypothermia, etc. (High Risk).  
3. Generator truck arriving in 30 minutes but can power only one section.

**Risk Comparison:**  
- The ventilated patients will lose life‑support after the 2‑hour battery expires unless power is restored; loss of ventilation is immediately fatal.  
- The flood threatens a large number of patients, but the scenario does not specify how quickly the water is rising or when it will become lethal. The risk is serious but less time‑critical than the ventilator batteries.

**Recommended Priority:**  
**Restore power to the ICU first (connect the generator to the ICU).**

**Reason:**  
The ICU patients depend on continuous ventilation; their batteries will run out in ≤2 hours, and death will occur rapidly once power is lost. The flood, while affecting many patients, lacks a defined imminent lethal timeline, making it comparatively less time‑sensitive. Supplying the generator to the ICU mitigates the most immediate, life‑threatening risk. After ICU power is secured, the generator (or other resources) can be directed to flood mitigation for the elderly ward.

---


# Apple Services Engineering SRE — 7-Day Interview Preparation Sprint

**Prepared:** 30 September 2026  
**Target:** Site Reliability Engineer — Apple Services Engineering  
**Timing:** A round may happen next week; exact date and format are unconfirmed.  
**Daily commitment:** 3 focused hours. Dates below are IST.  
**Status:** Preparation checklist; unchecked items are not yet recorded as completed.

> The exercises and questions below are preparation recommendations derived from the supplied job description. They are not a confirmed Apple interview question bank or interview sequence.

## 1. Priority labels and working rules

| Label | Meaning | Action |
|---|---|---|
| **P0 — MUST FINISH** | Essential preparation before the first round | Complete first and repeat weak answers |
| **P1 — NEXT PRIORITY** | Additional depth once the core is reliable | Add within the daily block if time permits |
| **P2 — STRETCH** | Useful if extra time becomes available | Defer until P0 is solid |

- Practice Python every day.
- Reuse existing Kubernetes, cloud, GitOps and incident experience; concentrate new learning on coding fluency, SRE decisions and distributed-system reasoning.
- Attempt a coding problem without notes; after reviewing a solution, rewrite it from scratch the next day.
- Rehearse answers aloud. For each technical answer explain the decision, evidence, tradeoff and verification.
- Keep a short mistake log. Repeated weaknesses take priority over new topics.
- If the interview moves earlier, use the three-day fallback in Section 9.

## 2. Role requirements mapped to preparation

| Role requirement | Preparation focus | Priority | Evidence to prepare |
|---|---|---|---|
| Software engineering approach to operations | Python, problem solving, safe automation, testing | P0 | One automation tool explained from input to failure handling |
| Monitoring, alerting, error budgets | SLI/SLO/SLA, burn rate, actionable alerts | P0 | One API SLO and its operational policy |
| Tier-1 services and on-call | Impact assessment, mitigation, escalation, communication | P0 | Two real incident stories |
| Linux and networking | CPU, memory, storage, DNS, TCP, TLS, routing | P0 | Ordered troubleshooting with commands and expected evidence |
| Distributed systems and scalable infrastructure | Dependency failure, retries, overload, data consistency | P0 | One service design with failure walkthroughs |
| Microservices and Kubernetes | Traffic path, resources, probes, scheduling, rollouts | P0 | Service failure despite healthy pods |
| Capacity and scale testing | Demand, bottlenecks, headroom, load tests | P0 | Capacity calculation and validation approach |
| DR exercises | RTO/RPO, restore, traffic failover, failback | P0 | Recovery plan with measured verification |
| Code/design reviews and collaboration | Ownership, tradeoffs, feedback, mistakes | P0 | Five concise experience stories |
| Evaluation of new technologies | Requirements, trial, security, operability, rollback | P1 | One adoption decision and rejected alternative |

## 3. Daily routine

| Block | Duration | Activity |
|---|---:|---|
| Programming | 60 min | Timed exercise, edge-case tests, explanation, correction |
| Technical topic | 60 min | That day's concepts and incident scenarios |
| Spoken practice | 40 min | Mock questions or whiteboard design |
| Review | 20 min | Mistake log and one experience story |

**Coding block:** 5 minutes clarify, 25–35 minutes implement, 10 minutes test/explain, remainder repair or repeat. Two easy tasks may fit; a difficult task can occupy the whole block.

## 4. Seven-day schedule and completion checklists

### Day 1 — Wednesday, 30 September: baseline and SRE fundamentals

**P0 — MUST FINISH**

- [ ] Rehearse a 90-second introduction linking platform work to reliability and customer impact.
- [ ] Select two incidents, one automation example and one architecture example.
- [ ] Explain SLI, SLO, SLA, error budget, toil and the four golden signals.
- [ ] Define an API success SLI, latency SLI, measurement window and exclusions.
- [ ] Explain what changes when the error budget is being consumed too quickly.
- [ ] Code **C1 linked-list reversal** and **C2 frequency counting**.

**Completion check:** Explain user journey → SLI → SLO → alert → response without notes.

### Day 2 — Thursday, 1 October: Linux and networking

**P0 — MUST FINISH**

- [ ] Troubleshoot high CPU, high load with low CPU, OOM and disk saturation.
- [ ] Trace client → DNS → TCP/TLS → load balancer → ingress/service → application → dependency.
- [ ] Distinguish DNS failure, connection refused, timeout, TLS failure and HTTP errors.
- [ ] Explain which command result would change the next investigation step.
- [ ] Code **C3 two-sum** and **C4 valid parentheses**.
- [ ] Reproduce linked-list reversal from memory if Day 1 needed help.

**Completion check:** Give a ten-minute investigation of a slow service using evidence rather than a random command list.

### Day 3 — Friday, 2 October: incidents and observability

**P0 — MUST FINISH**

- [ ] Work through rising 5xx errors, p99 latency and a bad deployment.
- [ ] Explain incident roles, escalation, mitigation, updates and recovery verification.
- [ ] Explain noisy-alert reduction: user impact, burn rate, grouping, deduplication and routing.
- [ ] Separate mitigation, root cause, contributing factors and preventive actions.
- [ ] Implement **C5 streaming log parser and top error endpoints**.
- [ ] Start the Apple coding-round drills with **AP1 IPv4 validation** and **AP2 N-lines-to-M-buckets**.
- [ ] Rehearse one incident with follow-up questions.

**Completion check:** Deliver a five-minute incident narrative with your own decisions and evidence.

### Day 4 — Saturday, 3 October: system design and distributed systems

**P0 — MUST FINISH**

- [ ] Design a customer-facing API with explicit traffic, latency, availability and data requirements.
- [ ] Cover timeouts, bounded retries/backoff/jitter, idempotency and dependency failure.
- [ ] Explain caching, queues, back-pressure, rate limits and load shedding.
- [ ] Discuss database failover, consistency, regional loss and recovery capacity.
- [ ] Code **C6 longest substring without repeating characters**.
- [ ] If time remains, complete **C8 binary search**.

**Completion check:** Present a 30-minute design and defend what happens under overload, dependency latency and regional loss.

### Day 5 — Sunday, 4 October: Kubernetes, capacity and DR

**P0 — MUST FINISH**

- [ ] Troubleshoot healthy pods with failing requests, Pending pods, OOMKilled pods and failed rollouts.
- [ ] Explain readiness/liveness/startup probes, requests/limits, CPU throttling and node pressure.
- [ ] Cover zone spread, disruption budgets, graceful shutdown and rollout/rollback checks.
- [ ] Estimate replicas from measured safe throughput, peak load and failure headroom.
- [ ] Explain load-test types, bottlenecks, autoscaling delay and dependency limits.
- [ ] Define RTO/RPO and walk through restore, failover, validation and failback.
- [ ] Code **C7 linked-list cycle detection**; outline **A1 bounded-concurrency health checker**.

**Completion check:** Explain how the service survives a zone failure and how the surviving capacity is validated.

### Day 6 — Monday, 5 October: mocks and repair

- [ ] 45-minute Python mock: unfamiliar easy/moderate problem and follow-ups; prefer one of **AP3–AP6** if not yet completed.
- [ ] 45-minute SRE/troubleshooting mock.
- [ ] 45-minute system-design mock.
- [ ] 45-minute repair session targeting the weakest two areas.

**Completion check:** Record scores in Section 10 and repeat any failed P0 item.

### Day 7 — Tuesday, 6 October: final rehearsal

- [ ] Repeat missed coding problems from a blank editor, prioritizing **AP1–AP6**.
- [ ] Rehearse introduction and five experience stories.
- [ ] Review SLO calculations, command purposes and system-design failure cases.
- [ ] Practice questions about ownership, mistakes, disagreements and learning.
- [ ] Prepare questions about service ownership, SLOs, on-call and current reliability challenges.
- [ ] Keep the final evening light and adapt this day if the interview is earlier.

**Completion check:** Explain key answers naturally without reading a script.

## 5. Programming — exactly what to practice

### 5.1 Python fundamentals — P0

- [ ] Lists, dictionaries, sets, tuples; mutability and choosing the right structure.
- [ ] Loops, functions, return values, enumerate, zip and sorting with a key.
- [ ] String parsing, whitespace, splitting and safe numeric conversion.
- [ ] Dictionary counting; Counter and defaultdict.
- [ ] Stack using list; queue using collections.deque.
- [ ] Classes and references needed to represent a linked-list node.
- [ ] Exceptions, context managers, file iteration and JSON parsing.
- [ ] Basic assertions or unit tests, readable names and small functions.
- [ ] Complexity: O(1), O(log n), O(n), O(n log n), O(n²).
- [ ] Explain that list membership is O(n); dictionary/set lookup is average O(1).

### 5.2 Core coding exercises

| ID | Priority | Exercise | What to implement/explain | Required edge cases |
|---|---|---|---|---|
| **C1** | **P0** | Reverse a singly linked list | Rewire next pointers with previous/current/next; return new head; O(n) time, O(1) extra space | Empty list, one node, multiple nodes |
| **C2** | **P0** | Count words/items and find most frequent | Dictionary/Counter; specify tie behavior; distinguish total input n and distinct items k | Empty input, ties, case and punctuation rules |
| **C3** | **P0** | Two-sum | Return indices using a hash map; avoid using the same element twice | Duplicates, negatives, no solution |
| **C4** | **P0** | Valid parentheses | Stack; enforce matching bracket types and order | Empty input, closing bracket first, leftover opening brackets |
| **C5** | **P0** | Parse JSON log lines and report top-K error endpoints | Stream file; count 5xx per endpoint; report malformed lines; sort counts for a simple solution | Empty file, bad JSON, missing fields, invalid status, ties |
| **C6** | **P0** | Longest substring without repeated characters | Sliding window with last-seen index or set; O(n) | Empty string, repeated single character, all unique |
| **C7** | **P0** | Detect a linked-list cycle | Slow/fast pointers; O(n) time, O(1) space | No cycle, self-cycle, cycle starting in the middle |
| **C8** | **P1** | Binary search | Maintain bounds and termination; O(log n) | Empty input, absent target, endpoints, duplicates policy |
| **C9** | **P1** | Merge two sorted linked lists | Relink nodes with dummy head; state assumptions about cycles/shared nodes | One empty list, equal values, uneven lengths |
| **C10** | **P1** | Merge overlapping intervals | Sort and scan; clarify whether touching intervals merge | Empty list, nested intervals, same start, touching boundaries |
| **C11** | **P1** | Top-K frequent items using a heap | Explain heap vs full sorting; O(n + k log K) for n inputs and k distinct keys with bounded heap | K=0, K larger than distinct count, ties |
| **C12** | **P1** | BFS/DFS for reachability in a service graph | Adjacency list, visited set, queue/stack; O(V+E) | Cycles, disconnected nodes, missing target |
| **C13** | **P2** | Simple dynamic programming recurrence | Climbing steps/Fibonacci-style recurrence, iterative space optimization | Base cases, small n, input constraints |
| **C14** | **P2** | LRU cache or token-bucket design | Discuss data structures, time, concurrency and constraints before coding | Capacity boundary, updates, repeated keys/time behavior |

**Linked-list reminder:** Printing values backward or reversing a Python list does not complete C1. The exercise requires changing node links and returning the new head.

**C5 sample input:**

~~~json
{"timestamp":"2026-09-30T10:00:00Z","path":"/login","status":503}
{"timestamp":"2026-09-30T10:00:01Z","path":"/health","status":200}
{"timestamp":"2026-09-30T10:00:02Z","path":"/login","status":500}
{"timestamp":"2026-09-30T10:00:03Z","path":"/search","status":502}
~~~

Expected top two: /login = 2 errors; /search = 1 error. Define deterministic tie ordering. Streaming avoids loading the entire log, but the count map still grows with the number of distinct endpoints.

### 5.3 Practical SRE programming

| ID | Priority | Practice task | Required engineering considerations |
|---|---|---|---|
| **A1** | **P0 outline; P1 implementation** | Check health of several HTTP endpoints | Timeout per request, bounded workers, exception handling, latency and status reporting, partial failures, clear summary |
| **A2** | **P1** | Add retries to an API client | Retry eligible failures, bounded attempts, backoff/jitter, total deadline, idempotency and avoiding retry storms |
| **A3** | **P1** | Compare desired configuration with actual configuration | Missing/extra resources, deterministic output, idempotence, dry-run, failure reporting |
| **A4** | **P1** | Compute service error rate from logs/JSON | Explicit valid request population, empty denominator, invalid records, time window and output format |

For A1, be able to discuss threads versus async for I/O, why unlimited concurrency is unsafe, and how per-request timeouts differ from an overall deadline. Use a familiar approach; a new language is unnecessary for this sprint.

### 5.4 Apple-focused Python drills — added for the confirmed coding round

These are **additional** exercises selected for the Apple ASE SRE coding round. Do not repeat an exercise already covered by C1–C14 or A1–A4. The existing C5 streaming-log exercise remains the large-file/log-processing drill.

#### Highest priority before the interview

| ID | Priority | Exercise | What to implement/explain | Important follow-ups |
|---|---|---|---|---|
| **AP1** | **P0** | Validate an IPv4 address | Parse four octets manually; validate characters, count and numeric range 0–255 | Empty input, missing/extra octets, non-numeric input, whitespace, leading zeros policy |
| **AP2** | **P0** | Split N file lines evenly into M buckets | Distribute lines so bucket sizes differ by at most one; avoid unnecessary full-file loading where possible | N < M, N = 0, M = 1, invalid M, very large files |
| **AP3** | **P0** | Find files matching a prefix and count their lines | Use pathlib/os, iterate files safely and return deterministic output | Missing directory, unreadable files, nested directories, empty files, symlinks |
| **AP4** | **P0** | Correlate START/END request log entries | Track request IDs and timestamps; calculate duration and identify unfinished requests | Duplicate START/END, END without START, malformed timestamp, out-of-order records |
| **AP5** | **P0** | Calculate p95 latency | Implement a correct percentile calculation for an in-memory list and state the chosen percentile convention | Empty list, one value, duplicates, huge datasets/streaming approximation |
| **AP6** | **P0** | Tail the last N lines of a large file | Return the final N lines without unnecessarily loading the whole file | N=0, N larger than file, empty file, long lines, binary/encoding errors |

#### Next priority

| ID | Priority | Exercise | What to implement/explain | Important follow-ups |
|---|---|---|---|---|
| **AP7** | **P1** | Find services exceeding an error-rate threshold | Maintain total and failed request counts per service and report services above the threshold | Empty denominator, malformed status, threshold boundary, deterministic ordering |
| **AP8** | **P1** | Normalize and validate phone-number-like input | Remove permitted separators, reject invalid characters and validate structural rules | Country code, whitespace, repeated separators, empty input |
| **AP9** | **P1** | Find missing sequence numbers in an event stream | Identify gaps in a sequence and discuss sorted versus unsorted input | Duplicates, unsorted input, very large ID range, memory tradeoffs |
| **AP10** | **P1** | Write a lazy record generator | Use `yield` to stream only matching/error records instead of building a full list | File errors, malformed records, generator exhaustion, cleanup/context manager |
| **AP11** | **P1** | Debug a broken Python script | Diagnose several defects in existing code and explain the fix before changing it | Mutable defaults, bad exception handling, unsafe dict access, file leaks, off-by-one errors |

**Recommended order:** AP1 → AP2 → AP3 → AP4 → AP5 → AP6. Only then move to AP7–AP11.

**Interview execution rule:** For every AP task, clarify input/output and constraints first, code in a blank VS Code file, test at least three edge cases, and state time/space complexity or the relevant memory/I/O tradeoff.

### 5.5 Definition of “coding exercise completed”

- [ ] Clarify inputs, output, constraints and ambiguous cases.
- [ ] Explain a straightforward solution and its tradeoffs.
- [ ] Implement from a blank editor.
- [ ] Test normal, empty, boundary and failure cases.
- [ ] State time and space complexity accurately.
- [ ] Explain the key invariant or why the algorithm is correct.
- [ ] Reproduce the solution the next day if help was needed.

**Practice targets:** about 20 minutes for an easy task; 35–40 minutes for a moderate task. These are preparation goals, not confirmed Apple timing rules.

## 6. Technical topics and scenario checks

### A. SRE principles — P0

- [ ] SLI/SLO/SLA and choosing a measurement point close to user experience.
- [ ] Availability and latency objectives, p95/p99 and why averages can hide problems.
- [ ] Request-based versus time-based error budgets.
- [ ] Burn rate = observed bad-event fraction / allowed bad-event fraction.
- [ ] Alert urgency, actionability, multiwindow evaluation and release decisions.
- [ ] Toil identification, automation safeguards and measuring results.

**Calculation drill:** At a 99.9% request-success SLO, 1,000,000 eligible requests permit 1,000 bad requests. Separately, a time-based 99.9% SLO over 30 days permits 43.2 minutes of bad time. These are different measurement models. A 1% bad-request rate is 10× the budget burn rate for a 99.9% request-success SLO.

**Questions:** What is an eligible request? Do all 4xx responses mean the service is healthy? How would you handle missing telemetry? Who agrees the objective and release policy?

#### SRE: turn definitions into decisions — P0 explicit questions

Prepare and rehearse answers to all six questions:

- [ ] **What would you measure to know customers are having a good experience?** Start with critical user journeys; define successful, correct and timely outcomes. Cover latency percentiles, errors and relevant freshness/durability indicators; segment by region or operation so aggregate health does not hide affected users.
- [ ] **How would you choose an SLO with the product team?** Agree the user journey, business impact, eligible events, measurement source/window and target. Use historical performance, customer expectations and engineering cost to justify the objective; document ownership and review it together.
- [ ] **What happens when the error budget is nearly exhausted?** Assess remaining budget and burn rate, identify the main contributors, and follow the agreed error-budget policy. Reduce risky changes, prioritize reliability work, and define recovery criteria with the product team; emergency fixes may still be necessary.
- [ ] **When should an alert page someone?** Page when an urgent, actionable condition threatens or harms users and needs intervention now. Tie urgency to service impact and budget consumption; include an owner and runbook. Route nonurgent work to tickets.
- [ ] **How do you reduce noisy alerts without hiding real incidents?** Review actual impact and actionability, use suitable evaluation windows, deduplicate/group correlated alerts, and improve routing. Validate changes against past incidents and retain diagnostic visibility; measure missed incidents as well as page reduction.
- [ ] **How do you prioritize and measure toil reduction?** Estimate frequency × manual effort, error risk and user impact; compare expected benefit with implementation and maintenance cost. Establish a baseline, automate safely, and track hours saved, ticket/page volume, failure rate and adoption.

**Practice checkpoint:** Explain one complete example from user journey → SLI → SLO → alert → operational decision, then show how you would measure improvement.

### B. Linux and networking — P0

| Symptom | Tools to practice explaining | Evidence sought |
|---|---|---|
| High CPU/load | top, ps, pidstat, vmstat | Busy processes, run queue, blocked tasks, CPU time distribution |
| Memory/OOM | free, /proc/meminfo, journalctl, dmesg | Available memory, process growth, reclaim/swap, kernel or cgroup OOM |
| Disk latency/full filesystem | iostat, df -h, df -i, du, lsof | Device latency, space/inodes, deleted files still open |
| Connection failures | ss, ip route, curl -v, tcpdump | Listening sockets, route, handshake/retransmits, response boundary |
| DNS/TLS | dig, getent hosts, openssl s_client | Resolver result, certificate chain/name/expiry, handshake outcome |
| Process stalls | strace where appropriate | Blocking calls and repeated failures |

Commands depend on installed tools and permissions. Explain expected output and use targeted collection.

### C. Incident response — P0

#### Troubleshooting: show an ordered investigation — P0

For every scenario, use:

**Customer impact → scope → recent changes → evidence → safe mitigation → recovery verification → prevention.**

| Step | What to explain |
|---|---|
| Customer impact | Which user journeys fail or slow down? Quantify errors, latency and correctness where possible. |
| Scope | Identify affected regions, zones, versions, endpoints, customers and dependencies. |
| Recent changes | Check deployments, configuration, traffic and infrastructure changes; treat correlation as a hypothesis. |
| Evidence | State a hypothesis, the metric/log/trace or command to test it, and what result changes your next action. |
| Safe mitigation | Choose rollback, traffic shift, throttling, scaling or degraded service with explicit risks and limits. Coordinate escalation and communication. |
| Recovery verification | Confirm user-facing signals and synthetic transactions recover; inspect data correctness, backlog and saturation for a suitable observation period. |
| Prevention | Explain root cause/contributors, corrective actions, owners and how the fix will be tested. |

Apply this sequence to every failure scenario below, including insufficient recovery-region capacity.

- [ ] Service has 5xx after a release: compare versions, scope rollout, rollback safely and verify.
- [ ] p99 rises while p50 is stable: segment traffic and inspect dependencies, queues and resource saturation.
- [ ] Alerts self-resolve: investigate impact and noise sources, then improve alert policy.
- [ ] CPU is low but latency is high: investigate waits, dependencies, pools, storage and locks.
- [ ] Regional errors with otherwise healthy dashboards: check regional/client segmentation and monitoring gaps.

### D. System design — P0

Use a customer-facing API as the main practice system. Start with traffic, payload, read/write ratio, latency, availability, security, consistency and recovery requirements.

- [ ] Client/edge/load balancer → application → cache/database/queue where needed.
- [ ] Dependency timeouts and end-to-end deadline budget.
- [ ] Retry safety, idempotency, circuit breaking and back-pressure.
- [ ] Database replication, failover, data loss risk and split-brain prevention.
- [ ] Cache misses/stampedes, stale reads and behavior when cache fails.
- [ ] Regional routing, failure detection, surviving capacity and failback.
- [ ] Observability, gradual releases and rollback constraints including schema changes.
- [ ] Least privilege, secrets, TLS and protection of customer data.

#### Design: make failure handling explicit — P0

Use the same customer-facing API for all follow-ups. For each, explain detection, failure containment, safe mitigation, verification and the design tradeoff.

- [ ] **Traffic increases tenfold.** Identify the bottleneck and measured safe throughput; cover admission/rate limits, load shedding, cache behavior, autoscaling delay, quotas and database/dependency limits. Verify latency and error objectives under load.
- [ ] **A downstream dependency becomes slow.** Use end-to-end deadlines, bounded timeouts/concurrency, circuit breaking and bulkheads. Explain when a fallback is valid and how queues or connection pools could fill up.
- [ ] **Retries amplify the outage.** Identify amplification across client/service layers; cap attempts, use a retry budget with backoff/jitter and enforce deadlines. Retry only eligible failures and handle idempotency. Verify actual backend attempt volume falls.
- [ ] **A database primary fails.** Explain failure detection, replica eligibility and lag, controlled promotion, fencing the old primary, connection recovery and transaction retry safety. Discuss consistency, possible data loss and RTO/RPO.
- [ ] **One availability zone or region disappears.** Distinguish zone recovery from region recovery. Cover traffic routing, data replication, dependency placement, surviving capacity, failover criteria and tested failback.
- [ ] **A deployment corrupts behavior while health checks stay green.** Use user-journey/synthetic checks, correctness metrics, traces and canary comparisons to detect semantic failure. Halt rollout and roll back when compatible; assess persisted data damage separately because code rollback does not repair it.
- [ ] **The recovery region lacks enough capacity.** Measure safe available capacity and dependency limits before shifting all traffic. Prioritize critical operations, rate-limit or shed lower-priority load, enable valid degraded modes and scale within quotas/provisioning constraints. Shift traffic gradually with rollback criteria; validate demand, latency, errors and data behavior. Prevent recurrence with reserved headroom, quota checks and realistic failover load tests.

**Additional drill:** A queue backlog keeps growing. Compare arrival and processing rates, find the consumer/dependency bottleneck, bound backlog growth, and explain ordering, duplicate handling and recovery time.

**Practice checkpoint:** Draw the API once, then walk through all seven failures using the investigation sequence in Section 6C. Name the evidence, mitigation risk and recovery signal for each.

### E. Kubernetes, capacity and DR — P0

- [ ] Trace ingress/load balancer → Service → EndpointSlice → Pod.
- [ ] Probes, resources, CPU throttling, OOM, scheduling and node pressure.
- [ ] PDBs cover eligible voluntary disruptions; they do not guarantee protection from node/zone failures.
- [ ] Graceful termination, connection draining, topology spread and rolling updates.
- [ ] Capacity = forecast demand / measured safe per-instance throughput, rounded up, plus explicit failure and growth headroom.
- [ ] Load, stress, spike and soak tests; evaluate latency/errors and dependency saturation.
- [ ] RTO/RPO, backups versus replication, tested restores, data validation and failback.

**Capacity drill:** Peak demand is 12,000 requests/second; measured safe capacity is 500 requests/second per instance at the target latency. Baseline is 24 instances. With three equally provisioned zones and a requirement to sustain full load after losing one, use at least 12 per zone (36 total) before additional growth headroom. Validate database, network and placement limits; replica arithmetic alone is insufficient.

## 7. Experience stories and positioning

Prepare five stories using **context → your responsibility → decision/actions → evidence/result → learning**.

| Story | Material to prepare | Follow-up to withstand |
|---|---|---|
| Major incident | Detection, customer impact, mitigation, coordination, verification | Why that mitigation? What alternatives and risks? |
| Automation | Manual baseline, code flow, safety, adoption, outcome | What happens on partial failure or repeated execution? |
| Reliability architecture | Requirements, failure domains, data and traffic path | Which failure did you test? What remained a risk? |
| Migration/change | Dependencies, rollout, rollback and validation | What would trigger rollback? Was data backward compatible? |
| Collaboration/mistake | Disagreement, ownership, communication, correction | What would you do differently? |

Use platform scale, PCF-to-Kubernetes modernization, GitOps/onboarding, network-policy automation and multi-region work where personally defensible. State your own responsibility and actual evidence. Claim Tier-1/on-call ownership only to the extent it reflects your experience.

**Introduction structure:** Experience and scope → reliability responsibilities → one automation result → reason this role fits.

## 8. Mock interview prompts

1. Define an SLO for a customer-facing API and defend the measurement point.
2. A release is planned while the error budget is almost exhausted. What do you do?
3. p99 latency doubled, CPU is normal and no pods restarted. Investigate.
4. The on-call receives repeated pages that recover within two minutes. Improve the situation.
5. A deployment causes elevated errors in one region. Lead the response.
6. Design a service that survives a zone failure and discuss regional recovery.
7. Traffic will triple next month. How do you plan and test capacity?
8. Kubernetes reports healthy pods but users receive 503s. Investigate.
9. Describe automation you built and how it handles failures safely.
10. Reverse a linked list, test it and explain complexity.
11. Parse a large log file to report the top failing endpoints.
12. Explain an incident where the first hypothesis was wrong.
13. Describe a tradeoff you negotiated with an application or product team.
14. How do you verify a DR exercise achieved its objectives?

## 9. If the interview comes earlier: three-day fallback

| Day | Essential work |
|---|---|
| 1 | Introduction, SLO/error-budget example, C1/C2/C3 |
| 2 | Linux/network scenarios, one incident, C4/C5 |
| 3 | API design with failure cases, Kubernetes/DR review, C6/C7 and a short mock |

Spend extra time on the confirmed round format once known. Retain daily coding and at least one incident story. Defer P2 topics and new tool stacks.

## 10. Readiness tracker

Rate each area: **0 = cannot explain; 1 = needs notes; 2 = independent with gaps; 3 = clear under follow-up questions.**

| Area | Score 0–3 | Weakness to fix | Retest date |
|---|---|---|---|
| Python core coding | | | |
| Practical SRE programming | | | |
| SLO/error budget/alerting | | | |
| Linux/network troubleshooting | | | |
| Incident response | | | |
| Distributed-system design | | | |
| Kubernetes reliability | | | |
| Capacity/DR | | | |
| Experience/communication | | | |

### Final readiness checks

- [ ] Core coding exercises solved and tested independently.
- [ ] One complete numerical SLO/error-budget example.
- [ ] Two evidence-based incident narratives.
- [ ] One service design with overload, dependency and regional failure handling.
- [ ] One capacity calculation and a DR validation explanation.
- [ ] Five concise stories with clear personal contribution.
- [ ] Recent errors reviewed; weak areas re-tested.

## 11. Focused references

The preparation schedule and exercises are tailored recommendations. Use these for targeted reading:

- [Apple ASE SRE role](https://jobs.apple.com/en-in/details/200682920-0321/site-reliability-engineer-apple-services-engineering)
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- [Google SRE: Embracing Risk and Error Budgets](https://sre.google/sre-book/embracing-risk/)
- [Google SRE: Incident Management Guide](https://sre.google/resources/practices-and-processes/incident-management-guide/)
- [Google SRE: On-call](https://sre.google/workbook/on-call/)

**Start here:** Day 1 checklist → C1/C2 → one SLO example → one incident walkthrough.
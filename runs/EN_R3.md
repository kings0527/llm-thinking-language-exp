# 限时解题测试卷 — 作答（顺序：Q4, Q1, Q7, Q2, Q9, Q5, Q3, Q10, Q6, Q8）

---

## Q4（汉语断句）

【思考】
The sentence "下雨天留客天留我不留" has no punctuation, so word boundaries and the scope of negation are ambiguous. I need to propose at least three plausible segmentations, each with punctuation, the natural pausing when read aloud, and the resulting meaning about who stays and who does not.

Candidate 1: "下雨天留客，天留，我不留。" Read with pauses after "客" and after "留". Here "下雨天" (rainy day) modifies "留客" (keep the guest): on a rainy day one keeps the guest; "天留" means heaven also keeps him; but "我不留" means the speaker (the host) will not keep him. This is the host refusing to keep the guest.

Candidate 2: "下雨天，留客天，留我不？留！" Read with pauses after each phrase and a rising tone on "留我不", then an emphatic "留". Here "留客天" is a noun phrase "a day for keeping guests"; "留我不？" asks "will you keep me?" and "留！" is the answer "yes, keep!". This is the guest begging/asking to stay and being accepted.

Candidate 3: "下雨天留客天，留我不留？" Read as one phrase then a question "留我不留？". "下雨天留客天" treats the rainy day as a guest-keeping day; "留我不留？" asks "does it keep me or not?". This is an open question from the guest about whether the rainy day justifies his staying.

Candidate 4 (optional): "下雨天，留客天，留，我不留。" "留" = [the host says] stay; "我不留" = I (the guest) will not stay. This is the guest declining to stay.

I will present three main ones plus a brief note on the fourth for completeness.

【答案】
至少三种合理断句如下：

1. **下雨天留客，天留，我不留。**
   停顿：下雨天留客 ‖ 天留 ‖ 我不留。
   意思：雨天本该留客，老天也留他，但"我"（主人）偏不留他。——主人拒客。

2. **下雨天，留客天，留我不？留！**
   停顿：下雨天 ‖ 留客天 ‖ 留我不？‖ 留！
   意思：雨天正是留客的日子，（客人问）"留我不留我？"（主人答）"留！"——客人求留、主人应允。

3. **下雨天留客天，留我不留？**
   停顿：下雨天留客天 ‖ 留我不留？
   意思：雨天是留客天，那么到底留不留我呢？——客人发出的开放式疑问。

（另可补第四种：**下雨天，留客天，留，我不留。** 即主人说"你留下"，客人说"我不留"，表示客人自己不愿留下。）

---

## Q1（数列）

【思考】
We are given a sequence defined by a1 = 2, a2 = 5, and for n ≥ 3, a_n = (a_{n-1} + a_{n-2}) mod 10. Because each term depends only on the previous two terms and each term is a digit from 0 to 9, the state (a_{n-1}, a_n) can take at most 100 values. Therefore the sequence must eventually become periodic. My task is to find a_2026.

I compute terms step by step:
a1 = 2
a2 = 5
a3 = (5+2) mod 10 = 7
a4 = (7+5) mod 10 = 2
a5 = (2+7) mod 10 = 9
a6 = (9+2) mod 10 = 1
a7 = (1+9) mod 10 = 0
a8 = (0+1) mod 10 = 1
a9 = (1+0) mod 10 = 1
a10 = (1+1) mod 10 = 2
a11 = (2+1) mod 10 = 3
a12 = (3+2) mod 10 = 5
a13 = (5+3) mod 10 = 8
a14 = (8+5) mod 10 = 3
a15 = (3+8) mod 10 = 1
a16 = (1+3) mod 10 = 4
a17 = (4+1) mod 10 = 5
a18 = (5+4) mod 10 = 9
a19 = (9+5) mod 10 = 4
a20 = (4+9) mod 10 = 3
a21 = (3+4) mod 10 = 7
a22 = (7+3) mod 10 = 0
a23 = (0+7) mod 10 = 7
a24 = (7+0) mod 10 = 7
a25 = (7+7) mod 10 = 4
a26 = (4+7) mod 10 = 1
a27 = (1+4) mod 10 = 5
a28 = (5+1) mod 10 = 6
a29 = (6+5) mod 10 = 1
a30 = (1+6) mod 10 = 7
a31 = (7+1) mod 10 = 8
a32 = (8+7) mod 10 = 5
a33 = (5+8) mod 10 = 3
a34 = (3+5) mod 10 = 8
a35 = (8+3) mod 10 = 1
a36 = (1+8) mod 10 = 9
a37 = (9+1) mod 10 = 0
a38 = (0+9) mod 10 = 9
a39 = (9+0) mod 10 = 9
a40 = (9+9) mod 10 = 8
a41 = (8+9) mod 10 = 7
a42 = (7+8) mod 10 = 5
a43 = (5+7) mod 10 = 2
a44 = (2+5) mod 10 = 7
a45 = (7+2) mod 10 = 9
a46 = (9+7) mod 10 = 6
a47 = (6+9) mod 10 = 5
a48 = (5+6) mod 10 = 1
a49 = (1+5) mod 10 = 6
a50 = (6+1) mod 10 = 7
a51 = (7+6) mod 10 = 3
a52 = (3+7) mod 10 = 0
a53 = (0+3) mod 10 = 3
a54 = (3+0) mod 10 = 3
a55 = (3+3) mod 10 = 6
a56 = (6+3) mod 10 = 9
a57 = (9+6) mod 10 = 5
a58 = (5+9) mod 10 = 4
a59 = (4+5) mod 10 = 9
a60 = (9+4) mod 10 = 3
a61 = (3+9) mod 10 = 2
a62 = (2+3) mod 10 = 5

Now a61 = 2 and a62 = 5, which equals a1 = 2 and a2 = 5. Since the recurrence is fully determined by the previous two terms, the sequence repeats from here. Thus the period is 60.

To find a_2026, I reduce the index modulo 60: 2026 ÷ 60 = 33 remainder 46 (because 60 × 33 = 1980, and 2026 − 1980 = 46). Since the period is 60 and a1 corresponds to index 1, a_2026 = a_46. From the computation above, a46 = 6.

So a_2026 = 6. The huge subscript is handled by recognizing the sequence is periodic modulo 10 (a Pisano-type period of 60) and reducing the index modulo the period.

【答案】
该数列模 10 必为周期数列。逐项计算得：a₁=2, a₂=5, …… 一直算到 a₆₁=2, a₆₂=5，恰好回到 a₁、a₂ 的取值，故周期为 60。

处理巨大下标的方法：因为每一项只由前两项决定，而每项只能取 0–9，状态最多 100 种，所以必然循环；先算出周期（此处为 60），再把下标对 60 取余：2026 = 60×33 + 46，故 a₂₀₂₆ = a₄₆。

由前面计算 a₄₆ = (a₄₅ + a₄₄) mod 10 = (9 + 7) mod 10 = 6。

**答案：a₂₀₂₆ = 6。**

---

## Q7（跨文化语用）

【思考】
The email sentence is "I would suggest looking at this again, with all due respect." I must determine the colleague's real attitude, identify the linguistic signals, and advise how a Chinese team lead should reply.

(a) Real attitude: This is not merely a gentle, neutral suggestion to re-examine. The phrase "with all due respect" is a conventionalized politeness marker that typically prefaces disagreement or contradiction. Combined with "I would suggest looking at this again," it softly signals that the colleague believes the current work is flawed or incorrect and should be redone. So the true attitude is polite but firm disagreement / a critique wrapped in indirectness.

(b) Linguistic signals supporting this:
- "with all due respect": a formulaic hedge that warns the hearer a challenge is coming; it does not literally express respect so much as mitigate face-threat.
- "I would suggest" (conditional "would"): hedged, non-imperative, softens the force but still implies the current version is inadequate.
- "looking at this again": the word "again" implies a prior look was insufficient; the analysis needs re-examination, i.e., it is currently wrong or incomplete.
The indirectness is typical of British English polite dissent, where criticism is dressed as a suggestion.

(c) As the Chinese team lead, I would reply by acknowledging the feedback, avoiding defensiveness, and offering concrete next steps. A reply could be: "Thank you for the feedback. We'll re-review the points you raised and come back to you with a revised version." Key points: (1) accept the critique gracefully without arguing; (2) show concrete action rather than agree/disagree; (3) ask for specifics if none were given. Reason: British politeness is indirect; taking it as merely "a soft suggestion" would under-respond, while becoming defensive would damage rapport. A measured, action-oriented reply preserves face on both sides and moves the work forward.

【答案】
(a) 这位同事的真实态度**并非**只是温和地建议"再看一遍"。结合语境，这是一句**包裹在礼貌外衣下的、礼貌但明确的反对/批评**——潜台词是"你现在的方案有问题，需要重做"。

(b) 支持这一判断的语言信号：
- **"with all due respect"**：这是英语中典型的"异议预警"套语，常用于即将反驳或否定对方之前，用以缓和面子威胁，并非真的在表达尊重。
- **"I would suggest"**：用情态动词 would 构成委婉条件式，把语气软化，但暗含"当前版本不够好"的判断。
- **"looking at this again"**：again 表明"之前看过但不够"，即现有分析需要重审、存在错误或不完整。

(c) 作为中国团队负责人，我会这样回复（要点）：先礼貌接纳反馈、不自辩，再给出具体行动。示例回复："Thank you for the feedback. We'll re-review the points you raised and come back to you with a revised version."
处理原因：英式礼貌偏间接，若只当"软建议"会回应不足，若 defensive（ defensive）则会伤和气；以"认可 + 具体行动"回应，既保全面子又推进工作。

---

## Q2（逻辑推理）

【思考】
We have five people 甲, 乙, 丙, 丁, 戊 with distinct ranks 1 to 5. Rule: ranks 1 and 2 tell the truth; ranks 3, 4, 5 lie.

Statements:
甲: I am not last.
乙: 丙 is 1st.
丙: 戊 is 3rd.
丁: I am not 2nd.
戊: 甲 is ranked ahead of 乙.

Exactly two people tell the truth (ranks 1 and 2); three lie.

Step 1: Test 乙. If 乙 tells the truth, then 丙 is indeed 1st, so 丙 also tells the truth. Then the two truth-tellers are 乙 and 丙, meaning 乙 must be 2nd (since 丙 is 1st). Now 丁 is a liar, so 丁's statement "I am not 2nd" is false, implying 丁 is 2nd. But 乙 is already 2nd. Contradiction. Therefore 乙 is a liar, and 丙 is NOT 1st.

Step 2: Since 乙 lies, the two truth-tellers are among {甲, 丙, 丁, 戊}. Consider whether 丙 tells the truth.

Case A: 丙 tells the truth. Then 戊 is 3rd (so 戊 lies). The other truth-teller is 甲 or 丁 (戊 is a liar).
- Subcase A1: 甲 and 丙 truthful. Then 丁 is a liar, so 丁's "I am not 2nd" is false → 丁 is 2nd. But ranks 1 and 2 are taken by 甲 and 丙. Contradiction.
- Subcase A2: 丁 and 丙 truthful. Then 丁 and 丙 are ranks 1 and 2; 戊=3rd. 丁 truthful → 丁 is not 2nd → 丁=1st, 丙=2nd. 甲 and 乙 are liars (ranks 4,5). 甲 liar → "I am not last" false → 甲=5th. Then 乙=4th. Check 戊 (liar, 3rd): "甲 ahead of 乙" means rank(甲) < rank(乙); 甲=5, 乙=4, so 甲 is NOT ahead → statement false ✓. All consistent.

Case B: 丙 lies. Then 戊 is not 3rd. Truth-tellers among {甲, 丁, 戊}.
- B1: 甲,丁 truthful → 丁=1st, 甲=2nd. 戊 liar and 戊≠3rd. 戊's "甲 ahead of 乙" false → 乙 ahead of 甲 → 乙=1st, but 丁=1st. Contradiction.
- B2: 甲,戊 truthful → 丁 liar → 丁=2nd, but 丁 is a liar (rank 3-5). Contradiction.
- B3: 丁,戊 truthful → 丁=1st, 戊=2nd. 甲 liar → 甲=5th. But 戊 truthful requires 甲 ahead of 乙, impossible if 甲=5th. Contradiction.

Only Case A2 works. Final ranking: 丁=1st, 丙=2nd, 戊=3rd, 乙=4th, 甲=5th.

【答案】
推理过程（逐步缩小范围）：

规则：第 1、2 名说真话，第 3、4、5 名说假话，故全场恰好 2 真 3 假。

1. **先判定乙说假话**：若乙真，则"丙是第 1 名"为真，丙也说真话；于是真话者是乙、丙，乙必为第 2。此时丁说假话，丁说"我不是第 2"为假 ⇒ 丁是第 2，与乙冲突。矛盾！所以**乙说假话**，且丙不是第 1。

2. **丙说真话的情形**：丙真 ⇒ "戊是第 3"为真，戊说假话。另一真话者只能是甲或丁。
   - 若甲、丙真：丁假 ⇒ 丁是第 2，但第 1、2 已被甲丙占，矛盾。
   - 若丁、丙真：丁、丙占第 1、2；丁真 ⇒ 丁≠第 2 ⇒ **丁=1，丙=2**；戊=3。甲、乙为假（占 4、5）。甲假 ⇒ "我不是最后"为假 ⇒ **甲=5**；则**乙=4**。核验戊（假，第 3）："甲比乙的rank靠前"即甲<乙，但甲=5、乙=4，不成立 ⇒ 假话成立 ✓。全部自洽。

3. **丙说假话的情形**：戊≠第 3，真话者在甲、丁、戊中；逐一验证（甲丁真 / 甲戊真 / 丁戊真）均推出矛盾（如丁假则丁=2 与"丁是假话者"冲突，或甲=5 与戊"甲靠前"冲突）。

唯一解：**第 1 名丁，第 2 名丙，第 3 名戊，第 4 名乙，第 5 名甲。**

---

## Q9（双向翻译）

【思考】
Part (a): Translate "The early bird catches the worm" into Chinese with three different styles and note contexts.
- Literal/daily: 早起的鸟儿有虫吃。 (closest to original, used in everyday exhortation to be early/diligent.)
- Idiomatic/competitive (business/strategy): 捷足先登。 (emphasizes seizing the first-mover advantage; suits competitive or commercial contexts.)
- Resource-scarcity context: 先到先得。 (stresses that order of arrival determines who benefits; suits limited-resource situations like tickets or seats.)

Part (b): Translate "三个臭皮匠，顶个诸葛亮" into English while preserving the metaphor (not abstract "collective wisdom").
A faithful metaphor-preserving version: "Three cobblers combined can match Zhuge Liang." To keep the cultural image, render 皮匠 as "cobblers" and 诸葛亮 as "Zhuge Liang" (optionally glossed as the master strategist). Alternative: "Three humble cobblers together surpass Zhuge Liang." The trade-off: a fully domesticated version like "Two heads are better than one" loses the specific Chinese imagery, so I keep the proper names and the cobbler metaphor, adding a brief gloss for an English reader.

【答案】
(a) "The early bird catches the worm" 三种中文译法：
1. **早起的鸟儿有虫吃。**（直译，最贴近原句；适用于日常劝人勤快、赶早的场景。）
2. **捷足先登。**（成语化，突出"抢占先机"；适用于商业竞争、博弈等语境。）
3. **先到先得。**（强调先后顺序决定收益；适用于资源有限如抢票、占座等场景。）

(b) "三个臭皮匠，顶个诸葛亮" 英译（保留原比喻）：
**"Three cobblers combined can match Zhuge Liang."**
取舍说明：把"皮匠"译为 cobblers、"诸葛亮"保留专名 Zhuge Liang（可加注 the master strategist），从而完整保留原句"底层手艺人合力胜过大谋士"的意象；若译为 "Two heads are better than one" 虽达意却丢失了原有文化比喻，故不取。

---

## Q5（英语句法歧义）

【思考】
The sentence "The chicken is ready to eat." is ambiguous.

(a) Two readings:
Reading 1: The chicken (the cooked food) is ready (for someone) to eat it. → 鸡肉可以吃了（被人吃）。
Reading 2: The chicken (the live bird) is ready to eat (something). → 这只鸡准备去吃东西了（它要吃了）。

(b) Syntactic mechanism: The adjective "ready" takes an infinitival complement "to eat". The ambiguity lies in the control/theta-role of the matrix subject "the chicken" with respect to the infinitive. In Reading 1, "the chicken" is the LOGICAL OBJECT of "eat" (it is what gets eaten) — this is an object-to-subject raising / tough-movement construction where the matrix subject is the underlying object of the infinitive. In Reading 2, "the chicken" is the LOGICAL SUBJECT of "eat" (it will perform the eating). So the ambiguity comes from whether the matrix subject is interpreted as the logical subject or the logical object of the infinitive clause.

(c) Disambiguated rewrites:
Reading 1: "The chicken is ready to be eaten." or "The chicken is ready for us to eat."
Reading 2: "The chicken is ready to start eating." or "The chicken is hungry and ready to eat."

【答案】
(a) 两种理解：
- 理解一：鸡肉（食物）已经可以**被吃**了。→ The chicken is ready (for someone) to eat it.
- 理解二：这只鸡（活禽）准备**去吃东西**了。→ The chicken is ready to eat (something).

(b) 句法机制：形容词 ready 带不定式补语 to eat，歧义来自矩阵主语 the chicken 与不定式 eat 之间的**论元角色（逻辑主语/逻辑宾语）**不明。
- 理解一中，the chicken 是不定式 eat 的**逻辑宾语**（被吃），属 tough-movement / 宾语提升结构；
- 理解二中，the chicken 是 eat 的**逻辑主语**（去吃）。
因此歧义源于"矩阵主语究竟是不定式的逻辑主语还是逻辑宾语"这一控制关系的不确定性。

(c) 消除歧义：
- 理解一：**The chicken is ready to be eaten.**（或 The chicken is ready for us to eat.）
- 理解二：**The chicken is ready to start eating.**（或 The chicken is hungry and ready to eat.）

---

## Q3（汉语语义）

【思考】
The pattern is "差点(没)VP" (almost / nearly). The meaning depends on whether the event VP is desirable (good) or undesirable (bad) from the speaker's perspective.

General rule:
- For an UNDESIRABLE event (bad thing): "差点 VP" = the bad thing almost happened but did NOT happen. "差点没 VP" = the bad thing also did NOT happen (the negative 没 cancels the near-miss, returning to "didn't happen"). So the two are the SAME: the bad event did not occur.
- For a DESIRABLE event (good thing): "差点 VP" = the good thing almost happened but failed, so it did NOT happen. "差点没 VP" = the good thing barely happened, so it DID happen. So the two are DIFFERENT.

Apply to each group:
(1) 摔倒 (fall) — undesirable. 他差点摔倒 = he almost fell, didn't fall. 他差点没摔倒 = he almost fell but didn't fall (barely avoided). SAME (both: did not fall).
(2) 考上大学 (get into university) — desirable. 他差点考上 = almost got in but failed (did NOT get in). 他差点没考上 = barely got in (DID get in). DIFFERENT.
(3) 死 (die) — undesirable. 他差点儿死了 = almost died, didn't die. 他差点儿没死 = almost died but survived (didn't die). SAME (both: did not die).
(4) 进 (ball goes in) — from the attacking side's perspective this is desirable. 球差点进了 = almost went in but didn't. 球差点没进 = barely went in (DID go in). DIFFERENT. (Note: if the speaker did NOT want it in, the two would be the same; but standard reading takes the kicker's side, so desirable → different.)

Summary: For bad events the two forms coincide in meaning (didn't happen); for good events they diverge (差点 = didn't happen, 差点没 = did happen).

【答案】
逐组判断与含义：

- **(1) 他差点摔倒。/ 他差点没摔倒。** —— **相同**。均为"没摔倒"。摔倒是不如意事："差点摔倒"=差点摔但没摔；"差点没摔倒"=差点摔但幸好没摔（勉强躲过），二者都表示没发生。
- **(2) 他差点考上大学。/ 他差点没考上大学。** —— **不同**。考上大学是如意事："差点考上"=差一点考上却没考上（落榜）；"差点没考上"=差点没考上却考上了（险胜录取）。
- **(3) 他差点儿死了。/ 他差点儿没死。** —— **相同**。均为"没死"。死是不如意事：两句都表示"差点死但活下来了"。
- **(4) 球差点进了。/ 球差点没进。** —— **不同**（按射门方视角，进球是如意事）："球差点进了"=差点进却没进；"球差点没进"=差点没进却进了（压线进球）。

**语法规律总结**："差点（没）VP" 的语义取决于事件 VP 对说话人是"如意"还是"不如意"。
- 不如意事：两句同义，都表示"未发生"（没摔倒/没死）。"没"否定了"差点发生"，回到"没发生"。
- 如意事：两句异义——"差点VP"=没发生；"差点没VP"=发生了（险成）。

---

## Q10（英文语境计算）

【思考】
The recipe needs 3/4 cup of flour. We scale by 2.5×.
Total flour needed = (3/4) × 2.5 = (3/4) × (5/2) = 15/8 = 1.875 cups.

We have a 1/4-cup scoop and a 1-tablespoon scoop. Given 1 cup = 16 tablespoons, a 1/4 cup = 4 tablespoons.

Plan: use the 1/4-cup scoop as many whole times as possible, then make up the remainder with tablespoons.
1.875 cups ÷ 0.25 cup = 7.5, so 7 scoops of 1/4 cup.
7 × 0.25 = 1.75 cups.
Remaining = 1.875 − 1.75 = 0.125 cups = 1/8 cup.
Convert remainder to tablespoons: 1/8 cup × 16 tbsp/cup = 2 tablespoons.

Check: 7 × 0.25 cup = 1.75 cups = 28 tbsp; 2 tbsp = 2/16 = 0.125 cup; total = 1.875 cups ✓.

So: 7 scoops of the 1/4-cup measure, plus 2 tablespoons.

【答案】
换算过程：
- 原需面粉 3/4 杯，做 2.5 倍量：3/4 × 2.5 = 3/4 × 5/2 = 15/8 = **1.875 杯**。
- 已知 1 杯 = 16 汤匙，故 1/4 杯 = 4 汤匙。
- 先用 1/4 杯量勺：1.875 ÷ 0.25 = 7.5，取整数 **7 次** → 7 × 0.25 = 1.75 杯。
- 剩余：1.875 − 1.75 = 0.125 杯 = 1/8 杯。
- 折成汤匙：1/8 × 16 = **2 汤匙**。

核验：7 次 × 1/4 杯 = 1.75 杯（28 汤匙），加 2 汤匙 = 0.125 杯，合计 1.875 杯 ✓。

**答案：用 1/4 杯量勺舀 7 次，再用汤匙舀 2 匙。**

---

## Q6（英语韵律）

【思考】
The line is "Shall I compare thee to a summer's day?" from Shakespeare's Sonnet 18.

Count syllables:
Shall (1) I (2) com (3) pare (4) thee (5) to (6) a (7) sum (8) mer's (9) day (10) → 10 syllables.

Divide into feet (iambic pentameter = five iambs, each unstressed-stressed):
Foot 1: Shall I → shăll Í (unstressed-stressed)
Foot 2: comPARE → cŏm PÁRE (unstressed-stressed)
Foot 3: thee TO → thĕe TÓ (unstressed-stressed)
Foot 4: a SUM → ă SUM (unstressed-stressed)
Foot 5: mer's DAY → mĕr's DÁY (unstressed-stressed)

Stress pattern: × / | × / | × / | × / | × /  (× = unstressed, / = stressed). Five iambic feet, 10 syllables. This matches iambic pentameter.

Conclusion: Yes, it is iambic pentameter.

【答案】
音节数与音步划分（×=轻读，/=重读）：

Shall I | comPARE | thee TO | a SUM | mer's DAY?
× /  × /   × /   × /   × /

- 音节数：**10 个**（Shall·I·com·pare·thee·to·a·sum·mer's·day）。
- 音步：5 个抑扬格（iamb），每脚为"轻—重"。
- 重音位置落在 I、PARE、TO、SUM、DAY 上。

**结论：是的，这是标准的抑扬格五音步（iambic pentameter）。**

---

## Q8（代码）

【思考】
I need a Python function is_palindrome(s) that:
- ignores case differences,
- ignores all spaces and punctuation,
- correctly handles Chinese strings (e.g., "上海自来水来自海上").

Approach:
1. Normalize the string with unicodedata.normalize('NFKC', s) so that full-width characters and compatibility forms are standardized.
2. Keep only alphanumeric characters using str.isalnum(). In Python, str.isalnum() returns True for CJK (Chinese) characters as well as ASCII letters and digits, so Chinese characters are retained while spaces and punctuation (e.g., "，。！" and ASCII , . ! ?) are removed.
3. Convert the kept characters to lower case with str.lower(). For Chinese this is a no-op, which is fine.
4. Compare the resulting list with its reverse; if equal, it is a palindrome.

This handles Unicode punctuation because isalnum() filters out any character that is not a letter or digit, regardless of script. Case is handled by lower(). For the Chinese example "上海自来水来自海上", all characters are kept, lowercased (unchanged), and the reverse equals the original, returning True.

【答案】
```python
import unicodedata

def is_palindrome(s):
    # 1) Unicode 归一化，统一全角/兼容字形
    normalized = unicodedata.normalize('NFKC', s)
    # 2) 仅保留字母与数字（isalnum 对中文也返回 True，
    #    从而自动过滤空格与所有 Unicode 标点）
    cleaned = [ch for ch in normalized if ch.isalnum()]
    # 3) 统一大小写（中文 lower() 不受影响）
    chars = [ch.lower() for ch in cleaned]
    # 4) 正读反读比较
    return chars == chars[::-1]
```

说明：
- **Unicode 标点/空格处理**：用 `str.isalnum()` 过滤，它对本语种字母、数字（含中文 CJK）返回 `True`，对空格与中英文标点（` ，。！, . ! ?` 等）返回 `False`，故一并剔除。
- **大小写处理**：`str.lower()` 统一英文大小写；中文 `lower()` 为无操作，不受影响。
- 测试 `is_palindrome("上海自来水来自海上")` 返回 `True`；`is_palindrome("A man, a plan, a canal: Panama")` 也返回 `True`。

# 限时解题测试卷 作答（ADAPT_R1）

---

## Q1（数列）

【判断题型】这是一道数列（递推关系 + 周期性）题。我打算用**中文**思考，因为涉及"个位数""下标"等中文数学表达，中文更直观，且便于逐步列出递推项。

【思考】
已知条件：a₁ = 2，a₂ = 5，当 n ≥ 3 时，aₙ = (aₙ₋₁ + aₙ₋₂) mod 10（即前两项之和的个位数）。

我需要求 a₂₀₂₆。由于递推只依赖前两项，而每一项都落在 0–9，相邻两项组成的有序对 (aₙ₋₁, aₙ) 最多只有 10×10 = 100 种可能，因此序列必然会出现循环（周期至多为 100，实际上更小）。我的策略是：先逐项算出序列，直到再次出现 (a₁, a₂) = (2, 5) 这个起始对，从而确定周期；然后用 2026 对周期取模，把巨大的下标降到可直接查表的范围内。

逐项计算：
- a₁ = 2
- a₂ = 5
- a₃ = (5+2) mod 10 = 7
- a₄ = (7+5) mod 10 = 2
- a₅ = (2+7) mod 10 = 9
- a₆ = (9+2) mod 10 = 1
- a₇ = (1+9) mod 10 = 0
- a₈ = (0+1) mod 10 = 1
- a₉ = (1+0) mod 10 = 1
- a₁₀ = (1+1) mod 10 = 2
- a₁₁ = (2+1) mod 10 = 3
- a₁₂ = (3+2) mod 10 = 5
- a₁₃ = (5+3) mod 10 = 8
- a₁₄ = (8+5) mod 10 = 3
- a₁₅ = (3+8) mod 10 = 1
- a₁₆ = (1+3) mod 10 = 4
- a₁₇ = (4+1) mod 10 = 5
- a₁₈ = (5+4) mod 10 = 9
- a₁₉ = (9+5) mod 10 = 4
- a₂₀ = (4+9) mod 10 = 3
- a₂₁ = (3+4) mod 10 = 7
- a₂₂ = (7+3) mod 10 = 0
- a₂₃ = (0+7) mod 10 = 7
- a₂₄ = (7+0) mod 10 = 7
- a₂₅ = (7+7) mod 10 = 4
- a₂₆ = (4+7) mod 10 = 1
- a₂₇ = (1+4) mod 10 = 5
- a₂₈ = (5+1) mod 10 = 6
- a₂₉ = (6+5) mod 10 = 1
- a₃₀ = (1+6) mod 10 = 7
- a₃₁ = (7+1) mod 10 = 8
- a₃₂ = (8+7) mod 10 = 5
- a₃₃ = (5+8) mod 10 = 3
- a₃₄ = (3+5) mod 10 = 8
- a₃₅ = (8+3) mod 10 = 1
- a₃₆ = (1+8) mod 10 = 9
- a₃₇ = (9+1) mod 10 = 0
- a₃₈ = (0+9) mod 10 = 9
- a₃₉ = (9+0) mod 10 = 9
- a₄₀ = (9+9) mod 10 = 8
- a₄₁ = (8+9) mod 10 = 7
- a₄₂ = (7+8) mod 10 = 5
- a₄₃ = (5+7) mod 10 = 2
- a₄₄ = (2+5) mod 10 = 7
- a₄₅ = (7+2) mod 10 = 9
- a₄₆ = (9+7) mod 10 = 6
- a₄₇ = (6+9) mod 10 = 5
- a₄₈ = (5+6) mod 10 = 1
- a₄₉ = (1+5) mod 10 = 6
- a₅₀ = (6+1) mod 10 = 7
- a₅₁ = (7+6) mod 10 = 3
- a₅₂ = (3+7) mod 10 = 0
- a₅₃ = (0+3) mod 10 = 3
- a₅₄ = (3+0) mod 10 = 3
- a₅₅ = (3+3) mod 10 = 6
- a₅₆ = (6+3) mod 10 = 9
- a₅₇ = (9+6) mod 10 = 5
- a₅₈ = (5+9) mod 10 = 4
- a₅₉ = (4+5) mod 10 = 9
- a₆₀ = (9+4) mod 10 = 3
- a₆₁ = (3+9) mod 10 = 2
- a₆₂ = (2+3) mod 10 = 5

此时 a₆₁ = 2 = a₁，a₆₂ = 5 = a₂，起始对 (2, 5) 再次出现，说明序列从第 1 项起以 60 为周期循环，即 aₙ = aₙ₊₆₀ 对所有 n 成立。

接下来处理大下标 2026：计算 2026 除以 60 的余数。
60 × 33 = 1980，2026 − 1980 = 46，所以 2026 ≡ 46 (mod 60)。
因为周期为 60 且 a₆₁ = a₁，所以 a₂₀₂₆ = a₄₆。
由上面算得 a₄₆ = 6。

【答案】a₂₀₂₆ 的值为 **6**。处理大下标的方法是：识别出序列相邻两项构成的有序对必然循环，逐项递推直到起始对 (2,5) 重现，确认周期为 60；再将 2026 对 60 取余得到 46，于是 a₂₀₂₆ = a₄₆ = 6。

---

## Q2（逻辑推理）

【判断题型】这是一道逻辑推理（真假话 + 名次分配）题。我打算用**中文**思考，因为题干、人物、名次均为中文表述，用中文建立和检验假设最顺手。

【思考】
规则：5 人甲、乙、丙、丁、戊名次 1–5 无并列；第 1、2 名说真话，第 3、4、5 名说假话。

五人的话：
- 甲：我不是最后一名（非第 5）。
- 乙：丙是第一名。
- 丙：戊是第三名。
- 丁：我不是第二名。
- 戊：甲的名次比乙靠前（即甲的名次数字 < 乙的名次数字）。

逐步缩小范围：

第一步，先判断乙说真话还是假话。
假设乙说真话（即乙是第 1 或第 2 名），则"丙是第一名"为真，所以丙 = 第 1。但乙说真话意味着乙 ∈ {1,2}，丙已是第 1，故乙 = 第 2。此时丙是第 1（真话者），丙的话"戊是第三名"为真 → 戊 = 第 3（假话者）。戊是假话者，其话"甲比乙靠前"必须为假，即乙比甲靠前（乙名次数字 < 甲名次数字）。乙 = 第 2，所以甲必须比第 2 更差，甲 ∈ {3,4,5}。甲是假话者，甲的话"我不是最后一名"必须为假，所以甲 = 第 5。剩下丁 = 第 4（假话者）。但丁的话"我不是第二名"实际为真（丁是第 4），而假话者必须说假话，矛盾。故假设不成立，**乙必为假话者（第 3、4 或 5 名）**，且"丙是第一名"为假 → 丙 ≠ 第 1。

第二步，确定谁是两名真话者（第 1、2 名）。乙已确定是假话者，所以真话者只能从 {甲, 丙, 丁, 戊} 中取两人。

- 若真话者为甲、丁：则丙是假话者，丙的话"戊=第3"为假 → 戊 ≠ 3。戊是假话者，戊的话"甲比乙靠前"为假 → 乙比甲靠前。但甲是真话者（第1或2），乙是假话者（≥3），乙不可能比甲靠前，矛盾。
- 若真话者为甲、戊：则丁是假话者（≥3），丁的话"我不是第2"实际为真，矛盾（假话者须说假）。
- 若真话者为丁、戊：则戊是真话者，戊的话"甲比乙靠前"为真 → 甲比乙靠前。但乙是假话者（≥3），甲若比第3还靠前则只能是 1 或 2，即甲也是真话者，与"仅丁、戊是真话者"冲突；且若甲是假话者（因只丁戊真），甲的话"我不是最后"为假 → 甲 = 第5，甲(5)并不比乙(≤4)靠前，又矛盾。
- 若真话者为丙、戊：丙真 → 戊 = 第3，但戊又是真话者（第1或2），戊不能既是第3又在第1/2，矛盾。
- 若真话者为甲、丙：丙真 → 戊 = 第3（假话者）；乙假 → 丙≠1，故丙 = 第2、甲 = 第1。戊假 → "甲比乙靠前"为假 → 乙比甲靠前，但甲=第1最佳，乙(≥3)不可能比甲靠前，矛盾。
- 若真话者为丙、丁：丙真 → 戊 = 第3（假话者，✓）。丁真 → "我不是第2"为真，故丁 = 第1、丙 = 第2（因丙≠1）。乙假 → "丙是第1"为假，✓（丙=2）。戊假 → "甲比乙靠前"为假 → 乙比甲靠前。剩余甲、乙占第4、5，且甲的话"我不是最后"为假 → 甲 = 第5，于是乙 = 第4。检验乙比甲靠前：乙(4) < 甲(5)，成立 ✓。

逐一验证最终排列：丁=1(真)"非第2"✓；丙=2(真)"戊=3"✓；戊=3(假)"甲比乙靠前"为假（甲5、乙4，乙在前）✓；乙=4(假)"丙=1"为假✓；甲=5(假)"非最后"为假（正是最后）✓。全部自洽。

【答案】五人名次为：**丁第 1 名，丙第 2 名，戊第 3 名，乙第 4 名，甲第 5 名**。

---

## Q3（汉语语义）

【判断题型】这是一道汉语词汇语义题，考察"差点/差点没"与事件期待值（期望/非期望）的互动。我打算用**中文**思考，因为分析对象是汉语句义本身，中文最准确。

【思考】
核心规律：对"差点（没）X"的解读，取决于 X 所表示事件是**说话人期望发生**（如意的事）还是**不期望发生**（如祸的事）。

- 当 X 是**不期望发生**的事件（坏事）时："差点 X" = 几乎发生但没发生；"差点没 X" = 几乎没发生（即险些发生但终究没发生）。二者都表示**事件未发生**，意思相同。
- 当 X 是**期望发生**的事件（好事）时："差点 X" = 几乎发生却没发生 = **没发生**；"差点没 X" = 几乎没发生（幸好发生了）= **发生了**。二者意思相反。

逐组分析：
(1) "他差点摔倒。" / "他差点没摔倒。"
摔倒是不期望的坏事。两句都表示"他没摔倒，只是险些摔倒"。**相同**，均指"未摔倒"。

(2) "他差点考上大学。" / "他差点没考上大学。"
考上是期望的好事。"差点考上" = 几乎考上却没考上 → **没考上**；"差点没考上" = 几乎没考上（幸好考上了）→ **考上了**。**不同**：前者未考上，后者考上了。

(3) "他差点儿死了。" / "他差点儿没死。"
死是不期望的坏事。两句都表示"他没死，只是险些丧命（勉强活下来）"。**相同**，均指"未死"。

(4) "球差点进了。" / "球差点没进。"
"进"（如射门/进球）通常是说话人期望的好事。"球差点进了" = 几乎进却没进 → **没进**；"球差点没进" = 几乎没进（幸好进了）→ **进了**。**不同**：前者没进，后者进了。

总结的语法规律：在"差点（没）+ 事件"结构中，事件的**期待极性**决定语义。"差点"倾向于否定该事件的实现；"差点没"倾向于肯定该事件的实现。对**非期望事件**，二者殊途同归（都表示未发生），故可互换；对**期望事件**，二者正好相反（"差点"=未发生，"差点没"=发生），不可互换。

【答案】
- (1) 相同：两句都表示"他没摔倒"。
- (2) 不同："差点考上"=没考上；"差点没考上"=考上了。
- (3) 相同：两句都表示"他没死（险些丧命但活下来）"。
- (4) 不同："球差点进了"=没进；"球差点没进"=进了。
规律：事件为"不期望（坏事）"时，"差点"与"差点没"同义（均表未发生）；事件为"期望（好事）"时，二者相反（"差点"=未发生，"差点没"=发生）。

---

## Q4（汉语断句）

【判断题型】这是一道汉语断句（标点歧义）题。我打算用**中文**思考，因为断句对象本身是中文无标点句，用中文分析停顿与语义最直接。

【思考】
原句："下雨天留客天留我不留"（共 10 字：下/雨/天/留/客/天/留/我/不/留）。通过在不同位置加标点，可得到主客双方不同立场的解读。下面给出 4 种合理断句。

断句一（客人诉求：希望被留）
标点：**下雨天，留客天，留我不？留！**
停顿：下雨天（，）｜留客天（，）｜留我不（？）｜留（！）
意思：下雨的日子，正是该留客人的日子；（客人问）你到底留我还是不留？——当然要留！表达客人希望留下、理直气壮被款待的态度。

断句二（主人拒绝：天留我不留）
标点：**下雨天留客，天留我不留。**
停顿：下雨天留客（，）｜天留（，）｜我不留（。）
意思：这是个下雨该留客的日子，天意要留（客人），但我（主人）不留（他）。主人借"天意"反衬自己的拒绝，明确逐客。

断句三（主人拒绝的另一种切分）
标点：**下雨天，留客，天留，我不留。**
停顿：下雨天（，）｜留客（，）｜天留（，）｜我不留（。）
意思：（客人说/或叙述）下雨了，本该留客；可天意留客，我却不挽留（或"我"指主人决定不留）。侧重"天要留、人不留"的对比，立场仍是拒绝。

断句四（主人/拟人决定不留）
标点：**下雨，天留客；天留，我不留。**
停顿：下雨（，）｜天留客（；）｜天留（，）｜我不留（。）
意思：下雨了，天意要留客；但天留归天留，我（主人）还是不留。同样表拒绝，且把"天"与"我"的意志对立起来。

（补充第五种，客人主动离开）
标点：**下雨天，留客天，留我？不留！**
意思：下雨是留客天，（问）留我吗？——不留！表示客人自尊，即便该留也选择不叨扰。

【答案】至少三种合理断句：
1. **下雨天，留客天，留我不？留！**（客人希望被留）
2. **下雨天留客，天留我不留。**（主人拒绝，天留人不留）
3. **下雨天，留客，天留，我不留。**（主人拒绝，天意留而己不留）
4. 还可：**下雨，天留客；天留，我不留。**（主人拒绝）

核心在于"留"的施事（天/我）与"留我不留"的停顿位置不同，导致"谁留、谁不留"完全相反。

---

## Q5（英语句法歧义）

【判断题型】This is an English syntax/ambiguity question about infinitival clauses. I will think in **English** because the object of analysis is an English sentence and its syntactic mechanism (logical subject of the infinitive), which is most precisely discussed using English syntactic terminology.

【思考】
(a) The sentence "The chicken is ready to eat." has at least two readings:
- Reading A (chicken as food / patient): "The chicken is ready [for someone] to eat (it)." The chicken has been cooked/prepared and is now in a state where it can be eaten. Here "the chicken" is the *understood object* of "eat."
- Reading B (chicken as agent/eater): "The chicken is ready to eat (something)." The chicken itself (personified, e.g. a live chicken) is in a state of readiness to consume food. Here "the chicken" is the *understood subject* of "eat."

(b) Syntactic mechanism — the ambiguity arises from the infinitive clause "to eat" having an unexpressed argument (often analyzed as a PRO subject or as a gap). The adjective "ready" is a *tough-adjective* that licenses an infinitival complement with a missing role. The matrix subject "the chicken" can serve two different syntactic functions relative to that infinitive:
- As the **understood object** via "tough-movement" / object gap: "The chickenᵢ is ready [PRO to eat ___ᵢ]" — the gap inside the infinitive is bound by "the chicken." This is the same construction as "The book is easy to read."
- As the **controller of PRO (subject)** of the infinitive: "The chickenᵢ is ready [PROᵢ to eat]." Here PRO = the chicken, so the chicken does the eating.
Because English does not overtly mark whether "the chicken" fills the subject or object slot of the infinitive, the sentence is structurally ambiguous.

(c) Disambiguated rewrites:
- Reading A: "The chicken is ready to be eaten." (or "The chicken is ready for us to eat.")
- Reading B: "The chicken is ready to eat (its food)." (or "The chicken is ready to start eating.")

【答案】
(a) 两种理解：① 鸡肉已经做好了，可以被吃（chicken 是 eat 的宾语）；② 鸡（拟人化）准备去吃东西（chicken 是 eat 的主语）。
(b) 歧义机制：形容词 "ready" 引导的不定式 "to eat" 含一个未显性出现的论元（PRO/空位）。"the chicken" 既可作该不定式的**控制主语**（鸡去吃），也可通过 tough-movement 作其**隐性宾语**（被吃），句法角色不确定导致歧义。
(c) 消歧改写：① "The chicken is ready to be eaten."（表可吃）；② "The chicken is ready to eat its food."（表鸡要去吃）。

---

## Q6（英语韵律）

【判断题型】This is a question about English prosody / scansion (meter identification). I will think in **English**, since the task requires syllable counting, foot division, and stress marking of an English line — terminology like "iamb" and "pentameter" is best handled in English.

【思考】
The line: "Shall I compare thee to a summer's day?"

Step 1 — Count syllables:
Shall (1) | I (2) | com (3) | pare (4) | thee (5) | to (6) | a (7) | sum (8) | mer's (9) | day (10) → **10 syllables**.

Step 2 — Divide into feet and mark stress. An iamb is an unstressed-stressed (× /) pattern. Natural pronunciation:
- Shall **I** → × /
- com **PARE** → × /
- thee **TO** → × /
- a **SUM** → × /
- mer's **DAY** → × /

So the scansion is:
× / | × / | × / | × / | × /
Shall I | comPARE | thee TO | a SUM | mer's DAY

Step 3 — Conclusion. There are exactly 5 feet, each an iamb (unstressed followed by stressed). That is the definition of iambic pentameter.

【答案】该行诗是**抑扬格五音步（iambic pentameter）**。音节数 10；音步划分为 Shall I / comPARE / thee TO / a SUM / mer's DAY，重音落在 I、PARE、TO、SUM、DAY 上（每音步均为"轻—重"的抑扬格），共 5 个抑扬格音步，符合定义。

---

## Q7（跨文化语用）

【判断题型】This is a cross-cultural pragmatics question about indirectness and politeness in (British) English workplace email. I will think in **English**, because the data is an English utterance and the analysis of attitude, linguistic signals, and a suitable reply are most naturally conducted in English.

【思考】
(a) The colleague's real attitude: This is **not** a mere gentle suggestion to "take another look." The phrasing is a polite but firm way of signaling **disagreement / a challenge to the current work**. "With all due respect" conventionally prefaces a contradiction; combined with "I would suggest looking at this again," the speaker is implying the existing version is flawed and should be reworked. The underlying message is closer to "I disagree / this needs redoing," softened for face-saving.

(b) Linguistic signals supporting this reading:
- **"with all due respect"** — a fixed hedge that typically introduces disagreement; it signals the speaker is about to contradict while staying civil.
- **"I would suggest"** — tentative mood ("would" + "suggest") softens the force, but the *content* is a directive to redo, not a neutral observation.
- **"looking at this again"** — implies the current pass is insufficient; "again" presupposes a prior attempt that did not satisfy, a veiled criticism.
- Overall register: negative-politeness / high-context indirectness typical of British workplace communication, designed to disagree without confrontation.

(c) As the head of the Chinese team, I would reply to (i) preserve face for both sides, (ii) convert vague critique into actionable points, and (iii) match the polite, indirect register without being submissive. Reply points:
- Thank them for the feedback and show it is valued ("Thanks — that's a useful flag").
- Ask for specifics rather than accepting the vague remark: "Could you point to the particular sections or assumptions you'd like us to revisit?" This turns "look again" into concrete revision items.
- Signal willingness to iterate without over-apologizing: "We'll review those parts and come back with adjustments."
- Optionally propose a short call to align quickly.
Why this works: it respects the British indirect style (no blunt defense, no excessive humility), protects the team's face, and extracts the concrete information needed to act — efficient and culturally fluent.

【答案】
(a) 同事的真实态度**并非**温和地建议"再看一遍"，而是以礼貌方式表达**不同意/认为当前成果需要重做**（一种带面子维护的委婉反驳）。
(b) 语言信号：① "with all due respect" 是引出反驳的固定客套语；② "I would suggest" 用虚拟语气弱化语气，但内容实为要求返工；③ "looking at this again" 暗示现有版本不足、"again"预设之前未达标，属含蓄批评；整体属英式高语境间接/消极礼貌策略。
(c) 作为中方负责人，回复要点：先致谢并表示重视；再追问具体需重看的部分（"能否指出具体章节/假设？"），把模糊批评转化为可执行项；表态会复核并给出修改，不过度道歉；必要时提议简短会议对齐。这样既契合对方间接风格、维护双方面子，又能拿到具体修改方向、高效推进。

---

## Q8（代码）

【判断题型】这是一道编程（回文判断 + Unicode 处理）题。我打算用**英文**思考代码逻辑（编程领域英文术语更精确），代码本身用英文书写，说明文字用中文。

【思考】
Requirements: a function `is_palindrome(s)` that (1) ignores case, (2) ignores spaces and punctuation, (3) correctly handles Chinese strings.

Key design decisions:
- **Case & fullwidth handling**: Use Unicode normalization (`unicodedata.normalize('NFKC', s)`) so that fullwidth characters (e.g. ＡＢＣ, fullwidth digits) map to their halfwidth forms, ensuring consistent comparison. For case-insensitivity, use `str.casefold()` (more thorough than `lower()`, e.g. handles German ß), or `lower()`; CJK has no case so it is unaffected.
- **Dropping spaces and punctuation**: Iterate over characters and keep only those where `ch.isalnum()` is True. In Python, `str.isalnum()` returns True for letters and digits across all scripts, including CJK unified ideographs (e.g. 上, 海) and fullwidth letters after NFKC. This naturally removes ASCII spaces, commas, periods, and Unicode punctuation (category P) and symbols.
- **Palindrome check**: After building the cleaned string, compare it with its reverse (`cleaned == cleaned[::-1]`).

Edge cases: empty string after cleaning → returns True (vacuously a palindrome); Chinese phrase "上海自来水来自海上" → all CJK, kept, reverses to itself → True.

```python
import unicodedata

def is_palindrome(s: str) -> bool:
    # NFKC normalization unifies fullwidth/halfwidth and compatibility forms
    s = unicodedata.normalize('NFKC', s)
    # Keep only letters and digits (includes CJK); this drops spaces & punctuation
    cleaned = [ch.casefold() for ch in s if ch.isalnum()]
    cleaned = ''.join(cleaned)
    return cleaned == cleaned[::-1]
```

Why `isalnum()` handles Unicode punctuation: Python's `str.isalnum()` consults the Unicode database; CJK ideographs are categorized as letters, so they pass, while commas, periods, spaces, and symbols return False and are dropped — no manual punctuation list needed.

【答案】
代码如下：

```python
import unicodedata

def is_palindrome(s: str) -> bool:
    s = unicodedata.normalize('NFKC', s)          # 统一全角/半角及兼容字形
    cleaned = [ch.casefold() for ch in s if ch.isalnum()]  # 仅保留字母与数字（含中文），丢弃空格与标点
    cleaned = ''.join(cleaned)
    return cleaned == cleaned[::-1]
```

说明：用 `unicodedata.normalize('NFKC', ...)` 将全角字符归一为半角、统一兼容字形；用 `str.casefold()`（比 `lower()` 更彻底）做大小写无关比较；用 `str.isalnum()` 判断，Python 的 Unicode 数据库把中文汉字归类为字母而通过、把空格和各类标点（Unicode 标点类 P）及符号判为否并丢弃，因此无需手工列举标点即可正确处理含中文的字符串（如 "上海自来水来自海上" 返回 True）。

---

## Q9（双向翻译）

【判断题型】这是一道双向翻译（英译中 + 中译英，且需保留比喻）题。我打算用**中文**思考，因为要比较译文的风格差异与比喻取舍，中文更便于组织说明。

【思考】
(a) "The early bird catches the worm" 英译中，3 种风格：
1. **直译口语体**："早起的鸟儿有虫吃。"——最贴近原句字面，适合日常劝人勤快、对儿童或轻松语境。
2. **文言/凝练体**："捷足者先得。"（或"先到先得"风格）——把"早起的鸟"抽象为"捷足/先到"，适合书面、强调"先行动者获利"的场合，但稍失原句的"鸟—虫"形象。
3. **意译职场体**："抢占先机者得利。" / "先人一步，方能领先。"——抛开鸟虫意象，直接传达"早行动=多收益"，适合商业、管理报告等正式语境。

(b) "三个臭皮匠，顶个诸葛亮" 中译英，要求保留原比喻（不能用"collective wisdom"这类抽象说法）：
直译保留比喻：**"Three cobblers can match Zhuge Liang."** 或 **"Three humble cobblers are a match for Zhuge Liang."**
取舍说明：诸葛亮是中华文化特有指称，英语读者可能不认识；为兼顾"保留原比喻"的要求，我优先直译并保留 cobbler 与 Zhuge Liang 的意象，必要时可加简短注解 "(Zhuge Liang: a proverbial Chinese master strategist)" 帮助理解。若完全意译为 "Two heads are better than one" 虽是英语自然等价表达，但丢失了"皮匠/诸葛亮"的原比喻，故按题目要求不优先采用。

【答案】
(a) 三种中文译文：① 早起的鸟儿有虫吃。（直译口语，日常/劝学语境）② 捷足者先得。（文言凝练，书面强调先动者获利）③ 抢占先机者得利。（意译职场，商业/管理语境）
(b) 英文保留比喻译法：**"Three cobblers can match Zhuge Liang."** 取舍：严格保留"皮匠"与"诸葛亮"的原比喻，必要时加注说明诸葛亮是足智多谋的代称；不译为 "collective wisdom" 等抽象说法，也不优先用 "Two heads are better than one"（虽自然但丢了原比喻）。

---

## Q10（英文语境计算）

【判断题型】This is a measurement/unit-conversion word problem set in an English recipe context. I will think in **English**, since all units (cup, tablespoon) and the arithmetic are given in English and are most naturally computed in English terms.

【思考】
Given: a recipe needs 3/4 cup of flour. We are making 2.5× the amount.
Step 1 — total flour needed:
3/4 cup × 2.5 = 3/4 × 5/2 = 15/8 = 1.875 cups.

Step 2 — convert everything to tablespoons, using 1 cup = 16 tbsp:
1.875 cups × 16 tbsp/cup = 30 tbsp total.

Step 3 — we have a 1/4-cup scoop and a 1-tablespoon scoop.
1/4 cup = 4 tbsp.
We want to use the 1/4-cup scoop as many times as possible, then fill the remainder with tablespoons:
30 tbsp ÷ 4 tbsp = 7 remainder 2.
So 7 scoops of 1/4 cup = 7 × 4 = 28 tbsp = 1.75 cups, plus 2 tbsp = 30 tbsp = 1.875 cups. ✓

Conclusion: use the 1/4-cup measure 7 times and the 1-tablespoon measure 2 times.

【答案】总共需要面粉 3/4 × 2.5 = 1.875 杯 = 30 汤匙（1 杯 = 16 汤匙）。1/4 杯量勺 = 4 汤匙；30 ÷ 4 = 7 余 2。因此需要：**用 1/4 杯量勺舀 7 次（共 1.75 杯 / 28 汤匙），再用 1 汤匙量勺舀 2 匙（2 汤匙）**，合计正好 1.875 杯。

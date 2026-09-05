# 限时解题测试卷 · 作答（EN 推理 / 中文答案）

---

## Q1（数列）

【思考】
The sequence is defined by a₁ = 2, a₂ = 5, and for n ≥ 3, aₙ = (aₙ₋₁ + aₙ₋₂) mod 10.
Because each term depends only on the previous two terms and every term is a digit from 0 to 9, the pair (aₙ₋₁, aₙ) can take at most 100 possible values. By the pigeonhole principle, the sequence of pairs must eventually repeat, so the whole sequence is eventually periodic. Since the recurrence is deterministic forwards and backwards, once a pair repeats the sequence is purely periodic from the start. Instead of computing up to 2026 directly, I compute terms until the initial pair (2, 5) reappears.

Compute:
a₁=2, a₂=5, a₃=(5+2)=7, a₄=(7+5)=2, a₅=(2+7)=9, a₆=(9+2)=1, a₇=(1+9)=0, a₈=(0+1)=1, a₉=(1+0)=1, a₁₀=(1+1)=2, a₁₁=(2+1)=3, a₁₂=(3+2)=5, a₁₃=(5+3)=8, a₁₄=(8+5)=3, a₁₅=(3+8)=1, a₁₆=(1+3)=4, a₁₇=(4+1)=5, a₁₈=(5+4)=9, a₁₉=(9+5)=4, a₂₀=(4+9)=3, a₂₁=(3+4)=7, a₂₂=(7+3)=0, a₂₃=(0+7)=7, a₂₄=(7+0)=7, a₂₅=(7+7)=4, a₂₆=(4+7)=1, a₂₇=(1+4)=5, a₂₈=(5+1)=6, a₂₉=(6+5)=1, a₃₀=(1+6)=7, a₃₁=(7+1)=8, a₃₂=(8+7)=5, a₃₃=(5+8)=3, a₃₄=(3+5)=8, a₃₅=(8+3)=1, a₃₆=(1+8)=9, a₃₇=(9+1)=0, a₃₈=(0+9)=9, a₃₉=(9+0)=9, a₄₀=(9+9)=8, a₄₁=(8+9)=7, a₄₂=(7+8)=5, a₄₃=(5+7)=2, a₄₄=(2+5)=7, a₄₅=(7+2)=9, a₄₆=(9+7)=6, a₄₇=(6+9)=5, a₄₈=(5+6)=1, a₄₉=(1+5)=6, a₅₀=(6+1)=7, a₅₁=(7+6)=3, a₅₂=(3+7)=0, a₅₃=(0+3)=3, a₅₄=(3+0)=3, a₅₅=(3+3)=6, a₅₆=(6+3)=9, a₅₇=(9+6)=5, a₅₈=(5+9)=4, a₅₉=(4+5)=9, a₆₀=(9+4)=3, a₆₁=(3+9)=2, a₆₂=(2+3)=5.

At a₆₁=2, a₆₂=5 we recover the initial pair (a₁, a₂) = (2, 5). Therefore the sequence has period 60, i.e. aₙ = aₙ₊₆₀ for all n. To handle the huge index 2026, reduce the index modulo 60: 2026 ÷ 60 = 33 remainder 46 (since 60×33 = 1980, and 2026 − 1980 = 46). So a₂₀₂₆ = a₄₆. From the computation a₄₆ = 6.

【答案】
数列的每一项只由前两项决定，且每项都是 0–9 的数字，因此相邻两项组成的"数对"最多只有 100 种可能，必会出现重复，从而整体呈周期性。我逐项正确计算，发现当算到第 61、62 项时又出现 (2, 5)，与第 1、2 项相同，故周期为 60。

处理巨大下标 2026 的办法是取模：2026 ÷ 60 = 33 余 46，所以 a₂₀₂₆ = a₄₆。
经计算 a₄₆ = 6。

**最终答案：a₂₀₂₆ = 6。**

---

## Q2（逻辑推理）

【思考】
There are five people (甲, 乙, 丙, 丁, 戊) ranked 1 to 5 with no ties. The rule: ranks 1 and 2 tell the truth; ranks 3, 4, 5 lie. So exactly two statements are true (those of the people in ranks 1 and 2) and three are false.

Statements:
- 甲: 甲 ≠ 5 (I am not last).
- 乙: 丙 = 1.
- 丙: 戊 = 3.
- 丁: 丁 ≠ 2.
- 戊: 甲 is ahead of 乙 (甲's number < 乙's number).

First, test whether 乙 is truthful. If 乙 tells truth, then 乙 ∈ {1,2} and 丙 = 1. But if 丙 = 1 then 丙 is also truthful, so 丙's claim 戊 = 3 is true → 戊 = 3 (a liar, consistent). The truth-tellers would be 乙 and 丙, so 乙 = 2, 丙 = 1. Then 甲, 丁, 戊 occupy ranks 3,4,5 as liars. 甲 liar ⇒ "甲≠5" is false ⇒ 甲 = 5. 丁 liar ⇒ "丁≠2" is false ⇒ 丁 = 2, but rank 2 is already 乙. Contradiction. Therefore 乙 is a liar, and 乙's claim is false, so 丙 ≠ 1.

So 乙 is a liar; the two truth-tellers are among {甲, 丙, 丁, 戊}.

Now test whether 丙 is truthful. Suppose 丙 tells truth ⇒ 丙 ∈ {1,2} and 戊 = 3 (liar). The other truth-teller must be 甲 or 丁.
- If truth-tellers are 丙 and 甲: then {丙,甲} = {1,2}, 戊 = 3, and 乙,丁 are liars (ranks 4,5). 甲 truthful ⇒ 甲≠5 (ok). 乙 liar ⇒ 丙≠1 ⇒ 丙=2, 甲=1. 丁 liar ⇒ 丁=2, but 丙=2. Contradiction.
- If truth-tellers are 丙 and 丁: then {丙,丁} = {1,2}, 戊=3, and 甲,乙 are liars (ranks 4,5). 丁 truthful ⇒ 丁≠2 ⇒ 丁=1, 丙=2. 乙 liar ⇒ 丙≠1 (ok, 丙=2). 甲 liar ⇒ 甲=5, so 乙=4. Now 戊 (rank 3, liar) says "甲 ahead of 乙": 甲=5, 乙=4, so 甲 is actually behind 乙, the statement is false — consistent with 戊 being a liar. This assignment works: 丁=1, 丙=2, 戊=3, 乙=4, 甲=5.

I verify the remaining alternatives to ensure uniqueness. If 丙 is a liar, the truth-tellers are two of {甲,丁,戊}:
- 甲 & 丁 truthful ⇒ 甲,丁 ∈ {1,2}; 戊 liar (rank 3,4,5). 戊's statement "甲 ahead of 乙" must be false, but 甲∈{1,2} and 乙∈{3,4,5} so 甲 is always ahead ⇒ statement true ⇒ contradiction.
- 甲 & 戊 truthful ⇒ 丁 liar ⇒ 丁=2, but ranks 1,2 are taken by 甲,戊 ⇒ contradiction.
- 丁 & 戊 truthful ⇒ 丁=1, 戊=2 (since 丁≠2). 甲 liar ⇒ 甲=5. 戊 truthful ⇒ 甲 ahead of 乙, but 甲=5, 乙∈{3,4} ⇒ 甲 behind ⇒ statement false ⇒ contradiction.

Thus the only consistent assignment is 丁=1, 丙=2, 戊=3, 乙=4, 甲=5. The narrowing strategy: (1) show 乙 must be a liar to avoid contradiction, fixing 丙≠1; (2) test 丙's truth value; (3) within 丙-truthful branch, the 丙&丁 pairing is the only one surviving the liar constraints on 丁 and 甲; (4) eliminate all 丙-liar branches via the 戊-statement contradiction or rank clash.

【答案】
推理缩小范围的步骤：
1. 先判断乙是否说真话。若乙说真话，则丙=1，丙也说真话，推出戊=3（说谎者），且乙=2、丙=1；此时甲、丁、戊为第3/4/5名（说谎）。但丁说谎 ⇒ "丁≠2"为假 ⇒ 丁=2，与丙=2冲突。故**乙必为说谎者**，且丙≠1。
2. 两名说真话者只能在 {甲,丙,丁,戊} 中。
3. 假设丙说真话 ⇒ 丙∈{1,2} 且戊=3。另一说真话者只能是甲或丁：
   - 若甲、丙说真话 ⇒ 丁说谎 ⇒ 丁=2，与丙=2冲突，排除。
   - 若丙、丁说真话 ⇒ 丁真话 ⇒ 丁≠2 ⇒ 丁=1、丙=2；甲说谎 ⇒ 甲=5，则乙=4；戊（第3名，说谎）说"甲比乙靠前"，而甲=5、乙=4，甲其实靠后，命题为假，符合戊说谎。**此分支成立。**
4. 若丙说谎，则说真话者在 {甲,丁,戊} 中取两个，逐一验证均因"戊命题"或名次冲突而被排除。

**最终名次：丁第1，丙第2，戊第3，乙第4，甲第5。**

---

## Q3（汉语语义）

【思考】
The construction 差点 / 差点儿 (almost) plus an event X behaves differently depending on whether X is a desirable (good) or undesirable (bad) event.
- When X is undesirable (a "bad" event one wants to avoid): both "差点X" and "差点没X" mean X did NOT happen. The "没" does not reverse the meaning; both describe a narrowly avoided bad outcome.
- When X is desirable (a "good" event one wants to happen): the two forms diverge. "差点X" means X almost happened but did NOT (a near miss / failure); "差点没X" means X almost failed to happen but DID happen (a narrow success).

Apply to each pair:
(1) 摔倒 (fall) is undesirable. 他差点摔倒 = he almost fell, did not fall. 他差点没摔倒 = he almost didn't fall, also did not fall. SAME.
(2) 考上大学 (get admitted to university) is desirable. 他差点考上大学 = almost got in, did NOT get in. 他差点没考上大学 = almost didn't get in, DID get in (barely). DIFFERENT.
(3) 死 (die) is undesirable. 他差点儿死了 = he almost died, did not die. 他差点儿没死 = he almost didn't die, also did not die. SAME. (差点儿 = 差点)
(4) 球进 (a goal is scored) is a positive/desirable outcome for the attacking side. 球差点进了 = almost went in, did NOT go in. 球差点没进 = almost didn't go in, DID go in (barely). DIFFERENT.

【答案】
逐组判断与含义：
- (1) 相同。两句都表示"他没摔倒"。摔倒是不希望发生的坏事，"差点"与"差点没"在此都指险情被避免。
- (2) 不同。"他差点考上大学"＝没考上（差一点就考上了，可惜没成）；"他差点没考上大学"＝考上了（险些没考上，最终勉强考上）。
- (3) 相同。两句都表示"他没死"。死是不希望发生的坏事，两种说法都指死里逃生。
- (4) 不同。"球差点进了"＝没进（险些破门）；"球差点没进"＝进了（勉强入网）。进球对进攻方是好事。

**语法规律总结：** "差（一）点（没）X" 的语义取决于 X 是否为"如意/好事"。
- 若 X 是**不如意（坏事）**：加不加"没"意思一样，都表示 X **没有**发生（险情幸免）。
- 若 X 是**如意（好事）**：加"没"会改变意思——"差点X"表示 X **没**发生（功亏一篑），"差点没X"表示 X **发生**了（勉强力成）。

---

## Q4（汉语断句）

【思考】
The unpunctuated string "下雨天留客天留我不留" is a classic ambiguous sentence. By inserting different punctuation and choosing different subjects/objects for the verbs 留 (keep/stay) and different scopes for 我 (me/guest vs. speaker), we get several coherent readings. I will list at least three, giving the punctuation, the spoken pause pattern, and who keeps/stays whom.

【答案】
给出 4 种合理断句（至少 3 种）：

**断句一（疑问，问主人留不留客）：**
> 下雨天，留客天，留我不留？
- 停顿：下雨天（，）留客天（，）留我（？）不留（？）
- 意思：下雨的日子正是留客的日子，你到底留我还是不留我？——**主人被问**，焦点在"主人是否留客"。

**断句二（客人说"我不留"，即客要告辞）：**
> 下雨天留客，天留我不留。
- 停顿：下雨天留客（，）天留我（，）不留（。）
- 意思：下雨天本该留客，老天要留我，但我（客）不肯留——**我（客人）不留（走）**。焦点在客人执意离开。

**断句三（主人拒绝留客）：**
> 下雨天，留客天，留我？不留！
- 停顿：下雨天（，）留客天（，）留我（？）不留（！）
- 意思：下雨天虽是留客天，可留我？不留下！——**主人说"我不留（你）"**，明确拒客。

**断句四（主人以"天意"为由拒绝）：**
> 下雨，天留客；天留，我不留。
- 停顿：下雨（，）天留客（；）天留（，）我不留（。）
- 意思：下雨了，老天要留客；可老天留归老天留，我（主人）还是不留（你）。——同样是**主人拒绝**，但把"天留"当成与自己意志无关的外力。

小结：同一句靠标点与"留"的施受关系（谁留谁）以及"我"指代（客人 vs 主人）产生完全不同的语义。

---

## Q5（英语句法歧义）

【思考】
(a) The sentence "The chicken is ready to eat." has at least two readings:
Reading 1 (food): The chicken (the cooked meat) is ready [for someone] to eat it. ⇒ The chicken is prepared and can be eaten.
Reading 2 (animal): The chicken (the live bird) is ready [for itself] to eat (something). ⇒ The chicken is hungry / wants to eat.

(b) Syntactic mechanism: The adjective "ready" takes an infinitival complement "to eat". This infinitive has an implicit logical subject (PRO) and a logical object. The ambiguity arises because:
- In Reading 1, "the chicken" is the semantic PATIENT/object of "eat" (what gets eaten), while the eater is an implicit arbitrary agent (PRO arb, i.e., people in general). This is an object-control / raising-like interpretation where the matrix subject is the theme of the infinitive.
- In Reading 2, the implicit subject PRO of "to eat" is CONTROLLED by the matrix subject "the chicken" (subject control): "the chicken is ready [for the chicken] to eat". Here the chicken is the agent/eater.
So the core mechanism is ambiguity in the control relation of the infinitival PRO (and correspondingly whether "the chicken" is the eater or the eaten), combined with the optionality of an explicit object.

(c) Disambiguated rewrites:
- Food reading: "The chicken is ready to be eaten." (or "The chicken is ready for us to eat." / "The chicken is ready for eating.")
- Animal reading: "The chicken is ready to eat [its food]." (or "The chicken is hungry and ready to eat.")

【答案】
(a) 两种理解：
1. **食物义**：这只鸡（做好的鸡肉）已经可以吃了。——"鸡"是"吃"的受事。
2. **动物义**：这只鸡（活鸡）饿了，准备去吃（东西）了。——"鸡"是"吃"的施事。

(b) 歧义的句法机制：形容词 ready 带不定式补足语 to eat，其逻辑主语 PRO 存在**控制关系歧义**：
- 食物义中，the chicken 是不定式 to eat 的**受事（被吃者）**，吃的人是隐含的任意施事（PRO arb，泛指"人们"）；
- 动物义中，不定式 to eat 的隐含主语 PRO 由矩阵主语 the chicken **主语控制**（subject control），即"鸡准备[让自己]去吃"。
本质是不定式 PRO 的控制对象（以及 the chicken 充当施事还是受事）不确定造成的结构歧义。

(c) 消歧改写：
- 食物义：*The chicken is ready to be eaten.*（或 *The chicken is ready for us to eat.*）
- 动物义：*The chicken is ready to eat [its food].*（或 *The chicken is hungry and ready to eat.*）

---

## Q6（英语韵律）

【思考】
The line is "Shall I compare thee to a summer's day?" I count syllables word by word:
Shall (1) / I (2) / com (3) - pare (4) / thee (5) / to (6) / a (7) / sum (8) - mer's (9) / day (10). Total = 10 syllables.
Iambic pentameter requires five metrical feet, each foot being an iamb (an unstressed syllable followed by a stressed syllable: × ′).
Mark stress placement:
- Shall (×) I (′) → foot 1
- com (×) PARE (′) → foot 2
- thee (×) TO (′) → foot 3
- a (×) SUM (′) → foot 4
- mer's (×) DAY (′) → foot 5
So the pattern is: ×′ | ×′ | ×′ | ×′ | ×′ — five iambic feet. This matches the standard scansion of Shakespeare's Sonnet 18, line 1.

【答案】
音节数与音步划分（× 表轻读，′ 表重读）：
> Shall I / comPARE / thee TO / a SUM / mer's DAY
> × ′  |  × ′   |  × ′  |  × ′  |  × ′

- 音节数：共 **10** 个音节（Shall·I·com·pare·thee·to·a·sum·mer's·day）。
- 音步：5 个，全部为**抑扬格（iamb = 轻+重）**。
- 重音位置落在 I、PARE、TO、SUM、DAY 上。

**结论：是抑扬格五音步（iambic pentameter）。** 这正是莎士比亚《 sonnet 18》的开篇句。

---

## Q7（跨文化语用）

【思考】
(a) The real attitude: This is NOT merely a mild suggestion to "look again." The phrase "with all due respect" is a conventionalized politeness hedge that typically prefaces disagreement or contradiction. The speaker is in fact signaling disagreement with the recipient's work and implying it needs re-examination. The true message is closer to "I think this is wrong; please reconsider," wrapped in politeness.

(b) Linguistic signals supporting this:
- "with all due respect": a formulaic marker that conventionally introduces or accompanies disagreement/criticism while preserving surface politeness; it is a red flag that the speaker is contradicting you.
- "I would suggest": the modal "would" and the verb "suggest" downgrade a direct assertion into a softened directive, often masking a stronger criticism ("you should redo this").
- "looking at this again": the word "again" implies a prior look was insufficient; it presupposes rework is needed.
- Overall indirectness is characteristic of British professional politeness, where disagreement is encoded indirectly.

(c) As the Chinese team lead, I would:
1. Stay calm; read the true intent (disagreement), not just the surface soft tone.
2. Reply politely to save face: thank them for the input.
3. Ask for concrete specifics ("Could you point to the parts that concern you?") to avoid vague, repeated rework.
4. Either clarify the rationale behind our approach with evidence, or agree to review/revise the specific points.
Why: British communication relies on hedging; recognizing the real disagreement while matching the politeness level prevents miscommunication and escalation, and requesting specifics protects the team from wasted effort.

【答案】
(a) 真实态度：**并不是温和地建议"再看一遍"**。"with all due respect" 是英式职场中典型的"先礼后驳"套话，往往预示着接下来（或整句）是在**表示不同意/提出批评**。真实意思是："我认为这有问题，请你重新考虑/重做。"

(b) 支持该判断的语言信号：
- **"with all due respect"**：约定俗成的礼貌缓冲语，专门用于"表面上客气、实际上要反驳"的场合，是"我要唱反调了"的信号。
- **"I would suggest"**：用情态动词 would 加 suggest 把强硬指令弱化为软建议，常用来掩盖更尖锐的批评（"你该重做"）。
- **"looking at this again"** 中的 **again**：暗示之前看过但不够好，预设了"需要返工"。
- 整体高度间接，符合英式职场"用含蓄表达异议"的习惯。

(c) 作为中方团队负责人，我会这样回复（要点）：
1. **保持冷静**，识破其"客气外表下的反对"，不把它当普通建议。
2. **礼貌接话、给足面子**：先感谢对方反馈。
3. **索要具体依据**："能否指出具体让你担忧的部分？"避免泛泛返工。
4. **用证据澄清我方思路**，或就具体点同意复核/修改。
原因：英式沟通靠含蓄与缓冲，准确读懂真实异议、并以同等礼貌层级回应，既能避免误会升级，又能通过"要具体"防止团队做无用功。

---

## Q8（代码）

【思考】
I need a Python function `is_palindrome(s)` that ignores case, spaces, and punctuation, and correctly handles Chinese strings. In Python 3, strings are Unicode. The method `str.isalnum()` returns True for letters and digits; crucially, CJK ideographs (e.g., 上, 海) are classified as letters, so they pass `isalnum()`, while spaces and punctuation (including Unicode punctuation such as ，。！ and the full-width space U+3000) return False and are dropped. For case insensitivity, `str.casefold()` is preferable to `lower()` because it handles more Unicode case mappings (e.g., German ß → ss); for Chinese it is a no-op, which is fine. After filtering to alnum characters and case-folding, I compare the cleaned string with its reverse.

【答案】
代码如下：

```python
def is_palindrome(s):
    # 只保留"字母和数字"：中文汉字（CJK）被 isalnum 判定为字母，会保留；
    # 空格与中英文标点（含 Unicode 标点如 ，。！、全角空格）都被过滤掉。
    cleaned = [ch.casefold() for ch in s if ch.isalnum()]
    seq = ''.join(cleaned)
    return seq == seq[::-1]
```

说明（Unicode 处理）：
- **大小写**：用 `casefold()` 而非 `lower()`，因为它对 Unicode 更彻底（如德语 ß→ss），对中文则是空操作，不影响。
- **标点与空格**：依赖 `str.isalnum()`。Python 3 字符串是 Unicode，汉字属于"字母"范畴，`isalnum()` 返回 True 会被保留；而 ASCII 空格、英文标点以及中文/全角标点（，。！、U+3000 全角空格等）均返回 False，被剔除。
- **回文判断**：清洗后字符串与其反转 `seq[::-1]` 比较即可。例如 `"上海自来水来自海上"` 清洗后仍是原串，反转相等，返回 `True`。

---

## Q9（双向翻译）

【思考】
(a) "The early bird catches the worm" → Chinese. I provide three styles with different registers/use cases:
1. Literal everyday proverb: 早起的鸟儿有虫吃。 (casual, used to encourage punctuality/diligence, e.g., to children or in daily life).
2. Idiom-like / competitive context: 捷足先登。 (concise classical idiom; used in business or competition to stress first-mover advantage).
3. Colloquial pragmatic advice: 先下手为强。 / 赶早不赶晚。 (used for queuing, sales, grabbing resources).

(b) "三个臭皮匠，顶个诸葛亮" → English, preserving the metaphor (not abstract "collective wisdom"). A faithful rendering keeps both "cobbler" and "Zhuge Liang": e.g., "Three cobblers together can match Zhuge Liang." Trade-off: Zhuge Liang is a culture-specific figure (a proverbial wise strategist) unknown to many English readers, so one may add a brief gloss, but the metaphor itself is retained. I avoid replacing it with the abstract "collective wisdom."

【答案】
(a) 英文谚语 "The early bird catches the worm" 的中译（3 种风格）：
1. **直译·常用俗语**：早起的鸟儿有虫吃。——适用于日常劝勉、鼓励孩子/同事勤快守时。
2. **成语化·竞争场景**：捷足先登。——适用于商业、竞赛等强调"抢占先机/先发优势"的正式或书面场合。
3. **意译·务实劝告**：先下手为强。（或"赶早不赶晚"。）——适用于排队、抢购、抢占资源等讲求"早行动"的具体情境。

(b) 中文俗语 "三个臭皮匠，顶个诸葛亮" 的英译（保留原比喻）：
> *Three cobblers together can match Zhuge Liang.*
>（或 *Three humble cobblers' wits can equal Zhuge Liang the master strategist.*）

取舍说明：题目要求保留原比喻、不能译成"集体智慧"这类抽象说法，因此我保留了 **cobbler（皮匠）** 与 **Zhuge Liang（诸葛亮）** 两个意象。代价是诸葛亮是文化专有形象，英语读者可能不熟；可考虑加简短注释（"Zhuge Liang, a proverbial wise strategist"），但本体比喻必须留存，以传达"平凡多人合力可抵一位智者"的意象，而非抽空为抽象概念。

---

## Q10（英文语境计算）

【思考】
The recipe needs 3/4 cup of flour. I am making 2.5 times the amount.
Total flour needed = (3/4) × 2.5 = 0.75 × 2.5 = 1.875 cups.
Given 1 cup = 16 tablespoons (tbsp), convert: 1.875 cups × 16 tbsp/cup = 30 tbsp.
I have a 1/4-cup scoop and a 1-tablespoon scoop. Note 1/4 cup = 4 tbsp.
Using the 1/4-cup scoop: 1.875 cups ÷ 0.25 cup = 7.5 scoops, so I take 7 full scoops = 7 × 0.25 = 1.75 cups = 28 tbsp.
Remaining = 1.875 − 1.75 = 0.125 cups = 2 tbsp.
So I need the 1-tablespoon scoop 2 times.
Check: 7 × 4 tbsp + 2 × 1 tbsp = 28 + 2 = 30 tbsp = 1.875 cups. Correct.

【答案】
换算过程：
1. 总面粉量 = 3/4 杯 × 2.5 = 0.75 × 2.5 = **1.875 杯**。
2. 已知 1 杯 = 16 汤匙，故 1.875 杯 = 1.875 × 16 = **30 汤匙**。
3. 1/4 杯量勺 = 4 汤匙。先用 1/4 杯量勺：1.875 ÷ 0.25 = 7.5 次，取满 7 次 = 7 × 0.25 = 1.75 杯 = 28 汤匙。
4. 剩余 = 1.875 − 1.75 = 0.125 杯 = 2 汤匙，用 1 汤匙量勺舀 **2 匙**。
5. 校验：7×4 + 2×1 = 30 汤匙 = 1.875 杯 ✓

**最终答案：用 1/4 杯量勺舀 7 次，再用 1 汤匙量勺舀 2 匙。**

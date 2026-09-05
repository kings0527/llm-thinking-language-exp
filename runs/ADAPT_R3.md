# 限时解题测试答卷（顺序：Q4, Q1, Q7, Q2, Q9, Q5, Q3, Q10, Q6, Q8）

---

## Q4（汉语断句）

【判断题型】这是一道汉语断句（无标点歧义句切分）题，属于经典句读/歧义分析；我打算用**中文**思考，因为材料是中文句子，用中文讨论停顿与语义最直观。

【思考】
原句："下雨天留客天留我不留"，共 9 个字，无标点，可通过不同停顿切分成语义相反或相异的句子。关键是"留"既可作"（主人）留客"，也可作"（客人）留下"；"我"既可指主人也可指客人；句末可成陈述也可成反问。逐条构造：

1. **主人逐客读法**：把前半当作常理"下雨天应当留客"，后半"天留我不留"理解为"天意要留（客），但我不留（客）"。
2. **客人求留读法**：把"下雨天""留客天"并列，当作两句话，再用"留我不？留！"构成自问自答。
3. **客人反问读法**：把整句理解为"下雨天本就是留客天，（你到底）留我不留？"
4. **对仗逐客读法**：拆成"下雨，天留客；天留，我不留"，主谓结构更显式。

下面给出四种（满足"至少 3 种"）。

【答案】
以下给出 4 种合理断句：

1. **下雨天留客，天留我不留。**
   - 停顿：下雨天留客，／天留我／不留。
   - 意思（主人逐客）：雨天本该留客，但（即便）天意要留（客），我（主人）也不留你。→ **不留客**。

2. **下雨天，留客天，留我不？留！**
   - 停顿：下雨天，／留客天，／留我／不？／留！
   - 意思（客人求留）：今天下雨，正是该留客的日子；（你）留不留我？（我想要的答案是）留！→ **留客**。

3. **下雨天留客天，留我不留？**
   - 停顿：下雨天留客天，／留我／不留？
   - 意思（客人反问）：下雨天本来就是留客的天，（你到底）留我还是不留我？→ 隐含**希望被留**。

4. **下雨，天留客；天留，我不留。**
   - 停顿：下雨，／天留客；／天留，／我不留。
   - 意思（对仗逐客）：下雨了，天意要留客；但天意虽留，我（主人）却不留。→ **不留客**。

---

## Q1（数列）

【判断题型】这是一道数列递推与周期性找规律题；我打算用**中文**思考，便于逐步推导并解释如何处理巨大下标 2026。

【思考】
已知：a₁=2，a₂=5，aₙ=(aₙ₋₁+aₙ₋₂) mod 10（n≥3）。

**处理巨大下标的思路**：每一项只由它前面相邻两项决定，而相邻两项构成的"状态对"(aₙ₋₁, aₙ)只有 10×10=100 种可能。只要某个状态对重现，序列就会从该处开始完全周期重复。我只需算出序列，直到状态对(2,5)再次（除开头外）出现，即得周期；再把 2026 对周期取余，映射到前若干项即可。

逐项计算（保留 aₙ 与状态对）：
- a₁=2, a₂=5 → 对(2,5)
- a₃=(5+2)=7 → 对(5,7)
- a₄=(7+5)=12→2 → 对(7,2)
- a₅=(2+7)=9 → 对(2,9)
- a₆=(9+2)=11→1 → 对(9,1)
- a₇=(1+9)=10→0 → 对(1,0)
- a₈=(0+1)=1 → 对(0,1)
- a₉=(1+0)=1 → 对(1,1)
- a₁₀=(1+1)=2 → 对(1,2)
- a₁₁=(2+1)=3 → 对(2,3)
- a₁₂=(3+2)=5 → 对(3,5)
- a₁₃=(5+3)=8 → 对(5,8)
- a₁₄=(8+5)=13→3 → 对(8,3)
- a₁₅=(3+8)=11→1 → 对(3,1)
- a₁₆=(1+3)=4 → 对(1,4)
- a₁₇=(4+1)=5 → 对(4,5)
- a₁₈=(5+4)=9 → 对(5,9)
- a₁₉=(9+5)=14→4 → 对(9,4)
- a₂₀=(4+9)=13→3 → 对(4,3)
- a₂₁=(3+4)=7 → 对(3,7)
- a₂₂=(7+3)=10→0 → 对(7,0)
- a₂₃=(0+7)=7 → 对(0,7)
- a₂₄=(7+0)=7 → 对(7,7)
- a₂₅=(7+7)=14→4 → 对(7,4)
- a₂₆=(4+7)=11→1 → 对(4,1)
- a₂₇=(1+4)=5 → 对(1,5)
- a₂₈=(5+1)=6 → 对(5,6)
- a₂₉=(6+5)=11→1 → 对(6,1)
- a₃₀=(1+6)=7 → 对(1,7)
- a₃₁=(7+1)=8 → 对(7,8)
- a₃₂=(8+7)=15→5 → 对(8,5)
- a₃₃=(5+8)=13→3 → 对(5,3)
- a₃₄=(3+5)=8 → 对(3,8)
- a₃₅=(8+3)=11→1 → 对(8,1)
- a₃₆=(1+8)=9 → 对(1,9)
- a₃₇=(9+1)=10→0 → 对(9,0)
- a₃₈=(0+9)=9 → 对(0,9)
- a₃₉=(9+0)=9 → 对(9,9)
- a₄₀=(9+9)=18→8 → 对(9,8)
- a₄₁=(8+9)=17→7 → 对(8,7)
- a₄₂=(7+8)=15→5 → 对(7,5)
- a₄₃=(5+7)=12→2 → 对(5,2)
- a₄₄=(2+5)=7 → 对(2,7)
- a₄₅=(7+2)=9 → 对(7,9)
- a₄₆=(9+7)=16→6 → 对(9,6)
- a₄₇=(6+9)=15→5 → 对(6,5)
- a₄₈=(5+6)=11→1 → 对(5,1)
- a₄₉=(1+5)=6 → 对(1,6)
- a₅₀=(6+1)=7 → 对(6,7)
- a₅₁=(7+6)=13→3 → 对(7,3)
- a₅₂=(3+7)=10→0 → 对(3,0)
- a₅₃=(0+3)=3 → 对(0,3)
- a₅₄=(3+0)=3 → 对(3,3)
- a₅₅=(3+3)=6 → 对(3,6)
- a₅₆=(6+3)=9 → 对(6,9)
- a₅₇=(9+6)=15→5 → 对(9,5)
- a₅₈=(5+9)=14→4 → 对(5,4)
- a₅₉=(4+5)=9 → 对(4,9)
- a₆₀=(9+4)=13→3 → 对(9,3)
- a₆₁=(3+9)=12→2 → 对(3,2)
- a₆₂=(2+3)=5 → 对(2,5)

在第 61、62 项，状态对重新变回(2,5)，与第 1、2 项完全相同，因此序列从第 1 项起以 **周期 60** 循环，即 aₙ₊₆₀ = aₙ。

现在求 a₂₀₂₆：2026 ÷ 60 = 33 余 46（因为 60×33=1980，2026−1980=46），故 a₂₀₂₆ = a₄₆ = 6（由上面 a₄₆=6）。

【答案】
**a₂₀₂₆ = 6。**
处理方法：序列由相邻两项唯一决定，状态对只有 100 种，必然周期循环；逐步计算发现状态对(2,5)在第 61、62 项重现，故周期为 60，于是把巨大下标 2026 对 60 取余得 46，a₂₀₂₆ = a₄₆ = 6。

---

## Q7（跨文化语用）

【判断题型】这是一道跨文化语用学/言语行为分析题（英语礼貌策略与间接表达）；我打算用**英文**思考，因为原始语料是英文邮件，需要逐一审视其英语语用信号。

【思考】
The sentence: *"I would suggest looking at this again, with all due respect."*

**(a) The colleague's real attitude.**
This is NOT merely a gentle, neutral suggestion to "take another look." In British professional discourse, the cluster of hedges here functions as a polite but firmly critical or oppositional move. The speaker is signaling disagreement with, or serious doubt about, the recipient's current work/product, and is pushing back. "With all due respect" is a conventionalized preface to a face-threatening act — it routinely introduces contradiction or criticism, not agreement. So the underlying message is closer to: "I disagree / I think this is wrong or inadequate, and you should reconsider it," wrapped in polite indirectness.

**(b) Linguistic signals supporting this reading.**
- *"I would suggest"*: the modal "would" + tentative verb "suggest" is a hedge that softens what is effectively a directive or correction. It lets the speaker avoid saying "you are wrong" outright.
- *"with all due respect"*: a pragmatic formula (disclaimer marker) that conventionally precedes disagreement or criticism; its very presence signals an imminent face-threatening act.
- The combination of multiple politeness markers (modal hedge + conventional disclaimer) is typical when a British speaker wants to deliver a negative assessment while preserving both parties' face. The excess of mitigation itself is the cue that something critical is being said.
- Indirectness/understatement: rather than stating the problem, the speaker implies "there is something wrong that you should re-examine," leaving the recipient to infer the criticism.

**(c) How I (as the Chinese team lead) would reply.**
Reply points:
1. Stay calm and do not take it at face value as a friendly tip — read the implied criticism.
2. Thank them for the feedback and acknowledge the concern professionally.
3. Ask for concrete specifics: which parts, what the exact worry is, what outcome they expect.
4. Propose a short follow-up (call or meeting) to go through the issues, showing openness without conceding fault prematurely.
5. Keep tone measured, avoid defensiveness or blunt contradiction, and avoid over-apologizing (which could read as admitting error).

Reason: British indirectness means the literal words understate the real message; as the lead I must decode the implied critique, respond with substance (specifics, not empty politeness), and manage "face" for both sides — neither dismissing the concern nor needlessly conceding.

【答案】
(a) 这位同事并非只是温和地建议"再看一遍"，而是在礼貌外壳下表达**反对/质疑**，潜台词是"我认为这有问题，你该重新考虑"。
(b) 语言信号："I would suggest" 用情态动词 would + suggest 作缓和（hedge），把批评包装成建议；"with all due respect" 是 Conventionalized 的"先礼后驳"标记，专用于引出异议或批评；多重礼貌标记叠加本身就是"即将说重话"的提示；整体用间接/含蓄方式让对方自己体会否定意味。
(c) 作为中方负责人，回复要点：先冷静读懂隐含批评、不过度字面理解；礼貌致谢并认可其关注；**索要具体问题点**（哪部分、担心什么）；提议短会/通话逐条对接；语气沉稳，不 defensive 也不过度道歉。理由：英式含蓄使字面弱于真实意图，须"听弦外之音"，用实质内容（而非空客气）回应，并兼顾双方面子。

---

## Q2（逻辑推理）

【判断题型】这是一道真假话排位逻辑推理题；我打算用**中文**思考，便于逐人排除、缩小范围。

【思考】
五人甲、乙、丙、丁、戊，名次 1–5 无并列。
陈述：
- 甲：我不是最后一名（≠5）。
- 乙：丙是第一名（丙=1）。
- 丙：戊是第三名（戊=3）。
- 丁：我不是第二名（≠2）。
- 戊：甲的名次比乙靠前（甲号 < 乙号）。

规则：第 1、2 名说真话（T），第 3、4、5 名说假话（F）。即**恰有两人说真话、三人说假话**，且说真话者必居 1、2 名。

**第一步：分析乙。**
若乙说真话（乙∈{1,2}），则丙=1。乙既真且≠1（丙已占1），故乙=2。丙=1 为真→丙说真话→戊=3。戊=3 是 F，其陈述"甲比乙靠前"必假→甲不在乙前→甲号>乙号。此时 1、2 名已为丙、乙，甲必∈{4,5}，且甲=F，其陈述"我不是最后"必假→甲=5。剩丁=4（F）。但丁=4 时"我不是第二名"为真，与丁是 F 矛盾。**故乙不能说真话，乙必为 F（乙∈{3,4,5}）。** 由乙=F 得"丙=1"为假→**丙≠1**。

**第二步：分析丙。**
若丙=F（丙∈{3,4,5}），则"戊=3"为假→戊≠3。又乙=F，则三名 F 为乙、丙、戊，T 必为甲、丁=1、2。甲=T→"我不是最后"真（成立）。丁=T→"我不是第二名"必真→丁≠2→**丁=1，甲=2**。戊=F 且戊≠3→戊∈{4,5}。戊陈述"甲比乙靠前"必假→甲不在乙前。但甲=2，乙是 F∈{3,4,5}即乙号>2，所以甲必在乙前，使戊陈述为真，矛盾。**故丙不能说假话，丙必为 T（丙∈{1,2}）。**

**第三步：丙=T。**
丙=T→戊=3（且戊=3 是 F）。又丙≠1（第一步结论），故**丙=2**（T）。另一 T（第1名）只能是甲或丁。
- 若甲=1（T）：甲陈述真（成立）。戊=F 陈述"甲比乙靠前"必假→甲不在乙前。但甲=1，乙无论几名都在甲后，甲必在乙前→戊陈述真，矛盾。故甲≠1。
- 故**丁=1**（T）。丁陈述"我不是第二名"→丁=1 为真，成立。
于是 1、2 名为丁、丙，3 为戊，剩甲、乙占 4、5（均为 F）。
戊=F 陈述"甲比乙靠前"必假→甲不在乙前→甲号>乙号→**甲=5，乙=4**。

**第四步：校验全部。**
- 丁=1(T)：≠2 ✓真。
- 丙=2(T)：戊=3 ✓真。
- 戊=3(F)：甲(5)比乙(4)靠前？否 ✓假。
- 乙=4(F)：丙=1？否 ✓假。
- 甲=5(F)：我不是最后？否（是最后）✓假。
全部一致，唯一解。

【答案】
五人名次（从第一到第五）：**丁、丙、戊、乙、甲**。即：丁第一，丙第二，戊第三，乙第四，甲第五。

---

## Q9（双向翻译）

【判断题型】这是一道双向翻译题（英译中保留风格、中译英保留比喻）；我打算用**中文**思考，便于对照中英文语义与风格取舍。

【思考】
**(a) "The early bird catches the worm" 译成中文，3 种风格：**
1. **直译通俗版：「早起的鸟儿有虫吃。」** —— 最贴近原文"鸟/虫"意象，口语化，适合儿童教育、日常劝人勤快。
2. **成语雅化版：「捷足先登。」** —— 用四字成语，书面/正式场合更凝练，强调"抢先者得利"，但丢失了鸟虫的具体画面。
3. **意译励志版：「抢占先机者胜。」／「早行动者得回报。」** —— 脱离原意象、提炼为通用励志格言，适合商务、管理或演讲语境。

**(b) "三个臭皮匠，顶个诸葛亮" 译成英文，保留比喻：**
直译并保留原比喻：**"Three cobblers pooling their wits can surpass Zhuge Liang."**（或 "Three humble cobblers together can match Zhuge Liang."）
取舍说明：题目要求保留原有比喻，所以不能译成 "collective wisdom" 这类抽象说法。我保留 "cobblers"（皮匠/鞋匠）与 "Zhuge Liang"（诸葛亮）两个文化专有项，以传达"平凡多人合力胜过一个智者"的画面；代价是英语读者可能不熟悉诸葛亮，必要时可加简短注释（如 the master strategist），但比喻本体不变。译文用 "pooling their wits / together" 体现"合"与"顶（胜/匹敌）"的含义。

【答案】
(a) 三种中文译法：
1. 直译通俗：「早起的鸟儿有虫吃。」（口语、儿童教育）
2. 成语雅化：「捷足先登。」（书面、正式）
3. 意译励志：「抢占先机者胜。」（商务、励志）

(b) 英文译文（保留比喻）：**"Three cobblers pooling their wits can surpass Zhuge Liang."** 取舍：保留 "cobblers" 与 "Zhuge Liang" 原比喻，不抽象为 "collective wisdom"；用 "pooling their wits" 译"臭皮匠合力"、"surpass/match" 译"顶个"，必要时可括注 the master strategist 帮助英语读者理解，但比喻本体不变。

---

## Q5（英语句法歧义）

【判断题型】这是一道英语句法歧义分析题（不定式逻辑主语/控制结构）；我打算用**英文**思考，因为需精确描述英语句法机制。

【思考】
Sentence: *"The chicken is ready to eat."*

**(a) Two readings.**
- Reading 1 (food sense): The cooked chicken is ready **for someone to eat it** → "The chicken is ready to be eaten." The chicken is the *theme/object* of eating.
- Reading 2 (animal sense): The live chicken is ready **to eat (something)** → "The chicken is ready to consume food." The chicken is the *agent/subject* that does the eating.

**(b) Syntactic mechanism.**
The adjective *ready* takes an infinitival complement (*to eat*). This infinitive has an implicit PRO subject whose reference is controlled. The ambiguity lies in the relation between the matrix subject *the chicken* and the infinitive:
- In Reading 1, *the chicken* is the **object** of *eat* (an instance of "tough-movement"/object-to-subject raising: *the chicken* is interpreted as the logical object of the infinitive, while PRO is an arbitrary/external agent, e.g. "for someone to eat it").
- In Reading 2, *the chicken* is the **subject** of *eat* (PRO = *the chicken*; the chicken itself will perform the eating).
Because the NP *the chicken* can saturate either the subject or the object role of the infinitive, the sentence is structurally ambiguous.

**(c) Disambiguated rewrites.**
- Reading 1: "The chicken is ready to be eaten." / "The chicken is ready for us to eat."
- Reading 2: "The chicken is ready to eat its food." / "The chicken is ready to start eating."

【答案】
(a) 两种理解：① 这只（做好的）鸡已经可以吃了（鸡是被吃的对象）；② 这只（活）鸡准备好去吃东西了（鸡是吃的主体）。
(b) 句法机制：形容词 ready 带不定式 to eat，其隐含逻辑主语 PRO 的控制关系不清——"the chicken" 既可作不定式的**宾语**（被吃，类 tough-movement/提升，PRO 为外部食者），也可作不定式的**主语**（鸡自己去吃），造成歧义。
(c) 消歧改写：① "The chicken is ready to be eaten."（或 "…for us to eat."）；② "The chicken is ready to eat its food."（或 "…to start eating."）。

---

## Q3（汉语语义）

【判断题型】这是一道汉语"差点（没）X"语义歧义分析题；我打算用**中文**思考，便于逐组辨析积极/消极事件。

【思考】
汉语"差点 X / 差点没 X"的核心规律取决于 X 是**说话人不希望发生的事（消极事件）**还是**希望发生的事（积极事件）**：

- 当 X 为**消极事件**（不希望发生）："差点 X"=X 没发生（险些发生但避免了）；"差点没 X" 中"没"看似否定，但在该格式里表示"险些没（避免掉）"，结果仍是 X **没发生**。二者**意思相同**，都表示 X 未发生。
- 当 X 为**积极事件**（希望发生）："差点 X"=X **没发生**（功亏一篑）；"差点没 X"=X **发生了**（惊险达成）。二者**意思相反**。

逐组分析：
(1) 摔倒——消极事件。
- "他差点摔倒"=他没摔倒（险些摔但站住了）。
- "他差点没摔倒"=他没摔倒（同样没摔，强调险些没躲过）。
→ **相同**，都表示"没摔倒"。

(2) 考上大学——积极事件。
- "他差点考上大学"=他没考上（分数不够，差一点）。
- "他差点没考上大学"=他考上了（差一点落榜但最终录取）。
→ **不同**。

(3) 死——消极事件。
- "他差点儿死了"=他没死。
- "他差点儿没死"=他没死（同样保住命）。
→ **相同**，都表示"没死"。

(4) 球进——以说话人希望进为前提（进攻方视角，进是积极事件）。
- "球差点进了"=球没进（打在门框/被扑出）。
- "球差点没进"=球进了（险些不进但最终进了）。
→ **不同**（若说话人是守门方、希望不进，则反过来；通常按进攻方理解）。

【答案】
(1) **相同**：两句都表示"他没摔倒"。
(2) **不同**："差点考上"=没考上；"差点没考上"=考上了。
(3) **相同**：两句都表示"他没死"。
(4) **不同**："差点进了"=没进；"差点没进"=进了（以说话人希望进为前提）。

**语法规律**：X 为消极事件时，"差点 X"与"差点没 X"都表示 X 未发生，二者同义；X 为积极事件时，"差点 X"表 X 未发生、"差点没 X"表 X 发生，二者义反。关键在说话人对 X 的期待（好/坏）决定"没"字是否被抵消。

---

## Q10（英文语境计算）

【判断题型】这是一道英文食谱单位换算计算题（cup / tablespoon）；我打算用**英文**思考，因为涉及英文计量单位与分数运算。

【思考】
Given: a recipe needs 3/4 cup of flour. We are making 2.5× the amount.
Total flour needed = (3/4) cup × 2.5 = (3/4) × (5/2) = 15/8 = 1.875 cups.

We only have:
- a 1/4-cup scoop, and
- a 1-tablespoon (tbsp) scoop,
with 1 cup = 16 tbsp.

Convert everything to tablespoons for exact counting:
1 cup = 16 tbsp → 1.875 cups = 1.875 × 16 = 30 tbsp total needed.
A 1/4-cup scoop = (1/4) × 16 = 4 tbsp.

Use the 1/4-cup scoop as many full times as possible:
30 ÷ 4 = 7 remainder 2.
7 scoops × 4 tbsp = 28 tbsp (= 7/4 = 1.75 cups).
Remaining = 30 − 28 = 2 tbsp → use the tablespoon scoop 2 times.

Check: 7 × (1/4 cup) = 7/4 = 1.75 cups; 2 tbsp = 2/16 = 1/8 = 0.125 cups; total = 1.875 cups ✓.

【答案】
需要面粉总量：3/4 × 2.5 = 15/8 = **1.875 杯**。换算成汤匙：1.875 × 16 = **30 汤匙**；1/4 杯量勺 = 4 汤匙。
因此：**用 1/4 杯量勺舀 7 次（共 28 汤匙 = 1.75 杯），再用 1 汤匙量勺舀 2 匙（共 2 汤匙 = 0.125 杯），合计 1.875 杯，正好。**

---

## Q6（英语韵律）

【判断题型】这是一道英语诗歌韵律（抑扬格五音步）分析题；我打算用**英文**思考，因为需做音节划分与重音标注。

【思考】
Line: *"Shall I compare thee to a summer's day?"*

**Count syllables:**
Shall(1) I(2) com(3) pare(4) thee(5) to(6) a(7) sum(8) mer's(9) day(10) → **10 syllables**.

**Iambic pentameter** = five iambs, each iamb = unstressed–stressed (x /). Divide into 5 feet and mark stress:

Foot 1: Shall **I**        (x /)
Foot 2: com **PARE**       (x /)
Foot 3: thee **TO**        (x /)
Foot 4: a **SUM**          (x /)
Foot 5: mer's **DAY**      (x /)

("summer's" = sum-mers, two syllables; the stress falls on "SUM", and "mer's" begins the final foot with "DAY" stressed.)

All five feet are regular iambs (x /), total 10 syllables, 5 feet.

【答案】
该诗句**是**抑扬格五音步（iambic pentameter）。
- 音节数：10 个（Shall I com·pare thee to a sum·mer's day）。
- 音步划分与重音：Shall **I** | com **PARE** | thee **TO** | a **SUM** | mer's **DAY**（每脚均为"轻–重"x /）。
- 结论：共 5 个标准抑扬格音步，符合 iambic pentameter。

---

## Q8（代码）

【判断题型】这是一道 Python 编程题（回文判断，需处理大小写、标点与中文 Unicode）；我打算用**中文**思考说明思路，代码本身用英文书写。

【思考】
需求：判断字符串 s 是否为回文；忽略大小写、忽略空格与标点；正确处理含中文的字符串（如"上海自来水来自海上"）。

**处理思路**：
1. **筛选字符**：只保留"字母/数字"，丢弃空格与标点。关键点在于中文——在 Python 中，汉字属于字母类，`str.isalnum()` 对汉字、英文字母、数字都返回 `True`，而对空格、逗号、句号等标点返回 `False`。因此用 `ch.isalnum()` 过滤即可同时"忽略空格和标点"并"保留中文"，无需单独写中文正则。
2. **大小写**：用 `str.casefold()`（比 `lower()` 更彻底，对部分 Unicode 大小写更稳妥）统一为小写，中文无大小写，调用无害。
3. **回文判断**：把筛选+归一后的字符序列反转，与原序列比较；相等即为回文。

**代码**：

```python
def is_palindrome(s: str) -> bool:
    # 只保留字母、数字（含汉字），忽略空格和所有标点
    cleaned = [ch.casefold() for ch in s if ch.isalnum()]
    # 比较正序与逆序
    return cleaned == cleaned[::-1]
```

**Unicode 说明**：`isalnum()` 基于 Unicode 属性，能把中文、日文等表意文字判为字母而保留，把 `，` `。` `！` 及西文标点判为非字母而丢弃，因此天然支持多语言与 Unicode 标点；`casefold()` 统一大小写（中文不受影响）。测试用例 `is_palindrome("上海自来水来自海上")` → `True`；`is_palindrome("A man, a plan, a canal: Panama")` → `True`。

【答案】
Python 代码如下（说明见上）：

```python
def is_palindrome(s: str) -> bool:
    # 只保留字母、数字（含汉字），忽略空格和所有标点
    cleaned = [ch.casefold() for ch in s if ch.isalnum()]
    # 比较正序与逆序
    return cleaned == cleaned[::-1]
```

要点：用 `ch.isalnum()` 按 Unicode 属性筛选，自动保留中文等表意文字、丢弃空格与中西文标点；用 `str.casefold()` 统一大小写（对中文无害，对英文比 `lower()` 更严谨）；最后比较字符序列与其反转是否相等。例如 `is_palindrome("上海自来水来自海上")` 返回 `True`。

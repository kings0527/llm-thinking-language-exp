# 高难度测试卷作答（H1–H6）

## H1

【判断题型】本题属于古汉语训诂／词义辨析题，考查"他"在先秦汉语中的本义及其与现代汉语第三人称代词的历时差异。我打算用**中文**思考，因为涉及《孟子》原文与训诂术语，中文更便于援引与辨析。

【思考】
1. 先定位语境。"王顾左右而言他"出自《孟子·梁惠王下》。上下文是孟子用层层递进的设问逼迫齐宣王，最后问"四境之内不治，则如之何？"齐宣王被问住、无法应对，于是"顾左右而言他"。
2. (a) "他"的意思。在先秦汉语中，"他"并不表示第三人称代词，而是表示"别的、其他的（事物）"，即"别的事、别的话题"。"顾左右而言他"整体意为：王环顾身边的侍从（左右），说起了别的事情（即岔开话题、避而不答）。
3. (b) 为什么不能理解为现代汉语的第三人称代词"他"。理由有两点：
   - 一是词义的历时演变。"他"作为第三人称代词是后起的用法，大约到魏晋南北朝以后才逐渐出现，至唐宋才普遍；先秦汉语里"他"的常见义是"别的、其他的"，如"他日"（改日、别的日子）、"无他"（没有别的／没有别的原因）、"它山之石"之"它"同源。因此用后世的代词义去套先秦文本，是时代错置。
   - 二是句法语义不通。"言他"若解为"说他（某个男子）"，则整句变成"王环顾左右而说他"，凭空引入一个上下文里并不存在的男性第三者；而"言+他事"才是先秦自然的动宾结构（"言"带事类宾语）。
4. (c) 若按"第三人称代词"理解，会产生什么具体偏差。
   - 第一，凭空制造了一个原文没有的所指对象（一个男性"他"），而《孟子》原文中并无此人。
   - 第二，完全丢失了"王故意岔开话题、避重就轻"这一核心语义与修辞效果——"顾左右而言他"正是后世"转移话题、答非所问"这一典故的出处。
   - 第三，与上下文脱节：原文是王被问住后主动换话题，而不是在谈论某个人。
   - 因此这种理解是误读，根子在把后起的代词义强加于先秦词形之上。

【答案】
(a) "他"在句中意为"别的、其他的（事情／话题）"，整句是说齐宣王环顾左右侍从而说起别的事，即岔开话题、避而不答。
(b) 不能理解为现代汉语第三人称代词，原因有二：一是词义历时演变——"他"作第三人称代词是魏晋以后才出现、唐宋才普遍的用法，先秦汉语中"他"表示"别的、其他的"（如"他日""无他"）；二是句法语义不通——"言他"若解为"说他（某男子）"，会凭空引入上下文中不存在的男性第三者，而"言他事"才是自然搭配。
(c) 若按第三人称代词理解，具体偏差为：①凭空制造原文没有的男性所指对象；②完全丧失"王故意转移话题、避而不答"的核心语义与典故含义；③与《孟子》上下文脱节（原文是王被问住后换话题，并非谈论某人）。这是把后起代词义强加于先秦词形导致的时代错置式误读。

## H2

【判断题型】本题属于组合计数／整除判别题，要求统计由1–7各用一次组成的七位数中能被11整除的个数。我打算用**中文**思考，便于列算式、做组合枚举与模运算推导。

【思考】
1. 设七位数从左到右各位为 d1 d2 d3 d4 d5 d6 d7（d1为最高位）。被11整除的判别法：奇数位数字和与偶数位数字和之差是11的倍数。这里奇数位=第1、3、5、7位（共4个数字），偶数位=第2、4、6位（共3个数字）。
2. 令 S奇 = d1+d3+d5+d7，S偶 = d2+d4+d6。需满足 S奇 − S偶 ≡ 0 (mod 11)。
3. 数字总和：1+2+3+4+5+6+7 = 28，故 S奇 + S偶 = 28。
4. 联立：S奇 − S偶 = 11k，S奇 + S偶 = 28。两式相加得 2·S奇 = 28 + 11k，即 S奇 = (28+11k)/2。S奇 必须为整数，故 28+11k 为偶数 → 11k 为偶数 → k 为偶数。
5. 确定 S奇 的取值范围：最小取 1+2+3+4 = 10，最大取 4+5+6+7 = 22，故 S奇 ∈ [10, 22]。
6. 枚举偶数 k：
   - k = 0 → S奇 = 14，可行。
   - k = 2 → S奇 = (28+22)/2 = 25 > 22，超出范围。
   - k = −2 → S奇 = (28−22)/2 = 3 < 10，超出范围。
   - |k| 更大的偶数只会更超出范围。
   因此唯一可能：S奇 = S偶 = 14。
7. 问题转化为：从 {1,2,3,4,5,6,7} 中选出4个数字使其和为14（这4个放奇数位），其余3个自动和为14（放偶数位）。
8. 枚举所有和为14的4元子集：
   - 含1：1+2+4+7=14 → {1,2,4,7}；1+2+5+6=14 → {1,2,5,6}；1+3+4+6=14 → {1,3,4,6}。（1+3+5+5 重复、1+4+5+4 重复，均不行。）共3个。
   - 不含1而含2：2+3+4+5=14 → {2,3,4,5}；其余如 2+4+? 需另两数和=8且大于4，无解。共1个。
   - 不含1、2（最小 3+4+5+6=18>14）不可能。
   合计4个4元子集：{1,2,4,7}、{1,2,5,6}、{1,3,4,6}、{2,3,4,5}。
9. 对每个划分：4个奇数位数字可任意排列，有 4! = 24 种；3个偶数位数字可任意排列，有 3! = 6 种。共计 24×6 = 144 种。
10. 注意首位 d1 属于奇数位集合，且数字中无0，因此所有排列均为合法七位数（不存在前导0问题）。
11. 总数 = 4（种划分）× 144 = 576。

【答案】
由1–7各用一次组成的七位数中，能被11整除的共有 **576** 个。

## H3

【判断题型】This is an English pragmatics question about presupposition and implicature, comparing two sentences that differ only by the phrase "bother to". I will think in **English** because the object of analysis is English sentence meaning, speaker stance, presupposition and implicature.

【思考】
(a) Literal propositional content vs. speaker stance.
- Both (A) "He didn't reply." and (B) "He didn't bother to reply." assert the SAME truth-conditional proposition: that he did not produce a reply. There is no difference in what is literally claimed to be true.
- The difference lies entirely in speaker stance/attitude. (A) is neutral and merely reports the absence of a reply. (B) is evaluative: it conveys that the speaker regards replying as something easy, minimal, expected, or normatively owed, and that his failure to reply reflects negatively on him (laziness, dismissiveness, lack of consideration). So (A) describes a fact; (B) judges the subject.

(b) Presupposition and implicature of "bother to".
- "bother to" PRESUPPOSES that the action (replying) was one that would have required only minimal effort and/or was the expected, courteous, or owed thing to do; it presupposes the action was easily within the subject's reach. This is a pragmatic presupposition built into the verb "bother".
- "bother to" IMPLICATES (via conversational implicature) that the subject was lazy, inconsiderate, or deliberately dismissive — that the non-reply is a character flaw or a slight, rather than a neutral, inconsequential fact.

(c) Why it cannot describe something the speaker thinks was not to be expected.
- "He didn't bother to reply" cannot be used for an event the speaker believes was NOT to be expected, because "bother to" carries the presupposition that the action was a minimal, expected, or owed behavior. If the speaker thinks no reply should have been expected at all, then saying "didn't bother" falsely presupposes that he should have replied / it was easy and he chose not to.
- Example 1: "My late grandfather didn't bother to reply to my email." This is infelicitous, because we do not expect a dead person to reply. The correct neutral report is "My grandfather didn't reply."
- Example 2: Writing to a foreign head of state or a total stranger who owes you nothing — "The president didn't bother to reply to my letter" is odd if you never expected a reply in the first place; "He didn't reply" is the appropriate form. Using "bother" wrongly imports an obligation or ease that does not exist.

【答案】
(a) 两句在字面命题内容上**没有差别**，都断言"他没有回复"这一事实；差别在说话人立场：(A) 是中性陈述，(B) 带有评价色彩，暗示说话人认为"回复"是容易、应做或理应做到的，未回复反映出此人的懒惰、轻慢或不在意。
(b) 加上 "bother to" 后，**预设（presuppose）**了"回复"是只需极小努力、且是理所应当/应尽的举动；**隐含（implicate）**了此人懒惰、怠慢或故意漠视，即未回复是其品格上的瑕疵而非中性事实。
(c) "He didn't bother to reply" 不能用来描述说话人认为"本就不该期待发生"的事，因为 "bother to" 预设了该举动是微小且理应做的；若说话人根本不期待回复，用此句会错误地强加一种"他本该回、且轻而易举却偏不回"的义务感。例如对死者说 "My late grandfather didn't bother to reply" 就不自然，应说 "He didn't reply"；又如给毫不相干的外国元首写信后说 "The president didn't bother to reply"，若你本就没期待回复，便属误用。

## H4

【判断题型】本题属于逻辑谜题（骑士永远说真话／无赖永远说假话），要求确定三人身份并排除其他可能。我打算用**中文**思考，便于逐步假设与排除。

【思考】
1. 记骑士为 T（永真），无赖为 K（永假）。三人陈述：
   - A："B 是无赖。"
   - B："A 和 C 是同一类人。"
   - C："A 是骑士。"
2. 先假设 A 是骑士（T）。则 A 的话为真 → B 是无赖（K）。B 是无赖，其话必假 → "A 和 C 同类"为假 → A 与 C 不同类。已知 A=T，故 C=K。但 C 是无赖，其话"C 说 A 是骑士"必须为假；而 A 实际是骑士，故该话竟为真，矛盾（无赖不能说真话）。所以 A 不可能是骑士。
3. 因此 A 必为无赖（K）。A 是无赖，其话为假 → "B 是无赖"为假 → B 不是无赖 → B 是骑士（T）。
4. B 是骑士，其话为真 → "A 和 C 同类"为真 → A 与 C 同类。A=K，故 C=K（无赖）。
5. 验证 C：C 是无赖，其话"C 说 A 是骑士"应为假；A 实际是无赖，故该话确为假，符合。
6. 排除其余可能以确认唯一：第一步已证 A 不能为 T，故 A=K 唯一；由 A 假话"B 是 K"推得 B=T 唯一；再由 B 真得 C 与 A 同类，故 C=K 唯一。八种分配中仅此一种自洽。

【答案】
A 是无赖，B 是骑士，C 是无赖。

## H5

【判断题型】本题属于汉语歧义分析题，考查"他谁都不认识"的句法／语义歧义及相关用法辨析。我打算用**中文**思考，便于使用汉语语法术语（任指、话题、论元结构等）进行描述。

【思考】
(a) "他谁都不认识"的两种理解及"谁"的用法：
- 理解1（他作施事／主语，谁作受事／宾语）：结构为"他[谁[都不[认识]]]"，意为"他对谁都不认识 → 他不认识任何人"。"谁"在这里是**任指**用法，相当于"任何人"，位于宾语位置，受"都…不"约束，表全称否定。
- 理解2（他作受事／宾语，经话题化前置；谁作主语）："他"是话题，"谁都不认识(他)"作述题，意为"谁都不认识他 → 没有人认识他"。"谁"仍是**任指**用法（"任何人"），位于主语句法位置，"谁都+不"整体表示"没有人"。
- 两种理解中"谁"都是任指，既不是疑问用法，也不是虚指用法。

(b) 歧义产生的句法／形态根源：
- 歧义源于**句法论元结构的不确定性**。汉语缺乏显性的格标记和主宾语形态，动词"认识"带两个论元（施事、受事），而"他"与"谁"都可充任主语或宾语；"都…不"的量化结构并不强制标明哪个名词短语是主语、哪个是宾语。"他"既可作主语（施事，理解1），也可经话题化前置作宾语／受事（理解2）。因此这是语法关系（主宾语位）的歧义，而非词汇多义。

(c) 与"他谁都认识"相比，歧义程度是否相同：
- 结构上二者**基本相同**，都是两读："他谁都认识"既可解"他认识所有人"（他施事），也可解"所有人都认识他"（他受事／话题）。所以可读出的结构数量相同，歧义根源也相同。
- 差别主要在于**语用显著度**：肯定式"他谁都认识"中"他作施事（他认识所有人）"这一读通常更自然、更默认；而否定式"他谁都不认识"里，由于"谁都不X"本身就可以表示"没人X"，"没有人认识他"这一读同样容易被激活，两读都常见。换言之，二者歧义的结构数量相同，只是各读的语用优先度略有差异。

【答案】
(a) 两种理解：①"他（主语）不认识任何人"——"谁"作宾语，为**任指**（任何人）；②"没有人认识他"——"他"作宾语经话题前置、"谁"作主语，为**任指**（任何人），"谁都+不"表"没有人"。两句中的"谁"都是任指，非疑问、非虚指。
(b) 歧义根源是句法论元结构的不确定性：汉语无显性格标记，"认识"的两个论元"他""谁"都可作主、宾语，"都…不"结构不强制标明主宾语位，"他"既可作施事主语也可话题化为受事宾语，故产生主宾关系歧义。
(c) 与"他谁都认识"相比，歧义程度**基本相同**（都是两读，结构根源相同）；细微差别在语用显著度：肯定式"他谁都认识"更默认读作"他认识所有人"，而否定式因"谁都不X"本就可表"没人X"，"没人认识他"这一读同样易激活。二者可读出的结构数量一致，仅各读优先度略有差异。

## H6

【判断题型】This is an English collocation / grammar error-correction task with six learner sentences. I will think in **English** to analyze each error type and produce the correct form.

【思考】
(1) "I'm looking forward to meet you."
- Error: After the phrase "look forward to", the word "to" is a PREPOSITION, not part of an infinitive marker. A preposition must be followed by a gerund (or noun), not a bare infinitive.
- Correct: "I'm looking forward to meeting you."

(2) "She suggested me to take the train."
- Error: "suggest" does NOT take the pattern "suggest + indirect object + to-infinitive". The accepted patterns are "suggest doing something" or "suggest (that) someone (should) do something". Also, the indirect object "me" would become the subject "I" inside a that-clause.
- Correct: "She suggested (that) I take the train." or "She suggested taking the train." (One may also say "She suggested the train to me.")

(3) "Despite of the rain, we went out."
- Error: "despite" is itself a preposition and is NEVER followed by "of". The "of" belongs to the alternative phrase "in spite of".
- Correct: "Despite the rain, we went out." (or "In spite of the rain, we went out.")

(4) "He's capable to do it."
- Error: "capable" is followed by the preposition "of" + gerund, not by an infinitive.
- Correct: "He's capable of doing it."

(5) "I would rather stay than to go."
- Error: The correlative "would rather … than …" requires PARALLEL BARE INFINITIVES on both sides. "than" should be followed by the bare infinitive "go", not "to go".
- Correct: "I would rather stay than go."

(6) "It's worth to try."
- Error: "worth" is followed by a gerund (or a noun), not an infinitive.
- Correct: "It's worth trying." (or "It's worth a try.")

【答案】
(1) 错误：介词误用（"to"是介词，后应接动名词）。正确：**I'm looking forward to meeting you.**
(2) 错误：动词搭配错误（suggest 不能接"间接宾语 + to do"）。正确：**She suggested (that) I take the train.** 或 **She suggested taking the train.**
(3) 错误：冗余介词（despite 本身即是介词，不接 of）。正确：**Despite the rain, we went out.**（或 In spite of the rain）
(4) 错误：形容词搭配错误（capable 后接 of + 动名词，不接不定式）。正确：**He's capable of doing it.**
(5) 错误：平行结构错误（would rather … than … 两边均用动词原形）。正确：**I would rather stay than go.**
(6) 错误：形容词搭配错误（worth 后接动名词或名词，不接不定式）。正确：**It's worth trying.**（或 It's worth a try.）

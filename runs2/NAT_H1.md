# 高难度测试卷答案（NAT_H1）

## H1

【思考】
原文是《孟子·梁惠王下》里的名句："王顾左右而言他。"先拆字看"他"。在先秦汉语里，"他"（本字常写作"它""佗"）的核心义是"别的、其他的"，并不是指人的第三人称代词。这个第三人称的用法是很晚才发展起来的——一般要到中古（唐以后）才普遍用作"别的某人/他"。所以这里要回到孟子时代的用法来读。

整句情境：孟子用层层逼问的方式，让齐宣王承认自己没尽到责任；最后齐宣王被问到关键点，不好意思回答，就"顾左右而言他"——转头看旁边的人，说些别的事、把话题岔开。所以"言他"="说别的事/谈别的话题"，是"顾左右"这个逃避动作的结果：看左右、然后讲别的东西（岔开）。

(b) 为什么不能当现代汉语第三人称"他"？因为时代错位。孟子时"他"没有"第三人称代词"这个义项；把"他"读成"他（那个男的）"，等于把一个后起的代词用法硬塞进先秦文本，属于以今律古。

(c) 偏差具体在哪？如果按"第三人称代词"理解，"言他"就成了"对他说/说他（某个人）"，整句变成"王顾左右而对他（某个人）说话"或"王顾左右而说到他"。这就：
1. 凭空造出一个具体指称对象（某个特定的"他"），但原文根本没有这个所指；
2. 丢掉了"岔开话题、回避、谈别的事"这个最关键的语义——也就是"顾左右"和"言他"共同构成的"回避"语用义；
3. 把"逃避回答"误读成"转向另一个人说话"，句子功能完全变了。
结合先秦"他=别的/其他的"用法，正确的理解应是"王环顾左右，说起了别的事（把话题岔开）"。

【答案】
(a) "他"在此处的意思是"别的、其他的（事/话）"。"王顾左右而言他"意为：大王环顾左右随从，说起了别的事情（把话题岔开、回避问题）。
(b) 不能理解为现代汉语第三人称代词"他"，是因为在先秦汉语中"他"（本字多作"它""佗"）的常用义是"别的、其他的"，第三人称代词的用法是中古以后才逐渐产生的；把后起义强加于《孟子》时代，属于"以今律古"的时代错位。
(c) 若按"第三人称代词"理解，"言他"会被误读为"对他（某特定男子）说/说到他"，整句变成"王顾左右而对他说起（某个人）"。这样产生的具体偏差是：①凭空制造出一个原文并不存在的特定指称对象；②丢失了"岔开话题、回避问题"这一核心语用义；③把"逃避回答"误解为"转向另一个人说话"，句子功能被彻底扭曲。结合先秦"他=别的/其他的"的用法，原句应理解为"王看着左右，谈起了别的事（回避了原问题）"。

## H2

【思考】
要用 1,2,3,4,5,6,7 各一次组成七位数，问能被 11 整除的有多少个。

先回忆被 11 整除的判别法：一个整数，其奇数位数字之和 与 偶数位数字之和 的差，能被 11 整除（包括差为 0），则该数能被 11 整除。

七位数有 7 个位置。位置从第 1 位（最高位）到第 7 位。奇数位 = 第 1,3,5,7 位，共 4 个位置；偶数位 = 第 2,4,6 位，共 3 个位置。

设 S_odd = 奇数位上 4 个数字之和，S_even = 偶数位上 3 个数字之和。
全部数字和：1+2+3+4+5+6+7 = 28。所以：
S_odd + S_even = 28。
被 11 整除要求 S_odd − S_even ≡ 0 (mod 11)，即 S_odd − S_even = 11k（k 为整数）。

两式相加：2·S_odd = 28 + 11k，故 S_odd = 14 + 11k/2。
要使 S_odd 为整数，11k 必须为偶数，所以 k 必须为偶数。

估计 S_odd 范围：4 个最小数字 1+2+3+4=10，4 个最大数字 4+5+6+7=22，故 10 ≤ S_odd ≤ 22。
- k = 0：S_odd = 14，S_even = 14（可行）。
- k = 2：S_odd = 25 > 22，不可行。
- k = −2：S_odd = 3 < 10，不可行。
更大的 |k| 更不可能。因此唯一可能是 S_odd = S_even = 14。

于是问题化为：从 {1,2,3,4,5,6,7} 中选出 4 个数字使其和为 14（放到奇数位），剩下 3 个数字自然和为 14（放到偶数位）。求这样的 4 元子集个数。

枚举所有 4 元子集并求和，和为 14 的有：
- {1,2,4,7} = 14（余 {3,5,6}=14）
- {1,2,5,6} = 14（余 {3,4,7}=14）
- {1,3,4,6} = 14（余 {2,5,7}=14）
- {2,3,4,5} = 14（余 {1,6,7}=14）

共 4 种选法。

对每一种：奇数位的 4 个数字可任意排列到 4 个奇数位（4! 种），偶数位的 3 个数字任意排列到 3 个偶数位（3! 种）。所以每种选法对应 4! × 3! = 24 × 6 = 144 个七位数。

总数 = 4 × 144 = 576。

【答案】
能被 11 整除的七位数共有 **576** 个。

推导：被 11 整除要求奇数位数字和与偶数位数字和之差为 11 的倍数。设奇数位（4 个位置）数字和为 S_odd，偶数位（3 个位置）和为 S_even，则 S_odd + S_even = 28，S_odd − S_even = 11k。解得唯一可行解 S_odd = S_even = 14。从 {1,2,3,4,5,6,7} 选 4 个数和为 14 的子集共 4 个：{1,2,4,7}、{1,2,5,6}、{1,3,4,6}、{2,3,4,5}。每种选法中奇数位 4! 排列、偶数位 3! 排列，共 4 × 4! × 3! = 576 个。

## H3

【思考】
Compare (A) He didn't reply. and (B) He didn't bother to reply.

(a) First, the literal/propositional content. Both (A) and (B) assert the same truth-conditional proposition: he did not produce a reply. So at the level of what is said (the actual event), the propositional content is identical — in both, no reply occurred. The difference is wholly in speaker stance/attitude. (A) is neutral: it just reports the fact. (B) is evaluative: by adding "bother to", the speaker frames the non-reply as something noteworthy, implying that replying would have been a trivial, low-cost action that was nevertheless not performed — so the speaker expresses a negative evaluation (the person was inconsiderate, careless, or that the omission is remarkable).

(b) Presupposition vs implicature of "didn't bother to reply". 
Presupposition (what must already hold for the sentence to be felicitous): that replying was a possible, low-effort action within his capacity, and — crucially — that there was some ground or expectation for him to reply (a normal reason, mild obligation, or at least a reasonable basis to expect it). "Bother" means "take the trouble"; so the construction presupposes the action was a small trouble that was warranted.
Implicature (what is conveyed beyond the proposition): the speaker conveys that he didn't care enough to expend even that minimal effort; the speaker disapproves or finds the omission worth commenting on; there is a conventional attitudinal coloring of trivialized effort + negative judgment. This is partly a conventional implicature (the "it was only a small thing" flavor) plus a Gricean implicature of negative stance.

(c) Why can't "He didn't bother to reply" describe something the speaker thinks "shouldn't have been expected to happen"? Because the construction presupposes that the action was a low-cost, expected (or at least reasonable-to-expect) deed. If the speaker believes the reply was NOT at all expected — e.g., the subject had no reason, obligation, or even capacity to reply — then "didn't bother to" is infelicitous: it falsely presupposes an expectation/obligation that doesn't exist. Example: "My cat didn't bother to reply to my question." — infelicitous, because a cat was never expected to reply. Or "A rock didn't bother to answer the email." — equally odd. The presupposition of an expectation is violated, so the sentence misfires. By contrast "He didn't reply" works fine for any case, expected or not.

【答案】
(a) 两句话的**字面命题内容相同**：都断言"他没有回复"（truth-conditionally 等价）。差别在**说话人立场**：(A) 是中性陈述，只报告事实；(B) 带有评价色彩，把"未回复"框定为一件值得注意的事，暗示回复本是一件轻而易举、却仍未被做的事，表达说话人的负面态度（认为对方不在意/敷衍）。
(b) 加上 "bother to" 后：
- **预设（presuppose）**：回复是一件可行的、低成本的、且本有理由/期待去做的动作（"bother"= 费心去做，预设此事是微小麻烦且理应发生）。
- **隐含（implicate）**：说话人隐含对方连这点微小 effort 都不肯花，带着不以为然/批评的态度，认为"不回复"这件事值得特意点出。
(c) "didn't bother to reply" **不能**用来描述说话人认为"本就不该期待发生"的事，因为该句式**预设了**回复是一件低成本、有理由被期待的动作。若说话人认为根本不该期待对方回复，这个预设就被破坏了，句子不成立。例："My cat didn't bother to reply to my question." 不自然——猫本来就不该被期待会回复；"A stone didn't bother to answer." 同理。而 "He didn't reply" 对任何情况都适用。

## H4

【思考】
三人 A、B、C，每人是骑士（永真）或无赖（永假）。
- A 说："B 是无赖。"
- B 说："A 和 C 是同一类人。"
- C 说："A 是骑士。"

用分情况法，从 A 的身份入手。

情况 1：A 是骑士（说真话）。
则 A 的话为真 → B 是无赖。
B 是无赖 → B 的话为假。B 说"A 和 C 是同一类人"，既为假，则 A 与 C **不是**同一类。A 是骑士，故 C 是无赖。
C 是无赖 → C 的话为假。C 说"A 是骑士"，若 C 永假，此句应为假 → A **不是**骑士 → A 是无赖。但这与"情况 1 假设 A 是骑士"矛盾。
所以情况 1 不可能。

情况 2：A 是无赖（说假话）。
则 A 的话"B 是无赖"为假 → B **不是**无赖 → B 是骑士。
B 是骑士 → B 的话为真。"A 和 C 是同一类人"为真 → 因 A 是无赖，故 C 也必须是无赖（同类）。
C 是无赖 → C 的话为假。C 说"A 是骑士"，为假即 A 不是骑士 → A 是无赖，与假设一致 ✓。
整套自洽，无矛盾。

逐一验证：
- A（无赖）说"B 是无赖"——假，因为 B 实为骑士 ✓；
- B（骑士）说"A 和 C 同类"——A、C 皆无赖，同类，真 ✓；
- C（无赖）说"A 是骑士"——假，A 实无赖 ✓。

再确认其他分配都不成立：上面已用穷尽二分证明 A 必为无赖（A 为骑士会导致矛盾），从而唯一确定 A=无赖、B=骑士、C=无赖。无需再列其余组合，因为 A 的两种可能已穷尽，骑士情形被排除，只剩这一种。

【答案】
A 是**无赖**，B 是**骑士**，C 是**无赖**。

推理：假设 A 是骑士，则 A 的话为真 → B 是无赖；B 的话为假 → A 与 C 不同类 → C 是无赖；C 的话为假 → "A 是骑士"为假 → A 是无赖，与假设矛盾，故 A 不可能是骑士。因此 A 必为无赖。A 是无赖 → A 的话为假 → B 是骑士。B 是骑士 → 其话为真 → A 与 C 同类 → C 也是无赖。验证 C（无赖）说"A 是骑士"为假，一致。故唯一解：A 无赖、B 骑士、C 无赖。

## H5

【思考】
句子："他谁都不认识。"

(a) 两种理解：
理解一（他为主语，谁为宾语）："他[对]谁都不认识" = 他谁也不认识 / 他不认识任何人。此时"他"是"认识"的施事主语，"谁"是受事宾语，表示"任何人"（在否定句中表全指）。
理解二（谁为主语，他为宾语）："谁都不认识他" = 谁也不认识他 / 没有任何人认识他。此时"谁"是"认识"的施事主语（周遍性主语），"他"是受事宾语。

"谁"在两种理解里都是**任指（周遍性）用法**：在"不……都……"的句式里，"谁"表示"任何人/每一个人"，不指向某个具体疑问对象，也不是虚指。区别在于它的句法角色（主语还是宾语）不同。

(b) 歧义的根源性：汉语缺少形态的格标记（主宾语无词形变化），且"谁"这类周遍性词语可以占据句首主语位置，也可以作宾语；而"他"既可以作主语也可以作宾语。于是"他谁都不认识"这一线性序列中，两个名词性成分的论元角色（施事/受事）无法由形态或语序唯一确定——"他"是施事还是受事、"谁"是施事还是受事存在两种指派方式，造成"施受同辞"型的论元角色/辖域歧义。

(c) 与"他谁都认识"相比：后者同样有两读——"他认识所有人"和"所有人都认识他"，结构上完全对称，歧义程度**相同**（都是两可歧义）。差别只在于极性（否定/肯定）带来的真值条件不同，并不改变歧义的结构与数量。之所以有人觉得有差别，是因为否定句"他谁都不认识"的"他为主语"读（他不认识任何人）最为自然、最常用，而"谁为主语"读（没人认识他）相对次要；肯定句"他谁都认识"的"他为主语"读（他认识所有人）同样最自然。但就"是否有两种理解"而言，两者歧义程度相同——都由"谁"的周遍主语/宾语两可造成。

【答案】
(a) 两种理解：
1. "他（主语）不认识谁（任指宾语）" = 他谁也不认识 / 他不认识任何人；
2. "谁（任指主语）都不认识他（宾语）" = 谁也不认识他 / 没有人认识他。
两种理解中"谁"都是**任指（周遍性）用法**（在"不……都……"中表"任何人"），并非疑问也非虚指；歧义仅在于"谁"的句法角色不同。
(b) 歧义的句法/形态根源：汉语无主宾语的形态格标记，且周遍词"谁"既可作句首主语也可作宾语，"他"同样可主可宾；因此"他谁都不认识"的线性序列无法唯一确定施事/受事角色，属于"施受同辞"型的论元角色与辖域歧义。
(c) 与"他谁都认识"相比，歧义程度**相同**——后者也有两读（"他认识所有人"与"所有人都认识他"），由同样的"谁"周遍主语/宾语两可造成，只是极性（否定/肯定）不同，不改变歧义的数量与结构。所谓"差别"只是语用偏好（"他为主语"的读法最自然常用），但两句话都同样是两可歧义。

## H6

【思考】
Go through each learner error.

(1) I'm looking forward to meet you.
"look forward to" — here "to" is a preposition, not the infinitive marker. Prepositions take a gerund (V-ing). So "to meet" is wrong.
Correct: I'm looking forward to meeting you.

(2) She suggested me to take the train.
"suggest" does NOT take the pattern "suggest + object + to-infinitive". The verb suggest is followed by a that-clause (subjunctive/should) or by a gerund, not by an object + infinitive. So "suggested me to take" is ungrammatical.
Correct options: She suggested (that) I take the train. / She suggested my taking the train. / She suggested taking the train.

(3) Despite of the rain, we went out.
"despite" is already a preposition; it is NOT followed by "of". The "of" belongs to the phrase "in spite of", not "despite".
Correct: Despite the rain, we went out. (or: In spite of the rain, we went out.)

(4) He's capable to do it.
"capable" is followed by "of" + gerund, not by an infinitive.
Correct: He's capable of doing it.

(5) I would rather stay than to go.
After "would rather ... than ...", both verbs are bare infinitives — no "to" on either side.
Correct: I would rather stay than go.

(6) It's worth to try.
"worth" is followed by a noun or a gerund, not by an infinitive.
Correct: It's worth trying. (or: It's worth a try.)

【答案】
(1) **错误**：搭配错误。"look forward to" 中 to 是介词，须接动名词。
正确：**I'm looking forward to meeting you.**

(2) **错误**：动词句型错误。"suggest" 不能接 "宾语 + to do" 结构，只能接 that 从句或动名词。
正确：**She suggested (that) I take the train.**（或 She suggested taking the train. / She suggested my taking the train.）

(3) **错误**：多余介词。"despite" 本身已是介词，后面不接 of（of 属于 in spite of）。
正确：**Despite the rain, we went out.**（或 In spite of the rain, we went out.）

(4) **错误**：形容词搭配错误。"capable" 后接 of + 动名词，不接不定式。
正确：**He's capable of doing it.**

(5) **错误**：句型错误。"would rather ... than ..." 两端都用动词原形，不加 to。
正确：**I would rather stay than go.**

(6) **错误**：形容词搭配错误。"worth" 后接名词或动名词，不接不定式。
正确：**It's worth trying.**（或 It's worth a try.）

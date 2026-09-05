# 解题记录（顺序：H6, H5, H4, H3, H2, H1）

## H6

【思考】
I will examine each sentence one by one, checking the required complement pattern (verb/ adjective/adposition + complement type) against standard English grammar.

(1) "I'm looking forward to meet you." The phrase "look forward to" uses "to" as a preposition, not an infinitive marker. A preposition must be followed by a gerund (verb-ing) or a noun phrase. "meet" is a bare infinitive, which is wrong. Correction: "I'm looking forward to meeting you."

(2) "She suggested me to take the train." The verb "suggest" does not take the pattern "suggest + object + to-infinitive". The standard patterns are "suggest (that) + clause" (with subjunctive "take") or "suggest + gerund". So "suggested me to take" is ungrammatical. Correction: "She suggested (that) I take the train" or "She suggested my taking the train."

(3) "Despite of the rain, we went out." "Despite" is a preposition and is never followed by "of". The phrase "in spite of" takes "of", but "despite" does not. Correction: "Despite the rain, we went out" or "In spite of the rain, we went out."

(4) "He's capable to do it." The adjective "capable" is followed by the preposition "of" + gerund, not by a "to"-infinitive. Correction: "He's capable of doing it."

(5) "I would rather stay than to go." The construction "would rather ... than ..." requires bare infinitives on both sides (no "to"). So "than to go" is wrong. Correction: "I would rather stay than go."

(6) "It's worth to try." The adjective "worth" is followed by a gerund, not a "to"-infinitive. Correction: "It's worth trying."

All six are errors except none of them is correct; each needs the correction stated.

【答案】
(1) 错误，搭配不当。"look forward to" 中的 to 是介词，须接动名词。正确：I'm looking forward to meeting you.
(2) 错误，动词句式误用。"suggest" 不能接 "宾语 + to do"。正确：She suggested (that) I take the train. 或 She suggested my taking the train.
(3) 错误，多用 of。"despite" 是介词，后面不加 of。正确：Despite the rain, we went out. 或 In spite of the rain, we went out.
(4) 错误，形容词介词搭配错。"capable" 后接 of doing。正确：He's capable of doing it.
(5) 错误，多了 to。"would rather ... than ..." 两端都用动词原形。正确：I would rather stay than go.
(6) 错误，worth 后接动名词。正确：It's worth trying.

## H5

【思考】
I analyze the sentence "他谁都不认识" for its possible structural parses.

(a) The string can be parsed in two ways. Parse 1: 他 is the subject (agent) of 认识, and 谁都 is an indefinite universal inside the negative scope acting as the object: "他 [谁都不认识]" = He does not know anyone / He knows nobody. Here 谁 is 任指 (free/universal indefinite), meaning "anyone/whoever", and 谁都 under negation means "nobody". Parse 2: 他 is a topicalized object (patient) and 谁都 is the subject: "[他] 谁都不认识" = Nobody knows him. Here 谁 is again 任指 as the subject, meaning "everyone/anyone", and the whole means "as for him, anyone does not know him" = nobody knows him. So the two readings are "He knows nobody" vs. "Nobody knows him."

(b) The root of the ambiguity is syntactic/morphological: Chinese allows an object or patient to be fronted before the subject (topic/object preposing), and there is no case marking to distinguish subject from object. The phrase 谁都 is a floating universal quantifier that can serve as either subject or object. Because 他 can be interpreted as either the agent subject or the preposed patient object, and 谁都 can correspondingly be either the object or the subject, the same linear string yields two distinct grammatical relations and meanings.

(c) Compare with "他谁都认识". It also has two readings: Parse A: 他 subject, 谁都 object → He knows everyone. Parse B: 他 topicalized object, 谁都 subject → Everyone knows him. So structurally the ambiguity is symmetric and the degree of ambiguity is essentially the same: both sentences admit an agent reading and a patient reading due to the same topic-fronting mechanism. The difference is only pragmatic/statistical: for the negative sentence, the "He knows nobody" reading is perhaps more frequent in use, and for the affirmative the "He knows everyone" reading is more frequent, but both readings remain grammatically available in each case. Thus the ambiguity degree is the same; the syntactic source is identical.

【答案】
(a) 两种理解：
- 理解一：他（主语，施事）+ 谁都不认识（宾语），意为"他谁也不认识 / 他什么都不认识"。句中"谁"是任指，在否定辖域内相当于"任何人/没有人"。
- 理解二：他（前置的话题/宾语，受事）+ 谁都（主语）不认识，意为"谁都不认识他 / 没人认识他"。句中"谁"仍是任指，作主语"任何人"。
(b) 句法/形态根源：汉语允许宾语（受事）话题化前置于句首，且无格标记来区分主宾语；"谁都"是浮动全称量化短语，既可作主语也可作宾语。于是"他"既能被分析为施事主语，也能被分析为前置的受事宾语，造成两种语法关系与两种意义。
(c) 与"他谁都认识"相比，歧义程度基本相同：后者也有两种理解（"他认识所有人" / "所有人都认识他"），二者因同样的话题前置机制而对称歧义。差别只在语用频率上（否定句更常取"他谁也不认识"，肯定句更常取"他认识所有人"），但两种理解在两句中都语法合法，故歧义程度相同、句法根源一致。

## H4

【思考】
There are three people A, B, C, each a Knight (always tells truth) or a Knave (always lies). Statements:
- A: "B is a Knave."
- B: "A and C are of the same type."
- C: "A is a Knight."

I will test both possibilities for A and show the other is impossible.

Assume A is a Knight. Then A's statement is true, so B is a Knave. Since B is a Knave, B's statement is false. B said "A and C are of the same type"; its negation means A and C are of different types. A is a Knight, so C must be a Knave. Now C is a Knave, so C's statement "A is a Knight" must be false, which would mean A is a Knave. This contradicts our assumption that A is a Knight. Therefore the assumption "A is a Knight" leads to a contradiction and is impossible.

Therefore A must be a Knave. Then A's statement "B is a Knave" is false, so B is a Knight. Since B is a Knight, B's statement is true: A and C are of the same type. A is a Knave, so C is also a Knave. Check C: C is a Knave, so C's statement "A is a Knight" must be false, which it is (A is a Knave). This is fully consistent.

We have excluded the only alternative (A a Knight), so the unique solution is A = Knave, B = Knight, C = Knave.

【答案】
A 是无赖，B 是骑士，C 是无赖。

推理：先假设 A 是骑士。则 A 说真话 → B 是无赖。B 说假话 → "A 和 C 同一类"为假 → A、C 不同类；A 是骑士故 C 是无赖。C 说假话 → "A 是骑士"为假 → A 是无赖，与假设矛盾。所以 A 不能是高骑士，必为无赖。
A 是无赖 → A 说假话 → "B 是无赖"为假 → B 是骑士。B 说真话 → A、C 同类；A 是无赖故 C 是无赖。C 说假话 → "A 是骑士"为假，成立。
已排除 A 为骑士的唯一其他可能，故唯一解为：A 无赖、B 骑士、C 无赖。

## H3

【思考】
I compare (A) "He didn't reply." and (B) "He didn't bother to reply."

(a) Literal propositional content: Both convey that he did not reply. "didn't bother to reply" presupposes and entails "didn't reply", so the core proposition is the same. The difference is in the speaker's stance: (A) is a neutral report of a fact. (B) expresses an evaluative attitude: it implies that replying was a small, easy, expected action, and that the person chose not to expend even that minimal effort, conveying dismissiveness, laziness, or a slight.

(b) Presupposition of "bother to": it presupposes that replying was a feasible, low-cost action that the person could reasonably have performed, and that there was a normative expectation that the person should/would reply. Implicature (conversational): the speaker judges the person as careless, indifferent, or rude; the non-reply is framed as an active choice to avoid minimal effort, possibly a deliberate slight, and the speaker expected or felt entitled to a reply.

(c) "bother to" cannot describe an action the speaker thinks should not have been expected, because the construction presupposes the action was a reasonable, low-cost, and expected thing to do. Example: "The baby didn't bother to reply to my email." is infelicitous, because we do not expect a baby to reply—replying is not a minimal expected action for a baby. Another example: "He didn't bother to levitate." is odd, because levitating is not a feasible expected action. If the speaker deems the action non-expectable or non-required, using "bother to" violates its presupposition and sounds wrong.

【答案】
(a) 字面命题内容相同：两句都断言"他没有回复"。差别在说话人立场：(A) 是中性陈述事实；(B) 带评价态度，暗示回复是轻而易举、理应发生的小事，而对方连这点微不足道的努力都不愿付出，含不屑、怠慢或指责意味。
(b) 预设（presuppose）：回复是一件可行、成本低、对方本可轻易做到的事，且存在"对方应当/会回复"的规范期待。隐含（implicate）：说话人认为对方粗心、冷漠或无礼；未回复被刻画为主动不愿费举手之劳的选择，可能是一种故意冷落，且说话人本期待/有资格得到回复。
(c) "bother to" 预设该动作是合理、低成本且被期待的；因此不能用于说话人认为"本就不该期待发生"的事。例："The baby didn't bother to reply to my email." 不成立，因为我们并不期待婴儿回邮件（回复对婴儿并非可期待的微小动作）；又如 "He didn't bother to levitate." 也很怪，因为悬浮并非可行且被期待的动作。若说话人认为该动作不可期待或不必要，用 "bother to" 就违背其预设，显得不自然。

## H2

【思考】
We form a 7-digit number using each of the digits 1,2,3,4,5,6,7 exactly once. We need the count of those divisible by 11.

The divisibility rule for 11: a number is divisible by 11 iff the alternating sum of its digits is a multiple of 11. For a 7-digit number d1 d2 d3 d4 d5 d6 d7, define
S_odd = d1 + d3 + d5 + d7 (positions 1,3,5,7, four digits)
S_even = d2 + d4 + d6 (positions 2,4,6, three digits)
Condition: (S_odd − S_even) ≡ 0 (mod 11).

Total sum of all digits: 1+2+3+4+5+6+7 = 28. So S_odd + S_even = 28, and S_odd − S_even = D.
Then D = S_odd − (28 − S_odd) = 2·S_odd − 28.
S_odd is the sum of 4 distinct digits from 1..7, so its minimum is 1+2+3+4 = 10 and maximum is 4+5+6+7 = 22. Thus D ranges from 2·10 − 28 = −8 to 2·22 − 28 = 16. The multiples of 11 within [−8, 16] are −? −11 is below −8, 11 and 0 are inside, 22 is above 16. So possible D values: 0 or 11 (and possibly −11 but excluded).
- D = 11 ⇒ 2·S_odd − 28 = 11 ⇒ 2·S_odd = 39 ⇒ S_odd = 19.5, not an integer ⇒ impossible.
- D = 0 ⇒ 2·S_odd − 28 = 0 ⇒ S_odd = 14, and then S_even = 14. This is the only viable case.

So we must choose 4 digits from {1..7} whose sum is 14; those four occupy the odd positions, and the remaining three (sum 14) occupy the even positions.

Enumerate 4-element subsets of {1,2,3,4,5,6,7} summing to 14:
{1,2,4,7} = 14
{1,2,5,6} = 14
{1,3,4,6} = 14
{2,3,4,5} = 14
No others (checking: all other 4-combinations give sums ≠ 14). So there are 4 such subsets.

For each valid choice: the 4 chosen digits can be arranged in the 4 odd positions in 4! = 24 ways, and the remaining 3 digits can be arranged in the 3 even positions in 3! = 6 ways. So each subset yields 24 × 6 = 144 numbers.

Total = 4 × 144 = 576.

【答案】
共有 576 个。

推导：被 11 整除的判别法为奇数位数字和与偶数位数字和之差是 11 的倍数。七位数各位数字 1–7 各用一次，总和 28。设奇数位（第1,3,5,7位，共4位）和为 S_odd，偶数位（第2,4,6位，共3位）和为 S_even，则 S_odd+S_even=28，差 D=2·S_odd−28。S_odd 最小 10、最大 22，故 D∈[−8,16]，其中 11 的倍数只有 0 和 11。D=11 时 S_odd=19.5 非整数，舍去；D=0 时 S_odd=14（S_even=14）。
从 {1..7} 取 4 个数和为 14 的子集共 4 个：{1,2,4,7}、{1,2,5,6}、{1,3,4,6}、{2,3,4,5}。每个子集对应：4 个奇数位排列 4!=24 种，3 个偶数位排列 3!=6 种，共 24×6=144 个。总数 = 4×144 = 576。

## H1

【思考】
The sentence is from Mencius: "王顾左右而言他。"

(a) Meaning of 他 here: In pre-Qin Chinese, 他 meant "other, another" (别的、其他的), not a third-person pronoun. So "言他" means "spoke of other things / changed the subject to something else." The king turned to his attendants on the left and right and spoke about other matters, thereby dodging the question.

(b) Why it cannot be the modern third-person pronoun "he/him": In classical/pre-Qin Chinese, 他 had not yet grammaticalized into a third-person personal pronoun. The third-person pronouns then were 之 (used as object) and 其 (used as possessive or in-clause subject). The use of 他 as a personal pronoun ("he/him/it") developed much later, in medieval/early modern Chinese (roughly after the Tang–Song period). In Mencius' time 他 was an adjective/determiner meaning "other" (e.g., 他人 "other people", 他国 "other states", 他日 "another day"). Therefore reading it as the modern pronoun is anachronistic.

(c) The specific deviation if read as third-person "him": The sentence would be misread as "The king looked left and right and spoke about him," falsely introducing a specific third-party referent ("him") who is not in the text. This destroys the actual pragmatic point: the king avoided answering by diverting to unrelated topics. The correct sense is "the king turned aside and spoke of other things (to evade the question)," not "spoke about some particular person." Thus the modern-pronoun reading corrupts both the reference (invents a nonexistent antecedent) and the intended meaning (evasion by changing the subject).

【答案】
(a) "他"在此意为"别的事、其他事情"（他=其他的）。"王顾左右而言他"指齐王环顾左右侍从，说起了别的话题，以此回避问题。
(b) 不能理解为现代汉语第三人称代词"他（他/她/它）"，因为在先秦汉语中"他"尚未语法化为人称代词。当时第三人称用"之"（作宾语）、"其"（作定语或从句主语）。"他"作人称代词是唐、宋以后才逐渐发展起来的用法。先秦"他"是"别的、其他的"之意，如"他人"（别人）、"他国"（别国）、"他日"（改日）。故以今义读古书属于以今律古。
(c) 若按"第三人称代词"理解，整句会被误读为"王环顾左右，说起他（某个人）来"，凭空添入一个原文并不存在的指称对象（"他"），并掩盖了原句的语用重点——王用岔开话题的方式来逃避回答。正确含义是"王转过头去谈别的事（以避而不答）"，而非"谈论某个特定的人"。因此这种误读既虚构了不存在的先行词，又歪曲了"顾左右而言他"所表达的回避、支吾之意。

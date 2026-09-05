# EN_H10 解题记录

## H1

【思考】
The sentence "王顾左右而言他" comes from the book Mengzi (Mencius), in the chapter "Liang Hui Wang Xia" (梁惠王下). The king, when pressed with an awkward political question, looked to his left and right attendants and spoke of "他" instead of answering.

(a) Step 1: Determine the meaning of "他" in this context. In Pre-Qin classical Chinese, the character 他 (often written 佗 in earlier texts) meant "other / another / different," used adjectivally or as a determiner meaning "别 (other)". The third-person pronoun usage of "他" (meaning "he/him") did not yet exist in Pre-Qin Chinese; it developed much later, becoming common only in the medieval and vernacular periods. Therefore in this sentence "言他" means "spoke of other things / changed the topic to something else." The king avoided the question by talking about a different matter.

(b) Step 2: Why can it not be read as the modern third-person pronoun "he/him"? First, chronologically, Pre-Qin texts used 之 (object form) and 其 (genitive/subject form) for third-person reference, never 他. Second, grammatically, if "他" were a third-person pronoun it would have to be the object of the verb "言" (to speak), requiring an identifiable antecedent male person in the discourse. But no such referent exists in the context; the king simply deflects to "other topics." So interpreting it as "him" produces a structurally unsupported pronoun with no antecedent.

(c) Step 3: The concrete deviation if one forces the modern pronoun reading. "王顾左右而言他" would then be parsed as "The king looked left and right and spoke to/about him," implying the king addressed some specific male person. This destroys the actual idiomatic point: the king's evasion by shifting to an unrelated subject ("changing the topic"). The famous idiom "顾左右而言他" means precisely "to dodge a question by talking about something else." A pronoun reading loses the meaning of topic-avoidance and incorrectly imports a referent who is absent from the text.

【答案】
(a) 句中的"他"是先秦汉语中的形容词/代词用法，意为"别的、其他的"。"言他"即"说别的事/转换话题"。整句意为：大王环顾左右侍从，说起了别的事情（借以回避问题）。

(b) 不能理解为现代汉语第三人称代词"他"，原因有二：其一，时代上，先秦汉语用"之""其"表示第三人称，并不用"他"作人称代词，第三人称的"他"是后世（近古、白话）才发展起来的；其二，语法上，若将"他"视作"言"的宾语（人称代词），则文中必须有一个明确的男性先行词，但上下文并无此指称对象，因此无法成立。

(c) 若按"第三人称代词"理解，句子会变成"大王环顾左右，对他说话/谈起他"，即大王在和某个特定男子交谈。这完全偏离了原意：原句的核心在于大王"顾左右而言他"是用转换话题来回避尴尬提问，现已凝固为"顾左右而言他"这一成语，表示"答非所问、岔开话题"。人称代词读法既丢失了"避而不答"的语用含义，又凭空引入了一个文本中不存在的所指对象。

---

## H2

【思考】
We must count 7-digit numbers formed by using each of {1,2,3,4,5,6,7} exactly once, that are divisible by 11.

Step 1: Divisibility rule for 11. A number with digits d1 d2 d3 d4 d5 d6 d7 (d1 is the leftmost/most significant) is divisible by 11 iff the alternating sum d1 − d2 + d3 − d4 + d5 − d6 + d7 is a multiple of 11 (i.e., congruent to 0 mod 11). Define S_odd = d1 + d3 + d5 + d7 (positions 1,3,5,7) and S_even = d2 + d4 + d6 (positions 2,4,6). The alternating sum equals S_odd − S_even.

Step 2: Total sum of all seven digits = 1+2+3+4+5+6+7 = 28. So S_odd + S_even = 28. We need S_odd − S_even ≡ 0 (mod 11).

Step 3: Determine which multiples of 11 are possible. The even positions hold exactly 3 distinct digits, so S_even ranges from a minimum of 1+2+3 = 6 to a maximum of 5+6+7 = 18. Then S_odd − S_even = (28 − S_even) − S_even = 28 − 2·S_even. Since S_even ∈ [6,18], 2·S_even ∈ [12,36], hence D = 28 − 2·S_even ∈ [−8, 16]. The multiples of 11 in this interval are only 0 and 11 (and −11 is out of range, 22 is out of range).

Step 4: Check parity. S_odd = (28 + D)/2 and S_even = (28 − D)/2 must both be integers. If D = 11, then S_odd = 39/2 = 19.5, not an integer, so D = 11 is impossible. If D = −11, S_odd = 17/2 = 8.5, impossible. Therefore the only feasible value is D = 0, which forces S_odd = S_even = 14.

Step 5: So we need to partition the set {1,2,3,4,5,6,7} into a 3-element subset (the even positions) summing to 14 and its 4-element complement (the odd positions) automatically summing to 28 − 14 = 14. Enumerate all 3-element subsets summing to 14:
- With largest element 7: the other two sum to 7 → {1,6}, {2,5}, {3,4}. This gives {1,6,7}, {2,5,7}, {3,4,7}.
- With largest element 6 (and excluding 7): other two sum to 8 from {1..5} → {3,5}. This gives {3,5,6}.
- With largest element 5 (excluding 6,7): other two sum to 9 from {1..4}, maximum 3+4=7 < 9, none.
Thus exactly 4 such subsets: {1,6,7}, {2,5,7}, {3,4,7}, {3,5,6}. Their complements are {2,3,4,5}, {1,3,4,6}, {1,2,5,6}, {1,2,4,7}, each summing to 14. So there are 4 valid partitions.

Step 6: For each partition, assign the 3 chosen digits to the 3 even positions (positions 2,4,6) in 3! = 6 ways, and the remaining 4 digits to the 4 odd positions in 4! = 24 ways. That yields 6 × 24 = 144 numbers per partition. With 4 partitions, total = 4 × 144 = 576.

【答案】
共有 **576** 个这样的七位数能被 11 整除。

推导要点：
- 被 11 整除判别法：奇数位数字和与偶数位数字和之差为 11 的倍数。
- 七个数字总和 28；偶数位恰 3 个数字，其和 S_even ∈ [6,18]，故差值 D = 28 − 2·S_even ∈ [−8,16]。该区间内 11 的倍数只有 0 和 11，而 D=11 会使 S_odd=19.5（非整数），舍去，故只能 D=0，即奇偶位和均为 14。
- 偶数位 3 个数字和为 14 的子集共 4 个：{1,6,7}、{2,5,7}、{3,4,7}、{3,5,6}。
- 每个划分下，偶数位 3! 排列、奇数位 4! 排列，共 4 × 3! × 4! = 4 × 6 × 24 = 576。

---

## H3

【思考】
Compare (A) "He didn't reply." and (B) "He didn't bother to reply."

(a) Literal propositional content: Both sentences assert the same truth-conditional proposition — that he did not produce a reply. In terms of what is strictly said (the at-issue content), they do not differ; both entail "no reply occurred." The difference is in speaker stance / attitude. Sentence (A) is neutral and merely reports the absence of a reply. Sentence (B), by adding "bother to," expresses the speaker's evaluative stance: the speaker treats replying as a low-cost, easy, and expectable action, and presents the subject's failure to do it as a sign of laziness, neglect, discourtesy, or lack of concern. So (B) is critical/negative toward the subject, while (A) is non-committal.

(b) Presupposition and implicature of "bother to." The expression "bother to V" presupposes that V is an action that is feasible/available to the subject and that it would normally require (at most) only trivial effort — i.e., it is the kind of thing one could easily do and that is, in the context, a reasonable candidate action. More specifically, "He didn't bother to reply" presupposes that replying was an option open to him and that it was (minimally) expected or at least appropriate in the circumstance. The conversational implicature (following Gricean reasoning) is that he should have replied, that replying would have cost him little, and that his not replying reflects badly on him (he was indifferent, lazy, or rude). The added "bother to" thus conveys criticism that is absent from (A).

(c) Why "He didn't bother to reply" cannot describe an action the speaker thinks should NOT be expected. Because "bother to" presupposes that the action is a feasible, low-cost, and contextually expectable thing for the subject to do. If the speaker believes the action is not something one would expect the subject to do (because it is beyond the subject's capacity or simply not a normal expectation), the presupposition is violated and the sentence becomes infelicitous. Example: "The stone didn't bother to move" is odd, because stones are not expected to move and moving is not a low-effort option for a stone. Another example: "The comatose patient didn't bother to reply" is inappropriate, since we do not expect a comatose person to reply; saying "bother to" wrongly presupposes that replying was an easy, expected action for him. Thus "bother to" requires the action to be one the speaker regards as normally expected and easily performable.

【答案】
(a) 两句话的真值命题内容（字面所说）没有差别，都断言"他没有回复"。差别在说话人立场：(A) 是中性报道，仅陈述"未回复"这一事实；(B) 加了 "bother to"，表达了说话人的评价立场——把"回复"视为成本低、本应做到的小事，并将对方未回复归结为懒散、疏忽、无礼或漠不关心，带有明显的批评色彩。

(b) 预设（presupposition）："bother to" 预设该动作对主语而言是可行且（至多）仅需极小努力的，是在该语境中合理、本可被期待去做的事；即"回复"本是对他开放的一个选项，且至少是恰当的、可期待的。隐含（implicature）：他本来应该回复；回复对他而言轻而易举；他不回复这件事反映出他冷漠/懒惰/无礼。因此 (B) 比 (A) 多出一层批评意味。

(c) "bother to" 预设该动作是主语"本可轻易做到、且理应被期待"的事。若说话人认为某动作根本不该被期待发生（即超出主语能力或本就不在常理预期内），该预设就被破坏，句子不成立。例如 "The stone didn't bother to move"（石头懒得动）很别扭，因为石头本就不会动、移动对它不是低成本选项；又如 "The comatose patient didn't bother to reply" 不合适，因为昏迷者本就不被期待回复。可见 "bother to" 要求动作是说话人眼中"正常且轻易可完成"之事。

---

## H4

【思考】
Three people A, B, C; each is either a Knight (always tells the truth) or a Knave (always lies).

Statements:
- A: "B is a knave."
- B: "A and C are of the same type."
- C: "A is a knight."

Step 1: Analyze A's statement. If A is a Knight (truth-teller), then his claim "B is a knave" is true, so B is a Knave. If A is a Knave (liar), then his claim "B is a knave" is false, so B is a Knight. Therefore A and B must be of OPPOSITE types in every consistent scenario: A=K ⇒ B=N, and A=N ⇒ B=K.

Step 2: Consider the two possible types of A.

Case 1 — A is a Knight. Then by Step 1, B is a Knave (liar). B's statement "A and C are of the same type" must therefore be false. So A and C are NOT of the same type. Since A is a Knight, C must be a Knave. Now check C: C is a Knave, so C's statement "A is a knight" must be false. That would mean A is NOT a knight (A is a Knave). But this contradicts our assumption that A is a Knight. Hence Case 1 is impossible.

Case 2 — A is a Knave. Then by Step 1, B is a Knight (truth-teller). B's statement "A and C are of the same type" must be true. Since A is a Knave, C must also be a Knave. Now check C: C is a Knave, so C's statement "A is a knight" must be false — that is, A is not a knight, i.e., A is a Knave. This is consistent with A being a Knave. All three statements are now satisfied:
- A (Knave) lies: "B is a knave" is false because B is a Knight. ✓
- B (Knight) tells truth: "A and C are the same type" — both are Knaves. ✓
- C (Knave) lies: "A is a knight" is false because A is a Knave. ✓

Step 3: Exhaustiveness. A can only be Knight or Knave. Case 1 (A=Knight) leads to a contradiction; Case 2 (A=Knave) is fully consistent and unique. Therefore there is exactly one solution.

【答案】
唯一解：**A 是无赖，B 是骑士，C 是无赖**（A=knave, B=knight, C=knave）。

完整排除过程：
- 由 A 说"B 是无赖"可知 A、B 必为异类：若 A 说真话（骑士）则 B 确为无赖；若 A 说谎（无赖）则其话为假，B 实为骑士。
- 情形一：假设 A 是骑士 → B 为无赖（说谎）。B 说"A 与 C 同类"为假，故 A、C 不同类；A 是骑士 ⇒ C 是无赖。但 C 若为无赖，其" A 是骑士"应为假，即 A 不是骑士，与假设矛盾。故情形一不成立。
- 情形二：假设 A 是无赖 → B 为骑士（说真话）。B 说"A 与 C 同类"为真，A 是无赖 ⇒ C 也是无赖。检验 C：C 是无赖，其" A 是骑士"为假，即 A 不是骑士（确为无赖），自洽。
- A 只有骑士/无赖两种可能，情形一矛盾、情形二唯一成立，故解唯一。

---

## H5

【思考】
Sentence: "他谁都不认识。"

(a) Possible interpretations and the usage of 谁.
Interpretation 1 (standard): "He doesn't know anyone / He knows no one." Structurally, 他 is the subject (experiencer) and 谁 is the object of 认识, with 都 marking the universal quantifier. Here 谁 is a 任指 (free/universal indefinite), meaning "anyone / everyone" under negation: for every x, he does not know x.
Interpretation 2 (also available): "No one knows him." Structurally, 他 is the object (theme) and 谁 is the subject, with 他 fronted as a topic/object: "[As for him], no one knows (him)." Again 谁 is 任指 ("anyone"), meaning for every x, x does not know him.
In both readings 谁 is 任指 (bound universal), NOT 虚指 (vague reference, as in "好像谁在敲门") and NOT 疑问 (interrogative, which would require a question form). The negation 不 plus the universal yields "no one."

(b) Root of the ambiguity. Chinese is an analytic language with no morphological case marking; the third-person pronoun 他 has the same form whether it is subject or object. The phrase 谁…都 is a quantificational construction (谁 = universal, 都 = distributive marker). In "他谁都不认识," the linear order S–[谁都–不–认识] allows two structural parses: (i) 他 is the matrix subject and [谁都…认识] is a VP with 谁 as the scrambled/fronted object; (ii) 他 is a topicalized/fronted object and 谁 is the subject of the clause. Because there is no case marker to distinguish subject from object, and because 他 can surface pre-verbally as either a genuine subject or a dislocated object/topic, the sentence is structurally ambiguous between "he knows no one" and "no one knows him." It is essentially a scope/linear-order ambiguity of an unmarked pronoun.

(c) Comparison with "他谁都认识." The ambiguity is NOT of the same degree. "他谁都认识" is strongly (almost exclusively) read as "He knows everyone" (他 subject, 谁 object), and the alternative "Everyone knows him" reading is heavily dispreferred or effectively unavailable. The asymmetry comes from the interaction of negation with the universal. In the negative sentence, "谁都不" naturally forms a negative universal subject meaning "no one," which licenses 他 as a fronted object/topic ("as for him, no one knows him"). In the affirmative sentence, "谁都" reads as "everyone," and with 他 already occupying the pre-verbal subject slot, the parser settles on 他 as the experiencer-subject, making the "everyone knows him" object-reading much harder to get. So the negative sentence is genuinely two-way ambiguous, whereas the positive sentence is essentially one-way (he knows everyone).

【答案】
(a) 两种理解：
1. "他谁都不认识" = 他不认识任何人（他主语、谁宾语）。此时"谁"是任指（约束性全称代词），意为"任何人/每个人"，在否定下表"无人"：对所有人 x，他都不认识 x。
2. "他谁都不认识" = 谁都不认识他（即"没有人认识他"）。此时"他"是宾语（受事），"谁"是主语，"他"前置为话题/宾语：对所有人 x，x 都不认识他。
两种读法里"谁"都是任指，不是虚指（如"好像谁在敲门"），也不是疑问（无疑问句式）。

(b) 歧义根源：汉语是分析语，无形态格标记；第三人称代词"他"作主、宾语形式相同。结构"谁…都"是量化结构（谁=全称，都=分配标记）。"他谁都不认识"的线性顺序 S–[谁都–不–认识]允许两种句法分析：(i) 他作矩阵主语，[谁都…认识]作谓语、谁为前置宾语；(ii) 他为话题/前置宾语，谁为小句主语。因无格标记区分主宾语，且"他"可前置作主语或脱位宾语/话题，故产生"他不认识任何人"与"没有人认识他"的结构歧义。本质上是无格标记代词的辖域/线性位置歧义。

(c) 与"他谁都认识"相比，歧义程度不同。后者几乎只读作"他认识所有人"（他主语、谁宾语），"所有人都认识他"这一读法极受抑制、基本不可得。差异来自否定与全称的互动：否定句中"谁都不"可自然构成否定的全称主语"没有人"，从而许可"他"作前置宾语/话题（"至于他，没人认识他"）；肯定句中"谁都"读"所有人"，且"他"已占据动词前主语位置，分析者倾向于把"他"定为感事主语，故"所有人都认识他"的宾语读法很难成立。简言之，否定句为双向歧义，肯定句基本为单向（他认识所有人）。

---

## H6

【思考】
Evaluate each learner sentence for naturalness/correctness.

(1) "I'm looking forward to meet you." — Error: "look forward to" takes a gerund/ noun phrase after "to" because "to" here is a preposition, not part of an infinitive. Correction: "I'm looking forward to meeting you."

(2) "She suggested me to take the train." — Error: "suggest" cannot be followed by an object + infinitive (no "suggest sb to do" pattern). Possible correct patterns: "She suggested (that) I take the train" (subjunctive/indicative complement), or "She suggested taking the train." Correction: "She suggested (that) I take the train." (or "She suggested taking the train.")

(3) "Despite of the rain, we went out." — Error: "despite" is itself a preposition meaning "in spite of"; it is NOT followed by "of." Correction: "Despite the rain, we went out." (Alternatively "In spite of the rain, we went out.")

(4) "He's capable to do it." — Error: "capable" is followed by "of" + gerund, not by an infinitive. Correction: "He's capable of doing it."

(5) "I would rather stay than to go." — Error: after "would rather ... than ...," both verbs are bare infinitives (no "to"). Correction: "I would rather stay than go."

(6) "It's worth to try." — Error: "worth" is followed by a gerund, not an infinitive. Correction: "It's worth trying." (If one wants an infinitive, use "worthwhile": "It's worthwhile to try.")

【答案】
(1) 错误。"look forward to" 中 to 是介词，后接动名词而非不定式。正确：I'm looking forward to **meeting** you.

(2) 错误。"suggest" 不能接"宾语 + to do"结构。正确：She suggested **(that) I take** the train. 或 She suggested **taking** the train.

(3) 错误。"despite" 本身就是介词（意为 in spite of），后面不接 of。正确：**Despite** the rain, we went out. （或 In spite of the rain, we went out.）

(4) 错误。"capable" 后接 of + 动名词，不接不定式。正确：He's capable **of doing** it.

(5) 错误。"would rather ... than ..." 两侧都用动词原形（不带 to）。正确：I would rather stay than **go**.

(6) 错误。"worth" 后接动名词，不接不定式。正确：It's worth **trying**. （若想用不定式，应改 worth 为 worthwhile：It's worthwhile to try.）

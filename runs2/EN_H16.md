# 高难度测试卷参考答案（H1–H6）

## H1

【思考】
Step 1: Identify the sentence. It is a famous line from Mencius: "Wang gu zuo-you er yan ta" — the King turned his head left and right and then spoke of "ta".
Step 2: Determine the meaning of "ta" in pre-Qin Chinese. In classical/official Chinese of the pre-Qin period, the graph 他 (often written 佗 or 它) meant "other", "another", "else", "different", or "other matters/things". It had not yet grammaticalized into the third-person pronoun "he/him/it" (that function was served by 其, 之, 彼, etc.).
Step 3: Therefore in this sentence "ta" means "other things / something else / other topics". The King, being asked an awkward question, turned aside and spoke about other matters — i.e., he changed the subject / dodged the question.
Step 4: Why can it not be the modern third-person pronoun? Because the third-person personal pronoun 他 did not exist as such in pre-Qin Chinese. The character 他 was used lexically for "other", not as a pronominal reference to a person. Reading it as modern "he/him" is an anachronism imported from Modern Mandarin.
Step 5: If one wrongly interpreted "ta" as the third-person pronoun "he/him", the sentence would be parsed as "The King looked left and right and spoke to/about him (a specific male third party)". This produces a concrete deviation: (i) it introduces a referent (a specific male person) that is absent from the original context; (ii) it changes the act from "changing the subject / deflecting" to "addressing or mentioning a particular person"; (iii) it destroys the idiomatic point of the line, which is to describe someone who avoids an uncomfortable question by talking about unrelated things. The modern idiom "gu zuo you er yan ta" means exactly "to evade a question by changing the subject".

【答案】
(a) "他"在句中意为"别的事/其他话题"，即"王左顾右盼，说起别的事情（岔开话题）"。
(b) 不能理解为现代汉语第三人称代词"他"，因为在先秦汉语中"他"（常写作"佗""它"）是"别的、其他的"之意，尚未虚化为第三人称代词；当时指代"他/它"多用"其""之""彼"等。把"他"当作现代"他"是时代错置。
(c) 若按"第三人称代词"理解，整句会变成"王左顾右盼，对他（某个特定的男性第三方）说话/说起他"，偏差在于：凭空引入原语境中并不存在的特定男性指称对象；把"岔开话题、回避问题"误读为"提及或针对某个具体的人"；并抹去了该名句"顾左右而言他"用以形容人回避尴尬问题、转移话题的语义核心。

## H2

【思考】
Step 1: We form 7-digit numbers using digits 1,2,3,4,5,6,7 each exactly once. Total such numbers = 7! = 5040.
Step 2: Divisibility by 11 rule: for a number with digits d1 d2 d3 d4 d5 d6 d7 (d1 most significant), it is divisible by 11 iff the alternating sum (d1 - d2 + d3 - d4 + d5 - d6 + d7) ≡ 0 (mod 11).
Step 3: Let S_odd = d1 + d3 + d5 + d7 (the four positions with plus signs) and S_even = d2 + d4 + d6 (the three positions with minus signs). The test is S_odd - S_even ≡ 0 (mod 11).
Step 4: The total sum of digits is 1+2+3+4+5+6+7 = 28, so S_odd + S_even = 28.
Step 5: S_odd is the sum of 4 distinct digits chosen from {1,...,7}. Minimum S_odd = 1+2+3+4 = 10; maximum S_odd = 4+5+6+7 = 22. S_even = 28 - S_odd, so S_even ranges from 6 to 18. Hence S_odd - S_even = 2·S_odd - 28 ranges from 2·10-28 = -8 to 2·22-28 = 16. The only multiple of 11 in [-8, 16] is 0. Therefore we require S_odd - S_even = 0, i.e., S_odd = S_even = 14.
Step 6: We must choose a 4-element subset of {1,...,7} summing to 14; the remaining 3 digits automatically sum to 14. Enumerate all 4-element subsets with sum 14:
- {1,2,4,7} = 14
- {1,2,5,6} = 14
- {1,3,4,6} = 14
- {2,3,4,5} = 14
These are exactly 4 subsets (verified by complement: the 3-element complements are {3,5,6},{3,4,7},{2,5,7},{1,6,7}, also summing to 14).
Step 7: For each valid partition, assign the 4 "odd-position" digits to the 4 odd positions (1,3,5,7) in 4! ways, and the 3 "even-position" digits to the 3 even positions (2,4,6) in 3! ways. That gives 4! × 3! = 24 × 6 = 144 arrangements per subset.
Step 8: Total = 4 × 144 = 576.

【答案】
能被 11 整除的七位数共有 **576** 个。

## H3

【思考】
Step 1: Compare (A) "He didn't reply." and (B) "He didn't bother to reply."
Step 2: (a) Literal propositional content: both sentences have the same truth-conditional content — they both assert that he did not produce a reply. There is no difference in what is literally claimed to be true. The difference is in speaker stance/attitude: (A) is neutral and merely reports the absence of a reply; (B) conveys that the speaker regards the non-reply as involving a failure on his part — that he could have replied but chose not to expend the (small) effort, showing laziness, indifference, or disrespect.
Step 3: (b) Presupposition of (B): "bother to V" presupposes that V was a feasible, effort-requiring, and at least normatively expected/appropriate action — i.e., that a reply was owed or reasonably expected and that replying would have been possible. Implicature of (B): by using "bother", the speaker conventionally and conversationally implicates a negative evaluation of the subject — that he was inconsiderate, dismissive, or lazy in not replying.
Step 4: (c) Why (B) cannot describe something the speaker thinks was not to be expected: because "bother to V" carries the presupposition that V was the expected/owed/appropriate action and that the subject declined to invest the required effort. If the speaker believes the action was genuinely not expected of the subject, the frame is infelicitous. Example: "The rock didn't bother to move." — a rock is not expected to move and cannot agentively exert effort, so "bother to" is bizarre. Another example: "The baby didn't bother to file a tax return." — babies are not expected to file tax returns, so the sentence is odd. Thus "didn't bother to V" requires a context where V was normatively expected and agentively possible.

【答案】
(a) 两句话的字面命题内容相同——都断言"他没有回复"，真值条件无差别。差别在说话人立场：(A) 中性地陈述"未回复"这一事实；(B) 带有评价色彩，暗示说话人认为"他本可以回复却懒得/不愿花这点力气去回复"，含有对其怠慢、冷漠或失礼的负面态度。
(b) "bother to" 预设（presuppose）：回复是一件可行、需要付出（至少少量）努力、且在规范层面是被期待/理应做的事（即回信本是被欠或合理的期待）。它隐含（implicate）：说话人对主语持负面评价——认为他漠不关心、敷衍或懒惰。
(c) "didn't bother to V" 预设 V 是被人期待/理应去做且主语本可施行的代理性动作；若说话人认为该动作根本不该被期待，此用法便不成立。例如："The rock didn't bother to move."（石头不会被期待去移动，也无法主动费力）或 "The baby didn't bother to file a tax return."（不会期待婴儿报税），均因缺乏"理应期待"的预设而显得不自然。

## H4

【思考】
Step 1: Setup. Each of A, B, C is either a Knight (always tells truth) or a Knave (always lies).
Statements:
- A: "B is a knave."
- B: "A and C are of the same type."
- C: "A is a knight."
Step 2: Test the hypothesis that A is a Knight.
If A is a Knight, then A's statement is true, so B is a Knave. Since B is a Knave, B's statement is false. B said "A and C are the same type"; its negation means A and C are of DIFFERENT types. A is a Knight, so C must be a Knave. But then C (a Knave) says "A is a knight" — that statement is TRUE (because A is a knight), yet a Knave cannot utter a true statement. Contradiction. Therefore A cannot be a Knight; A must be a Knave.
Step 3: Hence A is a Knave. Then A's statement "B is a knave" is false, so B is a Knight.
Step 4: Since B is a Knight, B's statement is true: "A and C are of the same type." A is a Knave, so C must also be a Knave.
Step 5: Verify C. C is a Knave, so C's statement "A is a knight" must be false. Indeed A is a Knave, so "A is a knight" is false — consistent with C being a Knave.
Step 6: Check the discarded alternatives explicitly. The only other assignments would make A a Knight, which we already showed leads to contradiction. The assignment (A=Knave, B=Knight, C=Knave) is the unique consistent one.

【答案】
A 是无赖（Knave），B 是骑士（Knight），C 是无赖（Knave）。
推理：假设 A 是骑士，则 A 说真话→B 是无赖；B 说谎→"A 与 C 同类"为假→A、C 异类→C 是无赖；但 C 说"A 是骑士"却为真（因 A 确为骑士），无赖不能说真话，矛盾。故 A 必为无赖。A 说谎→"B 是无赖"为假→B 是骑士。B 说真话→"A 与 C 同类"为真→C 也是无赖。验证：C 为无赖，其言"A 是骑士"为假（A 实是无赖），成立。其余分配均导致矛盾，故此解唯一。

## H5

【思考】
Step 1: Analyze the sentence "Ta shei dou bu ren-shi" (he / who / all / not / know).
Step 2: (a) There are two principal readings.
Reading 1 (Ta as subject): "He doesn't know anyone / he knows nobody." Here 他 is the subject and 谁 is the object of 认识, interpreted as a free-choice/universal (任指) pronoun meaning "anyone / everyone", bound by 都 and negated by 不.
Reading 2 (Ta as topicalized object): "No one knows him." Here 他 is a topic that is the object of 认识, and 谁 is the subject, also a 任指 universal meaning "anyone / everyone", so "shei dou bu ren-shi ta" = no one knows him, with 他 fronted as topic: "Ta, shei dou bu ren-shi."
In both readings 谁 is 任指 (universal/free-choice), NOT 疑问 (interrogative) and NOT 虚指 (vague "someone").
Step 3: (b) Root of ambiguity. The surface string allows two grammatical-relation assignments because (i) 认识 is a transitive verb with two human participants, and (ii) Chinese permits object topicalization, so the initial NP 他 can be either the clause subject or a fronted object. Combined with the universal quantifier 谁…都(不), the scope/grammatical role of 他 and 谁 can be reassigned. Thus the ambiguity is structural/syntactic (a scope and grammatical-relation ambiguity), not lexical.
Step 4: (c) Compare with "Ta shei dou ren-shi" (He knows everyone). This affirmative sentence likewise has two readings: Reading 1 "He knows everyone" (他 subject, 谁 object); Reading 2 "Everyone knows him" (他 topicalized object, 谁 subject). In principle the logical ambiguity is the same (two readings). The difference in degree: in the negative sentence the two readings are about equally natural and balanced, because the negated universal clause "shei dou bu ren-shi" (= no one knows) is itself a natural independent clause that readily takes 他 as a topicalized object. In the affirmative, the subject reading "he knows everyone" is the strongly preferred/default reading, while the object-topic reading "everyone knows him" is more marked and usually needs a context or prosodic break (Ta, shei dou ren-shi). So the affirmative is pragmatically less ambiguous in everyday interpretation, though logically both admit two readings.

【答案】
(a) 两种理解：
理解一（"他"作主语）："他谁都不认识"= 他一个人也不认识（他谁也不认识）。此时"谁"作"认识"的宾语，是任指用法，意为"任何人/所有人"，受"都"约束、被"不"否定。
理解二（"他"作话题/宾语）："他，谁都不认识"= 谁都不认识他（没人认识他）。此时"他"是"认识"的话题化宾语，"谁"作主语，仍是任指（任何人），整句为"任何人都认识不了他"。
两种理解中"谁"均为任指，不是疑问、也不是虚指。
(b) 歧义根源是句法/结构上的：一是"认识"为二元及物动词，两个论元都可为人；二是汉语允许宾语话题化，句首"他"既可是主语，也可是前置的宾语。再叠加"谁…都（不）"全称量化的辖域，使得"他"与"谁"的语法角色和辖域可重新分配，从而构成结构歧义（而非词汇歧义）。
(c) "他谁都认识"同样有歧义：理解一"他认识所有人"（他主语、谁宾语），理解二"所有人都认识他"（他话题化宾语、谁主语）。逻辑上两者歧义程度相同（都是两解）。差别在于语用显著度：否定句"他谁都不认识"的两个理解在自然度上更均衡（"谁都不认识"本身可作独立小句，便于把"他"当话题宾语）；而肯定句"他谁都认识"中"他认识所有人"这一主语句读是强势默认理解，"所有人都认识他"的话题宾语读更依赖语境或停顿，因而日常理解中歧义感略弱。

## H6

【思考】
Step 1: Examine each sentence for collocation/grammar errors.
(1) "I'm looking forward to meet you." Error: "look forward to" takes a gerund, because "to" here is a preposition, not the infinitive marker. Correct: "I'm looking forward to meeting you."
(2) "She suggested me to take the train." Error: "suggest" cannot take the pattern "suggest + indirect object + to-infinitive". Correct forms: "She suggested (that) I take the train" or "She suggested my taking the train" (or "She suggested taking the train").
(3) "Despite of the rain, we went out." Error: "despite" is a preposition and is NOT followed by "of"; the "of" belongs to "in spite of". Correct: "Despite the rain, we went out." (or "In spite of the rain, we went out.")
(4) "He's capable to do it." Error: "capable" is followed by "of + gerund", not an infinitive. Correct: "He's capable of doing it."
(5) "I would rather stay than to go." Error: after "would rather ... than ...", both verbs are bare infinitives; "to" must not appear after "than". Correct: "I would rather stay than go."
(6) "It's worth to try." Error: "worth" is followed by a gerund (or a noun), not an infinitive. Correct: "It's worth trying." (or "It's worth a try.")

【答案】
(1) 错误。"look forward to" 中 to 是介词，后接动名词。正确：I'm looking forward to meeting you.
(2) 错误。"suggest" 不能接 "sb to do" 结构。正确：She suggested (that) I (should) take the train. 或 She suggested taking the train.
(3) 错误。"despite" 是介词，后面不接 of（of 属于 in spite of）。正确：Despite the rain, we went out. 或 In spite of the rain, we went out.
(4) 错误。"capable" 后接 "of + 动名词"，不接不定式。正确：He's capable of doing it.
(5) 错误。"would rather ... than ..." 前后都用动词原形，than 后不加 to。正确：I would rather stay than go.
(6) 错误。"worth" 后接动名词或名词，不接不定式。正确：It's worth trying. 或 It's worth a try.

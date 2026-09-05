# 高难度测试卷作答（EN_H4）

## H1

【思考】
Step 1: Identify the sentence and its source. "王顾左右而言他" is a famous line from *Mencius* (《孟子·梁惠王下》). The context: Mencius corners King Xuan of Qi with a series of rhetorical questions, and the king, unable to answer, shifts the topic.

Step 2: Parse each word. "王" = the king. "顾" = to turn one's head / look around. "左右" = left and right, here meaning his attendants / retinue on either side. "而" = connective, "and then". "言" = to speak. "他" = the word in question.

Step 3: Determine the meaning of "他" in pre-Qin Chinese. In classical (pre-Qin) Chinese, "他" did NOT mean the third-person pronoun "he/him". Its original and standard meaning then was "别的、其他的" (other, another, different). The character is formed from 人 (person radical) + 也; its lexical sense was "别也" (other). So "言他" means "speak of other things" = change the subject / talk about something else. The whole sentence means: "The king looked left and right (at his attendants) and spoke of other matters" — i.e., he evaded the question by shifting the topic.

Step 4: Why it cannot be the modern third-person pronoun "他". The dedicated third-person pronouns in the modern sense (他=he, 她=she, 它=it) did not exist in pre-Qin Chinese. Third-person reference in classical Chinese used words like 之, 其, 彼, 厥. The shift of "他" to mean "he/him" is a later development (gradually from the Wei-Jin period onward, and standardized in the early 20th century with the 他/她/它 split). Therefore reading "他" as "he" imports a modern meaning anachronistically into a classical text — it is a case of the same character being reused for a different word.

Step 5: The specific deviation if read as third-person "he". If "他" = "him/he", the sentence becomes "The king looked left and right and spoke of him/about him." This is incoherent for two reasons: (i) there is no male antecedent introduced in the context for "他" to refer to, so it fails referentially; (ii) more importantly, it destroys the actual pragmatic point of the passage — that the king avoided answering by talking about unrelated things. The crucial meaning "to change the subject / evade the topic" is completely lost, and the sentence becomes nonsensical.

【答案】
(a) "他"在先秦汉语中是"别的、其他的"之意，"言他"即"说别的事"，整句意为：国王左右张望（看身边的侍从）而谈起别的事情——也就是顾左右以转移话题、回避问题。
(b) 不能理解为现代第三人称代词"他"，是因为先秦汉语中根本没有专门表示"他/她/它"的第三人称代词；当时指代第三人称用"之、其、彼"等。"他"原为"别的"之义（"他，别也"），借用为"他/她/它"是后世（约魏晋以后，现代规范更晚）的语义与用字演变。因此用现代"他"去套古文属于以今律古。
(c) 若按"第三人称代词"理解，句子变成"国王左右张望，说起他（某人）来"。这会产生具体偏差：一是语境中并无可指代的男性先行词，指代落空；二是彻底丢失了原句"转移话题、回避质问"的核心含义，使整句话变得不知所云。

## H2

【思考】
Step 1: State the divisibility rule for 11. A number is divisible by 11 iff the alternating sum of its digits is a multiple of 11 (including 0). Equivalently, let the seven-digit number be d1 d2 d3 d4 d5 d6 d7 (positions counted from the left). Then (d1 + d3 + d5 + d7) − (d2 + d4 + d6) ≡ 0 (mod 11). Since the number has 7 digits (an odd count), counting positions from left or from right gives the same parity classes, so the sets {positions 1,3,5,7} and {positions 2,4,6} are well defined.

Step 2: Let S_odd = sum of digits in positions 1,3,5,7 (four digits) and S_even = sum of digits in positions 2,4,6 (three digits). The total sum of available digits is 1+2+3+4+5+6+7 = 28. So S_odd + S_even = 28.

Step 3: The divisibility condition is S_odd − S_even ≡ 0 (mod 11), i.e., S_odd − S_even = 11k for some integer k. Substitute S_even = 28 − S_odd:
S_odd − (28 − S_odd) = 2·S_odd − 28 = 11k.

Step 4: Determine possible values. S_odd is the sum of 4 distinct digits from 1..7, so its minimum is 1+2+3+4 = 10 and maximum is 4+5+6+7 = 22. Thus 2·S_odd ranges from 20 to 44, so 2·S_odd − 28 ranges from −8 to 16. Within this range, the only multiples of 11 are 0 and 11 (and −11 is below −8). 
- If 2·S_odd − 28 = 0 → 2·S_odd = 28 → S_odd = 14. Valid (14 is in [10,22]).
- If 2·S_odd − 28 = 11 → 2·S_odd = 39 → S_odd = 19.5. Not an integer → impossible.
- If 2·S_odd − 28 = −11 → 2·S_odd = 17 → S_odd = 8.5, also below range → impossible.
So the ONLY valid case is S_odd = 14 and S_even = 14.

Step 5: Find the subsets. We need to choose 4 digits (for odd positions) summing to 14; the remaining 3 (even positions) automatically sum to 14. Enumerate 4-element subsets of {1,2,3,4,5,6,7} with sum 14:
- {1,2,4,7} = 14
- {1,2,5,6} = 14
- {1,3,4,6} = 14
- {2,3,4,5} = 14
There are exactly 4 such subsets (equivalently, 4 subsets of 3 elements summing to 14: {3,5,6},{3,4,7},{2,5,7},{1,6,7}).

Step 6: Count arrangements. For each of the 4 valid partitions, assign the 4 chosen digits to the 4 odd positions in 4! = 24 ways, and the 3 remaining digits to the 3 even positions in 3! = 6 ways. That gives 24 × 6 = 144 numbers per partition.

Step 7: Total = 4 × 144 = 576.

【答案】
能被 11 整除的七位数共有 **576** 个。推导：被 11 整除的判别法是奇数位数字和与偶数位数字和之差为 11 的倍数。设奇数位（1,3,5,7 共 4 位）数字和为 S_odd，偶数位（2,4,6 共 3 位）为 S_even，则 S_odd + S_even = 28，且 S_odd − S_even = 11k。代入得 2·S_odd − 28 = 11k。S_odd 介于 10 与 22 之间，故 2·S_odd−28 在 −8 到 16 之间，其中 11 的倍数只有 0，得 S_odd = S_even = 14。从 1–7 中取 4 个数和为 14 的子集恰有 4 个：{1,2,4,7}、{1,2,5,6}、{1,3,4,6}、{2,3,4,5}。每组在 4 个奇数位上有 4! 种、3 个偶数位上有 3! 种排列，即 24×6=144 个；总计 4×144=576。

## H3

【思考】
Step 1: Compare the literal propositional content of (A) and (B).
(A) "He didn't reply."
(B) "He didn't bother to reply."
Both sentences assert the same truth-conditional / propositional fact: he did not produce a reply. In terms of what is literally said (the at-issue content), there is no difference — both are true just in case no reply occurred.

Step 2: Difference in speaker stance / attitude. (A) is neutral and merely reports the absence of a reply. (B) adds the phrase "bother to", which encodes the speaker's evaluative stance: it conveys that replying would have required only trivial effort (a small, easy action), yet the person chose not to expend even that minimal effort. The speaker thereby expresses a negative assessment — that the person was inconsiderate, dismissive, lazy, or rude.

Step 3: Presupposition and implicature introduced by "bother to".
- Presupposition: "bother to V" presupposes that V is a low-cost, trivially easy action that one could and (given the context) normally would be expected to do; and that the subject had the capacity/opportunity to perform it. So "He didn't bother to reply" presupposes that replying was an easy, expectable thing for him to do.
- Implicature (conversational): by using "bother to" the speaker implicates that the person is being deliberately careless or dismissive — a mild pejorative evaluation of the subject's conduct.

Step 4: Why "bother to" cannot describe an action the speaker thinks "should not be expected to happen in the first place". The phrase presupposes that the action is a minimal, expectable effort. If the speaker believes the action was NOT something one should expect (because it is unreasonable, impossible, or beyond the subject's expected duties), the presupposition is violated and the sentence sounds odd or infelicitous. Example: "The baby didn't bother to thank the guests." A baby is not expected to thank guests; saying it "didn't bother to" falsely presupposes the baby should have made that trivial effort, which is absurd. Another example: "He didn't bother to read the entire 2000-page contract in one sitting." Reading a 2000-page contract at once is not a trivial, expectable action, so "bother to" is inappropriate — one would instead say "He didn't read the whole contract." Thus "bother to" requires the action to be a small, normatively expected effort.

【答案】
(a) 两句话的字面命题内容没有差别，都断言"他没有回复"。差别在说话人立场：(A) 中性陈述；(B) 通过 "bother to" 表达说话人认为"回复本是轻而易举的小事，对方却连这点力气都不肯花"，带有负面评价（轻率、怠慢、不礼貌）。
(b) 加上 "bother to" 后：预设（presuppose）"回复是一件成本低、轻而易举、本可且本应做的事，且对方有能力和机会去做"；隐含（implicate）"此人居心怠慢/刻意不理，说话人对其行为持贬义评价"。
(c) "bother to" 预设该动作是微小、可期待的努力。若说话人认为这件事"本就不该期待发生"（不合理、不可能或超出对方应有职责），预设落空，句子就不自然。例如 "The baby didn't bother to thank the guests."（婴儿本就不该被期待去致谢，说它"懒得"致谢是荒谬的）；又如 "He didn't bother to read the entire 2000-page contract in one sitting."（一夜读完 2000 页合同并非可期待的小事，故不宜用 bother to）。

## H4

【思考】
Step 1: Set up the problem. A, B, C are each either a Knight (always tells the truth) or a Knave (always lies). Their statements:
- A: "B is a Knave."
- B: "A and C are of the same type."
- C: "A is a Knight."

Step 2: Analyze by cases on A's type, since A's statement directly concerns B and C's statement directly concerns A, giving a tight loop.

Case 1: Suppose A is a Knight (truth-teller).
- Then A's statement "B is a Knave" is true → B is a Knave.
- Since B is a Knave, B's statement "A and C are of the same type" is false → A and C are NOT the same type.
- A is a Knight, so C must be a Knave.
- Since C is a Knave, C's statement "A is a Knight" is false → A is NOT a Knight → A is a Knave.
- Contradiction: we assumed A is a Knight but derived A is a Knave. Therefore Case 1 is impossible. A cannot be a Knight.

Step 3: Therefore A must be a Knave.
- A is a Knave, so A's statement "B is a Knave" is false → B is NOT a Knave → B is a Knight.
- B is a Knight, so B's statement "A and C are of the same type" is true → A and C are the same type.
- A is a Knave, so C is also a Knave.
- Check C: C is a Knave, so C's statement "A is a Knight" must be false → A is not a Knight → A is a Knave. This matches our assumption. Consistent.

Step 4: Rule out all other assignments to prove uniqueness. There are 2^3 = 8 possible assignments. From Step 2, any assignment with A = Knight leads to contradiction, so A must be Knave. Given A = Knave, A's false statement forces B = Knight (it is impossible for B to be Knave, because then "B is a Knave" would be true, contradicting that A the Knave lies). With A = Knave and B = Knight forced, B's true statement forces A and C same type, hence C = Knave. No other branch is possible. Thus the unique solution is A = Knave, B = Knight, C = Knave.

【答案】
唯一自洽且排除了所有其他可能的身份分配是：**A 是无赖，B 是骑士，C 是无赖**。

推理：
- 假设 A 是骑士，则 A 说真话→"B 是无赖"为真→B 是无赖；B 说谎→"A、C 同类"为假→A、C 不同类；A 是骑士故 C 是无赖；C 说谎→"A 是骑士"为假→A 是无赖，与假设矛盾。故 A 不可能是骑士，A 必为无赖。
- A 是无赖，则其话为假→"B 是无赖"假→B 是骑士；B 说真话→"A、C 同类"真→C 与 A 同类→C 是无赖；验证 C："A 是骑士"为假，符合 C 是无赖。一致。
- 唯一性：A 为骑士必矛盾，故 A 只能是无赖；A 是无赖时其假话强制 B 为骑士（B 不能是无赖，否则"A 说 B 是无赖"成真而与 A 说谎矛盾）；B 为真又强制 C 与 A 同类即无赖。无其他分支。

## H5

【思考】
Step 1: Identify the ambiguous sentence "他谁都不认识" and its two main readings. Chinese allows either NP (他) to be subject or object because there is no case marking.

Reading 1 (他 as subject / experiencer): 他 [subject] 谁都不认识 → "He does not know anyone." Here 他 is the subject of 认识, and 谁 is the object. The phrase 谁都 is a 周遍 (universal) phrase in a negative context: 谁 = 任指 "anyone/anybody", and 都不 = "none". So: He doesn't recognize/know anybody.

Reading 2 (他 as object / theme): 谁都不认识他 → "Nobody knows him." Here 谁 is the subject (任指 "everyone/nobody") and 他 is the object of 认识. The surface "他谁都不认识" is the topic-fronted / object-preposed version of "谁都不认识他" (with 他 moved to the front as topic). Meaning: No one knows him.

In both readings 谁 is the 任指 (free reference) use of the interrogative pronoun 谁 within a negative (or 都) construction, meaning "anyone / nobody" rather than an actual question.

Step 2: Root of the ambiguity (syntactic/morphological). The ambiguity is an argument-structure / grammatical-role ambiguity:
- Chinese has no morphological case marking (no nominative/accusative distinction) and no agreement, so 他 carries no marker telling us whether it is subject or object.
- The verb 认识 is symmetric-ish in surface form: both "X 认识 Y" (X knows Y) and "Y 被 X 认识" map onto the same lexical frame; 他 can occupy either the experiencer-subject slot or the theme-object slot.
- The 周遍 phrase 谁都(不) can scope over either argument, and Chinese permits object topicalization/fronting ("他，谁都不认识" = "him, nobody knows"). With no comma and no case marker, the surface string is genuinely ambiguous between 他=subject and 他=object.

Step 3: Compare with "他谁都认识". This affirmative version is also ambiguous in principle but the two readings are not equally balanced:
- Reading 1 (他 subject): 他 knows everyone. (Dominant, preferred reading.)
- Reading 2 (他 object): 谁都认识他 = Everyone knows him. (Possible but much less preferred / more marked.)

The difference in ambiguity degree: "他谁都不认识" has two roughly equally acceptable readings (both "He knows nobody" and "Nobody knows him" are natural). "他谁都认识" is strongly biased toward the single reading "He knows everyone"; the "Everyone knows him" reading is available but noticeably less natural. 

Why the asymmetry? Negation (不) with 都 creates a 周遍-negative construction that readily licenses object preposing / topicalization of either argument, making both scopal assignments equally plausible. In the affirmative, the pre-verbal NP 他 is overwhelmingly interpreted as the subject (SVO default), so the object-preposing reading is suppressed. Thus the negative sentence is MORE ambiguous (two balanced readings) than the affirmative one (one dominant reading).

【答案】
(a) 两种主要理解：
- 理解一（他作主语/认知者）："他谁都不认识" = 他一个人都不认识（他谁也不认识）。"谁"为任指用法，相当于"任何人"，在否定句中表"没有人"。
- 理解二（他作宾语/被知者）："谁都不认识他" = 没有人认识他。此时"谁"作主语（任指"人人/无人"），"他"是"认识"的宾语，原句是其话题前置/宾语前置形式（"他，[谁都不认识]"）。
两种理解中"谁"都是疑问代词的任指用法（在"都(不)"句中表"任何人/无人"），并非真正的疑问。
(b) 歧义的句法/形态根源：汉语无形态格标记（主宾语同形）、无一致关系，"他"不带任何标明主/宾的标记；动词"认识"的论元"他"既可占据"认知者-主语"位，也可占据"被知者-宾语"位；且"谁都(不)"这类周遍短语可作用于任一词论元，汉语又允许宾语话题化前置。于是无逗号、无格标记的表面字符串在"他=主语"与"他=宾语"两种结构间产生真歧义。
(c) 与"他谁都认识"相比，后者的歧义程度不同：后者也有两解（他认识所有人；所有人都认识他），但强烈偏向"他认识所有人"这一解，"所有人都认识他"虽可但明显不自然。原因在于否定词"不"配"都"构成的周遍否定句同时容纳两种论元前置，两解较为均衡；而肯定句中动词前的"他"默认按 SVO 理解为主语，宾语前置解被抑制。因此"他谁都不认识"歧义更重（两解均衡），"他谁都认识"歧义较轻（一解占优）。

## H6

【思考】
Evaluate each sentence for collocation/grammar correctness.

(1) "I'm looking forward to meet you."
- Error: "look forward to" takes a gerund (the "to" is a preposition, not part of an infinitive). 
- Correction: "I'm looking forward to meeting you."

(2) "She suggested me to take the train."
- Error: "suggest" is not a verb that takes an indirect object + infinitive complement (unlike advise/tell/order). It takes either a that-clause or a gerund.
- Correction: "She suggested (that) I take the train." or "She suggested taking the train." (If you want the "me + infinitive" pattern, use "advised": "She advised me to take the train.")

(3) "Despite of the rain, we went out."
- Error: "despite" is itself a preposition and does NOT take "of". (The phrase with "of" is "in spite of".)
- Correction: "Despite the rain, we went out." (or "In spite of the rain, we went out.")

(4) "He's capable to do it."
- Error: "capable" is followed by "of" + gerund, not by an infinitive.
- Correction: "He's capable of doing it."

(5) "I would rather stay than to go."
- Error: after "would rather ... than ...", both verbs must be bare infinitives; the "to" is ungrammatical.
- Correction: "I would rather stay than go."

(6) "It's worth to try."
- Error: "worth" is followed by a gerund (or a noun), not an infinitive.
- Correction: "It's worth trying." (or "It's worth a try.")

【答案】
(1) 错误。"look forward to" 中 to 是介词，后接动名词而非不定式。正确：I'm looking forward to meeting you.
(2) 错误。"suggest" 不能接"间接宾语 + 不定式"（不同于 advise/tell），应接 that 从句或动名词。正确：She suggested (that) I take the train. / She suggested taking the train.（若要表"建议某人做某事"可用 advise：She advised me to take the train.）
(3) 错误。"despite" 本身是介词，不能加 of（带 of 的是 in spite of）。正确：Despite the rain, we went out.
(4) 错误。"capable" 后接 of + 动名词，不接不定式。正确：He's capable of doing it.
(5) 错误。"would rather ... than ..." 后两动词均用原形（不带 to）。正确：I would rather stay than go.
(6) 错误。"worth" 后接动名词或名词，不接不定式。正确：It's worth trying. / It's worth a try.

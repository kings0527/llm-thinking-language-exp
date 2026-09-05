# 高难度测试卷解答（EN_H7）

## H1

【思考】
Step 1: Locate the sentence. The line "Wang gu zuo-you er yan ta" appears in the Confucian classic Mencius (the book attributed to the philosopher Mengzi), in a dialogue where the king is pressed with a series of moral/political questions about his duties. When cornered, the king avoids answering.

Step 2: Determine the meaning of the word "ta" in this context. In Old Chinese (pre-Qin Chinese), the word spelled "ta" (written 佗/它/他 interchangeably) meant "other, another, different" (别的). It was NOT a third-person pronoun. The third-person pronouns of that period were "zhi" (之) and "qi" (其). The use of "ta" as the masculine third-person pronoun "he/him" is a much later development (roughly medieval/early modern Chinese).

Step 3: Therefore "yan ta" (言他) literally means "speak of other [matters]" — i.e., the king turned to a different topic, changed the subject, and dodged the question. The whole line means: "The king looked to the left and right and spoke of other things" (= evaded the issue).

Step 4: Why it cannot be the modern third-person pronoun. Reading "ta" as "he/him" would force the parse "the king looked left and right and spoke TO him," which (a) introduces a mysterious third party who is not present in the two-person dialogue, and (b) destroys the documented point of the anecdote, which is precisely the king's evasion. The grammar and the narrative context both require "ta" = "other matters."

Step 5: Concrete deviation if read as third-person pronoun. The sentence would be wrongly translated as "The king looked left and right and spoke to him," implying the king addressed some unnamed male third person instead of changing the subject. This loses the semantic core "evasion / topic-shift" and invents a referent that the text never supplies.

Step 6: Pre-Qin usage evidence. "Ta" (它/他) routinely meant "other/another" in classical texts. Example from the Book of Songs (Shi Jing): "ta shan zhi shi, ke yi gong yu" — "the stones of OTHER mountains can be used to polish jade." Here "ta" clearly means "other," not a pronoun. So in Mencius the same word means "other matters."

【答案】
(a) "他"在这里的意思是"别的（事情/话题）"，即"言他"=说别的事、转移话题。
(b) 不能理解为现代汉语第三人称代词"他（他/他）"，因为先秦汉语中"他"（亦作"佗""它"）义为"别的、其他的"，而当时的第三人称代词是"之""其"；"他"作第三人称代词是后世才有的用法。
(c) 若按"第三人称代词"理解，整句会变成"王看了看左右，然后对他（某个男性第三者）说话"，凭空引入了一个文本中并不存在的对话对象，并且完全丢失了原文"顾左右而言他"所表达的"避而不答、转移话题"的核心含义。结合先秦用法（如《诗经》"它山之石，可以攻玉"中"它"即"别的"），可知此处只能是"别的事"。

## H2

【思考】
Step 1: We form seven-digit numbers using the digits 1,2,3,4,5,6,7 exactly once each (all distinct). Let the digits in positions 1 through 7 (from the left) be d1 d2 d3 d4 d5 d6 d7.

Step 2: Divisibility-by-11 test. A number is divisible by 11 iff the alternating sum of its digits is a multiple of 11 (i.e., ≡ 0 mod 11). Taking the sign starting with + on d1: (d1 − d2 + d3 − d4 + d5 − d6 + d7) ≡ 0 (mod 11).

Step 3: Define S_odd = d1 + d3 + d5 + d7 (the four odd-indexed positions) and S_even = d2 + d4 + d6 (the three even-indexed positions). The alternating sum equals S_odd − S_even. Also S_odd + S_even = 1+2+3+4+5+6+7 = 28.

Step 4: Conditions. We need S_odd − S_even ≡ 0 (mod 11), i.e., S_odd − S_even = 11k for some integer k. Together with S_odd + S_even = 28, adding gives 2·S_odd = 28 + 11k. So 28 + 11k must be even ⇒ 11k even ⇒ k even.

Step 5: Bounds on S_odd. Since S_odd is the sum of 4 distinct digits from {1,…,7}, its minimum is 1+2+3+4 = 10 and maximum is 4+5+6+7 = 22. So 10 ≤ S_odd ≤ 22.

Step 6: Test possible even k.
- k = 0: S_odd = (28+0)/2 = 14, S_even = 14. Valid (14 is within [10,22]).
- k = 2: S_odd = (28+22)/2 = 25 > 22. Impossible.
- k = −2: S_odd = (28−22)/2 = 3 < 10. Impossible.
- Larger |k| only worsens the bound. So the ONLY possibility is S_odd = S_even = 14.

Step 7: Find all 4-element subsets of {1,2,3,4,5,6,7} summing to 14. Enumerate:
- 1+2+4+7 = 14
- 1+2+5+6 = 14
- 1+3+4+6 = 14
- 2+3+4+5 = 14
No others (verified by exhaustive pairing). So there are exactly 4 valid partitions: the 4 odd-position digits are one of these sets, and the complementary 3 digits (which automatically sum to 14) occupy the even positions.

Step 8: Count arrangements. For each of the 4 partitions:
- The 4 chosen digits can be arranged among the 4 odd positions in 4! = 24 ways.
- The remaining 3 digits can be arranged among the 3 even positions in 3! = 6 ways.
So each partition yields 24 × 6 = 144 numbers.

Step 9: Total = 4 × 144 = 576.

【答案】
能被 11 整除的七位数共有 **576** 个。

推导要点：被 11 整除的判别法是"奇数位数字和与偶数位数字和之差是 11 的倍数"。设奇数位（第1、3、5、7位）数字和为 S_odd，偶数位（第2、4、6位）为 S_even，则 S_odd + S_even = 28，且 S_odd − S_even ≡ 0 (mod 11)。解得唯一可能是 S_odd = S_even = 14。从 {1…7} 中取 4 个数和为 14 的子集恰有 4 个：{1,2,4,7}、{1,2,5,6}、{1,3,4,6}、{2,3,4,5}。每个子集对应 4!×3! = 144 种排列，故总数为 4 × 144 = 576。

## H3

【思考】
Step 1: Compare propositional (truth-conditional) content. (A) "He didn't reply" and (B) "He didn't bother to reply" both assert the same factual proposition: he produced no reply. In strict truth conditions there is NO difference — if he did not reply, both are true; if he did reply, both are false.

Step 2: Speaker stance difference. (B) adds an evaluative, subjective layer. "Bother to" frames the action as one that would have required only minimal effort and that the speaker expected or felt was warranted. So (B) conveys irritation, criticism, or disappointment: the speaker thinks he could easily have replied but chose not to expend even that small effort.

Step 3: Presupposition of "didn't bother to reply." The construction presupposes:
- Replying was a genuine, available option for him (he was able to).
- Replying would have been a small/negligible effort ("bother" implies trivial cost).
- There was a reasonable expectation or obligation that he might reply (the action was a live, expected possibility).
Step 4: Implicature of "didn't bother to reply." By using "bother," the speaker conversationally implicates that he was at fault/negligent — that a reply was owed or at least naturally expected, yet he couldn't be troubled to give one. The speaker signals annoyance.

Step 5: Why it cannot describe something the speaker thinks "should never have been expected." "Bother to" carries the presupposition that the action was an easy, natural, and expectable thing to do. If the speaker holds that the event was never a reasonable expectation in the first place, that presupposition is violated, making the sentence infelicitous. Example: "My cat didn't bother to wish me happy birthday." We do not actually expect a cat to wish us a birthday — so "didn't bother to" is odd, because it falsely presupposes an expectation that doesn't exist. Equally: "The rock didn't bother to roll downhill" is bizarre, since rocks have no volition and no one expects a rock to "bother." The verb "bother" requires an agent and a presumed-minimal, expected action.

【答案】
(a) 两句话在字面命题内容上**没有差别**——都断言"他没有回复"这一事实。差别在于说话人立场：(B) 多了评价态度，暗示回复本是轻而易举、且说话人认为理应/期待发生的事，从而传达不满、批评或失望。
(b) 加上 "bother to" 后，**预设（presuppose）**了：回复是他能做到的、且只需极小代价、并且本有合理期待/义务他会回复；**隐含（implicate）**了：他是有过错的、本该回复却懒得费这点力气，说话人对此感到不快。
(c) "bother to" 预设该动作是轻而易举、自然且可期待的。若说话人认为此事"本就不该被期待"，预设失败，句子不成立。例如 "My cat didn't bother to wish me happy birthday."（猫本就不会祝生日快乐，谈不上"懒得费心"）或 "The rock didn't bother to roll downhill."（石头无意志，没人期待它会"费心"），均因预设落空而显得不自然。

## H4

【思考】
Let K = knight (always tells truth), N = knave (always lies). Statements:
- A: "B is a knave."
- B: "A and C are of the same type."
- C: "A is a knight."

Step 1: Case analysis on A.
Case 1 — Suppose A is a knight (K). Then A's statement is true, so B is a knave (N). Since B is a knave, B's statement is false. B said "A and C are the same type"; its negation means A and C are DIFFERENT types. A is K, so C must be N. Now check C: C is N, so C's statement must be false. But C said "A is a knight," and A IS a knight, so C's statement is TRUE. Contradiction (a knave cannot utter a true statement). Therefore Case 1 is impossible.

Step 2: Case 2 — Suppose A is a knave (N). Then A's statement "B is a knave" is false, so B is a knight (K). Since B is a knight, B's statement is true: "A and C are the same type" is true. A is N, so C must also be N. Check C: C is N, so C's statement must be false. C said "A is a knight"; A is actually N, so that statement is false — consistent. No contradiction.

Step 3: Exhaustiveness. A must be either K or N, and Case 1 fails while Case 2 succeeds uniquely. Hence the only consistent assignment is A = knave, B = knight, C = knave.

Step 4: Verification against all 8 assignments (to exclude others explicitly):
- A=K,B=K: A's claim "B is knave" would be false, but a knight can't lie → reject.
- A=K,B=N,C=K: from Case 1 already contradictory (C ends up forced to N) → reject.
- A=K,B=N,C=N: B lies ⇒ A,C different, but both K? no, A=K,C=N are different, that part ok; but recompute: A=K ⇒ B=N (ok); B=N ⇒ "A,C same" false ⇒ A,C different ⇒ C=N (ok so far); C=N ⇒ "A is knight" must be false, but A=K makes it true ⇒ reject.
- A=N,B=K,C=K: A=N ⇒ "B is knave" false ⇒ B=K (ok); B=K ⇒ "A,C same" true ⇒ A,C same, but A=N,C=K differ ⇒ reject.
- A=N,B=K,C=N: works (our solution).
- A=N,B=N,C=K: A=N ⇒ B=K, contradict B=N ⇒ reject.
- A=N,B=N,C=N: A=N ⇒ B=K, contradict B=N ⇒ reject.
- A=K,B=K,C=N already covered by A=K fail.
Only A=N,B=K,C=N survives.

【答案】
A 是无赖（knave），B 是骑士（knight），C 是无赖（knave）。

推理过程：假设 A 是骑士，则 A 说真话→B 是无赖；B 说谎→"A 和 C 同类"为假→A、C 不同类，因 A 是骑士故 C 是无赖；但 C 说" A 是骑士"为真，而无赖不能说真话，矛盾。故 A 必为无赖。A 是无赖→"B 是无赖"为假→B 是骑士；B 说真话→"A 和 C 同类"为真，A 是无赖故 C 也是无赖；C 说" A 是骑士"为假，符合无赖身份。逐一排除其余 7 种分配后，仅有此解自洽。

## H5

【思考】
The sentence is "TA SHUI dou bu ren-shi" (他谁都不认识), with TA = he/him, SHUI = who/anyone, DOU = all/every, BU = not, REN-SHI = know/recognize.

Step 1: Identify the two readings.
Reading 1 (TA as subject/experiencer, SHUI as object): "He doesn't know anyone." Formally: for every x, TA does not know x. Here SHUI is a free/bound indefinite meaning "anyone/whoever" (任指), serving as the object, and DOU quantifies over it.
Reading 2 (SHUI as subject, TA as object): "Nobody knows him." Formally: for every x, x does not know TA. Here SHUI is again 任指 ("whoever/anyone"), but now interpreted as the subject, and TA is the object. The sentence pragmatically means "As for him, whoever it is does not know him" = nobody knows him.

Step 2: Usage of SHUI. In both readings SHUI is 任指 (a generic/universal indefinite bound by DOU), NOT an interrogative (there is no question) and NOT mere 虚指 (empty/vague reference, as in "找个谁聊聊" = find someone to chat with). It is a bound variable over individuals.

Step 3: Root of ambiguity (syntactic/morphological). Chinese lacks morphological case marking: TA and SHUI are both bare pronouns with no nominative/accusative distinction. Word order is normally SVO (TA first would be subject), but Chinese also permits topic/focus structures where SHUI can be construed as the subject within a DOU-quantified construction. Because REN-SHI is transitive with two animate arguments, either argument can occupy the subject or object slot, and DOU can bind SHUI in either position. The absence of case morphology plus the floatability of DOU and the symmetric animacy of the two arguments produces the ambiguity.

Step 4: Compare with "TA SHUI dou ren-shi" (他谁都认识).
This sentence likewise has two readings:
- Reading A: "He knows everyone" (TA subject, SHUI object = everyone).
- Reading B: "Everyone knows him" (SHUI subject = everyone, TA object).
Structurally the ambiguity is of the SAME degree: both sentences are two-way ambiguous for exactly the same reason (interchangeable subject/object assignment of TA and SHUI, with SHUI as 任指 bound by DOU). Negation (BU) does not alter the argument structure, so the source of ambiguity is unchanged.

Step 5: Possible subtle pragmatic asymmetry (optional note). Some speakers find Reading 2 of the negated sentence ("nobody knows him") slightly more salient/natural than Reading B of the positive sentence ("everyone knows him"), because claiming that NOBODY knows someone is a more notable statement than that EVERYONE knows them. But this is a pragmatic preference, not a structural difference; both remain grammatically two-way ambiguous.

【答案】
(a) 两种理解：
- 理解一（"他"为主语/"认识"的 experiencer，"谁"为宾语）："他谁都不认识"="他一个人也不认识／他不认识任何人"。此处"谁"是**任指**（bound by "都"，相当于 anyone/whoever），作宾语。
- 理解二（"谁"为主语，"他"为宾语）："谁都不认识他"="任何人都（不）认识他"="没一个人认识他"。此处"谁"仍是**任指**，但作主语，"他"作宾语。
(b) 歧义的句法/形态根源：汉语代词无主格/宾格形态标记（"他""谁"都是光杆代词，无法区分主宾语）；"都"是可在句中浮动的全称量词，可约束处在任一论元位置上的"谁"；"认识"是及物动词且两个论元都是有生名词，主宾语位置可互换。三者叠加导致"他"与"谁"的主宾角色可以互换而不改变表层形式。
(c) "他谁都认识"的歧义程度**相同**（同样两句歧义："他认识所有人"与"所有人都认识他"）。原因：否定词"不"并不改变论元结构，歧义来源（"他""谁"主宾可逆、"谁"为受"都"约束的任指）完全一致。仅有的差别是语用偏好（否定句"没人认识他"的那一读可能更自然些），但结构上二者都是双向歧义。

## H6

【思考】
Evaluate each learner sentence for naturalness/correctness, identify error type, and give the correction.

(1) "I'm looking forward to meet you." — INCORRECT. "Look forward to" uses "to" as a PREPOSITION, so it must be followed by a gerund (noun form), not a bare infinitive. Correction: "I'm looking forward to meeting you."

(2) "She suggested me to take the train." — INCORRECT. The verb "suggest" does NOT take the pattern [indirect object + infinitive]. It takes either a that-clause or a gerund. Correction: "She suggested (that) I take the train" or "She suggested taking the train." (One cannot say "suggest someone to do something.")

(3) "Despite of the rain, we went out." — INCORRECT. "Despite" is itself a preposition and is NEVER followed by "of." The "of" belongs to the synonymous phrase "in spite of." Correction: "Despite the rain, we went out." (Or "In spite of the rain, we went out.")

(4) "He's capable to do it." — INCORRECT. The adjective "capable" is followed by the preposition "of" + gerund, not by an infinitive. Correction: "He's capable of doing it."

(5) "I would rather stay than to go." — INCORRECT. After "would rather … than …" both verbs are BARE infinitives (no "to"). Correction: "I would rather stay than go."

(6) "It's worth to try." — INCORRECT. The adjective "worth" is followed by a gerund, not an infinitive. Correction: "It's worth trying." (The variant "It's worth it to try" exists in some registers, but the standard, unambiguous correction is the gerund.)

【答案】
(1) 错误。"look forward to" 中 to 是**介词**，须接动名词。改正：I'm looking forward to meeting you.
(2) 错误。"suggest" **不能**接"宾语 + to do"结构，应接 that 从句或动名词。改正：She suggested (that) I take the train. / She suggested taking the train.
(3) 错误。"despite" 本身是介词，**后面不接 of**（of 属于 in spite of）。改正：Despite the rain, we went out.
(4) 错误。"capable" 须接 "of + 动名词"，不接不定式。改正：He's capable of doing it.
(5) 错误。"would rather … than …" 后接**不带 to 的动词原形**。改正：I would rather stay than go.
(6) 错误。"worth" 后接**动名词**，不接不定式。改正：It's worth trying.

# 高难度测试卷解答

## H1

【思考】
The sentence "王顾左右而言他" appears in the chapter "Liang Hui Wang (下)" of the Mencius (《孟子·梁惠王下》). The anecdote: Mencius presses King Xuan of Qi with a chain of progressively harder questions about official responsibility, culminating in "四境之内不治，则如之何？" (if the realm is badly governed, what should be done?). The king, unable to answer, "顾左右而言他".

Step 1: Determine the meaning of "他" in this sentence. In Old Chinese / pre-Qin Chinese, "他" is a 旁指代词 (an "other"-pointing pronoun), meaning "别的、其他的" (other / something else). It is not a personal pronoun. So "言他" means "spoke of other things / changed the subject" — the king looked around at his attendants and talked about something else to avoid the embarrassing question.

Step 2: Why can it not be read as the modern third-person pronoun "he/another person"? Because the third-person personal pronoun "他" (referring to a male person) did not exist in pre-Qin Chinese. In Old Chinese, third-person reference was expressed by "其", "之", or "彼"; "他" was exclusively an determiner/pronoun meaning "other". The grammaticalization of "他" into a third-person personal pronoun is a much later (roughly medieval, 六朝 and after) development. Therefore reading it as a personal pronoun anachronistically imports a meaning that did not yet exist.

Step 3: What concrete deviation results if we force the third-person reading? If "他" = "another person / him", then "言他" would be parsed as "spoke to/of him", giving something like "The king looked left and right and spoke to that other person." This reframes the king's action as redirecting his speech toward some bystander, rather than as evading the topic. The original pragmatic point — that the king, cornered, deflected and changed the subject ("顾左右" = glanced around to dodge, "言他" = spoke of other matters) — is lost. The sentence becomes about whom he addressed, not about his evasion. So the deviation is both semantic (meaning of "他") and pragmatic (loss of the "evasion/deflection" reading).

【答案】
(a) "他"是上古汉语的旁指代词，意为"别的、其他的（事/话题）"，"言他"即"说别的事、转移话题"。
(b) 先秦汉语中"他"还没有第三人称代词的用法；当时的第三人称代词是"其""之""彼"。"他"作为第三人称"他（他称）"是后世（约六朝以后）才语法化出来的。因此不能拿现代汉语的第三人称"他"去套。
(c) 若把"他"理解为第三人称"那个人"，整句会变成"王环顾左右，去跟那个人说话"，把原文"王被问住后顾盼左右、岔开话题（回避）"误读成"王转而与他人交谈"。这就丢失了原文的语用含义——王的"顾左右而言他"是被孟子步步逼问、无法作答时的回避/转移话题，而不是在跟某个旁人说话。

---

## H2

【思考】
We form a 7-digit number using the digits 1,2,3,4,5,6,7 each exactly once. We must count those divisible by 11.

Step 1: Recall the divisibility test for 11. A number is divisible by 11 iff the alternating sum of its digits is a multiple of 11 (including 0). For a 7-digit number with digits d1 d2 d3 d4 d5 d6 d7 (from left to right), the test is:
(d1 − d2 + d3 − d4 + d5 − d6 + d7) ≡ 0 (mod 11).

Note: because there are 7 digits, the "odd positions" counted from the left (1,3,5,7) are exactly the same set as the odd positions counted from the right (7,5,3,1). So define:
S_odd = d1 + d3 + d5 + d7  (4 digits)
S_even = d2 + d4 + d6      (3 digits)
The alternating sum = S_odd − S_even. Divisibility requires S_odd − S_even ≡ 0 (mod 11).

Step 2: Total sum of all digits is 1+2+3+4+5+6+7 = 28. So S_odd + S_even = 28.
We have S_odd − S_even = 11k for some integer k. Adding the two equations: 2·S_odd = 28 + 11k, so S_odd = (28 + 11k)/2. For S_odd to be an integer, 28 + 11k must be even; 28 is even, so 11k must be even, hence k is even.
Alternatively, from S_odd + S_even = 28 and S_odd − S_even ≡ 0 (mod 11): S_odd − S_even = 2·S_odd − 28 ≡ 0 (mod 11) → 2·S_odd ≡ 28 ≡ 6 (mod 11). Multiply by the inverse of 2 mod 11, which is 6 (since 2·6=12≡1): S_odd ≡ 6·6 = 36 ≡ 3 (mod 11). So S_odd ≡ 3 (mod 11).

Step 3: Bounds on S_odd. S_odd is the sum of 4 distinct digits from {1..7}. Minimum = 1+2+3+4 = 10. Maximum = 4+5+6+7 = 22. So S_odd ∈ [10, 22]. The values in this range congruent to 3 mod 11 are only 14 (since 3 is too small and 25 is too large). Also checking the difference directly: S_odd − S_even ranges between −8 and +16; the only multiples of 11 in that range are 0 and 11. Difference = 11 gives S_odd = 19.5 (impossible, not integer); difference = 0 gives S_odd = 14, S_even = 14. So the only viable case is S_odd = S_even = 14.

Step 4: Find all 4-element subsets of {1,2,3,4,5,6,7} summing to 14.
Enumerate:
- {1,2,4,7} = 14
- {1,2,5,6} = 14
- {1,3,4,6} = 14
- {2,3,4,5} = 14
No others: any 4 distinct numbers from 1..7 summing to 14 must avoid using 7 with too-large companions, etc.; exhaustive checking confirms exactly these 4 subsets. Each subset's complement (the remaining 3 digits) automatically sums to 14, satisfying S_even = 14.

Step 5: Count arrangements. For each valid partition:
- The 4 chosen digits occupy the 4 odd positions (1,3,5,7): they can be arranged in 4! = 24 ways.
- The 3 remaining digits occupy the 3 even positions (2,4,6): arranged in 3! = 6 ways.
So per subset: 24 × 6 = 144 numbers.
With 4 subsets: 4 × 144 = 576.

【答案】
能被 11 整除的七位数共有 **576** 个。
推导要点：被 11 整除要求奇偶位数字和之差为 11 的倍数。七位数字总和 1+2+3+4+5+6+7 = 28；设奇数位（第1、3、5、7位，共4位）数字和为 S_odd，偶数位（3位）和为 S_even，则 S_odd + S_even = 28，且 S_odd − S_even ≡ 0 (mod 11)。由此推出 S_odd ≡ 3 (mod 11)，结合 S_odd 取值范围 [10,22] 唯一得 S_odd = S_even = 14。和为 14 的 4 元子集恰有 4 个：{1,2,4,7}、{1,2,5,6}、{1,3,4,6}、{2,3,4,5}。每个子集对应 4!×3! = 144 种排列，故 4×144 = 576。

---

## H3

【思考】
Compare (A) "He didn't reply." and (B) "He didn't bother to reply."

Step 1 (literal proposition vs. speaker stance): Truth-conditionally, both sentences assert the same proposition — that he did not reply. The at-issue, truth-evaluable content is identical. The difference is in speaker stance / illocutionary coloring. (A) is neutral, merely reporting a fact. (B), by inserting "bother to", adds an evaluative stance: the speaker frames replying as a trivial, low-cost action and presents his failure to reply as a deliberate refusal to expend even that minimal effort. Thus (B) conveys criticism, disapproval, or the sense that the omission was a slight/laziness, whereas (A) does not.

Step 2 (presupposition and implicature of "bother to"): "bother to V" presupposes that V is a minor, easy, normally-expected action that the subject could perform without special effort or cost. It also presupposes the subject had the capacity/opportunity to do V. Conversationally (Gricean implicature), it implicates that (i) the action was expected, (ii) the speaker disapproves of the omission, and (iii) the non-performance was a choice/deliberate neglect rather than inability. So "He didn't bother to reply" presupposes "replying is a trivial expected thing" and implicates "he was careless/rude in not doing this easy expected act."

Step 3 (why it cannot describe something not expectable): Because "bother to" presupposes the action is a trivial, expected obligation, it is infelicitous when the speaker holds that the event "should not have been expected in the first place." Example: Suppose a colleague was in a coma in the hospital for a week. One cannot naturally say "He didn't bother to reply to my email" — replying while in a coma is not a trivial, expectable action, so the presupposition fails and the utterance is odd. A more everyday example: "The baby didn't bother to thank me" is strange, because we do not expect a baby to thank anyone. The verb "bother to" requires that the act be one the subject could and should trivially perform; if it is not expectable, the presupposition is violated.

【答案】
(a) 两句话的字面命题内容相同——都断言"他没有回复"。差别在说话人立场：(A) 是中性陈述；(B) 加上 "bother to" 后带有评价立场，把"回复"框定为一件微不足道、本应顺手做的事，暗示他是故意连这点小事都不肯做，带有批评/不以为然的意味。
(b) 预设（presuppose）：回复是一件轻而易举、理应发生的小事，且主语有能力和机会去做。隐含（implicate）：这件事本在预期之中；说话人不认可这种疏漏；且"没回复"是一种故意的怠慢/选择，而非无能为力。
(c) "bother to" 预设该动作是轻微、可期待的义务，因此若说话人认为此事"本就不该被期待发生"，预设就会失败，句子不自然。例如：一位同事昏迷住院一周，说 "He didn't bother to reply to my email" 就很奇怪，因为人在昏迷中本就不可能回邮件；又如 "The baby didn't bother to thank me" 也不自然，因为我们并不期待婴儿道谢。

---

## H4

【思考】
A, B, C are each either a Knight (always truthful) or a Knave (always lies).
Statements:
- A: "B is a knave."
- B: "A and C are of the same type."
- C: "A is a knight."

We must find the assignment and rule out alternatives.

Case 1: Suppose A is a Knight.
- Then A's statement is true → B is a Knave.
- B is a Knave, so B's statement "A and C are the same type" is false → A and C are NOT the same type. Since A is a Knight, C must be a Knave.
- C is a Knave, so C's statement "A is a knight" must be false. But A is in fact a Knight, so "A is a knight" is TRUE. A Knave cannot utter a true statement → contradiction.
Therefore A cannot be a Knight. So A must be a Knave.

Case 2: A is a Knave.
- A's statement "B is a knave" is false → B is NOT a knave → B is a Knight.
- B is a Knight, so B's statement "A and C are the same type" is true → A and C are the same type. A is a Knave, so C is also a Knave.
- Check C: C is a Knave, so C's statement "A is a knight" must be false. A is a Knave, so "A is a knight" is indeed FALSE → consistent. A knave uttering a false statement is valid.
Thus the only consistent assignment is A = Knave, B = Knight, C = Knave.

Exhaustiveness check: A is either Knight or Knave. The Knight sub-case leads to a contradiction (forced C = Knave yet C's statement would be true). Hence A must be Knave, which then uniquely forces B = Knight and C = Knave, and all three statements are satisfied. No other assignment works.

【答案】
唯一自洽的分配是：**A 是无赖，B 是骑士，C 是无赖**。
推理：假设 A 是骑士，则 A 说真话→B 是无赖；B 说谎→"A 与 C 同类"为假→C 与 A 不同类→C 是无赖；但 C 说" A 是骑士"按假设为真，无赖不能说真话，矛盾。故 A 必为无赖。A 说谎→"B 是无赖"为假→B 是骑士；B 说真话→"A 与 C 同类"为真→C 与 A 同属无赖；C（无赖）说" A 是骑士"为假，符合。其余可能均被排除。

---

## H5

【思考】
Sentence: "他谁都不认识。"

Step 1: Identify the readings and the use of "谁".
Reading 1 (他 as subject, 谁 as object): 他是主语，"谁都不认识" = "doesn't know anyone". Meaning: He doesn't know anyone / there is no person he knows. Here "谁" is 任指 (free reference) occurring under a negative universal: "谁…都不" = "anyone…not" = "no one (as object)". So 谁 = "任何人" in object position, bound by the universal-negative.
Reading 2 (他 as topicalized object, 谁 as subject): 他 is a fronted topic that is the OBJECT of 认识, and 谁 is the SUBJECT. Parsed as "他（话题），谁都不认识[他]" = "As for him, no one knows him" → No one knows him. Here "谁" is again 任指 (="任何人") functioning as subject, with "都不" giving the universal-negative "no one".
In both readings "谁" is 任指, not 虚指 (vague reference, e.g. "好像在说什么") and not a genuine interrogative (疑问).

Step 2: Root of the ambiguity (syntactic/morphological). Chinese lacks case marking and allows both subject and object to precede the verb; a sentence-initial NP can be either the subject or a topicalized object. The universal quantifier phrase "谁都" (with the interrogative 谁 serving as a universal under "都" + negation) does not itself fix whether 谁 is subject or object, and "他" at the front can be parsed as either the subject of 认识 or the object that has been topicalized. There is no morphological number/case distinction to disambiguate, so the grammatical relation (who knows whom) is structurally undecided → ambiguity.

Step 3: Compare with "他谁都认识" (positive, no 不).
Reading 1: 他 subject, 谁 object (任指): "He knows everyone."
Reading 2: 他 topicalized object, 谁 subject (任指): "Everyone knows him."
Thus "他谁都认识" is ALSO two-way ambiguous in exactly the same structural way. The polarity (negation vs. affirmation) does not remove the subject/object (or topic) ambiguity, because both readings rely only on the free assignment of 他 and 谁 to the subject/object roles of 认识, which is independent of whether 不 is present. So the degree and type of ambiguity are essentially the same for the two sentences. (Pragmatically, one reading may be more salient in a given context, but structurally both sentences are equally ambiguous.)

【答案】
(a) 两种理解：
- 理解一：他作主语、谁作宾语（任指）。意为"他谁也不认识／他不认识任何人"。句中"谁"是任指，在"谁…都不"的否定全称结构中相当于"任何人（作宾语）"。
- 理解二：他是话题性宾语、谁作主语（任指）。意为"（对于）他，谁都不认识（他）"＝"没有人认识他"。句中"谁"仍是任指（相当于"任何人"作主语）。
两种理解里"谁"都是任指，不是虚指，也不是疑问。
(b) 歧义的根源于句法/形态：汉语没有格标记，句首名词既可作主语也可作话题性前置宾语；"谁都"这个全称短语（疑问代词"谁"在"都"及否定下表任指）本身并不固定"谁"是主语还是宾语，而前置的"他"既可能被分析为"认识"的主语，也可能被分析为话题化的宾语。缺乏形态格/数区分，导致"谁认识谁"的语法关系结构性地不确定，从而产生歧义。
(c) 与"他谁都认识"相比，歧义程度基本相同。肯定的"他谁都认识"同样两可：理解一"他（主）认识任何人＝他认识所有人"；理解二"他（宾/话题），谁都认识（他）＝所有人都认识他"。否定/肯定并不消除主宾语（或话题）的歧义，因为两种理解只取决于"他"与"谁"在"认识"中主语/宾语角色的分配，与是否有"不"无关。故二者歧义类型与程度一致（只是具体语境下某一读法的凸显度可能不同）。

---

## H6

【思考】
Examine each learner sentence for collocation/grammar errors.

(1) "I'm looking forward to meet you."
Error: "look forward to" takes a preposition "to", so the following word must be a gerund (noun form), not a bare infinitive. "meet" is wrong.
Correction: "I'm looking forward to meeting you."

(2) "She suggested me to take the train."
Error: "suggest" cannot take the pattern "suggest + indirect object + to-infinitive". It does not license an infinitive complement nor a dative indirect object in this way.
Correction: "She suggested (that) I take the train." / "She suggested taking the train." / "She suggested the train to me." (One may also say "She advised me to take the train," but "suggest" itself does not permit "sb to do".)

(3) "Despite of the rain, we went out."
Error: "despite" is already a preposition and must NOT be followed by "of". (The phrase with "of" is "in spite of".)
Correction: "Despite the rain, we went out." (or "In spite of the rain, we went out.")

(4) "He's capable to do it."
Error: The adjective "capable" is followed by the preposition "of" + gerund, not by an infinitive.
Correction: "He's capable of doing it."

(5) "I would rather stay than to go."
Error: After "would rather ... than ...", both verbs must be bare infinitives (base forms). The "to" before "go" is incorrect.
Correction: "I would rather stay than go."

(6) "It's worth to try."
Error: The adjective "worth" is followed by a gerund, not an infinitive.
Correction: "It's worth trying." (Alternatively "It's worthwhile to try." or "It is worth a try.")

【答案】
(1) 错误。"look forward to" 中 to 是介词，后接动名词而非不定式。正确：I'm looking forward to meeting you.
(2) 错误。"suggest" 不能接 "sb to do" 结构，也不接间接宾语+不定式。正确：She suggested (that) I take the train. / She suggested taking the train.（对比：可用 advise me to take the train，但 suggest 不行。）
(3) 错误。"despite" 本身已是介词，不能加 of（含 of 的是 in spite of）。正确：Despite the rain, we went out.（或 In spite of the rain, we went out.）
(4) 错误。"capable" 后接 of + 动名词，不接不定式。正确：He's capable of doing it.
(5) 错误。"would rather ... than ..." 前后都用动词原形（不带 to）。正确：I would rather stay than go.
(6) 错误。"worth" 后接动名词，不接不定式。正确：It's worth trying.（或 It's worthwhile to try. / It is worth a try.）

# 高难度测试卷答卷（H1–H6）

## H1

【思考】
The sentence under analysis is from *Mencius* (《孟子》): "王顾左右而言他。" We must determine the meaning of "他" in this pre-Qin (Warring States) context and explain why it cannot be read as the modern third-person pronoun.

Step 1: Parse the sentence. "王" = the king (subject). "顾" = to look back / to turn one's gaze / to look around. "左右" = to the left and right (i.e., his attendants / those beside him). "而" = connective, roughly "and then" / marking a transition. "言" = to speak. "他" = object of 言. So literally: "The king turned to look left and right, and then spoke [of] 他."

Step 2: Determine the referent and meaning of "他". In pre-Qin Chinese, "他" is not a personal pronoun. Etymologically "他" (also written 佗/它) meant "别的、其他的" = "other, another, something else." This is the original sense: "他" = "异也" (different / other), as in "他日" = "another day / some other day." Therefore "言他" means "言他事" = "to speak of other matters / to change the subject." The whole sentence describes the king avoiding an embarrassing question by turning away and talking about something else. This is a classic anecdote where the king, cornered by Mencius's pointed questions, dodges the issue.

Step 3: Why it cannot be the modern third-person pronoun "he/him." In Old Chinese (先秦), the third-person pronouns were 之, 其, and occasionally 彼 — NOT 他. The character 他 did not acquire the third-person personal-pronoun sense until much later, roughly during the 六朝/魏晋 period (after the Han dynasty, several centuries later), through a gradual semantic shift from "other" to a personal pronoun. Since *Mencius* is a Warring States text, the personal-pronoun reading is anachronistic and impossible in that period's grammar.

Step 4: What specific deviation results if we force the third-person reading. If "他" meant "him" (a third person), then "言他" would mean "spoke to/of him" — but the sentence provides no antecedent male third person for "him" to refer to; grammatically there is no such referent in context. The sentence would become incoherent: "The king looked left and right and spoke of him" — who is "him"? More importantly, the pragmatic force is lost: the entire point of the passage is the king's evasion / topic-switching (顾左右而言他 has become an idiom meaning "to evade a question by changing the subject"). Reading "他" as "he/him" destroys the idiom's meaning and turns a deliberate act of avoidance into a nonsensical reference. Thus the deviation is both grammatical (no valid antecedent) and semantic/pragmatic (loss of the "changing the subject" meaning).

Conclusion: "他" = "别的（事/话）", other things; it is not a third-person pronoun in this period.

【答案】
(a) "他"在这里的意思是"别的、其他的（事/话）"，"言他"即"说别的事情/转移话题"。整句意为：大王环顾左右而说起别的事来（借以回避问题）。

(b) 不能理解为现代汉语第三人称代词"他"，因为在**先秦汉语**中，"他"（本字也作佗/它）的本义是"别的、其他的"（如"他日"=他日/改日），当时表示第三人称用的是"之、其、彼"等，而非"他"。"他"作为第三人称代词的用法是后世（约六朝/魏晋以后）才逐渐产生的，属于时代错置。

(c) 若按"第三人称代词他/他"理解，"言他"就成了"对他说话/说他"，但句中并无任何可作"他"指代对象的男性第三人称先行词，句法上失去所指；同时会彻底丢失这句话的核心语用义——大王"顾左右而言他"本是一个成语，表示**回避问题、转移话题**，强行读作"他"就把一种刻意的避答行为变成了一句无意义的指称，既不合语法也不合文意。

---

## H2

【思考】
We must count the 7-digit numbers formed by using each of the digits 1,2,3,4,5,6,7 exactly once, that are divisible by 11.

Step 1: Recall the divisibility rule for 11. A number is divisible by 11 iff the alternating sum of its digits is a multiple of 11 (including 0). For a 7-digit number with digits d1 d2 d3 d4 d5 d6 d7 (d1 is the leftmost/most significant), the rule is:
(d1 + d3 + d5 + d7) − (d2 + d4 + d6) ≡ 0 (mod 11).
Let S_odd = d1 + d3 + d5 + d7 (the sum of digits in the 4 odd-position slots: positions 1,3,5,7), and S_even = d2 + d4 + d6 (the sum of digits in the 3 even-position slots: positions 2,4,6).

Step 2: Use the total digit sum. The digits are exactly {1,2,3,4,5,6,7}, each used once. Their total sum is 1+2+3+4+5+6+7 = 28. Hence S_odd + S_even = 28.

Step 3: Express the divisibility condition. We need S_odd − S_even ≡ 0 (mod 11). Substitute S_even = 28 − S_odd:
S_odd − (28 − S_odd) = 2·S_odd − 28.
So we require 2·S_odd − 28 ≡ 0 (mod 11), i.e., 2·S_odd − 28 ∈ {…, −22, −11, 0, 11, 22, …}.

Step 4: Constrain the possible range of S_odd. S_odd is the sum of 4 distinct digits chosen from {1..7}.
- Minimum possible S_odd = 1+2+3+4 = 10.
- Maximum possible S_odd = 4+5+6+7 = 22.
Thus 2·S_odd − 28 ranges from 2·10 − 28 = −8 up to 2·22 − 28 = 16. So the only multiples of 11 that can fall in [−8, 16] are 0 and 11 (and −11 is below −8, 22 is above 16).
- Candidate 2·S_odd − 28 = 0 → S_odd = 14. (integer, valid)
- Candidate 2·S_odd − 28 = 11 → S_odd = 19.5. (not an integer → impossible)
- Candidate 2·S_odd − 28 = −11 → S_odd = 8.5. (not an integer → impossible)
Therefore the ONLY possibility is S_odd = 14 (and consequently S_even = 28 − 14 = 14 as well).

Step 5: Count the 4-element subsets of {1..7} summing to 14. Equivalently, count the complementary 3-element subsets summing to 14 (since the remaining 3 digits must sum to 14). Enumerate 3 distinct digits from {1..7} with sum 14:
- Starting with 1: 1 + a + b = 14 → a+b = 13, with a,b ∈ {2..7} distinct: 6+7 = 13 → {1,6,7}. ✓
- Starting with 2: 2 + a + b = 14 → a+b = 12, a,b ∈ {3..7} distinct: 5+7 = 12 → {2,5,7}. ✓ (6+6 not distinct)
- Starting with 3: 3 + a + b = 14 → a+b = 11, a,b ∈ {4..7} distinct: 4+7 = 11 → {3,4,7} ✓; 5+6 = 11 → {3,5,6} ✓.
- Starting with 4: 4 + a + b = 14 → a+b = 10, a,b ∈ {5,6,7} distinct: smallest is 5+6 = 11 > 10 → none.
- Starting with 5 or more: minimum 5+6+7 = 18 > 14 → none.
So the 3-subsets summing to 14 are: {1,6,7}, {2,5,7}, {3,4,7}, {3,5,6} — exactly 4 subsets. Their complements (the 4-subsets summing to 14) are:
- complement of {1,6,7} = {2,3,4,5}
- complement of {2,5,7} = {1,3,4,6}
- complement of {3,4,7} = {1,2,5,6}
- complement of {3,5,6} = {1,2,4,7}
So there are exactly 4 choices for which set of 4 digits occupies the odd positions.

Step 6: Assign digits to positions. Once we choose which 4 digits go to the odd positions (4! = 24 ways to arrange them in positions 1,3,5,7) and which 3 digits go to the even positions (3! = 6 ways to arrange them in positions 2,4,6), the number is fully determined. Each such arrangement satisfies S_odd = S_even = 14, hence is divisible by 11, and every valid number arises this way uniquely.

Step 7: Compute total. Total = 4 × 4! × 3! = 4 × 24 × 6 = 576.

【答案】
能被 11 整除的七位数共有 **576** 个。

推导要点：被 11 整除的判定法是"奇数位数字和与偶数位数字和之差为 11 的倍数"。设奇数位（第1、3、5、7位）数字和为 S_odd，偶数位（第2、4、6位）为 S_even。数字 1–7 总和为 28，故 S_odd + S_even = 28，且 S_odd − S_even ≡ 0 (mod 11)。代入后得 2·S_odd − 28 ≡ 0 (mod 11)。S_odd 为 4 个不同数字之和，范围在 [10, 22]，故 2·S_odd − 28 落在 [−8, 16]，其中 11 的倍数只有 0（11 与 −11 均对应非整数 S_odd）。因此 S_odd = 14（S_even 也为 14）。

从 {1..7} 中选 4 个数和为 14 的子集共有 4 个：{2,3,4,5}、{1,3,4,6}、{1,2,5,6}、{1,2,4,7}。选定后，4 个奇数位可排列 4! = 24 种，3 个偶数位可排列 3! = 6 种。故总数 = 4 × 24 × 6 = **576**。

---

## H3

【思考】
Compare (A) "He didn't reply." and (B) "He didn't bother to reply."

Step 1: Truth-conditional / literal propositional content. Both sentences assert the same proposition at the level of truth conditions: that he performed no act of replying. There is no difference in what is literally true or false about the world — in any situation where he failed to reply, both (A) and (B) are true; where he replied, both are false. So the literal propositional content is identical.

Step 2: Speaker stance. (A) is neutral and purely descriptive: it reports a fact without evaluating it. (B) carries a strong subjective stance. By adding "bother to," the speaker frames the non-reply as something that would have required only minimal effort, and implies that the person nevertheless chose not to make that small effort — conveying laziness, negligence, dismissiveness, or rudeness. The speaker is not merely reporting; they are commenting on the agent's attitude/conduct.

Step 3: Presupposition vs. implicature of (B).
- Presupposition: "bother to V" presupposes that V was possible/easy and within the agent's capacity — that replying was a feasible, low-cost action. It also presupposes that there existed at least a minimal normative or situational expectation that he might reply (the action is the kind of thing one could reasonably be expected to do). In other words, the use of "bother" presupposes the reply was an available, trivial-effort option.
- Implicature (conversational): By saying he "didn't bother," the speaker conversationally implicates that he was inconsiderate or deliberately dismissive — that skipping the reply was a slight/neglect rather than an accident or impossibility. The implicature can be cancelled ("He didn't bother to reply — he was in a coma") but in the unmarked case it conveys criticism.

Step 4: Why (B) cannot describe something the speaker thinks was "not to be expected in the first place." The word "bother" inherently presupposes that the action was a small, easy, and (at least minimally) expectable courtesy. If the speaker believes the action was not something one should expect at all, then "bother to" is infelicitous because there is no small owed effort being skipped.
Example 1: "He didn't bother to fly to the moon." Flying to the moon is not a trivial, expectable action for an ordinary person; it is extraordinary, so calling it something he "didn't bother to" do is absurd — there was never any reasonable expectation.
Example 2: If a complete stranger with whom you have no relationship fails to write you a birthday letter, you would NOT say "He didn't bother to write me" — because there was no expectation or obligation for a stranger to write you. "Bother" requires a baseline of expected/minimal effort that was flouted. Hence (B) is only appropriate when the speaker regards the reply as a small, owed, or expectable act that the agent negligently skipped.

【答案】
(a) 两句话的**字面命题内容相同**——都断言"他没有回复"这一事实，真值条件一致。差别在**说话人立场**：(A) 是中性、纯陈述地报道事实；(B) 带有强烈主观评价，暗示"回复本只需极小 effort，他却连这点力气都不愿费"，传达出怠惰、轻慢或无礼的态度。

(b) 加上 "bother to" 后：
- **预设（presuppose）**：回复这件事是可行、轻松、在他能力范围内的（只需极小 effort），且至少存在一种最低限度的、他"本可以/本应"回复的情境期待。
- **隐含（implicate）**：他态度敷衍、怠慢或故意冷落——没有回复是一种"本可轻易做到却懒得做"的失礼，而非意外或不可能。

(c) "He didn't bother to reply" 不能用于说话人认为"本就不该期待发生"的事，因为 "bother" 本身**预设该动作是微小、轻松且（至少最低限度）可期待的礼貌/义务性行为**；若根本无人期待此事发生，就不存在"本可轻易做到却不愿做"的懈怠可供指责。举例：不能说 "He didn't bother to fly to the moon"（飞月球对普通人绝非可期待的轻松之事）；又如一个与你毫无关系的陌生人没给你写信，你不会说 "He didn't bother to write me"，因为本就无人期待陌生人给你写信。"bother" 成立的前提是存在一个被草率跳过的、微小的应有努力。

---

## H4

【思考】
We have three people A, B, C. Each is either a Knight (always tells the truth) or a Knave (always lies). Their statements:
- A: "B is a knave."
- B: "A and C are of the same type."
- C: "A is a knight."

We must determine each person's identity and rule out other possibilities.

Step 1: Set up case analysis on A's type, since A's statement directly concerns B and C's statement directly concerns A.

Case 1: Suppose A is a Knight (truth-teller).
- Then A's statement "B is a knave" is true → B is a Knave.
- Since B is a Knave, B's statement "A and C are of the same type" must be false → A and C are NOT of the same type.
- A is a Knight, so for A and C to be different types, C must be a Knave.
- Now check C's statement: C (a Knave) says "A is a knight." But A IS a knight, so the statement "A is a knight" is TRUE. A knave cannot utter a true statement — contradiction.
- Therefore Case 1 is impossible. A cannot be a Knight.

Case 2: Suppose A is a Knave (liar).
- Then A's statement "B is a knave" is false → B is NOT a knave → B is a Knight.
- Since B is a Knight, B's statement "A and C are of the same type" is true → A and C are the same type.
- A is a Knave, so C must also be a Knave.
- Now verify C's statement: C (a Knave) says "A is a knight." Since A is actually a Knave, the statement "A is a knight" is FALSE, which is consistent with C being a Knave (a knave must utter false statements). ✓ No contradiction.

Step 3: Verify the full assignment (A = Knave, B = Knight, C = Knave):
- A (Knave) says "B is a knave" → false, because B is a Knight. ✓ (a knave lies)
- B (Knight) says "A and C are of the same type" → A and C are both Knaves, so same type → true. ✓ (a knight tells truth)
- C (Knave) says "A is a knight" → false, because A is a Knave. ✓ (a knave lies)
All three statements are consistent.

Step 4: Uniqueness. We exhausted A's two possible types. Case 1 (A knight) led to contradiction, so A must be a Knave. That forced B = Knight and then C = Knave. Hence the assignment is unique; no other combination works. (One can also check the other 7 combinations, but the case analysis on A already proves uniqueness since each branch deterministically fixes B and C and only one branch is consistent.)

【答案】
A 是无赖（Knave），B 是骑士（Knight），C 是无赖（Knave）。

完整推理（含排除）：
- 假设 A 是骑士：则 A 说"B 是无赖"为真 → B 是无赖。B 是无赖，其" A 和 C 同类"必假 → A、C 不同类；A 是骑士故 C 为无赖。但 C（无赖）说" A 是骑士"——这句话实际为真（A 确实是骑士），无赖不能说真话，矛盾。故 A 不可能是骑士。
- 因此 A 必为无赖：A 说" B 是无赖"为假 → B 是骑士。B（骑士）说" A 和 C 同类"为真 → C 与 A 同类，即 C 也是无赖。验证 C（无赖）说" A 是骑士"为假（A 确为无赖），符合无赖说假话。全部自洽。

唯一性：A 只可能是骑士或无赖，骑士情形已被排除，故 A 必为无赖，进而唯一确定 B=骑士、C=无赖。其他任何分配都会产生矛盾。

---

## H5

【思考】
Analyze the sentence "他谁都不认识。"

Step 1: Identify the two readings.
Reading 1 (他 as subject/agent): "He doesn't know anyone." Here 他 is the subject (agent) of 认识, and 谁 is the object, interpreted as the 任指 (free/universal) indefinite "anyone / everyone," with 都 marking universal quantification over the object. Surface parsing: 他 [subject] + 谁都 [universal object phrase] + 不认识. Meaning: 他不认识任何人 (for every person x, he does not know x).
Reading 2 (他 as object/patient): "No one knows him." Here 谁 is the subject (agent), interpreted as 任指 "everyone / anyone," and 他 is the semantic object (patient) of 认识. The sentence is a topic-comment structure where 他 is in topic position but is semantically the patient. Meaning: 谁都不认识他 (for every person x, x does not know him) = nobody knows him.

Step 2: Usage of 谁 in each reading. In BOTH readings, 谁 is 任指 (free reference / universal-indefinite), not 疑问 (interrogative) and not 虚指 (vague/non-referential such as "somebody or other"). It combines with 都 to express universal quantification ("anyone/everyone"). The difference is solely whether 谁 functions as the subject (Reading 2) or the object (Reading 1) of the verb 认识.

Step 3: Syntactic/morphological root of the ambiguity. Chinese has fixed S–V–O word order and a topic-prominent structure. The sentence places 他 in the topic (pre-verbal) position. Because Chinese topics can be either the syntactic subject (agent) or the semantic object (patient) that has been fronted, 他 can be interpreted as either the agent or the patient. Meanwhile the phrase 谁…都 is a floating universal quantifier that can scope over either the subject or the object slot. The verb 认识 is semantically symmetric-ish in that both its agent and patient are human, so neither reading is blocked by selectional restrictions. The ambiguity thus arises from (i) topic–subject/object indeterminacy (他 can be agent or patient) and (ii) the free placement/scoping of the 任指 谁…都 phrase, combined with (iii) the lack of morphological case marking to disambiguate who is doing the knowing and who is being known.

Step 4: Compare with "他谁都认识." This sentence has the same two structural readings:
- Reading A': "He knows everyone" (他 subject/agent, 谁 object, 任指).
- Reading B': "Everyone knows him" (谁 subject, 他 object/patient).
So the ambiguity TYPE and DEGREE are essentially the SAME as "他谁都不认识" — both exhibit the agent/patient topic reversal ambiguity with 任指 谁…都. There is no structural difference; both are equally ambiguous. The only difference is pragmatic/salience: for "他谁都不认识" the "he knows nobody" reading tends to be more salient/preferred, while for "他谁都认识" the "he knows everyone" reading tends to be more salient. But structurally the ambiguity degree is identical — both allow both readings. (One could note that negation in the first sentence may slightly favor the "he" agent reading, but this is a matter of preference, not of whether the alternative reading exists.)

【答案】
(a) "他谁都不认识" 有两种理解：
- 理解一（他为主语/施事）："他谁都不认识" = "他（主语）不认识任何人"。此时 他 是 认识 的施事主语，谁 是宾语，作**任指**用法（"任何人/每个人"），与"都"呼应表全称量化。意为：他不认识任何人。
- 理解二（他为宾语/受事）："谁都不认识他" = "任何人不认识他 / 没人认识他"。此时 谁 是主语（任指"每个人"），他 是 认识 的受事宾语（位于句首话题位）。意为：没人认识他。

两种理解中"谁"都是**任指**（全称指代"任何人/每个人"），既不是疑问用法，也不是虚指用法。

(b) 歧义的句法/形态根源：汉语是主—动—宾固定语序且话题优先（topic-prominent）。句首的"他"处于话题位，既可作句法主语（施事）也可作被前置的语义宾语（受事），因此"他"的施/受身份不确定；同时"谁…都"这一任指全称短语可在主语或宾语槽位自由落位/约束。加之"认识"的施事与受事都是人，无选择限制阻断任一理解，且汉语缺乏形态格标记来标明"谁在认识、谁被认识"，于是产生施受反转歧义。

(c) 与"他谁都认识"相比，后者的歧义程度**相同**。因为"他谁都认识"同样有两种结构理解："他（主语）认识每个人"与"每个人都认识他"，歧义类型（施受话题反转 + 任指"谁…都"）和程度完全一致。差别只在于语用凸显度（"他谁都不认识"更倾向读成"他不认识任何人"，"他谁都认识"更倾向读成"他认识所有人"），但两种理解在结构上均可成立，歧义的有无与程度并无不同。

---

## H6

【思考】
Evaluate each of the six learner sentences for naturalness/correctness, identify error type, and give the correct form.

(1) "I'm looking forward to meet you."
- Error type: wrong non-finite form after a preposition. The phrase "look forward to" uses "to" as a PREPOSITION, not the infinitive marker, so it must be followed by a gerund (-ing), not a bare infinitive.
- Correct: "I'm looking forward to meeting you."

(2) "She suggested me to take the train."
- Error type: wrong pattern for the verb "suggest." English "suggest" does NOT take the pattern "suggest + indirect object + to-infinitive" (*suggest someone to do). The verb "suggest" takes either a that-clause (subjunctive or should) or a gerund. (The pattern "verb + obj + to-infinitive" belongs to verbs like advise, recommend, tell, etc.)
- Correct: "She suggested (that) I take the train." / "She suggested taking the train." (If the intended meaning is "advised me," one could say "She advised me to take the train.")

(3) "Despite of the rain, we went out."
- Error type: preposition redundancy. "Despite" is itself a preposition and is NOT followed by "of." (The phrase with "of" is "in spite of.")
- Correct: "Despite the rain, we went out." (or "In spite of the rain, we went out.")

(4) "He's capable to do it."
- Error type: wrong complement after adjective "capable." "Capable" is followed by the preposition "of" + gerund, not by a to-infinitive.
- Correct: "He's capable of doing it."

(5) "I would rather stay than to go."
- Error type: wrong form after "would rather ... than ..." This correlative takes BARE infinitives (without "to") on both sides; "than" must be followed by the bare infinitive "go," not "to go."
- Correct: "I would rather stay than go."

(6) "It's worth to try."
- Error type: wrong complement after "worth." The adjective "worth" is followed by a gerund (-ing) or a noun phrase, never by a to-infinitive.
- Correct: "It's worth trying." (or "It's worth a try.")

All six are erroneous; none is correct as written.

【答案】
六句均为不准确/不自然表达，逐句如下：

(1) **I'm looking forward to meet you.**  
错误类型：介词后误用不定式。"look forward to" 中的 to 是**介词**，须接动名词。  
正确：**I'm looking forward to meeting you.**

(2) **She suggested me to take the train.**  
错误类型：动词搭配错误。"suggest" 不接 "宾语 + to 不定式"（无 *suggest sb. to do 结构），应接 that 从句或动名词（"建议某人"用 advise/recommend 才可接 to 不定式）。  
正确：**She suggested (that) I take the train.** 或 **She suggested taking the train.**（若意为"劝告"，可用 **She advised me to take the train.**）

(3) **Despite of the rain, we went out.**  
错误类型：介词冗余。"despite" 本身是介词，后面**不能加 of**（带 of 的是 in spite of）。  
正确：**Despite the rain, we went out.**（或 **In spite of the rain, we went out.**）

(4) **He's capable to do it.**  
错误类型：形容词后误用不定式。"capable" 后接 "of + 动名词"，不接 to 不定式。  
正确：**He's capable of doing it.**

(5) **I would rather stay than to go.**  
错误类型：并列结构形式不一致。"would rather ... than ..." 两边都用**省略 to 的不定式（bare infinitive）**，than 后不能加 to。  
正确：**I would rather stay than go.**

(6) **It's worth to try.**  
错误类型：形容词后误用不定式。"worth" 后接**动名词或名词**，不接 to 不定式。  
正确：**It's worth trying.**（或 **It's worth a try.**）

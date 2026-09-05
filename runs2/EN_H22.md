# 高难度测试卷 — 作答（EN reasoning / ZH answer）

## H1

【思考】
- The sentence "王顾左右而言他" comes from the *Mencius* (《孟子·梁惠王下》). The full anecdote describes the king being cornered by Mencius with a series of hypothetical questions about a ruler's responsibility; when the question becomes uncomfortable, the king "顾左右而言他."
- First, determine the meaning of "他" in this context. In pre-Qin Chinese, the character "他" (often written 佗/它 originally) meant "别的、其他的" — i.e., "other / another (thing or matter)." It did NOT function as a third-person personal pronoun. The third-person pronoun system in classical Chinese used "之" for the accusative/object position and "其" for the genitive/possessive (and sometimes subject) position; there was no dedicated nominative third-person pronoun like the modern "他."
- The phrase "顾左右" means "looked at (his) left and right," where "左右" refers to the attendants standing on the king's left and right. "而言他" means "and spoke of other (matters) / changed the subject." So the whole line describes the king avoiding the difficult question by turning to his attendants and talking about something else — i.e., dodging the topic.
- Why it cannot be the modern third-person pronoun "he/him": (1) Chronologically, "他" did not acquire the meaning of a third-person personal pronoun until much later — roughly emerging in the vernacular of the Tang/Song period and only becoming standard in the early modern vernacular (e.g., 明清 novels) and finally fixed in the 20th century. In the Warring States period when *Mencius* was written, "他" uniformly meant "other." So assigning it the modern pronoun reading is an anachronism. (2) Grammatically, if "他" were a pronoun, the clause "言他" would have to mean "spoke to him" or "spoke of him," requiring an object of speech; but the established classical usage and parallel constructions (顾…而言他) show "他" is a nominal adjective meaning "other matters."
- Specific偏差 if read as third-person pronoun: The sentence would be interpreted as "The king looked left and right and spoke to/about him (some third party)," which invents a referent ("him") that does not exist in the text and, more importantly, completely loses the core pragmatic point of the anecdote — the king's evasion and subject-changing. The famous idiomatic meaning "to dodge a question by talking about something else" depends entirely on reading "他" as "other things." Misreading it as a pronoun turns a deliberate act of evasion into a trivial statement about addressing an attendant, destroying the rhetorical force of Mencius's criticism.

【答案】
(a) "他"在句中意为"别的（事/话）"，即"其他的事情/别的话题"。整句意为：大王环顾左右侍从，说起了别的事情（顾左右而言他，即避而不答、转移话题）。
(b) 不能理解为现代汉语第三人称代词"他"，因为：在先秦汉语中"他"（本字多作"佗/它"）只有"别的、其他的"之义，并无第三人称代词用法；当时第三人称代词用"之"（宾语）、"其"（定语/主语）表示，"他"作人称代词是唐以后、尤其是近代白话才出现的用法，属于时代错位。
(c) 若按"第三人称代词"理解，"言他"会变成"对他说话/说起他"，凭空多出一个文中并不存在的指称对象，并且彻底丢失了"王回避问题、转移话题"这一核心含义，使原本讽刺君王推诿的著名典故变成一句无关紧要的"大王看看左右、对他说话"，歪曲了《孟子》原意。

---

## H2

【思考】
- We must form a 7-digit number using each of the digits {1,2,3,4,5,6,7} exactly once, and count how many such numbers are divisible by 11.
- Divisibility rule for 11: A number is divisible by 11 iff the alternating sum of its digits is a multiple of 11. For a 7-digit number with digits d1 d2 d3 d4 d5 d6 d7 (d1 the leftmost/most significant), this means (d1 − d2 + d3 − d4 + d5 − d6 + d7) ≡ 0 (mod 11). Equivalently, let S_odd = sum of digits in odd positions {1,3,5,7} and S_even = sum of digits in even positions {2,4,6}; then S_odd − S_even ≡ 0 (mod 11).
- The sum of all seven digits is 1+2+3+4+5+6+7 = 28. Hence S_odd + S_even = 28.
- Substituting S_even = 28 − S_odd into the condition gives S_odd − (28 − S_odd) = 2·S_odd − 28 ≡ 0 (mod 11). So 2·S_odd ≡ 28 (mod 11). Since 28 = 2·11 + 6, we have 28 ≡ 6 (mod 11), hence 2·S_odd ≡ 6 (mod 11).
- Solve for S_odd modulo 11. The multiplicative inverse of 2 modulo 11 is 6 because 2·6 = 12 ≡ 1 (mod 11). Multiplying both sides by 6: S_odd ≡ 6·6 = 36 ≡ 3 (mod 11).
- Now determine the feasible range of S_odd. S_odd is the sum of exactly 4 distinct digits chosen from {1,…,7}. Minimum possible: 1+2+3+4 = 10. Maximum possible: 4+5+6+7 = 22. So S_odd ∈ [10, 22].
- Integers in [10,22] that are ≡ 3 (mod 11) are only 14 (since the sequence is …, 3, 14, 25, … and 25 > 22). Alternatively, directly: S_odd − S_even = 2·S_odd − 28 must be a multiple of 11, and 2·S_odd − 28 ∈ [2·10−28, 2·22−28] = [−8, 16]; the only multiple of 11 in [−8,16] is 0. So 2·S_odd − 28 = 0 ⇒ S_odd = 14. Either way, S_odd must equal 14 exactly.
- Therefore we need to choose which 4 of the 7 digits occupy the odd positions, such that they sum to 14 (the remaining 3 automatically sum to 14 as well, since 28−14=14).
- Enumerate all 4-element subsets of {1,2,3,4,5,6,7} summing to 14 (strictly increasing to avoid duplicates):
  - Starting with 1: {1,2,4,7} (1+2+4+7=14); {1,2,5,6} (1+2+5+6=14); {1,3,4,6} (1+3+4+6=14).
  - Starting with 2: {2,3,4,5} (2+3+4+5=14).
  - Starting with 3 or more: no further subsets sum to 14 (e.g., smallest with 3 is 3+4+5+6=18 > 14).
  - So there are exactly 4 such subsets: {1,2,4,7}, {1,2,5,6}, {1,3,4,6}, {2,3,4,5}.
- For each such choice, the 4 selected digits fill the 4 odd positions and can be arranged in 4! = 24 ways; the remaining 3 digits fill the 3 even positions and can be arranged in 3! = 6 ways.
- Total count = 4 (choices of subset) × 4! × 3! = 4 × 24 × 6 = 576.
- Sanity check: each listed subset's complement also sums to 14 ({3,5,6}, {3,4,7}, {2,5,7}, {1,6,7}), confirming the partition is valid; and since the alternating sum is exactly 0 (not merely ±11), every arrangement counted is genuinely divisible by 11.

【答案】
共有 **576** 个。

推导要点：被 11 整除的判别法为奇数位数字和与偶数位数字和之差是 11 的倍数。设奇数位（第1、3、5、7位）数字和为 S_odd，偶数位（第2、4、6位）和为 S_even，则 S_odd + S_even = 1+2+…+7 = 28，且 S_odd − S_even ≡ 0 (mod 11)。代入得 2·S_odd − 28 ≡ 0 (mod 11)，即 2·S_odd ≡ 6 (mod 11)，解得 S_odd ≡ 3 (mod 11)。又 S_odd 为 4 个相异数字之和，范围在 10~22 之间，该范围内唯一 ≡3(mod11) 的值为 14，故 S_odd = 14（此时差为 0）。从 {1,…,7} 中选出 4 个数和为 14 的子集恰有 4 个：{1,2,4,7}、{1,2,5,6}、{1,3,4,6}、{2,3,4,5}。每个子集选定后，奇数位 4! 排列、偶数位 3! 排列，故总数 = 4 × 4! × 3! = 4 × 24 × 6 = 576。

---

## H3

【思考】
- (a) Propositional content: Both (A) "He didn't reply" and (B) "He didn't bother to reply" assert the same literal proposition — namely, that he did not produce a reply. The truth-conditional content is identical. The difference lies in the speaker's stance/attitude. (A) is a neutral, factive report. (B) adds an evaluative layer: by using "bother to," the speaker conveys that replying would have required only minimal effort and that there was at least some expectation or reason for him to reply, yet he chose not to expend even that small effort. Thus (B) expresses the speaker's judgment that he was lazy, inconsiderate, dismissive, or negligent, whereas (A) is non-committal about such evaluation.
- (b) Presupposition of "bother to": The phrase presupposes that (i) the action (replying) was within the subject's capacity and would have involved only trivial effort, and (ii) there existed some expectation, norm, or reason that he should / might reply. In other words, "bother" presupposes that the action was easily performable and at least weakly expected. Implicature (conversational, Gricean): By saying he "didn't bother," the speaker conversationally implicates that he was deliberately neglectful, rude, or indifferent — that he could easily have replied but willfully did not, and that this reflects poorly on him. The implicature is cancellable in special contexts but is the default inference.
- (c) Why it cannot describe something the speaker thinks "shouldn't have been expected to happen": "bother to" carries the presupposition that the action was expected (or at least reasonable to expect) and easily doable. If the speaker believes a reply was never to be expected in the first place — e.g., the subject inherently cannot reply, or there is no basis for expecting a reply — then the presupposition is violated and the utterance becomes infelicitous/odd. Example: "The newborn baby didn't bother to reply to my letter." This is strange because one would never expect a newborn baby to reply; there is no presupposed expectation or ease of action, so "didn't bother to" is inappropriate. Another example: sending a message to a wrong number and saying "They didn't bother to reply" is odd, because you never expected a stranger who got a misdirected message to reply. The construction requires a backdrop of reasonable expectancy.

【答案】
(a) 两句话的**字面命题内容相同**——都断言"他没有回复"。差别在**说话人立场**：(A) 是中性事实陈述；(B) 加入 "bother to" 后，说话人表达的是"回复本只需极小的 effort、且本可期待/理应回复，他却不屑于费这点力气"，带有评价色彩（认为他懒散、怠慢、不尊重人）。
(b) **预设（presuppose）**：回复这件事在他能力范围内、只需微不足道的力气，并且存在某种（哪怕很弱的）期待或理由让他回复。**隐含（implicate）**：他刻意怠慢/无礼/漠不关心——明明轻易就能回复却故意不回，反映出他的负面态度。
(c) 因为 "bother to" 预设了"该行为是可轻易做到的、且本可被合理期待"。若说话人认为某事"本就不该期待发生"（即根本不存在这种期待、主体也无力做到），预设被破坏，句子就不自然。例："The newborn baby didn't bother to reply to my letter."（新生儿没"费心"回我的信）——荒谬，因为没人会期待婴儿回信；又如给错号码发消息后说 "They didn't bother to reply" 也不妥，因为你本就不期待陌生人回复。

---

## H4

【思考】
- There are three people A, B, C. Each is either a Knight (always tells the truth) or a Knave (always lies). Their statements:
  - A: "B is a knave."
  - B: "A and C are the same type."
  - C: "A is a knight."
- I will examine cases based on A's identity, since A's statement directly targets B and C's statement directly targets A, making A a natural pivot.
- Case 1: Suppose A is a Knight (truth-teller). Then A's statement "B is a knave" is true, so B is a Knave. Since B is a Knave, B's statement must be false. B said "A and C are the same type"; its negation means A and C are NOT the same type. A is a Knight, so C must be a Knave. Now evaluate C: C is a Knave, so C's statement must be false. C said "A is a knight." But A IS a knight, so C's statement is actually true. A knave cannot make a true statement — contradiction. Therefore Case 1 is impossible. (This also shows the sub-derivation "C = Knave" cannot hold, so the assumption A = Knight fails.)
- Case 2: Suppose A is a Knave (liar). Then A's statement "B is a knave" is false, so B is NOT a knave — i.e., B is a Knight. Since B is a Knight, B's statement is true: "A and C are the same type" is true, so A and C share the same type. A is a Knave, therefore C is also a Knave. Now check C: C is a Knave, so C's statement must be false. C said "A is a knight." Since A is in fact a Knave, the statement "A is a knight" is false — consistent with C being a Knave. No contradiction.
- Verify the full assignment A = Knave, B = Knight, C = Knave against all three statements:
  - A (knave) says "B is a knave" → false, because B is a knight. ✓ (a knave utters a falsehood)
  - B (knight) says "A and C are the same type" → A=knave, C=knave, same type → true. ✓
  - C (knave) says "A is a knight" → false, because A is a knave. ✓
- All consistent. Since A must be either Knight or Knave, and Case 1 leads to contradiction while Case 2 is fully consistent, the ONLY valid assignment is A = Knave, B = Knight, C = Knave. No other combination survives.

【答案】
A 是**无赖**，B 是**骑士**，C 是**无赖**。

完整推理（排除法）：
- 假设 A 是骑士：则 A 说真话 → "B 是无赖"为真，故 B 是无赖。B 说谎 → "A 和 C 同类"为假，即 A、C 不同类；A 是骑士，所以 C 是无赖。但 C 若为无赖，其话" A 是骑士"必须为假，而 A 实际是骑士（真），矛盾。故 A 不可能是骑士。
- 假设 A 是无赖：则 A 说谎 → "B 是无赖"为假，故 B 是骑士。B 说真话 → "A 和 C 同类"为真；A 是无赖，故 C 也是无赖。检验 C：C 是无赖，其话" A 是骑士"应为假，而 A 确为无赖（假），一致，无矛盾。
- 验证：A(无赖)说"B是无赖"为假(✓)；B(骑士)说"A、C同类"为真(✓)；C(无赖)说"A是骑士"为假(✓)。全部自洽。
因此唯一解：A=无赖，B=骑士，C=无赖。

---

## H5

【思考】
- (a) The sentence "他谁都不认识" is ambiguous between two readings:
  - Reading 1 (他 as subject, 谁 as object): "He doesn't recognize anyone" / "He knows nobody." Structurally: 他 [subject] … 认识 谁 [object]. Here "谁" is a 任指 (free/bound indefinite) used in a negative context, meaning 'anyone' — the sentence means "For all x, he does not recognize x." So "谁" functions as the object, interpreted as the universal-negative 'nobody/anyone.'
  - Reading 2 (谁 as subject, 他 as object): "Nobody recognizes him." Structurally: 谁 [subject] … 不认识 他 [object]. Here "谁" is again a 任指 indefinite meaning 'anyone/any person,' scoping over the subject position, giving "For all x, x does not recognize him" = nobody recognizes him.
  - In both readings "谁" is the 任指 (referential/generic) use of the interrogative pronoun, NOT a true question (疑问) and NOT a purely empty/vague filler (虚指). The ambiguity is in which NP is subject and which is object, not in the status of 谁.
- (b) Syntactic/morphological root of the ambiguity: Chinese lacks morphological case marking, and the sentence "他 谁 都 不 认识" places both NPs before the verb. The floating quantifier/adverb "都" (with the preceding negation "不") can associate with either preceding NP, and Chinese permits the object to appear pre-verbally (as a topic or fronted object). Consequently the surface string does not disambiguate which of 他/谁 occupies the subject θ-role and which occupies the object θ-role. The ambiguity is thus a scope/θ-role (grammatical-relation) ambiguity: 都…不 can bind 谁 while 他 is subject (Reading 1), or 都…不 can bind 谁 while 谁 itself is the subject and 他 is the object (Reading 2). The absence of case morphology and the flexibility of pre-verbal word order produce the structural ambiguity.
- (c) Compare with "他谁都认识" (affirmative). Structurally it is the same type of ambiguity: Reading 1 "He knows everyone" (他 subject, 谁 object, 都 = all); Reading 2 "Everyone knows him" (谁 subject, 他 object). So the structural ambiguity is the same in kind. The difference in degree: In the negative sentence, "谁" is a clear negative-polarity item (NPI) and must be 任指 ('anyone'), and BOTH readings ("he knows nobody" / "nobody knows him") are fully natural and equally idiomatic, so the ambiguity is robust and symmetric. In the affirmative "他谁都认识," while both readings are grammatically available, the reading with 他 as subject ("He knows everyone") is the far more salient/default interpretation, because the affirmative "都" tends to scope the object more naturally and the subject-他 reading is the unmarked one; the "everyone knows him" reading is possible but less preferred. Hence the affirmative sentence's ambiguity is marginally weaker in practice (more biased toward one reading) than the negative one, even though the underlying structural ambiguity is identical. Additionally, the negative context forces 谁 into an unambiguous NPI/任指 interpretation, whereas in affirmative contexts 谁's quantificational force is also 任指 but the two scopal assignments are less balanced.

【答案】
(a) 两种理解：
- 理解一（他为主语，谁为宾语）："他谁都不认识" = 他[主语] 不认识 任何人[宾语]，意为"他一个人都不认识 / 他不认识任何人"。此处"谁"是**任指**用法（否定语境中的"任何人"）。
- 理解二（谁为主语，他为宾语）："谁都不认识他" = 任何人[主语] 都不认识 他[宾语]，意为"没一个人认识他"。此处"谁"仍是**任指**用法（"任何人"），并非疑问、也非虚指。
(b) 歧义的句法/形态根源：汉语无形态格标记，"他 谁 都 不 认识"把两个 NP 都放在动词前；浮动副词"都"（配合"不"）可与前面任一 NP 关联，且汉语允许宾语前置/话题化，因此表层词序无法判定"他"与"谁"谁充当主语、谁充当宾语，造成**题元角色（主/宾关系）与辖域歧义**。
(c) "他谁都认识"在结构上有**同类的歧义**（"他认识所有人" vs "所有人都认识他"）。但歧义程度略有差别：否定句中"谁"是明确的否定极性词（NPI），两种理解（"他不认识任何人"/"没人认识他"）都同样自然、对称，歧义更充分；而肯定句"他谁都认识"虽结构同样歧义，但"他为主语（他认识所有人）"这一读解更占优势、为默认理解，"所有人都认识他"虽可但不那么自然，故实际歧义感略弱。根本的结构歧义类型相同，只是肯定句偏向某一读解。

---

## H6

【思考】
- (1) "I'm looking forward to meet you." — Error type: "look forward to" is a fixed phrase in which "to" is a **preposition**, not an infinitive marker. A preposition must be followed by a gerund (-ing), not a bare infinitive. Correct: "I'm looking forward to meeting you."
- (2) "She suggested me to take the train." — Error type: wrong subcategorization of the verb "suggest." "Suggest" cannot take the pattern "suggest + indirect object + infinitive" (it is not like "advise/tell/order sb to do"). Correct alternatives: "She suggested (that) I take the train" (subjunctive/indicative clause), "She suggested taking the train" (gerund), or "She suggested the train." 
- (3) "Despite of the rain, we went out." — Error type: redundant preposition. "Despite" is itself a preposition and does NOT take "of." (The "of" belongs to the synonymous phrase "in spite of.") Correct: "Despite the rain, we went out" or "In spite of the rain, we went out."
- (4) "He's capable to do it." — Error type: wrong complement of the adjective "capable." "Capable" is followed by the preposition "of" + gerund, not by a to-infinitive. Correct: "He's capable of doing it."
- (5) "I would rather stay than to go." — Error type: wrong form after "than" in the "would rather … than …" construction. Both sides take the **bare infinitive**; the "to" must be omitted. Correct: "I would rather stay than go."
- (6) "It's worth to try." — Error type: wrong complement of "worth." "Worth" (as a predicative adjective) is followed by a gerund (-ing) or a noun, never a to-infinitive. Correct: "It's worth trying" or "It's worth a try."

【答案】
(1) 错误。**错误类型**："look forward to" 中 to 是介词，须接动名词而非原形不定式。**改正**：I'm looking forward to **meeting** you.
(2) 错误。**错误类型**：suggest 不能接 "宾语 + to do" 结构（不同于 advise/tell sb to do）。**改正**：She suggested (that) I take the train. / She suggested taking the train.
(3) 错误。**错误类型**：despite 本身是介词，后面不能加 of（of 属于 in spite of）。**改正**：**Despite** the rain, we went out. 或 In spite of the rain, we went out.
(4) 错误。**错误类型**：capable 须接 "of + 动名词"，不能接 to 不定式。**改正**：He's capable **of doing** it.
(5) 错误。**错误类型**：would rather … than … 两侧都用动词原形，than 后不应有 to。**改正**：I would rather stay than **go**.
(6) 错误。**错误类型**：worth 后接动名词或名词，不接 to 不定式。**改正**：It's worth **trying**. / It's worth a try.

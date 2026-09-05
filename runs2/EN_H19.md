# 高难度测试卷作答（EN thinking / 中文答案）

## H1

【思考】
The sentence "王顾左右而言他" is recorded in the *Mencius* (《孟子·梁惠王下》). I need to determine the meaning of the word "他" in its pre-Qin context.

Step 1: In Old Chinese of the Warring States period, the graph 他 (often written 佗 or 它 in earlier texts) meant "other, else, different" — that is, "别的 / 其他的 (other things / another)". It functioned as a determinative/indefinite adjective meaning "other," not as a personal pronoun.

Step 2: Supporting evidence from classical usage. We find phrases such as "无他" (meaning "there is no other [reason]"), "他日" (another day / some other day), "他国" (another state), "他人" (other people). In all these, 他 means "other." The third-person pronoun sense of 他 (he/him/she) did not develop until much later — roughly the Wei–Jin–Northern–Southern Dynasties period, and it only became the standard third-person pronoun many centuries afterward.

Step 3: Applying this to the sentence. "王顾左右而言他" describes the king, when pressed with an uncomfortable question, turning his gaze to the attendants on his left and right and "言他" — speaking of other things, i.e., changing the subject / deflecting. So "他" here means "other matters / other topics."

Step 4: Why it cannot be the modern third-person pronoun. Reading 他 as the modern personal pronoun "he/him" is anachronistic: that grammatical function did not yet exist in Mencius's time. Assigning it a personal-pronoun role imports a category alien to the period.

Step 5: The concrete deviation if misread as third-person. If 他 meant "him," then "言他" would mean "spoke about him," which would require some third-party referent "him" in the context — but there is none. The whole point of the anecdote is that the king dodged the question by switching to unrelated topics. The pronoun reading produces a contextless, garbled sentence and completely misses the intended meaning of "deflecting to other subjects."

【答案】
(a) "他"在句中是"别的、其他的（事情）"之意，即"言他"=说别的事、转移话题。
(b) 先秦汉语中"他"（本字多作"佗/它"）义为"别的、其他的"，属于指示/不定用法，并不表示人称代词；第三人称代词"他"是后世（约魏晋南北朝以后）才逐渐产生的。因此按现代人称代词去理解是时代错置。
(c) 若理解为第三人称"他（him）"，"言他"就成了"说他"，句中却并无这样一个被言说的第三方指称对象，整句会变成无来由的废话，且完全丢失了"国君左右张望、顾而言他以回避问题"的原意。

## H2

【思考】
We form a 7-digit number using digits 1,2,3,4,5,6,7 exactly once each, and count those divisible by 11.

Step 1: Divisibility by 11 rule. A number with digits d1 d2 d3 d4 d5 d6 d7 is divisible by 11 iff the alternating sum (d1+d3+d5+d7) − (d2+d4+d6) is a multiple of 11 (…, −22, −11, 0, 11, 22, …).

Step 2: Let S_odd = d1+d3+d5+d7 (four digits, the odd positions) and S_even = d2+d4+d6 (three digits, the even positions). The total of all digits is 1+2+3+4+5+6+7 = 28, so S_odd + S_even = 28.

Step 3: The divisibility condition is S_odd − S_even = 11k for some integer k. Adding the two equations: 2·S_odd = 28 + 11k, so S_odd = (28 + 11k)/2. For S_odd to be an integer, 28+11k must be even; since 28 is even, 11k must be even, hence k must be even.

Step 4: Bounds on S_odd. It is the sum of 4 distinct digits chosen from 1..7, so its minimum is 1+2+3+4 = 10 and its maximum is 4+5+6+7 = 22. Thus 10 ≤ S_odd ≤ 22.

Step 5: Try even k values.
- k = 0: S_odd = 14, S_even = 14. Valid (within bounds).
- k = 2: S_odd = (28+22)/2 = 25 > 22. Impossible.
- k = −2: S_odd = (28−22)/2 = 3 < 10. Impossible.
Larger |k| only moves further out of range. So the ONLY possibility is S_odd = S_even = 14.

Step 6: We must partition {1,2,3,4,5,6,7} into a 3-digit subset (the even positions) summing to 14 and its 4-digit complement (the odd positions) automatically summing to 14. Enumerate the 3-digit subsets summing to 14:
- containing 7: need two distinct digits from {1..6} summing to 7 → (1,6), (2,5), (3,4) → {1,6,7}, {2,5,7}, {3,4,7}.
- containing 6 but not 7: need two distinct digits from {1..5} summing to 8 → (3,5) → {3,5,6}. (4,4) invalid.
- containing 5 but not 6,7: need sum 9 from {1..4}, max 4+3=7 < 9 → none.
So there are exactly 4 such 3-digit subsets: {1,6,7}, {2,5,7}, {3,4,7}, {3,5,6}. Each determines a unique partition (the complement is the 4-digit odd-position set).

Step 7: For each of the 4 partitions: the 3 even-position digits can be arranged in the 3 even slots in 3! = 6 ways; the 4 odd-position digits can be arranged in the 4 odd slots in 4! = 24 ways.

Step 8: Total count = 4 × 6 × 24 = 4 × 144 = 576.

【答案】
共有 **576** 个。推导：被 11 整除要求奇数位数字和与偶数位数字和之差为 11 的倍数；七位数字总和为 28，设奇数位和 S_odd、偶数位和 S_even，则 S_odd+S_even=28 且 S_odd−S_even=11k。由奇偶性得 k 必为偶数，结合 S_odd 取值范围 [10,22]，唯一可能是 k=0，即 S_odd=S_even=14。枚举可知偶数位（3 位）和为 14 的子集恰有 4 个：{1,6,7}、{2,5,7}、{3,4,7}、{3,5,6}，其补集为奇数位。每种划分下偶数位有 3! 种排法、奇数位有 4! 种排法，故总数 = 4 × 3! × 4! = 4 × 6 × 24 = 576。

## H3

【思考】
Compare (A) "He didn't reply." and (B) "He didn't bother to reply."

Step 1 (a): Literal propositional content. Both sentences have the same truth-conditional content: they both assert that he did not produce a reply. If he did reply, both are false; if he did not, both are true. So the proposition expressed is identical. The difference lies in speaker stance/attitude: (A) is neutral reportage, while (B) conveys that the speaker evaluates his non-reply negatively — that replying would have been easy or expected, yet he chose not to expend the (minimal) effort. (B) implies criticism, dismissiveness, or that he was negligent/rude.

Step 2 (b): Presupposition vs. implicature of "bother to." The phrase "bother to V" presupposes that V was an action that was feasible, of low cost, and at least minimally expected or appropriate for the agent to perform — i.e., it presupposes a norm or expectation that the agent should / could easily do V. It also presupposes the agent had the capacity and the opportunity. The conversational implicature (via the choice of this frame) is that the agent was at fault: he was inconsiderate, lazy, or deliberately dismissive, because doing V would have been the ordinary, easy thing and he failed even that. So (B) implicates "he showed disregard / was neglectful."

Step 3 (c): Why it cannot describe something the speaker thinks was not to be expected. "Didn't bother to V" is infelicitous when V is not something the agent was expected or able to do, because the construction presupposes that V was a reasonable, low-effort, expectable action. Example: "The statue didn't bother to reply." A statue cannot reply and no one expects it to, so saying it "didn't bother" is nonsensical — it falsely presupposes an expectation and capacity. Similarly, "He didn't bother to fly to the moon" is odd because flying to the moon is not an expectable, easy action. Closer to the reply case: if a complete stranger who was never addressed receives no reply, saying "The random passerby didn't bother to reply to my letter" is odd, because a passerby is not someone expected to reply; one would simply say "He didn't reply." The construction imposes an expectation that, in the speaker's view, should not hold.

【答案】
(a) 两句话的字面命题内容相同：都断言"他没有回复"。差别在说话人立场：(A) 是中性陈述；(B) 带有负面评价，暗示回复本应轻易做到或被期待，他却连这点力气都不肯费，含批评、怠慢之意。
(b) "bother to" 预设（presuppose）了"回复"是一件可行、成本低、且说话人认为当事人本应/本可轻易去做的事（即存在一种应做/可做的规范期待）；它蕴含（implicate）了当事人有过失——轻率、冷漠或故意怠慢。
(c) "didn't bother to V" 预设 V 是一件理应被期待、轻而易举的事，因此不能用来描述说话人认为"本就不该期待发生"的事。例如 "The statue didn't bother to reply."（雕像不会也不能回复，无人期待它回复）就荒谬；又如对一个本就无关、无人期待其回复的陌生人说 "The random passerby didn't bother to reply to my letter." 也不自然，此时应只说 "He didn't reply."。

## H4

【思考】
Three people A, B, C; each is either a Knight (always truthful) or a Knave (always lies).
- A says: "B is a knave."
- B says: "A and C are of the same type."
- C says: "A is a knight."

Step 1: Consider the two possibilities for A.

Case 1: A is a Knight. Then A's statement is true, so "B is a knave" is true → B = Knave. Since B is a knave, B's statement "A and C are the same type" must be false. With A = Knight, "A and C same type" being false means C ≠ A, so C = Knave. Now C is a knave, so C's statement "A is a knight" must be false. But A is a Knight, so "A is a knight" is TRUE — a knave cannot utter a true statement. Contradiction. Therefore Case 1 is impossible.

Case 2: A is a Knave. Then A's statement "B is a knave" is false, so B is NOT a knave → B = Knight. Since B is a knight, B's statement "A and C are the same type" is true. With A = Knave, C must be the same type as A → C = Knave. Now C is a knave, so C's statement "A is a knight" must be false. A is indeed a Knave, so "A is a knight" is false — consistent with C lying. No contradiction.

Step 2: Verify the full assignment A=Knave, B=Knight, C=Knave:
- A (knave) says "B is a knave": B is a knight, so the statement is false → correct for a knave. ✓
- B (knight) says "A and C are the same type": A=knave, C=knave, same → true → correct for a knight. ✓
- C (knave) says "A is a knight": A is a knave, so false → correct for a knave. ✓

Step 3: Exhaustiveness. The only two cases for A are Knight or Knave. Case A=Knight leads to a contradiction, so it is eliminated. This forces A=Knave, which uniquely determines B=Knight (from A's false claim) and C=Knave (from B's true claim). Hence the solution is unique; no other assignment is possible.

【答案】
A 是无赖（Knave），B 是骑士（Knight），C 是无赖（Knave）。
推理：先假设 A 是骑士，则 A 说真话→B 是无赖；B 说谎→"A 与 C 同类"为假→因 A 是骑士故 C 必为无赖；但 C 作为无赖必须说假话，而 C 说"A 是骑士"此时为真，矛盾，故 A 不可能是骑士。因此 A 必为无赖：A 说谎→"B 是无赖"为假→B 是骑士；B 说真话→"A 与 C 同类"为真→C 与 A 同为无赖；C 说谎→"A 是骑士"为假，与 A 是无赖一致。三句均自洽，且 A 两种身份中仅"无赖"可行，故分配唯一。

## H5

【思考】
The sentence "他谁都不认识" is ambiguous. The word 谁 is a universal/free indefinite (任指) meaning "anyone / everyone," and 都 is a distributive universal quantifier; the negation 不 scopes over the verb 认识 ("to know").

Step 1 (a): Two parses.
- Parse 1 (他 = subject / experiencer): 他 [谁都 [不认识 t]] — "He doesn't know anyone" (He knows nobody). Here 他 is the knower (subject), 谁都 is the object meaning "anyone," and with negation it yields universal negation: for every person x, he does not know x.
- Parse 2 (他 = object / theme, fronted as topic): [他_i [谁都 [不认识 t_i]]] — "No one knows him." Here 他 is the object, 谁都 is the subject meaning "everyone," and 不 gives "everyone does not know him" = "no one knows him."
In both readings 谁 is 任指 (a universal/bound indefinite licensed by 都), not 虚指 (vague reference such as "someone") and not an interrogative.

Step 2 (b): Root of ambiguity. 认识 is a transitive verb whose subject is the knower and object the known. Chinese permits a sentence-initial NP to be either the subject or a fronted object (topicalization). Because 谁都 can function as either the object (when 他 is subject) or the subject (when 他 is the fronted object), the initial 他 is structurally ambiguous between experiencer-subject and theme-object. The ambiguity is syntactic/structural: it arises from theta-role assignment and constituent structure, compounded by the fact that 他, as a third-person pronoun with no case marking, cannot disambiguate its grammatical relation.

Step 3 (c): Compare "他谁都认识" (affirmative). It also has two readings: "He knows everyone" (他 subject) and "Everyone knows him" (他 object). So the same kind of ambiguity exists, and 谁 is 任指 in all cases. However, the degree is not perfectly identical. In the negative sentence, the two readings are both available but the "他 knows no one" reading is more salient/default, because 不 naturally scopes over the object 谁 and 谁都不 is a canonical negative universal ("nobody"). In the affirmative, 谁都 means "everyone," and the two readings are more evenly balanced, with the object reading "everyone knows him" fully natural. The asymmetry comes from how negation interacts with the universal quantifier 都/谁: the negative 谁都不 is a fixed negative-polarity universal, which slightly biases but does not eliminate the object reading. Thus both sentences are ambiguous, but the negative one shows a stronger preference for the subject reading.

【答案】
(a) 两种理解：① 他作主语（认知者）："他谁都不认识"="他任何人都不认识"→"他谁也不认识 / 他一个也不认识"（He doesn't know anyone）。② 他作宾语（被知者，话题化前置）："（对于）他，谁都不认识"→"没人认识他"（No one knows him）。两种理解中"谁"都是任指（受"都"约束的周遍性不定代词），既非虚指也非疑问。
(b) 歧义根源是句法/论元结构的：动词"认识"主语为知者、宾语为被知者；汉语允许句首 NP 既作主语，也可作前置的话题化宾语。由于"谁都"既可作宾语（他为主语时）也可作主语（他为前置宾语时），句首的"他"在"知者"与"被知者"两种题元角色间歧义；且"他"作为无格标记的人称代词，无法靠形态消歧。
(c) "他谁都认识"同样有歧义（"他认识所有人"与"所有人都认识他"），"谁"亦为任指，歧义类型相同。但程度不完全一致：否定句中"他谁都不认识"的"他为主语（他不认识任何人）"解读更占优势/更自然，因为"不"自然统辖宾语"谁"，且"谁都不"是固定的否定周遍式（"没人"）；而肯定句"谁都"表"所有人"，两种解读更均衡。差别源自否定词与周遍量词"都/谁"的互动：否定式"谁都不"作为负极性周遍式略偏向主语解读，但并不消除宾语解读。

## H6

【思考】
Six learner sentences; judge each.

(1) "I'm looking forward to meet you." Error: "look forward to" uses "to" as a preposition, so it requires a gerund, not a bare infinitive. Correct: "I'm looking forward to meeting you."

(2) "She suggested me to take the train." Error: "suggest" does not take an indirect object + infinitive complement. The verb pattern is "suggest (that) someone do something" (subjunctive) or "suggest doing something" / "suggest one's doing something." Correct: "She suggested (that) I take the train" or "She suggested my taking the train."

(3) "Despite of the rain, we went out." Error: "despite" is itself a preposition and is NOT followed by "of." (The phrase with "of" is "in spite of.") Correct: "Despite the rain, we went out" or "In spite of the rain, we went out."

(4) "He's capable to do it." Error: the adjective "capable" is followed by the preposition "of" + gerund, not by a bare infinitive. Correct: "He's capable of doing it."

(5) "I would rather stay than to go." Error: after the correlative "rather … than …," the base (bare infinitive) form is required on both sides; "to" before "go" is ungrammatical. Correct: "I would rather stay than go."

(6) "It's worth to try." Error: the adjective "worth" is followed by a gerund (or a noun phrase), not by a bare infinitive. Correct: "It's worth trying" (or "It's worth a try").

【答案】
(1) 错误（介词后接动名词）。"look forward to" 中 to 是介词，应接动名词。正确：*I'm looking forward to meeting you.*
(2) 错误（suggest 不能接"间接宾语 + 不定式"）。正确：*She suggested (that) I take the train.* 或 *She suggested my taking the train.*
(3) 错误（despite 本身即是介词，不接 of；带 of 的是 in spite of）。正确：*Despite the rain, we went out.* 或 *In spite of the rain, we went out.*
(4) 错误（capable 后接 of + 动名词）。正确：*He's capable of doing it.*
(5) 错误（rather … than … 后接动词原形，不可加 to）。正确：*I would rather stay than go.*
(6) 错误（worth 后接动名词或名词，不接不定式）。正确：*It's worth trying.* 或 *It's worth a try.*

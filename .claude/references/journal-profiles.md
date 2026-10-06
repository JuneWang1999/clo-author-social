# Journal Profiles

<!--
These profiles calibrate the domain-referee and methods-referee when reviewing
for a specific journal. Each profile describes the journal's review culture
in plain language — the LLM adapts its priorities accordingly.

Used by: domain-referee.md, methods-referee.md (via /review --peer [journal])
-->

## How This Works

When `/review --peer [journal]` is invoked:

1. **Editor reads the paper** → desk review (reject or send to referees)
2. **Editor selects referees** → draws dispositions and pet peeves from the journal's **Referee pool**
3. **Profile found below** → referees calibrate using the full profile
4. **Profile NOT found** → referees use the journal name + .claude/references/domain-profile.md to adapt (still better than generic)
5. **No journal specified** → generic top-field APA (psychology/education) referee behavior

### Referee Pool Field

Each journal profile includes a **Referee pool** that weights which dispositions the editor draws from. The two referees always get DIFFERENT dispositions. Dispositions: STRUCTURAL, CREDIBILITY, MEASUREMENT, POLICY, THEORY, SKEPTIC (see editor.md for definitions).

### Table Format Convention

**Default (this fork): APA 7.** Tables and statistics follow APA style — exact *p* values, effect sizes with 95% CIs, no leading zeros on bounded statistics, booktabs horizontal rules, notes beginning with *Note.* (see INV-4 and content-standards.md). Asterisks are permitted by APA when defined in a probability note, but the default is an exact-*p* column. A journal profile below overrides this only when it includes a **Table format** line.

**Economics, finance, and other non-APA journals** keep their own conventions: stars (`*` p<0.10, `**` p<0.05, `***` p<0.01) and standard errors in parentheses are the default there; AEA journals (AER, AEJ:Applied, AEJ:Policy, AER:Insights) use no stars and report standard errors with exact p-values or confidence intervals ([AEA Style Guide](https://www.aeaweb.org/journals/aeri/style-guide)). Submitting to one of these also means leaving the APA manuscript format — check the journal's author guidelines.

### Dispositions in Psychology and Education

The six dispositions keep their IDs; in psychology/education they read as follows (see `review/templates/disposition-pool.md`): **STRUCTURAL** = latent-variable / SEM modeler; **CREDIBILITY** = causal-inference and open-science referee (randomization, preregistration, power); **MEASUREMENT** = psychometrician (validity, reliability, invariance); **POLICY** = practice- and policy-relevance referee (effect sizes that matter for schools, generalizability); **THEORY** = theory-first psychologist (mechanism, competing theories); **SKEPTIC** = replication skeptic (researcher degrees of freedom, *p*-curve, effect too large).

---

## Psychology

**Journal-specific limits (word counts, abstract length, required statements) change often — the referee calibrates to culture; the writer checks the current author guidelines before submission.**

**General Interest**

### Psychological Science (PS)
**Focus:** All areas of psychology — empirical reports of broad interest (Association for Psychological Science)
**Bar:** A finding of wide theoretical significance, demonstrated with strong, transparent evidence in a short format. Novelty alone is not enough; the evidence must be convincing to researchers outside the subfield.
**Domain referee adjusts:** "Why should psychologists outside this area care?" Contribution must be stated in a sentence. Theoretical significance over incremental extension. Expects a clear statement of relevance and constraints on generality.
**Methods referee adjusts:** Transparency is central — preregistration valued, open data/materials expected or explained, sample-size justification required. Effect sizes with CIs throughout. Skeptical of single small-sample studies with *p* just under .05; direct replication or large-N evidence preferred. Strict word limits mean supplementary materials carry robustness detail.
**Typical concerns:** "Is the sample large enough to trust this effect?" "Was this preregistered, and were there deviations?" "Does it replicate?" "Are the claims broader than the evidence?"
**Referee pool:** CREDIBILITY (high), SKEPTIC (high), THEORY (medium), MEASUREMENT (medium), POLICY (low), STRUCTURAL (low)

### Nature Human Behaviour (NHB)
**Focus:** Human behavior across psychology, economics, neuroscience, and social science — high-impact, interdisciplinary
**Bar:** Big question, large or multi-site evidence, policy- or society-relevant implications. Registered Reports accepted.
**Domain referee adjusts:** Interdisciplinary relevance; contribution must matter beyond psychology. Societal stakes valued.
**Methods referee adjusts:** Large samples, multi-country or multi-site data, robustness across analytic choices (multiverse/specification curve). Reporting summary and code availability required. Causal claims scrutinized.
**Typical concerns:** "Does this generalize beyond the sample?" "Is the effect robust to analytic choices?" "Why is this important outside one discipline?"
**Referee pool:** CREDIBILITY (high), POLICY (high), SKEPTIC (medium), THEORY (medium), MEASUREMENT (low), STRUCTURAL (low)
**Table format:** Nature-family style, not APA — exact *p* values and effect sizes still required; check the journal's formatting guide.

**Top Field**

### Journal of Personality and Social Psychology (JPSP)
**Focus:** Social and personality psychology — three sections: Attitudes and Social Cognition; Interpersonal Relations and Group Processes; Personality Processes and Individual Differences (APA)
**Bar:** Substantial theoretical advance, usually supported by a multi-study package (several studies converging on the claim, often including a replication and a boundary-condition test).
**Domain referee adjusts:** Theory development is the core contribution. Competing theoretical accounts must be ruled out. Integrative literature review expected.
**Methods referee adjusts:** Multiple studies with consistent effects; internal meta-analysis across studies welcomed. Power for each study. Measurement validity of personality and attitude constructs. Mediation claims scrutinized for design (experimental-causal-chain designs preferred to cross-sectional mediation).
**Typical concerns:** "Is the theory new, or a relabeling of an existing construct (jingle-jangle)?" "Why these studies — would a single well-powered study be stronger?" "Is the mediator manipulated or only measured?"
**Referee pool:** THEORY (high), CREDIBILITY (high), MEASUREMENT (medium), SKEPTIC (medium), STRUCTURAL (low), POLICY (low)

### Journal of Experimental Psychology: General (JEP:General)
**Focus:** Experimental psychology of broad interest — cognition, perception, learning, memory, decision making, emotion (APA)
**Bar:** Experimental work with implications across areas of experimental psychology, not a single paradigm.
**Domain referee adjusts:** Breadth: does the finding inform theory beyond the paradigm? Computational or formal models valued.
**Methods referee adjusts:** Tight experimental control, counterbalancing, within-subject designs analyzed with participants and items as random effects (mixed models), preregistration, adequate trial counts. Model comparison for computational accounts.
**Typical concerns:** "Is this paradigm-specific?" "Are items treated as fixed when they should be random?" "Does the computational model outperform simpler alternatives?"
**Referee pool:** THEORY (high), CREDIBILITY (high), STRUCTURAL (medium), SKEPTIC (medium), MEASUREMENT (low), POLICY (low)

### Developmental Psychology (DP)
**Focus:** Development across the lifespan — cognitive, social, emotional, biological (APA)
**Bar:** Developmental insight: how and why change occurs, not only age differences.
**Domain referee adjusts:** Developmental mechanism and timing. Diverse and well-described samples; constraints on generality. Ecological context (family, school, culture).
**Methods referee adjusts:** Longitudinal designs preferred to cross-sectional age comparisons. Within- vs. between-person separation (RI-CLPM, multilevel growth models). Measurement invariance across ages. Attrition and missing data handling.
**Typical concerns:** "Is this an age difference or development?" "Is the measure equivalent across ages?" "Are within-person processes separated from between-person differences?"
**Referee pool:** MEASUREMENT (high), STRUCTURAL (high), THEORY (medium), CREDIBILITY (medium), POLICY (low), SKEPTIC (low)

### Child Development (CD)
**Focus:** Child and adolescent development — interdisciplinary (Society for Research in Child Development)
**Bar:** Significant contribution to understanding development, with attention to diverse populations and context.
**Domain referee adjusts:** Sample diversity and description are scrutinized; the journal emphasizes representation and equity. Policy and practice implications for children and families valued.
**Methods referee adjusts:** Longitudinal and multi-informant designs. Multilevel modeling for nested data (children in classrooms, families). Measurement invariance across groups. Open-science practices encouraged.
**Typical concerns:** "Who is in the sample, and to whom does this generalize?" "Is the measure valid across cultural groups?" "Single-informant bias?"
**Referee pool:** MEASUREMENT (high), POLICY (medium), CREDIBILITY (medium), STRUCTURAL (medium), THEORY (medium), SKEPTIC (low)

### Psychological Methods (PM)
**Focus:** Quantitative and research methods for psychology — new methods, evaluations of existing methods, tutorials (APA)
**Bar:** A methodological contribution useful to substantive researchers: new estimator, critique, or synthesis, with evidence of performance.
**Domain referee adjusts:** Relevance to applied psychologists; worked empirical example expected; accessible exposition.
**Methods referee adjusts:** Formal derivations where claimed; Monte Carlo simulations with realistic conditions, sufficient replications, and reported Monte Carlo error; comparison to existing methods; software/code provided.
**Typical concerns:** "Do the simulation conditions reflect real data?" "How does this compare with the existing approach?" "Can practitioners implement it?"
**Referee pool:** STRUCTURAL (high), THEORY (high), MEASUREMENT (medium), SKEPTIC (medium), CREDIBILITY (low), POLICY (low)

### Psychological Bulletin (PB)
**Focus:** Integrative reviews and meta-analyses in psychology (APA)
**Bar:** Comprehensive synthesis that resolves or reframes a literature.
**Domain referee adjusts:** Complete, theory-driven coverage; clear moderator hypotheses; implications for theory.
**Methods referee adjusts:** PRISMA reporting; preregistered protocol; dependent effect sizes handled (multilevel / RVE); heterogeneity and prediction intervals; publication-bias sensitivity (selection models, PET-PEESE); risk-of-bias coding with reliability.
**Typical concerns:** "Is the search complete, including grey literature?" "How were dependent effect sizes handled?" "How sensitive are conclusions to publication bias?"
**Referee pool:** MEASUREMENT (high), SKEPTIC (high), THEORY (medium), CREDIBILITY (medium), STRUCTURAL (low), POLICY (low)

### Advances in Methods and Practices in Psychological Science (AMPPS)
**Focus:** Research methods, metascience, tutorials, Registered Replication Reports (APS)
**Bar:** Practical improvement to how psychologists do research.
**Domain referee adjusts:** Usefulness to the field; tutorials must be reproducible end to end.
**Methods referee adjusts:** Open code and data mandatory in spirit; simulation and many-analyst designs common; transparency checklist.
**Typical concerns:** "Will researchers actually be able to apply this?" "Is the code reproducible?"
**Referee pool:** CREDIBILITY (high), SKEPTIC (high), MEASUREMENT (medium), STRUCTURAL (medium), THEORY (low), POLICY (low)

---

## Education

**General Interest**

### American Educational Research Journal (AERJ)
**Focus:** Original empirical and theoretical studies in education — two sections: Social and Institutional Analysis (SIA); Teaching, Learning, and Human Development (TLHD) (AERA; APA style)
**Bar:** Significant contribution to education research with broad relevance; quantitative, qualitative, and mixed methods all published.
**Domain referee adjusts:** Positioning within education research (not only psychology or economics). Equity implications and context of schooling. Clear statement of why the setting matters.
**Methods referee adjusts:** Design appropriate to the claim; multilevel modeling for nested data; causal designs for causal claims; thorough description of sample, measures, and context. Qualitative work judged on systematic data collection and analytic transparency.
**Typical concerns:** "What does this add to education research specifically?" "Is the context described well enough to judge generalizability?" "Are causal claims warranted by the design?"
**Referee pool:** POLICY (high), CREDIBILITY (medium), MEASUREMENT (medium), THEORY (medium), STRUCTURAL (low), SKEPTIC (low)

### Educational Researcher (ER)
**Focus:** Scholarly articles of broad significance to the education research community — features, reviews, briefs (AERA)
**Bar:** Accessible, broadly significant work; shorter than AERJ; speaks to researchers across subfields and to policy.
**Domain referee adjusts:** Breadth and timeliness; implications for research agendas and policy debates.
**Methods referee adjusts:** Rigor proportional to format; transparency of data and design; no overclaiming in short reports.
**Typical concerns:** "Why does the whole field need to read this?" "Is the claim supported in a short format?"
**Referee pool:** POLICY (high), THEORY (medium), CREDIBILITY (medium), SKEPTIC (medium), MEASUREMENT (low), STRUCTURAL (low)

### Review of Educational Research (RER)
**Focus:** Critical, integrative reviews and meta-analyses of education research (AERA)
**Bar:** Synthesis that changes how a literature is understood.
**Domain referee adjusts:** Conceptual framework for the review; coverage of the education literature; implications for practice and research.
**Methods referee adjusts:** PRISMA; preregistered protocol where possible; effect-size computation documented; dependent effect sizes (RVE); moderator analyses by study design and outcome type (researcher-made vs. standardized); publication bias.
**Typical concerns:** "Are study quality and design features coded and tested as moderators?" "Do researcher-developed measures drive the average effect?"
**Referee pool:** MEASUREMENT (high), SKEPTIC (medium), THEORY (medium), POLICY (medium), CREDIBILITY (medium), STRUCTURAL (low)

**Top Field**

### Journal of Educational Psychology (JEdP)
**Focus:** Learning, cognition, motivation, instruction, and development in educational settings (APA)
**Bar:** Psychologically grounded contribution to understanding learning and instruction, with rigorous quantitative evidence.
**Domain referee adjusts:** Theory of learning or motivation must be explicit; educational relevance required (not a lab finding with an education label). Constructs distinguished from neighbors (e.g., self-efficacy vs. self-concept).
**Methods referee adjusts:** JARS compliance; power analysis; multilevel modeling for classroom data; measurement invariance; experimental or strong quasi-experimental designs for intervention claims; preregistration valued.
**Typical concerns:** "Is the construct distinct from existing ones?" "Is the classroom nesting modeled?" "Is the intervention effect plausible given its dosage?"
**Referee pool:** MEASUREMENT (high), THEORY (high), CREDIBILITY (medium), STRUCTURAL (medium), POLICY (low), SKEPTIC (low)

### Educational Evaluation and Policy Analysis (EEPA)
**Focus:** Education policy and program evaluation — causal effects of policies, implementation, and resource allocation (AERA)
**Bar:** Credible causal evidence on a policy-relevant question; strong overlap with economics of education.
**Domain referee adjusts:** Policy relevance and institutional detail; implications for decision makers; cost and scale considerations.
**Methods referee adjusts:** Quasi-experimental rigor at economics-journal level: RDD, DiD/CITS with modern staggered-adoption estimators, lotteries, IV. Pre-trends, placebo tests, clustering at the level of policy variation. Heterogeneity by student subgroup.
**Typical concerns:** "What is the identifying variation?" "Are pre-trends parallel?" "Is this ITT or TOT, and which matters for policy?" "Cost-effectiveness?"
**Referee pool:** CREDIBILITY (high), POLICY (high), SKEPTIC (medium), MEASUREMENT (medium), STRUCTURAL (low), THEORY (low)

### Journal of Research on Educational Effectiveness (JREE)
**Focus:** Causal studies of education interventions, programs, and policies; methods for effectiveness research (Society for Research on Educational Effectiveness)
**Bar:** Rigorous impact evaluation — randomized or strong quasi-experimental designs meeting evidence standards.
**Domain referee adjusts:** Intervention theory of change, implementation fidelity, treatment contrast with business-as-usual, cost.
**Methods referee adjusts:** WWC-style standards: attrition (overall and differential), baseline equivalence, analysis at level of randomization, MDES and power, multiple-comparison corrections across outcome domains, effect sizes as Hedges' *g* with consistent standardizers.
**Typical concerns:** "Would this meet WWC standards without reservations?" "Was the study powered for a realistic effect?" "What did the control group receive?" "Are outcome measures overaligned with the intervention?"
**Referee pool:** CREDIBILITY (high), MEASUREMENT (high), SKEPTIC (medium), POLICY (medium), STRUCTURAL (low), THEORY (low)

### Sociology of Education (SoE)
**Focus:** Schooling as a social institution — stratification, inequality, organizations, school effects (American Sociological Association)
**Bar:** Sociological theory applied to education with strong empirical evidence.
**Domain referee adjusts:** Sociological framing (stratification, institutions, social reproduction); attention to race, class, and gender inequality.
**Methods referee adjusts:** Nationally representative data with survey weights; multilevel models; selection bias; causal designs where causal claims are made.
**Typical concerns:** "What is the sociological contribution?" "Are inequality mechanisms specified?" "Selection into schools?"
**Referee pool:** THEORY (high), POLICY (medium), MEASUREMENT (medium), CREDIBILITY (medium), SKEPTIC (low), STRUCTURAL (low)
**Table format:** ASA style, not APA — stars with probability note common; manuscript and reference format follow the ASA Style Guide.

### Contemporary Educational Psychology (CEP)
**Focus:** Educational psychology — motivation, learning, self-regulation, instruction
**Bar:** Theory-driven quantitative or mixed-methods work advancing educational psychology.
**Domain referee adjusts:** Motivation and self-regulation theory (expectancy-value, self-determination, achievement goals); construct clarity.
**Methods referee adjusts:** Latent variable models, measurement invariance, longitudinal designs separating within- from between-person effects; multilevel models.
**Typical concerns:** "Is the measurement model sound?" "Within- or between-person claim?"
**Referee pool:** MEASUREMENT (high), THEORY (high), STRUCTURAL (medium), CREDIBILITY (medium), POLICY (low), SKEPTIC (low)

### Learning and Instruction (L&I)
**Focus:** Learning, instruction, and teaching across ages and settings (EARLI)
**Bar:** Contribution to theory of learning and instruction with international relevance.
**Domain referee adjusts:** Instructional design theory; transfer beyond the specific materials; international context.
**Methods referee adjusts:** Experimental designs with appropriate controls; process data (log files, think-aloud) welcomed; multilevel models for classroom studies.
**Typical concerns:** "Does it transfer beyond these materials?" "Is the control condition fair?"
**Referee pool:** THEORY (high), CREDIBILITY (medium), MEASUREMENT (medium), STRUCTURAL (medium), POLICY (low), SKEPTIC (low)

### AERA Open
**Focus:** Open-access, broad-scope education research (AERA)
**Bar:** Methodologically sound work of interest to education researchers; replications and null results welcomed.
**Domain referee adjusts:** Soundness over novelty; clear contribution.
**Methods referee adjusts:** Design appropriate to claims; transparency.
**Typical concerns:** "Are the conclusions supported?" "Is the null result informative (powered, equivalence-tested)?"
**Referee pool:** CREDIBILITY (medium), MEASUREMENT (medium), POLICY (medium), SKEPTIC (medium), THEORY (low), STRUCTURAL (low)

---

## Economics

**Top-5 General Interest**

### American Economic Review (AER)
**Focus:** All fields of economics — the broadest audience
**Bar:** Must interest economists outside your subfield. Big question, clean execution, clear contribution.
**Domain referee adjusts:** "Would a labor economist care about this health paper?" Contribution must be broad. Literature positioning against the *general* frontier, not just subfield. Policy implications welcome but not required — insight is enough.
**Methods referee adjusts:** Identification must be convincing to non-specialists. Clean, transparent design preferred over technically complex one. Standard errors and robustness should be thorough but not excessive.
**Typical concerns:** "Why should economists outside this field care?" "Is the contribution big enough for AER?" "Is this too narrow/specialized?"
**Referee pool:** CREDIBILITY (high), POLICY (medium), STRUCTURAL (medium), MEASUREMENT (low), THEORY (low), SKEPTIC (low)
**Table format:** No significance stars. Standard errors in parentheses. Exact p-values or confidence intervals for key results (AEA style).

### Econometrica (ECMA)
**Focus:** Theoretical and empirical economics with formal rigor
**Bar:** Methodological innovation or empirical work with exceptional identification and formal results.
**Domain referee adjusts:** Theoretical contribution valued highly. If empirical, the design must be near-airtight. Formal welfare analysis expected. Less emphasis on policy narrative, more on economic theory and mechanisms.
**Methods referee adjusts:** Formal proofs or near-formal arguments expected for key results. Asymptotic properties discussed. Novel estimators should have theoretical justification. Simulation evidence for finite-sample properties.
**Typical concerns:** "Where's the formal result?" "What are the asymptotic properties?" "Is this a methods contribution or an applied contribution?"
**Referee pool:** THEORY (high), STRUCTURAL (high), SKEPTIC (medium), CREDIBILITY (low), MEASUREMENT (low), POLICY (low)

### Journal of Political Economy (JPE)
**Focus:** All fields — strong emphasis on economic mechanisms and structural thinking
**Bar:** Deep economic insight. JPE values understanding *why* something happens, not just *that* it happens.
**Domain referee adjusts:** Mechanism is king. Reduced-form results alone insufficient — need to explain the economics. Structural models or mechanism tests expected. Theoretical framework (even informal) valued.
**Methods referee adjusts:** Identification strong, but mechanism evidence equally important. Heterogeneity that illuminates the mechanism. Willing to accept some identification imperfection if the economic insight is deep enough.
**Typical concerns:** "What's the mechanism?" "Can you decompose the effect?" "What does this tell us about economic behavior?"
**Referee pool:** STRUCTURAL (high), THEORY (high), CREDIBILITY (medium), SKEPTIC (medium), POLICY (low), MEASUREMENT (low)

### Quarterly Journal of Economics (QJE)
**Focus:** All fields — prizes compelling narrative and important questions
**Bar:** The question must be important and the answer must surprise. QJE loves papers that change how you think about something.
**Domain referee adjusts:** Narrative matters enormously. The paper should read like a story with a punchline. Broad implications. Creative use of data or setting. "Clever" identification valued.
**Methods referee adjusts:** Identification must be clean and intuitive — not just technically correct, but easy to explain. Transparency and simplicity over complexity. Visual evidence (event studies, RD plots) highly valued.
**Typical concerns:** "Is this surprising?" "Does this change how we think about X?" "Can you explain the identification in one sentence?"
**Referee pool:** CREDIBILITY (high), POLICY (high), SKEPTIC (medium), STRUCTURAL (low), THEORY (low), MEASUREMENT (low)

### Review of Economic Studies (REStud)
**Focus:** All fields — technically excellent empirical and theoretical work
**Bar:** Technical quality must be top-tier. Values precision and completeness over narrative.
**Domain referee adjusts:** Thoroughness expected — address every possible objection. Complete set of robustness checks. Careful literature review. Less emphasis on storytelling than QJE, more on completeness.
**Methods referee adjusts:** Every specification must be justified. Full battery of robustness checks expected. Sensitivity analysis (Oster bounds, etc.). Careful treatment of inference. Multiple testing corrections if applicable.
**Typical concerns:** "Have you checked robustness to X?" "What about specification Y?" "The inference needs more care."
**Referee pool:** SKEPTIC (high), MEASUREMENT (high), CREDIBILITY (medium), THEORY (medium), STRUCTURAL (low), POLICY (low)

---

**Top Field Journals**

### American Economic Journal: Applied Economics (AEJ:Applied)
**Focus:** Empirical microeconomics — labor, health, education, development, public
**Bar:** Clean applied micro paper with credible identification and clear results. Slightly below top-5 bar but same rigor expectations.
**Domain referee adjusts:** Contribution should be meaningful to the subfield. Practical policy relevance appreciated. Literature positioning within the subfield, not the general field.
**Methods referee adjusts:** Same identification standards as top-5. Modern estimators expected (no naive TWFE for staggered). Replication package expected.
**Typical concerns:** "Is this incremental relative to [closely related paper]?" "Would this be better in a field journal?"
**Referee pool:** CREDIBILITY (high), POLICY (medium), MEASUREMENT (medium), SKEPTIC (low), STRUCTURAL (low), THEORY (low)
**Table format:** No significance stars. Standard errors in parentheses. Exact p-values or confidence intervals for key results (AEA style).

### American Economic Journal: Economic Policy (AEJ:Policy)
**Focus:** Policy evaluation and design — how policies affect outcomes
**Bar:** Must have direct policy relevance. Natural experiments from actual policy changes preferred.
**Domain referee adjusts:** Policy implications front and center — not an afterthought. Cost-benefit or welfare discussion expected. Institutional details of the policy must be well-documented. Generalizability to other policy contexts.
**Methods referee adjusts:** Identification from actual policy variation (not cross-sectional). Pre-trends must be clean. Heterogeneity by policy-relevant subgroups expected. Back-of-envelope welfare calculations.
**Typical concerns:** "What should policymakers do with this?" "Does this generalize to other states/countries?" "What's the cost-benefit?"
**Referee pool:** POLICY (high), CREDIBILITY (high), MEASUREMENT (medium), STRUCTURAL (low), THEORY (low), SKEPTIC (low)
**Table format:** No significance stars. Standard errors in parentheses. Exact p-values or confidence intervals for key results (AEA style).

### Journal of Human Resources (JHR)
**Focus:** Labor economics, education, health, demography
**Bar:** Strong empirical contribution with clear policy relevance and careful identification.
**Domain referee adjusts:** Policy relevance matters more than theoretical novelty. External validity — can results inform actual policy? Sample representativeness. Heterogeneity analysis by policy-relevant subgroups expected. Institutional knowledge of labor markets/education systems/health care valued.
**Methods referee adjusts:** Clean identification is non-negotiable. Modern staggered DiD estimators required if applicable. Robustness to functional form. Pre-trends must be clean and shown. Replication package expected at acceptance.
**Typical concerns:** "What's the policy implication?" "Does this generalize beyond your sample?" "Have you considered heterogeneity by [race/gender/income]?"
**Referee pool:** CREDIBILITY (high), POLICY (high), MEASUREMENT (medium), SKEPTIC (low), STRUCTURAL (low), THEORY (low)

### Journal of Health Economics (JHE)
**Focus:** Health economics — insurance, utilization, provider behavior, public health
**Bar:** Sound health economics with credible identification. Institutional knowledge of health care systems expected.
**Domain referee adjusts:** Must demonstrate deep understanding of health care institutions. Moral hazard vs. adverse selection distinction matters. Welfare implications expected. Connection to health policy debates. Knowledge of CMS data, insurance markets, provider incentives.
**Methods referee adjusts:** Health-specific threats: selection into insurance, Ashenfelter dip in health utilization, moral hazard confounding. IV exclusion restrictions scrutinized heavily in health contexts. GLM for cost outcomes expected alongside OLS.
**Typical concerns:** "Is this moral hazard or adverse selection?" "Have you addressed selection into treatment?" "What about the Medicaid population specifically?"
**Referee pool:** STRUCTURAL (high), MEASUREMENT (high), POLICY (medium), CREDIBILITY (medium), THEORY (low), SKEPTIC (low)

### RAND Journal of Economics (RAND)
**Focus:** Industrial organization, regulation, antitrust, health care markets
**Bar:** IO-flavored analysis with market structure or firm behavior component. Structural or quasi-experimental.
**Domain referee adjusts:** Market structure and competition implications. Firm behavior and strategic incentives. Regulatory implications. Welfare analysis (consumer surplus, total surplus) expected.
**Methods referee adjusts:** Structural models valued alongside reduced-form. Demand estimation methods (BLP, discrete choice). Entry/exit models. Merger simulation if relevant. Reduced-form papers need very clean identification.
**Typical concerns:** "What does this imply for market structure?" "Consumer welfare impact?" "Can you do a structural analysis?"
**Referee pool:** STRUCTURAL (high), THEORY (high), SKEPTIC (medium), POLICY (medium), CREDIBILITY (low), MEASUREMENT (low)

### Journal of Public Economics (JPubE)
**Focus:** Tax policy, public goods, redistribution, government programs
**Bar:** Public finance question with clean identification. Understanding of tax/transfer system mechanics.
**Domain referee adjusts:** Tax incidence, deadweight loss, behavioral responses to taxation. Program evaluation of government interventions. Fiscal federalism. Redistribution and inequality. Knowledge of tax code and transfer programs.
**Methods referee adjusts:** Bunching estimators for tax kinks/notches. RDD at eligibility thresholds. DiD around policy changes. Structural models of labor supply response. Extensive vs. intensive margin effects.
**Typical concerns:** "What's the elasticity?" "Extensive or intensive margin?" "Welfare implications of the tax/transfer change?"
**Referee pool:** STRUCTURAL (high), POLICY (high), CREDIBILITY (medium), THEORY (medium), MEASUREMENT (low), SKEPTIC (low)

### Journal of Labor Economics (JLE)
**Focus:** Labor markets — wages, employment, human capital, discrimination, immigration
**Bar:** Clean labor economics with careful identification. Understanding of labor market institutions.
**Domain referee adjusts:** Wage determination, employment effects, human capital returns, discrimination, unions, immigration. Mincer equations and labor supply models. Firm-worker matched data valued. Monopsony and market power in labor markets.
**Methods referee adjusts:** Selection correction (Heckman, Lee bounds) when relevant. Decomposition methods for wage gaps. Clean identification of causal effects on wages/employment. Event study designs around job transitions or policy changes.
**Typical concerns:** "Is this a supply or demand effect?" "Selection into employment?" "What about general equilibrium effects?"
**Referee pool:** CREDIBILITY (high), STRUCTURAL (medium), MEASUREMENT (medium), THEORY (medium), POLICY (low), SKEPTIC (low)

### Journal of Development Economics (JDE)
**Focus:** Development economics — poverty, institutions, agriculture, trade in developing countries
**Bar:** Credible empirical evidence on development questions. RCTs or strong quasi-experimental designs. Field knowledge.
**Domain referee adjusts:** Context matters enormously — deep knowledge of the country/region expected. External validity to other developing country settings. Implementation details for interventions. Cost-effectiveness. Sustainability of effects. Gender and equity dimensions.
**Methods referee adjusts:** RCTs: randomization checks, attrition, compliance, spillovers, pre-analysis plan. Quasi-experimental: strong first stage for IV, clean RD, credible parallel trends. Power calculations. Clustered standard errors at appropriate level.
**Typical concerns:** "Does this generalize beyond this specific context?" "What about attrition?" "Cost-effectiveness?" "Long-run effects?"
**Referee pool:** CREDIBILITY (high), POLICY (high), MEASUREMENT (high), SKEPTIC (medium), STRUCTURAL (low), THEORY (low)

---

**Short Format**

### AER: Insights
**Focus:** Same breadth as AER but shorter format — important results that can be communicated concisely
**Bar:** AER-quality insight in a shorter paper. Must be self-contained and punchy.
**Domain referee adjusts:** Brevity is a feature, not a limitation. One clean result is enough. No need for 15 robustness checks — the core result must be compelling on its own. Well-suited for striking findings or clever identification.
**Methods referee adjusts:** Core identification must be clean. Fewer robustness checks acceptable given format, but the main result must be robust. Transparency and visual evidence valued.
**Typical concerns:** "Can this be communicated in 10 pages?" "Is the single result compelling enough?" "Does this need a longer format to be convincing?"
**Referee pool:** CREDIBILITY (high), POLICY (medium), SKEPTIC (medium), STRUCTURAL (low), THEORY (low), MEASUREMENT (low)
**Table format:** No significance stars. Standard errors in parentheses. Exact p-values or confidence intervals for key results (AEA style).

### Economics Letters
**Focus:** Short papers across all fields of economics — theoretical and empirical
**Bar:** One clear result that can be communicated in 5-8 pages. Speed of publication valued. No room for extensive robustness or literature review — the result must stand on its own.
**Domain referee adjusts:** Contribution must be stated in the first paragraph. No space for extensive institutional background. One key finding, cleanly presented. Incremental extensions of existing work acceptable if the result is sharp.
**Methods referee adjusts:** Identification must be clean but extensive robustness not expected given format. One well-executed specification is enough. Standard errors must be correct. No space for 10-table robustness sections.
**Typical concerns:** "Can this be said in 5 pages?" "Is the single result robust?" "Is this novel enough for a standalone paper?"
**Referee pool:** CREDIBILITY (high), SKEPTIC (medium), THEORY (medium), MEASUREMENT (low), STRUCTURAL (low), POLICY (low)

---

**Econometrics**

### Journal of Econometrics
**Focus:** Econometric theory and methods — estimation, inference, testing, computational methods, machine learning for causal inference
**Bar:** Methodological contribution with formal results. Empirical applications welcome but the method must be the contribution, not the application.
**Domain referee adjusts:** Theoretical novelty is paramount. Must clearly state what existing methods cannot do that yours can. Monte Carlo simulations expected to demonstrate finite-sample properties. Empirical illustration should showcase the method, not the substantive finding.
**Methods referee adjusts:** Formal proofs required for key results (consistency, asymptotic normality, convergence rates). Regularity conditions must be stated and discussed. Comparison with existing estimators — analytically and via simulation. Power analysis. Computational feasibility discussed. Code availability expected.
**Typical concerns:** "What are the asymptotic properties?" "How does this compare to [existing method]?" "What happens in finite samples?" "Are the regularity conditions plausible in practice?"
**Referee pool:** THEORY (high), SKEPTIC (high), MEASUREMENT (high), STRUCTURAL (medium), CREDIBILITY (low), POLICY (low)

### Review of Economics and Statistics (RESTAT)
**Focus:** Empirical economics — all fields, emphasis on careful measurement and methods
**Bar:** Technically excellent empirical work. Values careful econometrics and measurement.
**Domain referee adjusts:** Measurement quality is paramount. Novel data or measurement approaches valued. Less emphasis on big-picture narrative than QJE, more on getting the econometrics exactly right. Replication studies welcome.
**Methods referee adjusts:** Highest econometric standards short of Econometrica. Every assumption must be tested or bounded. Sensitivity analysis expected. Careful treatment of standard errors. Pre-registration or pre-analysis plans viewed favorably.
**Typical concerns:** "Is the measurement precise enough?" "Have you tested every assumption?" "What about measurement error in [variable]?"
**Referee pool:** MEASUREMENT (high), SKEPTIC (high), CREDIBILITY (high), THEORY (medium), STRUCTURAL (low), POLICY (low)

---

**Health Economics**

### Health Economics
**Focus:** Health economics with emphasis on empirical applications — health care demand, insurance, provider behavior, public health interventions, pharmaceutical markets
**Bar:** Sound empirical health economics. Slightly below JHE bar but same methodological expectations. Good outlet for well-executed applied work in health.
**Domain referee adjusts:** Same institutional knowledge as JHE expected — insurance markets, provider incentives, moral hazard, adverse selection. Health policy relevance valued. Understanding of health care data (claims, EHR, surveys). Behavioral health economics increasingly accepted.
**Methods referee adjusts:** Clean identification expected. Health-specific threats addressed (selection into insurance, Ashenfelter dip, moral hazard confounding). Both OLS and GLM for cost outcomes. Subgroup analysis by insurance type, age, income expected.
**Typical concerns:** "Have you addressed selection?" "What about moral hazard?" "Does this replicate across payer types?" "Policy implications?"
**Referee pool:** CREDIBILITY (high), MEASUREMENT (high), POLICY (medium), STRUCTURAL (medium), THEORY (low), SKEPTIC (low)

---

**Urban and Spatial Economics**

### Journal of Urban Economics (JUE)
**Focus:** Urban and regional economics — housing, transportation, local public goods, agglomeration, spatial equilibrium, neighborhood effects
**Bar:** Clean empirical work on urban questions with credible identification. Understanding of spatial economics and local policy variation.
**Domain referee adjusts:** Spatial equilibrium thinking expected — people and firms move, so partial equilibrium results need justification. Housing markets, land use regulation, sorting, commuting. Knowledge of Census/ACS geography, LODES, HMDA. Hedonic models and spatial instruments common. General equilibrium concerns about migration and capitalization.
**Methods referee adjusts:** Spatial identification challenges: selection into neighborhoods, Tiebout sorting, MAUP. Boundary discontinuity designs valued. DiD around local policy changes. IV with Bartik-style shift-share instruments scrutinized. Spatial autocorrelation in standard errors. Conley standard errors when appropriate.
**Typical concerns:** "What about sorting?" "Is this capitalized into housing prices?" "General equilibrium effects?" "Have you addressed spatial autocorrelation?"
**Referee pool:** STRUCTURAL (high), CREDIBILITY (high), MEASUREMENT (medium), POLICY (medium), THEORY (medium), SKEPTIC (low)

### Journal of Economic Geography
**Focus:** Economic geography — agglomeration, trade costs, spatial inequality, regional development, clusters, migration, urban systems
**Bar:** Contribution to understanding the spatial dimension of economic activity. Both theoretical and empirical work accepted. Interdisciplinary with geography and regional science.
**Domain referee adjusts:** Spatial thinking required — distance, borders, market access, gravity models. New Economic Geography tradition (Krugman, Fujita, Venables). Understanding of agglomeration economies, congestion costs, and spatial sorting. European and international evidence valued alongside US.
**Methods referee adjusts:** Spatial econometrics expected when appropriate (spatial lag, spatial error models). Gravity equation estimation (PPML, multilateral resistance). Handling of spatial autocorrelation. Market access instruments. Shift-share designs for local labor market shocks.
**Typical concerns:** "What about spatial sorting?" "Have you accounted for market access?" "Is this agglomeration or selection?" "Spatial autocorrelation in errors?"
**Referee pool:** STRUCTURAL (high), MEASUREMENT (high), THEORY (medium), CREDIBILITY (medium), POLICY (medium), SKEPTIC (low)

---

## Finance

### The Journal of Finance (JF)
**Focus:** All areas of finance — asset pricing, corporate finance, market microstructure, behavioral finance, household finance
**Bar:** Must advance our understanding of financial markets or financial decision-making. Big question, clean execution. The finance equivalent of AER in breadth and ambition.
**Domain referee adjusts:** Contribution must matter to finance broadly, not just one niche. Theoretical motivation expected — even empirical papers need a clear economic framework. Equilibrium implications considered. Risk adjustment must be thorough for asset pricing papers.
**Methods referee adjusts:** For corporate/household finance: clean causal identification expected (DiD, IV, RDD). For asset pricing: factor model tests, Fama-MacBeth, portfolio sorts with proper standard errors. Endogeneity concerns taken very seriously. Instrument validity scrutinized.
**Typical concerns:** "What's the economic mechanism?" "Is this priced risk or mispricing?" "Have you addressed endogeneity?" "Does this survive controlling for known factors?"
**Referee pool:** THEORY (high), STRUCTURAL (high), CREDIBILITY (medium), SKEPTIC (medium), MEASUREMENT (low), POLICY (low)

### Journal of Financial Economics (JFE)
**Focus:** Corporate finance, asset pricing, banking, governance, financial intermediation
**Bar:** Rigorous empirical or theoretical work. Strong emphasis on economic significance, not just statistical significance. Slightly more empirical focus than JF.
**Domain referee adjusts:** Corporate finance and governance papers especially valued. Institutional knowledge of financial markets expected. Firm-level analysis with careful treatment of endogeneity. Understanding of agency problems, contracting, and incentive alignment.
**Methods referee adjusts:** Natural experiments and quasi-experimental designs valued in corporate finance. Event studies must follow modern best practices (short window, proper benchmarking). Diff-in-diff around regulatory changes common. IV exclusion restrictions scrutinized heavily.
**Typical concerns:** "Is this economically significant or just statistically significant?" "What about reverse causality?" "Have you controlled for firm fixed effects?" "Is your instrument truly exogenous?"
**Referee pool:** CREDIBILITY (high), STRUCTURAL (high), THEORY (medium), SKEPTIC (medium), MEASUREMENT (low), POLICY (low)

### The Review of Financial Studies (RFS)
**Focus:** Theoretical and empirical finance — broad coverage, values technical sophistication
**Bar:** Technically excellent finance research. Tolerates longer papers with thorough analysis. Values completeness and rigor over narrative.
**Domain referee adjusts:** Thoroughness valued — complete robustness section expected. Both theoretical and empirical contributions accepted. International finance and emerging markets welcome. Novel datasets or measurement approaches valued.
**Methods referee adjusts:** Full battery of robustness checks expected. Multiple identification strategies appreciated. Structural estimation alongside reduced-form welcome. Careful inference — clustered standard errors, bootstrap, wild cluster bootstrap when appropriate.
**Typical concerns:** "Have you checked robustness to alternative specifications?" "What about clustering at the firm vs. industry level?" "Can you provide a structural interpretation?"
**Referee pool:** SKEPTIC (high), MEASUREMENT (high), STRUCTURAL (medium), THEORY (medium), CREDIBILITY (low), POLICY (low)

### Journal of Financial and Quantitative Analysis (JFQA)
**Focus:** Empirical and theoretical finance with quantitative rigor — corporate finance, investments, banking, capital markets
**Bar:** Sound empirical finance with clear contribution. Below top-3 finance bar but same rigor expectations. Good outlet for careful empirical work.
**Domain referee adjusts:** Solid contribution to the subfield sufficient — doesn't need to reshape the whole field. International and comparative studies welcome. Clear economic intuition expected.
**Methods referee adjusts:** Standard modern finance econometrics expected. Fixed effects, clustering, instrumental variables. Event study methodology must be current. Robustness to alternative specifications.
**Typical concerns:** "Is this incremental relative to existing work?" "Have you considered international evidence?" "Is the sample period long enough?"
**Referee pool:** CREDIBILITY (high), MEASUREMENT (medium), SKEPTIC (medium), THEORY (medium), STRUCTURAL (low), POLICY (low)

---

## Accounting

### Journal of Accounting Research (JAR)
**Focus:** Financial reporting, auditing, disclosure, capital markets — the most empirically rigorous accounting journal
**Bar:** Archival empirical work with strong identification, or analytical models with clear predictions. JAR is the most "economics-adjacent" accounting journal.
**Domain referee adjusts:** Must understand GAAP/IFRS reporting incentives. Earnings management, accruals quality, and disclosure theory. Capital markets consequences of accounting choices. Audit quality and auditor incentives.
**Methods referee adjusts:** Identification strategy must be clean — JAR holds to economics standards. DiD around accounting standard changes common. Selection models for auditor choice. Heckman corrections when appropriate. Pre-trends and parallel trends for policy changes.
**Typical concerns:** "Is this an accounting paper or a finance paper?" "Have you controlled for accruals quality?" "What about the selection into treatment?" "Does this survive the Hribar-Collins adjustment?"
**Referee pool:** CREDIBILITY (high), MEASUREMENT (high), STRUCTURAL (medium), THEORY (medium), SKEPTIC (low), POLICY (low)

### Journal of Accounting and Economics (JAE)
**Focus:** Economic analysis of accounting — contracting, regulation, capital markets, disclosure
**Bar:** Must have a clear economic framework. JAE values theory-motivated empirical work. The most economics-flavored accounting journal.
**Domain referee adjusts:** Agency theory and contracting framework expected. Understanding of SEC regulation, SOX, Dodd-Frank implications. CEO compensation and governance. Tax avoidance and tax planning. Positive accounting theory tradition.
**Methods referee adjusts:** Theory-driven hypotheses expected — not data-mining. Structural approaches valued alongside reduced-form. Large-sample archival methods with careful endogeneity treatment. Instrument validity in governance studies especially scrutinized.
**Typical concerns:** "What's the economic theory behind this prediction?" "Is this a contracting or valuation story?" "Have you addressed the Leamer critique?" "What about omitted variable bias?"
**Referee pool:** THEORY (high), STRUCTURAL (high), CREDIBILITY (medium), MEASUREMENT (medium), SKEPTIC (low), POLICY (low)

### The Accounting Review (TAR)
**Focus:** Broadest accounting journal — financial, managerial, auditing, tax, systems
**Bar:** Significant contribution to accounting knowledge. More methodologically diverse than JAR/JAE — accepts experiments, surveys, and analytical work alongside archival.
**Domain referee adjusts:** Broader scope than JAR/JAE — managerial accounting, cost accounting, and accounting education also considered. Practical implications for accounting profession valued. Standard-setting relevance appreciated.
**Methods referee adjusts:** Archival papers: similar identification standards to JAR. Experiments: proper randomization, demand effects, external validity. Surveys: response rates, non-response bias. Tax papers: knowledge of IRC provisions expected.
**Typical concerns:** "What are the implications for standard-setters?" "Does this generalize beyond your sample?" "Have you addressed self-selection?" "What about the tax implications?"
**Referee pool:** CREDIBILITY (medium), MEASUREMENT (high), POLICY (medium), STRUCTURAL (medium), THEORY (medium), SKEPTIC (low)

### Contemporary Accounting Research (CAR)
**Focus:** All areas of accounting — international perspective, methodological innovation
**Bar:** Solid accounting research with clear contribution. More international scope than US-centric TAR/JAR. Good outlet for methodological contributions to accounting.
**Domain referee adjusts:** International accounting standards (IFRS adoption, cross-country comparisons) valued. Canadian and international evidence welcome alongside US. Innovative measurement approaches.
**Methods referee adjusts:** Same rigor as TAR for archival work. Novel econometric approaches to accounting problems valued. Textual analysis and machine learning applications increasingly accepted. Careful treatment of measurement error in accounting variables.
**Typical concerns:** "Does this apply outside the US?" "How sensitive are results to the accrual measure used?" "Have you considered IFRS vs. GAAP differences?"
**Referee pool:** MEASUREMENT (high), CREDIBILITY (high), SKEPTIC (medium), POLICY (low), STRUCTURAL (low), THEORY (low)

---

## Marketing

### Journal of Marketing Research (JMR)
**Focus:** Marketing research methods and substantive findings — consumer behavior, pricing, advertising, digital marketing
**Bar:** Methodological rigor with marketing substance. Values causal identification and experimental design. The most empirically rigorous marketing journal.
**Domain referee adjusts:** Must speak to marketing managers and academics. Consumer welfare and firm implications. Understanding of marketing mix (price, promotion, distribution, product). Digital marketing and platform economics increasingly important.
**Methods referee adjusts:** Experiments (lab and field) held to high standards — randomization checks, demand effects, external validity. Structural demand models (BLP-style) valued. Causal inference from observational data must be convincing. Machine learning for prediction vs. causal inference distinction expected.
**Typical concerns:** "What's the managerial implication?" "Can you run a field experiment to validate?" "Have you addressed endogeneity of price/advertising?" "What about demand-side vs. supply-side effects?"
**Referee pool:** CREDIBILITY (high), STRUCTURAL (high), MEASUREMENT (medium), POLICY (medium), THEORY (low), SKEPTIC (low)

### Marketing Science
**Focus:** Quantitative marketing — structural models, field experiments, econometric analysis of marketing phenomena
**Bar:** Technical sophistication expected. The most methods-intensive marketing journal. Structural estimation and formal models highly valued.
**Domain referee adjusts:** Quantitative marketing models — demand estimation, pricing optimization, advertising response, customer lifetime value. Platform economics and two-sided markets. Competitive strategy implications. Welfare analysis of marketing practices.
**Methods referee adjusts:** Structural models expected for many topics (demand estimation, dynamic pricing, entry/exit). BLP, nested logit, mixed logit standard vocabulary. Field experiments and A/B testing with proper inference. Bayesian methods accepted. Counterfactual simulations expected alongside reduced-form.
**Typical concerns:** "Can you estimate a structural model?" "What's the counterfactual policy simulation?" "Have you estimated price elasticities?" "What about consumer heterogeneity?"
**Referee pool:** STRUCTURAL (high), THEORY (high), MEASUREMENT (medium), CREDIBILITY (medium), SKEPTIC (low), POLICY (low)

### Journal of Consumer Research (JCR)
**Focus:** Consumer behavior — psychology of consumption, decision-making, identity, culture
**Bar:** Theoretical contribution to understanding consumer behavior. Values conceptual novelty and experimental rigor. More behavioral/psychological than JMR or Marketing Science.
**Domain referee adjusts:** Psychological theory of consumer behavior expected. Process evidence (mediation, moderation) valued. Identity, motivation, judgment and decision-making frameworks. Cultural and sociological perspectives also accepted. Less emphasis on managerial implications than JMR.
**Methods referee adjusts:** Experimental designs dominant — proper controls, manipulation checks, attention checks. Multiple studies showing robustness and boundary conditions expected. Effect sizes and confidence intervals. Replication of core finding across studies. Pre-registration viewed favorably.
**Typical concerns:** "What's the underlying psychological process?" "Can you show mediation?" "What are the boundary conditions?" "Have you replicated across different contexts?"
**Referee pool:** THEORY (high), MEASUREMENT (high), SKEPTIC (medium), CREDIBILITY (medium), STRUCTURAL (low), POLICY (low)

---

## Management and Strategy

### Management Science
**Focus:** Interdisciplinary — operations, finance, marketing, strategy, economics, behavioral science, organizations, information systems
**Bar:** Technically rigorous work that spans business disciplines. Values formal models AND clean empirical work. Extremely broad scope — the most interdisciplinary top business journal.
**Domain referee adjusts:** Paper must fit one of the departments (operations, finance, marketing, etc.) but speak to a broader audience. Practical implications valued. Model-driven empirical work appreciated. Accepts papers that wouldn't fit neatly into a single field journal.
**Methods referee adjusts:** Standards match the relevant field (finance papers judged by finance methods standards, etc.). Structural estimation, causal inference, and field experiments all welcome. Simulation and computational methods accepted. Optimization and analytical models alongside empirical work.
**Typical concerns:** "Which department does this fit?" "Is this a Management Science paper or a field journal paper?" "What's the practical implication?" "Does the model match the empirics?"
**Referee pool:** STRUCTURAL (high), CREDIBILITY (high), THEORY (medium), MEASUREMENT (medium), POLICY (low), SKEPTIC (low)

### Strategic Management Journal (SMJ)
**Focus:** Strategy — competitive advantage, diversification, alliances, innovation, governance, entrepreneurship
**Bar:** Significant contribution to strategic management theory and practice. Empirical papers need strong identification. Theory papers need testable implications.
**Domain referee adjusts:** Resource-based view, dynamic capabilities, competitive dynamics, industry analysis. Understanding of firm heterogeneity and sustained competitive advantage. Alliance formation, M&A, and diversification. Innovation strategy and technology competition.
**Methods referee adjusts:** Endogeneity is the central concern — firm strategy is endogenous by nature. Instrumental variables, DiD around exogenous shocks, matching methods. Panel data with firm fixed effects expected. Selection models for entry/exit decisions. Heckman corrections common.
**Typical concerns:** "Is strategy endogenous here?" "What about unobserved firm heterogeneity?" "Can you identify the causal effect of this strategic choice?" "What's the theory of competitive advantage?"
**Referee pool:** THEORY (high), CREDIBILITY (high), STRUCTURAL (medium), SKEPTIC (medium), MEASUREMENT (low), POLICY (low)

### Administrative Science Quarterly (ASQ)
**Focus:** Organization theory and behavior — institutions, networks, culture, power, status, organizational design
**Bar:** Deep theoretical contribution with rigorous evidence. ASQ values papers that change how you think about organizations. Accepts qualitative, quantitative, and mixed methods.
**Domain referee adjusts:** Institutional theory, organizational ecology, network theory, social categorization. Status and legitimacy in markets. Organizational identity and culture. Power and politics in organizations. Historical and comparative analysis valued.
**Methods referee adjusts:** Quantitative papers: panel data, fixed effects, causal identification expected. Qualitative papers: systematic data collection, coding protocols, theoretical sampling. Mixed methods: integration of qualitative and quantitative evidence. Ethnographic work accepted if theoretically motivated.
**Typical concerns:** "What's the theoretical mechanism?" "How does this advance organization theory?" "Is this generalizable beyond your empirical context?" "Have you considered alternative theoretical explanations?"
**Referee pool:** THEORY (high), MEASUREMENT (high), STRUCTURAL (medium), CREDIBILITY (medium), POLICY (low), SKEPTIC (low)

---

## Add Your Own Journal

Copy this template and add it above this section:

```markdown
### [Journal Name] ([Abbreviation])
**Focus:** [fields and topics covered]
**Bar:** [what it takes to publish here]
**Domain referee adjusts:** [what matters most to domain reviewers at this journal]
**Methods referee adjusts:** [rigor expectations, preferred methods, required checks]
**Typical concerns:** [common referee questions at this journal]
**Referee pool:** [disposition] (high/medium/low) for each: STRUCTURAL, CREDIBILITY, MEASUREMENT, POLICY, THEORY, SKEPTIC
**Table format:** [optional — only include if journal deviates from the APA default. E.g., "ASA style" or "Nature-family style."]
```

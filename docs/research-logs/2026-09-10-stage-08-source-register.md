# Stage 8 source register: experiments, measurement and attribution

Research date: 10 September 2026. This register supports [the Stage 8 model](2026-09-10-stage-08-experiment-measurement-attribution-model.md). Sources are the public material actually returned by web retrieval, not a claim that every linked paper, dataset, account feature or implementation was inspected.

The model distinguishes source findings from original project design. Platform documentation establishes documented product behaviour, not account availability, independent effectiveness or commercial approval. Research abstracts support bounded methodological findings, not unexamined full methods. Teaching material supports the stated elementary calculations under its assumptions. No PDF, raw campaign dataset, advertising account, experiment platform or live customer record was accessed.

## R01

**Google Ads: Set up a custom experiment**  
Source: https://support.google.com/google-ads/answer/6261395/set-up-a-campaign-experiment  
Publication/update: Undated living documentation. Retrieved: 10 September 2026.  
Access: Public documentation text returned by web search.

Finding used: Experiment setup distinguishes traffic/budget allocation and cookie- versus search-based assignment, and warns that in-flight changes complicate interpretation.

Limitation: No experiment was configured. The provider's split recommendations, eligibility numbers and supported campaign list are not universal power or identity guarantees; exact execution support needs current account/product verification.

## R02

**Google Ads: About Conversion Lift**  
Source: https://support.google.com/google-ads/answer/12003020?hl=en  
Publication/update: Undated living documentation. Retrieved: 10 September 2026.  
Access: Public HTML overview opened and read, including study-type and metric descriptions.

Finding used: Conversion Lift addresses incremental conversions; user- and geography-based studies and their available quantities differ. Access is not available to every account.

Limitation: This simplified overview is not a complete statistical analysis plan. No study access, randomisation, output or account data was verified. Reported value/spend definitions must be retained rather than assuming one universal incremental-return ratio.

## R03

**Google Ads: About Brand Lift**  
Source: https://support.google.com/google-ads/answer/9049825?hl=en  
Publication/update: Undated living documentation. Retrieved: 10 September 2026.  
Access: Public HTML overview opened and read; embedded video was not viewed.

Finding used: Survey-based brand measures differ from clicks and other delivery metrics; reported response counts, baseline/exposed rates and lift types matter. Feature access has account conditions.

Limitation: No survey, respondent data or commercial effect was observed. A positive brand-response change is not a measured revenue return. Account-specific access and requirements must be checked at execution.

## R04

**Google Ads: About data-driven attribution**  
Source: https://support.google.com/google-ads/answer/6394265  
Publication/update: Undated living documentation. Retrieved: 10 September 2026.  
Access: Public HTML opened and read at the unparameterised URL after an initial parameterised request failed.

Finding used: The model allocates conversion credit using advertiser-specific interaction/conversion information and can influence bidding. Depending on available data, attribution outputs can coincide with other models.

Limitation: The linked methodology PDF was not read. Vendor descriptions of contribution do not independently establish causal validity, business qualification or cross-provider deduplication for a consuming project. No account configuration was changed.

## R05

**Microsoft Research: Diagnosing Sample Ratio Mismatch in A/B Testing**  
Source: https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/  
Publication: 14 September 2020. Retrieved: 10 September 2026.  
Access: Public practitioner article text returned by web search, including detection and diagnosis sections.

Finding used: Sample-ratio mismatch concerns counts relative to configured assignment; diagnosis can involve assignment, execution, log processing and analysis/triggering. The article treats unresolved mismatch as a trustworthiness problem.

Limitation: Its internal threshold and incidence figures are not adopted as universal advertising settings. A diagnostic pass does not establish that every source of bias is absent. Linked papers, tooling, images and example systems were not executed or exhaustively inspected.

## R06

**Johari, Koomen, Pekelis and Walsh: Always Valid Inference: Continuous Monitoring of A/B Tests**  
Source: https://pubsonline.informs.org/doi/10.1287/opre.2021.2135  
Publication: Online 10 August 2021; Operations Research 70(3), 1806–1821. Retrieved: 10 September 2026.  
Access: Original publisher abstract and bibliographic information returned by web search.

Finding used: Ordinary fixed-sample inference can lose its guarantees under outcome-dependent continuous stopping; the paper develops inference designed for sequential monitoring and multiple-testing control.

Limitation: Full methods and implementation were not read or reproduced. The source motivates a method-specific contract, not a claim that this repository implements sequential inference or that every adaptive analysis is valid.

## R07

**NIST/SEMATECH e-Handbook: Comparing two proportions, section 7.3.3**  
Source: https://www.itl.nist.gov/div898/handbook/prc/section3/prc33.htm  
Publication/update: No page-specific date established. Retrieved: 10 September 2026.  
Access: Public HTML opened and read.

Finding used: For reasonably large independent binomial samples, the equality test uses a pooled proportion in the standard error and compares the resulting statistic with an appropriate normal critical value.

Limitation: This is not a clustered, adaptive, sparse-data or arbitrary-ratio analysis method. No claim is made that fractional attribution outputs or repeated impressions satisfy its assumptions.

## R08

**Penn State STAT 509: Sample Size and Power, Lesson 8**  
Source: https://online.stat.psu.edu/stat509/Lesson08  
Publication/update: No page-specific date established. Retrieved: 10 September 2026.  
Access: Search-returned primary teaching extract containing the two-proportion sample-size formula and allocation definition. Direct page opens returned 502 errors; the full page was not accessed.

Finding used: The stated normal planning approximation connects allocation, significance, power, pooled proportion and effect size; sample size does not itself cure lack of validity.

Limitation: The model uses only the returned equation for an explicitly synthetic independent binary calculation. It does not claim a full course review, exact finite-sample guarantee, sequential power calculation or real traffic forecast. Clinical examples are not advertising recommendations.

## R09

**Penn State STAT 200: Inference for Two Samples, Lesson 9**  
Source: https://online.stat.psu.edu/stat200/Lesson09  
Publication/update: No page-specific date established. Retrieved: 10 September 2026.  
Access: Search-returned primary teaching extract containing the independent-proportion confidence-interval and test-statistic summary. Direct page opens returned 502 errors; the full page was not accessed.

Finding used: The normal difference-in-proportions confidence interval uses the separate sample variances, while the equality test uses pooled variance; applicability conditions matter.

Limitation: Only the supplied summary equation and conditions support the arithmetic probes. They are not a universal interval method for advertising metrics. No hidden sections, software or teaching examples were reproduced.

## R10

**Gordon, Zettelmeyer, Bhargava and Chapsky: A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook**  
Source: https://pubsonline.informs.org/doi/10.1287/mksc.2018.1135  
Publication: Online 4 April 2019; Marketing Science 38(2), 193–225. Retrieved: 10 September 2026.  
Access: Original publisher abstract/bibliographic text returned by search; the authors' institutional abstract was also encountered.

Finding used: The studied observational approaches often disagreed with the randomised experiment estimates despite extensive available covariates.

Limitation: Full paper, appendix and raw data were not analysed or replicated. The finding does not imply that every observational model fails, nor that a new platform experiment automatically supplies a valid counterfactual.

## Discovery, exclusions and remaining limits

Research began with the literal experiment/measurement requirements, then checked assignment, sample-ratio diagnostics, optional stopping, power/precision, attributed versus incremental value and survey outcomes. Primary sources were preferred over agency glossaries, certification-answer sites and search-result replicas. Unrelated search results were not evidence.

No source was used to choose actual campaign thresholds, spend, account settings, commercial terms or legal conclusions for the user. The illustrative thresholds and counts are labelled synthetic design inputs; numerical outputs are calculated from them rather than invented as observed outcomes. The unavailable full Penn State pages limit access claims but not use of the exact retrieved equations. No mandatory named source is missing from the Stage 8 bootstrap requirement.

This is a purpose-bounded model-design review, not a systematic literature review, full all-platform audit or implementation benchmark. Current execution still requires the selected study's actual method, account capabilities, appropriate legal/data-use decisions and technical evidence.

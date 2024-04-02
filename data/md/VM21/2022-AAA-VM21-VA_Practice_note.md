# Implementation of Requirements for Principle-Based Reserves for Variable Annuities - 2022 Edition of VM-21 

February 2022

Developed by the Variable Annuity Reserves \& Capital Work Group of the Life Practice Council of the American Academy of Actuaries

![](https://cdn.mathpix.com/cropped/2024_03_24_c585537438f7869e560ag-01.jpg?height=263&width=711&top_left_y=2091&top_left_x=707)

Objective. Independent. Effective.

## Implementation of Requirements for Principle-Based Reserves for Variable Annuities - 2022 Edition of VM-21

February 2022

## Developed by the Variable Annuity Reserves \& Capital Work Group of the Life Practice Council of the American Academy of Actuaries

![](https://cdn.mathpix.com/cropped/2024_03_24_c585537438f7869e560ag-02.jpg?height=325&width=705&top_left_y=1488&top_left_x=707)

The American Academy of Actuaries is a 19,500+ member professional association whose mission is to serve the public and the U.S. actuarial profession. For more than 50 years, the Academy has assisted public policymakers on all levels by providing leadership, objective expertise, and actuarial advice on risk and financial security issues. The Academy also sets qualification, practice, and professionalism standards for actuaries in the United States.

# Variable Annuity Reserves \& Capital Work Group Practice Note Contributors 

Connie Tang, MAAA, FSA

Chair

Cindy Barnard, MAAA, FSA

Linn K. Richardson, MAAA, FSA

Thomas Campbell, MAAA, FSA

Patricia Schwartz, MAAA, FSA

Dianna Goodman, MAAA, FSA Yuan Tao, MAAA, FSA

Craig Morrow, MAAA, FSA William Wilton, MAAA, FSA

Zohair Motiwalla, MAAA, FSA Kaihua Yu, MAAA, FSA

Scott O'Neal, MAAA, ASA

We welcome your comments and suggestions for additional questions to be addressed by this practice note. Please address all communications to the Academy's life policy analyst at lifeanalyst@actuary.org.
Table of Contents
Introduction ..... 4
List of Acronyms ..... 5
Background ..... 5

1. Transition ..... 6
2. Standard Projection ..... 8
Product and/or Contractual Conflicts ..... 8
Other questions ..... 9
3. Asset Modeling \& Discount Rates ..... 17
4. Scenarios ..... 20
5. Hedging ..... 24
6. C-3 Phase 2 RBC ..... 28
7. Disclosures ..... 29
8. Miscellaneous / Other ..... 33

## Introduction

This practice note supplement was prepared by the Variable Annuity Reserves \& Capital Work Group of the American Academy of Actuaries to provide information to actuaries on current and emerging practices concerning the 2020 revisions to principle-based reserves and capital for variable annuities (VAs). It is intended to supplement the available actuarial literature in the area under discussion. Actuaries are not in any way bound to comply with practice notes nor to conform their work to the practices described in practice notes. This practice note is not a promulgation of the Actuarial Standards Board, is not an actuarial standard of practice, is not binding upon any actuary and is not a definitive statement as to what constitutes generally accepted practice in the area under discussion. Events occurring subsequent to this publication of the practice note may make the practices described in this practice note irrelevant or obsolete.

The practices here represent the views of actuaries who have been involved in the revision of the VA standards, along with practicing actuaries. The purpose of the practice note is to assist actuaries with implementation of the revisions adopted by the NAIC as detailed in the Requirements for PrincipleBased Reserves for Variable Annuities-2022 Edition of VM-21. It is important that the reader review any differences that exist between the version of VM-21 on which this practice note was based and the version that is viewed as applicable to current valuations because the Valuation Manual is a living document and subject to change. This practice note does not include discussion of any state variations to the statutory reserve and capital requirements, such as New York Regulation 213.

It is expected that actuarial practice for determining principle-based statutory reserves and capital will continue to emerge over time. It is likely that additional actuarial practice will be developed that is not contained in this practice note. The goal of this practice note is twofold: to assist actuaries who are implementing VM-21 revisions in understanding the new requirements and to provide an overview of some of the actuarial practices being used.

Additions and revisions to this practice note may be needed in the future as practices are further developed and issues that are not anticipated below are addressed.

## List of Acronyms

| ASC | Accounting Standards Codification |
| :--- | :--- |
| CDHS | Clearly Defined Hedging Strategy |
| CSMP | Company-Specific Market Path |
| CTE | Conditional Tail Expectation |
| CTEPA | Conditional Tail Expectation with Prescribed <br> Assumptions |
| DIM | Direct Iteration Method |
| DTA | Deferred Tax Asset |
| FAS | Financial Accounting Standards |
| GAPV | Guarantee Actuarial Present Value |
| GMDB | Guaranteed Minimum Death Benefit |
| GMIB | Guaranteed Minimum Income Benefit |
| GMWB | Guaranteed Minimum Withdrawal Benefit |
| GPVAD | Greatest Present Value of Accumulated |
| Deficiencies |  |
| IMR | Interest Maintenance Reserve |
| MTA | Macro Tax Adjustment |
| NAIC | National Association of Insurance Commissioners |
| NAER | Net Asset Earned Rate |
| PIMR | Pretax Interest Maintenance Reserve |
| SPA | Standard Projection Amount |
| SSAP | Statement of Statutory Accounting Principles |
| STR | Specific Tax Recognition |
| VA | Variable Annuity |

## Background

Variable annuity (VA) products have been subject to principle-based methodologies since 2005 for C-3 Phase 2 risk-based capital (RBC) and 2009 for reserves. The 2020 revisions consisted of targeted changes to:

- remove restrictions that limit the use of hedging in risk management; and
- reduce non-economic reserve and capital requirements and volatility.

Basic principles, including the setting of company assumptions and margins and projection of liability cash flows, were largely unchanged. As a result, this practice note focuses on transition issues and the changes to VM-21 and is intended to supplement the existing VA practice note (https://www.actuary.org/sites/default/files/files/VAPN\ FINAL\ WEB\ 040511.4.pdf/VAPN\ F INAL\%20WEB\%20040511.4.pdf).

Key changes include:

- Aligning reserve and capital projections, including calculations for hedging and revenue sharing
- Redefining C-3 Phase 2 RBC as 25\% of the tax-adjusted difference between CTE98 and the statutory reserve and modifying RBC smoothing calculations
- Eliminating the C-3 Phase 2 Standard Scenario and replacing the reserve Standard Scenario with a Standard Projection that uses prescribed assumptions but better aligns with the stochastic calculation methodology
- Eliminating the use of working reserves in the stochastic calculations
- Clarifying discount rates and the methodology used to determine deficiencies
- Designating the Academy Interest Rate Generator as the prescribed generator and adopting VM20 general account asset projection guidance
- Allocating aggregate reserves to each contract based on risk
- Simplifying certain hedging projections
- Expanding disclosure and hedging back-testing requirements and incorporating all disclosuresin the VM-31 PBR Report.


## 1. Transition

Q 1.1: What are some of the considerations for determining whether the framework change is $a$ statutory change in valuation basis?

A: A statutory "change in valuation basis" is an accounting concept that is covered in the NAIC Accounting Practices and Procedures Manual, specifically SSAP 51R Paragraphs 36 through 40.

Paragraph 37b states that a change in valuation basis shall include cases where the required reserve methodology has changed. Though there is not a bright-line definition of what constitutes a "methodology" change under principle-based reserves, some actuaries believe that the changes to VM21/Actuarial Guideline XLIII (AG43) effective under the 2020 Valuation Manual and the 2019 version of AG43 were extensive enough to be classified as a statutory change in valuation basis. Some actuaries believe the NAIC's documentation in the submission forms updating SSAP 51R supports this view.

According to SSAP 51R, Paragraph 37a, changes due to normal assumption changes or automatic changes required by the methodology (e.g., reported reserve transitions between stochastic reserves and the Standard Projection Amount) are not considered statutory changes in valuation basis.

SSAP 51R, Paragraph 37b has been updated to clarify that a statutory change in valuation basis does occur when commissioner approval is required for a voluntary decision to change from one allowable reserving calculation (sometimes referred to as "method") to another.

Q 1.2: What are some of the considerations for determining the amount of the change in valuation basis to be reported in Exhibit 5A? What if a company opted for the 36-month Phase-in under VM-21? Should it be reported only in the year of implementation or recognized in each of the three years?

A: Paragraph 39 of SSAP 51R provides that the change is "based on the difference between the reserve under the old and new methods as of the beginning of the year." For example, assuming the reserve difference attributable to the change in basis is $\$ 90$ million as of Jan. 1,2020 , and the company has not elected to phase in the impact, $\$ 90$ million would be reported in Exhibit 5A.

If the above company had instead elected a three-year phase-in for the $\$ 90$ million impact, some actuaries believe the change in basis reported in Exhibit 5A would be $\$ 30$ million in $2020, \$ 30$ million in 2021 , and $\$ 30$ million in 2022 . One rationale for this approach is consistency with companies that do not phase-in impacts as well as paragraph 39 of SSAP 51R, which provides guidance that such "difference shall not be phased in over time unless this statement or the Valuation Manual, Section VM-21 Requirements for Principle-Based Reserves for Variable Annuities (VM-21), prescribes a new method and a specific transition that allows for grading."

A different approach may produce inconsistencies between the change in surplus resulting from an Exhibit 5A amount and the actual reserve held.

The actuary may want to consider discussing any questions regarding change in basis amounts with the statutory financial accountants at the company and may also wish to consider guidance in the Statutory Accounting Principles Preamble VII Materiality.

## Q 1.3: If a company changes from the Company-Specific Market Path (CSMP) method to the CTE with Prescribed Assumptions (CTEPA) method, or vice versa, should this be considered a change in basis?

A: According to Paragraph 37b of SSAP 51, "voluntary decisions to choose one allowable reserving methodology over another, which require commissioner approval under the Valuation Manual, shall be reported as a change in valuation basis." BecauseVM-21 Section 6.B. 2 requires domiciliary commissioner approval for CSMP / CTEPA changes, it appears that such a change may qualify as a statutory change in basis that is reportable in Exhibit 5A if the amount is non-zero.

## Q 1.4: Would a change in the prescribed assumptions applicable to the Standard Projection Amount be a change in basis?

Some actuaries believe that the methods in VM-21 involve a review and routine update of the assumptions such that changes to these prescribed assumptions would meet the accounting definition of "an update to estimate" and would therefore not be a change in basis.

## 2. Standard Projection

## Product and/or Contractual Conflicts

Q 2.1: What are some of the ways that product or contractual features that conflict with Standard Projection requirements may be reflected? For example, what if a GMIB rider specifies or requires a policyholder to set the annuitization age?

A: Some actuaries might consider factors such as the degree of certainty, level and conservatism, and materiality of the contractual features. For example, if the GMIB rider specifies the annuitization age with certainty, some actuaries would model the contractually specified annuitization age. Others might follow prescribed annuitization assumptions and adjust annuitization assumptions only after the specified event has occurred. Some may reflect contractual features if they produce more conservative reserves but follow Standard Projection requirements when they are more conservative (e.g., Standard Projection forbids contracts with guaranteed death benefits to lapse even though they contractually would). If the contractual features do not materially impact the result, some actuaries believe it may be acceptable to not reflect these features and use the Standard Projection requirements.

Regardless of the decision, the actuaries may wish to consider explicitly documenting the approach and rationale. VM-31 Section 3.F.12.d requires discussion of differences between stochastic and Standard Projection cash-flow models, and Section 3.F.12.i requires documentation of modifications to the Standard Projection requirements. Actuaries may also consider language in VM-21 Sections 6.B.1 and 6.C.1.a.

## Q 2.2: What are some of things an actuary may do when their VM-21 models cannot exactly reflect the prescribed Standard Projection assumptions or methodology?

A: The language in VM-21, Sections 6.B.1 and 6.C.1.a provides some guidance in this case. Some actuaries believe that the answer depends on the materiality of the specific feature. If omitting these prescribed assumptions or methodologies materially understates the Standard Projection Amount, especially when the Additional Standard Projection Amount may drive the aggregate reserve, some actuaries would include a topside adjustment in the final reserve amount.

The actuary may wish to consider VM-31 Section 3.F.12.i when documenting the approach used and explaining deviations from VM-21 prescribed assumptions and methodology. This documentation might include estimates of the feature in question and/or rationalization for why simplifications would not result in a material understatement per VM-31 Section 3.F.2.e.

Q 2.3: How should GMIB contracts that have guaranteed growth and only dollar-for-dollar partial withdrawal treatment (rather than dollar-for-dollar up to a threshold and proportional thereafter) be treated under the Standard Projection?

A: Some actuaries believe these contracts should be treated as a hybrid GMIB because they have guaranteed growth and the dollar-for-dollar withdrawal treatment means that the policyholder can essentially strip the contract by withdrawing the entire account value and then annuitizing the net amount at risk for a stream of periodic payments (thereby resembling a GMWB that is taking systematic withdrawals). In this case, although there is no dollar-for-dollar maximum withdrawal amount threshold above which withdrawals are proportional, some actuaries may set the threshold based on company historical experience, at the rollup rate, or some other reasonable assumption.

Regardless of approach, the actuary may wish to consider documenting the assumption used in accordance with the language in VM-31 Section 3.F.12.f and 3.F.12.j and VM-21 Sections 6.B. 1 and 6.C.1.a.

Q 2.4: Consider a GMWB or Hybrid GMIB contract that has a benefit base with guaranteed growth that is tied to a Treasury rate. When calculating the GAPVs under the Withdrawal Delay Cohort Method, what interest rate should be used for projecting the benefit base growth? (Recognizing that using the Treasury rate on the valuation date would result in a different set of GAPVs on different valuation dates)

A: Some actuaries interpret the language in VM-21 Section 6.C.3.n that states that "these calculations only need to be performed once for a given set of contracts with a certain issue age, guaranteed benefit product, and tax status" as providing support for not refreshing the GAPVs used in the Withdrawal Delay Cohort Method process (and the resulting withdrawal curves). Accordingly, this calculation could be carried out on a specific date (and using the requisite Treasury rate on this date) as a one-off exercise. Other actuaries might use a steady state assumption based on a long-term view or the $3 \%$ fixed rate that is specified for the GAPV calculation under the Withdrawal Delay Cohort Method.

Regardless of the approach used, VM-21 Section 6.C.3.f states that the rate that is used shall be assumed to remain constant at its value during the projection interval (within the GAPV calculation).

## Other questions

Q 2.5: What are some practical approaches for implementing the different mortality modeling requirements within the Standard Projection?

A: VM-21 Section 6.9 provides the formulae to determine the final mortality rates used in the projection, which leverage the 2012 IAM Basic mortality table $q_{x}^{2012}$ with prescribed multipliers $F_{n}$ applied (depending on whether the policy has a living benefit) and Projection Scale G2 mortality improvement
$G 2_{x}$, as shown in the formula below:

$$
q_{x}^{2012+n}=q_{x}^{2012} *\left(1-G 2_{x}\right)^{n} * F_{n}
$$

VM-21 Section 6.C.3.h specifies the mortality assumptions for the Guarantee Actuarial Present Value (GAPV) calculation:

$$
q_{x}^{2012+n}=q_{x}^{2012} *\left(1-G 2_{x}\right)^{n}
$$

The differences in the mortality assumption between the projection and GAPV are summarized in the table below:

| Notation | Description | Projection | GAPV |
| :---: | :--- | :--- | :--- |
| $q_{x}^{2012}$ | 2012 IAM Basic Mortality Table | Used in the same way, as the base mortality rate |  |
| $G 2_{x}$ | Mortality improvement from <br> Projection Scale G2 | No end date to the <br> mortality improvement | Only improved to Dec. <br> 31,2017 |
| $F_{n}$ | Mortality multiplier by GLB or <br> no-GLB. | Used as the mortality <br> multiplier | Not applicable |

For projection systems that currently do not support different projected mortality experience based on different aspects of the calculation, some actuaries may determine that the projection of mortality improvement beyond 2017 does not materially impact the results and therefore become comfortable with a modeling simplification for the prescribed mortality assumption in the GAPV calculation. Actuaries may wish to consider documenting such a simplification in accordance with VM-31 Section 3.F.2.e.

## Q 2.6: What are some potential methods for quantifying the impact of aggregation in the Standard Projection (per VM-21 Section 6.A.1.a)?

A: VM-21 Section 6.A.1.a provides a guidance note for both CSMP and CTEPA methods.

The guidance note suggests calculating GPVAD at both the model point level and the aggregate level using the aggregate GPVAD year for both, with the difference ascribed to the impact of aggregation.

$$
\sum G P V A D_{\text {policy }}-G P V A D_{\text {Aggregate }}
$$

Some actuaries believe the calculation of the GPVAD at the model point level may require a separate process, which may be challenging for some existing projection systems. If an actuary plans to use a different method from the guidance note, the guidance note in VM-21 Section 6.A.1.a states that they should discuss that method with their domiciliary commissioner.

Other actuaries might calculate the present value of net liabilities for each model point. The impact of aggregation would then be defined as:

$$
\sum \max (C S V, P V \text { of Net Liab })-\sum P V \text { of Net Liab }
$$

Under this illustrative approach, the present value of net liabilities calculation would follow the assumptions and discount rate noted in the guidance note. As noted above, this method (or any other method other than that described in the guidance note) should be discussed with the domiciliary commissioner.

The guidance note does not specify how quantities that are not calculated at the model point (or contract level) should be reflected in the model point calculations (e.g., investment income or aggregate reinsurance cash flows). Given that business is usually managed at the portfolio level, some actuaries might apply the earned rates from the aggregate projection to all model points or allocate aggregate investment income based on projected model point assets. Depending on the investment strategy, other actuaries may proxy the earned rate in the model point calculations using simplifications (e.g., a rolling average of the initial portfolio earned rates and new money rates). For cash flows that are only determined in aggregate, some actuaries might allocate the cash flows for the block to the model points in that block based on an identified driver. Depending on the nature and materiality of the cash flows, other actuaries may omit the aggregate cash flows from both the model point and aggregate calculations as a simplification. The actuary may wish to consider aligning with the treatment of aggregate calculations in both projections to support a reasonable estimate of aggregation benefits.

VM-31 Section 3.F.12.m requires documentation of the methods used to determine the aggregation impact.

## Q 2.7: What if the actuary cannot identify a Standard Projection Path A under the CSMP method?

A: If Path $A$ is not initially identified, Section 6.B.3.a.iv requires the actuary to identify a new Path $A$. If additional scenarios are needed, VM-21 Sections 6.B.6.a and 6.B.6.b specify how the equity return and interest rate scenarios would be incrementally expanded.

After each additional equity return and/or interest rate scenario is generated and the associated Scenario Reserves calculated under the CSMP method, Section 6.B.3.a.iii requires the actuary to determine whether a Path A can now be identified from the newly expanded Company Standard Projection Set. If not, the expansion process should be repeated until such a Path $A$ is found.

In practice, some actuaries might choose to automate this identification process for production purposes. One way to do this is to use an expanded range of scenarios from the outset in order to lower the risk of not identifying a Path $A$ during the iterative process.

## Q 2.8: What are some potential methods for alleviating the run-time challenges associated with the Withdrawal Delay Cohort Method?

A: The Withdrawal Delay Cohort Method may produce a considerable number of initial withdrawal age cohorts for each GMWB or Hybrid GMIB contract. In order to improve computational tractability and
reduce run-time, VM-21 Section 6.C.5.k allows actuaries to discard certain cohorts and use others as representative. The method for doing so is discretionary, with the proviso that the result should reasonably approximate a full-blown approach under which the company elects not to discard any initial withdrawal age cohorts, in accordance with the requirements set forth in VM-31 Section 3.F.12.h.

One such discarding method is provided in VM-21, Section 6.C.5.k, whereby for odd-numbered issue ages, the actuary may discard the initial withdrawal ages that are odd-numbered; and for evennumbered issue ages, the actuary may discard initial withdrawal ages that are even-numbered. The guidance note provided in VM-21 Section 6.C.5.k also indicates that random sampling methods may be used to assign only a small number of initial withdrawal age cohorts (and potentially a single cohort) to each contract.

Some actuaries choose to employ a method that limits the number of initial withdrawal age cohorts to a certain maximum number (or certain maximum weight), and remap the remaining cohorts to the cohorts that lie within such thresholds.

Regardless of which method is chosen, VM-31 Section 3.F.12.h requires disclosure of withdrawal age discarding approaches and discussions of their appropriateness. The actuary may wish to consider testing to ensure that the result reasonably approximates the full-blown approach outlined in VM-21 Section 6.C.5. For other considerations, actuaries may want to refer to Q 2.12.

## Q 2.9: What are some modeling considerations when using random sampling for the Withdrawal Delay Cohort Method?

A: The following is a (non-exhaustive) list of modeling considerations that could be helpful to actuaries as they implement a random sampling solution:

- Choice of random number generator.
- Choice of random number "seed," which is an input to the random number generator. (For example, some actuaries believe this seed should vary uniquely by contract and/or scenario).
- The number of cohorts to be assigned via random sampling.
- The total number of cohorts to be modeled under the full-blown approach as outlined in VM-21 Section 6.C.5.
- Number of policies or cells to which random assignments will be made.

Regardless of how the actuary chooses to address these considerations, if a random sampling solution is used, the actuary may wish to consider performing adequate testing to ensure that the result reasonably approximates the full-blown approach.

After the random sampling solution has been developed, the actuary may also wish to consider the stability of results (that is, confirming that changing the random number seed does not materially change the Standard Projection Amount) and how the random number seeds are stored in order to facilitate reproducing results at a later date.

For replication of results, the actuary may wish to consider specifying and/or storing the random
number seed in such a way that policy-level and aggregate-level results can easily be replicated for audit or other purposes.

## Q 2.10: How can a company demonstrate the appropriateness of any modeling simplifications used to address the Withdrawal Delay Cohort Method?

A: Regardless of approach, VM-31 Section 3.F.12.h requires the actuary to discuss the appropriateness of the approach. The actuary may also wish to consider VM-31 Section 3.5.2.e documentation requirements for simplifications and approximation.

Some actuaries might demonstrate the appropriateness of their simplification by running both the simplified approach and the full-blown approach for all scenarios (under either the CSMP or CTEPA methods) and comparing results. This may be considerably run-time-intensive, particularly if running the full-blown approach using (1) initial withdrawal age cohorts generated from a seriatim in-force file and (2) over a large number of stochastic economic scenarios (as might be the case under the CTEPA method).

Other actuaries might choose to obtain support for their simplified approach by running both the simplified approach and the full-blown approach for a smaller subset of scenarios. For example, under the CTEPA method, this could be carried out for select percentiles of results (such as the $85^{\text {th }}, 95^{\text {th }}$ and $99^{\text {th }}$ percentiles) to check that the shape of the distribution is similar for both approaches. Other simplified approaches that reasonably approximate a full-blown approach would also be acceptable.

## Q 2.11: For the CTEPA method, do companies generate the initial withdrawal age cohorts based on a model office or a seriatim in-force file?

A: VM-21 Section 6.B.3.b.i states that if a company uses a model office to calculate the CTE Amount, then the company may continue to use the same model office (or one that is no less granular than the model office that was used to determine the CTE Amount) for the CTEPA method, provided that the company shall maintain consistency in the grouping method used from one valuation to the next.

Some actuaries interpret this to mean that while a model office can be used to generate the initial withdrawal cohorts under the Withdrawal Delay Cohort Method, the Standard Projection Amount that is produced should not be materially lower than that which would have been obtained had the company applied the CTEPA method using a seriatim in-force file to generate the cohorts, in accordance with the language in VM-31 Section 2.F.2.f.

## Q 2.12: How should the never-elect withdrawal cohort be treated when discarding cohorts with initial withdrawal ages prior to the valuation date?

A: Some actuaries believe that the weight for the never-elect withdrawal cohort should be rescaled so that its weight after rescaling may be different from the prescribed weight (as outlined in VM-21 Section 6.C.5.m) after discarding cohorts with initial withdrawal ages prior to the valuation date and rescaling
the remaining withdrawal curve.

Q 2.13: For GMWB or Hybrid GMIB contracts, if the company calculates a terminal claim at the end of the projection period (and assuming the account value has not yet been depleted), should a partial withdrawal utilization scalar be applied to this lump sum value?

A: The instructions in VM-21 Section 6.C.4.g through Section 6.C.4.j indicates that a partial withdrawal scalar of $90 \%$ (Lifetime GMWB or Hybrid GMIB) or 70\% (non-Lifetime GMWB) applies to the projected partial withdrawal amount, assuming the account value has not been depleted. VM-21 Section 6.C.4.f states that if the account value has been depleted, a scalar of $100 \%$ applies.

Some actuaries interpret the above to mean that at the end of the projection period, even if the account value has not yet been depleted, a partial withdrawal scalar of $100 \%$ applies to the terminal claim (because at some point beyond the projection period, the account value is likely to be depleted).

Other actuaries believe that if the account value has not yet been depleted at the end of the projection period, then a partial withdrawal scalar of either $90 \%$ (Lifetime GMWB or Hybrid GMIB) or $70 \%$ (nonLifetime GMWB) applies to the terminal claim. In this case, the actuary should be confident that the resulting reserve is not materially lower than that obtained by continuing the projection and using a partial withdrawal scalar of $100 \%$ when account values are depleted.

## Q 2.14: For an unexercised Traditional GMIB or Hybrid GMIB contract, what GMIB annuity option should be modeled under the Standard Projection for the purposes of the Annuitization GAPV calculation?

A: As there is no specific guidance regarding this in VM-21 Section 6, some actuaries believe developing a prudent estimate assumption for the annuity option is appropriate, which is in line with VM-21 Section 6.B.1, which states "where not inconsistent with the guidance given here, the process and methods used to determine the additional standard projection amount under either the CSMP method or the CTEPA method shall be the same as required in the calculation of the stochastic reserve as described in Section 3.D of these requirements."

Other actuaries believe that using the most conservative annuity option that is available under the GMIB rider is appropriate under VM-21.

Regardless of approach, the actuary may wish to consider documenting the assumption used in accordance with VM-21 Section 6.B. 1 and VM-31 Section 3.F.12.j and/or I.

## Q 2.15: Is the 2012 IAM Basic Mortality Table improved to 2017 a published table?

A: The 2012 IAM Basic Mortality Table is a published table, but there is no official publication of the table improved to 2017. The table will need to be developed from various sources. Some actuaries use
the initial report document at

https://www.actuary.org/sites/default/files/files/publications/Payout Annuity Report 09-28-11.pdf

Other actuaries may start at the SOA website:

## https://www.soa.org/resources/experience-studies/2011/2012-ind-annuity-reserving-rpt/

As well as using the Society of Actuaries Tool \& Resources Page, Mortality and Other Rate Tables located at:

## https://mort.soa.org/

Section 5 of NAIC Model Regulation 821 (NAIC Model Rule [Regulation] For Recognizing A New Annuity Mortality Table For Use In Determining Reserve Liabilities For Annuities) includes guidance on rounding. The guidance states that each mortality rate should be projected from 2012 and then rounded to three decimal places, for deaths per 1,000 . Projecting rounded rates further forward is described as incorrect. For example, the regulation states that "It is incorrect to use the already rounded $\mathrm{qx}^{2013}$ to calculate qx $x^{2014}$."

Some actuaries who follow the mechanics in Model Regulation 821 might apply mortality improvement on an annual basis and align mortality rate changes with their model's projection ages. Others might consider available modeling capabilities (e.g., from the stochastic projections) when making implementation decisions (e.g., annual vs. monthly mortality improvement or whether to align annual mortality improvement changes with policy anniversaries, policyholder birthdays, or calendar years). The actuary may wish to consider documenting their approach.

## Q 2.16: When determining the initial withdrawal curve under the Withdrawal Delay Cohort Method in

 in VM-21 Section 6.C.5, should foreknowledge of policyholder actions be taken into account? For example, assume a policy has a doubler provision that allows for a doubling of the benefit base in policy year 10 if the policyholder has not taken a withdrawal to that point. If the policyholder has already voided the doubler by taking a withdrawal before policy year 10 , should the at-issue withdrawal curve calculated under the Withdrawal Delay Cohort Method assume that the doubler is voided or should it be reflected?A: Some actuaries believe that because the derivation of the withdrawal curve under the Withdrawal Delay Cohort method is from issue, foreknowledge of policyholder actions should not be taken into account. With respect to the example provided, under this interpretation the doubler should always be reflected irrespective to actual policyholder actions.

Some actuaries believe that for policies where such actions are possible, a distinction should be introduced between policies when deriving the withdrawal curve under the Withdrawal Delay Cohort Method. With respect to the example provided, under this interpretation there would be separate withdrawal curves calculated for:

- A policy that (in reality) has not taken a withdrawal and so the doubler is reflected when deriving the withdrawal curve, and
- A policy that (in reality) has taken a withdrawal and so the doubler is not reflected when deriving the withdrawal curve.

Under this interpretation, at transition (from AG 43 to VM-21 at 1/1/2020) the actuary may choose to reflect different withdrawal curves for two existing policies A and B that are otherwise identical (from an issue age, gender, guaranteed benefit, product design, and tax status perspective) but where policy $\mathrm{A}$ has taken a withdrawal in reality and policy B has not. In addition, post-1/1/2020 if policy B decides to take a withdrawal in reality, the actuary may also choose to switch the at-issue withdrawal curve for policy $\mathrm{B}$ to match that for policy $\mathrm{A}$.

Regardless of approach, the actuary may wish to consider explicitly documenting the assumption used in accordance with VM-21 Section 6.B.1 and VM-31 Section 3.F.12.I.

## Q 2.17: How should the initial withdrawal age be determined for the GAPV calculation under the Withdrawal Delay Cohort Method in VM-21 Section 6.C.5 if withdrawals are contractually allowed but the policyholder would incur penalties at certain ages? For example, consider the case where the policyholder has started taking withdrawals and therefore incurred the penalties.

A: Some actuaries believe that if foreknowledge of policyholder actions should not be taken into account, then the penalties should not be considered either (and so the initial withdrawal age should then start from the earliest possible age allowed by the contract).

Other actuaries believe that to the extent that the actuary believes that foreknowledge of policyholder actions should considered, the penalties should similarly also be taken into account when developing the GAPVs under the Withdrawal Delay Cohort.

Other actuaries who focus on the general case (where policyholders have not taken withdrawals) might use the contractual availability of the withdrawal benefit or consider conservatism and materiality when setting the initial withdrawal age.

Regardless of approach, the actuary may wish to consider explicitly documenting the assumption used in accordance with the language in VM-21 Section 6.B. 1 and VM-31 Section 3.F.12.I.

## Q 2.18: What are some considerations for selecting the CSMP or CTEPA approach for the Standard Projection?

A: There are potential conceptual, operational, and runtime considerations.

Conceptually, the CTEPA approach provides the most direct quantification of company vs. prescribed assumption differences.

Operationally, CTEPA runs may leverage the same projection process and liability data as the stochastic reserve projection. CSMP deterministic runs and path selection may involve a separate process after the stochastic projection and may require exception handling or additional consideration if Path A cannot be
identified from the original deterministic scenario set. The seriatim CSMP runs would also require different liability data inputs if the company uses model cells for its stochastic reserve projection.

However, runtimes may be more manageable for the 40 deterministic CSMP scenarios than the potentially 1,000 (or more) CTEPA stochastic scenarios.

## 3. Asset Modeling \& Discount Rates

## Q 3.1: VM-21 allows two different methods for the calculation of the Scenario Reserve. What are the two methods, and how are they different?

A: The two methods are the NAER method described in Section 4.B. 2 and 4.B. 3 and the Direct Iteration Method (DIM) described in Section 4.B.4. The two methods can be summarized as follows:

- The NAER method includes projecting asset and liability cash flows, then discounting them at the net asset earned rate on additional assets.
- The DIM identifies the level of starting assets by projecting asset and liability cash flows to the end of the projection period, iterating as necessary until the starting assets are sufficient to fully liquidate all policy obligations, leaving zero assets at the end of any projection year.

The primary difference between the two methods is that the NAER method uses a net asset earned rate on additional assets to discount accumulated deficiencies, whereas the DIM makes direct use of asset cash flows produced by the asset-liability model.

Calculating the net asset earned rate on additional assets subject to VM-21 requirements can be complicated and may require modifications and/or approximations. Considerations may include items such as differences in the way assets are modeled, the timing of cash flows, the manner in which the model purchases and sells assets, and the treatment of non-cash items. VM-31 Section 3.F. 6 includes documentation requirements for the NAER calculations.

## Q 3.2: How may borrowing strategies be reflected, including situations where the company's borrowing and asset investment strategies differ?

A: Section 4.D.4.c of VM-21 requires the actuary to model a borrowing strategy that is reflective of the company's cost of borrowing, provided that the assumed cost of borrowing is not lower than the rate that positive asset cash flows are reinvested at during the same period considering durations, ratings, and other characteristics of the borrowing facility. A guidance note below the requirement clarifies that the intent is to prevent overly optimistic borrowing assumptions in general rather than requiring absolute compliance at each time step in every scenario.

Some actuaries believe that if it is not practical to meet the full requirements of Section 4.D.4.c, simplifications may be made to the borrowing strategy provided that they do not materially reduce the
reserve. Some actuaries may feel that a demonstration comparing reserves determined using the company's borrowing strategy against reserves determined only using asset sales would satisfy the spirit of Section 4.D.4.c if the reserve amount was not materially lower using the company's borrowing strategy.

## Q 3.3: How is the NAER applied to positive and negative accumulated deficiencies when determining the Scenario Reserve in Section 4.B.2 and 4.B.3?

A: Some actuaries interpret the Scenario Reserve to be the amount of assets needed to decease liabilities with zero accumulated deficiencies.

Suppose a company's starting asset portfolio earns 10\%, and the Additional Invested Asset Portfolio earns $5 \%$ (i.e., NAER is 5\%). If the greatest accumulated deficiency is positive, the company uses the additional assets earning $5 \%$ to cover the deficiency, so the greatest present value of accumulated deficiency (GPVAD) is determined using NAER as the discount rate.

However, if the greatest accumulated deficiency is negative, the starting asset portfolio is more than sufficient, and no additional assets are needed. Using a NAER based on the hypothetical investment of additional (positive) assets as the discount rate implicitly assumes borrowing an amount equal to the negative GPVAD at that rate. Using the rates from the prior example, scenario reserves would reflect starting assets earning $10 \%$ offset by borrowing at $5 \%$.)

Some actuaries believe that VM-21 requires discounting at the NAER, defined as the reinvestment rate, under all circumstances. Others believe that implicitly assuming borrowing would be inappropriate unless it aligns with the companies' actual management strategy and would instead use the net earned rate in the projection for discounting. That would be consistent with assuming a proportional reduction in starting assets in the Direct Iteration Method (DIM).

The actuary may wish to consider the DIM when setting the NAER because the NAER method is a simplification of the DIM and is generally expected to produce materially similar results. Actuaries may also wish to consider the different sources of additional assets, including any assets in the product portfolio that were not included in starting assets, assets outside of the product portfolio (such as those backing surplus), and assumed new assets purchased from cash infusions. When incorporating these sources, the actuary might consider the availability of assets given the asset needs of other lines of business in that scenario.

## Q 3.4: How are starting assets determined?

A: VM-21 (Section 4.D.1a) requires that "the value of assets at the start of the projection shall be set equal to the approximate value of statutory reserves at the start of the projection plus the allocated amount of PIMR attributable to the assets selected" (estimated reserves). This includes general and separate account reserves for in-scope products and productfeatures.

All in-scope separate account assets and hedge assets are included, although VM-21 Section 4.A.4.a.ii
allows the market value of the hedge assets to optionally be replaced by a equivalent amount of cash general account assets. All or a portion of the general account assets associated with products in scope are then added such that the starting assets are approximately equal to the statutory reserves plus allocated PIMR in the model as of the start of the model projection. It is possible that the amount of general account assets needed is less than zero.

VM-21 Section 4.D.1.a specifies that assets should be valued consistently with their annual statement values. In determining which assets to include and how to project those assets, the actuary may consider actuarial standards of practice, such as sections 3.3 and 3.4 in ASOP No. 7, Analysis of Life, Health, or Property/Casualty Insurer Cash Flows.

In developing an estimate for starting reserves, some actuaries might use reserves as of the last reported date. Other actuaries might use a ratio of reserve to account value where the ratio is estimated based on analysis of historical data. Others might use the DIM and solve for the required amount of assets. VM-31 Section 3.F. 4 includes documentation requirements for starting assets, including the methods used and rationale.

## Q 3.5: How close are starting assets expected to be to the actual reserves ultimately held for in-scope products?

A: There are no specific criteria for C-3 Phase 2 RBC or VM-21. Some actuaries believe that they should be reasonably certain that the level of starting assets has not resulted in a material understatement/overstatement of the actual reserve.

## Q 3.6: How is IMR for the contracts and guarantees included in VM-21?

A: VM-21 4.A. 7 requires that the IMR be handled consistently with the company's cash-flow testing methodology. Q23 of the Asset Adequacy Analysis practice note (https://www.actuary.org/sites/default/files/files/publications/Asset Adequacy PN 092517.pdf;

September 2017) provides some additional considerations on how to determine which portion of IMR can be used to support certain products. For example, if the assets and IMR are allocated by line, then one approach the actuary might consider is to use the line of business unamortized portion. If assets are not specifically allocated to support the included contracts and guarantees, some actuaries may take a pro-rata portion based on assets allocated. Other actuaries may use more refined methods that reflect a different subset of assets, as opposed to a pro-rata share, may support the subset of liabilities included in the modeling. Other actuaries may determine that allocating zero IMR is a reasonable assumption. The treatment of PIMR should be documented in accordance with VM-31 Section 3.F.4.g.

## Q 3.7: How should the actuary set assumed gross asset spreads over U.S. Treasuries for "other fixed income investments" as mentioned in VM-21 4.D.4.a.v?

A: Some actuaries may receive gross asset spreads from their investment departments or investment
advisers. Some actuaries might review the relationship of spreads received, including spreads on public non-callable bonds, to prescribed spreads to ensure the spreads for "other fixed income investments" in relation to spreads for public non-callable bonds and/or interest rate swaps is not unreasonable. Other actuaries may rely on modeling systems to solve for the spreads that equate modeled market values to actual market values at time zero.

Some actuaries may hold the initial spread over Treasuries constant for the projection while others may consider adjustments over the course of the projection (e.g., consistent with the prescribed grading from current to ultimate spreads for public non-callable bonds).

The actuary may wish to consider VM-31 Section 3.F. 6 documentation requirements if the spreads affect the modeled investment strategy or projected market values.

## Q. 3.8: What if using the VM-20 spreads results in market values that are materially different from the statement values?

A: VM-21 Section 4.D.1.a states that starting asset values need to be consistent with their annual statement values, and that assets purchased during a projection, which can occur as early as the first time step in a projection, need to be valued in a manner consistent with the value of assets at the start of the projection that have similar investment characteristics (Section 4.D.2).

VM-21 Section 4.D.4.iii prescribes spreads for non-callable corporate bonds that reflect current market conditions as of the projection start date and grade to long-term conditions based on historical data.

However, these "generic" spreads by credit rating and weighted average life may not necessarily reproduce the market values for the individual securities reported in the statutory statements. Some actuaries will add/subtract a security-specific spread to each starting asset so that the market values validate at the projection start date. These actuaries might hold such spread constant for the duration of the asset or grade them off over time.

## 4. Scenarios

## Q 4.1: What are some considerations for a company using scenario stratification or reduction techniques?

A: Although the previous equity calibration criteria in AG 43, Appendix 5 are no longer included in VM21 , they are consistent with the prescribed scenario generator and the actuary may wish to consider using these as a reference. Although never formally adopted, proposed interest rate calibration criteria in the Academy's Economic Scenario Work Group's December 2008 report to the NAIC may also be informative. The actuary may also wish to consider the scenario reduction principles in the prior version of AG 43, Appendix 5.

Note that VM-31, Sections F.9.c and d require documentation of the rationale used to select the number of scenarios and any scenario reduction technique and that the approach does not materially understate reserves.

Periodic testing, perhaps with a representative or simplified model, might be considered to confirm that results with a stratified set of scenarios are sufficiently close to results from the full set of scenarios and do not materially understate reserves.

The actuary may wish to consider the discussion on scenarios in Section 6 of the March 2011 practice note, The Application of C-3 Phase II and Actuarial Guideline XLIII (https://www.actuary.org/sites/default/files/files/VAPN\ FINAL\ WEB\ 040511.4.pdf/VAPN\ FI NAL\%20WEB\%20040511.4.pdf).

Note that that considerations for VM-20 and VM-21 may differ. VM-21, Section 8.E allows the use of non-prescribed generators, so scenario stratification or reduction techniques may be applied to either prescribed or non-prescribed scenarios. VM-21 Section 8.E also allows non-prescribed scenario reduction or stratification approaches while VM-20, Section 7.G.2.c prescribes the use of the scenario picker embedded in the prescribed scenario generator. For VA products, the actuary may wish to consider approaches that reflect factors other than the purely interest rate-driven scenario picker tool.

## Q 4.2: How may the change in CTE level from CTE 90 to CTE 98 affect the determination of the number of scenarios?

A: Question 6.4 of the March 2011 practice note, The Application of C-3 Phase II and Actuarial Guideline XLIII, introduced the Variance of the CTE Estimator as a metric to examine when assessing the number of scenarios. All else being equal, additional scenarios would generally be needed to maintain a similar level of variance between CTE98 and CTE90 TAR. However, the new C-3 Phase 2 RBC requirement is 25\% of the excess of CTE 98 over reserves, and the $25 \%$ factor may reduce the variance of the relevant C-3 Phase 2 amounts by a factor of 16 . The actuary may wish to consider whether the $25 \%$ factor would reduce the variance of RBC using the CTE 98-based metric below that of the former CTE 90 metric.

## Q 4.3: How might one use the variance of the CTE estimator in determining the CTE reserve and RBC amounts?

A: The variance of the CTE estimator is a measure of the sampling error attributable to the stochastic scenarios. This measure may be used to assist the actuary in determining whether additional scenario analysis is warranted.

Some actuaries believe the variance by itself provides limited insights whereas comparing it to the CTE measure provides information regarding dispersion. One can take the standard deviation of the CTE estimator and divide it by the CTE measure to obtain a "relative error" (or coefficient of variation). This may be viewed as a measure of the dispersion of the accumulated deficiencies around the CTE measure.

Assume Block A has a CTE 98 measure of $\$ 2,000$ with an estimated CTE 98 variance of $\$ 10,000$, and Block B has a CTE 98 of $\$ 250$ and estimated CTE variance 98 of $\$ 10,000$. Calculating the dispersion relative to the CTE yields $5 \%$ for Block A (square root of $\$ 10,000$ divided by $\$ 2,000$ ) and $40 \%$ for Block B. Although the blocks have the same dollar amount of dispersion about the CTE 98 measure, Block B has a much higher relative dispersion.

If the actuary believes the dispersion is high relative to the mean, the actuary might consider conducting further testing. Note that a high relative dispersion does not mean that the CTE amount is too high or too low. For example, assume Block $C$ has a CTE 70 of $\$ 2,000,000$ and a square root of the variance of the CTE 70 measure of $\$ 500,000$ across 1,000 stochastic scenarios. The relative error is $25 \%$. Additionally, assume that only 50 of the 1,000 scenarios had deficiencies. If the actuary were to run 2,000 scenarios and the deficiencies in such scenarios had roughly the same magnitude and slope as that in the 1,000 scenarios (in this example 100 deficiencies with a magnitude and slope similar to that of the 50 scenarios), the CTE 70 metric would change very little. However, the variance of the CTE would likely drop significantly as the number of scenarios have doubled. The point is that a high variance or relative error may suggest the need for further testing. It does not necessarily mean the CTE measure needs to be adjusted or recalculated.

If the actuary determines that additional scenario analysis is needed, such analysis might include some of the following:

- Reviewing the tail scenarios to see whether they adequately capture the product risks
- Running a different set of scenarios
- Running a larger set of scenarios
- Employing variance reduction techniques (e.g., control variate method)

Some actuaries have observed the following with respect to their blocks of variable annuities with guaranteed living and death benefits. Such observations may or may not be indicative of other blocks of variable annuities.

- Deep in-the-money guaranteed living and death benefits-Many scenarios in the CTE tail with deficiencies. The CTE amount tends to be high and relative error tends to be low. Graphing the deficiencies shows a flatter/gentleslope.

The low relative error suggests that additional analysis regarding the scenarios may not be needed. However, one may decide to conduct additional analysis depending on the materiality of the estimated standard deviation relative to the overall company results.

- Deep out-of-the-money guaranteed living and death benefits-Fewer scenarios in the CTE tail with deficiencies. A low CTE amount with a high relative error. Graphing the deficiencies shows a steeper slope.

The high relative error suggests that additional analysis may be warranted. However, the low CTE amount relative to the block of business may not be material. In an extreme case where there are no scenarios with deficiencies in the CTE measure, the actuary may explore what scenario returns would be needed to produce deficiencies.

Additional information regarding the variance metric as well as some practical approaches to its use can be found in the paper "Variance of the CTE Estimator" by B. John Manistre FSA, FCIA and Geoffrey H. Hancock FSA, FCIA.

## 5. Hedging

## Q 5.1: What are some considerations for determining the E-Factor when there is a strategy change?

A: The guidance note in Section 9.C. 7 provides some examples and guidance in determining the E-Factor when there has been a change in the hedge program.

Additional examples might include the following:

- The company was dynamically hedging S\&P and NASDAQ delta but decides to only dynamically hedge S\&P delta. Here, the E-Factor could increase or decrease depending on factors such as how well the model replicates S\&P versus NASDAQ hedging.
- The company was dynamically hedging S\&P delta and decides to hedge the NASDAQ delta as well. Some actuaries believe that the E-Factor, at least initially, should not decrease and could perhaps be increased given uncertainties in the newly modeled hedging.
- The company replaces its dynamic daily hedge with a dynamic weekly hedge. The company models hedge cash flows directly (explicit method) with monthly time steps. Some actuaries may expect the E-Factor to increase as one may expect more hedge breakage when moving to weekly hedging.

Regardless of the expectation, the actuary should document the approach and rationale for the E-factor per VM-31 Section 3.F.8.e and may also wish consider whether back-testing (even on a pro-forma basis) is necessary to support $\mathrm{E}$-factor changes.

## Q 5.2: How has the E-Factor changed with the 2020 Valuation Manual?

A: The formula that utilizes the E-Factor is now the same for both reserves and RBC, and it is an "error" factor. VM-21 Section 9.C adopts the E-Factor formula previously used for C-3 Phase 2 RBC, and the revised C-3 Phase 2 instructions requires the use of the same methods and processes as VM-21.

Section 9.C. 5 requires the company to support the E-Factor by conducting a formal back-test based on analysis of at least the most recent 12 months. " $E$ " is subject to an absolute minimum of $5 \%$ and may be higher to reflect the amount of experience available if a company does not have 12 months of experience to date. The E-Factor shall be determined at least once each year.

Companies that do not have a CDHS no longer need an E-Factor.

## Q 5.3: What back-testing methods can a company use to support the E-Factor?

A: There are three methods based on the nature of the hedge modeling, as noted in Section 9.C.6.

## Q 5.4: What are some practical considerations for back-testing an explicit method?

A: Some actuaries believe some adjustment to the historical experience is appropriate for back-testing. Because the goal is to measure how well the model matches actual results, the comparison is useful if it is performed on a consistent basis.

One example in VM-21 Section 9.C.6.a notes that in order to isolate differences in modeled and actual hedge results, the projected liabilities should reflect actual liabilities throughout the back-testing period, Therefore, adjustments that facilitate this accuracy (e.g., reflecting actual experience instead of model assumptions, including new business, etc.) are permissible.

Some actuaries believe that if hedge positions changed during the back-testing period-e.g., increased the swap position from $50 \%$ to $80 \%$-it may be reasonable to reflect the new position in both the actual experience and the modeled hedge strategy by adjusting the gains/losses.

## Q 5.5: If a company has a CDHS, is back-testing required if the expected costs and benefits of future

 hedge positions produce CTE 70 (best efforts) in excess of CTE(adjusted)?A: Some actuaries believe that back-testing to support the E-Factor is unnecessary in this situation because reserves would not depend on the E-Factor (the second term in the formula reduces to $\$ 0$ ). Other actuaries would continue to back-test because the relationship between best efforts and adjusted might reverse at another CTE level or vary depending on initial market conditions, making the E-Factor applicable.

## Q 5.6: SSAP 108, Paragraph 16 states that "the amortization timeframe shall equal the Macaulay duration of the guarantee benefit cash flows based on the VM-21 Standard Scenario, but shall not exceed a period of 10 years." How is the amortization period calculated now that the Standard Projection is not based on a single deterministic scenario?

A: Some actuaries may consider the Macaulay durations for the cash flows from the deterministic scenarios selected as Path A and Path B under the CSMP method or the scenario used for Standard Projection disclosures under the CTEPA method. Under this approach, if durations for both CSMP scenarios exceed 10 years, the actuary may set the amortization period to 10 years in accordance with the requirements of SSAP 108. Other actuaries may consider interpolation approaches such as the process used to calculate the Prescribed Projection Amount.

## Q 5.7: What types of hedge target changes would require notification of the domiciliary state commission under SSAP 108, Paragraph 8?

A: Paragraph 8 of SSAP 108 states:

"While an initially documented hedging strategy may subsequently change, any change in hedging strategy, which includes a change in hedge target, shall be documented, with notification to the domiciliary state commissioner, and include an effective date of the change in strategy. Reporting entities that elect to change a documented hedging strategy prior to the end of the three-month minimum implementation timeframe shall identify the hedging strategy, and all hedging instruments executed under the strategy, as ineffective. The three-month timeframe begins with the stated effective date of the hedging strategy regardless if any hedging instruments have been executed under the hedging strategy. Changes in a documented hedging strategy that occur after the threemonth implementation timeframe do not necessitate an ineffective determination as long as hedged items and hedging instruments under the revised/new strategy continue to meet the requirements of a highly effective fair value hedge. Reporting entities are permitted to have more than one hedging strategy implemented, but all implemented strategies must qualify as a component of a Clearly Defined Hedging Strategy pursuant to paragraph 7."

Footnote 4, in paragraph 7, clarifies that the three-month minimum implementation timeframe may be met "by having evaluated the effective implementation of the hedging strategy for at least three months without actually having executed the trades indicated by the hedging strategy (e.g., mock testing or by having effectively implemented the strategy with similar annuity products for at least three months.)"

Together with the fact that more than one hedging strategy may be "implemented," notification may not be required during the testing period during which another strategy is still being executed. Notifications might generally occur upon changes in the documented strategy. A minor change in hedge target calculation, such as one based on practicability considerations mentioned in SSAP 100R and in the response to Question 5.8, may not require notification. However, the expectations of state regulators may differ, so actuaries might wish to consider providing notification of even minor changes, perhaps noting the minor nature of the change.

## Q. 5.8: What are some potential considerations for SSAP 108 if the hedge target basis differs from fair value?

A: Some actuaries believe that a hedge target that is conceptually a fair value but may not strictly comply with every element of the SSAP 100R definition of fair value may still be acceptable for SSAP 108 purposes. Because the key use of liability fair values in SSAP 108 is to allocate changes in values to hedged and unhedged elements, some variations in definitional terms, consistently applied, may have limited impact on the allocation, and practicability considerations (i.e., consideration of excessive costs) are allowed. If the hedge target basis differs significantly from a fair value, some actuaries might use a fair value framework, rather than the hedge target basis, to determine the allocations.

## Q. 5.9: What are the advantages and disadvantages of explicit and implicit hedge modeling?

A: Explicit Method-In this method, hedging positions and cash flows are included in the stochastic cash flow model used to determine the scenario reserve.

## Advantages

- May be applied to any hedging strategy, including full or partial strategies and strategies that include sales, purchase, or rebalancing decisions.
- May be necessary to reflect the impact of complex hedging strategies and/or instruments.
- Projecting hedge cash flows and market values for each scenario and projection period may provide a better understanding of hedging costs and benefits, liquidity needs, and internal or external hedge limits.
- May be able to justify a lower " $E$ " factor than an implicit approach.


## Disadvantages

- May be computationally challenging (e.g., potentially involving stochastic-on-stochastic modeling for strategies that target liability "greeks")
- Modeling simplifications to make the projections tractable may limit the reflection of "real life" dynamics and risks (e.g., lagged data, less frequent projection steps or rebalancing, simplified assets, simplified assumptions for implied volatility).
- May not produce a materially different result than a simpler approach for small or simple hedging strategies.

Implicit Method-In this method, the impact of the hedging program is evaluated outside of the stochastic cash flow model and reflected as an adjustment to the stochastic reserve.

## Advantages

- Less complex and simpler to implement than the explicit method.
- Explanations and attributions of impacts may be easier.
- May be adequate for simple strategies.


## Disadvantages

- Does not provide cash flow information or insights about liquidity, hedge limits, hedge breakage, or other dynamics (e.g., reinvestment spreads).
- May be more difficult to justify a low " $\mathrm{E}$ " factor.
- May be difficult to reflect partial hedging, particularly if coverage ratios are not constant.

Note that companies may employ a combination of both methods (e.g., for different hedging programs)

## 6. C-3 Phase 2 RBC

Q 6.1: The second term in the Macro Tax Adjustment (MTA) formula, (Statutory Reserve - Tax Reserve)x Federal Income Tax Rate, has a limit equal to "the portion of the company's non-admitted deferredtax assets (DTA) attributable to the same portfolio of contracts to which VM-21 is applied in calculating statutory reserves." What does this mean?

A: The second term recognizes the economic benefits of non-admitted DTA as an offset to CTE 98 TAR. While the term only references reserves, some actuaries believe that the limit includes all sources of nonadmitted DTA attributed to VM-21 contracts, including those from statutory and tax asset and reserve differences, DAC tax, net operating loss carryforwards, and other such timing differences.

For example, suppose a company's only DTA is from a $\$ 10$ statutory to tax reserve difference and that only $30 \%$ of the difference has been admitted at a $21 \%$ tax rate. The total DTA is $\$ 10 \times 21 \%=\$ 2.1$, with $30 \%$ of the $\$ 2.1=\$ 0.63$ admitted and $70 \%$ of the $\$ 2.1=\$ 1.47$ inon-admitted. In this example, the second term in the MTA RBC formula would be limited to $\$ 1.47$ million, the amount not already recognized in statutory statements.

## Q 6.2: Which tax adjustments may be reflected in the Specific Tax Recognition (STR) formula?

A: The impact of taxes attributable to contracts subject to VM-21 is reflected in the "CTEAT (98)" term. Some actuaries believe that the instructions "to reflect the effect of Federal Income Tax" includes consideration of both temporary and permanent timing differences. In the case of temporary timing differences, the actuary may need to be careful not to reflect any timing differences that are included in the admitted DTA.

Temporary timing differences may include, but not be limited to, such items as statutory reserve and tax reserve differences, statutory asset and tax asset differences, DAC tax, Net Operating Loss carryforwards, and other items allocated to the contracts subject to VM-21.

Permanent timing differences may include, but not be limited to, such items such as Dividend Received Deduction (DRD) and tax-exempt interest.

Some actuaries might also limit the impact of tax benefits if they do not believe the company could realize the tax benefits assumed in all the stochasticscenarios.

Q 6.3: Do the VM-21 / C-3 Phase 2 revisions change the contracts subject to C-3 Phase 2 RBC?

A: When C-3 Phase 2 was originally implemented, it applied to all contracts (regardless of issue date) while AG43 followed CARVM as defined in the NAIC Model Standard Valuation Law and included contracts issued on or after January 1, 1981.

Some actuaries note that the 2020 RBC instructions explicitly state that the calculations apply to contracts valued following the "requirements of AG43 and VM-21" and believe that C-3 Phase 2 RBC requirements now apply only to contracts subject to AG43 / VM-21.

Other actuaries believe that the 2020 changes modify the mechanics of the C-3 Phase 2 RBC projections (e.g., using $25 \%$ of CTE 98 instead of CTE 90 anytime stochastic projections apply) but do not narrow the contracts that are in scope.

In practice, some companies with immaterial pre-1981 in-force blocks may align the contracts included

in the projections (e.g., including pre-1981 business in AG43 or excluding pre-1981 business from C-3 Phase 2 RBC) as an operational simplification. Companies with material pre-1981 in-force blocks may wish to consider seeking additional guidance from their domiciliary commissioner.

## 7. Disclosures

## Q 7.1: How are fair values defined and calculated for VM-21, Section 9.D and VM-31, Section 3.F.8.g?

A: Companies reflecting a CDHS are required to calculate and compare the "fair value of the portfolio of contracts" to both CTE 70 (Best Efforts) and CTE 70 (Adjusted) before the cash surrender value floor. However, neither VM-21 nor VM-31 specify how full contract fair values should be calculated.

SSAP No. 100R contains the statutory definition of fair value used in the reporting of other assets and liabilities. The statutory accounting fair value definition ("the price that would be received to sell an asset or paid to transfer a liability in an orderly transaction between market participants at the measurement date") follows U.S. GAAP FAS 157 with certain notable exceptions. The primary modification is the exclusion of consideration of non-performance risk (own credit risk). Paragraph 57 of SSAP 100R states that "the consideration of own credit risk in the measurement of fair value liabilities is inconsistent with the statutory accounting concept of conservatism and the assessment of financial solvency for insurers." However, some actuaries believe that this modification may cause values to deviate from the fair value definition while others believe that some reflection of the credit risk of the purchaser of the liability, which may be similar to their own credit risk, may be appropriate.

SSAP 100R allows for practicability, e.g., considerations of the cost of estimating fair value, materiality, and the required precision of estimates.

Under U.S. GAAP, certain variable annuity guarantees have historically been considered embedded derivatives under FAS 133 (ASC 815) and subject to fair value accounting. Some actuaries may refer to

FAS 157 (ASC 820), the U.S. GAAP fair value guidance, and extend those principles to full contract cash flows. As noted in the American Academy of Actuaries' FAS 157 and FAS 159 practice note, (http://dev.actuary.org/files/publications/practice note that discusses the application of FAS $157 \mathrm{a}$ nd FAS 159 to life insurance feb2009.pdf; February 2009), risk-neutral valuations are a common approach for fair-valuing variable annuity guarantees that are embedded derivatives.

Some actuaries believe that fair values calculated without the FAS 157 adjustments for nonperformance risk and/or market participant risk margins may be more relevant for the disclosure comparison. Others might consider leveraging (1) their hedge target scenarios and methodologies if the hedging program is based on some type of fair value metric or (2) calculations performed for SSAP No. 108 (Derivatives Hedging Variable Annuity Guarantees). Some might also consider adjustments for implied vs. realized equity volatility differences.

## Q 7.2: How is the cumulative decrement projection for VM-31, Section 3.F.12.b.ii (CSMP method) or Section 3.F.12.c.ii (CTEPA method) calculated? What are some potential considerations?

A: VM-31, Section 3.F. 12 requires the disclosure of cumulative decrements using Standard Projection assumptions and the company's prudent estimate assumptions. Companies using the CSMP method will use Path A (as described in VM-21 Section 6.B.2.a) while companies using the CTEPA method will select the scenario whose value is closest to the CTE 70 (adjusted). Each cumulative decrement projection "shall include, at the end of each projection year, the projected proportion (expressed as a percent of the total projected account value) of persisting contracts, as well as the allocation of projected decrements across death, full surrender, account value depletion, elective annuitization, and other benefit election."

VM-31 does not specify a method for deriving the cumulative decrements or the allocation of projected decrements, although it does reference an account value basis. Some actuaries might use projected end of period account values (AVs) and the AV released for each type of decrement. Given market and AV changes during each period, decrement rates may be derived for each period, and then cumulative rates may be calculated from the per period rates. Other actuaries might also consider AV growth, AVs before the decrements, and/or the timing of decrements when approximating AV levels in the decrement rates.

Other actuaries question whether such an account value-based calculation will be fully representative of policyholder behavior. For example, account value depletion (i.e., instances of living benefit claims) may be under-represented because account values before depletion are, by definition, low. To a lesser extent, the AV-weighted full surrender rates may also mask the presence or significance of low dynamic lapse rates for deep-in-the-money contracts if the projected in-force includes a mix of business at different durations or moneyness levels. A counts-based cumulative decrement disclosure or countsbased view of account value depletion may provide additional insights about projected policyholder behavior, but such additional information is not required.

Given the potential limitations of any given approach, the actuary may wish to consider performing additional review of results and monitoring emerging practices.

The actuary may wish to consider documenting the cumulative decrement approach and consistently applying it to the projections using the Standard Projection assumptions and the company's prudent estimate assumptions to maintain comparability and facilitate interpretations.

Q 7.3: VM-21, Section 12 states that "the excess of the aggregate reserve over the aggregate cash surrender value shall be allocated to each contract based on a measure of the risk of that product relative to its cash surrender value in the context of the company's in-force contracts. The measure of risk should consider the impact of risk mitigation programs, including hedge programs and reinsurance, that would affect the risk of the product. The specific method of assessing that risk and how it contributes to the company's aggregate reserve shall be defined by the company. The method should provide for an equitable allocation based on risk analysis." What are potential methods for allocating reserves to the contract level?

A: The principle-based approach in VM-21, Section 12 allows for a range of approaches based on the actuary's risk analysis.

One theoretical approach would be to use accumulated contract level cash flows with allocations of aggregate reinsurance or hedging cash flows (if applicable) from the stochastic projections or the singlescenario cumulative decrement disclosure.

Some actuaries believe practical expedients may also lead to reasonable allocations. For example:

- Using the contract-level accumulated deficiencies from the Standard Projection impact of aggregation disclosure (see Q2.8);
- Using available seriatim metrics for the benefits that may drive stochastic results (e.g., present value of living benefit claims, FAS 133 liabilities, GAPV amounts); or
- Not explicitly adjusting for reinsurance or hedging programs if their impacts are likely to be roughly in proportion to the underlying metric being used.

Some actuaries believe that reinsurance may be considered only when allocating the post-reinsurance ceded aggregate reserve but not when allocating the pre-reinsurance ceded aggregate reserve in VM21, Section 5. Other actuaries may be concerned about allocation inconsistencies and/or interpret the VM-21, Section 12 requirement to consider risk mitigation programs as suggesting a common allocation, i.e., including reinsurance, for when allocating both pre-and post-reinsurance ceded aggregate reserves.

VM-31, Section 3.F.13.a requires the actuary to document their selected allocation basis.

Q 7.4: Is there a required "as of" date for the annual disclosures and other VM-21 testing (e.g., use of seriatim vs. modeled cells for Standard Projection, demonstrating that non-prescribed scenario results are not materially less than results under the prescribed scenarios)?

A: Neither VM-21 nor VM-31 specify an "as of" date for the annual disclosures or testing. Some actuaries might extend VM-31 guidance on the use of prior dates or simplifications to the disclosure calculations and use results as of a prior date (with adjustments, as appropriate) if it would not materially change the disclosed quantities or relationships. For example:

VM-31, Section F.2.e:

"Approximations and Simplifications-Description of any approximations and simplifications used in cash flow projection calculations and not described in a different section of this report, including documentation that these did not materially reduce the resulting reserve."

VM-31, Section F.12.e:

"Prior Date-If the additional standard projection amount was developed as of a date prior to the valuation date, disclosure of the prior date, the additional standard projection amount of the in-force on the prior date, and an explanation of why the use of such a date will not produce a material change in the results compared to if the results were based on the valuation date. Such an explanation shall describe the process that the qualified actuary used to determine the adjustment, the amount of the adjustment, and the rationale for why the adjustment is appropriate."

## Q.7.5: Are the VM-31 disclosures and tests annual or ongoing (i.e., quarterly) requirements?

A: Because the VM-31 PBR Actuarial Report is a yearly report, some actuaries may view the VM-31 disclosures as annual requirements. However, they may wish to consider whether to perform more frequent analysis or disclosures if, for example, changes are made during the year (e.g., model or assumption updates, asset strategy changes, markets, in-force composition) that might materially affect results.

## Q.7.6: How does the Standard Projection impact of aggregation disclosure relate to cell compression testing?

A: The two requirements are separate and distinct.

- VM-21 Section 6.A.1.a and VM-31 Section F.12.m require all companies, regardless of whether they are using seriatim in-force or model cells, to quantify and disclose the impact of aggregation in the Standard Projection. This measures economic risk offsets between business with sufficiencies and deficiencies.
- VM-31 Section F.2.f requires companies that use a compressed liability model to state that the compression method does not intentionally understate reserves and to provide auditable information to the domiciliary commissioner (upon request) demonstrating that the model cells do not materially understate reserves. This compression validation is a test of a modeling simplification/limitation.


## 8. Miscellaneous / Other

Q 8.1: How should the general account payout phase (e.g., from annuitization or living benefit claims) be reflected in the stochastic projections once the benefit is exercised? What are the considerations for using VM-21 or VM-22 for reporting contracts in the payout phase?

A: Some actuaries apply VM-22 mechanics because in principle, the benefits, risks, and their management are identical to payout annuities. Other actuaries continue to include the benefits within the VM-21 projection.

The actuary may wish to consider documenting their rationale and consistently applying their selected approach. They may also monitor emerging actuarial practice in this area (e.g., as more contracts reach this phase) and reserve/capital requirements.

## Q 8.2: How should the general account payout phase (e.g., from annuitization or living benefit claims)

 be reflected in the stochastic projections before the benefit is exercised?A: VM-21 Section 4.E.2.a states that projected GMIB and GMWB claims either (1) should be modeled as a surrender with the a reserve amount consistent with guidance for fixed payout annuity benefits (e.g., VM-22) or (2) the guaranteed cash flows from GMWB/GMIB claims are to be included in the modeled cashflows when due.

Some actuaries believe that the computation of reserves for projected claims in the stochastic model under method 1 would consider how the benefits arising from the variable annuity will actually be reserved when exercised. For example, if upon GMIB annuitization, the company uses a formulaic calculation with prescribed mortality and VM-22 interest rates, the stochastic model should reflect a projection of VM-22 interest rates.

Note that for the Additional Standard Projection Amount, the annuitization rate for contracts that do not have a GMIB shall be $0 \%$ (Section 6.7.a).

## Q 8.3: How are variable payout annuities included in VM-21?

A: Practices may vary based on considerations such as whether the contracts contain floor guarantees, payout status, and stochastic vs. Standard Projection requirements.

(1) Contracts with floor guarantees

Some actuaries might include contracts currently in the payout phase in both the stochastic reserve and the Standard Projection Amount (SPA) in order to reflect the potential impact of guarantees.

Some actuaries might also include contracts projected to annuitize in the future. However, stochastic and Standard Projection modeling may differ based on the 0\% Standard Projection annuitization assumption (except for GMIBs).

## Contracts without floor guarantees

Some actuaries might include contracts currently in the payout phase in the stochastic modeling, while others might model/address them separately to avoid modeling complexity or based on materiality. Some actuaries believe explicit stochastic modeling might not be required if the associated statutory reserve can be documented as conservative (e.g., asset fees exceed moderately adverse mortality losses and expenses) or if additional amounts are included to maintain conservatism and the intent of VM-21.

Some actuaries may also include contracts projected to annuitize in the future in the stochastic modeling although the contracts may continue to be projected or modeled as surrenders at time of annuitization. Stochastic and Standard Projection modeling may differ based on the 0\% Standard Projection annuitization assumption (except for GMIBs).


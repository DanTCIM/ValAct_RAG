## Annuity Principle-Based Reserves Under VM-22

September 28, 2026

Developed by

the Life Practice Council's Annuity Reserves and Capital Subcommittee, Variable Annuity Reserves and Capital Subcommittee, and Life Investment and Capital Adequacy Committee

<!-- image -->

This practice note is not a promulgation of the Actuarial Standards Board, is not an actuarial standard of practice, is not binding upon any actuary, and is not a definitive statement as to what constitutes generally accepted practice in the area Annuity Reserves and Capital Subcommittee, Variable Annuity Reserves and Capital Subcommittee, and Life Investment and Capital Adequacy Committee of the American Academy of Actuaries under discussion. Events occurring subsequent to this publication of the practice note may make some of the practices described in this practice note irrelevant or obsolete.

Annuity Reserves and Capital Reserve Subcommittee, Variable Annuity Reserves and Capital Subcommittee, and Life Investment and Capital Adequacy Committee

Ricky Trachtman, MAAA, FSA, Chair

Chris Conrad, MAAA, FSA Brent Dooley, MAAA, FSA Bruce Friedland, MAAA, FSA Simon Gervais, MAAA, FSA Stephen Krupa, MAAA, FSA Zi Xiang Low, MAAA, FSA, FIA Zohair Motiwalla, MAAA, FSA Amanda Muhlbaier, MAAA, FSA Sam Su, MAAA, FSA, CERA Jonah von der Embse, MAAA, FSA, CERA Thomas Wurfel, MAAA, FSA

<!-- image -->

1850 M Street NW, Suite 300Washington, DC 20036-5805

| Table of Contents                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Introduction ................................................................................................................................................. 3 |
| 1. Exemptions, Transition Rules, and Details on Products Covered ....................................................... 6                                       |
| 2. Available Information on Common Practice ...................................................................................... 10                            |
| 3. VM-22 Calculation ................................................................................................................................ 12         |
| 4. VM-22 Calculation Overview-Part A. Stochastic Reserve .............................................................. 17                                       |
| 5. VM-22 Calculation Overview-Part B. Deterministic Reserve ......................................................... 21                                         |
| 6. Standard Projection Amount ............................................................................................................... 22                 |
| 7. Stochastic Exclusion Test and Single Scenario Test ........................................................................... 26                             |
| 8. Difference From Cash Flow Testing-Scenario Reserve Calculation ............................................... 30                                             |
| 9. Considerations When Performing Reserve Calculations on Other Than the Valuation Date ........ 33                                                              |
| 10. Details on Starting Assets and Asset Modeling ................................................................................. 36                           |
| 11. Details on Scenarios / Scenario Generators / Economic Assumptions ............................................ 54                                            |
| 12. Setting Prudent Estimate and Anticipated Experience Assumptions ............................................. 60                                             |
| 13. Setting Margins .................................................................................................................................... 66      |
| 14. Setting Mortality Assumptions ........................................................................................................... 72                 |
| 15. Setting Contract Holder Behavior Assumptions for the DR/SR ..................................................... 75                                          |
| 16. Setting Expense Assumptions ............................................................................................................. 78                 |
| 17. Setting Non-Guaranteed Element Assumptions ............................................................................... 81                                |
| 18. Treatment of Reinsurance .................................................................................................................. 84               |
| 19. Treatment of Hedging / Derivative Programs ................................................................................... 87                            |
| 20. Disclosures ............................................................................................................................................ 92  |

## Introduction

This practice note was prepared by the Annuity Reserves and Capital Subcommittee, Variable Annuity Reserves and Capital Subcommittee, and Life Investment and Capital Adequacy Committee of the American Academy of Actuaries to provide information to actuaries on current and emerging practices concerning principle-based non-variable annuity reserve valuation practices for nonvariable annuity products. It is intended to supplement the available actuarial literature in the area under discussion. Actuaries are not in any way bound to comply with practice notes or to conform their work to the practices described in practice notes.

The practices here represent the views of actuaries in industry, consulting, and public accounting firms that have been involved in the development of the non-variable annuity reserving standards, along with practicing actuaries who have been valuing policies using VM-22 requirements. The purpose of the practice note is to assist actuaries with implementation of the principle-based nonvariable annuity reserve valuation approach adopted by the NAIC as detailed in the VM-22: Requirements for Principle-Based Reserves for Non-Variable Annuities-2026 Edition of the Valuation Manual, describing the requirements for calculating minimum valuation standard statutory reserves for non-variable annuity products. It is important that the reader review any differences that exist between the version of VM-22 on which this practice note was based and the version that is viewed as applicable to current valuations because the Valuation Manual is a living document and subject to change.

It is expected that actuarial practice for determining principle-based statutory reserves for nonvariable annuity insurance products will continue to emerge over time. It is likely that additional actuarial practice will be developed that is not contained in this practice note. The goal of this practice note is twofold: to assist actuaries who are implementing VM-22 with the understanding of what the requirements are and to provide an overview of actuarial practice. The work group attempted to meet both goals as well as it could.

Additions and revisions to this practice note will likely be needed in the future as practices are further developed and issues that are not anticipated below are addressed.

As of date of this practice note, the following is a list of Amendment Proposal Forms ("APF") that are impacting VM-22, are either undergoing discussions and revisions, or have been approved to be adopted in the 2027 or subsequent Valuation Manual. This practice note does not comment on these APFs, but only provides guidance based on what is in the 2026 Valuation Manual.

## As of July 8, 2026

|   No | APF         | Topic                                                                                                                   | Adopted by LATF?   |
|------|-------------|-------------------------------------------------------------------------------------------------------------------------|--------------------|
|    1 | APF 2025-16 | Reinvestment Guardrail                                                                                                  | Yes                |
|    2 | APF 2025-12 | VM-22 Standard Projection Amount: Disclosures & Credibility                                                             | Yes                |
|    3 | APF 2024-12 | Group Annuity Mortality Experience                                                                                      | Yes                |
|    4 | APF 2025-20 | Remove criteria requirements of VM-22 Aggregation                                                                       | Yes                |
|    5 | APF 2025-19 | Provide optional valuation treatment for new settlements/annuitizations on contracts written prior to VM-22 PBR or VM-V | No                 |
|    6 | APF 2025-18 | Clarify VM-22 applicability to deposit-type contracts based on Academy proposed edits                                   | Yes                |

## VM-22 Calculation Schematic

<!-- image -->

1 For this purpose, future hedging strategy does not include:

- hedging programs solely supporting index credits as described in VM-22 Section 4.A.4
- hedging strategies supporting the contracts are solely associated with product features that are determined to not be material under VM-22 Section 4.A due to low utilization

## 1. Exemptions, Transition Rules, and Details on Products Covered

## Q 1.1: What are the most important sections of the Valuation Manual that support VM-22?

A: The following sections of the Valuation Manual provide supplemental guidance that may prove helpful in implementing VM-22.

- Section II
- o Subsection 2: Annuity Products
- o Subsection 3: Deposit-Type Contracts
- o Subsection 6: Rider and Supplemental Benefits
- VM-01: Definitions for Terms in Requirements
- VM-31: PBR Actuarial Report Requirements for Business Subject to a Principle-Based Valuation
- VM-A: Appendix A - Requirements
- VM-C: Appendix C - Actuarial Guidelines
- VM-G: Appendix G - Corporate Governance Guidance for Principle-Based Reserves
- VM-M: Appendix M - Mortality Tables
- VM-V: Statutory Maximum Valuation Interest Rates for Formulaic Reserves

Section II points to VM-22 for the prescribed reserve methodology for Annuity Products (Subsection 2) and Deposit-Type Contracts (Subsection 3) for issues on or after 1/1/2026, and VM-A, VM-C, VM-M, and VM-V for issues prior to then. Section II, subsection 2.D provides guidance on the Annuity PBR Exemption that allows the continued use of pre-PBR reserving methodologies. Section II, Subsection 6 provides guidance on whether riders and supplemental benefits are reserved for in conjunction with the base contract or separately. VM-01 provides standardized definitions for terms used throughout the Valuation Manual, including VM-22 (i.e., terms used in VM-22 are not necessarily defined in VM-22). VM-31 provides content and format guidance for the PBR Actuarial Report that must be submitted to the company's regulator on an annual basis. VM-G provides roles and responsibilities for the Qualified Actuary, Senior Management and the Board.

## Q 1.2: Which contracts are covered by VM-22?

A: As described in VM-22 Section 2.A, VM-22 applies to all non-variable annuity contracts, including all individual and group annuity contracts whether directly written or assumed through reinsurance. For clarification, fixed income payment streams attributable to variable annuity guaranteed living benefits are excluded.

VM-22 defines three reserving categories for in-scope contracts: Payout Annuities, Accumulation, and Longevity Reinsurance. The Payout Annuities Reserving Category includes products identified in VM-22 Section 3.F.1.a and the Longevity Reinsurance Reserve Category includes reinsurance defined in VM-01. Products in this reserving category include:

- Single Premium Immediate Annuities (SPIAs);
- Deferred Income Annuities (DIAs);
- Term Certain Payout Annuities;
- Pension Risk Transfer Annuities (PRT);
- Structured Settlement Contracts (SSC); and
- Longevity Reinsurance.

The Accumulation Reserving Category includes all other annuities in scope of VM-22, including fixed income payment streams attributable to guaranteed living benefits associated with deferred annuity contracts. Products in this reserving category include:

- Fixed Deferred Annuities (SPDAs &amp; FPDAs);
- Multi-Year Guarantee Annuities (MYGAs); and
- Fixed Indexed Annuities (FIAs).

If the annuity product does not fall under VM-21 or is not explicitly excluded by VM-22, then VM22 applies. Annuity products explicitly excluded from the scope of VM-22 are listed in the Reserve Requirements section of the VM (section II), under the Annuity Products subsection (specifically, subsection 2.C), and include Preneed Annuities, Guaranteed Investment Contracts, Synthetic Guaranteed Investment Contracts, Funding Agreements, and other Stable Value Contracts. In the future there may be new products that fall under VM-22, possibly including some of these currently excluded annuity products.

For the VM-22 eligible annuity contracts described above, only issues on or after 1/1/2029 are required to be in scope of VM-22, although companies may elect to adopt VM-22 as early as 1/1/2026. However, as of the drafting of this practice note, retroactivity is under consideration for contracts issued prior to company's adoption of VM-22. The pre-PBR reserve methodology (i.e., VM-A, VM-C, VM-M, and VM-V) is applicable for these contracts not in scope of VM-22.

## Q 1.3: Do changes to an annuity contract issued prior to the operative date of the Valuation Manual make it subject to the requirements of the Valuation Manual?

A: The nature of the contract change would dictate whether the contract should be subject to the VM. For example, a change in the contract holder's beneficiary or address would not trigger valuation under the VM for a contract issued prior to the VM's operative date. However, if a new contract is issued as a result of the contract change (e.g., new contract number), many actuaries may consider this situation to qualify for a change in valuation method.

## Q 1.4: Are riders and supplemental benefits that are attached to non-variable annuity policies subject to VM-22 reserve requirements?

A: Reserves for riders and supplemental benefits are determined as described in Section II Subsection 6 of the Valuation Manual and illustrated in the VM Reserve Guidance for Riders and Supplemental Benefits Flowchart in this practice note. The regulatory guidance describes situations where the reserve for rider or supplemental benefits must be calculated in conjunction with the base contract, separately from the base contract, or where the company has the option for either approach.

Some actuaries use a process similar to that shown in the following flowchart when interpreting how to apply Valuation Manual reserve requirements to a rider or supplemental benefit:

## PBR Rider Valuation Treatment

<!-- image -->

## Q 1.5: What is the Annuity PBR Exemption and why would I apply for one?

A: The Annuity PBR Exemption described in Section II Subsection 2.D of the Valuation Manual allows the company to electively use pre-PBR reserve methodologies (i.e., VM-A, VM-C, VM-M, and VM-V) in lieu of VM-22. It applies for contracts without guaranteed living benefits (e.g., GMIBs, GMABs, GLWBs) and where exempted reserves are below specified thresholds or all annuity exposure is a result of election of contract benefits or features from pre-PBR reserve methodology contracts.

The Annuity PBR Exemption is for all issues of a given calendar year, except for contracts with guaranteed living benefits which must be subject to the VM-22 valuation methodology. If approved, the company may still electively subject certain blocks of business to the VM-22 reserving methodology.

Actuaries may want to apply for this exemption due to the intensive modeling and resources required to determine the VM-22 and they do not believe the pre-PBR reserve methodology understates the liability. However, even if the exemption is granted, they still may elect to value some of this business under VM-22 if the pre-PBR methodology results in perceived reserve redundancy for those blocks.

Thus, assuming a company would qualify for this exemption, it may decide to initially apply for this exemption for calendar year 2029 (i.e., first year VM-22 must be in effect). In addition to any contracts with guaranteed living benefits, it may also decide to subject other business issued in 2029 to the VM-22 reserving methodology. This exemption remains in place for future calendar years for as long as the company qualifies. Note that the Annuity PBR Exemption is not required during the 3year transition period to exclude selected blocks of business, as the company can simply elect not to early adopt VM-22 for these blocks during this period.

If the Annuity PBR Exemption status changes over time, the reserve methodology in place at contract issue prevails throughout the life of the contract. However, there is an exception to this guidance if the exemption criteria become more lenient in the future, whereby that future criteria can be applied retroactively to business that previously did not qualify (but also requires regulator approval).

## 2. Available Information on Common Practice

## Q 2.1: Which actuarial standards of practice (ASOPs) would apply to the actuary when performing the tasks in conjunction with determining reserves under VM-22?

A: According to ASOP No. 1, Section 4.3, "Actuaries are responsible for determining which ASOPs apply to the task at hand." The following ASOPs, as of the date of this practice note, are among those the actuary may wish to consider:

| ASOP No. 1          | Introductory Actuarial Standard of Practice                                                                                                         |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| ASOP No. 2          | Nonguaranteed Charges or Benefits for Life Insurance Policies and Annuity Contracts                                                                 |
| ASOP No. 7          | Analysis of Life, Health, or Property/Casualty Insurer Cash Flows                                                                                   |
| ASOP No. 11 Reports | Treatment of Reinsurance or Similar Risk Transfer Programs in Financial                                                                             |
| ASOP No. 12         | Risk Classification (for All Practice Areas)                                                                                                        |
| ASOP No. 15         | Dividends for Individual Participating Life Insurance, Annuities, and Disability Insurance                                                          |
| ASOP No. 22         | Statements of Opinion Based on Asset Adequacy Analysis by Actuaries for Life Insurance, Annuity, or Health Insurance Reserves and Other Liabilities |
| ASOP No. 23         | Data Quality                                                                                                                                        |
| ASOP No. 25         | Credibility Procedures                                                                                                                              |
| ASOP No. 38         | Catastrophe Modeling                                                                                                                                |
| ASOP No. 41         | Actuarial Communications                                                                                                                            |
| ASOP No. 52         | Principle-Based Reserves for Life Products under the NAIC Valuation Manual                                                                          |
| ASOP No. 56         | Modeling                                                                                                                                            |

## Q 2.2: Are there other practice notes that cover topics relevant to principle-based reserve calculations as described in the Valuation Manual?

A: Some helpful practice notes may include: Life Principles Based Reserves under VM-20, VM21 Supplement, the Asset Adequacy Analysis practice note, the Credibility practice note, the Model Governance practice note, the PBR Assumptions Resource Manual, and the PBA Projections practice note include relevant information for actuaries performing PBR reserve calculations. These practice notes can be found at the American Academy of Actuaries website at http://www.actuary.org/category/site-section/public-policy/practice-notes.

## Q 2.3: What is the Qualified Actuary and his/her responsibilities, and how does this differ from the "Appointed Actuary"?

A: The term "Appointed Actuary" means a Qualified Actuary who is appointed or retained in accordance with the Valuation Manual to prepare the actuarial opinion required in Section 3.A and/or 3. B of Model #820. The responsibilities of the appointed actuary are described in VM-30.

The term "Qualified Actuary" means an individual who meets the requirements specified in the Valuation Manual and is thereby qualified to sign the applicable statement of actuarial opinion. The requirements an actuary must satisfy to be considered qualified to sign the applicable statement of actuarial opinion can be found in the Qualification Standards for Actuaries Issuing Statements of Actuarial Opinion in the United States promulgated by the American Academy of Actuaries.

The Qualified Actuary assigned to oversee the principle-based valuation of a group of policies or contracts has a number of responsibilities outlined in VM-G. These responsibilities include:

- Overseeing the PBR calculations
- Verifying that the 1) PBR assumptions, methods and models, and 2) company's internal standards and controls reflect VM requirements. Specifically, assumptions are required to be prudent estimates.
- Responsibility for providing a summary report to the board and to senior management
- Responsibility for preparing the PBR Actuarial Report according to VM-31 requirements
- Responsibility for disclosing to the company's external auditors and regulators any significant unresolved issues regarding the company's PBR held

In addition, depending upon assigned responsibilities by the company the Qualified Actuary may be required to make and sign certifications required by the VM but is not required to opine on or certify the adequacy of aggregate reserves.

## 3. VM-22 Calculation

## Q 3.1: How would actuaries approach the calculation of the minimum reserve requirement under VM-22?

A: The following VM-22 Reserve Methodology Decision Tree illustrates allowable reserve VM-22 methodologies and the criteria that must be satisfied to use them. It shows one way to approach the decision-making process, but other considerations or priorities may result in a different order of operations. This particular exhibit reflects the perspective that the company prioritizes simplifying the reserve methodology and calculation complexity. For this perspective, the company may prefer the pre-PBR calculation methodologies, so would first attempt to qualify for the exemption or pass the SET, before attempting the SST to reduce the stochastic calculation requirement to a single deterministic scenario calculation. However, if the company determines that the PBR is less redundant than pre-PBR methodologies, it may not attempt a request for exemption or any of the exclusion tests.

For contracts ultimately subject to the DR or SR reserve methodology, model segments (i.e., group of contracts and associated assets that are modeled together) should be determined and will generally align with the company's asset segmentation plan, investment strategies, or approach used to allocate investment income for statutory purposes.

Model segments should be categorized into the three VM-22 reserving categories: Payout Annuities, Accumulation Annuities, and Longevity Reinsurance. However, the Payout Annuities and Accumulation Annuities Reserving Categories may be aggregated into a single Reserving Category to recognize diversification benefits. Contracts subject to DR calculations may not be aggregated with contracts not used in DR calculations for the SET and the determination of final VM-22 reserves.

The DR and SR require an integrated asset and liability model and determining associated prudent estimate assumptions. A couple of key aspects of this requirement include, but are not limited to, allocating existing company assets and PIMR to and developing reinvestment assumptions for all model segments

As applicable, SR intermediate model results are determined for each model segment according to VM-22 Section 4, with the appropriate modeling of reinsurance and hedging prescribed in VM-22 Sections 5 and 9, respectively. VM-22 Section 7.E.2 prescribes that the DR is also calculated according to the guidance provided in these sections but is limited to a single specified scenario. These intermediate model results are then aggregated across model segments for each Reserving Category (or across aggregated Reserving Categories described in VM-22 Section 3.F.2), using the methodology prescribed within VM-22 Section 3.F.5. Finally, the minimum aggregate VM-22 reserve is calculated as the aggregated SR plus the aggregated DR for contracts that pass the Single Scenario Test, plus the reserve for any contracts valued under applicable requirements in VM-A, VM-C, VM-M, and VM-V.

The ASPA also needs to be calculated in accordance with VM-22 Section 6 and disclosed in accordance with VM-22 Section 3.C. The SR is impacted by the ASPA if it is indicated and the company cannot attribute the difference between the SR and SPA to differences in the assumptions between their calculations, for those company assumptions that are based on reliable, relevant and credible company experience. In this situation, the assumptions and/or margins must be strengthened until the ASPA is no longer indicated.

## Q 3.2: How is the reported reserve adjusted for any due premiums modeled?

A: The company shall project gross premium received from the contract holder or the ceding company in the case of reinsurance (including any due premiums as of the projected start date). If due premiums are modeled, the final reported reserve needs to be adjusted by adding the due premium asset.

## Q 3.3: Why would an actuary perform the Stochastic Exclusion Test?

A: Some actuaries may attempt this test due to significant time and resources required to determine the SR and/or DR and they do not believe the prescribed alternative reserve methodology understates the liability. However, some actuaries may decide to perform the stochastic calculation even if the group of policies would pass this test because there may be some diversification benefits the company would then recognize in the minimum reserve calculation under VM-22.

Another consideration in attempting this test is probability of passing, which may be contingent on how well-matched liability and supporting asset cash flows are or the pre-PBR reserve methodology margin over PBR.

## Q 3.4: Why would an actuary perform the Single Scenario Test?

A: Some actuaries may attempt this test due to significant time and resources required to determine the SR and they do not believe the alternative reserve methodology understates the liability. However, some actuaries may decide to perform the stochastic calculation even if the group of policies would pass this test because there may be some diversification benefits the company would then recognize in the minimum reserve calculation under VM-22.

Another contributing factor on whether the actuary attempts this test is the eligibility of the contracts under consideration, as they cannot have guaranteed living benefits, surrender benefits impacted by economic conditions, or be supported by future hedging strategies.

## Q 3.5: What are model segments and considerations used in defining them?

A: Model segments are a grouping concept for individual liability contracts and assets which allows their projected cash flows for a given stochastic scenario to be combined. In addition to the netting of liability and asset cash flows, diversification benefits are also realized across contracts with different risk characteristics (e.g., product type and characteristics, gender, age, duration/issue era, etc.).

In addition to netting and diversification benefits, operational efficiencies may arise in using fewer model segments to span all contracts in scope of VM-22. Fewer model runs may require less model run time to cover the same number of contracts, but a given model segment should have consistent investment assumptions with actual company investment methodology and practice.

The actuary may define model segments to be consistent with the company's asset segmentation plan, investment strategies, or approach used to allocate investment income for statutory purposes, subject to VM-22 limitations on aggregating across Reserving Categories. Other considerations in deriving model segments may include homogeneity in contract holder behavior, the application of the company's NGE policy or the existence of non-proportional reinsurance.

## Q 3.6: What considerations when deciding how to group contracts when defining modeling cells for the cash flow model under Section 4.A.3?

A: The underlying premise in determining the grouping of contracts into modeling cells is that the selected grouping should not intentionally understate the reserve. With this in mind, the actuary will first want to decide each contract's model segment. Then, to assess the potential to group contracts into cells, homogeneity between products should be considered, including their features, sales distribution method(s) and historical experience for decrements, benefit utilization, premium persistency, etc. Some actuaries use model office projections for a subset of scenarios to determine the impact various groupings may have on the resulting reserve amount to ensure that the contract grouping methodology does not have a material impact. Some actuaries rely on seriatim projection output data across a sampling of scenarios that may suggest how contracts should be grouped together. The actuary may wish to consider Section 3.3 of ASOP No. 52, Principle-Based Reserves for Life Products under the NAIC Valuation Manual, which discusses these and other considerations for PBR models.

## Q 3.7: What are considerations in selecting a model time step/frequency of projection?

A: VM-22 Section 4.F.1 allows for the use of annual time steps when benefits/features are relatively insensitive to projection frequency but requires more frequent time steps otherwise. Actuaries typically use monthly, quarterly, or annual time steps in cash flow projections.

While sensitivity testing or other analysis should ultimately be used to make this determination, other considerations include product characteristics, the frequency and method of setting credited interest rates or other NGE, and model platform or other practical limitations. Time step selection should be considered at the model segment level, which can result in differing time steps across model segments.

It is not uncommon to use a more refined time step than necessary (e.g., monthly) even when product features are not sensitive to projection period frequency, as it may be the default time step for many vendor modeling systems. Some more sophisticated models may allow for multiple time step sizes within the same projection (i.e., more frequent earlier time steps when cash flows are relatively larger, followed by less frequent time steps as the block runs off). In addition, the implementation of skewness within a time step for a given cash flow is sometimes used to further refine modeling accuracy for that given time step.

## Q 3.8: How is the length of the projection period determined?

A: While VM-22 Section 4.A.6 requires projecting cash flows for as long as there are obligations, some actuaries may cut the projection off earlier by replacing the last period's normally projected cash flows with "terminal" cash flows that represent the impact from all future cash flows.

## Q 3.9: How is an individual policy reserve allocated defined under VM-22?

A: The seriatim cash surrender value, after any reinsurance, is the floor for the reserve for any specific policy. The methodology allocates more of the excess reserve to policies with the greatest risk. The contract-level reserve is the sum of the contract's minimum allocation value (MAV) plus the contract's allocated excess reserve (AER).

A scenario actuarial present value is the discounted present value of the liability cash flows at the NAER for the scenario that produces the aggregate scenario reserve not greater than the aggregate SR.

The MAV for

1. Payout contracts is MAX (APV, CSV);
2. Account value-based contracts is MAX (0, CSV); and
3. Longevity Reinsurance is 2% of the scheduled longevity benefits over the next 12 months from the valuation date.

The AER is determined by allocating the excess of a group's aggregate reserve over the group's MAV to a contract in proportion to the excess of the scenario APV over the MAV for the contract. An illustrative example is provided in Section 13.E.

## Q 3.10: How might an actuary determine that simplifications and approximations do not cause a material understatement of the reserve, as required by Section 3.J?

A: Some actuaries test the impact of using simplifications/approximations by calculating the minimum reserve without the simplifications/approximations on a small block of policies that are a good proxy for the entire group of policies and then comparing the result to the minimum reserve on the same small block of policies with the simplifications/approximations. Another approach used by some actuaries is to calculate the minimum reserve on all policies both with and without the simplifications/approximations every three to five years to see whether there are material understatements. This comparison could occur at a time other than the valuation date. Others may choose to use a reduced set of scenarios and provide a theoretical, statistical or mathematical argument to explain why the reserves are not understated.

## Q 3.11: What is PIMR and how is it used in VM-22?

A: The interest maintenance reserve (IMR) is a mechanism to smooth earnings due to realized capital gains and losses caused by interest rate fluctuations. It is the net balance of the deferral of these capital gains and their subsequent amortization. It can be positive or negative and is effectively treated as a negative asset. It is adjusted to a pretax basis (i.e., PIMR) by dividing the admitted portion under statutory accounting procedures by (1 - statutory corporate tax rate) because the VM-22 minimum reserve calculation ignores the impact of income taxes.

The (P)IMR shall be handled consistently with the treatment in the company's cash flow testing and allocated to each model segment. Although the method is not prescribed, the company shall use a reasonable and equitable approach to allocate the (P)IMR balance between the PBR and non-PBR business and across PBR model segments. When allocating (P)IMR, some actuaries consider the assets that were selected to back the PBR business and the level of data granularity available for what generated the applicable (P)IMR.

When performing VM-22 calculations, PIMR is reflected in two ways. When calculating the final scenario reserve, the PIMR is subtracted from the starting asset amount (under Direct Iteration Method) or from the starting asset amount plus the greatest present value of accumulated deficiencies (under the net asset earned rate ["NAER"] method). Additionally, if using the NAER method, the amount of assets in the general account at the start of the projection should be scaled to the approximate value of the statutory reserve, less any hedge instruments held in support of the contracts being valued and plus the allocated amount of PIMR. This is not done for the Direct Iteration Method due to that method solving for the exact amount of starting assets to run off the liabilities, and thus the PIMR does not need to be reflected when solving for the amount of starting assets.

## Q 3.12: How is reinsurance ceded reflected?

A: Per VM-22 Section 3.B, VM-22 reserves are to be determined and reported on both a preand post-reinsurance-ceded basis. VM-22 Section 4.A.1.f specifies that reinsurance cash flows are to be included in the determination of the scenario reserve. However, VM-22 Section 5 is the main section for reinsurance, providing details on how to reflect reinsurance in pre-PBR reserve methodologies, DR/SR calculations, SET/SST, and the SPA/ASPA calculation. This section also specifies that all these quantities must be calculated on both a pre-reinsuranceceded basis.

One observation made in VM-22 Section 5.A.3 is that since the SET and SST are required to be determined on both a pre- and post-reinsurance-ceded basis, the SR may be required for one basis but not the other for a given group of contracts (e.g., passes SET for one basis, but fails in the other).

Additional details for implementation of the regulatory guidance provided in VM-22 Section 5 can be found in Section 18 of this practice note.

## Q 3.13: How is hedging reflected?

A: VM-22 Section 4.A.1.g specifies that hedging cash flows are to be included in the determination of the scenario reserve, and VM-22 Section 4.A.4 provides detailed guidance on how to do so. This section provides separate guidance for hedging solely to support index crediting strategies versus otherwise. A key provision for both types of hedging programs is the reflection of hedge program ineffectiveness. Specific guidance is also provided for reflecting existing hedging assets as of the valuation date, as well as modeling future hedging activity. If the company does not have a future hedging program, it may consider existing hedging assets, but not the impact to cash flows from future hedging activities.

VM-22 Section 6.B prescribes the treatment of hedging for the calculation of the SPA/ASPA. VM-22 Sections 7.A.1.c and 7.E.1.b specifies that contracts supported by hedging are automatically ineligible for SR and DR, respectively, except future hedging strategies supporting the contracts are solely associated with product features that are determined to not be material under VM-22 Section 4. A due to low utilization.

VM-22 Section 9 prescribes the detailed treatment of hedging, except where the company only hedges index credits.

Additional details for implementation of the regulatory guidance regarding hedging for the calculation of DR and SR, as well as the modeling of derivative assets, can be found in Sections 10 and 19 of this practice note

## 4. VM-22 Calculation Overview-Part A. Stochastic Reserve

## Q 4.1: How is the Stochastic Reserve determined as required by VM-22?

A: Section 4 of VM-22 contains the requirements for determining the Stochastic Reserve (all section references below are to VM-22).

- Determine the number of VM-22 Reserving Categories for which the Stochastic Reserve is to be calculated. The definition of VM-22 Reserving Categories is found in Section 3.F. and includes: Payout Annuity Reserving Category, Longevity Reinsurance Reserving Category, and Accumulation Reserving Category. The Payout and Accumulating Reserving categories may be combined for purposes of stochastic modeling if the company demonstrates that the risks are managed together under an integrated risk management framework (e.g. common ALM strategy or supporting asset portfolio. It is important to note that Section 3.F. specifies that the company may aggregate groups of policies within each Reserving Category when determining the SR. However, groups of policies within different Reserving Categories and groups of policies excluded from the SR calculation (e.g. via the Stochastic Exclusion Test or use of the Single Scenario Test) are not included in the aggregation used to determine the SR. With that in mind, for each VM-22 Reserving Category, the following steps apply.
- Determine margins and Prudent Estimate Assumptions for all Risk Factors as described in Section 3.I.
- Generate the stochastic economic scenarios as described in Section 8 using the prescribed economic scenario generator (or an approved alternative).
- Determine the number of stochastic economic scenarios to use in the calculation as described in Section 8.
- For each VM-22 Reserving Category, calculate the Stochastic Reserve as follows:
- o The projection begins with a defined starting asset portfolio that supports the liabilities being modeled, consistent with Section 4 requirements.
- o Project asset and liability cash flows for each model segment under each economic scenario as described in Section 4.
- o Determine the Scenario Reserve for each scenario using the methodology described in Section 4.B, including the use of Net Asset Earned Rates (NAER) or direct iteration.
- o Calculate the CTE amount by ranking the Scenario Reserves from lowest to highest and taking the average of the worst 30% (i.e. Conditional Tail Expectation at the 70 th percentile or CTE 70) of these Scenario Reserves.
- o Adjustments may be required to reflect material risks not fully captured in the stochastic cash flow model.

## Q 4.2: How is the Scenario Reserve calculated?

A: As per Section 4.B, the Scenario Reserve can be determined using either:

- Net Asset Earned Rate (NAER) Approach: Scenario Reserve is equal to the Starting Assets less the allocated amount of PIMR plus the Greatest Present Value of Accumulated Deficiencies (GPVAD) across all projection years within the scenario. As per VM-01, the accumulated deficiency is the amount, measured as of the end of a projection year, equal to the negative projected statement value of general account and separate account assets. The accumulated deficiencies are discounted to the valuation date using NAER derived from the additional asset portfolio for the given scenario as further described in this practice note.

- Direct Iteration Approach: Scenario Reserve is determined by iteratively solving for the level of Starting Assets such that there is no positive accumulated deficiencies at the end of any projection year after subtracting the allocated portion of the PIMR as defined under VM-22.

-

The scenario reserve for a given scenario shall not be less than the aggregate cash surrender value, on the valuation date, for the underlying policies, including any applicable market value adjustment (MVA) where permitted. MVAs may be reflected in the aggregate cash surrender value calculation only when the assets supporting the liability are held at market value.

## Q 4.3: What are the differences in calculation of Scenario Reserves between VM-20, VM-21, and VM-22?

A: The differences in the scenario reserve calculation between VM-20, VM-21, and VM-22 are outlined below.

## Scenario Reserve Application

The scenario reserve applicability varies by Valuation Manual chapter. In VM-20 and VM-21, the scenario reserve calculation is only applicable to the Stochastic Reserve. In VM-22, the scenariobased projection techniques are used in both the Stochastic Reserve and the Deterministic Reserve; however, the DR is based on a prescribed single scenario rather than a distribution of stochastic scenarios. Note that the Deterministic Reserve concept does not exist in VM-21.

## Scenario Reserve Aggregation

In VM-20 and VM-22, the scenario reserve can be aggregated within each reserving category. In VM-20, the reserving categories are based on product type. In VM-22, there are reserving categories for annuities in the accumulation phase, annuities in the payout phase, and longevity reinsurance. In VM-21, aggregation occurs at a portfolio level, with scenario reserves typically determined across all modeled contracts within the scope of the valuation.

## Scenario Reserve Floor

The scenario reserve is floored at the cash surrender value in VM-21 and VM-22. There is no scenario reserve floor in VM-20 since floor is effectively provided through the Net Premium Reserve rather than within the scenario reserve calculation itself.

## Scenario Reserve Discount Rate

In VM-21 and VM-22, the accumulated deficiencies are discounted at the net asset earned rate (NAER) on additional assets (unless using the Direct Iteration Method). In VM-20, the scenario reserve is discounted at 105% of the path of one-year Treasury rates under the scenario.

## Scenario Reserve Interim Deficiencies

VM-21 and VM-22 incorporate constraints on interim deficiencies through the NAER or Direct Iteration Method. The additional invested asset portfolio for a scenario is a portfolio of general account assets as of the valuation date, outside of the starting asset portfolio, that is required in that projection scenario so that the projection would not have a positive accumulated deficiency at the end of any projection year. VM-20 does not impose the same constraints on interim accumulated deficiencies as those embedded in the NAER or Direct Iteration approaches used in VM-21 and VM-22.

## Scenario Reserve Hedging

The scenario reserve includes all currently held hedges. If the company has a future hedging strategy, then future adjustments to the strategy may be reflected subject to additional requirements and documentation. VM-22 has distinct treatment for hedging programs that solely hedge index credits and hedging programs designed to hedge anything other than solely index credits.

## Q 4.4: What is the appropriate level of aggregation when determining the Stochastic Reserve?

A: Per Section 3.F, the highest level of aggregation of policies determining the SR is generally limited to within each VM-22 Reserving Category level, except as permitted, specified in Section 3.F.2. Section 3.F.2 outlines the criteria under which aggregation across the Payout Annuity Reserving Category and Accumulation Reserving Category may be allowed, subject to demonstrating that the risks are managed together under a consistent ALM framework.

VM-22 allows the actuary to group policies into one or more model segments within a Reserving Category for purposes of projection. Separate model segments are required if a company elects to use the DR for a group of contracts within a Reserving Category. In other words, one model segment would be needed for the group of contracts that are calculated using the SR and one model segment for the group of contracts that are calculated using the DR. The level of aggregation within a VM-22 Reserving Category is subject to actuarial judgment, and should reflect similarity in product features, risk characteristics, and management practices. The selected level of aggregation may materially impact the SR and should be consistent with the risk practices and investment management practices of the company.

## Q 4.5: Are the prudent estimate assumptions the same for the Stochastic Reserve as for the Deterministic Reserve?

A: Section 3.I defines the prudent estimate assumption and provides guidance on their development and periodic review. Per Section 7.E.2, the prudent estimate assumptions used in determining the Deterministic Reserve should be consistent with those used for the Stochastic Reserve, including the underlying methodology and margins for adverse deviation. Differences in results may arise due to the interaction of certain assumptions with the economic scenario even if the same assumption framework is applied. Assumptions that are dynamically linked to the economic scenario, (e.g. lapse rates, credited rates, or withdrawal behavior) may vary across stochastic scenarios but reflect a single prescribed scenario in the DR. As a result, differences between the Stochastic and Deterministic Reserves should reflect scenario-dependent behavior rather than the differences in the underlying prudent estimate assumptions.

## Q 4.6: How are the discount rates determined?

A: Unless the Direct Iteration Method is used (in which case a discount rate is not required for purposes of determining the scenario reserve), the accumulated deficiencies are discounted using the NAER on additional invested assets.

The additional invested assets portfolio is outside of the initial starting assets to avoid a positive accumulated deficiency. This portfolio may consist of the following: General Account assets, cash, or a pro-rata slice of the original starting asset portfolio. The NAER is determined by projecting the additional asset portfolio from the valuation date to the end of the projection. Cash and investment proceeds are reinvested in accordance with the company investment policy or alternative investment strategy including appropriate returns, defaults and investment expenses for the given scenario. Liability cash flows are excluded from the construction of this portfolio.

If the value of the additional asset portfolio doesn't equal or exceed the accumulated deficiencies, then increase the size of the additional invested assets. Determine a vector of annual earned rates that replicates the growth of the additional invested assets over the projection period. This vector represents the NAER for the scenario and is used to discount accumulated deficiencies to the valuation date.

## Q 4.7: How does the actuary calculate the path of net asset earned rates on additional assets?

A: In determining the Scenario Reserve, unless the Direct Iteration Method is used pursuant to Section 4.B.1.b, the accumulated deficiencies are discounted using the Net Asset Earned Rates (NAER) on additional assets as described in VM-22 Section 4.B. To determine the NAER on additional invested assets for a given scenario:

## 1) Construct and project the additional invested asset portfolio:

The additional invested asset portfolio is defined as a portfolio of general account assets as of the valuation date, separate of the starting asset portfolio, that is required in that projection scenario to eliminate accumulated deficiencies at the end of any projection year, incorporating appropriate assumptions for investment returns, defaults, and investments expenses under the scenario.

## 2) Derive the NAER vector:

A vector of annual earned rates is determined such that it replicates the projected growth of the additional invested asset portfolio from the valuation date to the end of the projection period for the scenario. This vector will be the NAER for the scenario and is used to discount accumulated deficiencies to the valuation date.

## Q 4.8: How does the actuary determine the amount (if any) to add to the cash flow model results to capture any material risk not otherwise reflected in the Stochastic Reserve?

A: VM-22 does not prescribe a specific method for determining adjustments to reflect material risks not otherwise captured in the stochastic cash flow model. Actuaries should assess whether the modeling framework fully reflects all material risks associated with the underlying policies and make appropriate adjustments. In practice, some actuaries develop adjustments for material risks outside of the cash flow model where it is known that their cash flow models used for their Stochastic Reserve do not cover specific policy risks. For example, if there is a certain rider that would pay an additional benefit if some contingent event happened and that event is not being modeled, then the actuary might include an adjustment for the payment of this benefit as a topside adjustment to the final model output. Alternatively, actuaries may incorporate such adjustments directly into the stochastic cash flow model so that it is reflected in the Scenario Reserves and the final CTE amount. The chosen approach should be consistent with the company's overall modeling framework and supported by appropriate analysis and documentation, demonstrating that all material risks have been adequately reflected in the Stochastic Reserve.

## 5. VM-22 Calculation Overview-Part B. Deterministic Reserve

## Q 5.1: VM-22 allows two different methods for the calculation of the Scenario Reserve. What are the two methods, and how are they different?

A: The two methods for calculating the Scenario Reserve are the NAER method, described in Section 4.B.1.a and 4.B.3 and the Direct Iteration Method (DIM) described in Section 4.B.1.b. These methods can be summarized as follows:

- The NAER method includes projecting asset and liability cash flows for each scenario, then discounting to the valuation date using the NAER on additional assets.
- The DIM identifies the level of starting assets by projecting asset and liability cash flows to the end of the projection period, iterating as necessary until the starting assets are sufficient to fully liquidate all policy obligations, leaving zero assets at the end of any projection year and no positive accumulated deficiencies at the end of any projection year during the projection period.

The primary difference between the two methods is that the NAER method determines the Scenario Reserve by discounting accumulated deficiencies using a derived discount rate (NAER), whereas the DIM directly determines the required level of starting assets using the projected asset and liability cash flows by iteratively adjusting the size of the starting portfolio. Under the NAER method, the additional asset portfolio may be constructed using various approaches, such as a pro-rata allocation of the actual initial portfolio, cash that is immediately reinvested, or a combination of general account assets used to cover projected shortfalls. The selection of assets for this portfolio would be the same across all scenarios. This prevents the allocation of cash or different asset types to certain scenarios to produce a higher NAER on additional assets due to knowing the amount of accumulated deficiencies for each scenario. Note that for reinvestment, this additional asset portfolio is subject to the alternative investment strategy discussed in section 4.D.3.b.

In practice, calculating the net asset earned rate on additional assets subject to VM-22 requirements can be complex and may require modifications and/or approximations. Considerations may include items such as differences in the way assets are modeled, the timing of cash flows, the manner in which the model purchases and sells assets, and the treatment of non-cash items. VM-31 Section 3.F.6 outlines documentation requirements for the NAER calculations.

## Q 5.2: When would a company calculate a Deterministic Reserve (DR) for a model segment?

A: The DR may be calculated for a model segment when the segment meets the eligibility criteria for the Deterministic Certification Option, as outlined in Section 7.E, and the company elects to apply that option. In this case, the model segment is not subject to the SR calculation, and the reserve for that segment is determined using the DR instead of the SR.

## Q 5.3: How would actuaries approach the calculation of the Deterministic Reserve (DR) for each model segment as required by VM-22?

A: The DR for a model segment is determined using projected cash flows projected in compliance with the applicable requirements in Section 4, Section 5, Section 10, and Section 11 of VM-22 under a single prescribed economic scenario (Scenario 12 as defined in Appendix 1 of VM-20). The DR is calculated using the same framework as the Scenario Reserve described in Section 4; however, instead of evaluating results across a range of stochastic scenarios, the calculation is performed solely under this prescribed deterministic scenario. As a result, the DR represents the Scenario Reserve determined for that single scenario.

## Q 5.4: Is Deterministic Reserve aggregation allowed across product types (Deferred Income Annuity contracts and Longevity Reinsurance, for example.)?

A: Per Section 3.F, if a group of policies for which a Deterministic Reserve is calculated includes policies from more than one VM-22 Reserving Category (i.e., the Accumulation Reserving Category, Payout Annuity Reserving Category, or the Longevity Reinsurance Reserving Category), a Deterministic Reserve shall be determined for each subgroup consisting of only those policies within each individual VM-22 Reserving Category, following the requirements in Section 4. The NAER used for discounting each such subgroup may be the NAER for the group of policies. If the sum of the Deterministic Reserves for these subgroups does not equal the total Deterministic Reserve calculated for the group of policies as a whole, the Deterministic Reserve for the group of policies shall be allocated to each such subgroup proportionally. See Question 3.12.

## Q 5.5: What economic scenario assumptions are used to determine the Deterministic Reserve?

A: Per Section 7.E.2, the Deterministic Reserve is determined using a single prescribed economic scenario (i.e. Scenario 12 as defined in Appendix 1 of VM-20.)

## Q 5.6: How will actuaries model assets in the deterministic and stochastic calculations?

A: See Section 11 of this practice note for questions and answers related to asset modeling and the determination of starting assets for both deterministic and stochastic calculations.

## Q 5.7: How is reinsurance incorporated into the Deterministic Reserve?

A: Section 19, titled "Reflection of Reinsurance Cash Flows in the DR or SR," outlines the considerations for including reinsurance cash flows in the modeled reserves.

## Q 5.8: Is the decision to select the method to calculate the scenario reserve completely at the company's discretion, or do certain conditions have to be met?

A: No explicit conditions are prescribed for selecting the method used to calculate the Scenario Reserve. The choice between methods is made at the discretion of the company.

## Q 5.9: Can the company move back and forth between SR and DR for a model segment in subsequent valuation dates?

A: There is no explicit provision prohibiting the movement between DR and SR in subsequent valuation dates. The DR is calculated for groups of contracts for which a company elects the Deterministic Certification Option in Section 7.E. If a company does not elect the Deterministic Certification Option or does not pass the Deterministic Certification Option, then the SR should be calculated.

## 6. Standard Projection Amount

## Q 6.1: What are some of the ways that product or contractual features that conflict with Standard Projection requirements may be reflected?

A: Some actuaries might consider factors such as the degree of certainty, level of conservatism, and materiality of the contractual features. Some actuaries may model the contractually specified as specified while others might follow prescribed assumptions and adjust other assumptions only after the specified event has occurred. Some may reflect contractual features if they produce more conservative reserves but follow Standard Projection requirements when they are more conservative (e.g., Standard Projection forbids contracts with guaranteed death benefits to lapse even though they contractually would). If the contractual features do not materially impact the result, some actuaries believe it may be acceptable to not reflect these features and use the Standard Projection requirements. Regardless of the decision, the actuaries should explicitly document the approach and rationale. VM-31 Section 3.F.12.d requires discussion of differences between stochastic and Standard Projection cash flow models, and Section 3.F.12.i requires documentation of modifications to the Standard Projection requirements. Actuaries may also consider language in VM-22 Sections 6.B.1 and 6.C.1.

## Q 6.2: What approaches might an actuary consider when their VM-22 models cannot exactly reflect the prescribed Standard Projection assumptions or methodology?

A: The language in VM-22, Sections 6.B.1 and 6.C.1 provides guidance in this situation. Some actuaries conclude that the appropriate approach depends on the materiality of the specific feature. If omitting these prescribed assumptions or methodologies materially understates the Standard Projection Amount, especially when the Additional Standard Projection Amount may drive the aggregate reserve, some actuaries would include a topside adjustment in the final reserve amount. The actuary may wish to consider VM-31 Section 3.F.12.i when documenting the approach used and explaining deviations from VM-22 prescribed assumptions and methodology. This documentation might include estimates of the feature in question and/or rationalization for why simplifications would not result in a material understatement per VM-31 Section 3.F.2.e.

## Q 6.3: What are the reporting and disclosure requirements associated with the Additional Standard Projection Amount (ASPA)?

A: VM-22 Section 3.C states that the additional standard projection amount is only required for disclosure purposes pursuant to VM-31. However, the guidance note in Section 3.c clarifies that future versions of the Valuation Manual will require specific information in the disclosure. An attribution analysis individually covering all material drivers and a residual impact may be required for all products, regardless of whether the ASPA is greater than 0 or not. If an ASPA is indicated and no strengthening of reserves is done in response to the SPA result, support for material company assumptions that are drivers of the ASPA should be provided.

A: Section 3.C of VM-22 states that the Additional Standard Projection Amount (ASPA) is only required for disclosure purposes pursuant to VM-31. However, the guidance note in Section 3.C clarifies that future versions of the Valuation Manual will require specific information in the disclosure. An attribution analysis individually covering all material drivers and a residual impact may be required for all products, regardless of whether the ASPA is greater than 0 or not. If an ASPA is indicated and no strengthening of reserves is done in response to the SPA result, support for material company assumptions that are drivers of the ASPA should be provided

## Q 6.4 What is the difference between the prescribed projection amount and the additional standard projection amount (ASPA) and how does the buffer impact these values? Are there any differences in the buffer if a company uses the DR instead of the SR?

A: As described in Section 6.B.4.a.ii, the prescribed projection amount is calculated following the same method as outlined in Section 9.C, which is the same as following Section 4.A.4 for a company that does not have a future hedging strategy supporting the contracts other than those supported index interest rate credits. Once the prescribed projection amount is determined, it is reduced by the CTE70 (adjusted) for contracts calculating an SR or by the DR for contracts that calculate the DR. This amount is referred to as the unbuffered ASPA.

For contracts following the SR, the unbuffered ASPA is reduced by the difference between the CTE70

(adjusted) without the cash surrender value floor and the CTE65 (adjusted) without the cash surrender value floor. The ASPA is the greater of this amount and 0.

For contracts following the DR, because it is not possible to calculate a different CTE metric from a single scenario, a company can either elect to use no buffer or can calculate the buffer for the DR based on a calculation of the buffer as a percentage of CTE70 (adjusted). This percentage is calculated as the difference between an unfloored CTE70 (adjusted) and an unfloored CTE65 (adjusted), following the requirements of Section 6.B.4.c., divided by the CTE70 (adjusted). The DR buffer is this percentage, which must be calculated on a valuation date no earlier than December 31 on the prior calendar year, multiplied by the DR following Section 6.B.4.a. The unbuffered ASPA is reduced by this amount. The ASPA is the greater of this amount and 0.

## Q 6.5 How is the maintenance expense assumption applied to contracts without an account value?

A: Section 6.C.2 describes the prescribed maintenance expense assumption. A base maintenance expense is applied based on the contract type. For contracts with an account value, an additional expense equal to seven basis points of the projected account value each year is added. For contracts without an account value, this same amount is multiplied by a proxy of account value derived from the present value of benefits using the prescribed mortality assumption in Section 6.C.8 and the discount rate described in Section 13.B.
## Q 6.6 What is the purpose of the rate factor, market factor, and market rate in the prescribed lapse formula and how are they calculated?

A: Section 6.C.5 describes the calculation of full surrenders. The total lapse is influenced by economic conditions through the rate factor. The rate factor, in turn, is influenced by the market factor and the surrender charge amount and is equal to the market factor * Max (0, 1 - 5 *(1 - CSV/AV)).

The market factor is dependent on the difference between the crediting rate and the market rate. For indexed annuities and fixed annuities with Interest Guarantee Period &lt; 2 Years:

MR = Max (3-month Treasury rate, 5-year Treasury rate plus 50% A/50% AA spread) minus Pricing Spread

For fixed annuities with Interest Guarantee Period ≥ 2 Years:

MR = N-year Treasury rate plus 50% A/50% AA spread minus Pricing Spread, which is set to 0%.

N = 5-year Treasury rate for 2 years ≤ Interest Guarantee Period &lt; 5 years

N = 7-year Treasury rate for 5 years ≤ Interest Guarantee Period &lt; 7 years

N = 10-year Treasury rate for Interest Guarantee Period ≥ 7 years

The value of N should take into consideration the duration of renewal segments and impact of the surrender charge period.

An actuary may consider the requirements of VM-22 Section 4.D.3.b when determining the value of MR.

- Q 6.7 The prescribed mortality tables in Section 6.C.8 are Age Nearest Birthday (ANB). Should they be used even if a company uses Age Last Birthday (ALB)?

A: The guidance note in Section 6.C.8 clarifies that the prescribed mortality should align with whether a company uses ALB or ANB. If a company uses ALB, a conversion formula is described as: q(x)ALB = [q(x)ANB + (1 - q(x)ANB) * q(x+1)ANB]/(2 - q(x)ANB)

This conversion should be applied to the mortality rate after the multiplicative factor has been applied. Converting either the base table alone or the base table and the adjustments separately would result in a different mortality rate.

- Q 6.8 Does the ANB to ALB conversion apply for the constant extra death (CED) methodology for structured settlements substandard lives?
- A: Section 6.C.8.iii describes the prescribed mortality for structured settlement contracts. For substandard lives, mortality should reflect the inclusion of "Constant Extra Death" (CED) methodology as described in Actuarial Guideline IX-A. This amount is applied prior to the application of the multiplicative factor, and thus the conversion between ANB to ALB should apply after.

- Q 6.9 What prescribed mortality tables should be used for group annuities owned or purchased by retirement plans, as defined in the NAIC Model 820 - Standard Valuation Law?
- A: Group annuities that are owned or purchased by retirement plans are discussed in Section 6.C.8.iv. It is expected that each company should use the most granular data available when assigning annuitants to the appropriate table by collar. If a company cannot determine the collar for a group of annuitants, then the company should use the Total table. Retirement tables should be used for in-pay annuities (retired annuitants) and Employee tables should be used for deferred annuities (active or term-vested annuitants). Contingent survival tables should be used for beneficiaries to the extent that beneficiaries can be identified, or the base tables should be weighted based on company expectation of proportion of benefits associated with beneficiaries.
- Q 6.10 What utilization assumption should be used for guaranteed living benefit riders?
- A: Section 6.C.4 outlines that prudent estimate assumptions of the company shall be used, but that guardrails around the cumulative utilization assumption. One may view the prescribed utilization guardrails in section 6.C.4.c as an overall requirement inclusive of contracts currently receiving withdrawal benefits.

## 7. Stochastic Exclusion Test and Single Scenario Test

## Q 7.1: What is the purpose of the Stochastic Exclusion Test and why would I want to perform it?

A: As described in Section 7.A of VM-22, the company can elect to exclude one of more groups of contracts from the SR calculation by passing the SET. In situations where risks are adequately reflected in the pre-PBR methodology, the level of PBR may be similar to that from the pre-PBR methodology. If the SET is passed, operational efficiencies may be realized using the pre-PBR methodology. However, some actuaries may decide against performing this test to take advantage of potential SR diversification benefits from aggregating excludable contracts with others.

## Q 7.2: What contracts are eligible for the SET and what types of asset and liability portfolios are most likely to pass the SET?

A: All contracts are eligible for the SET, except for contracts supported by hedging programs under certain conditions. Specifically, hedging programs solely supporting index credits or solely supporting product features that are determined to be immaterial under VM-22 Section 4.A due to low utilization are eligible, while contracts subject to other future hedging programs are not.

Groups of contracts and their supporting assets that are most likely to pass the SET would not have material interest rate risk, mortality and/or longevity risk, or asset return volatility risk (i.e., the risk on non-fixed-income investments having substantial volatility of returns, such as common stocks and real estate investments). Groups of contracts with material levels of these risks will tend to increase SR, possibly above reserve levels produced by pre-PBR methodologies.

Asset and liability portfolio characteristics contribute to these risks. Accordingly, contracts with limited guarantees or an expectation of minimal variation of contract holder behavior across changing economic conditions are more likely to pass the SET. Asset portfolios that are well matched with the liabilities they support and result in less required reinvestment or asset sales are also more likely to pass the SET.

## Q 7.3: What are the allowable SET methods?

A: The actuary may use any of the following three approaches to pass the SET.

The Stochastic Exclusion Ratio Test (SERT) described in Section 7.C requires 16 specified economic scenarios to be run for each of 3 different mortality improvement assumptions for each group of contracts under consideration. In this context, each group of contracts should not have contracts with significantly different risk profiles. A baseline run is defined from these 48 combinations and the difference of the largest adjusted scenario reserve from the other 47 runs and the baseline run is noted. If this difference divided by the present value of benefits from the baseline run is less than the minimum of the company's materiality threshold and 6%, the test is passed. The SERT must be calculated annually within twelve months prior to the valuation date.

The Stochastic Exclusion Demonstration Test (SEDT) described in Section 7.D requires that the actuary provide a reasonable assurance that if the SR was calculated on a stand-alone basis for the group of contracts, the resulting stochastic reserve for the group of contracts would not be higher than the statutory reserve determined pursuant to the pre-PBR methodology. The demonstration shall take into account whether changing conditions over the current and two subsequent calendar years would be likely to change the conclusion to exclude the group of contracts from the SR requirements. VM-22 provides four examples of eligible demonstration methodologies but does not limit the demonstration methodology to these four choices. The SEDT is calculated in the first year that the SEDT is utilized and at least once every three calendar years thereafter.

The SET Certification Method (SETCM) may be used if either the SERT or the SEDT has been passed within the last three years. If so, the SETCM described in Section 7.B.3 is passed if the qualified actuary certifies that the group of contracts has not had material changes in interest rate risk, mortality and/or longevity risk, or asset return volatility risk in the last three years. Alternatively, this test is passed if the qualified actuary can confirm that groups of contracts that do not have guaranteed living benefits, future hedging strategies, or pension risk transfer business do not have material levels of these risks.

While the SERT focuses on the contracts' sensitivity to changing economic environments, the SEDT objective is to ensure that the pre-PBR reserve that would alternatively be used is adequate. The SETCM Certification Method may rely on either of these methods, or other analysis. For blocks of business that do not have living benefits, do not have future hedges, and are not PRT, alternative analyses are permitted demonstrating and certifying that risks outlined in Section 7.B.3 are not material.

## Q 7.4: How might an actuary choose between the available SET methods?

A: There are some considerations before deciding which SET to choose.

One consideration is the operational complexity and burden of executing one SET method over another. The SERT is fully prescribed and based on an existing model with a few specified modifications, requiring the calculation of 48 adjusted scenario reserves and the calculation of the present value of benefits for these adjusted scenario reserves. It requires a minimal amount of judgment or decision-making compared to the other two methods. The SEDT effectively requires calculating VM-22 scenario reserves across multiple or all economic scenarios as well as corresponding pre-PBR reserves, or understand SR and pre-PBR drivers (i.e., Section 7.D.2.d). It also requires assessing potential changing conditions over the next two years in addition to the current year, in determining whether the SR would be higher than the corresponding pre-PBR reserve. The SETCM requires the most judgment and is also subject to more uncertainty regarding regulator acceptance relative to the other two methods.

Another consideration may be the required frequency of the test. The SERT must be performed for each year it is chosen for the SET. Alternatively, analysis supporting the SEDT and SETCM are required to be performed only once every three years if certain conditions are met (e.g., interest rate risk, mortality and/or longevity risk, or asset return volatility risk have not materially changed during this period).

The existence of models that can currently calculate a VM-22 SR may also influence a company's decision as to their specific path. If such a model already exists, there should be no limitations. Conversely, there are fewer pathways to passing the SET if no such model exists, including leveraging the cash flow testing model (assuming one exists) or using other analysis to demonstrate that the group of contracts does not have material interest rate risk, mortality and/or longevity risk, or asset return volatility.

SET options may be limited if a specific test is attempted and failed. For example, the SERT cannot be attempted if either the SEDT or SETCM has been attempted and failed. Similarly, VM-22 Section 7.D.1.b indicates that if the SEDT fails because the pre-PBR reserve is no longer adequate, then the SET also fails, therefore also making the SETCM unavailable as an option. It may be strategically advantageous to perform the SERT first, as the other two options are still available even if the SERT fails.

One approach to optimize operational efficiency for situations characterized by minimal changes to the risk profile of these VM-22 cohorts may be to perform the SERT or SEDT once every three years and use the SETCM that relies on these successful tests for the other two years. This may be offset by the challenge of SETCM regulator acceptance.

## Q 7.5: Is the SET performed on a pre- or post-reinsurance-ceded basis?

A: As alluded to in VM-22 Section 5.A.3, the SET is required to be performed on both a pre- and postreinsurance-ceded basis in order to determine the pre- and post-reinsurance-ceded reserves. Thus, it is possible to have to calculate the SR for a group of contracts on a pre-reinsurance-ceded basis, but not on a post-reinsurance-ceded basis, and vice versa.

One exception for the SERT described in VM-22 Section 7.C.2.a.ii.e is for pro rata coinsurance that does not materially impact the interest rate risk, mortality and/or longevity risk, or asset return volatility in the contract, where the actuary can choose to perform the SERT on either a pre- or post-reinsurance-ceded basis that can be used to satisfy the requirements for both bases.

## Q 7.6: Should I monitor supporting SET metrics between reporting cycles?

A: It may be challenging for some companies to implement on short notice the ability to calculate the SR for contract groups where the pre-PBR methodology had been elected because the SET had previously been passed. Accordingly, off-cycle monitoring of the SET status may be necessary to comply with VMG 4.A.3.a communication and readiness requirements. Monitoring can take the form of simplified recalculations of supporting SET metrics, tracking key risk indicators, or other relevant analytics.

The following are examples of such circumstances that may result in increased interest rate risk, mortality and/or longevity risk, or asset return volatility risk:

- Most recent SET passing margin is small
- Adverse changes to the models that produce the supporting SET metrics, including assumption updates
- Normal changes to the liability in-force risk profile (e.g., resulting from new business terminations and in-force aging)
- Normal changes to the supporting asset portfolio risk profile (e.g., maturities or sales of existing assets and the corresponding reinvestment, reinvestments from coupon/dividend income and net positive liability cash flows, and credit downgrades or defaults)
- Adverse changes to the economic environment
- Implementation of new products or purchase of new asset types

## Q 7.7: What is the purpose of performing the Single Scenario Test (SST)?

A: As described in Section 7.E, the SST is used to determine if the company may elect to calculate the DR in lieu of the SR for a group of contracts using a single deterministic economic scenario, if certain conditions are met. The SST allows improved operational efficiency in situations where the risk profile of the blocks passing the SST is such that the SR scenario reserve results are not expected to vary materially from each other or the DR. Also like the SET, some actuaries may decide against performing this test to take advantage of potential diversification benefits in the SR calculation.

The pre-PBR reserve methodology may be considered less operationally difficult than the SST requirements, so the company may initially attempt the SET. If the SET is passed, the company would generally use the pre-PBR methodology, and thus not attempt the SST. Conversely, if the SET fails, the company may elect to attempt the SST.

The DR is the VM-22 scenario reserve for scenario #12 found in Appendix 1 of VM-20.

## Q 7.8: What contracts are eligible for the SST?

A: The contracts must have predictable, stable cash flows and limited contract holder behavior, and economic conditions do not materially influence anticipated contract holder behavior for the group of contracts. While the materiality status of economically dependent contract holder behavior is generally defined by the company, as a "floor" the regulatory guidance explicitly lists product feature examples that would not qualify: surrender benefits, recurring premium payments, and guaranteed living benefits. Groups of contracts supported by future hedging strategies are also not eligible, except if these strategies solely support immaterial product features due to low utilization. These restrictions would tend to exclude many if not all products in the Accumulation Reserving Category.

## Q 7.9: How does the SST compare with the SET?

A: The SST exclusion test requirements are similar to the SET since it allows the same three methodology options, but with some exceptions. The SST version of the SERT does not require the +1% or -1% mortality improvement assumption adjustments, requiring only the 16 pre- and postreinsurance-ceded runs. The SST version of the SEDT replaces the pre-PBR reserve with the DR for the comparison with the SR (i.e., the demonstration shows that the SR calculated for the SST block is not higher than the DR). The SST version of the SETCM does not require a statement or support of immaterial mortality and/or longevity risk, however it does require a quantitative demonstration of immaterial interest rate risk and asset return volatility risk. An example is provided whereby the reserve is deemed adequate in the cash flow testing model for all 16 economic scenarios using its assumptions adjusted with explicit margins and/or sensitivities such that moderately adverse conditions are reflected for risks other than the economic scenarios.

There are also differences in eligibility between SST and SET. The SET allows groups of contracts with future hedging solely for either supporting index credits or product features that are determined to not be material under VM-22 Section 4.A due to low utilization, while the SST is more restrictive in that it only allows the latter hedging situation. There are also some eligibility differences regarding product features, whereby the SST is more limited than the SET, as described earlier in this practice note.

## 8. Difference From Cash Flow Testing-Scenario Reserve Calculation

## Q 8.1: May the actuary use an asset adequacy testing cash flow model to calculate the scenario reserve in the Stochastic Reserve calculation for VM-22?

A: Some actuaries may use their cash flow testing (CFT) models in calculating the scenario reserve. However, the actuary may need to adjust the CFT model to reflect the different purposes of the calculations. Some potential differences between CFT and VM-22 are listed below. Note that this list is not intended to be exhaustive.

- CFT models may include approximations or model simplifications that are not appropriate for VM-22.
- VM-22 uses prudent estimate assumptions; CFT assumptions may include margins for adverse experience, but those margins may not be the margins required by VM-22.
- Some assumptions in VM-22 are prescribed and must be used in the calculation. CFT may have different prescribed assumptions, depending on state requirements.
- There may be some differences in projection periods, time steps, or model segments.
- Some business/model segments for which the scenario reserve must be determined may not be subject to cash flow testing.
- The starting assets used in the model and reinvestment assumptions may differ.
- Cash flow testing models may include issue years that are not within the scope of VM22.
- Treatment of IMR and AVR may differ.
- CFT models include federal income taxes while VM-22 should exclude federal income tax
- There may be specific requirements for modeling hedges under non-index credit and index credit strategies.

## Q 8.2: May the actuary use the same assumptions for VM-22 as those used for cash flow testing?

A: VM-22 Section 3.I.1 requires that prudent estimate assumptions be used. VM-01 defines "prudent estimate assumption" as "a risk factor assumption developed by applying a margin to the anticipated experience assumptions for that factor." For each scenario in a stochastic reserve calculation, the prudent estimate assumption may vary to reflect scenario-dependent risks as described in Section 12.B.7. Some modifications to cash flow testing assumptions may be required if the cash flow testing assumptions are not prudent estimate assumptions. In addition, some assumptions are fully or partially prescribed for the Stochastic Reserve calculation. Examples include asset spreads and default cost assumptions as described in Section 4.D.

## Q 8.3: In calculating the Stochastic Reserve, may the actuary use the same interest rate, corporate bond, and equity scenarios as used for the CFT projections?

A: Section 8.E provides for the use of non-prescribed scenario generators as long as the TAR is not materially lower than the TAR resulting from the use of the Prescribed Scenarios. Appendix 1 of VM-22 states that the prescribed economic scenario generator is available on the NAIC Scenario Files website. Scenario reduction techniques are allowed to reduce the number of scenarios, but only if they do not materially reduce the reserve. Accordingly, a smaller set of scenarios may be used for VM-22 calculations if scenario reduction techniques are applied and the approach is documented and does not result in a material understatement of results. A scenario selection tool is available on the NAIC Scenario Files website offering example approaches based off the 20-year UST significance measure or equity Greatest Wealth Factors (GWF) from the Large Cap fund. CFT analysis does not require a prescribed generator and parameters.

## Q 8.4: Can the CFT projection period be used without modification for VM-22 calculations?

A: Section 4.A.6 of VM-22 states that "Projections of accumulated deficiencies shall be run for as many future years as needed so that no obligations remain at the end of the projection periods." Some actuaries may assume 100% deaths or 100% surrenders after an appropriate period of time, provided no material amount remains.

Actuaries wishing to use the same projection period in the VM-22 calculations as is used for CFT should ensure that these conditions are satisfied.

## Q 8.5: Would the actuary generally use the same starting assets in both the VM-22 and CFT calculations?

A: Some actuaries may assign the same assets for both calculations, but it is not a requirement. Because VM-22 may include only a portion of the business and/or issue years, some actuaries select a limited subset of assets associated with the business being valued. Other actuaries use a pro-rata portion of the CFT assets for VM-22.

## Q 8.6: Would the actuary generally use the same model aggregation in VM-22 as is used in the CFT calculations?

A: The minimum reserve requirements specified by Section 3 of VM-22 clearly state that policies subject to VM-22 requirements must be included in a specific VM-22 Reserving Category, where the VM-22 Reserving Categories are (1) Payout Reserving Category; (2) Longevity Reinsurance Reserving Category; and (3) Accumulation Reserving Category. The Payout and Accumulation Reserving Categories may be aggregated. The reserve may be determined in aggregate across various groups of contracts within each Reserving Category, or within the combined Accumulation and Payout reserving categories following Section 3.F.2, as a single model segment when determining the SR or DR. Aggregation may also be done across multiple model segments following Section 3.F.5. This approach may or may not be consistent with the company's CFT calculations. Some actuaries carefully review the CFT model structure before using a similar structure for VM-22 minimum reserve calculations.

## Q 8.7: How are IMR and AVR treated in Stochastic and Deterministic Reserve calculations?

A: Because VM-22 is determined on a pre-tax basis, the IMR used in the Stochastic and Deterministic Reserve calculations is adjusted to a pre-tax basis. The VM-22 reserve methodology (for both DR and SR) reflects the pretax IMR (PIMR) by deducting it from the aggregate scenario reserve calculated for a given scenario and then applying the applicable cash surrender value floor as of the valuation date.

## Q 8.8: How are federal income taxes treated in VM-22 versus CFT?

A: VM-22 requires that federal income taxes be excluded from both the projection of cash flows and the determination of discount rates. Typically, federal income taxes are reflected in CFT.

## Q 8.9: Are taxes other than federal income taxes ignored for the purpose of calculating reserves under VM-22? For example, does the actuary ignore premium taxes?

A: Section 12.D.1.f states that expenses paid to provide fraternal benefits in lieu of federal income taxes should be excluded along with foreign income taxes. Section 12.D.1.k states that expenses categorized in the annual statement as "taxes, licenses and fees" (Exhibit 3 of the Annual Statement) should be reflected in the expense assumption.

## Q 8.10: What is the treatment of reinsurance differences between CFT and VM-22?

A: Treatment of reinsurance in VM-22 is discussed in Section 18 of this practice note.

## 9. Considerations When Performing Reserve Calculations on Other Than the Valuation Date

## Q 9.1: What valuation date is required for the DR, SR, and the Additional Standard Projection Amount?

A: Per Section 3.K of VM-22, the calculation of the DR, SR, and the Additional Standard Projection Amount can be performed as of a date up to three months prior to the valuation date as long as an appropriate method is used to adjust the reserves to the valuation date.

Although the calculation may use prior data, some actuaries take into account relevant experience up to the valuation date when determining Anticipated Experience and Prudent Estimate Assumptions used in the calculations.

## Q 9.2: How might an actuary "use an appropriate method to adjust" the DR, SR, and the Additional Standard Projection Amount to the valuation date when it is calculated as of an earlier date?

A: VM-22 does not prescribe a method for this adjustment. Some actuaries use a model office as of the earlier date and make several adjustments to take into account changes to the valuation date. The adjustments could include taking into account mortality, surrenders, withdrawals, deposits, and new contracts issued since the projection start date but prior to the valuation date through a pro-rata adjustment to the relevant contract information (e.g., account value) so the overall characteristics for the group of contracts approximate those characteristics on the valuation date. Additionally, the actuary could review all Prudent Estimate Assumptions in the model and make any adjustments necessary for information or experience from the projection start date and the valuation date. Adjustments to the assets may or may not be made depending on how materially the asset portfolio has changed. In particular, some actuaries would use the economic scenarios as of the valuation date if the economic conditions have changed materially.

Some actuaries apply a high-level adjustment to the overall reserve amount or to each of several portions of the reserve. The adjustment may be based on analysis of past trends in the reserve, including "roll-forward" analysis of the change in the reserve balance. Such analysis would typically isolate the main drivers of the reserve change and would enable the actuary to estimate short-term changes in the reserve after the projection start date based on correlation with those drivers. This could include using some characteristics of the group of contracts in the calculation (e.g., account value) and a ratio method to modify the DR, SR, and Additional Standard Projection Amount for the group of contracts actually in force on the valuation date. Other actuaries calculate the DR, SR, and Additional Standard Projection Amount on a small, representative sample of contracts from the group of contracts on the valuation date and compare this amount to the DR, SR, and Additional Standard Projection Amount for those contracts as of the earlier projection start date. This information could be used in a number of ways to modify the calculations made using the earlier projection start date to the valuation date. Of course, the actuary would need to be prudent in determining the number of representative samples that are appropriate and which contracts to use in this calculation.

The actuary will typically confirm that the approach used is appropriate for the group of contracts being valued. If the contract characteristics or economic environment have changed materially, most actuaries would consider a projection start date prior to the valuation date to not be appropriate. Other actuaries would provide additional disclosures to explain why they determined a prior start date was appropriate (e.g., if using an older date is expected to produce a more conservative reserve than using a more recent date).

## Q 9.3: Should changes in economic conditions from the projection start date also be incorporated in the adjustment of the reserves?

A: Some actuaries performing the calculations may modify the reserve calculations to take into account the economic conditions as of the valuation date if the valuation date is different from the projection start date. This adjustment would take into consideration both the impact on the liability cash flows and the net asset earned rate.

For products whose liability cash flows are dependent on changes in the economic environment, such as fixed indexed annuities, some actuaries may reflect the economic conditions on the valuation date (if there have been material changes) and adjust the liability cash flows accordingly. This may require a re-computation of the reserve amounts or could include high-level adjustments reflecting expected changes to the liability cash flows. Some actuaries may apply adjustments that were based on sample calculations or prior sensitivity testing.

For products whose future expected liability cash flows are not sensitive to changes in market conditions, some actuaries may not make modifications to the liability calculation. In such cases, actuaries should document their rationale in accordance with VM-31. An example would be a fixed payout annuity. The liability cash flows would not be dependent on a change in the economic environment, so no adjustments would generally be made. Some actuaries might make adjustments in order to reflect the impact of changes in interest rates on discount rates.

Some actuaries believe that actuarial judgment should be used to determine whether adjustments to the reinvestment assumptions and the projected net asset earned rate used in the calculation are needed. Those actuaries may modify the asset projection based on updated economic conditions as of the valuation date if the changes would lead to materially different reserves.

Some actuaries may include a specific description and discussion of how the asset and liability cash flows were adjusted in the documentation supporting the calculation per the requirements in VM-31 Section 3.D.11.i.

## Q 9.4: Will actuaries adjust the calculation for new business and lapses if company in-force data from prior to the valuation date is used?

A: If policy in-force data from a date prior to the valuation date is used, some actuaries determine that no adjustments to the in-force data or model is necessary if they have demonstrated that interim terminations, lapses, and new issues between the projection start date and valuation date do not materially affect the resulting reserves. If large volumes of new business have been issued, some actuaries may estimate the additional reserves from the new issues. It is also expected that some actuaries would have a lapse and new business assumption or roll-forward method to reflect changes in the in-force data between the projection start date and the valuation date.

Some actuaries may analyze whether including policies no longer in force as of the valuation date in the Stochastic Reserve modeling would materially affect the reserves. If there were a material difference in actual to expected terminations, some actuaries make modifications to the models to take into account the changes. In accordance with VM-31 Section 3.F.16.d, actuaries include a specific description and discussion of how the in-force policies were modified to take into account changes up to the valuation date in the documentation supporting the calculation and why unadjusted differences were determined to be material or immaterial.

## Q 9.5: Does the calculation need to be adjusted for policyholder actions such as additional premium payments, taking or repayment of a policy loan, partial withdrawals, utilization of living benefits, and other policy changes that have occurred since the projection start date but prior to the valuation date?

A: It is expected that some actuaries may not make adjustments to the reserve for policyholder actions between the projection start date and the valuation date. However, if there have been policyholder actions that would materially affect the minimum reserve, some actuaries would make modifications.

## Q 9.6: Are there other types of changes occurring between the projection start date and the valuation date that could lead to adjustments in the calculations?

A: In addition to those items addressed above, some actuaries may consider the impact of changes to the business's risk profile, such as:

- Significant changes in asset allocation or mix of assets (by quality, duration, or other characteristics);
- New, terminated, or recaptured reinsurance;
- Changes in counterparty risk;
- Changes in non-guaranteed elements;
- Changes in disintermediation risk; and
- Merger and acquisition activity.

## 10. Details on Starting Assets and Asset Modeling

## Q 10.1: How are due premiums reflected in the starting assets?

A: Since most products in-scope for VM-22 are either single premium or flexible premium contracts, deferred premiums are not directly addressed in the VM. However, there are some inscope products (e.g., certain Longevity Reinsurance contracts) that may have due premiums on any given valuation date. Some actuaries may choose to be consistent with the treatment of such premiums in VM-20 and thus not include the due premium asset in the level of starting assets used when calculating the SR or DR (if applicable). Instead, these actuaries may choose to include the due premiums in the expected future cash flows used in calculating the SR or DR (if applicable). Other actuaries may examine whether the contracts with due premiums also have associated accrued benefit payments (e.g., for reinsurance contracts that are cash settled in arrears) and include a net cash flow in the SR or DR (if applicable) only to the extent that the difference between due premiums and accrued benefits is material. Regardless of the method chosen, an actuary working with such products should ensure that due premiums are consistently treated from one valuation to the next, that no double counting of due premiums is inadvertently applied under the chosen treatment, and that reserves are not inappropriately understated by the chosen treatment.

## Q 10.2: If the company passes the Stochastic Exclusion Test, does the actuary still have to model assets?

A: If a company passes the Stochastic Exclusion Test and elects to hold reserves pursuant to VMA, VM-C, and VM-V, assets do not need to be modeled. However, performing the stochastic exclusion test could require assets depending on the methodology. If a company passes the single scenario tests for eligible products and elects to use the single scenario to calculate the reserves, assets must be modeled just like would be done for a full stochastic reserve calculation.

## Q 10.3: What is the level of starting assets required in the calculation of the Deterministic and Stochastic Reserve, and how does an actuary set an initial estimate of the starting assets?

A: Section 4.D.1 states that at the start of the projection, the starting assets shall be equal to an amount of assets held in the general account equal to the approximate value of the statutory reserves, less the hedge instruments included in the starting assets that support the contracts being valued, and the allocated PIMR attributable to the assets selected. The amount of iterations used to reach the "approximate" value is at the discretion of the actuary and must be documented in the VM-31.

A typical initial estimate for accumulation products could be the account value or the cash surrender value at the start of the projection, or a ratio of the account value or cash surrender value based on a previously reported SR. For payouts, or products with no account value or cash surrender value, an initial estimate could be derived from either a small subset of scenarios or the deterministic scenario, or the calculation of the APV following the requirements in Section 13.

For all products, another initial estimate could be derived from taking the statutory reserve from the prior reporting period and making adjustments to reflect the impact of such things as new sales, new products, change in economic environment, and new reinsurance agreements since the prior valuation date, or any other items that impact the expected reserve level.

## Q 10.4 How does the actuary select the assets for additional asset portfolio?

A: In Section 4.B.3, VM-22 discusses the NAER on additional assets, which is used to discount the accumulated deficiencies unless a company uses the direct iteration method described in Section 4.B.1.b. The additional asset portfolio consists of general account assets and/or cash outside the starting asset portfolio that would be required in a projection scenario so that the projection would now have a positive accumulated deficiency at the end of any projection year.

The additional asset portfolio can be comprised of one or more of the following:

- 1) Pro-rata slice of the starting asset portfolio
- 2) Cash that is immediately reinvested
- 3) A combination of assets that would be transferred to the portfolio from the general account to cover a potential shortfall.

As required by Section 4.B.3.a, the initial additional asset portfolio should be determined using the same asset allocation methodology for all stochastic scenarios at the valuation date. The methodology used to create the additional asset portfolio should generally be logically consistent with the method used to select assets for the starting asset portfolio. For example, some actuaries believe that if the starting asset portfolio is pro-rata from the general account, then pro-rata for the additional asset portfolio would be consistent. Some actuaries believe if the starting asset portfolio selects assets using certain criteria, e.g. highest yielding or duration matching with the liability, then it would not be appropriate to use a pro-rata slice of the total portfolio for the additional portfolio, because the entirety of certain assets are already in the starting asset portfolio, and may instead use a combination of assets that were not selected for the starting asset portfolio in the additional portfolio.

Additionally, the company should be able to support that the additional assets are not double counted across various PBR calculations. For example, it would be inappropriate to have the same asset transferred to the additional asset portfolio for VM-21 and VM-22.

## Q 10.5: How does the actuary choose which assets to include in the calculation?

A: The principles outlined in VM-20 Section 7.A.1.b, and Section 7.D.2 also apply to VM-22. Model segments are used to determine the group of policies and associated assets that are modeled together. VM-20 Section 7.A.1.b states that model segments should be selected that are consistent with the company's asset segmentation plan, or the approach used to allocate investment income for statutory purposes.

VM-20 Section 7.D.2 states that where an asset portfolio supports both PBR (in this case VM-22) policies and non-PBR policies, an equitable method should be used to apportion assets to the policies.

Some actuaries may choose general account assets that, for management purposes, are generally associated with policies modeled. For example, where asset segmentation is used, the starting assets are selected from the asset segment that supports the block of policies subject to PBR (i.e., the asset segment that is used to track investment strategies and allocation of investment income to the policies they support).

Additionally, per Section 4.D.1.b., the assets shall generally be selected on a consistent basis from one reserve valuation to the next.

## Q 10.6: Under what circumstances may a company have insufficient starting assets in a portfolio under VM-22? If a company doesn't have enough existing assets in a portfolio, and the Stochastic or Deterministic Reserve calculation requires more assets, how is this handled? Can the actuary add more assets to the projection than are currently held?

A: There are at least two circumstances where a portfolio may have insufficient assets in the VM22 calculations:

1.) When determining the NAER on the additional invested asset portfolio, there may be insufficient assets within the supporting asset segment and outside of the starting asset portfolio to meet the requirement in Section 4.B.3.a., which states that the accumulated value of the additional assets be sufficient to eliminate positive deficiencies at the end of one or more projection years under a given scenario. In that case, the actuary should follow the guidance in Section 4.B.3.a. and select either general account assets available to the company on the valuation date outside of the starting asset portfolio from another general account segment or cash assets that are assumed to be immediately reinvested. To the extent that the portfolio segment contains sufficient assets, it is also permissible to use a pro-rata slice of the starting asset portfolio to determine the NAER on the additional invested asset portfolio. In any case, the actuary should confirm that the selected assets are not being used to support multiple PBR applications within the same legal entity under any given scenario (e.g., the same assets should not be assumed to be selected under a given scenario to cover deficiencies for both VM-21 and VM-22).

2.) When using the Direct Iteration method, the actuary may exhaust the available assets in the supporting asset segment for the contracts included in the valuation. In that case, some actuaries may identify specific assets in the surplus portfolio or in other general account portfolios (e.g., a corporate segment) so there are enough assets available for the projection. Other actuaries may model an injection of cash that can then be re-deployed within the projection according to the reinvestment strategy being applied (i.e., either the company's reinvestment strategy or the reinvestment guardrail specified in Section 4.D.3.b, as applicable). While some actuaries may choose to proportionally increase the assets in the portfolio to equal the starting asset amount under the assumption that assets would be transferred into the portfolio with the same average characteristics of the existing portfolio, under this approach, the actuary should consider that sufficient assets of the assumed characteristics are available within some portfolio within the legal entity. Similar to above, the actuary should also confirm that the selected assets added to the portfolio are not being used to support multiple PBR applications within the same entity under any given scenario (e.g., the same assets should not be assumed to be selected under a given scenario to cover deficiencies for both VM-21 and VM-22).

## Q 10.7: To the extent that starting assets have unstable market values, what impact would this have on the projected cash flows?

A: Per Section 4.D.2, the projected value of starting assets shall be determined in a manner consistent with their values at the start of the projection. Section 4.A.1.h also requires modeling the proceeds arising from modeled asset sales, prepayments, asset default costs, investment expenses and determining the portion representing realized capital gains and losses.

During any projection interval, actuarial modeling principles suggest that the actuary reflect any uncertainty in the timing and amounts of asset cash flows related to the paths of interest rates, equity returns or other economic values.

In considering future uncertainty when applying this principle, actuaries would not make any modification to prescribed asset assumptions, or the modeled interest rates or equity returns because they are generated stochastically using a prescribed generator.

Some actuaries may take into account market instability by making modifications to nonprescribed assumptions, where appropriate, using actuarial judgment.

## Q 10.8: Is it possible for the general account portion of starting assets to be negative?

A: Yes. Additionally, Section 4.D.1.b states that if the amount of initial general account assets is negative, the model should reflect a projected interest expense.

## Q 10.9: How will the actuary choose assets to include in the model if there are more general account assets associated with the modeled policies than are needed as starting assets?

A: Some actuaries may choose a pro-rata portion of a segmented portfolio or other grouping of assets. Some actuaries may follow how assets are assigned for determining credited rates. Some actuaries may choose specific assets based on modeling constraints. However, the same asset would not be included in the starting assets of different model segments where the total amount of such asset is more than what the company owns.

## Q 10.10: What types of grouping of assets might be used in the projection?

A: Section 3.J.states that acceptable model efficiency techniques include grouping of assets, and such techniques are allowed only if i.) the company can demonstrate that grouping does not materially understate the minimum reserve that would have been obtained using a seriatim approach and ii.) the expected value of the reserve determined using the technique is not less than the expected value of the reserve determined using a seriatim approach.

Some assets may be similar enough in nature that some actuaries might reasonably expect their cash flows and valuations to react in similar fashions as economic conditions change and therefore would group them together for modeling purposes. For grouping of fixed-income investments, some actuaries might assess whether parameters such as credit quality, time to maturity, duration, and interest and principal patterns are similar before considering grouping of individual securities.

Another important consideration when considering grouping of assets is the degree of optionality (e.g., call or put provisions, expected prepayment behavior, extension risk, etc.) inherent in the assets that might cause divergent cash flow profiles under certain economic scenarios, even if more similar results would be expected under many economic scenarios. In light of these potential complexities, some actuaries may elect to model assets on a seriatim basis.

## Q 10.11: How are investment cash flows (returns and principal repayments) for general account fixed-income assets modeled?

A: VM-20 states that fixed-income assets include public bonds, convertible bonds, preferred stocks, private placements, asset-backed securities, commercial mortgage loans, residential mortgage loans, mortgage-backed securities, and collateralized mortgage obligations. (See Guidance Note after Section 7.F.1.c.)

Investment cash flows on fixed-income assets are modeled for each projection interval per Section 4.D.4 as follows:

- Project the gross investment income and principal repayments for each asset (or grouping of assets) consistent with each scenario.
- Subtract prescribed default costs from gross investment income.
- Subtract investment expenses, using prudent estimate assumptions, from gross investment income.
- Project the proceeds from asset sales and determine the portion representing any realized capital gains and losses.
- Reflect any uncertainty in the timing and amounts of the asset cash flows related to the paths of interest rates, equity returns or other economic values (calls, puts, prepayments, extensions, etc.).
- Model the impact of the derivative asset programs (if any) associated with these assets.

For starting assets, gross investment income shall be modeled in accordance with the contractual provisions of each asset and in a manner that is consistent with each economic scenario. For reinvestment assets, gross investment income is determined by adding a prescribed spread (see Tables F through I on the Related Documents tab of the LATF page of the NAIC website, updated on a monthly basis for current spreads, and quarterly basis for long-term spreads) to the prescribed Treasury rate in each projection interval (where the prescribed Treasury rate comes from the economic scenario).

## Q 10.12: How are investment cash flows for general account total return equity investments modeled, such as money market funds, diversified bond funds, real estate, U.S. or international equity, private equity, etc.?

A: VM-22 states that equity assets are non-fixed-income investments having substantial volatility of return, such as common stocks and real estate investments. Per Section 4.D.b, investment cash flows from these assets are modeled as follows:

- Determine the grouping of these assets (called "proxy funds") in a manner consistent with the grouping for index crediting as described in section 4.A.2. The grouping into proxy funds shall reflect characteristics of the efficient frontier.
- Allocate equity assets into each proxy fund. Each proxy fund is typically expressed as a linear combination of recognized market indices.
- Project the future gross investment return, including realized and unrealized capital gains, for each proxy fund in a manner that is consistent with the prescribed general account equity returns from the economic scenario as described in Section 8.C.
- Modeling the timing of asset sales that is consistent with the investment policy of the company for that type of asset.
- Reflect investments expenses through a deduction to the gross investment return using prudent estimate assumptions.

This process involves actuarial judgment to determine the appropriate proxy funds and methodology to "map" the return from proxy funds to the prescribed general account equity returns from the prescribed economic scenario. See Q11.1 for details on the different returns produced by the prescribed generator.

Actuaries might wish to effect modeling of proxy funds in different ways. For example, some actuaries might perform a regression of past fund performance against past performance of market indices consistent with the scenario generator classifications and develop a scenario set for each proxy fund that is consistent with an appropriate weight of such scenario returns derived from the regression. Alternatively, funds might be decomposed using regression techniques into funds corresponding to each of the indices, or some other way could be used. Whatever method is used, the actuary must be able to document that the projected returns for the proxy funds are not overly optimistic.

VM-22 provides additional guidance in Section 8.C to assist actuaries in performing this mapping process. The goal of mapping the proxy funds to the prescribed funds is to generate consistent scenarios, i.e., higher expected returns for higher risk, and lower expected returns for lower risk. Risk is often measured as standard deviation of log returns. One approach to establish consistent scenarios would set the model parameters to maintain a near-constant market price of risk. Another closely related method would assume some form of "mean-variance efficiency", i.e. to establish and adjust the parameters of the proxy fund such that it lies on or within a corridor of the efficient frontier, which can be constructed by standard curve fitting or regression techniques. The underlying principle and treatment of proxy funds mapping is consistent between VM-20 and VM-21.

## Q 10.13: How are Separate Account assets modeled?

A: Certain products in-scope for VM-22 (e.g., Pension Risk Transfer contracts) may be supported by assets held in one or more separate accounts. Assets held within these separate accounts may be held at either statutory book value or at fair market value. Typically, these separate accounts are not unitized and assets held within them are not subject to periodic policyholder-directed re-allocation. However, the contractual benefit payments made to policyholders under such contracts may or may not depend on the value of the assets held within the separate account depending on the contractual terms (e.g., through the application of experience credits, experience premium refunds, or other mechanisms). For these types of separate accounts, actuaries may choose to model the separate account assets in a manner similar to identical assets held within the general account and would apply the company's reinvestment and disinvestment strategies as needed within the projection. Actuaries may elect to include some or all of the separate account assets in the portfolio of Starting Assets used in determining the SR (or, if applicable, the DR). However, there may be situations in which the company's overall investment and/or hedging strategies consider assets in both the general account and one or more separate accounts taken together, and in that case, actuaries may choose to select initial assets according to their actual investment and/or hedging practices. Other actuaries may choose to simply use a pro rata slice of all separate account and general account assets within the supporting asset segment as a practical expedient (when it can be demonstrated such choice would not materially understate or bias the resulting reserve).

## Q 10.14: How are derivative programs modeled?

A: Section 4.D.1.a.i requires that any hedge instruments held in support of the contracts being valued, including derivatives, be included in the starting assets used to determine the SR or (if applicable) the DR. Section 4.D.2 specifies that derivative instruments that are used in hedging and that are not assumed to be sold during a particular projection period may be accounted for at amortized cost in an appropriate manner elected by the company (recognizing any methodology requirements that may be prescribed by a company's state of domicile).

For derivatives held as part of a hedging program, Section 4.A.4 lays out the requirements for the modeling of the overall hedging strategy, and the requirements vary by the type of hedging program.

If the company currently holds derivatives as hedge instruments but does not have a future hedging strategy, then the requirement is to simply include the existing hedge instruments currently held by the company on the valuation date in the starting assets and run them off within the projection. In this case, no future hedge purchases or hedge rebalancing should be modeled in subsequent projection periods.

If the company has a future hedging strategy designed solely to offset index credits for policyholders via purchases of derivative instruments (e.g., purchasing options to fund index credits on fixed indexed annuities), then the company should include its existing hedge instruments held on the valuation date in the starting asset portfolio and should include cash flows from future hedge purchases or rebalancing of existing hedge assets intended solely to offset index credits to contract holders in future projection periods. As specified in Section 4.A.4.b.i.(c), an index credit hedge margin is reflected in both the "best efforts" and "adjusted" runs by reducing index credit hedge payoffs by a margin justified by credible company experience and accounting for potential model error. Such margin shall be no less than 1.5%. If no experience data is available for calibrating the error factor, then a margin of 20% should be assumed. There is no maximum cap on the margin that should be applied, and a margin exceeding 20% may be appropriate if company experience or analysis of expected hedge performance suggests it is warranted.

If the company has a future hedging strategy designed to hedge more than just offsetting future index credits, complete requirements and considerations are included in Section 9 of VM-22. Essentially, the SR and (to the extent applicable) the DR are developed as a weighted average of a "CTE70 (best efforts)" calculation, which reflects the future expected costs and benefits of the hedging program along each scenario path, and a "CTE70 (adjusted)" calculation, which reflects only the existing hedge instruments held on the valuation date plus future hedge purchases and adjustments solely for offsetting index-credits. For hedge instruments held on the valuation date for purposes other than hedging solely index credits, the CTE70 (adjusted) calculation can be calculated either reflecting the future cash flows from the existing instruments or replacing the existing instruments with cash or other general account assets with an equal market value.

All of the risks, costs, hedge mismatches, and potential imperfections or tolerances in the hedge must be recognized in the company's implementation of the hedge within their modeling. However, companies are allowed to use either "explicit methods" or "implicit methods" to model their hedge positions. "Explicit methods" reflect the cash flows from the hedge position directly in the cash flow model used to calculate the SR, while "implicit methods" determine at least some portion of the impact to projected deficiencies outside of the cash flow model, with correspondingly derived adjustments then made to components of the cash flow model or the resulting reserve to reflect the costs and benefits of the hedge program.

The company must determine an appropriate error factor (E) in the range of 5% to 100%, reflecting the potential error associated with the hedging strategy. This error factor must be justified based on back-testing of at least 12 months of historical experience using one of the approaches outlined in Section 9.C.6. If fewer than 12 months of experience are available or for which changes have been made to the hedging program, a minimum floor on error factors applies. See Section 9.C.7 for details.

Once an appropriate E is determined, the final SR or DR is then determined as follows:

CTE70 (best efforts) + E * MAX [0, (CTE70 (adjusted) - CTE70 (best efforts))

## Q 10.15: What investment strategies for modeling reinvestment assets are permitted?

A: Section 4.D.3.b states that the aggregate reserve will be the higher of that produced using the company's modeled reinvestment strategy or using the alternative investment strategy. A general principle in determining a reinvestment strategy is that it should be reflective of a company's actual reinvestment strategy or the strategy that they anticipate will be used in the future. This should be based on sound reasoning and should not be speculative (e.g., there is clear evidence that the company is modifying their reinvestment practices).

In addition, the alternative investment strategy should include fixed income reinvestment assets with the same weighted average life as the reinvestment assets in the modeled company investment strategy. The assets are all public, non-callable bonds with gross asset spreads, default costs and investment expenses consistent with the credit quality blend as described in Section 4.D.3.b. The principles in Section 4.D.3.a for projecting general account assets are also relevant.

Many actuaries find it advantageous to start the modeling of reinvestment assets by having a thorough discussion with the company's investment department or external investment advisors, if necessary, to understand the company's actual investment strategy. If the investment strategy used for asset adequacy analysis is a reasonable representation of the company's actual investment strategy, the assumed investment strategy for Asset Adequacy Analysis (AAA) might also be a reasonable starting point.

Some actuaries will use a mix of asset types and final maturities that produce a desired pattern of gross investment income and principal repayments. Other actuaries will assume fixed or floating rate coupons, or zero coupons. Other actuaries will prefer to utilize a complex model representation for reinvestment assets, which might include, for example, illiquid or callable assets. Other actuaries will prefer a simple model representation, which may involve mapping of more complex assets to combinations of asset types, such as combinations of public non-callable corporate bonds, U.S. Treasuries, and cash.

## Q 10.16: How are gross spreads determined for reinvestment assets?

A: Gross spreads are discussed in VM-22 Section 4.D.3, which in turn references VM-20 sections 7.E, 7.F, and 9.F. VM-20 Section 7.E.1.d states that the gross spreads on public non-callable corporate bonds purchased in the model subsequent to the valuation date are determined by a prescribed methodology. The methodology is based on current and historical spread levels relative to U.S. Treasuries and is consistent with the prescribed approach to determine default costs on existing assets. For these bonds:

- Gross spreads are determined based on actual current and historical market data, using the same tables used in the calculation of default costs.
- The prescribed gross spreads start at current average market spreads in effect at the valuation date (published by the NAIC from a market source on a monthly basis) and grade linearly in yearly steps to the long-term benchmark spreads (derived and published by the NAIC based on actual historical data from the same market source on a quarterly basis) by the start of projection year four.
- Prescribed default costs are then deducted explicitly for purchased assets, using the same approach to calculate default costs as for existing assets (but ignoring the maximum net spread adjustment factor).

For investments other than public, non-callable corporate bonds, gross spreads are not prescribed, but are to be consistent with and in reasonable relationship to the prescribed spreads for public, non-callable corporate bonds. As each bond or security is unique due to its contractual provisions (callability, prepayment priority, sinking fund etc.) and other features (ratings, public, liquidity etc.), there is no general rule of thumb for setting a spread for each individual bond or security.

Some actuaries consult with an investment professional (internal or external) to obtain a general framework on the current spreads and historical long-term average spreads. The actuary might select a sample of recently purchased assets, compute their option-adjusted spreads (OAS) and compare them with the current and long-term market observed spreads.

VM-20 Section 9.F.2.b provides a definition of OAS. Actuaries might keep in mind that the OAS for bonds and securities other than non-callable bonds is based on arbitrage-free stochastic interest rate scenarios rather than the scenarios for PBR.

With respect to grading from the current spread to the ultimate long-term spread, VM-20 Section 9.F.8 prescribes a 4-year grading period for non-callable bonds. Some actuaries consider using the same or shorter grading periods for bonds and securities other than non-callable bonds.

Per VM-22 Section 4.D.3.b, the methodology also incorporates a floor on the modeled reserve.

- The modeled reserve cannot be less than would be obtained by substituting an alternative investment strategy in which all fixed income reinvestment assets are public non-callable corporate bonds with a credit quality blend of 5% Treasury, 15% "Aa2/AA", and 80% "A2/A".
- The blend is intended to represent an approximate equivalent of the industry average asset allocation.

The VM-22 Actuarial Report requires that the actuary provide documentation demonstrating compliance with the minimum floor requirement. Some actuaries may decide to run the reserve calculation twice, the first using spreads following the company's investment strategy, and a second calculation assuming a strategy following the 5/15/80 mix of Treasury, Aa2/AA, and A2/A bonds. However, if the model investment strategy does not involve callable assets, some actuaries may conclude that demonstration of compliance will not require running the reserve calculation twice. For example, an analysis of the weighted average net reinvestment spread on new purchases by projection year (gross spread minus prescribed default costs minus investment expenses) of the model investment strategy compared to the weighted average net reinvestment spreads by projection year of the alternative strategy may suffice.

Some actuaries may conclude that they need to adjust the assumed mix of asset types, asset credit quality, or the levels of nonprescribed spreads for other fixed-income investments to achieve compliance.

## Q 10.17: How are asset market values modeled when assets are sold?

As outlined in Section 4.D.3.a.ii, the price for fixed income investments and derivative instruments associated with fixed income investments should reflect the projected Treasury curve along the relevant scenario along with the prescribed asset spread assumption relevant to the modeled investment or instrument. An actuary may model, to the extent possible, the impact on market value along the scenario path of any embedded options (e.g., call or put options, prepayment behavior, etc.) or other economically sensitive features present in the assets being sold. Where such features cannot be modeled directly, the guidance provided in Section 3.J regarding simplifications and model efficiency techniques should be applied. The actuary should consider whether the modeling of the market value of assets being sold should be consistent with the modeling of market value of assets being purchased.

Per Section 4.D.3.a.iii, the gross spread assumptions used to compute market values for public noncallable corporate bonds when modeling the sale of starting assets as well as the purchase and sale of reinvestment assets should follow the requirements of VM-20 Sections 7.E, 7.F, and 9.F. The prescribed spreads reflect current market conditions as of the model start date and grade to longterm conditions at the start of projection year 4. Similarly, transactions of derivative instruments associated with fixed income investments should follow the interest rate swap spreads in VM-20 Section 9.F.

For sales of fixed income assets other than public non-callable corporate bonds, gross asset spreads over U.S. Treasuries should be set in a manner consistent with, and in a reasonable relationship to, the prescribed spreads for public non-callable corporate bonds and interest rate swaps.

Bid-ask spreads should also be considered. As there could be differentiation in bid spreads and ask spreads, the spreads used in calculating the market value when assets are sold are to be consistent with, but not necessarily the same as, the spreads used for purchases. The actuary should also consider that specific starting assets may have different characteristics than the modeled reinvestment assets.

## Q 10.18: What is the Pretax IMR (PIMR) and why is it used instead of the IMR?

A: The PIMR is the statutory interest maintenance reserve (IMR) adjusted to a pretax basis for each model segment. It is adjusted to a pretax basis because the minimum reserve calculation in VM-22 ignores the impact of income taxes. The PIMR is recognized as a reduction to the starting asset amount in determining the scenario reserve.

## Q 10.19: Are the assets backing the PIMR included in the starting assets?

A: The PIMR liability is described as a negative asset that equals the portion of the total company PIMR allocable to each model segment. The PIMR may be positive or negative. Section 4.B.1 notes that the value of the starting assets on the projection start date is reduced by the allocated PIMR. Conditions for allocating PIMR balances to the policies being modeled are provided in Section 7.D.7 of VM-20. Some actuaries will use the same approach to allocate the PIMR that is used for cash flow testing. Simplified approaches are explicitly allowed if the impact of the PIMR on the minimum reserve is minimal.

## Q 10.20: How will the actuary model negative assets when they arise in the projections?

A: When performing financial projections, cash outflows can exceed cash inflows. If the amount of net cash outflows is below certain corporate cash management threshold (e.g., 4% of reserves), the business could resolve the negative cashflow issue with short-term borrowing or other disinvestment strategies such as purchasing negative assets or selling existing assets. The Asset Adequacy Analysis Practice Note published by the American Academy of Actuaries has additional information about modeling disinvestment cash flows.

Negative assets may also be used to support the general account liability of separate account business at the beginning of the projection.

VM-22 Section 4.D.3.c requires the actuary to model a disinvestment strategy in accordance with the corporate disinvestment guideline. If short-term borrowing is involved, some actuaries assume the cost of borrowing to be no less than the average yield rate of reinvestment assets in order to avoid an arbitrage free opportunity for the insurer.

If the assumed disinvestment strategy is "purchasing negative assets" and the negative assets are assumed to be borrowed from other lines of business or the corporate, the lender's investment strategy could be used as the guidance for the assumed negative assets portfolio.

As the line of business becomes the pseudo-issuer of the negative assets, asset risks (such as default risk and prepayment risk) of the negative assets are likely to be based on the insurer's risk profile rather than the issuers of re-investment assets.

- Default Risk - The default risk and associated borrowing costs of a negative asset should be based on the insurer's own credit rating. For example, a B-rated company will generally face higher borrowing costs than an A-rated company.
- Salvage Value - The assumed salvage value may be reduced.
- Prepayment Risk - Some actuaries use a different prepayment assumption for negative assets because the line may not have the ability to redeem the negative assets until maturity. Even when the line intends to redeem, the corporate internal transaction provisions may deny the line from redeeming the negative assets without the consent of the lender (i.e., other lines or surplus).

If the amount of negative assets is immaterial, modeling negative assets is a viable disinvestment strategy. However, if the projected cash outflows exceed cash inflows for an extended period, some actuaries may use other disinvestment strategies (e.g., selling existing assets) to satisfy the net cash outflows as the alternatives may be closer to the insurer's actual cash management practice.

## Q 10.21: What approaches are acceptable to model asset disinvestments?

A: Section 4.D.3.c of VM-22 requires disinvestment to be modeled in a manner that is consistent with the company's investment policy and reflects the company's borrowing cost, if applicable (e.g., if borrowing is used to fund net negative periodic cash flows instead of disinvesting assets).

Some actuaries model funding of net negative periodic cash flows by selling assets according to a priority list that aligns with how the company manages its portfolio. For example, more liquid assets, assets with lower yields, assets with specified tax characteristics, or assets with lower bid spreads may be prioritized for sale to fund intermediate cash flow needs, while less liquid assets, assets with higher yields, or assets with higher bid spreads may be de-prioritized for sale. Spreads used in calculating the market value of assets sold are to be consistent with but not necessarily the same as the spreads used for purchases, recognizing that specific starting assets may have different characteristics than the modeled reinvestment assets.

However, buying negative assets or other techniques for modeling disinvestment are not prohibited by VM-22; some actuaries model the purchase of negative assets (i.e., borrowing money) at a rate that reflects the company's borrowing cost as opposed to selling initial or reinvestment assets. When borrowing is modeled, the assumed cost of borrowing should not be lower than the rate at which positive cash flows are reinvested in the same time period.

## Q 10.22: What approach is used to model asset defaults?

A: In VM-22 Section 4.D.4.a, default costs and the assumptions used to derive them follow the requirements in VM-20 Section 9.F. As described in VM-20 Section 9.F.1, a three-step process is required to determine default costs for fixed-income assets with an NAIC designation or NAIC commercial mortgage designation (i.e., corporate bonds, preferred stocks, residential mortgagebacked securities (RMBS), commercial mortgage-backed securities (CMBS), and commercial mortgages). Total annual default cost factors are calculated by projection year for each asset and are expressed as a percentage of the statement value each year. The default cost factors are the sum of three components:

- Baseline annual default cost factor. Cost factors are based on historical corporate default and recovery experience and include a margin for conservatism. Factor is a table "look-up" based on a "PBR credit rating" and weighted average life (WAL) of the asset.
- Spread related factor. Based on the corporate bond spread environment as of the valuation date. Adjustment can be positive or negative, and grades off over three years (subject to a floor and a cap).
- Maximum net spread adjustment factor. Portfolio-wide upward adjustments, graded off over three years, if the net spread of the portfolio exceeds the net spread of a "regulatory threshold" index bond.

A different prescribed methodology applies to fixed-income assets that lack an NAIC designation. This may include but is not limited to, some commercial mortgage loans, CMBS, RMBS, and residential mortgages (whole loans). VM-20 Section 9.F.5 provides the requirements for default cost factors for such assets without an NAIC designation.

With respect to reinvestment of fixed income security assets, VM-20 Section 9.F.6 provides guidance for their default determination process.

## Q 10.23: What company inputs are needed to determine the prescribed asset default rates for assets with an NAIC designation?

A: In VM-22 Section 4.D.4.a, default costs and the assumptions used to derive them follow the requirements in VM-20 Section 9.F. Per VM-20 Section 9.F.2, there are three items that need to be provided from company records:

- Investment expense assumption for each asset type.
- o This is the company's anticipated experience assumptions (with no margin).
- o Expressed as an annual percentage of statement value.
- Option adjusted spread (OAS) for each asset.

- o Average spread over zero coupon Treasury bonds that equates a bond's market price as of the valuation date with its modeled cash flows across an arbitrage free set of stochastic interest rate scenarios.
- o For floating rate bonds, the OAS equals the equivalent spread over Treasuries if the bonds were swapped to a fixed rate.
- o VM-22 allows for market conventions and other approximations.
- Weighted Average Life (WAL).
- o WAL equals the weighted average number of years until 100% of the outstanding principal is expected to be repaid (rounding to the term available in the WAL column).
- o For bonds or preferred stocks that are perpetual or mature after 30 years, the WAL shall be 30.
- o VM-22 allows for market conventions and other approximations.
- o WAL is considered by investment professionals as the weighted average of the times of the principal repayments, weighted by the amount of principal repayment; in other words, the WAL is the weighted average time until a dollar of principal is repaid.

## Q 10.24: How is the PBR credit rating used to determine asset default rates?

A: In VM-22 Section 4.D.4.a, default costs and the assumptions used to derive them follow the requirements in VM-20 Section 9.F. VM-20 Section 9.F.3 summarizes the determination of PBR credit rating to calculate asset default rates. VM-22 uses a numeric rating system from 1 to 21 to determine the credit quality of each asset. Table K, referenced in Appendix 2 in VM-20 and found on the Related Documents tab of the LATF page of the NAIC website (NAIC PBR Data Page) converts the ratings of NAIC Approved Ratings Organizations (AROs), NAIC designations, and NAIC commercial mortgage designations to this numeric rating system. A rating of 21 applies for any ratings of lower quality than those shown in the table.

The 1-21 PBR credit rating system attempts to provide a more granular assessment of credit risk than has been used for establishing NAIC designations for risk-based capital (RBC) and asset valuation reserve (AVR) purposes. Unlike for RBC and AVR, the VM-22 reserve cash flow models start with the gross yield of each asset and make deductions for asset default costs. The portion of the yield represented by the purchase spread over Treasuries is often commensurate with the more granular rating assigned, such as A+ or A-. Thus, use of the PBR credit rating system may provide a better match of risk and return for an overall portfolio in the calculation of VM-22 reserves. However, for assets that have an NAIC designation that does not rely directly on ARO ratings, a more granular assessment consistent with the designation approach is not currently available.

For an asset with an NAIC designation that is derived solely by reference to underlying ARO ratings without adjustment, the PBR credit rating is determined by taking the average of the numeric ratings corresponding to each available ARO rating, rounded to the nearest whole number. Corporate bonds are in this category.

For example, for a bond with an NAIC designation of 1 that is rated A+ by S&amp;P and A3 by Moody's, the PBR rating is 6, determined as follows:

S&amp;P rating of A+ -* PBR numeric rating of 5 (from Table K)

Moody's rating of A3 -* PBR numeric rating of 7 (from Table K)

PBR rating = average of 5 and 7 = 6

For a bond with an NAIC designation of 5 that is rated CCC by S&amp;P and Caa3 by Moody's, the PBR rating is 19, determined as follows:

S&amp;P rating of CCC -* PBR numeric rating of 18 (from Table K)

Moody's rating of Caa3 -* PBR numeric rating of 19 (from Table K)

PBR rating = average of 18 and 19 = 18.5 = 19 (rounded)

For an asset with an NAIC designation that is not derived solely by reference to underlying ARO ratings without adjustment, the PBR credit rating is determined by taking the second least favorable numeric rating associated with the NAIC designation. Non-agency RMBS and traditional private placements fall into this category. For example, for a private placement designated NAIC 1, there are seven potential PBR ratings shown in Table K, 1 through 7. So, the PBR rating is the second least favorable, that is, a PBR rating of 6.

For commercial mortgage assets with an NAIC commercial mortgage designation, Table K is used to look up the corresponding PBR credit rating.

Once the PBR credit rating is determined for each asset, the baseline default cost is a table "look-up" based on the PBR credit rating and the WAL of the asset.

## Q 10.25: What is the purpose of the spread related factor, and how is it used to determine asset default rates?

A: The purpose is to incorporate in the default cost the impact of current market spreads (i.e., spreads over Treasuries) on the valuation date, based on the premise that a portion of the difference between the current spread and historical spreads represents near-term expected default experience (could be a positive or a negative adjustment). The spread related factor is intended to mitigate short term fluctuation of default spreads due to severe market conditions such as the financial crisis in 2008.

A floor and cap have been provided to assure that this component cannot reduce the total default cost factor in year one by more than the baseline default cost factor and cannot increase the total default cost factor in year one by more than two times the baseline default cost factor. The cap is intended to help limit reserve volatility, which remains a concern for both the spread related factor and the maximum net spread adjustment factor. The spread related factor grades linearly from the prescribed amount in year one to zero in years four and after.

In VM-22 Section 4.D.4.a, default costs and the assumptions used to derive them follow the requirements in VM-20 Section 9.F. Per VM-20 Section 9.F.1.b, the prescribed amount in year one may be positive or negative and is calculated as follows:

- Multiply 25% by the result of (a) minus (b), where:
    - (a) equals the current market benchmark spread published by the NAIC consistent with the PBR credit rating and WAL of the asset on the valuation date (see Tables F and G on the Related Documents tab of the LATF page of the NAIC website (NAIC PBR Data Page) updated by NAIC on a monthly basis).
    - (b) equals the most current available historical mean benchmark spread published by the NAIC consistent with the PBR credit rating and WAL of the asset on the valuation date (see Tables H and I on the Related Documents tab of the LATF page of the NAIC website (NAIC PBR Data Page) updated by NAIC on a quarterly basis)
- The resulting amount shall not be less than the negative of the baseline annual default cost in year one and shall not be greater than 2 times the baseline annual default cost in year one.

## Q 10.26: What is the maximum net spread adjustment and how it is used to determine asset default rates?

A: The maximum net spread adjustment increases the required assumed default costs in the VM22 calculations if the average credit quality of the company's asset portfolio falls below the targeted threshold. The targeted threshold is a Baa2/BBB Bond (NAIC 2, PBR credit rating of 9).

In VM-22 Section 4.D.4.a, default costs and the assumptions used to derive them follow the requirements in VM-20 Section 9.F. Per VM-20 Section 9.F.1.c, for each model segment, a comparison is to be made of two spread amounts, both being net of the default costs calculated thus far and net of investment expenses. In each case, the gross option adjusted spread is based on current market prices at the valuation date.

- The first spread amount in the comparison represents the weighted average net spread of all the assets in the model segment, as if all the assets were purchased at their current market spreads.
- The second spread amount in the comparison represents the net spread for a portfolio of index Baa2/BBB bonds (NAIC 2, PBR credit rating of 9), as if the index Baa2/BBB portfolio were purchased at the current average market spread.

If the first result is higher than the second, additional default costs must be added to each asset until the two results are equal for the first projection year. This additional amount of default cost on each asset then grades off linearly in the model until it reaches zero in year four and after. This process is repeated each actual valuation date.

A company that invests in an asset mix earning an average gross spread greater than Baa2/BBB bonds initially, or an asset mix whose average market spread could widen significantly relative to market spreads for Baa2/BBB bonds, are examples of situations likely to trigger additional assumed default costs either initially or in the future.

The calculation is as follows:

The prescribed amount in year one shall be the excess, if any, of (a) over (b):

- (a) Weighted average net spread for the asset portfolio, calculated as follows:
1. For each asset, calculate a preliminary year one net spread equal to the option adjusted spread of the asset on the valuation date less the sum of the amounts from VM-20 Sections 9.F.1.a and 9.F.1.b (baseline and spread related factor) and less the investment expense for the asset.
2. Calculate a weighted average preliminary year one net spread for the total asset portfolio (i.e., assets subject to this section) using weights equal to each asset's statement value on the valuation date multiplied by the lesser of three years and the asset's WAL on the valuation date.
- (b) The net spread for a "hypothetical asset," which is called the "regulatory

threshold asset." The regulatory threshold asset is determined as follows:

- Calculate the preliminary year one net spread for a hypothetical asset with the following assumed characteristics (the regulatory threshold asset):
- o A PBR credit rating of 9 (equivalent to Baa2/BBB).
- o A WAL equal to the average WAL on the valuation date for the assets in the portfolio.
- o An option adjusted spread equal to the current market benchmark spread published by the NAIC for the assumed PBR credit rating and WAL (see Table F on the Related Documents tab of the LATF page of the NAIC website (NAIC PBR Data Page) updated by NAIC on a monthly basis).
- o Investment expense of 0.10%.
- The preliminary year one net spread is equal to the option adjusted spread of the hypothetical asset on the valuation date less the sum of the baseline and spread related

factor for the hypothetical asset, and less the investment expense for the hypothetical asset.

## Q 10.27: What are the default rates required in the VM-22 calculation for commercial mortgages, CMBS and RMBS investments, and residential whole loans?

A: In VM-22 Section 4.D.4.a, default costs and the assumptions used to derive them follow the requirements in VM-20 Section 9.F. If the asset does not have an NAIC designation or an NAIC commercial mortgage designation, per VM-20 Section 9.F.5, a prescribed default assumption is established such that the net yield shall be capped at 104% of the applicable historical U.S. Treasury yield rate most closely coinciding with the purchase date and maturity structure, plus 25 basis points. If the assets have an NAIC designation or an NAIC commercial mortgage designation, their default assumptions are determined according to VM-20 Sections 9.F.3 and 9.F.4.

VM-20 Section 9.F.5 only provides the cap on the net yield, and many actuaries seek additional advice from internal or external investment professionals.

## Q 10.28: If a company is using assets for which the modeling requirements are not explicitly defined in VM-22 (e.g., private fixed income assets, private equity assets, exotic derivatives, collateralized loan obligations, structured securities with underlying private fixed income assets as collateral, private asset backed securities, structured notes, rated feeder funds, letters of credit, contingent notes, etc.) , how should these assets be handled in the VM-22 calculation?

A:VM-22 is silent on the use and modeling treatment of such assets beyond the general principles in Section 1B and the broad guidance provided for general account assets in Section 4.D. The range of practice in modeling for these assets varies considerably depending on a number of factors, including:

- (i) the nature of the asset,
- (ii) the sensitivity of the asset cash flows to various economic variables,
- (iii) statutory book valuation requirements for the asset,
- (iv) the sensitivity of the asset's market value to various economic variables,
- (v) the similarity of the asset to traditional public fixed income and/or equity assets,
- (vi) the overall materiality of the asset in the company's portfolio,
- (vii) the materiality of the asset in the results of the reserve projection, and others.

In the absence of definitive guidance, some actuaries who intend to use such assets in a VM22 valuation may choose to obtain approval from their domiciliary regulator regarding the appropriate modeling approach. Other actuaries may look to guidance for modeling assets in other contexts (e.g., NAIC Model #787, Term and Universal Life Insurance Reserve Financing Model Regulation) for non-authoritative guidance.

As a general proposition, some actuaries believe that the best approach for modeling such assets is to model the cash flows, statutory book values, and market values from first-principles using the output from the economic scenario generator or, where necessary (e.g., when the economic scenario generator does not include output for all of the relevant variables needed to project the asset), using output from a non-prescribed scenario generator. Some actuaries may adjust other assumptions that are directly prescribed within VM-22 for more traditional fixed income assets (e.g., default charges, market spreads, etc.) and then apply these adjusted values to assets whose treatment is not directly prescribed. In making these decisions, some actuaries may be guided by the overall goal to maintain the targeted level of conservatism required in Principle 3 of VM-22 and to select assumptions on the conservative range of practice when limited data is available or when uncertainty around an assumption is higher.

As a hypothetical example, an actuary modeling private fixed income assets may be able to demonstrate from historical experience data that their company's private fixed income assets generally have slightly wider spreads and slightly higher long-run default charges than similarly rated public fixed income assets and may thus choose to model these assets by down-notching the rating for the private fixed income assets relative to their statutory classification and then use the long-run default charges for a similar public fixed income asset with similar weighted-average life. When determining the appropriate assumptions to use for assets whose modeling is not directly prescribed, such actuaries may apply general economic principles such as the guidance in Section 8 C. of VM-22 regarding nonprescribed scenario generators that an asset's expected return and potential risk should be consistent with other assets (sometimes referred to colloquially as the "no free lunch" principle). Other actuaries believe it is appropriate to model such assets using simplified valuation and projection techniques when it can be demonstrated that such modeling does not bias the projection results and does not materially understate the ultimate reserve. Such actuaries may consider and apply the guidance on approximations, simplifications, and model efficiency techniques in Section 3 J. of VM-22 when deciding on a modeling approach for a particular asset.

## Q 10.29: What if using the VM-20 spreads results in market values that are materially different from the statement values?

A: VM-22 Section 4.D.1.a states that starting asset values need to be consistent with their annual statement values, and that assets purchased during a projection, which can occur as early as the firsttime step in a projection, need to be valued in a manner consistent with the value of assets at the start of the projection that have similar investment characteristics (VM-22 Section 4.D.2).

VM-21 Section 4.D.3.iii prescribes spreads for non-callable corporate bonds that reflect current market conditions as of the projection start date and grade to long-term conditions based on historical data.

However, these "generic" spreads by credit rating and weighted average life may not necessarily reproduce the market values for the individual securities reported in the statutory statements. Some actuaries may add or subtract a security-specific spread to each starting asset so that the market values validate at the projection start date. These actuaries might hold such a spread constant for the duration of the asset or grade them off over time.

## Q 10.30 Is the additional asset portfolio subject to the alternative reinvestment strategy and PBR spreads and defaults?

A: Yes. As discussed in Section 4.B.3.1, the additional asset portfolio is meant to represent assets outside of the starting asset portfolio that the projection would not have a positive accumulated deficiency at the end of any projection year. Thus, the assets in the additional asset portfolio are subject to the same prescribed assumptions as the starting asset portfolio, including the prescribed spreads and defaults and the alternative reinvestment strategy floor.

## 11. Details on Scenarios/Scenario Generators/Economic Assumptions

## Q 11.1: What economic assumptions are stochastically generated?

A: The NAIC publishes the following files on a monthly basis:

- Basic\_Data\_Set\_YYYYMMDD
- Basic\_Data\_Set\_Validation\_Report\_YYYYMMDD
- Basic\_Data\_Set\_Additional\_Statistics\_YYYYMMDD
- Scenario\_Picking\_Data\_Set\_YYYYMMDD
- SERT\_Scenarios\_Set\_YYYYMMDD
- Initial\_Treasury\_Fitting\_and\_State\_Variables\_YYYYMMDD

The prescribed economic scenario generator produces the following economic parameters in separate columns with rows for each time period for 12 months and 100 years:

- 33 points of Treasury rates at maturities of 1 month, 3 months, 6 months and 1 - 30 years for both spot and coupon rates
- 8 Bond markets with income and price returns for: International Government Bonds, Long Term Investment Grade Corporate Bonds, Money Market, Short Term Government Bonds, Long Term Government Bonds, Short Term Investment Grade Corporate Bonds, High Yield Corporate Bonds, and International Investment Grade Corporate Bonds
- 6 Equity markets with income (dividend) and price returns for: Large Cap, Small Cap, Aggressive US Equity, Mid Cap, Aggressive Foreign Equity, and International Diversified Equity

Treasury spots are expressed as continuously compounded rates and the coupons are expressed as bond equivalent (semi-annual compounded) rates.

Bond and Equity returns are expressed with income and price columns. The total return is defined by adding the income and price columns.

For an additional fee, a Robust Data Set can be provided that contains, on a consistent basis as the Basic Data Set, stochastic scenarios for credit spreads, additional equity indices and returns on alternative investments and other asset classes.

Actuaries may or may not choose to generate other measures stochastically, including inflation rates, or currency exchange rates, or volatility rates for the equity and bond return indices. Consideration should be given to the internal consistency of other stochastic quantities with the scenario data.

The Basic Data Set contains 10,000 scenarios produced on a monthly timestep basis, requiring significant data storage (e.g. 3 plus GB zipped and over 10 GB unzipped). To optimize model run times and manage data capacity, some practitioners elect to download the minimum sized scenario subset needed for their specific valuation or remove unused and unneeded Treasury maturities, bond indices and equity indices, rather than keeping these large data sets within the working model. Including these large files within the working actuarial model will also increase the time to distribute the model to grid nodes during distributed processing runs.

Alternatively, instead of using the static sets of scenarios available for free on the NAIC website, modelers may consider using the dynamic application programming interface (API) available for a fee or use a non-prescribed dynamic replicating tool that is optimized for distributed processing. A

versatile API could be used for both time 0 valuation and for future projection periods, as long as initial state variables are fitted to future time steps.

## Q 11.2: How would actuaries generate the scenarios for the VM-22 calculations?

A: VM-22 prescribes a generator of economic scenarios (GOES) to generate scenarios for VM-22 calculations, see VM-20 Appendix 1 for a full description. Alternatively, a non-prescribed economic generator may be used as long as the scenarios are provided in an electronic spreadsheet for regulator review and the VM-22 reserve using the non-prescribed scenario generator is greater than or equal to the VM-22 reserve using the prescribed GOES. The GOES will be used by the NAIC to publish scenario sets on a monthly basis. The NAIC's Life Actuarial Task Force and Life RBC working group are charged with oversight and model governance of GOES. It is not expected that underlying parameters used in the models will change frequently.

GOES refers to the 10,000 scenarios published on the NAIC website and not the GEMS platform that underpins the NAIC's official GOES scenarios. GEMS itself is fundamentally a proprietary software owned by Conning. This implies that if the 10,000 scenarios are created by any other tool, other than GEMS, and the tool produces exactly the same scenarios as the 10,000 published by GOES, then this would not be considered a non-prescribed generator, since it matches the prescribed scenarios.

Alternatively, companies can pay a fee to obtain either (i) the GOES API to generate the scenario data sets or (ii) a full license to the GOES software.

## Q 11.3: How many scenarios are run to determine the Stochastic Reserve?

A: The current version of VM-22 does not define the appropriate number of scenarios to run. The prescribed scenario generator allows the user to choose the "full set of 10,000 scenarios," as well as representative scenario subsets using the scenario picking tool under the NAIC Economic Scenarios link within the "Documentation" tab in the section "Documentation Describing the ESG". The scenario picking tool offers the Significance Measure based on the 20-year UST (similar to the Academy Interest Rate Generator (AIRG)) or the Gross Wealth Factors based on Large Cap Equity returns. The user can select any scenario subset less than 10,000. Before generating a subset, the user must go to the "Filter Values" tab and replace column B "Significance Value" and column C "Large Cap GWF" with the applicable columns in the Scenario\_Picking\_Data\_Set\_YYYYMMDD where YYYY is the year of valuation, MM is the month and DD is the day.

From this, some actuaries would run all 10,000 scenarios to meet the regulatory requirements under VM-22, while some actuaries would use fewer than the 10,000 scenarios. See Q 12.4 for additional details.

## Q 11.4: How would the actuary determine the appropriate number of scenarios if less than the full 10,000 scenario set is used?

A: There are several reasons an actuary may choose to use fewer scenarios than the full 10,000 scenario set, including managing model run time or reducing the complexity of sensitivity tests.

Section 3.J indicates that the use of fewer scenarios rather than a higher number of scenarios is permissible as a model efficiency technique provided that:

- The smaller set of scenarios is generated using the prescribed scenario picker tool or
- A non-prescribed picking tool that complies with Section 3.J.

Section 3.J states that a company may use simplifications, approximations and modeling efficiency techniques provided that:

- The company can demonstrate that the use of such techniques does not understate the reserve by a material amount, and
- The expected value of the reserve calculated using simplifications, approximations, and modeling efficiency techniques is not less than the expected value of the reserve calculated that does not use them.

The "Significance Measure" scenario picker tool relies on either the 20-year Treasury rate or gross wealth factor for large cap equities for scenario selection. Thus, for products that are sensitive to other maturities, the scenario picker may not be an effective scenario reduction technique, and testing will be required to demonstrate compliance with the requirements of Section 3.J. Similarly, for products that are sensitive to equity or bond performance, the "Large Cap GWF" may not be an effective scenario reduction technique for other indexes, and testing will be required to demonstrate compliance with the requirements of Section 3.J.

Additional information on the use of CTE estimator as a measure of sampling error can be found in the response to Q4.3 of the VM-21 Practice Note Supplement.

VM-22 does not specify how to demonstrate compliance with Section 3.J or how to perform the periodic analysis of different numbers of scenarios. Some actuaries might follow a process similar to the following:

1. Select a subset of the scenarios.
2. Select a representative subset of the liabilities.
3. Calculate reserves across the subset of scenarios using the tentatively selected subset of the liabilities and also using the entire in-force business population. If these results are similar, then the actuary might reasonably conclude that the subset of the liabilities (i.e., the smaller or representative model) is appropriate to use to measure the appropriateness of a scenario subset. If reserves are materially smaller using the subset of liabilities, repeat steps 2 and 3 using a different or larger subset of liabilities.
4. Finally, calculate reserves for the subset of the liabilities across both the reduced set of scenarios and the full set of scenarios. If the reserves calculated for the subset of liabilities using the scenario subset are not materially smaller than the reserves calculated for the subset of liabilities using all the scenarios, then the actuary might reasonably conclude that the subset of scenarios is appropriate to use.
5. If reserves are materially smaller using the subset of scenarios, repeat step 3 using a larger subset of scenarios to determine if an appropriate subset can be selected.

Some actuaries might conclude that if the same technique is used to pick a representative subset of the liabilities in successive periods, then it is not necessary to revalidate the appropriateness of that liability subset for use in validating scenario subsets. Some actuaries might conclude that it is necessary to repeat this process only when the characteristics of the liabilities, the assets backing them, or the economic environment have materially changed.

## Q 11.5: What if there are a lower number of scenarios that results in a higher reserve than a greater number of scenarios?

A: VM-22 does not prevent the actuary from selecting a scenario subset that produces a reserve that is greater than that produced using the full set of 10,000 scenarios. Some actuaries would hold the lower reserve based on the larger number of scenarios to take into account the additional credibility of the larger scenario set. Other actuaries would hold the higher reserve based on the smaller scenario set (if in the actuary's judgment the number of scenarios in the smaller scenario set is reasonable for the purpose of calculating the Stochastic Reserve requirement).

## Q 11.6: Can the actuary use scenarios other than prescribed scenarios for calculating the Stochastic Reserve?

A: Yes, if the scenarios produce a more conservative Stochastic and Deterministic Reserve. Section 1.A states that the VM-22 requirements establish the minimum reserve valuation standard. Section 8 on Scenario Generation describes both the use of a "prescribed" or "non-prescribed" generator. The use of non-prescribed scenarios is allowed as long as they produce a reserve in excess of the minimum requirement or are exactly equal to the 10,000 published GOES scenarios. Some actuaries wishing to use other than prescribed scenarios to determine statutory reserves may need to work with their tax department to understand any implications for the calculation of tax reserves.

## Q 11.7: How are separate account funds mapped into the specific equity return indices of the prescribed economic scenario generator?

A: Per Section 8.C of VM-22, the company shall design an appropriate proxy for each variable subaccount in order to develop the investment return paths and map each variable account to an appropriately crafted proxy fund normally expressed as a linear combination of recognized market indices.

Actuaries might wish to effect modeling of funds in different ways. For example, some actuaries might perform a regression of past fund performance against past performance of market indices consistent with the scenario generator classifications and develop a scenario set for each such fund that is consistent with an appropriate weight of such scenarios derived from the regression.

Alternatively, funds might be decomposed using regression techniques into funds corresponding to each of the indices.

## Q 11.8: How can the actuary obtain the scenarios used for the Stochastic Exclusion Ratio Test?

A: VM-22 Section 7.C requires that the same prescribed economic scenario generator used for stochastic scenario generation be used to generate the 16 scenarios used for the Stochastic Exclusion Ratio Test. These are produced by downloading the applicable SERT\_Scenarios\_Set\_YYYYMMDD for the valuation year YYYY, month MM and day DD from the NAIC website.

## Q 11.9: How can the actuary obtain the scenario used for the Deterministic Reserve?

A: VM-22 Section 7.E specifies that the Deterministic Reserve is to be calculated using scenario 12 from the set of prescribed scenarios used in the Stochastic Exclusion Ratio Test.

## Q 11.10: What changes are made to the prescribed economic stochastic scenario generator parameters for non-U.S. economies?

A: Section 8 provides for both prescribed and non-prescribed scenario generation. That said, some actuaries might conclude that it is unreasonable to use the prescribed scenario parameters for nonU.S. interest rates. In a situation where non-U.S. interest rates are required, some actuaries may deem it appropriate to use a non-prescribed generator. Adjustments to the prescribed generator may not be appropriate since underlying parameters were developed using historic US interest rates and the generalized fractional floor was set to a negative rate level anticipated or observed for US interest rates. In addition, some actuaries might wish to update volatility, correlation, and other parameters to be consistent with the market in question.

For equity returns in non-U.S. markets, the actuary might want to use techniques similar to what is used for U.S. funds to map each fund into one or more of the funds generated by the prescribed economic scenario generator. Section 8.C.4 states that if a proxy fund cannot be appropriately mapped to some combination of the prescribed returns, the company shall determine an appropriate return using a non-prescribed generator and disclose the rationale for determining such return.

## Q 11.11: How does the actuary generate interest rates for maturities not generated by the economic scenario generator?

A: The prescribed economic scenario generator now includes a complete 33-point yield curve including most terms to maturity. For some purposes, the actuary might need a full set of interest rates at other intermediate maturities. A range of options are available for this. VM-22 gives no guidance.

Techniques some actuaries might find reasonable could include, but would not be limited to, the following:

- Linear interpolation;
- Bootstrapping the curve to find forward rates that increase linearly between the given maturity points and are consistent with the given rates;
- Cubic spline interpolation.

## Q 11.12 How are scenarios generated for VM-22 calculations?

A: Per Section 3.K of VM-22, the calculation of the Stochastic and Deterministic Reserves can be performed as of a date up to three months prior to the valuation date as long as an appropriate method is used to adjust the reserves to the valuation date.

Some actuaries generate refreshed scenarios as of each valuation date. Others use scenario data from up to three months prior to the valuation date, although in this case, the actuary will need to use an appropriate method to adjust the reserves to the valuation date. If a model segment is not sensitive to the economic environment, actuaries may choose to generate new scenarios on a less frequent basis, keeping in mind the requirements for making simplifications in Section 3.J.

If fewer scenarios than the full set of 10,000 scenarios are used, then the subset of scenarios are reproduced each time scenarios are generated. The filter values tab of the scenario-selection-tool-

040324.xlsx column B for Significance Values column C for Large Cap GWF needs to be updated with the applicable Scenario\_Picking\_Data\_Set\_YYYYMMDD and Basic\_Data\_Set\_YYYYMMDD, where YYYYMMDD is the valuation date or 3 months prior.

See Question 12.2 for more details on documentation on the prescribed generator provided on the NAIC website.

## Q 11.13: What are some considerations for a company using scenario stratification or reduction techniques?

A: VM-31, Sections F.9.c and d require documentation of the rationale used to select the number of scenarios and any scenario reduction technique and that the approach does not materially understate reserves. Periodic testing, perhaps with a representative or simplified model, might be considered to confirm that results with a stratified set of scenarios are sufficiently close to results from the full set of scenarios and do not materially understate reserves.

Companies may pick a different subset of scenarios if deemed relevant based on the underlying liabilities, this includes both the numbers of scenarios picked and the scenario subset picking approach. For example, a company may want to reflect different factors (interest rates, equity returns, corporate bond fund returns) in their scenario subset approach for FDA and FIA products.

Note that using the provided scenario picking tool does not exempt a company from the requirements outlined in VM-22 Section F regarding the number of scenarios.

## Q 11.14: What components of the GOES are prescribed and what requires a demonstration satisfying the requirements of VM-22 Section E?

A. The use of any interest rates, equity returns, and separate account fund returns not included within the scenario set released by Conning on the NAIC portal (https://naic.conning.com/scenariofiles) is considered a non-prescribed generator and must meet the requirements outlined in VM-22 Section E.

Note that the use of a blend of markets from the prescribed scenarios is permissible and not subject to the requirements of VM-22 Section E.

## Q 11.15: How might a company determine the projected implied volatility for the GOES?

A. VM-22 Section D indicates that the projected implied volatility scenario is left to company judgement. Companies may elect to leverage Conning as the provider of the GOES to gain insight into the implied volatility surface consistent with the scenario returns or develop an internal methodology aligned with the key considerations laid out in VM-22 Section D.

## 12. Setting Prudent Estimate and Anticipated Experience Assumptions

## Q 12.1: How are prudent estimate assumptions determined?

A: VM-01 defines margins and prudent estimate assumptions, where prudent estimate assumptions equal anticipated experience assumptions plus a margin. The margin may increase or decrease the assumption as appropriate to cover adverse deviations and estimation error of the assumed risk factors. The margin should result in a larger reserve than would otherwise result without it. Assumptions that are stochastically modeled are considered material risks, but there is no requirement in VM-22 to add a margin to assumptions that are stochastically modeled because the applicable conditional tail expectation (CTE) measure provides a margin. Per Section 12.B.4, it is expected that companies will not stochastically model risk factors other than economic scenarios until VM-22 provides more specific guidance. Companies must discuss with their domiciliary regulator if they wish to stochastically model other risk factors.

VM-22 requires a margin for each material risk factor. If sensitivity testing shows that the risk factor does not have a material impact on the reserve, some actuaries will establish the prudent estimate assumption for this risk factor without separately identifying a margin.

Some actuaries may also review the Academy's "Life Principle-Based Reserves (PBR) Assumptions Resource Manual" for guidance in setting assumptions.

Section 4.3 of ASOP No. 1, Introductory Actuarial Standard of Practice, states: "Actuaries are responsible for determining which ASOPs apply to the task at hand." Relevant actuarial standards of practice may include, but are not limited to, the following:

| ASOP No. 2   | Nonguaranteed Charges or Benefits for Life Insurance Policies and Annuity Contracts                                                                 |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| ASOP No. 7   | Analysis of Life, Health, or Property/Casualty Insurer Cash Flows                                                                                   |
| ASOP No. 11  | Treatment of Reinsurance or Similar Risk Transfer Programs in Financial Reports                                                                     |
| ASOP No. 15  | Dividends for Individual Participating Life Insurance, Annuities, and Disability Insurance                                                          |
| ASOP No. 22  | Statements of Opinion Based on Asset Adequacy Analysis by Actuaries for Life Insurance, Annuity, or Health Insurance Reserves and Other Liabilities |
| ASOP No. 23  | Data Quality                                                                                                                                        |
| ASOP No. 25  | Credibility Procedures                                                                                                                              |
| ASOP No. 27  | Selection of Assumptions for Measuring Pension Obligations                                                                                          |

## Q 12.2: Should margins be determined in aggregate or independently for each behavior assumption?

A: Per Section 10.B.3, the company must determine prudent estimate assumptions independently for each behavior unless the company can demonstrate that an appropriate method was used to determine the level of margin in aggregate for two or more material behavior assumptions.

## Q 12.3: How are material risk factors assessed?

A: Section 1.D requires the company to establish a standard containing the criteria for determining whether an assumption, risk factor, or other element of the principle-based valuation has a material impact on the size of the reserve. This standard must be applied when identifying material risks and is based on the impact relative to the size of the reserve, as opposed to the impact relative to the overall financial statement (e.g., total company reserves or surplus). This materiality standard must be documented in Annuity Summary required by VM-31. Although an actuary might use a broader view of materiality when assessing assumption setting for alternative purposes or bases, this may not be appropriate for VM-22.

Section 1.B Principle 3 and requirements in Section 12.C provide guidance on which risk factors are categorized as material risks.

The standard also applies to exclusion tests.

## Q 12.4: Are the same prudent estimate assumptions used for deterministic and stochastic calculations?

A: Section 3.D for SR and Section 3.E for DR both point to Section 3.I for determining prudent estimate assumptions. Some actuaries would use the same assumptions except where the risk factor is scenario-dependent, e.g., dynamic lapses due to changes in projected interest rates

## Q 12.5: Which risk factors do not require a prudent estimate assumption?

A: According to Sections 10.E.1 and 12.B.1, the company is not required to develop prudent estimates for assumptions that are stochastically modeled. Per Section 12.B.3, risk factors that must be stochastically modeled, and therefore do not require prudent estimate assumptions, include interest rate movements (i.e., Treasury interest rate curves) and equity performance.

Some actuaries might not develop a prudent estimate assumption for risk factors that do not materially affect modeled reserves as permitted by Section 12.C.4. In this case, anticipated experience assumptions should be used pursuant to Section 12.B.5.

## Q 12.6: How will actuaries set anticipated experience assumptions?

A: Per Section 12.B.5, the actuary must use company experience, if relevant and credible, to establish the anticipated experience assumption for any risk factor. To the extent the company experience is not available or credible, the actuary may use industry experience or other data to establish the anticipated experience assumption, making modifications as needed to reflect the circumstances of the company.

Per Section 12.B.5.b, for risk factors that do not lend themselves to use of statistical credibility theory, and for risk factors to which statistical credibility theory can be appropriately applied but cannot currently be applied due to a lack of industry data, the company must establish anticipated experience assumptions in a manner that is consistent with accepted actuarial practice and that reflects any available relevant company experience, any available relevant industry experience, or any other experience data that are available and credible.

Some actuaries develop anticipated experience assumptions based on the assumptions used for pricing and development of the product. Many actuaries consider whether it is necessary to work closely with the product development actuary to understand the basis for assumptions and review the studies performed prior to using them in the reserve calculations to assure they meet the criteria set in Section 12.B.5.

## Q 12.7: Can actuaries use company experience if it predates the effective date of VM-22?

A: Some actuaries will use company experience that predates the effective date of VM-22 if it is relevant and credible for the assumption or margin that is being determined. There is no requirement in VM-22 that the experience data used to determine anticipated experience assumptions and/or margins for prudent estimate assumptions has to occur on and after the effective date of VM-22. Section 11.B.4.c states that in determining expected mortality curves, the "age" of the experience data should be documented.

## Q 12.8: When will the actuary update the anticipated experience assumptions?

A: Section 12.B.5.e requires the actuary to annually review relevant emerging experience, and Section 12.B.2 requires that the assumptions be periodically reviewed and updated. Therefore, it is expected that actuaries will update assumptions if there is new experience data or other information that changes the actuary's assumptions of anticipated experience. Actuaries will evaluate the materiality of the assumptions using the results of sensitivity tests, company practice for updating assumptions, and the credibility of the new data and other information in determining whether to update the experience assumptions. Experience assumptions are not locked in at issue.

## Q 12.9: What data sources are used to set anticipated experience assumptions?

A: Per Section 12.B.5, the company must use its own experience, if relevant and credible, to set anticipated experience assumptions. In instances where company-specific data is not available or credible, actuaries might wish to consider looking to alternative sources as discussed in Section 12.B.5.

A non-exhaustive list of possible data sources to consider for developing anticipated experience assumptions is listed below:

- Company data on the same or similar products
- Industry or reinsurer data on the same or similar products
- General population data
- Predictive models or algorithms
- Statistical methods such as conservation of deaths or the "Dukes-MacDonald" method
- Sound actuarial judgment, if risk factors have limited or no experience, or other applicable data available

For assumptions that are established based on limited data, Section 12.B.5 requires the actuary to sensitivity test the assumption chosen to ensure the assumption is set at the conservative end of the plausible range.

## Q 12.10: What other issues would the actuary take into account when setting anticipated experience assumptions?

A: The actuary may wish to consider whether anticipated experience assumptions developed from the data should be modified as needed to reflect the circumstances of the company. For example, the actuary may wish to consider adjusting assumptions that are based on historical experience to consider contractual guarantees that are present in the contracts being valued that were not present in the contracts that contributed to the experience base. For example, if a company's contracts include rich in-the-money guarantees but the experience base does not, the actuary may wish to consider adjusting assumptions. The actuary may also wish to consider the possibility of anti-selection affecting assumptions. For example, anti-selection may involve a combination of lapses, persistency, mortality, and the level of guarantees.

The actuary may also wish to consider reviewing contractual guarantees to determine whether and to what degree these contractual guarantees will impact future cash flows of the model.

## Q 12.11 Should extreme behavior be included in calculation?

A: Section 10.D.7 states that the company should neither assume that all contract holders act with 100% efficiency in a financially rational manner nor assume that contract holders will always act irrationally. These extreme assumptions, however, may be used for modeling efficiency if the result is more conservative. Per Section 10.D.4, however, the company must assume that policyholders' efficiency will increase over time without relevant and credible experience to the contrary. Note that technological advancements and increased consumer access to information may increase policyholder efficiency over time.

## Q 12.12: How do trends in data affect the anticipated experience assumption?

A: Some actuaries assess a granular subset of data for comparison to experience of other exposure periods. An example of this analysis would be in comparing lapse data for a certain product over calendar years 2017- 2021 to the same grouping over calendar years 2022-2026. For these comparisons, the actuary would confirm the data used continues to be relevant and credible at this level, as stated in Section 12.B.5.

Some actuaries project trends that in their judgment are likely to be sustained in the future in the anticipated experience assumption, subject to any applicable restrictions. Some actuaries make a judgment on the uncertainty surrounding the projection of the trend and increase the margin as uncertainty increases, such as in later durations.

Specific to mortality, for purposes of the adjustment for credibility, the industry mortality table may be adjusted for a mortality segment and must be adjusted for a longevity segment to reflect mortality improvement according to Section 11.C.2.

Per Section 11.C.4, up to the valuation date it is required that the credibility adjusted table used for longevity segments be adjusted for mortality improvement using the applicable mortality improvement scale described in Section 11.B.3 from the experience weighted average date to the valuation date. This is also permitted, but not required, for mortality segments.

Per Section 11.D, the prudent estimate mortality assumption must be adjusted for mortality improvements beyond the valuation date if such an adjustment would serve to increase the resulting DR or SR. If such an adjustment would reduce the DR or SR, reflecting mortality improvement is permitted, but not required. The mortality improvement assumption must be based on current relevant data with a margin for uncertainty (increasing assumed rates of improvement if that results in a higher reserve or reducing them otherwise).

In Section 12.B.5, the last paragraph states that "the qualified actuary, to whom responsibility for this group of policies is assigned, must annually review relevant emerging experience for the purpose of assessing the appropriateness of the anticipated experience assumption. If the results of statistical or other testing indicate that previously anticipated experience for a given factor is inadequate, then the qualified actuary must set a new, adequate, anticipated experience assumption for the factor."

## Q 12.13: How does the actuary determine whether company experience data is credible?

A: A discussion of credibility in the context of the mortality assumption is found in Section 15 of this practice note. ASOP No. 25, Credibility Procedures, is available on the Actuarial Standards Board's website. To determine the credibility of company experience data, some actuaries might use concepts from classical credibility theory. In this sense, the actuary may determine that full credibility (i.e., the subject experience will have full predictive value) has been achieved when there are sufficient observations such that the actual frequency of an event falls within a defined percentage of the expected results, given a specified probability.

Additional adjustments to the definition of full credibility may be used in cases where the actual observed events can range in their magnitude of severity. The Credibility practice note 1 has further details on this subject. Further guidance regarding credibility in the context of mortality can be found in Section 11.C.3.

If the number of observations is fewer than the amount needed for full credibility, partial credibility of the data may be established. This can be done by using information such as the expected number of observations and the number of observations needed for full credibility.

Some actuaries with data that is only partially credible might use actuarial judgment to combine partially credible data with other industry experience to determine their anticipated experience assumptions. Some actuaries also increase the margin where company experience data is only partially credible.

## Q 12.14: Would the actuary perform sensitivity testing to set anticipated experience assumptions or prudent estimate assumptions?

A: Yes. Section 12.B.6 requires sensitivity testing for assumptions that are not stochastically modeled to understand the impact this testing has on the modeled reserve. The sensitivity testing must be updated periodically as appropriate. Section 12.B.6 states that the company may test less frequently when the tests show less sensitivity of the modeled reserve to changes in the assumptions being tested or that the experience is not changing rapidly, but no less frequently than every three years. Section 12.B.6 provides a guidance note that clarifies sensitivity analysis is not required on an annual basis.

To perform the sensitivity testing, some actuaries use anticipated experience assumptions. Other actuaries instead perform the sensitivity testing using prudent estimate assumptions.

If sensitivity testing shows that an assumption is material to the modeled reserve, Section 12.C.3 states that greater analysis and more detailed justification are needed to determine the level of uncertainty when establishing margins for risk factors that produce greater

1 Available on the Academy's website at http://www.actuary.org/files/publications/Practice_note_on_applying_credibility_theory_july2008.pdf.

sensitivity on the modeled reserve. Therefore, it might be prudent for the actuary to review the credibility of the data used to set the assumption and whether the assumption is set at the appropriate level.

## 13. Setting Margins

## Q 13.1: What types of risks require margins?

A: Material risks require margins. VM-22 Section 12.B.1 states that the company must use prudent estimate assumptions for risk factors that are not stochastically modeled by applying a margin to the anticipated experience assumption for the risk factor, if such risk factor has been categorized as a material risk. Section 12.C.1 categorizes risks as summarized below.

1. Risks that must be considered material risks
- Risks that are stochastically modeled (e.g., interest rates, equity returns)
- Risks that have prescribed margins or guardrails (e.g., assets, revenue sharing)
2. Risks that are generally considered material risks. These include but are not limited to:
- mortality
- contract holder behavior
- maintenance expenses
- overhead expense
- Inflation
- implied volatility
3. Risks that may be considered material risks in some cases. These risks include:
- acquisition expenses
- morbidity (e.g., LTC riders)
- partial withdrawals
- policy loans
- annuitizations
- account transfers and deposits
- non-guaranteed elements, and/or option elections that contain an element of anti-selection

## Q 13.2: Is there a standard for determining which risks are categorized as material risks?

A: Yes. VM-22 Section 1.D states that the company must establish a standard containing the criteria for determining whether an assumption, risk factor or other element of the principle-based valuation has a material impact on the size of the reserve. This standard must be applied when identifying material risks and is based on the impact relative to the size of the reserve, as opposed to the impact relative to the overall financial statement (e.g., total company reserves or surplus). For example, the standard may be expressed as an impact of more than X dollars or Y% of the reserve, whichever is greater.

Note that VM-31 Section 3.E.1 requires disclosure of the standard established by the company.

## Q 13.3: What are the VM-22 requirements when determining appropriate margins?

A: Regarding contract holder behavioral assumptions, VM-22 Section 10.B.3 states that the company must determine an explicit set of initial margins for each material risk independently unless the company can demonstrate that an appropriate method was used to determine the level of margin in aggregate for two or more material behavior assumptions. If applicable, the actuary may apply an adjustment to take into account the fact that risk factors are not normally 100% correlated. VM-22 Section 12.C.1 states that it is not permissible to adjust the initial margin to recognize, in whole or in part, implicit or prescribed margins that are present, or are believed to be present, in other risk factors. For example, if lapses are a material risk, it is not permissible to reduce or eliminate the lapse margin because the prudent estimate mortality assumptions are conservative. Per VM-22 Section 12.C.4, a margin is permitted but not required for assumptions that do not represent material risks.

VM-22 Section 12.C.2 states that higher margins should be used when:

- The experience data has less relevance or lower credibility;
- The experience data are of lower quality, such as incomplete, internally inconsistent, or not current;
- There is doubt about the reliability of the anticipated experience assumption, such as, but not limited to, recent changes in circumstances or changes in company policies; or
- There are constraints in the modeling that limit an effective reflection of the risk factor.

Greater analysis and more detailed justification are required when establishing margins for risk factors that produce greater sensitivity on the modeled reserve.

VM-22 Section 12.C.5 states that a margin should reflect the magnitude of fluctuations in the historical experience of the company for that risk factor, as appropriate.

VM-22 Section 12.C.6 states that the company must apply the method used to determine the margin consistently on each valuation date but is permitted to change the method from the prior year if the rationale for the change and the impact on modeled reserve is disclosed. VM-22 Sections 11.A.4 and 10.B provide specific requirements for setting margins for mortality and contract holder behavior, respectively.

## Q 13.4: What other references are available when determining appropriate margins?

A: Many actuaries use the following:

- Life Principle-Based Reserves (PBR) Assumptions Resource Manual
- A Society of Actuaries research paper titled Analysis of Methods for Determining Margins for Uncertainty Under a Principle-Based Framework for Life Insurance and Annuity Products (March 31, 2009).
- ASOP No. 52, Principle-Based Reserves for Life Products under the NAIC Valuation Manual, adopted September 2017.
- The C3 Phase III Report and associated practice note.
- The AG-43/C3 Phase II practice note.
- VM-20 Practice Note and VM-21 Practice Note Supplement
- Internal documentation of margins used for other financial reporting methods.
- Various Canadian valuation technique papers and educational notes
- ASOP No. 25, Credibility Procedures

## Q 13.5: What general methods are used in setting margins?

A: Some actuaries focus on the key assumptions (those that are most material) for the underlying product first and then analyze how those margins affect other assumptions. For example, for a fixed annuity with a guaranteed living benefit product, the actuary might initially focus on setting the anticipated utilization and margin assumptions (because it is likely the most material risk factor) and then set other assumptions such as lapse rates and expenses such that these assumptions are internally consistent with the utilization assumption. One advantage of concentrating on the key assumptions is avoiding situations where the margin applied to one assumption affects the direction of the appropriate margin for another. For example, applying a high utilization margin may cause lower, rather than higher lapses to be a conservative assumption.

Some actuaries would develop an approach to setting margins in a manner consistent with the underlying principle of reflecting the underlying risk characteristics of the product.

## Q 13.6: When can and how does the actuary apply an adjustment in setting the margins to account for risk factors not being 100% correlated?

A: Per VM-22 Section 10.B, the initial level of a particular margin may be adjusted to take into account the fact that risk factors are not normally 100 % correlated. The initially determined margin may only be reduced to the extent the company can quantitatively demonstrate and document that an appropriate method was used to determine the level of margin in the aggregate for two or more material behavior assumptions, if relevant to the risks in the product, and thus the approach will not understate the reserves.

Industry practice determining covariance adjustments is expected to evolve over time.

## Q 13.7: Does the sensitivity of an assumption's impact on the overall reserve level affect how the margin is set?

A: Yes. VM-22 Section 12.B.6 requires companies to sensitivity test risk factors that are not stochastically modeled and examine the impact on the modeled reserve. VM-22 Section 12.C.3 states that in complying with these sensitivity testing requirements, greater analysis and more detailed justification are needed to determine the level of uncertainty when establishing margins for risk factors that produce greater sensitivity on the modeled reserve. One approach to determine the uncertainty of a risk factor is to measure the standard deviation around the mean or other standard statistical measure (if meaningful historical experience data is available for the risk factor).

## Q 13.8: Are there instances where it may be appropriate to use no margin, or to use a small margin?

A: Yes. VM-22 Section 12.C.4 indicates that a margin is not required for assumptions that do not represent material risks.

It could be appropriate to use a small margin for some assumptions. Some actuaries use small margins for risk factors having a material impact on the reserves but little uncertainty. For example, if an expense assumption has a large impact on the reserve but is known with certainty (it has been outsourced for a fixed contractual cost), then a smaller margin could be appropriate.

## Q 13.9: Are there additional considerations for setting margins for specific assumptions?

A: The specific considerations for mortality (Q 15.1), contract holder behavior (Q 16.3), expense margins (Q 17.8), and index credits (Q 14.15) are further discussed in this practice note.

## Q 13.10: To what extent does the size of the company affect the size of the margins used?

A: Some actuaries would not modify the size of the margins based solely on the size of the company. For example, smaller margins generally coincide with a reduction in uncertainty that might be due to a large number of observations but is not necessarily dependent on company size because a large number of observations could be generated over time from a smaller company.

## Q 13.11: What are the considerations for setting margins across blocks of business?

A: Some actuaries would assess whether the margins were appropriate by product as well as adequate over a broad set of contracts. This assessment would be particularly useful for products with uncertain risks or particularly unique characteristics. Some actuaries would review the margins in aggregate, particularly where contract characteristics are similar or have homogeneous risks. Note that per Section 10.B.3, margins may not be determined at an aggregate level

VM-31 Section 3.F.16.b requires disclosure of the specific sensitivity tests performed for each risk factor or combination of risk factors and an explanation of how the results of sensitivity tests were used or considered in developing assumptions. If a model segment contains multiple distinct product types, this is done for each product type.

## Q 13.12: How are margins set when the impact of assumption movements changes over the duration of the business?

A: For some products, the impact on the aggregate reserve of increasing or decreasing an assumption may vary according to the contract duration. Consistent with the concept of margin determination described earlier, the company must perform testing to determine whether the modeled reserve is materially impacted by variations in the size and direction of the margin and must do so using a methodology that recognizes that the appropriate size and/or direction of a margin in the early durations may be quite different from that in later durations. If the impact on the modeled reserve is material, the company must establish margins accordingly.

VM-31 Section 3.F.3requires disclosure of the rationale for the particular margins used, including how the results of sensitivity testing were used in connection with setting the margins. Also, as noted earlier in this question, VM-31 Section 3.F.16.b requires disclosure of the specific sensitivity tests performed for each risk factor and an explanation of how the results of sensitivity tests were used or considered in developing assumptions. If a model segment contains multiple distinct product types, this should be done for each product type.

## Q 13.13: How are margins determined for dynamic assumptions?

A: Risk factors that are modeled dynamically should encompass the plausible range of behavior consistent with the economic scenarios and other variables in the model, including the nonscenario tested assumptions. The company must use sensitivity testing to ensure that the dynamic assumption is set at the conservative end of the plausible range of results and to understand the materiality of making alternate assumptions.

Where an assumption is dependent on interest rates or equity returns and a dynamic formula is included in the modeling, some actuaries would not add an additional margin to the calculation, on the basis that conservatism is inherent in the tail measure (i.e., CTE).

However, other actuaries add conservatism, based on the assessment that the use of the tail measure will only inject conservatism regarding the interest rate or equity risk, but not necessarily the dynamically related risk, which they might see as a distinct risk. Some of these actuaries would add conservatism by making the dynamic formula slightly more or less dynamic (depending on what would be more conservative) than anticipated.

Some actuaries consider margins on the base underlying assumption to be applicable to the resulting assumption including dynamic components, so would not add an additional margin.

## Q 13.14: How often are margins updated?

A: VM-22 Section 3.I.1 states that with respect to the SR and DR, the company must establish the prudent estimate assumption for each risk factor in compliance with the requirements in Section 12 of Model #820 and must annually review and update the assumptions as appropriate in accordance with these requirements.

Some actuaries would use consistent margins or the same margins from one reporting date to the next unless there is a particular reason the actuary believes the credibility, quality, or reliability of the assumption has changed. Most actuaries review and update their margins as needed as part of their review of the assumptions used in the principle-based valuation.

For those margins that relied on sensitivity tests, VM-22 Section 12.B.6 states that the company must update the sensitivity tests periodically as appropriate, considering the materiality of the results of the tests. The company may update the tests less frequently (but no less than every 3 years) when the tests show less sensitivity of the modeled reserve to changes in the assumptions being tested or the experience is not changing rapidly.

## Q 13.15: How should margins for index credits be determined?

A: For future hedging strategies with hedge payoffs that offset index credits associated with index crediting strategies, the index credit margin for these hedge instruments must be reflected in both the "best efforts" and "adjusted" runs by reducing the index credit hedge payoffs by a margin multiple that must be justified by sufficient and credible company experience and account for model error. This could be accomplished by examining historical hedge payoffs versus actual index credits. It must also be no less than 1.5% multiplicatively of the portion of the index credit that is hedged. In the absence of credible company experience, a margin of 20% must be assumed. Note that there is no cap on the index credit hedge margin if company experience indicates actual error is greater than these minimums.

## 14. Setting Mortality Assumptions

## Q 14.1: What are the steps to determining prudent estimate mortality assumptions for the Deterministic Reserve and/or Stochastic Reserve?

A: The steps to determine prudent estimate mortality assumptions for the DR and SR are as follows:

- Determine mortality business segments as described in Section 11.A.3.
- Develop expected mortality curves for each mortality business segment based on either available experience or published tables. This is described in Section 11.B.
- Apply an adjustment for credibility by blending the expected mortality curves including margins for uncertainty with the mortality assumptions described in Section 11.A.4 in order to arrive at prudent estimate mortality. This is described in Section 11.C.
- Apply future mortality improvement where required or permitted. This is described in Section 11.D.

When little or no data exists, Section 11.B.3 requires use of expected curves no less conservative than the mortality assumptions in Section 6.C.8.

## Q 14.2: How is "business segment" defined for the purposes of Section 11: Guidance and Requirements for Setting Prudent Mortality Assumptions?

A: Per Section 11.A.3, products should be grouped into business segments where mortality is expected to be materially different based on geographic, health, or any other relevant risk factors expected to impact mortality for the segments. The grouping should generally follow the pricing, marketing, risk management, and any reinsurance programs of the company. At a minimum, the business segments should differentiate between payout annuities or deferred annuity contracts with GLBs, and deferred annuities with no guaranteed benefits or only GMDBs. For example, some actuaries may differentiate PRT contracts from a union plan and a private single employer plan.

## Q 14.3: What is the distinction between a mortality segment and longevity segment for the purposes of determining prudent estimate mortality assumptions?

A: For purposes of Section 11, a business segment is referred to as a mortality segment if applying a margin where mortality rates are increased results in a higher reserve. A business segment is referred to as a longevity segment if applying a margin where mortality rates are decreased results in a higher reserve.

Sensitivity testing may be needed to determine the appropriate direction of the provision for uncertainty to mortality. The test could be a prior year mortality sensitivity analysis of the business segment or an examination of current representative cells of the segment.

Note that it may be necessary, because of a change in the mortality risk profile of the segment, to reclassify a business segment from a mortality (longevity) segment to a longevity (mortality) segment to the extent compliance with Section 11 requires such a reclassification.

## Q 14.4: Is the company required to determine its own company experience mortality rates, or can it just use an industry mortality table?

A: The company must use its own experience data, directly applicable to the business segment, in determining the expected mortality curves. If experience data is not available, the company should then look to use data from a segment that is similar to the business segment.

When little or no experience or information is available on a business segment, the company must use expected mortality curves that are no less conservative than the mortality assumptions used in the SPA, described in Section 6.C.8. If mortality experience on the business segment is expected to be atypical (e.g., demographics of target markets are known to have higher or lower mortality than typical), this "no data" mortality requirement may not be adequate.

## Q 14.5: What considerations should be made involving mortality data and analysis?

A: The following must be taken into consideration around the mortality data and assumption setting:

- Adjustments must be considered to reflect differences between the business segments, and subsequent margins shall be considered to the adjusted expected mortality curves to reflect the data uncertainty associated with using data from a similar but not identical business segment.
- Adjustments must be considered if there is evidence of death underreporting.
- Adjustments must be considered for evidence of mortality selection.
- Adjustments and smoothing must be considered depending on the quantity and quality of data. Expected mortality curves applied to recent historic exposures, should not result in an estimate of aggregate deaths that deviates materially from the actual number of deaths during the exposure period.
- Adjustments should be considered from observed trends in mortality experience, trends in exposure, volatility in year-to-year A/E mortality ratios, mortality by lives relative to mortality by amounts, and changes in the mix of business.

## Q 14.6: Would the actuary need to use a specific credibility method to determine the credibility of the mortality experience used to develop the mortality assumptions?

A: No, the actuary need not use a specific credibility method, but the credibility procedure must meet the following conditions according to Section 11.C.3:

- Produce results that are reasonable.
- Not tend to bias the results in any material way.
- Be practical to implement.
- Give consideration to the need to balance responsiveness and stability.
- Take into account not only the level of aggregate claims but the shape of the mortality curve.
- Contain criteria for full credibility and partial credibility that have a sound statistical basis and be appropriately applied.

The actuary must also consider ASOP No. 25, Credibility Procedures, which is available on the Actuarial Standards Board's website.

## Q 14.7: How is mortality improvement reflected?

A: Per Section 11.C.2, the industry mortality table for a mortality segment may be adjusted and the industry mortality table for a longevity segment must be adjusted for mortality improvement to the experience weighted average date for purposes of adjusting credibility.

According to Section 11.C.4, up to the valuation date, it is required that the credibility adjusted table used for longevity segments be adjusted for mortality improvement using the applicable mortality improvement scale from the experience weighted average date to the valuation date. This is also permitted, but not required, for mortality segments. Some actuaries may use Projection Scale G2, which is consistent to what is described in Section 6.C.8.

Beyond the valuation date, per Section 11.D the prudent estimate mortality assumption must be adjusted for mortality improvements if such an adjustment would serve to increase the resulting DR or SR. If such an adjustment would reduce the DR or SR, reflecting mortality improvement is permitted, but not required. The mortality improvement assumption must be based on current relevant data with a margin for uncertainty (increasing assumed rates of improvement if that results in a higher reserve or reducing them otherwise).

## 15. Setting Contract Holder Behavior Assumptions for the DR/SR

## Q 15.1: What contract holder behaviors might be considered in the calculation of reserves?

A: The company should consider all relevant forms of contract holder behavior and persistency, including, but not limited to the following:

- Surrenders
- Partial Withdrawals
- Account Transfers
- Future Deposits
- Income start date for benefit utilization
- Option election
- Commutation of benefit
- Annuitization
- Selection of elective (Living Benefits) and non-elective options (Death Benefits)
- Type of Pension Risk Transfer contract (Accumulating phase vs Payout phase), form of payment and accumulation phase income options available at retirement
- Optional rider utilization (Long Term Care, etc.)
- Resets/ratchets (choice of policyholder to reset a floor)

## Q 15.2: When are dynamic policyholder behavior assumptions used?

A: Section 10.E states that a company should exercise care in using static assumptions when it would be more appropriate to use a dynamic model or other scenario-dependent formulation for behavior. Dynamic models are encouraged but not mandatory and appropriate simplifications, approximations and modeling efficiency techniques are allowed.

No guidance is given as to how to determine when an assumption can be represented "appropriately" by static assumptions. Most actuaries document the rationale for using static assumptions if static assumptions are used in place of dynamic policyholder behavior.

Some actuaries use dynamic policyholder behavior assumptions in instances where an external environment or actions of the company, which can be reflected in the model, affect policyholder behavior.

Some examples the actuary may wish to consider include, but are not limited to, the following:

- Under decreasing or low-interest scenarios, the guarantees may become attractive, possibly leading to lower lapses or additional premium payments or exercise of guaranteed settlement options.
- For interest-sensitive products, when interest rates change (in particular, under increasinginterest scenarios), the assumption of how credited rates are set (i.e., how fast they increase) might be assumed to affect the lapse assumption, which may affect other assumptions such as mortality and premiums.
- For Fixed Indexed Annuities, in highly volatile equity markets, hedging costs increase resulting in the need for dynamic assumptions to model lower cap rates and participation rates, typically on an annual basis.

- For Pension Risk Transfer models, dynamic assumptions apply to the elective retirement assumptions in the deferred stage.
- Dynamic lapse assumptions may depend on in-the-moneyness of the underlying guarantees, attained age, remaining surrender charge period, guaranteed period, related features (e.g. market value adjustment), and competitor market rates.
- Partial withdrawal assumptions may depend on guaranteed elective withdrawals (e.g. lifetime and non-lifetime), attained age, issue age, duration, and qualified tax status.
- Dynamic reinvestment assumptions may focus on duration matching, cash flow matching, credit default probability, market values, and selling based on liquidity, maturity, or pro rata sales.
- Dynamic reinsurance assumptions may vary by recapture assumptions or experience adjustments for quota share or coinsurance agreements.

## Q 15.3: Are there specific considerations in setting margins on assumptions for contract holder behavior?

A: Section 10.D.6 states that where relevant and fully credible empirical data do not exist for a given contract holder behavior assumption, the company shall set the contract holder behavior assumption to reflect the increased uncertainty such that the contract holder behavior assumption is shifted towards the conservative end of the plausible range of expected experience that serves to increase the DR and/or SR.

Section 10.D.4 states that margins should reflect an increase in contract holder efficiency over time, unless the company has relevant and credible experience or clear evidence to the contrary.

Section 10.D.5 states that the margin must reflect the data uncertainty when using assumptions from similar but not identical blocks of business.

## Q 15.4: How might policyholder behavior assumptions differ between the various exclusion tests and projections required under VM-22?

A: Some actuaries would conclude that the Deterministic Reserve and Stochastic Reserve calculations as well as the Stochastic Exclusion Ratio Test use the same assumptions, except that the prudent estimate assumptions will vary dynamically for the 16 scenarios to reflect scenariodependent risks.

If the qualified actuary chooses to pass the Stochastic Exclusion Test by certifying that a group of policies are not subject to material interest rate or asset return volatility risk, then different assumptions may be used, for example results of the New York seven scenarios from cash flow testing, as opposed to the 16 interest rate scenarios from Appendix 1 in VM-20.

Per Section 7.D, for the Stochastic Exclusion Demonstration Test, reserves may be calculated in accordance with VM-A, VM-C, VM-M, and VM-V. Those assumptions would vary from those used in the SR and DR projections.

Per Section 7.A, for the SET Certification Method, if the company uses the cash flow testing model then it should be used with explicit margins and/or sensitivities such that moderately adverse conditions are reflected for risks other than the economic scenarios.

## Q 15.5: What are some of the general considerations that actuaries may take into account in setting premium assumption for flexible premium products under VM-22?

A: Per Section 10.C, for any assumption that is not prescribed or stochastically modeled, the company shall use sensitivity testing to ensure that the assumption is set at the conservative end of the plausible range. For the premium assumption, an actuary may consider sensitivity testing different premium payment patterns including continued scheduled deposits, continued increasing deposits with assumed inflation and wage growth, all capped at the maximum level of deposits allowed in the underlying deferred annuity contract. The actuary shall analyze the results of the sensitivity tests to ensure that the assumption is set at the conservative end of the plausible range and understand the materiality of the assumption on the modeled reserve. Sections 12.B.5 and 12.B.6 provide further guidance on identification of risk factors and materiality.

## Q 15.6: What are some of the additional considerations that actuaries may take into account in setting assumptions applicable to Guaranteed Living Benefits under VM-22?

A: Per Section 10.G, experience for contracts without guaranteed living benefits may be of limited use in setting a lapse assumption for contracts with in-the-money or at-the-money guaranteed living benefits. Such experience may only be used if it is appropriate (e.g., lapse experience on contracts without a living benefit may have relevance to the early durations of contracts with living benefits) and relevant to the business. Section 12.B.5 provides more guidance and techniques for risk factors (such as utilization of guaranteed living benefits) that do not lend themselves to the use of statistical credibility theory. The company shall establish anticipated experience assumptions in a manner that is consistent with accepted actuarial practice and that reflects any available relevant company experience, any available relevant industry experience, or any other experience data that are available and relevant.

## 16. Setting Expense Assumptions

## Q 16.1: What types of expenses are included in the models for determining reserves?

A: Section 12.D provides that all types of expenses-including but not limited to applicable overhead expenses that have been allocated to the modeled contracts, commissions, fund expenses, contractual fees and charges, and taxes (excluding federal income taxes and expenses paid to provide fraternal benefits in lieu of federal income taxes)-be reflected in the modeling. Some actuaries consider ASOP No. 2, Nonguaranteed Charges or Benefits for Life Insurance Policies and Annuity Contracts, and ASOP No. 7, Analysis of Life, Health, or Property/Casualty Insurer Cash Flows, when determining the expenses included in the projections where it is not specifically addressed in VM-22. Investment expenses are to be included in the net investment earnings.

## Q 16.2: Must acquisition and significant non-recurring expenses be included?

A: Per Section 12.D.1.l, acquisition costs associated with the business in force as of the valuation date and significant nonrecurring expenses that are expected to be incurred after the valuation date shall be included in the reserve calculation.

## Q 16.3: How are overhead expenses reflected and allocated in the calculation?

A: Per Section 12.D.1.k, an appropriate portion of indirect costs and overhead expenses should be included along with other expenses consistent with the block of policies being modeled. Some actuaries would use the company's practices of expense allocation among lines of business if it includes overhead expenses and is reasonable for the specific cohorts of business in scope for VM-22. Some actuaries develop an allocation specifically for reserve modeling that might be based on pricing methodology.

## Q 16.4: How is inflation reflected?

A: Section 12.D.1.d requires that expense assumptions reflect the impact of inflation. Some actuaries would thus make an assumption for inflation that is related to the scenarios being modeled. One way to do this is to base the rate of inflation on the interest rate scenario being projected, such as assuming a base real rate of return with some portion of the additional amount assumed to be inflation. Some actuaries model inflation separately.

Note that inflation expenses are prescribed for the disclosure of the Standard Projection Amount with differences when the company is and isn't responsible for the contract administration.

## Q 16.5: What future improvements in expenses may be included?

A: Under Section 12.D.1.e, prudent estimate expense assumptions may not assume future expense improvements. However, according to Section 12.D.1.j, expense efficiencies that are derived and realized from the combination of blocks of business only can be assumed when the costs of achieving these efficiencies are also recognized.

## Q 16.6: How are federal income taxes reflected in the calculation?

A: Per Section 12.D.1.f, the following shall not be included in the calculation:

- federal income taxes;
- expenses paid to provide fraternal benefits in lieu of income taxes; and
- foreign income taxes.

Per Section 12.D.1.k, expenses categorized as "taxes, licenses and fees" shall be reflected in the expense assumption.

## Q 16.7: How would expense assumptions be set for new products or new lines of business where there is no experience within the company?

A: Section 12.D.1.m provides that the company should review expense factors used to determine anticipated experience for an existing block of mature policies and adjust those factors for any differences in long-term expense factors that would be expected between the new product and existing mature block of business, taking steps to ensure that all expenses are fully allocated as outlined in Sections 12.D.1.h, 12.D.1,i and 12.D.1.k.

Some actuaries would look to pricing assumptions; expense experience for other similar products within the company; or to studies done by industry groups, reinsurers, or consultants for similar products to adjust the anticipated experience assumption. Some actuaries would increase the margin on this assumption compared to other expense assumptions to reflect the greater uncertainty in the anticipated experience assumption.

## Q 16.8: How would the actuary set margins for an expense assumption?

A: A process that some actuaries might use would be to review the historical experience data (for example, unit costs for the last five years) for the line of business or relevant block. Assuming the actuary is comfortable that the level of expenses will not significantly increase or decrease in the future, the actuary would then determine what type of modification to this assumption would increase the reserve (likely an increase to expenses). Then, taking into account the criteria above for determining margins, including the uncertainty, credibility, quality of experience data, and the level of the anticipated experience assumption relative to the historical values, the actuary would develop a range of potential outcomes for future expenses. This range could vary by duration with a tighter range expected in the next few projection years and a wider range further out in the projection. The margin would be set so that in the actuary's judgment, the range of the prudent estimate assumption includes the potential deviations from the anticipated experience in tail scenarios. See Section 12.C for general guidance on assumption margins and Section 10 on Aggregate vs Individual margins.

## Q 16.9: How are capital expenditures, such as technology investment costs, considered in the expense assumptions?

A: Section 12.D.1.a and the subsequent Guidance Note provide that certain capital expenditures may be spread over a reasonable number of years in accordance with statutory accounting principles as defined in the Statements of Statutory Accounting Principles but that care should be taken with regard to the potential interaction with other assumptions.

## Q 16.10: Can expenses for items like death claim processing, election of future annuitization options, and projection of GMWB upon depletion of account value be included with maintenance expenses?

A: Section 12.D.1.c states that an actuary shall choose an appropriate expense basis that properly aligns an expense with the assumption. For example, the Guidance Note states that the expense assumption for handling death benefit payments should be allocated per death incurred. For contracts projected to elect future annuitization options or projections of GMWB benefits once the account value has been depleted, projections assume the contract remains in force, projected payments are paid and associated maintenance expense are incurred.

## Q 16.11: Should the company use the same expense assumptions for the deterministic and stochastic scenarios?

A: The expense assumptions are the same for the deterministic and stochastic reserves, except with the applicable inflation expense that may vary by economic scenario.

## 17. Setting Non-Guaranteed Element Assumptions

## Q 17.1: What are non-guaranteed Elements ("NGEs") and how should they be included in the models under VM-22?

A: Non-guaranteed elements ("NGEs"), as defined in VM-01, refer to charges or credits to a policyholder's account value, benefit, premium, or consideration that are both established and which may be adjusted at the discretion of an insurance company. Non-variable annuity NGEs include, for example, the credited rates on fixed accounts, index parameters (caps, spreads, participation rates, etc.), rider fees, rider benefit features being subject to change (rollup rates, rollup period, etc.), account value charges, and dividends under participating policies or contracts. Section 10.I provides guidance on how NGEs should be modeled. In addition, Section 5.A.2.d outlines items that companies should include in setting assumptions for the NGE in reinsurance cash flows.

## Q 17.2: Can the actuary modify (up or down) the assumed NGEs scale or spread in response to the experience unfolding in the scenario?

A: Section 10.I.3 and 10.I.4 indicate that projected levels of NGEs in the cash flow model must be consistent with how actual NGEs are determined (10.I.3) and consistent with the experience assumptions used in each scenario (10.I.4). Policyholder behavior assumptions in the model must be consistent with the NGE methodology reflected in the model.

## Q 17.3: What are some of the factors that are considered when deciding to include NGE in reserves covered by VM-22?

A: According to Section 10.I.2, the projected NGE shall reflect factors that include, but are not limited to, the following:

- The nature of the contractual guarantees;
- The company's past NGE practices and policies;
- The timing of any change in NGE relative to the date of recognition of a change in experience; and
- The benefits and risks to the company of continuing to authorize the NGE.

## Q 17.4: When determining the NGE assumptions for each scenario, what considerations might the actuary take into account when modifying the current NGEs?

A: Examples of considerations about NGEs include:

- Existence of contract guarantees;
- The company's ability to modify its non-guaranteed elements on items such as credited rates on fixed accounts, index-related parameters (i.e. index cap and participation rates), rider fees, expense charges, etc.;
- Effect on policyholder behavior of maintaining the current non-guaranteed elements under the scenario;
- Effect of the NGE assumptions on the competitive position of the product under the scenario;
- The extent to which a change in experience is recognized in the non-guaranteed element;
- The timing lag from when a change in experience occurs to when it is recognized in the non-guaranteed elements; and
- Management philosophy.

## Q 17.5: What adjustments to the model can be made to take into account lags in the changing of NGEs?

A: Some actuaries may find it difficult to model lags in changing NGEs in these calculations. One technique that some actuaries use is to assume that NGEs are determined based on prior projection year values, or the prior projection period if quarterly or monthly time steps are used in the model. Some actuaries would consider whether the modeled timing of changes to NGEs materially distorts the minimum reserve.

For example, the setting of crediting rates may rely on a prior period's earned rate as a reference point.

## Q 17.6: Is it appropriate to limit the review of NGE impacts to only the tail scenarios used in the Stochastic Reserve Calculation? How should NGEs be reviewed for the Deterministic Reserve?

A: Some actuaries would pay particular attention to how the model assumes NGEs are modified as the market conditions change across all scenarios. This would include scenarios outside of the tail scenarios where NGEs play a significant part in risk mitigation because an error or misstatement in one of those scenarios could lead to that scenario (that was not previously in the tail) now becoming part of the tail. This is particularly true for blocks where changes to NGEs are likely to have a significant impact on calculation of reserves.

Under Section 7.E, the cash flows used for the Deterministic Reserve should be predictable and stable, have limited contract holder behavior, and economic conditions do not materially influence anticipated contract holder behavior for the group of contracts and certificates. If NGE changed materially in scenario(s) used for Stochastic Reserve, the actuary should consider whether the Deterministic Reserve is applicable.

## Q 17.7: Will actuaries assume the prudent estimate assumptions or anticipated experience assumptions actually occur when projecting the NGEs as part of VM-22?

A: Section 10.I.4 states that projected levels of NGEs in the cash flow model must be consistent with the experience assumptions used in each scenario. Some actuaries interpret this to imply the NGEs be established based on the prudent estimate assumption set.

Like all other assumptions, VM-22 requires that the NGEs include a margin as stated in Section 10.I.8. Hence, some actuaries may not assume that the company will fully reflect the projected experience in the modeled NGEs, because doing so would eliminate the margin built into the prudent estimate assumption. As an example, if rider charge increases are assumed to fully offset the impact of decreases in projected mortality, some actuaries may assume that rider charges are only increasing to partially offset the mortality margin. Others may assume a lag in the reflection of projected experience on modeled rider charges.

As an example, if future GLWB charges on renewal roll-up periods are increased to exactly offset the projected higher claims due to the margin in the mortality assumption, the mortality margin providing additional persistency is essentially eliminated. Some actuaries may assume a lower increase in GLWB charge as the NGE margin. Other actuaries may choose to reflect a higher percentage of policies electing to renew the roll-up period as the NGE margin.

## Q 17.8: Are there situations where an NGE may be excluded in the determination of the Deterministic or Stochastic Reserves?

A: According to Section 10.I.5, the actuary may exclude any portion of the NGE that is not based on some aspect of the contract's experience

However, if the board has guaranteed a portion of the NGE into the future, the company must model that amount (as stated by Section 10.I.6).

If the board identified a non-guaranteed distribution to policyholders, such as a special dividend from the sale of unrelated block of business, some actuaries interpret Section 10.7 as allowing its exclusion from the model.

.

## 18. Treatment of Reinsurance

## Q 18.1: When would the actuary include a reinsurance agreement in the calculation?

A: Section 5.A.2 states that a company shall include a reinsurance agreement in calculating the minimum reserve if under the terms of the Accounting Practices and Procedures Manual the agreement or amendment qualifies for credit for reinsurance.

Section 5.A.2.a.iv states that if a reinsurance agreement or amendment does not qualify for credit for reinsurance but treating the reinsurance agreement or amendment as if it did so qualify would result in a reduction to the company's surplus, then the company shall increase the minimum reserve by the absolute value of such reductions in surplus.

Some actuaries may include a reinsurance agreement that has an effective date after the valuation date in future valuation cash flows if the treaty was executed by both parties on or prior to the valuation date and it qualifies for reinsurance credit under the terms of the Accounting Practices and Procedures Manual.

## Q 18.2: What are ways a company should reflect reinsurance in the Stochastic Exclusion Ratio Test (SERT)?

A: The Stochastic Exclusion Ratio Test (SERT) in VM-22 Section 7.C is defined as: SERT = (b-a)/c Where:

a = the adjusted scenario reserve described in Section 7.C.2.a using the baseline economic scenario described in VM-20 Appendix 1.F.

b = the largest adjusted scenario reserve described in Section 7.C.2.a under any of the 16 economic scenarios described in VM-22 Appendix 1.F with -1.0% future mortality improvement, +1% future mortality improvement, and no adjustments to future mortality improvement

c = an amount calculated from the baseline economic scenario described in VM-20 Appendix 1.F with no adjustment to future mortality improvement that represents the present value of benefits for the policies, adjusted for reinsurance by subtracting ceded benefits. For clarity, premium, ceded premium, expense, reinsurance expense allowance, modified coinsurance reserve adjustments and reinsurance experience refund cash flows shall not be considered "benefits", but items such as death benefits, surrender or withdrawal benefits and policyholder dividends shall be. The benefit cash flows from the calculation of quantity "a" and the same path of discount rates shall be used.

If SERT &lt; 6.0%, SERT is "Passed."

In many, but not all cases, quota-share coinsurance scales "b," "a," and "c" roughly in proportion to 1- QS%, leaving the SERT result similar both pre- and post-quota share coinsurance. Thus, VM-22 section 7.C.2.ii.e allows for companies to elect to conduct SERT on either pre-reinsurance-ceded or post-reinsurance-ceded only if the reinsurance arrangements are pro-rata coinsurance and do not materially impact the interest rate risk, mortality and/or longevity risk, or asset return volatility risk in the contract. If a reserve calculation segment passes SERT pre- reinsurance but fails SERT postreinsurance, some actuaries may attempt to demonstrate that sensitivity of the adjusted scenario reserve to economic scenarios is comparable pre- and post-reinsurance and thus argue that the SERT result should be determined to be a "Pass" both pre- reinsurance and post- reinsurance. One form of such a demonstration that some actuaries may use is as follows (and is found in Section 7.C.3.a).

For convenience in notation, call the pre-non-proportional- reinsurance results "gross of nonproportional," with a subscript "gn," and the post-non-proportional results "net of non-proportional," with subscript "nn." If a block of business being tested is subject to one or more non-proportional reinsurance cessions as well as other forms of reinsurance, such as coinsurance, take "gross of nonproportional" to mean net of all non-proportional reinsurance but ignoring the non-proportional contract(s), and "net of non-proportional" to mean net of all reinsurance contracts. That is, treat nonproportional reinsurance as the last reinsurance in, and compute certain values below with and without that last component.

So, if we have

SERTgn ≤ 0.060 but SERTnn &gt; 0.060, then move to a second-stage test as follows:

Compute the Largest Percent Increase in Reserve = LPIR = (b - a)/a , both "gross of nonproportional" and "net of non-proportional."

```
LPIRgn = (bgn - agn)/agn
```

LPIRnn = (bnn - ann)/ann

If SERTgn × LPIRnn/LPIRgn &lt; 6.0%, then the Stochastic Exclusion Ratio Test result is considered to be passed on the post-reinsurance basis.

Note that the scenario underlying bgn could be different than the scenario underlying bnn.

Another more qualitative approach is to calculate the adjusted scenario reserve for the 48 combined economic and mortality scenarios of the Stochastic Exclusion Ratio Test both gross and net. Array the results in table and chart, demonstrating a similar pattern of sensitivity by scenario.

## Q 18.3: Do the assumptions used by both the assuming and ceding company have to be the same for a specific block of business subject to a reinsurance agreement?

A: Section 5.A.1 discusses how the ceding company should use the assumptions consistent with those used in the DR and/or SR when calculating the pre and post reinsurance reserve. Section 5.A.2.c states that an assuming company shall use assumptions to project cash flows to and from ceding companies that reflect the assuming company's experience for the business segment to which the reinsured policies belong and reflect the terms of the reinsurance agreement. Thus, the assumptions used by the ceding and assuming companies are not required to be the same.

## Q 18.4: How might non-proportional reinsurance be reflected in the cash flow projections used to determine the Deterministic and Stochastic Reserves?

A: Some actuaries may not include non-proportional reinsurance ceded benefits in the cash flows if such benefits are immaterial.

Some actuaries may include non-proportional reinsurance cash flows in the projections directly where possible.

Other actuaries may perform separate stochastic analysis as discussed in Section 5.A.2.e to quantify the impact where a single deterministic valuation assumption for a risk factor will not adequately capture the risk (e.g., mortality on a stop-loss reinsurance agreement). Some actuaries may consider stochastic analysis to be essential for assumed non-proportional reinsurance.

## Q 18.5: What does VM-22 Section 5.A.2.d mean by treating counterparties to a reinsurance treaty as "knowledgeable counterparties"?

A: Section 5.A.2.d requires the company to assume that each party to the reinsurance agreement will act in its own economic interest when exercising contractual rights and options. Section 5.A.2.d addresses knowledgeable counterparties in the following way:

Assume that the counterparties to a reinsurance agreement are knowledgeable about the contingencies involved in the agreement and thus likely to exercise the terms of the agreement to their respective advantage, taking into account the context of the agreement in the entire economic relationship between the parties. In setting assumptions for the non-guaranteed elements in reinsurance cash flows, the company shall include, but not be limited to the following:

- The usual and customary practices associated with such agreements.
- Past practices by the parties concerning the changing of terms, in an economic environment similar to that projected.
- Any limits placed upon either party's ability to exercise contractual options in the reinsurance agreement.
- The ability of the direct-writing company to modify the terms of its policies in response to changes in reinsurance terms.
- Actions that might be taken by a party if the counterparty is in financial difficulty.

## Q 18.6: How are assets that support the reserve modeled when held by another party?

A: Section 5.A.2.b provides considerations for how these assets should be modeled from the perspective of the ceding company, which may vary depending on the nature of the reinsured business, the form of reinsurance, the amount and type of assets held by the counterparty, and other treaty-specific factors. Some actuaries would apply these same considerations for an assuming company under a reinsurance arrangement where applicable.

To the extent that the management of non-guaranteed elements, dividends, or other policy factors for the reinsured business depend on the performance of the underlying assets supporting the business, some actuaries may ensure consistency between the assets selected for modeling, the modeled performance of the selected assets under each economic scenario, and the projected values of the associated policy elements under each economic scenario.

## Q 18.7: How does the actuary reflect the creditworthiness of a reinsurance counterparty?

A: Section 5.A.2.a.iii requires a margin for the risk of default to be included when the one party has knowledge that the other party is financially impaired. However, if there is no known financial impairment, then there is no requirement to establish a margin for the risk of default.

Industry practice regarding the definition of financial impairment is expected to develop over time. Some actuaries may consider financial impairment to include situations where a counterparty is known (e.g., through public credit ratings, regulatory actions, or similar information) to have a deteriorating credit profile, even if all contractual payments on the reinsured business have been received historically.

## Q 18.8: How is creditworthiness of the ceding company modeled if on assumed business the assuming company may terminate the reinsurance upon nonpayment by the ceding company?

A: VM-22 is silent on this topic. However, Section 8.C.16 of VM-20 states that the margin for default risk otherwise established for the risk of default may be reduced or eliminated in this circumstance. Some actuaries may follow the VM-20 guidance on this topic for VM-22 business where applicable.

## Q 18.9: Is there a difference in the modeling or reporting of authorized versus unauthorized reinsurers?

A: Notwithstanding the requirements in Section 5.A.2.a for an agreement to be treated as reinsurance for statutory accounting purposes in order to be reflected in the SR/DR calculation, VM-22 is silent on this topic. However, Section 8.C.17 of VM-20 requires the actuary to take into account the ratings, risk-based capital ratio, or other available information related to the probability of the risk of default of any counterparty. Only if there were some differences in the probability of the risk of default would there be a difference in the modeling. Some actuaries may follow the VM-20 guidance on this topic.

## Q 18.10: How is the pre-reinsurance-ceded reserve determined?

A: Section 3.B requires that the minimum reserve be recalculated, ignoring the impact of any reinsurance ceded.

Section 5.A.2.b indicates that the Deterministic and Stochastic pre-reinsurance-ceded reserves are determined by ignoring the effects of reinsurance ceded within the projection (e.g., by removing all reinsurance cash flows). This same section also provides guidance on how the supporting assets for the pre-reinsurance reserve should be selected.

## Q 18.11: Does VM-22 Section 5 apply for business that is excluded from VM-22?

A: In Section 5.A.1, VM-22 states that for business that is excluded from VM-22 and is valued using requirements in VM-A, VM-C, VM-M, and VM-V, the post-reinsurance ceded reserve is determined by subtracting the reinsurance reserve credit. Sections 5.A.2 and 5.A.3 discuss adjustments for determining the DR and/or SR on both a post-reinsurance ceded and a pre-reinsurance ceded basis.

## 19. Treatment of Hedging/Derivative Programs

## Q 19.1: Do the terms "derivative instrument," "derivative program," and "hedging program" all mean the same thing as used in VM-22?

A: These terms do not have similar meanings. The terms "derivative instrument" and "derivative program" are defined in VM-01.

The term "derivative instrument" includes, but is not limited to, an option, warrant, cap, floor, collar, swap, forward, or future, or any other agreement or instrument substantially similar thereto or any series or combination thereof. Each derivative instrument shall be viewed as part of a specific derivative program.

The term "derivative program" means a program to buy or sell one or more derivative instruments, or open or close hedging positions to achieve a specific objective. This definition also includes both future hedging programs (derivative programs used to reduce risk) and non-hedging programs (derivative programs used for replication or income generation objectives).

## Q 19.2: Are there limitations on including the impact of derivative programs in the additional standard projection amount (ASPA) and Deterministic Reserve (DR) calculation?

A: For ASPA, Section 6.B.6 of VM-22, states that "cash flows associated with hedging shall be projected in the same manner as that used in the calculation of the CTE70 (adjusted) as discussed in Section 9.C or Section 4.A.4.b."

For DR, the requirements with regards to the use of future hedging strategies as stated in Section 7.E limits the scope of derivative programs that can be reflected in the DR calculation.

More broadly and not specific to ASPA or DR, for derivative programs that are not associated with hedging of index credits, Section 9.B.4 states that the reduction to the DR and/or SR attributable to the hedging strategy may need to be limited due to the uncertainty associated with the company's ability to implement the hedging strategy in a timely and effective manner. The level of operational uncertainty varies indirectly with the amount of time that the new or revised strategy has been in effect. In addition, Section 9.D further clarifies additional requirements for CTE 70 (best efforts) where one or more future hedging strategies are supporting the contracts.

## Q 19.3: What is a Future Hedging strategy?

A: VM-01 defines a future hedging strategy to be derivative program undertaken by a company to manage risks through one or more future hedging transactions, including the future purchase or sale of hedging instruments and the opening and closing of hedging positions. VM-01 also states that a future hedging strategy involving the offsetting of the risks associated with products under the scope of the Valuation Manual (e.g. VM-20, VM-21 or VM-22) is not considered a future hedging strategy.

In addition, a clearly defined hedging strategy ("CDHS") is a future hedging strategy with the following clearly documented:

- The specific risks being hedged (e.g., cash flow, policy interest credits, delta, rho, vega, etc.).
- The hedge objectives.
- The material risks that are not hedged (e.g., variation from expected mortality, withdrawal, and other utilization or decrement rates assumed in the hedging strategy, etc.).
- The financial instruments used to hedge the risks.
- The hedge strategy's trading rules including the permitted tolerances from hedging objectives.
- The metrics for measuring hedging effectiveness.
- The criteria used to measure effectiveness.
- The frequency of measuring hedging effectiveness.
- The conditions under which hedging will not take place and for how long the lack of hedging can persist.
- The person or persons, including whether internal or external, responsible for implementing the hedging strategy.

- Areas where basis, gap, or assumption risk related to the hedging strategy have been identified.
- The circumstances under which hedging strategy will not be effective in hedging risks.

## Q 19.4: Are costs and benefits of a hedging program that does not qualify as a CDHS included in the cash flow model in some way?

A: Section 4.A.4.a provides clarification if a company does not have a future hedging strategy supporting contracts. It states that cash flows from any future hedge purchases or any rebalancing of existing assets shall not be considered in the modeling. However, existing hedging instruments that are currently held in support of the contracts in scope of VM-22 shall be included in the starting assets and therefore the model projections.

For future hedging strategies that are not a CDHS, Section 9.C.8 provides clarification for not reflecting the costs and benefits of these hedging programs within the SR calculations.

## Q 19.5: What are index crediting hedges and how are these reflected in VM-22?

A: Index crediting hedges is a future hedging strategy where the hedge payoffs solely offset the index credits. Section 4.A.4.b.i of VM-22 indicates that a company that has one or more such future hedging strategies supporting the contracts should include the cash flows from future hedge purchases or any rebalancing of existing hedge assets that are intended solely to offset index credits to contract holders.

In addition, existing hedging instruments that are currently held by the company for offsetting the index credits shall be included in the starting assets. Lastly, an index credit margin shall be reflected by reducing the hedge payoffs in both the CTE70 (best efforts) and CTE70 (adjusted) with a minimum of 1.5% or a higher margin, where credibility is insufficient.

## Q 19.6: What is the error factor to be reflected with future hedging strategies other than index crediting hedges?

A: Section 9.C.4 states that the error factor ("E") is a percentage ranging from 5% to 100% to reflect the potential error resulting from the level of sophistication of the stochastic cash flow model and its ability to properly reflect the parameters of the hedging strategy (i.e., the Greeks being covered by the strategy), as well as the associated costs, risks and benefits. E is used as an adjustment to the stochastic reserve as stated in Section 9.C.3.

Section 9.C.5 states that a formal back-test shall be conducted based on a minimum of 12 months of relevant data. Section 9.C.6 provides further required analyses dependent on whether the hedge cash flows are modelled explicitly, implicitly, or neither.

In situations where less than 12 months of data is available, Section 9.C.7 provides several hypothetical scenarios that may apply. In general, a higher E factor, or even set at a maximum of 100%, may be warranted depending on the facts and circumstances.

## Q 19.7: How will actuaries determine a hedging program's expected future cash flows?

A: Per Section 9.B in VM-22, the impact of the hedging strategy on cash flows is typically performed using either an explicit or implicit methodology.

An explicit methodology is characterized by including hedging positions and their resulting cash flows in the stochastic cash flow model used to determine the scenario reserve, for each scenario.

An implicit methodology is characterized by the observation that the effectiveness of the current hedging strategy on future cash flows is evaluated, in part or in whole, outside of the stochastic cash flow model.

Regardless of the methodology used by the company, the ultimate effect of the current hedging strategy (including currently held hedge positions) needs to recognize all risks, associated costs, imperfections in the hedges, and hedging mismatch tolerances associated with the hedging strategy. The risks include, but are not limited to, basis, gap, price, parameter estimation and variation in assumptions (mortality, persistency, withdrawal, annuitization, etc.). Costs include, but are not limited to transaction, margin (opportunity costs associated with margin requirements), and administration.

In addition, the reduction to the DR and/or SR attributable to the hedging strategy may need to be limited due to the uncertainty associated with the company's ability to implement the hedging strategy in a timely and effective manner. The level of operational uncertainty varies indirectly with the amount of time that the new or revised strategy has been in effect.

## Q 19.8: If a company has a future hedging strategy, is back-testing required if the expected costs and benefits of future hedge positions produce CTE 70 (best efforts) in excess of CTE 70 (adjusted)?

A: Some actuaries believe that back-testing is still necessary in this situation because it serves to validate the modeling of the hedge strategy within the VM-22 calculations, in addition to supporting the value of the error factor. Other actuaries would continue to back-test because the relationship between best efforts and adjusted might reverse at another CTE level or vary depending on initial market conditions, making the E factor applicable.

## Q 19.9: If a derivative program is going to be revised or changed in the future, is this change included in the calculation?

A: If changes are going to be made to a derivative program, some actuaries include the changes in the model, while other actuaries wait until the changes are implemented to the derivative program, particularly if the changes to the program are not final or approved.

If future changes or revisions are going to be included in the model, it would be prudent for the actuary to document the basis for including changes to derivative programs included in the reserve model in accordance with VM-31 Section 3.F.8.e.

Furthermore, VM-22 Section 9.C.7 describes the considerations of the error factor and applicable mock testing for changes in the hedge program for non-index credit hedging strategy.

## Q 19.10: Do the limitations of projected hedge effectiveness in other reserve and capital calculations such as VM-21 and C3 Phase II apply to the minimum reserve calculation in VM22?

A: There are no required limits to hedge effectiveness in VM-22. VM-22 Section 9.E provides specific considerations for estimating the future effectiveness of the current hedging strategy for the purpose of reducing the SR. VM-21 provides similar guidance. VM-31 Section 3.F.8.a provides descriptions of the effectiveness of the strategy and results of historical hedging effectiveness. VM31 Section 3.F.8.d.v states that for future hedging strategies, the company may not assume that residual risks and frictional costs have a value of zero, unless the company demonstrates in the PBR Actuarial Report that "zero" is an appropriate expectation.

Some actuaries may choose effectiveness measures consistent with the hedge effectiveness factors used in their VM-21 and C3 Phase II calculations if they have variable annuity business. Other actuaries develop hedge effectiveness factors specifically for the business being modeled for VM22. Many actuaries consider whether hedge effectiveness will vary under extremely adverse or favorable scenarios.

## Q 19.11: Are there other things that the actuary takes into account when modeling a derivative program?

A: Some actuaries would aim to fully capture the practical realities associated with the program and the modeling of the program-frequency of rebalancing, transaction costs, margin costs, basis risk, gap risk, pricing risk, parameter estimation, assumption limitations, and trading limits. These actuaries would determine these other costs and limitations in the framework of the tail scenarios that end up determining the Stochastic Reserve.

With dynamic hedging strategies, in some cases the cash flow model supporting the CTE calculation may be able to adequately reflect residual risks through margins in program assumptions, adjustments to costs and benefits, etc. In other cases, reference to additional external models or analyses may be necessary where such results cannot be readily expressed in a format directly amenable to a CTE calculation. In such cases, some actuaries combine the results of such models by a method that is consistent with the objectives of VM-22 requirements.

Section 9.E provides further guidance on specific considerations and requirements when modeling a derivative program for a non-index credit hedging strategy.

## Q 19.12: Is there a certification needed if a derivative program is included in the calculation?

A: Yes, Section 3.F.19.a states that a certification from a duly authorized investment officer that the modeled asset investment strategy, including any future hedging strategies supporting the contracts, is consistent with the company's current investment strategy except where the modeled reinvestment strategy may have been substituted with the alternative investment strategy, and that documentation of the CDHS attributes for any future hedging strategies supporting the contracts are accurate.

## 20. Disclosures

## Q 20.1: How are fair values defined and calculated for VM-22, Section 9.D and VM-31, Section 3.F.8.g?

A: Companies reflecting a CDHS are required to calculate and compare the "fair value of the portfolio of contracts" to both CTE 70 (Best Efforts) and CTE 70 (Adjusted) before the cash surrender value floor. However, neither VM-22 nor VM-31 specify how full contract fair values should be calculated.

SSAP No. 100 contains the statutory definition of fair value used in the reporting of other assets and liabilities. The statutory accounting fair value definition ("the price that would be received to sell an asset or paid to transfer a liability in an orderly transaction between market participants at the measurement date") follows U.S. GAAP FAS 157 with certain notable exceptions. The primary modification is the exclusion of consideration of non-performance risk (own credit risk). Paragraph 57 of SSAP 100 states that "the consideration of own credit risk in the measurement of fair value liabilities is inconsistent with the statutory accounting concept of conservatism and the assessment of financial solvency for insurers." However, some actuaries believe that this modification may cause values to deviate from the fair value definition while others believe that some reflection of the credit risk of the purchaser of the liability, which may be similar to their own credit risk, may be appropriate.

SSAP 100 allows for practicability, considerations of the cost of estimating fair value, materiality, and the required precision of estimates.

Under U.S. GAAP, certain variable annuity guarantees have historically been considered embedded derivatives under ASC 815 (formerly FAS 133) and subject to fair value accounting. Some actuaries may refer to ASC 820 (formerly FAS 157), the U.S. GAAP fair value guidance, and extend those principles to full contract cash flows. As noted in the American Academy of Actuaries' FAS 157 and FAS 159 practice note from February 2009,

Some actuaries conclude that fair values calculated without the FAS 157 adjustments for nonperformance risk and/or market participant risk margins may be more relevant for the disclosure comparison. Others might consider leveraging (1) their hedge target scenarios and methodologies if the hedging program is based on some type of fair value metric or (2) calculations performed for SSAP No. 108 (Derivatives Hedging Variable Annuity Guarantees). Some might also consider adjustments for implied vs. realized equity volatility differences.

## Q 20.2: How is the cumulative decrement projection for VM-31 Section 3.F.14.a.ii (CTEPA method) calculated? What are some potential considerations?

A: VM-31, Section 3.F.14 requires the disclosure of cumulative decrements using Standard Projection assumptions and the company's prudent estimate assumptions. Companies using the CTEPA method will select the scenario whose value is closest to the CTE 70 (adjusted). Each cumulative decrement projection "shall include, at the end of each projection year, the projected proportion (expressed as a percentage of the total projected account value) of persisting contracts, as well as the allocation of projected decrements across death, full surrender, account value depletion, elective annuitization, and other benefit election."

VM-31 does not specify a method for deriving the cumulative decrements or the allocation of projected decrements, although it does reference an account value basis. Some actuaries might use projected end of period account values (AVs) and the AV released for each type of decrement. Given market and AV changes during each period, decrement rates may be derived for each period, and then cumulative rates may be calculated from the per period rates. Other actuaries might also consider AV growth, AVs before the decrements, and/or the timing of decrements when approximating AV levels in the decrement rates.

Other actuaries question whether such an account value-based calculation will be fully representative of policyholder behavior. For example, account value depletion (i.e., instances of living benefit claims) may be under-represented because account values before depletion are, by definition, low. To a lesser extent, the AV-weighted full surrender rates may also mask the presence or significance of low dynamic lapse rates for deep-in-the-money contracts if the projected in-force includes a mix of business at different durations or moneyness levels. A counts-based cumulative decrement disclosure or counts based view of account value depletion may provide additional insights about projected policyholder behavior, but such additional information is not required.

Given the potential limitations of any given approach, the actuary may wish to consider performing additional review of results and monitoring emerging practices.

The actuary may wish to consider documenting the cumulative decrement approach and consistently applying it to the projections using the Standard Projection assumptions and the company's prudent estimate assumptions to maintain comparability and facilitate interpretations.

## Q 20.3: The allocation of reserves for a model segment is prescribed in VM-22 Section 13. If multiple segments are aggregated, how should the reserves post aggregation benefit be allocated across model segments?

A: If multiple model segments are aggregated according to Section 3.F.5, a company shall disclose the method used to allocate the aggregation benefit to each model segment in VM-31. Some actuaries may allocate the aggregation benefit based on the estimated reserves of each model segment pre-aggregation. Others may use the actuarial present value (APV) method described in Section 13, while others may use another risk-based measure.

The final reserve post aggregation benefit for a model segment may be different from what it would have been if the model segment had been valued individually, which could impact the allocation of the aggregate reserve to the contract level. Section 13 states that if aggregation is done across multiple model segments, the allocation calculations shall be done separately for each model segment. Section 13.B.1 states that the APV shall be determined using the scenario that produces the aggregate scenario reserve for the group that is closest to, but not greater than, the SR. Some actuaries use the scenario that is closest to the reserve of the model segment without aggregation, while others use the scenario that is closest to the model segment reserve post aggregation, both of which may result in different allocation scenarios for each model segment. Others use the same scenario for all model segments that were aggregated that produced the aggregate scenario reserve that is closest to, but not greater than, the aggregate SR.

## Q 20.4: Is there a required "as of" date for the annual disclosures and other VM-22 testing (e.g., use of seriatim vs. modeled cells for Standard Projection, demonstrating that non-prescribed scenario results are not materially less than results under the prescribed scenarios)?

A: Neither VM-22 nor VM-31 specify an "as of" date for the annual disclosures or testing. Some actuaries might extend VM-31 guidance on the use of prior dates or simplifications to the disclosure calculations and use results as of a prior date (with adjustments, as appropriate) if doing so would not materially change the disclosed quantities or relationships. For example:

## VM-31, Section F.2.e:

"Approximations and Simplifications-Description of any approximations and simplifications used in cash flow projection calculations and not described in a different section of this report, including documentation that these did not materially reduce the resulting reserve."

## VM-31, Section F.16.d:

"Calculations as of a Date Preceding the Valuation Date - If the DR, SR and/or the additional standard projection amount were developed as of a date prior to the valuation date, disclosure of the prior date, the SR and the additional standard projection amount of the in force on the prior date, and an explanation of why the use of such a date will not produce a material change in the results compared to if the results were based on the valuation date. Such an explanation shall describe the process that the qualified actuary used to determine the adjustment required by VM-21 Section 3.I and VM-22 Section 3.K, the amount of the adjustment, and the rationale for why the adjustment is appropriate."

## Q 20.5: Are the VM-31 disclosures and tests annual or ongoing (i.e., quarterly) requirements?

A: Because the VM-31 PBR Actuarial Report is a yearly report, some actuaries may view the VM-31 disclosures as annual requirements. However, they may wish to consider whether more frequent analysis or disclosures are appropriate if, for example, changes are made during the year (e.g., model or assumption updates, asset strategy changes, market changes, in-force composition) that might materially affect results.

## Q 20.6: How does the Standard Projection impact of aggregation disclosure relate to cell compression testing?

A: The two requirements are separate and distinct.

- VM-22 Section 6.A.1.a and VM-31 Section F.14.j require all companies, regardless of whether they are using seriatim in-force or model cells, to quantify and disclose the impact of aggregation in the Standard Projection. This measures economic risk offsets between business with sufficiency and deficiency.
- VM-31 Section F.2.g requires companies that use a compressed liability model to state that the compression method does not intentionally understate reserves and to provide auditable information to the domiciliary commissioner (upon request) demonstrating that the model cells do not materially understate reserves. This compression validation is a test of a modeling simplification/limitation.

## Q 20.7: What are some of the methods used to determine option adjusted spreads used to determine the Maximum Net Spread Adjustment Factor for VM-31 Section 3.F.6.h?

A: The option adjusted spread ("OAS") is defined in VM-20 Section 9.F.2.b. as the average spread over zero coupon Treasury bonds that equates a bond's market price as of the valuation date with its modeled cash flows across an arbitrage free set of stochastic interest rate scenarios. The "stochastic interest rate scenarios" required for this purpose are not prescribed by the Valuation Manual. VM-20 Section 9.F.2.b. also states that the use of market conventions and other approximations is acceptable for purposes of determining the OAS. For floating rate assets, VM-20 Section 9.F.2.b. further states that the OAS should be calculated as the equivalent spread over Treasuries after swapping to fixed rates.

Based on this guidance, for publicly traded instruments, some actuaries may simply use the OAS supplied by a market data provider (e.g., Bloomberg, FactSet, LSEG, etc.) for the instrument, which would be based on their data provider's proprietary valuation model for the cash flows and embedded options included in the instrument and their proprietary interest rate scenario set. Some actuaries may choose to directly calculate their own OAS on an asset-by-asset basis using a consistent, companyspecific set of interest rate scenarios.

For instruments that are not publicly traded, some actuaries project future cash flows for the asset under a pre-defined set of proprietary interest rate scenarios and determine the OAS implied by equating the present value of those cash flows to a quotation for the asset provided by a third-party valuation service. For instruments that are not publicly traded but which are originated at a stable and persistent spread relative to a similar publicly traded instrument, some actuaries may instead use the OAS based on a similar publicly-traded asset plus a long-term assumption about the relationship between spreads between publicly-traded and non-publicly-traded assets.

## Q 20.8: What are some approaches to justifying the margin on any future hedging strategy that offsets indexed credits associated with index interest strategies for VM-31 Section 3.F.8.d.x?

A: As specified in the definition for "index credit hedge margin" in VM-01, the risks considered in this margin should include, inter alia, the risk of inefficiencies in the hedging program driven by basis risk, persistency risk, modeling risks, and uncertainties with the future costs of the hedging program.

Since these risk factors can all be impacted by the unique operational considerations specific to each company, the actuary should ensure that they have a thorough understanding of the index crediting strategy, the company's hedge target, and the company's hedging process prior to quantifying the margin appropriate for these risks.

For companies with sufficient historical data on actual hedge performance, some actuaries may start by determining the empirical distribution of the historical index credit hedging error (i.e., the quantities formed by expressing the periodic hedge gains/(losses) as a fraction of the hedged portion of the index credits for the same period) and selecting an initial margin that is at least as great as a relevant statistic (e.g., the 85 th percentile or the average of the worst 30% of historical observations) formed from the historical hedging error distribution. Similarly, some actuaries may use regression analysis or other statistical techniques to quantify the historical effectiveness of their hedging program.

Some actuaries may then adjust the initial margin for additional factors (e.g., future operational cost uncertainties) that cannot be quantified using historical data using model-derived or subjectively determined add-ons (e.g., by applying an additional X% margin to their historical error). For example, if a company's hedge target for index credits includes an allowance for persistency, the actuary may consider modeling the hedge error that would result if actual persistency were higher or lower than the persistency assumed in its hedge target and develop an additional error factor based on the resulting under-hedge or over-hedge observed under the shocked persistency scenarios.

Clearly, the future cost of the index credit hedges purchased is also a critical factor in modeling the future costs of the hedging program. While the projection of implied volatility scenarios within VM-

22 is left to the judgment of the company, guidance on modeling implied volatility is provided in VM-22 Section 8.D. If a company chooses to employ a simpler approach to modeling implied volatility within its model that does not robustly capture the range of potential future index credit hedge costs under a range of potential future economic conditions, some actuaries may add an additional error margin to reflect potential deviation in actual hedging outcomes from the modeled results.

Regardless of the methodology chosen to quantify the margin, a minimum margin of 1.5% (multiplicative) is specified in VM-22 Section 4.A.4.b.i.c. For a company without sufficient credible company experience, a minimum margin of 20% must be applied.
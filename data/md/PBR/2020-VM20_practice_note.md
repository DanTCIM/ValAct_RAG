# Life Principle-Based Reserves (PBR) Under VM-20 

## April 2020

Developed by the Life Principle-Based Approach Practice Note Work Group of the Life Valuation Committee of the American Academy of Actuaries

<img src="https://cdn.mathpix.com/cropped/2024_03_15_8ba611b8476c665b9018g-001.jpg?height=201&width=718&top_left_y=2087&top_left_x=693" alt="image" style="width:100%;height:auto;">

AMERICAN ACADEMY of ACTUARIES

Objective. Independent. Effective. ${ }^{\text {m }}$

This practice note is not a promulgation of the Actuarial Standards Board, is not an actuarial standard of practice, is not binding upon any actuary, and is not a definitive statement as to what constitutes generally accepted practice in the area under discussion. Events occurring subsequent to this publication of the practice note may make some of the practices described in this practice note irrelevant or obsolete.

## 2020 Practice Note Update Work Group

Rhonda Ahrens, MAAA, FSA

Patricia Allison, MAAA, FSA

Bryan Amburn, MAAA, FSA

Benjamin Bock, MAAA, FSA

Elizabeth Caldwell, MAAA, FSA

Serena Chao, MAAA, FSA

Nadeem Chowdhury, MAAA, FSA

Rachel Hemphill, MAAA, FCAS, FSA

Karen Jiang, MAAA, FSA, CERA

Jason Kehrberg, MAAA, FSA

Stephen Krupa, MAAA, FSA

Linda Lankowski, MAAA, FSA
Chanho Lee, MAAA, FSA

Michael McCarty, MAAA, FSA

Reanna Nicholsen, MAAA, FSA

Scott O'Neal, MAAA, FSA

Gary Osterhout, MAAA, FSA

Roland Rose, MAAA, FSA

Karen Rudolph, MAAA, FSA

Grace Senat, MAAA, FSA

Benjamin Slutsker, MAAA, FSA

Vincent Tsang, MAAA, FSA

Christopher Whitney, MAAA, FSA

<img src="https://cdn.mathpix.com/cropped/2024_03_15_8ba611b8476c665b9018g-002.jpg?height=342&width=696&top_left_y=1721&top_left_x=709" alt="image" style="width:100%;height:auto;">

1850 M Street NW, Suite 300

Washington, DC 20036-5805

## TABLE OF CONTENTS

Introduction. ..... 3
PBR Calculation Schematic ..... 4

1. Exemptions, Transition Rules, and Details on Products Covered. ..... 3
2. Available Information on Common Practice ..... 10
3. VM-20 Calculation ..... 11
4. VM-20 Calculation Overview—Part A. Net Premium Reserve (NPR) ..... 18
5. VM-20 Calculation Overview—Part B. Deterministic Reserve ..... 28
6. VM-20 Calculation Overview—Part C. Stochastic Reserve ..... 33
7. Stochastic Exclusion Test ..... 36
8. Deterministic Exclusion Test ..... 43
9. Difference From Cash Flow Testing-Scenario Reserve Calculation ..... 46
10. Considerations When Performing Reserve Calculations on Other Than the Valuation Date ..... 49
11. Details on Starting Assets and Asset Modeling. ..... 51
12. Details on Scenarios / Scenario Generators / Economic Assumptions ..... 68
13. Setting Prudent Estimate and Anticipated Experience Assumptions ..... 73
14. Setting Margins ..... 77
15. Setting Mortality Assumptions ..... 82
16. Setting Premium Assumptions ..... 93
17. Setting Policyholder Behavior Assumptions Other Than Premiums. ..... 95
18. Setting Expense Assumptions ..... 99
19. Setting Non-Guaranteed Element Assumptions ..... 101
20. Treatment of Reinsurance ..... 104
21. Treatment of Hedging / Derivative Programs ..... 109
American Academy of Actuaries

## Introduction

This practice note was prepared by the Life Principle-Based Approach Practice Note Work Group of the American Academy of Actuaries to provide information to actuaries on current and emerging practices concerning principle-based life insurance reserve valuation practices for individual life insurance. It is intended to supplement the available actuarial literature in the area under discussion. Actuaries are not in any way bound to comply with practice notes or to conform their work to the practices described in practice notes.

The practices here represent the views of actuaries in industry, consulting, and public accounting firms that have been involved in the development of the life reserving standards, along with practicing actuaries who have been valuing policies using VM-20 requirements. The purpose of the practice note is to assist actuaries with implementation of the principle-based life reserve valuation approach adopted by the NAIC as detailed in the Requirements for Principle-Based Reserves for Life Products-2020 Edition of VM-20, describing the requirements for calculating minimum valuation standard statutory reserves for individual life insurance products. It is important that the reader review any differences that exist between the version of VM-20 on which this practice note was based and the version that is viewed as applicable to current valuations because the Valuation Manual is a living document and subject to change.

It is expected that actuarial practice for determining principle-based statutory reserves for life insurance products will continue to emerge over time. It is likely that additional actuarial practice will be developed that is not contained in this practice note. The goal of this practice note is twofold: to assist actuaries who are implementing VM-20 with the understanding of what the requirements are and to provide an overview of actuarial practice. The work group attempted to meet both goals as well as it could.

Additions and revisions to this practice note will likely be needed in the future as practices are further developed and issues that are not anticipated below are addressed.

## PBR Calculation Schematic

<img src="https://cdn.mathpix.com/cropped/2024_03_15_8ba611b8476c665b9018g-005.jpg?height=1559&width=1525&top_left_y=440&top_left_x=300" alt="image" style="width:100%;height:auto;">

Chart assumes values are either consistently net of reinsurance or consistently direct (before reinsurance). DDPA = Due and Deferred Premium Asset.

Each VM-20 Reserving Category (ULSG; Term; Other) must follow this process separately.

## 1. Exemptions, Transition Rules, and Details on Products Covered

## Q 1.1: Which products are covered by VM-20?

A: According to Section II (Reserve Requirements) of the Valuation Manual, VM-20 applies to all individual life insurance policies issued on or after the operative date of the Valuation Manual that fall within the scope of VM-20. Policies subject to VM-20 include all individual life insurance policies whether directly written or assumed through reinsurance:

- Universal life insurance policies;
- Variable life and variable universal life insurance policies;
- Term life insurance policies;
- Traditional whole life insurance policies;
- Indexed life and indexed universal life insurance policies; and
- Combination policies that include other benefits such as annuity benefits or long-term care benefits in addition to life insurance benefits but are filed as individual life insurance policies.


## $Q$ 1.2: What products and reserves are not covered by $V M-20$, and where are these reserve requirements

 listed?A: The following shows the products and locations in the Valuation Manual of reserve requirements according to Section II:

- Guaranteed issue life insurance is specifically excluded from VM-20. A definition of a guaranteed issue life insurance policy can be found in VM-01. Reserve requirements for guaranteed issue life insurance follow VM-A and VM-C.
- Pre-need life insurance products are specifically excluded from VM-20. A definition of pre-need life insurance can be found in VM-01. Reserve requirements for pre-need life insurance follow VM-A and VM-C.
- Industrial life insurance products are specifically excluded from VM-20. A definition of industrial life insurance can be found in VM-01. Reserve requirements for industrial life insurance follow VM-A and VM-C.
- Annuity products-Reserve requirements are subject to VM-21 if variable annuity. For fixed annuity contracts, the requirements are in VM-A and VM-C except for the minimum requirements for the valuation interest rate for single premium immediate annuity contracts, and other similar contracts, issued after Dec. 31, 2017. The maximum valuation interest rates for those contracts are defined in VM-22. Section II of the Valuation Manual provides detail for establishing reserve requirements for annuity products.
- Deposit-type products-Reserve requirements are subject to VM-A and VM-C. Section II of the Valuation Manual provides detail for establishing reserve requirements for deposit-type products.
- Health insurance products-Reserve requirements are subject to VM-25 and VM-A and VM-C. Section II of the Valuation Manual provides detail for establishing reserve requirements for health insurance products.
- Credit life and disability products-Reserve requirements are subject to VM-26. Section II of the Valuation Manual provides definitions of types of credit life and disability products and detail for establishing reserve requirements for credit life and disability products.
- Claim reserves including waiver of premium claims are not subject to the PBR requirements of VM20, according to Section II of the Valuation Manual. The definition of claim reserves can be found in VM-01.


## $Q$ 1.3: Are simplified issue, accelerated underwriting, and guaranteed issue life insurance subject to VM20 reserve requirements?

A: The Valuation Manual explicitly excludes guaranteed issue life contracts from VM-20. Reserve requirements for guaranteed issue life insurance follow VM-A and VM-C. However, life insurance policies underwritten through accelerated underwriting or simplified issue, if not otherwise exempt, would be subject to VM-20 reserve requirements.

## $Q$ 1.4: What industry tables are used for Guaranteed Issue business?

A: Per the Reserve Requirements provided in Section II of the Valuation Manual, Subsection 1.B, the same table shall be used for reserve requirements as is used for minimum nonforfeiture requirements. This is further clarified within VM-02, Section 4.E for Guaranteed Issue (GI) life insurance:

| GI Life Insurance Policy Issue Date | Applicable Industry Table(s) |
| :---: | :---: |
| Prior to January 1, 2017 | - Ultimate form of the 2001 Commissioners Standard <br> Ordinary (CSO) Table |
| January 1, 2017 - December 31, 2018 | - Ultimate form of the 2001 CSO Table, OR <br> - 2017 CSO Table |
| January 1, 2019 - December 31, 2019 | - $\quad$ Ultimate form of the 2001 CSO Table, OR <br> - 2017 CSO Table, OR <br> - 2017 Commissioners Standard Guaranteed Issue Mortality <br> Tables (2017 CSGI) |
| January 1, 2020 and onwards | - Ultimate form of the 2001 CSO Table |

The 2017 CSGI Table was originally approved by LATF in 2018, with mandatory adoption of the 2017 CSGI Table for policies issued after Dec. 31, 2019. The mandatory adoption of the 2017 CSGI Table was removed from the 2020 VM and replaced with language providing for the table above. Future revisions are expected to address introducing a new table for GI life insurance policies.

## Q 1.5: Is group life insurance subject to VM-20 reserve requirements?

A: The Valuation Manual does not explicitly state whether group insurance is or is not subject to VM-20 reserve requirements. However, according to Paragraph B under the heading "Life Insurance Products" in Section II (Reserve Requirements) of the Valuation Manual, VM-20 sets the minimum reserve requirements for "individual life contracts". Some actuaries interpret this language as indicating that group insurance is not subject to VM-20. That being said, some actuaries might have less clarity for life insurance contracts that are filed as group life insurance for statutory reporting purposes but underwritten on an individual contract basis. If in question actuaries typically consult the domiciliary commissioner for further guidance.

## $Q$ 1.6: Are riders and supplemental benefits that are attached to life insurance policies subject to $V M-20$ reserve requirements?

A: According to VM-20 Section 2.H, reserves for riders and supplemental benefits are calculated as described in Section II of the Valuation Manual. According to Section II, if the rider or supplemental benefit does not have a separate premium or the value or benefits within the base policy and rider or supplemental benefit are determined in reference to each other, then the rider or supplement benefit is valued using the same reserve requirements as the base policy. This would result in the rider or supplemental benefit not only following the same Net Premium Reserve methodology as the base policy, but being grouped with the base policy for the purposes of VM-20 exclusion tests and VM-20 Reserving Category.

Some exceptions to the above rule are listed in VM-20. The first is that a ULSG or other secondary guarantee rider shall follow the ULSG reserve requirements under VM-20, including the Net Premium Reserve methodology and being grouped within the ULSG Reserve Category for the purposes of calculating the PBR reserve in Section 2 of VM-20 and performing the VM-20 exclusion tests. In addition, for supplemental benefits that include Guaranteed Insurability, Accidental Death or Disability Benefits, Disability of Waiver of Premium Benefits may be valued together or separately from the base policy.

If the rider or supplemental benefit has a separate premium or charge, and the value and benefits within the base policy and rider or supplemental benefit are not determined in reference to each other, and is not subject to the exceptions listed above, then the rider or supplemental benefit may be valued together or separately from the base policy. However, an exception to this is that a term life insurance rider with a guaranteed level or near level premium design is required to follow term reserve requirements, including the Net Premium Reserve, modeled reserve, and exclusion testing rules.

Some actuaries use a process similar to that shown in the following flowchart when interpreting how to apply Valuation Manual reserve requirements to a rider or supplemental benefit:

## PBR Rider Valuation Treatment

<img src="https://cdn.mathpix.com/cropped/2024_03_15_8ba611b8476c665b9018g-009.jpg?height=2025&width=1550&top_left_y=321&top_left_x=206" alt="image" style="width:100%;height:auto;">

## $Q$ 1.7: Are return of premium (ROP) riders attached to life policies treated as a stand-alone policy for purposes of VM-20?

A: Consistent with Actuarial Guideline XLV, as referenced in VM-C, some actuaries combine ROP benefits with the base policy benefits for the purposes of VM-20, whether there is a separate premium or not. Some actuaries interpret that combining ROP benefits with the base policy is also consistent with requirements outlined in Section II of the Valuation Manual.

## $Q$ 1.8: Will VM-20 apply to all inforce policies as of the operative date?

A: VM-20 applies only to policies issued on or after the operative date of VM-20. It does not apply to business in force prior to the operative date.

## $Q$ 1.9: Are there any transition rules at the operative date of the Valuation Manual?

A: Section II of the Valuation Manual states that a company may elect to establish minimum reserves using VM-A and VM-C for business otherwise subject to VM-20 during the first three years following the operative date of the Valuation Manual.

## $Q$ 1.10: Do changes to a policy issued prior to the operative date of the Valuation Manual (e.g., the addition of a rider) make it subject to the requirements of the Valuation Manual?

A: Section II of the Valuation Manual states that the minimum reserve requirements in the Valuation Manual apply to contracts issued on or after the operative date. Therefore, only if a new contract is issued would the requirements of the Valuation Manual, and VM-20 if applicable, apply. Many actuaries would conclude that when a new policy number is issued for a contract after the operative date of the Valuation Manual, VM-20 would apply.

## Q 1.11: What is the Life PBR Exemption?

A: Subject to commissioner approval, a Life PBR Exemption (informally referred to as the "small company exemption") is allowed for companies that meet the following conditions (Valuation Manual, Section II):

- The company has less than $\$ 300$ million of ordinary life premium and, if the company is a member of a group of life insurers, the group has combined ordinary life premiums of less than $\$ 600$ million. This premium threshold excludes premiums for Guaranteed Issue policies and preneed life contracts. It also excludes amounts that represent transfer of reserves in force as of the effective date of a reinsurance assumed transaction as reported in the blue book.

The exemption may be filed for ordinary life insurance policies except for ULSG policies with a secondary guarantee that does not meet the definition of non-material secondary guarantee found in VM-01.

## Q 1.12: Is the Life PBR Exemption optional?

A: The exemption is optional. If a company decides to use the exemption, it must elect the exemption each year prior to July 1 by filing a statement with its commissioner certifying the company meets the exemption criteria. That statement must also be included with the NAIC second-quarter filing.

## $Q$ 1.13: If a company uses the Life PBR Exemption for a time period and then no longer qualifies or the

exemption is disallowed, are reserves recomputed from the effective date of PBR or going forward from the date the exemption is no longer allowed?

A: The computation method in place at policy issue is retained throughout the life of the policy.

## Q 1.14: What is the process for electing the Life PBR Exemption?

A: Section II of the Valuation Manual states that a company meeting the exemption conditions may file a statement of exemption for the current calendar year with its domestic commissioner prior to July 1 of that year. This exemption may be filed for ordinary life insurance policies except any ULSG business that does not meet the definition for non-material secondary guarantee found in VM-01. The statement of exemption must state that the exemption condition is met based on Ordinary Life Insurance premiums from the prior calendar year financial statements. The statement of exemption must be included with the NAIC filing for the second quarter of that year.

The commissioner, however, may reject such statement of opinion prior to September 1 and require the company to follow the requirements of VM-20 for Ordinary Life policies.

## Q 1.15: If a company elects the Life PBR Exemption, how are reserves computed?

A: If a company is granted the Life PBR Exemption, the minimum reserve requirements for Ordinary Life policies are those pursuant to VM-A and VM-C.

$Q$ 1.16: If a company uses the Life PBR Exemption, is it allowable to use the new mortality tables as they are released?

A: Yes. The Life PBR Exemption provides that minimum reserve requirements for Ordinary Life policies follow VM-A and VM-C using the mortality as defined in VM-20 Section 3.C. 1 and VM-M Section 1.H (e.g., 2017 CSO).

Q 1.17: When will mortality as defined in VM-20 Section 3.C.1 and VM-M Section 1.H (e.g., 2017 CSO) become the prevailing mortality for tax reserves under IRC 807(c)?

A mortality table becomes prevailing for tax reserves when it is the most recent table permitted to be used in computing reserves by at least 26 states as of the date of issue of the contract. Because the Standard Valuation Law, which includes the Valuation Manual, has been approved by at least 26 states as of Jan. 1, 2017, the mortality tables included in VM-M will be prevailing as of Jan. 1, 2017, for use in tax reserves.

This means that the 2017 CSO is the prevailing mortality table for tax reserves as of Jan. 1, 2017.

However, the tax law provides for a transition period. If the prevailing commissioners' standard mortality table as of the beginning of any calendar year (e.g., year of change) is different from the prevailing commissioners' standard mortality table as of the beginning of the preceding calendar year, the insurer may use the former table as of Jan. 1 of the "year of change" for any contract issued after the change and for a three-year period beginning on Jan. 1 of the "year of change." The "year of change" is the calendar year in which the prevailing commissioners' standard mortality table, as of the beginning of the year, is different from the prevailing commissioners' standard table as of the beginning of the preceding year.

Thus, because the 2017 CSO table became prevailing as of Jan. 1, 2017, for policies issued as of Jan. 1, 2017, and later, a company may elect to use 2001 CSO for policies issued from Jan. 1, 2017, through Dec. 31, 2019 (three-year period beginning on Jan. 1 of the "year of change"). It would then need to use 2017 CSO for tax purposes beginning with policies issued Jan. 1, 2020.

This three-year transition period for tax reserves is consistent with the transition period provided in VM-20 for the 2017 CSO for statutory reserving.

It should be noted that the Valuation Manual contains the following Guidance Note with respect to tables adopted after the Valuation Manual is effective:

The Valuation Manual can be updated by the NAIC to define a new valuation table. Because of the various implications to systems, form filings, and related issues (such as product tax issues), lead time is needed to implement new requirements without market disruption. It is recommended that this transition be for a period of about 4.5 years - that is, that the table be adopted by July 1 of a given year, that it be permitted to be used starting Jan. 1 of the second following calendar year, that it be optional until Jan. 1 of the fifth following calendar year, thereafter mandatory.

## $Q$ 1.18: What is a non-material secondary guarantee universal life policy?

A: The term is defined in VM-01: Definitions for Terms in Requirements. There are three conditions that need to be met at issue of the policy.

- The policy can have only one secondary guarantee provision, and it must be of the specified annual or cumulative premium type.
- The duration of the secondary guarantee can be no longer than 20 years from issue for issue ages through 60, grading down by $2 / 3$ year for each higher issue age to 82 . For issue ages 83 and older, the period can be at most five years.
- The present value of the required premiums for the secondary guarantee must be at least as great as the present value of net premiums over the maximum secondary guarantee period allowable under the contract (in aggregate and subject to the above duration limit). Such present values use minimum allowable Valuation Basic Table (VBT) rates and maximum valuation interest rate.

Q 1.19: Does a company have to apply for the Life PBR Exemption the first year that VM-20 is effective or can it use the three-year phase-in period first before applying for the exemption?

A: Some actuaries conclude that the three-year phase-in period can be applied before applying for the Life PBR Exemption. An actuary may wish to check with the domiciliary state to be sure it agrees with that interpretation.

## $Q$ 1.20: Some states offer single state exemption which exempts companies only of operating in that state from PBR. What are Blue Book and VM-20 supplement implications for those companies?

A: In situations where the state offers a single state exemption, companies need an exemption in writing from the commissioner. The company may use assumptions and methods used prior to the operative date of the valuation manual in addition to any requirements established by the commissioner. The commissioner might not require such a company to fill out VM-20 supplement Part 1.

## 2. Available Information on Common Practice

## $Q$ 2.1: Which actuarial standards of practice (ASOPs) would apply to the actuary when performing the

tasks in conjunction with determining reserves under VM-20?

A: According to ASOP No. 1, Section 4.3, "Actuaries are responsible for determining which ASOPs apply to the task at hand." The following ASOPs, as of the date of this practice note, are among those the actuary may wish to consider:

ASOP No. 1 Introductory Actuarial Standard of Practice

ASOP No. 2 Nonguaranteed Charges or Benefits for Life Insurance Policies and Annuity Contracts

ASOP No. 7 Analysis of Life, Health, or Property/Casualty Insurer Cash Flows

ASOP No. 11 Treatment of Reinsurance Transactions Involving Life or Health Insurance 1

ASOP No. 12 Risk Classification (for All Practice Areas)

ASOP No. 15 Dividends for Individual Participating Life Insurance, Annuities, and Disability Insurance

ASOP No. 22 Statements of Opinion Based on Asset Adequacy Analysis by Actuaries for Life and Health Insurers

ASOP No. 23 Data Quality

ASOP No. 25 Credibility Procedures

ASOP No. 38 Using Models Outside the Actuary's Area of Expertise (Property and Casualty)

ASOP No. 41 Actuarial Communications

ASOP No. 52 Principle-Based Reserves for Life Products under the NAIC Valuation Manual

The Actuarial Standards Board is likely to issue a fourth exposure draft of a new proposed ASOP, Modeling and a second exposure draft of a new proposed ASOP, Setting Assumptions. (ASOP No. 1, Section 3.1.7 explains: "Exposure drafts of the ASOP ... form part of the literature of the actuarial profession; actuaries may look to them at their discretion for advisory guidance. An ASOP is not binding until the effective date of the ASOP.”)

## Q 2.2: Are there other practice notes that cover topics relevant to principle-based reserve calculations as described in the Valuation Manual?

A: The Asset Adequacy Analysis practice note, the Credibility practice note, the Model Governance practice note, the PBR Assumptions Resource Manual, and the PBA Projections practice note include relevant information for actuaries performing PBR reserve calculations. These practice notes can be found at the American Academy of Actuaries website at http://www.actuary.org/category/site-section/publicpolicy/practice-notes.

## Q 2.3: VM-20 often uses the term "Qualified Actuary." What does VM-20 mean by Qualified Actuary and

 how does this differ from "Appointed Actuary"?A: The term "Appointed Actuary" means a Qualified Actuary who is appointed or retained in accordance with the Valuation Manual to prepare the actuarial opinion required in Section 3.A and/or 3.B of Model \#820. The term "Qualified Actuary" means an individual who meets the requirements specified in the Valuation Manual and is thereby qualified to sign the applicable statement of actuarial opinion. The requirements an actuary
must satisfy to be considered qualified to sign the applicable statement of actuarial opinion can be found in the Qualification Standards for Actuaries Issuing Statements of Actuarial Opinion in the United States (2008) promulgated by the American Academy of Actuaries.

## $Q$ 2.4: Are there practices in other countries that an actuary can review for reference?

A: Published papers on principle-based reserve calculations in other countries may provide useful information to U.S. actuaries. It should be noted, however, that acceptable practice in other countries is not a safe harbor for principle-based calculations in the United States. Annotation 3-1 of the Code of Professional Conduct states that "[i]t is the professional responsibility of an Actuary to observe applicable standards of practice ... for the jurisdictions in which the Actuary renders Actuarial Services.” U.S. actuaries subject to the Code are obliged to follow the standards of practice promulgated by the Actuarial Standards Board. Annotation 3-2 of the Code of Professional Conduct establishes, however, that " $[\mathrm{w}]$ here a question arises with regard to the applicability of a standard of practice or where no applicable standard of practice exists, an Actuary shall utilize professional judgment, taking into account generally accepted actuarial principles and practices.”

The Canadian Institute of Actuaries has Valuation Technique Papers (VTP) and educational notes that explain how Canadian actuaries calculate reserves. There are some similarities between U.S. principle-based reserves and Canadian valuation techniques. For Canadian documentation, please see the Canadian Institute of Actuaries website at www.actuaries.ca.

## 3. VM-20 Calculation

Q 3.1: VM-20 describes three components of the minimum reserve: the Net Premium Reserve (NPR), the Deterministic Reserve (DR), and the Stochastic Reserve (SR). Is the company required to calculate all three components for all policies?

A: The Net Premium Reserve is required to be calculated for all policies subject to VM-20. The company may elect to perform exclusion tests that, if passed, exempt some groups of policies from the Deterministic Reserve and/or the Stochastic Reserve. These exclusion tests are optional, and a company can decide to calculate all three components for all policies. For certain types of products and riders, namely term and ULSG with a material secondary guarantee provision (i.e., one that does not meet the definition of "nonmaterial secondary guarantee”), Deterministic Reserves must be calculated so the Deterministic Exclusion Test is not applicable.

Later sections of this practice note provide detail for each of the three components that go into the calculation of the minimum reserve: the Net Premium Reserve, the Deterministic Reserve, and the Stochastic Reserve.

## $Q$ 3.2: What is the minimum reserve for all policies as required by VM-20?

A: Section 2.A of VM-20 defines the minimum reserve in terms of VM-20 Reserving Categories. The total minimum reserve equals the sum of the minimum reserve as determined for each VM-20 Reserving Category.

It is important to note that VM-20 Section 3 defines the requirements for the policy Net Premium Reserve; Section 3.E defines the policy minimum Net Premium Reserve as the policy Net Premium Reserve less a credit for reinsurance ceded.

In general, the minimum reserve for a VM-20 Reserving Category is determined as the sum of policy minimum Net Premium Reserves plus the excess, if any, of the greater of the Deterministic Reserve for all policies in the VM-20 Reserving Category and the Stochastic Reserve for all policies in the VM-20 Reserving Category over the quantity (A-B), where A equals the sum of policy minimum Net Premium Reserves for all policies in the VM-20 Reserving Category and B equals any due and deferred premium asset held on account of those policies. When determining the minimum reserve on a net-of-reinsurance basis, all three reserve components are net of any credit for reinsurance ceded for the policies in the VM-20 Reserving Category.

In mathematical terms, this could be represented as:

$$
\text { Minimum Reserve }=\operatorname{AggNPR}+\operatorname{Max}(0,(\operatorname{Max}(\mathrm{DR}, \mathrm{SR})-(\operatorname{AggNPR}-\mathrm{DDPA})))
$$

Where

| AggNPR | $=$ | Sum of Policy Minimum Net Premium Reserves |
| :--- | :--- | :--- |
| DR | $=$ | Deterministic Reserve |
| SR | $=$ | Stochastic Reserve |
| DDPA | $=$ | Due and Deferred Premium Asset |

Section 2 defines three VM-20 Reserving Categories: Term Policies, Universal Life with Secondary Guarantee policies, and life insurance policies subject to Section 3.A.2. The sum of the minimum reserve for each VM-20 Reserving Category equals the total minimum reserve.

All policies are assumed to be subject to the calculation of all three reserve components of VM-20 (NPR, DR, SR) unless the company has either elected to exclude the group of policies from the SR calculation or both the SR and DR calculations and has applied and passed the applicable exclusion tests and documented the results. However, VM-20 does not allow the Deterministic Exclusion Test for either the Term VM-20 Reserving Category or the ULSG VM-20 Reserving Category. Therefore, for these two VM-20 Reserving Category, all three reserve components of VM-20 (NPR, DR, SR) will need to be calculated unless the company elects to exclude the Term and/or ULSG VM-20 Reserving Category of policies from the SR calculation, applied and passed the Stochastic Exclusion Test (SET), and documented the results.

If the company makes use of the exclusion tests, then for a group of policies that pass both the Stochastic Exclusion Test and the Deterministic Exclusion Test, the minimum reserve for that group of policies is the sum of the policy minimum Net Premium Reserves.

For a group of policies that pass the Stochastic Exclusion Test but not the Deterministic Exclusion Test, the minimum reserve equals: the sum of the policy minimum Net Premium Reserves plus the excess, if any, of the Deterministic Reserve over the sum of the policy minimum Net Premium Reserves adjusted for any due and deferred premium asset held on account of those policies.

For a group of policies that fail the Stochastic Exclusion Test and for policies not subjected to any exclusion tests, the minimum reserve equals: the sum of the policy minimum Net Premium Reserves plus the excess, if any, of the greater of the Deterministic Reserve and the Stochastic Reserve over the sum of the policy minimum Net Premium Reserve adjusted for any due and deferred premium asset held on account of those policies.

Q 3.3: Why is the Net Premium Reserve adjusted for any due and deferred premium asset in determining the excess, if any, of the greater of the Deterministic Reserve and Stochastic Reserve over the Net Premium Reserve?

A: Because two of the components of the comparison (the Deterministic Reserve and Stochastic Reserve) are calculated as of the reporting date, and require that due and deferred premiums be included in the expected future cash flows when calculating the DR and SR, whereas the Net Premium Reserve is as of the policy anniversary date, so per statutory accounting rules an adjustment to the Net Premium Reserve is required to put all of the values on the same basis.

## $Q$ 3.4: How would actuaries approach the calculation of the minimum reserve requirement under VM-20?

A: One approach for completing the calculation is outlined below.

- Determine policies in scope of the VM-20 requirements. Determine in which of the three VM-20 Reserving Categories of Section 2 these policies belong.
- Within each VM-20 Reserving Category, determine the model segments for all policies in scope of the requirements. Per the definition of model segment in VM-01, this determination will generally align with the company's asset segmentation plan, investment strategies, or approach used to allocate investment income for statutory purposes. It should be noted that a model segment could be an entire block of business.
- Select the amount of starting assets for each model segment and allocate existing assets to each model segment.
- Build asset and liability populations in a cash flow model. This cash flow model may represent each in-scope policy in force on the date of valuation or represent policies by grouping such policies into representative cells of model plans as described in Section 7.B.2.
- Determine anticipated experience assumptions for all risk factors.
- Determine investment expense assumptions and asset default assumptions for each model segment.
- Determine prudent estimate assumptions for all risk factors that are not prescribed or stochastically modeled by applying margins to the anticipated experience assumptions.
- Perform Stochastic Exclusion Test (if the company elects to do so). This may be performed for any block of policies for which this test is deemed appropriate. If the block of policies passes the test, the company can skip the calculation of the Stochastic Reserve for those policies.
- Determine the Stochastic Reserve as described in Section 5 of VM-20 for policies where the Stochastic Reserve is required or deemed appropriate.
- Perform Deterministic Exclusion Test (if the company elects to do so). This may be performed only for life insurance policies subject to Section 3.A. 2 (per Section 2.A.3). If the block of policies passes the test, the company can skip the calculation of the Deterministic Reserve for those policies.
- Calculate the Deterministic Reserve as described in Section 4 of VM-20 for policies where the Deterministic Reserve is required.
- Calculate the Net Premium Reserve for all policies subject to VM-20 as described in Section 3 of VM-20.
- Calculate the minimum reserve for all policies within each Section 2 VM-20 Reserving Category subject to VM-20 as the sum of the following amounts:

o For the group of policies that pass both the Stochastic Exclusion and the Deterministic Exclusion Tests, the minimum reserve equals the sum of the policy Net Premium Reserves.

o For the group of policies that pass the Stochastic Exclusion Test but fail the Deterministic Exclusion Test or are not eligible for it, the minimum reserve equals the sum of the policy Net Premium Reserves plus the excess, if any, of the Deterministic Reserve for those policies over the quantity (A - B), where A = the sum of the policy Net Premium Reserves and B = any due and deferred premium asset held on account of those policies.

o For the group of policies that fail the Stochastic Exclusion Test, and for the group of policies not subject to the exclusion tests, the minimum reserve equals the sum of policy Net Premium Reserves plus the excess, if any, of the greater of the Deterministic Reserve and the Stochastic Reserve over the quantity ( $A$ - B), where $A=$ the sum of the policy Net Premium Reserves and $\mathrm{B}=$ any due and deferred premium asset held on account of those policies.

- Calculate the total minimum reserve as the sum of the minimum reserve for each of the three VM-20 Reserving Categories.

Some actuaries undertake approaches that are different than what is summarized above depending on the specific circumstances of their company.

$Q$ 3.5: In determining the minimum reserve under Section 2, how are separate accounts handled when comparing the NPR, DR, and SR for variable products?

A: Section II of the Valuation Manual specifies that minimum reserve requirements for variable and nonvariable individual life contracts are provided by VM-20, except for pre-need life contracts, industrial life contracts, and credit life contracts. The NPR for variable products is determined according to Section 3.A. If the variable contract is a term policy or ULSG, then Section 3.A. 1 applies. Otherwise, Section 3.A. 2 applies. Section 3.A. 2 would point to the current Commissioners Reserve Valuation Method (CRVM) requirements, which include a provision for Separate Accounts in the reserve. So the comparison in Section 2 for variable products does reflect separate accounts in each of the three components.

Q 3.6: When allocating the total reserve between the general account (GA) and the separate account (SA), VM-20 states that the amount allocated to the GA must not be less than zero, and the amount allocated to the SA must not be less than the sum of the cash surrender values and not be greater than the sum of the account values attributable to the separate account portion of all such contracts. If the company books a negative amount into the general account due to the CRVM expense allowance, couldn't this result in an increase in the total reserve ( $G A+S A$ ) if the negative amount cannot be recognized?

A: Because the SA reserve has a floor of the variable cash surrender value and a ceiling of the variable account value, the first constraint of GA reserve not less than zero also means there is an implicit floor of the SA equal to the minimum reserve. So the sum of the SA and GA will not ever exceed the minimum reserve.

## Q 3.7: Why would an actuary perform the Stochastic Exclusion Test?

A: Some actuaries would calculate the Stochastic Exclusion Test because the block of policies does not have material market risk and the Stochastic Reserve will not contribute to the minimum reserve calculation. The benefit in that instance is that the time and expense to determine the Stochastic Reserve is not required. Some actuaries decide to perform the stochastic calculation even if the group of policies would pass the Stochastic Exclusion Test because there may be some diversification or risk offsets the company would then recognize in the minimum reserve calculation under VM-20 or for other reasons.

## Q 3.8: Why would an actuary perform the Deterministic Exclusion Test?

A: Some actuaries with policies that pass the Stochastic Exclusion Test would also perform the Deterministic Exclusion Test to avoid the burden of performing the deterministic reserve calculation. Again, some actuaries would still calculate the Deterministic Reserve even if the policies pass the Deterministic Exclusion Test as it can be used in the VM-20 calculation even if the Deterministic Exclusion Test is passed.

## $Q$ 3.9: How does an actuary define a model segment and determine the policies to include in each model segment?

A: Section 7.A of VM-20 addresses the cash flow model requirements for the Stochastic and Deterministic

Reserves. This section requires the model segments to be consistent with the company's asset segmentation plan, investment strategies, or approach used to allocate investment income for statutory purposes. Each policy can be included in only one segment. Some actuaries might also consider how non-guaranteed elements are set in determining model segments. It should be noted that a model segment can be an entire block of business or an entire VM-20 Reserving Category, where VM-20 Reserving Categories are defined by Section 2.A.

## Q 3.10: What is the difference between the grouping of policies described in Section 7.B. 2 and the VM-20 Reserving Category described in Section 2.A?

A: Section 7.B. 2 addresses the level of granularity when constructing the cash flow model. VM-20 allows policies to be grouped into modeling cells for both the Stochastic Reserve and Deterministic Reserve calculation, rather than requiring a seriatim, policy-by-policy reserve calculation. VM-20 requires that the grouping of policies must be done in a manner consistent with Section 2.G. VM-20 requires a seriatim calculation (i.e., with no grouping) for the Net Premium Reserve.

Section 2.A refers to the minimum reserve in terms of three VM-20 Reserving Categories, where these categories consist of Term policies, ULSG policies, and other life insurance policies subject to Section 3.A.2. Within each of these VM-20 Reserving Categories, the concept of aggregation refers to the combining of cash flows when calculating the Stochastic Reserve for the purpose of recognizing the amount of risk diversification among the policies. Aggregating policies into a common model segment allows the cash flows arising from the policies for a given stochastic scenario to be netted against each other (i.e., allows risk offsets between policies to be recognized). Full aggregation would find the cash flows for all policies are combined together in one large group. Currently, full aggregation is not allowed due to the VM-20 Reserving Categories
defined by Section 2.A and the allocation provision of Section 5.G, which would come into play if a company includes policies from two or more VM-20 Reserving Categories in the calculation of a Stochastic Reserve.

## Q 3.11: What considerations are taken into account when deciding how to group policies when defining modeling cells for the cash flow model under Section 7.B.2?

A: First, the actuary will want to decide which of the Section 2.A VM-20 Reserving Category each policy belongs in. Then, within each VM-20 Reserving Category, the actuary may wish to consider the similarities between policies and their respective assumptions when grouping policies together. Some actuaries use model office projections for a subset of scenarios to determine the impact various groupings may have on the resulting reserve amount to ensure that the policy groupings do not have a material impact. Some actuaries rely on seriatim projection output data across a sampling of scenarios to gather data that suggests how policies are grouped together. The actuary may wish to consider Section 3.3 of ASOP No. 52, Principle-Based Reserves for Life Products under the NAIC Valuation Manual, which discusses considerations in modeling for principle-based calculations.

Q 3.12: If traditional UL and ULSG policies are managed in the same asset portfolio, are we allowed to model them together for PBR? If term is part of that, how would we split them out for reporting purposes?

A: Term insurance could be modeled together with Universal Life (UL) and Universal Life with Secondary Guarantees (ULSG) policies if the company is managing the risks of two or more products with significantly different risk profiles as part of an integrated risk management process.

Per Section 4.C of VM-20, if a group of policies for which a Deterministic Reserve is calculated includes policies from more than one VM-20 Reserving Category, where VM-20 Reserving Category is defined as in Section 2, to be term insurance policies, ULSG policies or all other types of policies, a Deterministic Reserve shall be determined for each subgroup of policies consisting of only those policies from each individual VM-20 Reserving Category by following the process of Section 4.A and Section 4.b of VM20. The Net Asset Earned Rate (NAER) used for discounting each such subgroup may be the NAER for the group of policies. If the sum of the Deterministic Reserves for these subgroups does not equal the total Deterministic Reserve calculated for the group of policies as a whole, the Deterministic Reserve for the group of policies shall be allocated to each such subgroup proportionally. The amount of the Deterministic Reserve calculated for the group is the one that is reported, even if it is less than the sum of the Deterministic Reserves calculated separately for the subgroups. VM-31 Section 3.D.11.f outlines the reporting requirements.

Per Section 5.G of VM-20 the company shall calculate the Stochastic Reserve for policies from each VM-20 Reserving Category on a stand-alone basis as well as on a combined basis. VM-31 Section 3.D.11.g outlines the reporting requirements.

## $Q$ 3.13: What is the required modeling time step / frequency of projection?

A: While there is no required model time step in the VM-20 requirements, actuaries commonly use monthly, quarterly, or annual time steps in cash flow projections. In choosing a time step, many actuaries consider factors such as product characteristics, the frequency and method of setting credited interest rates or other non-guaranteed elements, the sensitivity of the projection to the time step, and practical limitations. Some
actuaries have a quarterly time step for a specific model segment while using a monthly time step for other model segments. Some actuaries use longer (annual) time steps for very stable model segments with little interest rate sensitivity.

## $Q$ 3.14: What is the required length of the projection period?

A: Section 7.A.1.d mandates that the model project "cash flows for a period that extends far enough into the future so that no obligations remain.” However, Section 2.G allows for approximations when these approximations do not cause a material understatement of the reserve. Some actuaries might interpret this to mean that shorter projection periods are appropriate when no material liabilities remain after some period of time, or when the actuary can demonstrate that longer projection periods would not result in a materially greater reserve. Some actuaries would instead assume a 100 percent termination rate (either through death or surrender) to ensure no obligations remain at the end of the projection period where the actuary believes that this assumption would not materially understate the reserve.

## Q 3.15: How would the actuary determine whether using a longer projection period would result in a "materially greater reserve"?

A: Some actuaries determine that the amount of business in force after a certain period is immaterial and could not lead to a materially greater reserve.

It is also possible that some actuaries would use current or historical results to determine that the greatest present value of accumulated deficiencies is achieved within the projection period for every scenario in the Stochastic Reserve calculation. This analysis could include actually performing the projection with a longer projection period (potentially with a more compressed model) and determining that there is no material increase in the Stochastic Reserve calculation. Other analysis could be used including an analysis of when the greatest present value of accumulated deficiency (GPVAD) occurs in the calculation (i.e., if the GPVAD occurs at a point within the projections for all of the scenarios where it is not possible for future deficiencies to become the greatest).

Other actuaries rely on historical reserve calculations. For example, assume a longer projection period was run historically and showed that in all cases the GPVAD occurred prior to a certain projection year. Assuming no changes in the policy mix or assumptions have been made that would affect this outcome, a projection period that includes the GPVAD year but does not go all of the way out to the end of the policy period for all policies may be shown not to materially understate the reserve.

## Q 3.16: How is an individual policy reserve defined under VM-20?

A: The seriatim Net Premium Reserve is the floor for the reserve for any specific policy. Section 2.C specifies that the reserve for each VM-20 Reserving Category, as defined in Section 2.A, is allocated to each policy within that VM-20 Reserving Category in the same proportion as the minimum Net Premium Reserve for that policy to the minimum Net Premium Reserve for the VM-20 Reserving Category.

Each policy's share of the excess reserve is determined by multiplying the Net Premium Reserve for that policy by the ratio of the reserve excess divided by the sum of policy Net Premium Reserves for the applicable VM-20 Reserving Category. In this context, the Net Premium Reserve is net of any credit for reinsurance ceded. For example, consider policy (x):

$$
\operatorname{NPR}(\mathrm{x})=100
$$

DR Excess of VM-20 Reserving Category A (containing (x)) $=80$

Sum of policy minimum NPRs of VM-20 Reserving Category A $=1,000$

Min Reserve(x) $=100+[100 x(80 / 1000)]=108$

VM-20 Section 2.C. does allow an exception to this approach for companies to make best efforts to minimize allocating the Deterministic or Stochastic Reserve in excess of the Net Premium Reserve, with any adjustment for due and deferred premiums, to policies which did not produce this excess. Some actuaries make use of this exception when necessary to produce reasonable reinsurance reserve credits at the reinsurance treaty level.

## Q 3.17: How might an actuary determine that simplifications and approximations do not cause a material understatement of the reserve, as required by Section 2.G?

A: Some actuaries test the impact of using simplifications / approximations by calculating the minimum reserve without the simplifications / approximations on a small block of policies that are a good proxy for the entire group of policies, and then comparing the result to the minimum reserve on the same small block of policies with the simplifications / approximations. Another approach used by some actuaries is to calculate the minimum reserve on all policies both with and without the simplifications / approximations every three to five years to see whether there are material understatements. This comparison could occur at a time other than the valuation date.

## 4. VM-20 Calculation Overview—Part A. Net Premium Reserve (NPR)

## Q 4.1: How does an actuary determine which of the Net Premium Reserve calculations in Section 3 of VM20 apply?

A: Section 3.A. 1 of VM-20 provides that term insurance policies and universal life policies with a secondary guarantee should follow the calculations in Section 3. When valuing term riders pursuant to Paragraph E in "Riders and Supplemental Benefits Requirements" in Section II, the reserve requirements for term policies are applicable. Section 3.A. 2 provides that all other policies subject to VM-20, but for which 3.A. 1 does not apply, are subject to the requirements in VM-A, VM-C, and VM-M for basic reserves. VM-A, VM-C, and VM-M reproduce the CRVM methodology and assumptions in existence prior to VM-20.

VM-01 includes a definition for the term "secondary guarantee.” It states:

A "secondary guarantee" is a conditional guarantee that a policy will remain in force, even if its fund value is exhausted, for either:

- more than five years (the secondary guarantee period), or
- five years or less (the secondary guarantee period) if the specified premium for the secondary guarantee period is less than the net level reserve premium for the secondary guarantee period based on the CSO valuation tables defined in VM-20 Section 3.C and VM-M and the valuation interest rates
defined in this Section, or if the initial surrender charge is less than $100 \%$ of the first year annualized specified premium for the secondary guarantee period.

Once the policy type has been determined, the NPR methodology follows according to policy type as referenced below.

| Policy Type | Applicable NPR Methodology |
| :--- | :--- |
| Term Insurance | Section 3.B.4. |
| ULSG—during SG period | Max(Section 3.B.5; ${ }^{1}$ Section 3.B.6) |
| ULSG—after expiration of the SG period | Section 3.B.5 |

## Q 4.2: What are the steps for determining the NPR for term insurance policies?

A: Per Section 3.B.4.b, determine the adjusted gross premiums for the policy. These will be equal to the annual mode guaranteed gross premiums for the policy multiplied by the factors below.

<img src="https://cdn.mathpix.com/cropped/2024_03_15_8ba611b8476c665b9018g-022.jpg?height=143&width=629&top_left_y=1072&top_left_x=395" alt="image" style="width:100%;height:auto;">

Then, determine the uniform percentage of the present value of adjusted gross premiums equivalent to the present value of benefits (PVB) at issue plus $\$ 2.50$ per $\$ 1,000$ of insurance. The product of the uniform percentage and the adjusted gross premiums is the vector of valuation net premiums (unless adjustments as described next are required).

Adjustment to the valuation net premium may be required for policies subject to the shock lapse provisions. In any year that the prescribed lapse rate is greater than or equal to $25 \%$, a shock lapse is deemed to have occurred. For periods following the shock lapse, if the present value of valuation net premiums (PVP) exceeds the PVB by more than 35\%, then the valuation net premium following the shock lapse must be reduced uniformly to produce a PVP/PVB ratio of $135 \%$. If the application of the $135 \%$ limitation results in an adjustment to the valuation net premiums following the shock lapse, increase the valuation net premiums for policy years prior to the shock lapse by a uniform percent. At issue and after adjustments, the present value of adjusted gross premiums equals the PVB at issue plus $\$ 2.50$ per $\$ 1,000$ of insurance. This situation results in two uniform percentages, one for the policy years prior to the shock lapse and one for the policy years following the shock lapse. Policies with more than one shock lapse shall determine adjustments using only one shock lapse, namely the shock lapse that produces the largest PVP/PVB ratio.

The Net Premium Reserve equals the present value of future benefits less the present value of future valuation net premiums but not less than the greater of the policy's cash surrender value and the cost of insurance to the date to which the policy is paid. The cash surrender value used should be consistent (from the standpoint of determining the value on other-than-anniversary dates) with that used to determine the Net Premium Reserve on other-than-anniversary dates.[^0]

For valuation dates other than on policy anniversary, the Net Premium Reserve is intended to assume an annual premium mode for the policy and the actual valuation date relative to the policy issue date. A deferred premium asset may be required under accounting rules using the method in Section 3. The approach of calculating the reserve for a given policy taking into account the exact issue date of the policy may be similar to approaches undertaken prior to the Valuation Manual adoption. Background on these approaches can be found in SSAP 51.

## Q 4.3: What are the steps for determining the Net Premium Reserve for a universal life policy without a secondary guarantee, and for a universal life policy with a secondary guarantee?

A: Per VM-20 Section 3.A.2, if a universal life policy form has no secondary guarantee as defined in VM-20, then the Net Premium Reserve must be determined according to the requirements in VM-A, VM-C, and VMM. These are the same requirements applicable before the operative date of the Valuation Manual.

Per VM-20 Section 3.A.1, if a universal life policy form has a secondary guarantee, then the Net Premium Reserve must be determined according to the requirements of Sections 3.B.5 and 3.B.6.

## Q 4.4: VM-20 Section 3.B.5 addresses requiring the calculation of a reserve determined without consideration for the secondary guarantee provision. What purpose does this serve, and why is it necessary for a ULSG NPR?

A: The process for calculating the NPR for a ULSG policy involves the comparison of two calculated reserve amounts. The first reserve amount is defined in Section 3.B.5. This amount prevails when it is larger than the second reserve amount, which is defined in Section 3.B.6. The Section 3.B.5 reserve amount also prevails when the secondary guarantee period has expired. The steps to get a Section 3.B.5 reserve amount are described below.

- First determine the level gross premium at issue such that if this premium is paid each year for which premiums are permitted, the policy would remain in force for the entire coverage period. This determination is made using the policy's guarantees of interest, mortality, and expense. *Note that unlike Universal Life Model Regulation methodology, "maturity" (i.e., endowment) of the policy is not required, only inforce status.
- The premium derived in the step above is used in defining the expense allowance components for the policy at issue as shown below.

| o | Policy Year 1: | $100 \%$ of the premium and $\$ 2.50$ per $\$ 1,000$ <br> of insurance |
| :--- | :--- | :--- |
| o Policy Years 2-5: | $10 \%$ of the premium <br> o Policy Years 6+: | $0 \%$ of the premium |

- Determine the valuation net premium ratio from Section 3.B.5.c. The ratio is derived by taking the $\mathrm{PVB}$ at issue divided by the present value at issue of future gross premiums from the first step. These actuarial present values are calculated using the interest, mortality, and lapse assumptions that are appropriate for the policy from Section 3.C.
- The valuation net premium is the gross premium from the first step times the valuation net premium ratio.
- At any valuation date $t$, the Net Premium Reserve will equal the product of $m_{x+t}$ times $r_{x+t}$. The quantity $m_{x+t}$ is the present value of future benefits less the present value of future valuation net premiums and less the unamortized expense allowance for the policy. Determination of the unamortized expense allowance is provided in Section 3.B.5.b.
- The quantity $r_{x+t}$ is a ratio of two fund values, $e_{x+t}$ and $f_{x+t}$. The amount $e_{x+t}$ equals the actual policy fund value on the valuation date floored at zero. The amount $\mathrm{f}_{\mathrm{x}+\mathrm{t}}$ is determined as that amount which, together with the payment of future level gross premiums from the first step above, will keep the policy in force for the entire period that coverage is provided, using the policy guarantees for mortality, interest, and expense. The quantity $r_{x+t}$ equals 1 if $f_{x+t}$ is less than or equal to zero, otherwise $\mathrm{r}_{\mathrm{x}+\mathrm{t}}$ equals the quantity $\mathrm{e}_{\mathrm{x}+\mathrm{t}}$ divided by $\mathrm{f}_{\mathrm{x}+\mathrm{t}}$ capped at 1 .
- In determining the value of $\mathrm{m}_{\mathrm{x}+\mathrm{t}}$, the future benefits shall be based on:

0 the greater of $e_{x+t}$ and $f_{x+t}$,

o the future payment of level gross premiums as determined in Section 3.B.5.a., and

0 assuming the mortality, interest, and expense guaranteed in the contact.

## Q 4.5: What are the steps for determining the Net Premium Reserve for universal life policies with a secondary guarantee?

A: The net premium approach for universal life policies with a secondary guarantee provision that meets the definition of secondary guarantee as provided by VM-01 is explained below. If, however, all secondary guarantee periods have expired, then the methods described in Question 4.4 apply. If a policy has more than one secondary guarantee period, the approach assumes the longest guarantee period for which the policy can remain in force.

- During the secondary guarantee period, the Net Premium Reserve is the greater of the reserve calculated assuming no secondary guarantee and the reserve assuming the secondary guarantee. After the end of all secondary guarantee periods, the reserve is calculated according to the requirements for universal life policies without secondary guarantees. (Section 3.B.6.a.)
- As of the policy issue date, find the level gross premium that will maintain the policy in force for the length of the secondary guarantee period based on the secondary guarantee provisions for mortality, interest, and expenses. The valuation net premium is the uniform percentage of this gross premium such that at issue and over the secondary guarantee period, the present value of future valuation net premiums equals the present value of future benefits. The uniform percentage is the Valuation Net Premium Ratio (VNPR) and will not change for the policy. (Section 3.B.6.c.iii.)
- Base the valuation expense allowance components on the level premium amount determined in the prior step. (Section 3.B.6.c.ii.) The expense allowance components are:

o Policy Year 1: $\quad 100 \%$ of the premium and $\$ 2.50$ per $\$ 1,000$ of insurance

o Policy Years 2-5: $10 \%$ of the premium

o Policy Years 6+: $\quad 0 \%$ of the premium

Section 3.B.6.c.ii shows that the expense allowance is further adjusted by the VNPR.

- After issue and on each future valuation date, $t$, the Net Premium Reserve is determined as described below. The terms in this step are based on the definitions found in Section 3.B.

Where

$$
\operatorname{Min}\left[\frac{A S G_{x+t}}{F F S G_{x+t}}, 1\right] * N S P_{x+t}-E_{x+t}
$$

$A S G_{x+t}=$ the amount of the policy's actual secondary guarantee on the valuation date

$F F S G_{x+t}=$ the amount necessary to fully fund the policy's secondary guarantee on the valuation date

$N S P_{x+t}=$ the net single premium on the valuation date for the coverage provided by the secondary guarantee for the remainder of the secondary guarantee period, using the interest lapse and mortality assumptions found in Section 3.C; the $N S P_{x+t}$ includes consideration for death benefits only

$E_{x+t}=$ the policy's unamortized expense allowance at the valuation date calculated in a manner consistent with that for the policy without secondary guarantee, but using secondary guarantee parameters and a different valuation interest rate

The amount determined in this step is to be compared with the amount determined for the policy, absent the secondary guarantee, and the greater amount used as the Net Premium Reserve for the policy.

Q 4.6: How is the Net Premium Reserve calculated for policies with non-level death benefits or death benefits where the level of benefits is not guaranteed?

A: Similar to the pre-principle-based reserve (pre-PBR) Standard Valuation Law, the NPR section of VM-20 was drafted in the context of a level annual premium, level benefit contract. Adjustments to handle non-level benefits would generally follow the similar adjustments made pre-PBR. The only item in the NPR calculation that specifically relates to benefits is the first-year expense allowance of $\$ 2.50$ per $\$ 1,000$. No explicit instructions are included in VM-20 about whether a non-level death benefit would affect the first-year value to which the $\$ 2.50$ is applied, and therefore some actuaries would use the benefits payable in the first year.

Q 4.7: How is the Net Premium Reserve calculation affected if structural changes are made to the policy (i.e., changes separate from the automatic workings of the policy and initiated by the policyholder)?

A: In the NPR calculation, some actuaries would follow the principles and practices that would apply under pre-PBR CRVM if there were structural changes to the policy.

## Q 4.8: How are non-annual modes reflected in the Net Premium Reserve calculation?

A: The Net Premium Reserve requirements were written to provide a standard for terminal reserves under an assumption of an annual mode premium similar to the pre-PBR formulaic requirements. Standard actuarial adjustments such as inclusion of a deferred premium asset or unearned premium liability can be made to accommodate actual premium modes that are not annual. For flexible premium products, some actuaries
would not calculate a deferred premium asset or unearned premium liability, which is consistent with actuarial practice pre-PBR.

## Q 4.9: How are policy fees considered?

A: For universal life products, the Net Premium Reserve approach uses a "solved-for" premium and, as a result, any policy fees required by the product would not directly enter into the calculation. For term insurance products, the Net Premium Reserve approach requires the use of the maximum guaranteed gross premium for the policy year as the gross premium used in setting the valuation net premium. Section 3.B.4.c requires that the policy fee for the policy be included in the gross premium amount when determining the uniform percentage of Section 3.B.4.a.

## Q 4.10: Do return of premium (ROP) products introduce any special considerations for the Net Premium Reserve?

A: Section 3.B. 7 requires the actuarial present value of future benefits to include death benefits, endowment benefits including endowments intermediate to the term of coverage, and cash surrender benefits. Some actuaries would conclude that "endowments” includes ROP benefits. All these benefits are determined before consideration for reinsurance and before consideration for policy loans in force. In the situation of a return of premium benefit feature, all interim return amounts must be included in the Net Premium Reserve calculation. In this situation, Section 3.C.3.b.iii specifies a 6 percent lapse rate for the first half of the initial level premium period, and 0 percent for the remainder of the initial level premium period except the final year where the lapse rate is defined by 3.C.3.b.vi.

## Q 4.11: Is the Net Premium Reserve calculation similar to Universal Life Model Regulation Reserves (ULMR)?

A: In terms of Section 3.B.5 (Net Premium Reserve for universal life without considering any secondary guarantee provisions), there are some similarities. However, while there are concepts that are similar, there are some differences. Both methods employ premium-solves at issue and at valuation dates. However, the ULMR is solving for a maturity premium, while the VM-20 method is solving for a premium that keeps the policy in force and not necessarily matures the policy. The " $\mathrm{r}$ " ratio is similar in that it is a ratio of the actual policy account value to a solved-for account value, but in the context of ULMR, the solved-for account value considers maturity of the policy, while in the context of VM-20, the solved-for account value considers only maintaining the policy in force.

## Q 4.12: For fixed premium policies, if an interpolated terminal plus an unearned premium liability CRVM reserve is calculated instead of a mean reserve, would the actuary still need to calculate the Deferred Premium Asset?

A: Terminal Net Premium Reserves are computed as of the end of a policy year and not the reporting date, so the terminal reserve as of policy anniversaries immediately prior and subsequent to the reporting date are adjusted to reflect that portion of the net premium that is unearned at the reporting date. This is generally accomplished using either the mean reserve method or the mid-terminal method. Other appropriate methods, including an exact reserve valuation, are also commonly used (see SSAP 51). Whatever valuation reserve method is used, actuaries typically confirm that all three components (Deterministic Reserve, Stochastic Reserve, and Net Premium Reserve as adjusted for the reporting date) are internally consistent with respect to the assumption of premiums in the reserve. Consistency may be achieved by using the mean reserve method,
the mid-terminal method, or the exact reserve method with appropriate adjustments to the terminal Net Premium Reserve amount as summarized below.

- Mean Reserve Method: Net Premium Reserve (using annual premium assumption) less deferred premium asset.
- Mid-Terminal Reserve Method: Net Premium Reserve (using annual premium assumption) plus unearned premium reserve.
- Exact Reserve Method: Net Premium Reserve (using actual premium mode for the policy) with no adjustment needed.

Q 4.13: For flexible premium policies, would the actuary still need to calculate the Deferred Premium Asset?

A: For products with flexible premiums, some actuaries would not calculate a deferred premium asset or unearned premium liability because the methodology results in a reserve that is consistent with the valuation date.

## $Q$ 4.14: Is the deferred premium asset on a gross or valuation net premium basis?

A: With respect to adjusting entries such as the deferred premium asset, the Net Premium Reserve methodology is intended to behave similar to the pre-PBR formulaic Standard Valuation Law (SVL) methodologies. Some actuaries, therefore, would determine the DPA on a net basis and make any other adjustments consistent with pre-PBR adjustments.

Q 4.15: How would the actuary calculate the deferred premium asset for fixed premium policies in the first year?

A: For term insurance-based policies, the adjusted gross premium in the first year is zero, so the valuation net premium and the deferred premium asset in the first year would also be zero, except possibly for riders attached thereto. For fixed premium universal life policies, the valuation net premium is a level percentage of the solved-for gross premium, so some policies may have a non-zero deferred premium asset.

$Q$ 4.16: Are there any requirements with respect to the timing of premiums and claims (i.e., curtate vs. continuous) in the Net Premium Reserve?

A: The requirements are written in terms of an annual premium and some actuaries would interpret this as beginning-of-year timing. With respect to claims, Section 3 of VM-20 states that the NPR shall reflect immediate payment of claims. Some actuaries would interpret this to mean the immediate payment of claims on deaths assumed to occur continuously.

## Q 4.17: How does the actuary apply the floors that are defined in Section 3.D?

A: For a term insurance policy, some actuaries would compare the terminal Net Premium Reserve amounts to terminal cash value amounts and take the larger of the two. Then they would use these values to interpolate between policy anniversaries and compare the result to the cost of insurance to the next paid to date.

Other actuaries calculate the interpolated Net Premium Reserve amount prior to comparing to the consistently interpolated cash value amount and the cost of insurance to the next paid to date..

For UL policies, the calculation is similar but uses the cost of insurance to the next processing date on which cost of insurance charges are deducted with respect to the policy, with the cost based on the policy's net amount at risk.

VM-20 states that the cost of insurance for this purpose shall be based on the policy year in which the valuation date falls, using the valuation mortality tables for the policy prescribed in VM-20 Section 3, i.e. not the UL policy's contractual cost of insurance or expense charges.

## Q 4.19: Are there specific lapse assumptions required in the NPR calculation for level premium term products?

A: Yes, section 3.C.3.b of VM-20 prescribes the required lapse assumptions that must be used in NPR amounts calculated according to Section 3.B.4.

Base lapse rates are $10 \%$ per year during any level premium period of less than 5 years and $6 \%$ per year during any level premium period of 5 years or more years, except as noted below.

- For return of premium type term policies, the lapse rates are $6 \%$ for the first half of the initial level premium period and $0 \%$ for the remainder of the initial level premium period. For example, the first $0 \%$ lapse rate would be at the end of year 11 for a 20 -year ROP and at the end of year 8 for a 15 -year ROP.
- Lapse rates are $10 \%$ per year during any premium paying period after an initial level premium period of less than 5 years.
- Lapse rates are $0 \%$ per year for any policy whose final premium has by then been payable.

Section 3.C.3.b.vi. Prescribes the lapse rate for the final year of a level premium period (i.e., shock lapse), applied after any benefits assumed payable in the final year, and prior to the payment of the increased premium rate. The shock lapse rates vary by the length of the level premium period before and after the increase, and the percent increase in the gross premium (including policy fee) per $\$ 1,000$ of death benefit (not face amount). The table of prescribed shock lapse rates is reproduced below.

| Length of Premium <br> Period Prior to <br> Increase | Length of Premium <br> Period after Increase | Percent Increase in <br> Gross Premium Per <br> $\$ 1,000$ | Lapse for the Final <br> Year of the Level <br> Premium Period <br> (Shock Lapse) |
| :---: | :---: | :---: | :---: |
| $1<\mathrm{PP} \leq 5$ | 1 | Any | $50 \%$ |
| $1<\mathrm{PP} \leq 5$ | $1<\mathrm{PP}$ | Any | $25 \%$ |
| $5<\mathrm{PP} \leq 10$ | 1 | $<400 \%$ | $70 \%$ |
| $5<\mathrm{PP} \leq 10$ | 1 | Over $400 \%$ | $80 \%$ |
| $5<\mathrm{PP} \leq 10$ | $1<\mathrm{PP} \leq 5$ | Any | $50 \%$ |
| $5<\mathrm{PP} \leq 10$ | $5<\mathrm{PP}$ | Any | $25 \%$ |
| $10<\mathrm{PP}$ | 1 | $<400 \%$ | $70 \%$ |
| $10<\mathrm{PP}$ | 1 | Over $400 \%$ | $80 \%$ |
| $10<\mathrm{PP}$ | $1<\mathrm{PP} \leq 5$ | Any | $70 \%$ |
| $10<\mathrm{PP}$ | $5<\mathrm{PP}$ | Any | $50 \%$ |
|  |  |  |  |
|  |  |  |  |

Q 4.20: How is the level premium period in the NPR calculation determined for term products with level premium rates and non-level premiums due to increasing/decreasing face amounts?

A: Some actuaries would define the level premium period as the amount of time where the premium rates remain level.

$Q$ 4.21: Are there specific lapse assumptions required in the NPR calculation for universal life policies with secondary guarantees?

A: Section 3.C.3.a specifies lapse rates are 0\% for NPR amounts calculated according to Section 3.B. 5 (i.e. without considering any secondary guarantee provisions).

Section 3.C.3.c specifies the formula for determining the level annual lapse rate used for NPR amounts calculated according to Section 3.B.6 (i.e. considering secondary guarantee provisions). Although the rate is level for the calculation of the NPR on the valuation date, the rate is not generally equal to what it was for the same policy on the previous valuation date.

Q 4.22: In the NPR calculation, do assumed lapses occur annually, monthly, or on premium due dates?

A: VM-20 does not provide any requirement as to the timing of assumed lapses. Some actuaries will assume lapses occur on a basis consistent with how their cash flow testing is performed. It is common for a monthly assumption as to lapses to be made in future projections for those actuarial systems that process monthly cash flows. Other actuaries assume average lapse rates during the year and process lapses on an annual basis.

Q 4.23: If the actuary expects policies to be limited pay, but they contractually allow for future premiums, what premium period is used for the reserve calculation?

A: For universal life policies, Sections 3.B.5 and 3.B.6 require the calculation of an annual premium for the period over which the premiums are permitted to be paid that would keep the policy in force over the entire period coverage is to be provided or under the provisions of the secondary guarantee that provides the greatest NPR as of the valuation date.

Q 4.24: How do the Net Premium Reserve interest rates compare to current SVL interest rates for term and universal life policies?

A: Per Section 3.C.2.a, the valuation interest rate for policies with NPR amounts calculated according to Section 3.B.5 is the same as the current SVL. For policies with NPR amounts calculated according to Section 3.B. 4 or 3.B.6, the valuation interest rate is the same as the current SVL increased by 1.5 percent, but limited to 125 percent of the current SVL rate. The final rate is rounded to the nearest one-quarter of one percent ( $1 / 4$ of 1 percent).

## Q 4.25: How is the NPR calculated on an IUL policy?

A: The NPR requirements in VM-20 Section 3 do not distinguish between indexed and non-indexed UL policies. Like UL, the NPR requirements differ depending on whether or not the IUL policy has a secondary guarantee as defined in VM-01.

If the IUL policy has a secondary guarantee as defined in VM-01, then the policy meets the definition of a ULSG policy that is subject to VM-20 sections 3.B.5 and 3.B.6, which together define the NPR methodology for ULSG policies whether indexed or not. When calculating the NPR on IUL policies, practice varies as to the guaranteed minimum credited rate used in the Section 3.B.5 part of the calculation. For example, some actuaries use the fixed account minimum credited rate, some may use the floor for indexed account crediting, others use methods consistent with CRVM such as the implied guarantee rate method from AG36.

If the IUL policy has a conditional guarantee that does not meet the definition of a secondary guarantee as defined in VM-01 or has no secondary guarantee at all, then it is subject to the requirements of VM-A and VM-C and per VM-C must follow AG36.

Q 4.26: What equity return rates are used in calculating Net Premium Reserve interest for separate account products?

A: VM-20 does not give clear direction on the assumption for separate account returns for NPR. Some actuaries assume that the equity return assumptions under the NPR method would be developed in a manner similar to how it is developed under the CRVM approach for variable life policies.

$Q$ 4.27: For universal life contracts with secondary guarantees, can different tables be used for the Net Premium Reserve main guarantee, Net Premium Reserve secondary guarantee, and cost of insurance (COI) floor?

The mortality standards for the main guarantee, secondary guarantee, and COI floor are provided in Section 3.C.1. It is expected that the same mortality standard will apply to these calculations, except possibly during the short period of transition to new tables. As an example, during the transition from 2001 CSO to 2017 CSO, a company may have flexibility in applying different tables until it must use 2017 CSO beginning Jan. $1,2020$.

Q 4.28: Are the assumptions in the NPR calculation (specifically interest and mortality) locked in by year of issue? Does a company's use of the three-year transition period matter in this regard?

A: With respect to valuation mortality, a Guidance Note in Section 3.C. 1 suggests that adoption of new valuation tables (e.g. new "CSO" tables) after the operative date of the Valuation Manual would apply to all business issued since the adoption of the Valuation Manual. This Guidance Note states "The details of how to implement any unlocking of mortality tables will need to be addressed in the future."

With respect to valuation interest, Section 3.C. 2 includes a Guidance Note at the beginning of the section that makes clear the valuation interest rate assigned to a policy at issue date is not unlocked at future valuation dates.

Q 4.29: If a product has anticipated mortality higher than the CSO valuation table, might the higher mortality be used for the NPR calculation?

A:

Yes. Section 3.C.1.f addresses NPR mortality for policies issued on a substandard basis. CSO mortality rates for such policies shall be increased in a manner commensurate with the substandard rating, subject to a cap that ensures mortality rates do not exceed 100\%. Alternatively, for groups of policies for which the NPR
dominates the DR and SR, the company may choose to reserve for the substandard extra mortality separately in Exhibit 5.

Section 3.C.1.g addresses situations where anticipated mortality experience may materially exceed the prescribed CSO mortality (e.g., conversion mortality, simplified issue mortality). In these situations, the company shall adjust the CSO mortality rates used in the NPR calculation in a manner commensurate with the anticipated mortality experience for the policy, subject to a cap that ensures mortality rates do not exceed $100 \%$. Such mortality adjustments should be consistent with mortality adjustments made for the Deterministic Exclusion Test (DET) Net Premium Test if applicable. The resulting NPR must not be lower than the NPR calculated without adjusted mortality.

Q 4.30: VM-20 Section 3.B.6.d talks about the funding ratio in terms of the components ASG $_{x+t}$ and FFSG $_{x+t}$. How are these components defined in the context of a shadow account product or in the context of a specified premium product?

A: Refer back to the definitions found in Sections 3.B.1 and 3.B. 2 in evaluating how to calculate ASG $_{x+t}$ and FFSG $_{\mathrm{x}+\mathrm{t}}$ components of the ULSG NPR 3.B. 6 reserve for these different secondary guarantee designs.

## 5. VM-20 Calculation Overview-Part B. Deterministic Reserve

Q 5.1: VM-20 allows two different methods for the calculation of the DR. What are the two methods, and how are they different?

A: The two methods allowed for the calculation of the DR are known as the Gross Premium Valuation (GPV) method described in Section 4.A, and the Direct Iteration Method (DIM) described in Section 4.B. In theory, both methods produce exactly the same DR amount. Both methods serve to assure adequacy by identifying theoretically equivalent levels of starting assets that support and mature policy obligations under prudent estimate assumptions and a moderately adverse economic scenario. The two methods can be summarized as follows:

- The GPV method identifies the level of starting assets by projecting liability cash flows, then discounting them at net asset earned rates (NAER) derived from an integrated asset-liability model, iterating as necessary until the discounted liability cash flows are within 2 percent of the starting assets.
- The DIM identifies the level of starting assets by projecting asset and liability cash flows to the end of the projection period, iterating as necessary until the starting assets are sufficient to fully liquidate all policy obligations, leaving zero assets at the end of the projection period.

The primary difference between the two methods is that the GPV method has the separate NAER derivation and discounting step, whereas the DIM makes direct use of asset cash flows already being produced by the asset-liability model to arrive at the same answer.

Calculating NAER (net investment earnings divided by invested assets) subject to VM-20 requirements can be complicated and may require modifications and/or approximations. Considerations include differences in the way invested assets are defined for NAER, the timing of investment income within each projection interval, and the treatment of non-cash items. Although theoretically equivalent, consideration should be
given to the cumulative impact of approximations over long periods, which can lead to differences between the two methods in practice.

## Q 5.2: How would actuaries approach the calculation of the Deterministic Reserve (DR) for each model segment as required by VM-20?

A: Unlike the NPR, which is a seriatim reserve based on specific formulas using prescribed assumptions, the DR is an aggregate reserve based on general cash flow projections using company-specific assumptions. As such, instead of prescribing the exact steps and formulas to calculate the DR, VM-20 Section 4 on the DR generally describes two methods actuaries may use to calculate the DR using cashflows projected from the company's integrated asset-liability models, i.e. the Gross Premium Valuation method and the Direct Iteration Method (see Q 5.1). Both methods have iterative elements to them. Unlike the NPR, the specific steps taken to calculate the DR are largely left to actuarial judgement. Some actuaries would begin either method with similar initial steps, followed by different steps depending on the method chosen, for example:

Initial steps:

a. Determine margins and prudent estimate assumptions for all risk factors as described in Section 9 of VM-20.

b. Determine the makeup of starting assets as described in Section 7.D of VM-20.

c. Select the level of starting assets. For the first iteration, some actuaries may use a simple estimate based on the current period's NPR or an approximate roll forward of last period's DR.

d. Run the integrated asset-liability cash flow model to project asset and liability cash flows under the prescribed economic scenario.

Gross Premium Valuation method:

e. Determine the path of net asset earned rates as described in Section 7.H of VM-20.

f. Calculate a gross premium reserve by discounting projected benefits and expenses less premiums using the path of net asset earned rates, as described in Section 4.A of VM-20.

g. Calculate DR as the gross premium reserve, less the positive or negative pretax interest maintenance reserve (PIMR) balance at the valuation date allocated to the model segment as described in Section 7.D. 7 of VM-20, plus the balance of separate account assets on the valuation date, and plus the policy loan balance at the valuation date if policy loans are modeled explicitly under Section 7.F.3.b of VM-20.

h. Iterate starting with step c. until the level of starting assets for all model segments combined is within the asset collar described in Section 7.D. 3 of VM-20, i.e. is greater than $98 \%$ of the modeled reserve and less than or equal to the greater of the NPR and $102 \%$ of the modeled reserve, where modeled reserve is defined in VM-01 as the DR on policies determined under sections 2.A.1.a, 2.A.2.a, and 2.A.3.b plus the greater of the DR and the SR on policies determined under sections 2.A.1.b, 2.A.2.b, and 2.A.3.c. Although VM-20 only requires the asset collar be satisfied once for all model segments combined, to ease implementation some actuaries choose to satisfy the asset collar for each model segment individually subject to verifying that this more restrictive implementation of the asset collar doesn't have a material impact on aggregate results. Alternatively, VM-20 allows a company to stop iterating before the asset collar is satisfied as long as the company documents and provides reasonable assurance in the PBR Actuarial Report that the modeled reserve is not materially understated as a result of having starting assets outside the collar.

Direct Iteration Method:

i. Iterate starting with step c. until the level of starting assets is sufficient to fully liquidate all policy obligations, as described in Section 4.B of VM-20.

j. Calculate DR as the level of starting assets less the positive or negative PIMR balance at the valuation date allocated to the model segment as described in Section 7.D.7 of VM-20.

k. If starting assets for all model segments combined fall outside the asset collar described in Section 7.D. 3 of VM-20, the actuary will need to document and provide reasonable assurance in the PBR Actuarial Report that the modeled reserve is not materially understated as a result of having starting assets outside the collar. Some actuaries include documentation based on step i. above showing the level of starting assets is sufficient to fully liquidate all policy obligations.

Some actuaries use modeling systems that automate the iterative nature of either method.

Some actuaries find they need to justify and perform additional steps if asset and liability cash flow models are not integrated.

## Q 5.3: Is Deterministic Reserve aggregation allowed across product types (Whole Life and term, for example.)?

A: Per Section 4.C, if a group of policies for which a Deterministic Reserve is calculated includes policies from more than one VM-20 Reserving Category, where VM-20 Reserving Category is defined, as in Section 2, to be Term Reserving Category, ULSG Reserving Category or All Other VM-20 Reserving Category, a Deterministic Reserve shall be determined for each subgroup of the group of policies consisting of only those policies from each individual VM-20 Reserving Category by following section 4.A and Section 4.B of VM20. The NAER used for discounting each such subgroup may be the NAER for the group of policies. If the sum of the Deterministic Reserves for these subgroups does not equal the total Deterministic Reserve calculated for the group of policies as a whole, the Deterministic Reserve for the group of policies shall be allocated to each such subgroup proportionally. See Question 3.12.

## $Q$ 5.4: What economic scenario assumptions are used to determine the Deterministic Reserve?

A: Per Section 7.G.1, the Deterministic Reserve assumes the U.S. Treasury interest rate curves for Scenario 12 from the set of prescribed scenarios used in the stochastic exclusion ratio test (defined in Section 6.A. 2 of VM-20). The total investment return paths for general account equity assets and separate account fund performance also use those investment returns for corresponding investment categories contained in Scenario 12 from the set of prescribed scenarios used in the stochastic exclusion ratio test defined in Section 6.A.2.

## Q 5.5: How does the actuary calculate the path of net asset earned rates?

A: Companies that use the Gross Premium Valuation method to calculate the Deterministic Reserve must discount projected cash flows using the path of Net Asset Earned Rates (NAER) as described in VM-20 Section 7.H:

Determine a path of projected portfolio NAER for each projection interval used in the model (monthly, quarterly, annual, etc.). The NAER for each projection interval is calculated in a manner that is consistent with the timing of cash flows and length of the projection interval of the related cash flow model.

The NAER for each projection interval will equal Net Investment Earnings divided by Invested Assets.

Net Investment Earnings include:

- Gross investment income (including any amortization of premium or accrual of discount) less prescribed default costs and less investment expenses
- Capital gains and losses
- Income from derivative asset programs

Invested Assets:

- Are determined in a manner that is consistent with the timing of cash flows within the cash flow model
- Include the annual statement value of derivative instruments or a reasonable approximation thereof

Thus, the NAER will depend on:

- Projected Net Investment Earnings from the portfolio of starting assets
- Projected Net Investment Earnings from reinvestment assets
- The pattern of projected net liability cash flows (premiums less benefits and expenses)
- The pattern of projected asset cash flows from starting assets and reinvestment assets

However, per Section 7.H.2.a, separate account income and assets and interest (investment) income on policy loans and the policy loan asset are not included in the NAER calculation.

VM-20 permits the use of approximations and simplified approaches to determine appropriate NAER if the approach used is consistent with the requirements of Section 2.G. Considerations include differences in the way invested assets are defined for NAER, the timing of investment income within each projection interval, and the treatment of non-cash items. See Q 5.1 for additional information regarding NAER within each of the two methods for calculating the DR.

$Q$ 5.6: What is the common practice when Net Asset Earned Rate is negative? (ex. General account assets for VUL products) Do we floor at zero?

A: When Net Asset Earned Rate is negative, the discount factor is usually computed the same way as when it is positive, adding the Net Asset Earned Rate to 1. Flooring the Net Asset Earned Rate at zero could result in an understatement of the reserve.

## Q 5.7: How will actuaries model assets in the deterministic and stochastic calculations?

A: See Section 11 of this practice note for questions and answers about modeling of assets and the starting asset amount.

## Q 5.8: How are separate account cash flows and balances reflected in the Deterministic Reserve?

A: VM-20 Section 4.A on the Gross Premium Valuation method says to include the balance of separate account assets on the valuation date when calculating the DR using the GPV method; that is:

o Actuarial present value of benefits, expenses, and related amounts

o Less actuarial present value of premiums and related amounts

o Less the applicable positive or negative PIMR balance at the valuation date
o Plus the balance of separate account assets on the valuation date

o Plus the applicable policy loan balance at the valuation date (if policy loans are explicitly modeled)

o Equals Deterministic Reserve (using GPV method)

VM-20 Section 4.A.4.b addresses separate account cash flows, stating that the present value of future net cash flows from the separate account to the general account is to be included in the actuarial present value of premiums and related amounts when calculating the DR using the GPV method.

VM-20 Section 4.B. 3 addresses separate account balances and changes in those balances when calculating the DR using the Direct Iteration Method, stating that the balance of separate account assets on the valuation date is modeled each period in compliance with the applicable changes to those asset balances as defined in VM20 Section 7.

Separate account cash flows include, but are not limited to, deposits of policyholder premiums to the separate account, transfers between fixed and variable investment options, transfers of separate account values to pay death or withdrawal benefits, and amounts charged to separate account values for cost of insurance, expense, or other similar amounts.

## Q 5.9: How is reinsurance incorporated into the Deterministic Reserve?

A: Section 8.C, titled "Reflection of Reinsurance Cash Flows in the Deterministic Reserve or Stochastic Reserve," outlines all the considerations for including reinsurance cash flows in the modeled reserves.

$Q$ 5.10: Is the decision to select the method to calculate the DR completely at the company's discretion, or do certain conditions have to be met?

A: No conditions need to be met when deciding which method to use to calculate the DR. The choice is made at the discretion of the company.

## $Q$ 5.11: Can the company move back and forth between the two methods in subsequent valuation dates?

A: There is no provision prohibiting the movement back and forth between methods in subsequent valuation dates. However, switching methods would likely result in additional model governance, auditing, and documentation considerations.

## Q 5.12: What are the primary advantages of the Direct Iteration Method (DIM) compared to the Gross Premium Valuation (GPV) method?

A: The primary advantage of the DIM is that it eliminates the need for a separate NAER derivation and discounting step. Calculating NAER can be complicated and may require modifications and/or approximations related to the timing of asset cash flows, policy loan cash flows, and the treatment of non-cash accrual items. Consideration should be given to the cumulative impact of approximations over long time periods.

Another advantage of the DIM is that it automatically provides proof of reserve adequacy, because starting assets by definition are adequate to fund all future cash flow obligations as evidenced by the ending asset value. Also, although solve routines can be programmed to automate the iterative aspects of both methods, many asset-liability models will already have routines to solve for the starting assets to fully liquidate all
policy obligations, leaving zero assets at the end of the projection period. Note that both methods may require modifications to the asset-liability model related to negative assets in order to converge.

## $Q$ 5.13: Are there any disadvantages of the Direct Iteration Method (DIM) compared to the Gross Premium Valuation (GPV) method?

A: The primary disadvantage of the DIM is that most actuaries are very comfortable with the concept and practice of discounting future cash flows. GPV calculations have been done for years for a variety of applications, including U.S. statutory regulations. Some actuaries are less familiar with the DIM of solving for starting assets that accumulate to zero over time. However, the DIM is not entirely new and has been used by actuaries in certain applications and regulatory frameworks (e.g., the Canadian Asset Liability Method (CALM)).

Some actuaries find the GPV method better suited for certain situations where the actuary is limited to a liability-only model and can justify a method for obtaining NAER from a separate asset only model (e.g., from the investments area).

## 6. VM-20 Calculation Overview—Part C. Stochastic Reserve

## Q 6.1: How is the Stochastic Reserve determined as required by VM-20?

A: Section 5 of VM-20 contains the requirements for determining the Stochastic Reserve (all section references below are to VM-20).

- Determine the number of VM-20 Reserving Categories for which the Stochastic Reserve is to be calculated. The definition of VM-20 Reserving Categories is found in VM-01 and includes: Term Reserving Category, ULSG Reserving Category, and All Other Reserving Category. It is important to note that Section 5.A specifies that the company shall determine the number and composition of policy subgroups for aggregation purposes in a manner consistent with how the company manages risk across the different product types. However, if an aggregation subgroup includes policies from more than one VM-20 Reserving Category, then the Stochastic Reserve for policies from each VM-20 Reserving Category must be calculated on a stand-alone basis by following the steps in Section 5.A through Section 5.F. With that in mind, for each VM-20 Reserving Category, the following steps apply.
- Determine margins and Prudent Estimate Assumptions for all Risk Factors as described in Section 9.
- Generate the stochastic economic scenarios as described in Section 7.G.2.
- Determine the number of stochastic economic scenarios to use in the calculation as described in Section 7.G.2.c, d, and e.
- For each VM-20 Reserving Category, calculate the Stochastic Reserve as follows:

o Project cash flows for each model segment under each economic scenario as described in Section 5.

o Determine the Scenario Reserve for each scenario as described in Section 5.B.3.

o Calculate the CTE amount by ranking the Scenario Reserves from lowest to highest and taking the average of the highest 30 percent (CTE 70) of these Scenario Reserves.

- Determine any additional amount needed to capture any material risk included in the scope of VM-20 but not already reflected in the CTE amount, per Section 5.E.
- Subtract the positive or negative PIMR balance allocated to the policies under Section 7.D.7.


## Q 6.2: How is the Scenario Reserve calculated?

A: Section 5.B describes how the Scenario Reserve is calculated. The Scenario Reserve may include more than one model segment. A model segment is defined in VM-01 and discussed in Section 7.A.1.b. It is a group of policies and associated assets that are modeled together. Model segments should be consistent with the company's asset segmentation plan, investment strategies, or approaches used to allocate investment income for statutory purposes. If a company is managing the risks of two or more products with significantly different risk profiles as part of an integrated risk management process, then the products may be combined into the same subgroup (an aggregation subgroup). The Guidance Note in Section 5.A states that aggregating policies into a common subgroup allows the cash flows arising from the policies for a given stochastic scenario to be netted against each other. Section 5.A also requires that if policies from more than one VM-20 Reserving Category are included in an aggregation subgroup, the Stochastic Reserve for each VM-20 Reserving Category shall also be determined, as described in Section 5.G. Section 5.G. requires that the Stochastic Reserve be calculated on a stand-alone basis for each VM-20 Reserving Category.

A Scenario Reserve is the negative of the present value of accumulated net cash flows at the beginning or end of the year when the present value of the accumulated deficiency is the most negative during the projection period. This method is often called the Greatest Present Value of Accumulated Deficiency (GPVAD). In this method, future sufficiencies beyond the minimum point are not taken into account in the calculation.

The reserve for each scenario is determined as follows:

- At the valuation date, and at the end of each projection year, calculate the negative of the projected statement value of assets (may be positive or negative) for all model segments. The negative of the projected statement value of assets is called the negative accumulated deficiency.
- Discount the negative accumulated deficiencies at the end of each projection year to the valuation date.
- Discount rate $=105 \%$ of 1-year Treasury rate.
- Sum the discounted negative accumulated deficiencies across all model segments.
- $\quad$ Scenario Reserve $=$ the largest of discounted values plus the starting asset amount.

Below is a simplified hypothetical numerical example showing the calculation of the Scenario Reserve across all model segments:

## Hypothetical Example for Scenario Reserve Calculation

Scenario \#: $\quad 123$ of 10,000

Product: 5 Year Term Insurance

Projection Period: 5 Years (assumption of 100\% lapse at end of year 5 )

Starting Assets: $\$ 1,000$

| Projection Year $(t)$ |  | 0 | 1 |  | 2 |  | 3 | 4 | 5 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [1] Statement Value of Assets | $\$$ | 1,000 | 500 | $\$$ | $(100)$ | $\$$ | (50) | $\$ \quad(105)$ | 500 |
| [2] Negative of the Statement Value of Assets $=-1 *$ [1] | $\$$ | $(1,000)$ | $\$ \quad(500)$ | $\$$ | 100 | $\$$ | 50 | 105 | $\$ \quad(500)$ |
| [3] One-Year Treasury Rate (beginning of year) |  |  | $0.200 \%$ |  | $1.000 \%$ |  | $3.000 \%$ | $3.000 \%$ | $2.000 \%$ |
| [4] 105\% of One-Year Treasury Rate = 1.05 x (3) |  |  | $0.210 \%$ |  | $1.050 \%$ |  | $3.150 \%$ | $3.150 \%$ | $2.100 \%$ |
| [5] Discount Factor $(t)=$ Discount Factor (t-1) / (1+[4]@t-1) |  | 1.000 | 0.998 |  | 0.988 |  | 0.957 | 0.928 | 0.909 |
| [6] Discounted Negative Accumulated Deficiencies = [2] x [5] | $\$$ | $(1,000)$ | $\$ \quad(499)$ | $\$$ | 99 | $\$$ | 48 | 97 | $\$ \quad(455)$ |
| [7] Greatest Present Value of Accumulated Deficiency (GPVAD) $=\operatorname{Max}([6])$ | $\$$ |  |  |  |  |  |  |  |  |
| [8] Scenario Reserve = Starting Assets + [7] | $\$$ | 1,099 |  |  |  |  |  |  |  |

$Q$ 6.3: Can Scenario Reserves be negative, and are such negatives be reflected in a CTE 70 calculation?

A: Section 5.B of VM-20 states that a scenario reserve equals starting assets plus the greatest present value of accumulated deficiencies (GPVAD) for the scenario. Because a scenario's GPVAD can be negative, the scenario reserve can also be negative if the level of starting assets is sufficiently small. Negative scenario reserves will only be reflected in a CTE 70 calculation to the extent more than 70 percent of the scenario reserves are negative.

## $Q$ 6.4: What is the appropriate level of aggregation when determining the Stochastic Reserve?

A: Section 5.G requires that, for a company that includes policies from two or more VM-20 Reserving Categories (as defined in VM-01) in an aggregation subgroup, the Stochastic Reserve for each such VM-20 Reserving Category must be determined on a stand-alone basis. Therefore, the highest level of aggregation allowed is at the VM-20 Reserving Category level.

Aggregation in Section 5.A refers to the number of aggregation subgroups of policies used to combine cash flows when calculating the Stochastic Reserve for the purpose of limiting / allowing the amount of risk diversification between policies within a VM-20 Reserving Category. Aggregating policies into an aggregation subgroup allows the cash flows arising from the policies for a given stochastic scenario to be netted against each other (i.e., allows risk offsets between policies to be recognized).

VM-20 allows the actuary to group policies into more than one aggregation subgroup. VM-20 requires that the level of aggregation must be consistent with how the company manages risks across the different product types and must reflect the likelihood of any change in risk offsets that could arise from shifts between product types. For example, if a company is managing the risks of two or more different term insurance periods as part of an integrated risk management process, then these forms may be combined into the same aggregation subgroup. The level of aggregation within a VM-20 Reserving Category is up to actuarial judgment, consistent with the risk practices of the company.

Q 6.5: Will term insurance products with different level premium periods be projected in an aggregated basis or separately in the Stochastic Reserve?

A: Some actuaries model all of the level term products in one model in aggregate because the products are managed together and are believed to have similar risks. Other actuaries combine some level premium periods but model others separately (e.g., 30-year level premium period) because they believe that the product risks are different. Also, some actuaries model each different level premium period separately because the risk for each level premium period is managed separately or they believe separate models are more appropriate.

## Q 6.6: Are the prudent estimate assumptions the same for the Stochastic Reserve as for the Deterministic Reserve?

A: Per Section 9.A.5, prudent estimate assumptions for the Stochastic Reserve must be consistent with the prudent estimate assumptions used for the Deterministic Reserves, modified as appropriate to reflect the effects of each scenario in the Stochastic Reserve. That is, there will be natural differences but not a lack of consistency for assumptions that are dependent (i.e., dynamically linked) on the economic scenario, such as lapse rates that move up or down with changes in interest rates.

## Q 6.7: How are the discount rates determined?

A: Per Section 7.H.4, the discount rates for the Stochastic Reserve are set equal to the path of one-year Treasury rates at the beginning of each projection year for the scenario, multiplied by 1.05. The Guidance Note in this section has additional information on why this discount rate was chosen and why it is different from the one used for the Deterministic Reserve.

Q 6.8: How does the actuary determine the amount (if any) to add to the cash flow model results to capture any material risk not otherwise reflected in the Stochastic Reserve per Section 5.E of VM-20?

A: VM-20 is not specific on how this adjustment will be determined. Some actuaries make an adjustment for material risks outside of the cash-flow model where it is known that their cash-flow models used for their Stochastic Reserve do not cover specific policy risks. For example, if there is a certain rider that would pay an additional benefit if some contingent event happened and that event is not being modeled, then the actuary might include an adjustment for the payment of this benefit as a topside adjustment to the final model output. Alternatively, some actuaries first build this adjustment outside of the stochastic calculation, but then include the adjustment within the cash-flow model so that it is reflected in the final CTE amount and the scenario reserves.

## 7. Stochastic Exclusion Test

## Q 7.1: What is the Stochastic Exclusion Test?

A: As described in Section 6.A of VM-20, the Stochastic Exclusion Test (SET) can be used to identify groups of policies that do not have material interest rate or asset return volatility risk. Such groups of policies would likely have minimal variation in financial outcomes over varying economic conditions. Companies may elect to use this test to exclude groups of policies from the calculation of the Stochastic Reserve.

## Q 7.2: What methods are available to pass the Stochastic Exclusion Test?

A: The actuary may use any of three approaches to pass the Stochastic Exclusion Test. One approach, the Stochastic Exclusion Ratio Test (SERT), as described in Section 6.A.2, is to run 16 specified scenarios that are used in a ratio to demonstrate minimal variation by economic scenario in the present value of cash flows. Alternatively, as described in Section 6.A.3, the actuary can demonstrate that the Stochastic Reserve would not increase the minimum reserve required for the group of policies. The third approach, which can be used only for policies that are not variable life or not universal life with secondary guarantees, is for a qualified actuary to certify and report that the policies are not subject to material interest rate risk or tail risk, or asset risk.

## Q 7.3: What products might be good candidates for the Stochastic Exclusion Test? What products may not be excluded? What products are only allowed to pass the test under specific testing methods?

A: Life insurance products where the main risks are not highly dependent on interest rate movements or equity performance, or where these types of risks can be shared or passed on to the policyholder, are strong candidates for the Stochastic Exclusion Test. Some actuaries use the Stochastic Exclusion Test for products such as term life insurance, which focus primarily on mortality risk, or for some variations of traditional permanent life insurance and accumulation-oriented universal life insurance where non-guaranteed elements help transfer the asset performance risk to the policyholder. Variable life or universal life insurance products that contain secondary guarantees may not use the certification method to pass the Stochastic Exclusion Test. These types of policies may only be excluded through the use of the Stochastic Exclusion Ratio Test under Section 6.A. 2 or the Stochastic Exclusion Demonstration Test under Section 6.A.3.

## Q 7.4: Can a group of policies with a clearly defined hedging program be excluded from calculating the

 Stochastic Reserve?A: Maybe. Section 6.A.1.b states that a company may not exclude a group of policies for which there is one or more clearly defined hedging strategies from the Stochastic Reserve requirements. However, if the clearly defined hedging strategy is solely associated with product features that are not material under section 7.B. 1 due to low utilization, then the group of policies may be eligible for the stochastic exclusion test.

## Q 7.5: Is it necessary to perform the Stochastic Exclusion Test on all blocks of life insurance?

A: No. Section 2.A states if a company elects to calculate Stochastic Reserves for one or more groups of policies, the Stochastic Exclusion Test is optional for those groups of policies. In other words, within a given VM-20 Reserving Category, the test may be performed for all groups of policies, for selected groups of policies, or for no groups of policies.

Q 7.6: How does a company determine whether a group of policies passes the Stochastic Exclusion Ratio Test?

A: The Stochastic Exclusion Ratio Test is one method to pass the Stochastic Exclusion Test, thereby excluding a group of policies from calculation of Stochastic Reserves. The company calculates a ratio that evaluates the sensitivity of the reserve to changes in the economic scenario.

The numerator of the ratio is equal to the difference between the largest Adjusted Deterministic Reserve calculated under any of the prescribed economic scenarios minus the Adjusted Deterministic Reserve
calculated under the baseline economic scenario. The method for creating the economic scenarios is found in Appendix 1.E of VM-20, and these can be produced using the prescribed Economic Scenario Generator. The Adjusted Deterministic Reserve is calculated following one of two possible methods defined in Section 6.A.2.b.

The first method is to calculate the Adjusted Deterministic Reserve similarly to the Deterministic Reserve in Section 4, but with adjustments specified in Section 6.A.2.b.

The second method is to calculate a gross premium reserve from the cash flows from the company's Asset Adequacy Analysis models. This gross premium reserve would use the experience assumptions of the company's cash flow analysis models except that:

- the interest rate and equity return assumptions used are specific to each of the 16 exclusion test scenarios; and
- the rates used to discount the cash flows follow the methodology defined in Section 7.H but use the company's cash flow testing assumptions for default costs and reinvestment earnings.

The denominator of the Stochastic Exclusion Ratio is the present value of benefits for the group of policies, as determined in the baseline economic scenario, with an adjustment to reflect reinsurance by subtracting out ceded benefits.

If the ratio of the numerator to the denominator is less than 6.0 percent, it implies that the reserve calculation is relatively insensitive to variation in economic scenarios, and the group of policies passes the Stochastic Exclusion Ratio Test.

## $Q$ 7.7: What are the differences between the Deterministic Reserve and the reserve in the numerator of the Stochastic Exclusion Ratio Test?

A: The reserve in the numerator of the Stochastic Exclusion Ratio is called the "Adjusted Deterministic Reserve.” The calculation of the Adjusted Deterministic Reserve uses assumptions that do not include margins.

Net asset earned rates used across the 16 scenarios in calculating the Adjusted Deterministic Reserves are specific to each scenario in order to discount cash flows, whereas the discounting assumption in the Deterministic Reserve would be based on one specified scenario (the Deterministic Scenario).

As in the calculation of the Deterministic Reserve, the Adjusted Deterministic Reserve still uses dynamic adjustments for experience assumptions that depend on the economic scenario.

## Q 7.8: What is the difference between the two methods of calculating an Adjusted Deterministic Reserve?

The Adjusted Deterministic Reserve method that follows Section 4.A uses liability assumptions equal to the anticipated experience assumptions defined in VM-20. These assumptions do not include margins, so the company does not need to add a provision for margins as required for the prudent estimate assumptions. However, the other requirements of VM-20 regarding the use of prescribed assumptions and development of anticipated experience assumptions must be met. For example, the prescribed asset spreads and defaults must be used.

On the other hand, the gross premium reserve approach uses assumptions that are used by the company in its asset adequacy analysis. The development of these assumptions does not need to follow the VM-20 requirements, but instead uses the same assumptions determined by the appointed actuary used for asset adequacy analysis. For example, the asset spread and default assumptions from the asset adequacy analysis may be used instead of the asset spreads and defaults prescribed by VM-20.

Another possible difference between the two approaches is that if the appointed actuary has added margins in the asset adequacy analysis assumptions, the gross premium reserve used in the SERT calculation includes a margin for conservatism. Whether a margin is included depends on the asset adequacy assumptions.

If both the SET and DET are passed, then if the Adjusted Deterministic Reserve method that follows Section 4.A is used for the SERT, the company will still need to follow the full guidance of VM-G. However, if both the SET and DET are passed, then if the gross premium reserve approach using assumptions that are used by the company in its asset adequacy analysis is used for the SERT, then the governance requirements of VM-G Section 2 and Section 3 for the board and senior management do not apply.

$Q$ 7.9: Can the actuary include mortality improvement beyond the valuation date when performing the Stochastic Exclusion Ratio Test?

A: No-per Section 6.A.2.b.v, mortality improvement past the projection start date is not allowed in the anticipated experience assumptions used in the Stochastic Exclusion Ratio Test.

Q 7.10: What amounts are included and excluded from the present value of benefits in the denominator of the Stochastic Exclusion Ratio?

A: The present value of the benefits used in the denominator of the Stochastic Exclusion Ratio specifically includes benefits such as death benefits, surrenders, withdrawal benefits, and policyholder dividends. These benefits are net of reinsurance benefits when the Stochastic Exclusion Ratio Test (SERT) is calculated on a net-of-reinsurance basis. Section 6.A.2.a.iii states that premium, ceded premium, expenses, reinsurance expense allowances, modified coinsurance reserve adjustments, and reinsurance experience refund cash flows may not be included in the calculation of the benefit amount.

## $Q$ 7.11: Is the SERT calculation net of reinsurance?

A: The calculation is net of reinsurance when applying the SERT for the purpose of calculating the Stochastic Reserve component of the minimum reserve. The calculation excludes reinsurance when applying the SERT for the purpose of calculating the Stochastic Reserve component for the pre-reinsurance reserve required by Section 8.D.2.

Q 7.12: Does the company need to pass the Stochastic Exclusion Ratio Test on a pre-reinsurance basis in order to exclude policies from the pre-reinsurance Stochastic Reserve calculation, even if the policies have passed the ratio test on a post-reinsurance basis?

A: Yes. Section 8.D. 2 states that the ratio test must be passed on a pre-reinsurance basis in order to exclude the policies in the pre-reinsurance Stochastic Reserve calculation, even if the policies pass the ratio test on the post-reinsurance basis.
$Q$ 7.13: What happens when the policies pass the ratio test on a pre-reinsurance basis, but not the postreinsurance basis (or vice versa)?

A: If policies pass the ratio test on a pre-reinsurance basis, but not on a post-reinsurance basis, then the postreinsurance Stochastic Reserve will need to be calculated, while the pre-reinsurance Stochastic Reserve will not need to be calculated. Similarly, if policies pass the ratio test on a post-reinsurance basis, but not on a prereinsurance basis, then the pre-reinsurance Stochastic Reserve will need to be calculated, while the postreinsurance Stochastic Reserve will not need to be calculated.

$Q$ 7.14: If a block of business fails the SERT post-YRT reinsurance, but passes it pre-YRT reinsurance, is there a demonstration that will satisfy the test and allow the use of the exclusion?

A: Section 6.A.2.c allows for a group of policies to still pass the SERT if the company can demonstrate that the sensitivity of the adjusted Deterministic Reserve to economic scenarios is comparable between pre-YRT and post-YRT reinsurance. One such example of a demonstration as given in Section 6.A.2.c.i is to calculate the Largest Percent Increase in Reserve (LPIR), both pre- and post-YRT reinsurance.

Given the SERT is the ratio (b-a)/c as defined in Section 6.A.2.a, the LPIR is defined as (b-a)/a. Letting the subscript "gy" denote "gross of YRT" and "ny" denote "net of YRT," if SERT $\mathrm{gex} \times \mathrm{LPIR}_{\mathrm{ny}} / \mathrm{LPIR}_{\mathrm{gy}}<0.06$, then the block of policies passes the Stochastic Exclusion Ratio Test.

## $Q$ 7.15: How is YRT reinsurance addressed in the Stochastic Exclusion Ratio Test?

A: For the pre-reinsurance Stochastic Reserve calculation (which is required by Section 8.D.2), the impact of YRT reinsurance is ignored when performing the SERT. For the minimum reserve calculation (i.e., the postreinsurance reserve), the total YRT reinsurance cash flows should be included in the numerator, and the denominator should reflect the YRT reinsurance benefit cash flows. The latter includes claim settlements and dividends, but not reinsurance expense allowances, mod-co reserve adjustments, and experience refunds (per Section 6.A.2.a.iii).

## Q 7.16: Is coinsurance treated differently from YRT reinsurance when performing the SERT?

A: No. The applicable reinsurance cash flows for each reinsurance agreement are to be reflected in both the numerator and denominator of the SERT regardless of the type of reinsurance agreement (YRT, coinsurance, stop-loss, etc.).

Q 7.17: How does the company create the 16 economic scenarios used for the Stochastic Exclusion Ratio Test?

A: The methodology for creating the 16 economic scenarios is defined in Appendix 1 of VM-20.

$Q$ 7.18: Are there other requirements for the actuary to understand when determining the minimum reserve requirement for a group of policies passing the Stochastic Exclusion Test?

A: If a group of policies passes the Stochastic Exclusion Test, then Stochastic Reserve calculations are not required in determining the minimum reserve.

If the Stochastic Exclusion Test is relied upon to avoid calculating the Stochastic Reserve, then, according to Section 4.A.5, future transactions associated with non-hedging derivative programs may not be included in
calculating the Deterministic Reserve. If the Stochastic Exclusion Ratio Test is used to pass the Stochastic Exclusion Test, the demonstration must be done annually and within 12 months before the valuation date.

Some actuaries calculate the Stochastic Reserve and use it in the determination of the minimum reserve even if the block of business passes the Stochastic Exclusion Test.

## Q 7.19: What happens if a group of policies fails the Stochastic Exclusion Test?

A: If a group of policies fails the test, both the Stochastic Reserve and Deterministic Reserve must be calculated for that group of policies. Section 2.A specifies the definition of the minimum reserve in this situation.

Q 7.20: How does a company demonstrate that a group of policies passes the Stochastic Exclusion Test because it is not subject to material risks? What methods are acceptable? What information is needed? What demonstrations and reports need to be prepared?

A: Section 6.A. 3 outlines several methods that may be used to demonstrate that the group of policies is not subject to material risk.

- The company may opt to show that the greater of A and B is greater than the Stochastic Reserve, where:

o A equals the Deterministic Reserve, and

o B equals the Net Premium Reserve less any associated due and deferred premium asset.

- The company may show that the greater of A and B is greater than a Scenario Reserve in each of a sufficient number of adverse deterministic scenarios.
- The company may show that the greater of A and B is greater than the Stochastic Reserve calculated on a stand-alone basis, but using a smaller representative subset of the policies in the stochastic calculation, rather than the entire group of policies.
- The company may show that the main risk characteristics that would drive the Stochastic Reserve to exceed the larger of $A$ and $B$ have been substantially mitigated through various company actions. These actions may include hedging, risk reducing investment strategies, reinsurance, or transferring of the risk to the policyholder through contractual provisions.

The company may also use another method that is acceptable to the commissioner.

If any of these methods are used, the company must provide a demonstration in the PBR Actuarial Report. The demonstration must provide reasonable assurance that if the Stochastic Reserve were calculated, the minimum reserve would not increase.

The report must be prepared in the first year that the demonstration is performed, and at least once every three years thereafter.

$Q$ 7.21: How would a qualified actuary certify that a group of policies may be excluded from the Stochastic Reserve calculation?

A: Per the Guidance Note in Section 6.A.1.a.iii, "the qualified actuary should develop documentation to support the actuarial certification that presents the analysis clearly and in detail sufficient for another actuary to understand the analysis and reasons for the actuary's conclusion that the group of policies is not subject to material interest rate risk or asset return volatility risk. Examples of methods a qualified actuary could use to support the actuarial certification include, but are not limited to:

- A demonstration that Net Premium Reserves for the group of policies calculated according to Section 3 are at least as great as the assets required to support the group of policies using the company's cashflow testing model under each of the 16 scenarios identified in Section 6 or alternatively each of the New York seven scenarios.
- A demonstration that the group of policies passed the SERT within 36 months prior to the valuation date and the company has not had a material change in its interest rate risk.
- A qualitative risk assessment of the group of policies that concludes that the group of policies does not have material interest rate risk or asset return volatility. Such assessment would include an analysis of product guarantees, the company's NGE policy, assets backing the group of policies and the company's investment strategy."

$Q$ 7.22: What analysis would be done on a regular basis for groups of policies that satisfy the Stochastic Exclusion Test?

A: Some actuaries review the characteristics of each group of policies on a regular basis to make sure that the group of policies still passes the test, particularly if the block only passed the test by a small margin. Other actuaries identify certain economic parameters or other characteristics of the block of policies that drive variability to economic conditions and monitor those items to see whether the calculations need to be recomputed. An example of this may be a block of universal life policies without secondary guarantees, with cash values that are a very low percentage of the death benefit. It may be that this block is not currently sensitive to economic conditions, but the sensitivity of that block could increase to the point where it no longer passes the test if the cash values increase.

Other actuaries only perform the test when it is required under VM-20 if they believe the block has not changed enough to make retesting worthwhile.

## Q 7.23: If a group of policies becomes subject to material risks after having previously been certified, what transition does the company need to make in light of the Stochastic Exclusion Test?

A: In this situation, the company would need to re-evaluate whether the group of policies requires a calculation of the Stochastic Reserve. It may be that the group of policies still satisfies one of the other exclusion tests; if not, the exclusion needs to be discontinued. The company would then be required to calculate Stochastic Reserves in the determination of the minimum reserve.

## Q 7.24: Does the Stochastic Exclusion Test need to be performed with year-end valuation data?

A: According to Section 6.A.1.a.i, groups of policies pass the Stochastic Exclusion Test if annually and within 12 months before the valuation date the company demonstrates that the groups of policies pass the Stochastic Exclusion Ratio Test defined in Section 6.A.2. Therefore, year-end data does not need to be used.

## Q 7.25: If a base policy passes the Stochastic Exclusion Test, does an associated rider with a separate charge need to be tested separately for the Stochastic Exclusion Test?

A: The treatment of riders and supplemental benefits is described in Valuation Manual, Section II, Subsection 6. Section II, Subsection 6 outlines which riders shall be valued with the base policy, which riders may be valued with the base policy, and which riders shall be valued separately from the base policy. If the associated rider is required to be valued with the base policy or the associated rider may be valued with the base policy and the actuary has elected to do so, then the actuary may group together the base policy and associated rider when performing the Stochastic Exclusion Test. If the associated rider is required to be valued separately from the base policy or the associated rider may be valued separately from the base policy and the actuary has elected to do so, and the rider is valued under VM-20, then the actuary may test the rider separately for the Stochastic Exclusion Test in order to avoid needing to calculate Stochastic Reserves for the rider.

## 8. Deterministic Exclusion Test

## Q 8.1: What is the Deterministic Exclusion Test?

A: The Deterministic Exclusion Test (DET) is a test that a company may elect to perform in order to simplify its valuation process. For a group of policies or riders that fall within the term or ULSG VM-20 Reserving Categories, and does not meet the definition of "non-material secondary guarantee" (definition within VM01), the Deterministic Exclusion Test is not available. Otherwise, if a group of policies passes both the Stochastic Exclusion Test and the Deterministic Exclusion Test, then Section 2.A.3 specifies that the minimum reserve would be the sum of the policy minimum NPRs for those policies. In other words, the Deterministic Reserve does not need to be calculated for those policies. However, if the group of policies fails the Stochastic Exclusion Test, then both the Deterministic Reserve and the Stochastic Reserve must be calculated.

In some instances, the Valuation Manual permits valuing term riders with base policies. In these cases, it may be possible that the term rider is eligible for the Deterministic Exclusion Test - refer to Q8.4 below and Q1.5 of this practice note for more details.

## Q 8.2: How would a group of policies pass the Deterministic Exclusion Test?

A: As described in Section 6.B, there are two methods to pass the Deterministic Exclusion Test, called the Deterministic Net Premium Test and the DET Certification Method.

- A group of policies passes the Deterministic Net Premium Test when the company demonstrates that the sum of valuation net premiums for all future years is less than or equal to the sum of the corresponding guaranteed gross premiums.
- A group of policies is eligible for the DET Certification method if it is a group of policies that have converted to conversion products other than term life, variable life, indexed life, and ULSG with a material secondary guarantee. In the first year and every three years thereafter the qualified actuary must certify that the total reserve for each of the policies (including either the NPR adjusted for excess conversion mortality or the NPR plus an additional reserve for excess reserve mortality) includes a prudent provision for the additional mortality associated with the conversion and the total reserve
reasonably exceeds the value of a Deterministic Reserve which otherwise would have been calculated. The Guidance Note in Section 5.B.2.b provides as an example that an actuary may hold a net single premium as an additional reserve for the converted policy to support the certification.

A company may elect to perform the Deterministic Exclusion Test for a group of policies only if the group has passed the Stochastic Exclusion Test, to determine whether it is required to calculate the Deterministic Reserve for that group of policies.

## $Q$ 8.3: Is it necessary to perform the Deterministic Exclusion Test on all blocks of life insurance?

A: No. Section 2.A states that the Deterministic Exclusion Test is optional. The test may be applied to all groups within the entire inforce life insurance business with the exceptions noted in Section 6.B.1.

## Q 8.4: Are there any types of products that cannot be excluded from calculating the Deterministic Reserve through the Deterministic Exclusion Test?

A: Section 6.B. 1 notes, six types of policy and rider groups are automatically deemed to not pass the Deterministic Exclusion Test.

- Universal life policies with a secondary guarantee that do not meet the definition of a non-material secondary guarantee (Section 6.B.1.a);
- Any base policies that have ULSG or other secondary riders, which are to be valued with the base policy and follow the reserve requirements for ULSG policies under VM-20 pursuant to paragraph C in the Riders and Supplement Benefits Requirements in Section II, if any such ULSG or other secondary guarantee riders do not meet the definition of a non-material secondary guarantee (Section 6.B.1.a);
- Groups of policies that are not excluded from the Stochastic Reserve calculation (Section 6.B.1.a);
- Term insurance policies subject to Section 3.A.1 (Section 6.B.1.b)
- Riders that are being valued with base policies covered under the first four bullets above, subject to the Riders and Supplement Benefits Requirements in Section II; and
- Term riders subject to paragraph E in the Riders and Supplemental Benefits Requirements in Section II (Section 6.B.1.b).

Deterministic Reserves must be calculated for these policies.

## Q 8.5: What limitations exist for grouping policies when using the Deterministic Exclusion Test?

A: Section 6.B. 3 states that different contract types may not be grouped together for a combined test if the contract types present significantly different risk profiles. Section 2.A also requires distinct VM-20 Reserving Categories for the calculation of the minimum reserve, which consist of "Term Reserving Category" (Section 2.A.1), "ULSG Reserving Category" (Section 2.A.2), and “All Other VM-20 Reserving Category" (Section 2.A.3).

Some actuaries use the same grouping for the Stochastic Exclusion Ratio Test and the Deterministic Exclusion Test due to the similar requirements of Section 6.A.2.b.iv and 6.B.3. For example, a block of policies with high guaranteed gross premiums relative to their valuation net premiums may have less mortality risk than other blocks within the company. Some actuaries, therefore, do not combine this block with other contract types that have high mortality risk in order for the combined group collectively to pass the

Deterministic Exclusion Test. As noted in Q 8.4, some products are deemed to not pass the Deterministic Exclusion Test and would therefore not be grouped together with other products when performing this test.

Actuaries who expect to calculate both the Stochastic Exclusion Ratio Test and the Deterministic Exclusion Test might consider the grouping requirements for both tests when determining the appropriate grouping for modeling the policies.

## $Q$ 8.6: What valuation net premiums are used in the Deterministic Net Premium Test?

A: The valuation net premiums used in the Deterministic Net Premium Test are defined in Section 6.B.5 as follows:

For policies where the Net Premium Reserve is the minimum reserve required under VM-A and VM-C, then the valuation net premiums are determined according to those minimum reserve requirements.

The Deterministic Net Premium Test is not available for term life insurance.

For any group of policies for which the Deterministic Net Premium Test is being performed, if anticipated mortality is expected to be higher than the valuation mortality for the group of policies, then anticipated mortality must be used in the determination of the valuation net premium.

## Q 8.7: What gross premiums are used in the Deterministic Net Premium Test?

A: Per Section 6.B.5.e, guaranteed gross premiums used in the Deterministic Net Premium Test will generally be the guaranteed gross premiums specified in the contract, including applicable policy fees. For some universal life policies, there may not be a schedule of guaranteed gross premiums. If no guaranteed gross premiums are specified, VM-20 defines the gross premium to use as the level annual gross premium at issue that will keep the life insurance policy in force for the entire coverage period based on the policy guarantees.

## $Q$ 8.8: Is the comparison of valuation net premiums and guaranteed gross premiums done before (direct) or after reinsurance?

A: Per Section 6.B.2.a, the Deterministic Net Premium Test is performed on either a direct or assumed basis. This means it is performed before reinsurance ceded and including all assumed business.

## Q 8.9: What products might be good candidates for the Deterministic Exclusion Test?

A: Traditional products that have guaranteed gross premium levels in excess of valuation net premiums might serve as good candidates for the Deterministic Net Premium Test. These product types generally have gross premiums that provide sufficient revenues to cover the development of adverse mortality, expense, or investment income experience. Groups of converted policies (other than term life, variable life, indexed life, or ULSG with a material secondary guarantee) for which the company is already holding a prudent reserve can serve as good candidates for the DET Certification Method. However, the Deterministic Exclusion Test is not mandatory, and some actuaries calculate the Deterministic Reserve even for policies that likely would pass the test.

## Q 8.10: What are the implications of a group of policies passing the Deterministic Exclusion Test?

A: If a group of policies passes the Deterministic Exclusion Test, then Deterministic Reserve calculations are not required in determining the minimum reserve. Some actuaries still calculate the Deterministic Reserve, however, and use it in the determination of the minimum reserve.

## Q 8.11: How frequently is the Deterministic Exclusion Test performed?

A: For both the Deterministic Net Premium Test and the DET Certification Method, Section 6.B. 4 states that for a group of policies that is no longer adding new issues and the test has been passed for three consecutive years, the test is assumed to be passed each year as long as the test is computed once each five years going forward. For the DET Certification Method only, the certification is only required in the first year and every three years thereafter.

## $Q$ 8.12: What changes may occur that could cause a group of policies where no new business is being issued in that group to fail the Deterministic Exclusion Test after passing for several consecutive years?

A: Significant changes in the risk profile of a group of policies could cause a group of policies that had been passing to start failing the test. For example, for the Deterministic Net Premium Test, if poor experience emerges in the group over time that has sufficient credibility, then the actuary might change the future anticipated mortality assumption such that it may begin to approach or exceed the valuation mortality. In this case, the new, higher anticipated mortality will be used to determine valuation net premiums, and the resulting net premiums may be higher than the guaranteed gross premiums for the group. Additionally, the natural aging of a block could cause a group of policies that had previously passed the Deterministic Net Premium Test to fail the Deterministic Net Premium Test, since the test is prospective from each valuation date, comparing future valuation net premiums to future guaranteed gross premiums. For the DET Certification Method, deterioration in conversion experience might make it such that the actuary is no longer able to certify that the formulaic reserve being held includes a prudent provision for the additional mortality associated with conversion and reasonably exceeds the value of a Deterministic Reserve, which otherwise would have been calculated for this group of policies.

## 9. Difference From Cash Flow Testing-Scenario Reserve Calculation

## Q 9.1: May the actuary use an asset adequacy testing cash flow model to calculate the scenario reserve in the Stochastic Reserve calculation for VM-20?

A: Some actuaries will make use of their cash flow testing (CFT) models in calculating the scenario reserve. However, the actuary may need to adjust the CFT model to reflect the different purposes of the calculations. Some of the potential differences between CFT and VM-20 are listed below. Note that this list is not intended to be a complete listing of the differences.

- CFT models may have some approximations or model simplifications that are not appropriate for VM-20.
- VM-20 uses prudent estimate assumptions; CFT assumptions may include margins for adverse experience, but these may not be the margins required by VM-20.
- Some assumptions in VM-20 are prescribed and must be used in the calculation. CFT may have different prescribed assumptions, depending on state requirements.
- There may be some difference in projection periods / time step / model segments.
- Some business / model segments for which the scenario reserve needs to be determined may not be cash flow tested.
- The starting assets used in the model and reinvestment assumptions may be different.
- Cash flow testing models may include issue years that are not within the scope of VM-20.
- Treatment of IMR and AVR may be different.


## Q 9.2: May the actuary use the same assumptions for VM-20 as those used for cash flow testing?

A: VM-20 Section 9.A. 1 requires that prudent estimate assumptions must be used. VM-01 defines "prudent estimate assumption" as "a risk factor assumption developed by applying a margin to the anticipated experience assumptions for that factor." Some modifications to cash flow testing assumptions may be required if the cash flow testing assumptions are not prudent estimate assumptions. Also, some assumptions are fully or partially prescribed for the Stochastic Reserve calculation. Examples include lapse rates for certain universal life policies per Section 9.D.5 and asset reinvestment and default cost assumptions as described in Section 9.F.

## Q 9.3: In calculating the Stochastic Reserve, may the actuary use the same interest rate and equity scenarios as used for the CFT projections?

A: Section 7.G.2.a states that a prescribed economic scenario generator with prescribed parameters is required to be used to generate the interest rate and equity scenarios used in the determination of the Stochastic Reserve. Appendix 1 of VM-20 states that the prescribed economic scenario generator is available on the SOA website. Scenario reduction techniques are allowed to reduce the number of scenarios, but only if they do not materially reduce the reserve. In order to use a smaller set of scenarios for VM-20 calculations, the scenario picker tool within the economic scenario generator must be used to select that subset. CFT analysis does not require a prescribed generator and parameters.

## Q 9.4: Can the CFT projection period be used without modification for VM-20 calculations?

A: Section 7.A.1.d of VM-20 states that "The Company shall use a cash flow model that projects cash flows for a period that extends far enough in the future so that no obligations remain.” There is also a Guidance Note in this section that states "For example, it may be reasonable to assume $100 \%$ deaths or $100 \%$ surrenders after some appropriate period of time.”

Actuaries wishing to use the same projection period in the VM-20 calculation as is used for CFT will have to make sure these conditions are satisfied.

## Q 9.5: Would the actuary generally use the same starting assets in both the VM-20 and CFT calculations?

A: Section 7.D requires the assignment of a set of starting assets satisfying certain criteria to each model segment. Some actuaries will assign the same assets for both calculations, but it is not a requirement. Because VM-20 applies to new issues only, some actuaries select a limited subset of assets that were purchased during
the time period when the sales occurred and that meet the criteria. Other actuaries use a pro-rata portion of the CFT assets for VM-20 if these assets meet the criteria.

## Q 9.6: Would the actuary generally use the same model aggregation in VM-20 as is used in the CFT calculations?

A: The minimum reserve requirements specified by Section 2 of VM-20 clearly state that policies subject to VM-20 requirements must be included in a specific VM-20 Reserving Category, where the VM-20 Reserving Categories are (1) term Reserving Category; (2) universal life with secondary guarantee Reserving Category; and (3) All Other VM-20 Reserving Category. Further, there is a requirement in Section 5.G that the Stochastic Reserve for each VM-20 Reserving Category be calculated on a stand-alone basis. This approach may or may not be consistent with the CFT calculations of the company. Some actuaries review carefully the CFT model structure before using that structure for VM-20 minimum reserve calculations.

## Q 9.7: How are IMR and AVR treated in Stochastic and Deterministic Reserve calculations?

A: Because VM-20 is on a pre-tax basis, the IMR in the Stochastic and Deterministic Reserve calculation is adjusted to a pre-tax basis. The VM-20 reserve methodology (for both DR and SR) recognizes that the pretax IMR (PIMR) is redundant under a PBR regime because the PIMR only impacts the timing of recognizing investment income over the lifetime of the investment. Hence, the approach to reflect the PIMR in the DR calculations is to forgo adjusting the NAER calculation by including the amortization of the PIMR and, instead, simply make a direct post-calculation reduction/increase to the modeled reserve in the amount of the positive/negative PIMR existing on the valuation date. With respect to the SR, the approach is to forgo adjusting the modeled statutory asset values at all projection durations for unamortized PIMR (arising from PIMR amounts existing at the start of a projection and amounts arising as a result of capital gains and losses occurring during a projection) and, again, simply make a direct post-calculation reduction/increase to the final CTE 70 reserve in the amount of the existing allocated positive/negative PIMR at the valuation date.

The AVR does not enter into the calculation of either the Stochastic Reserve or the Deterministic Reserve.

## Q 9.8: How are federal income taxes treated in VM-20 versus CFT?

A: VM-20 requires that federal income taxes be excluded from cash flows. Typically, federal income taxes would be reflected in CFT.

## Q 9.9: Are taxes other than federal income taxes ignored for the purpose of calculating reserves under VM-20? For example, does the actuary ignore premium taxes?

A: Section 7.B.1.e states that taxes (excluding federal income taxes and expenses paid to provide fraternal benefits in lieu of federal income taxes) should be included in the cash flows. Section 9.E contains more information on taxes and expenses, including that foreign income taxes are excluded (Section 9.E.1.g).

## 10. Considerations When Performing Reserve Calculations on Other Than the Valuation Date

## Q 10.1: What valuation date is required for the Stochastic and Deterministic Reserves?

A: Per Section 2.E of VM-20, the calculation of the Stochastic and Deterministic Reserves can be performed as of a date up to three months prior to the valuation date as long as an appropriate method is used to adjust the reserves to the valuation date.

Although the calculation may use prior data, some actuaries take into account relevant experience up to the valuation date in their determination of Anticipated Experience and Prudent Estimate Assumptions used in the calculations.

## Q 10.2: Does the Net Premium Reserve have to be calculated using data as of the valuation date?

A: The Net Premium Reserve is a seriatim reserve that is calculated for each policy in force on the valuation date. It is expected that actuaries would perform the Net Premium Reserve calculation as of the valuation date using current inforce data, if possible. VM-31 section 3.D.11.h.i requires a statement confirming that the NPR was calculated based on policies inforce as of the valuation date.

## $Q$ 10.3: How might an actuary "use an appropriate method to adjust" the Deterministic and Stochastic Reserves to the valuation date when it is calculated as of an earlier date?

A: VM-20 does not prescribe a method for this adjustment. Some actuaries use a model office as of the earlier date and make several adjustments to take into account changes to the valuation date. The adjustments could include taking into account lapses and new policies issued since the projection start date but prior to the valuation date through a pro-rata adjustment to the relevant policy information (e.g., face amount, account value) so the overall characteristics for the group of policies approximate those characteristics on the valuation date. Additionally, the actuary could review all prudent estimate assumptions in the model and make any adjustments necessary for information / experience from the projection start date to the valuation date. Adjustments to the assets may or may not be made depending on how materially the asset portfolio has changed. In particular, some actuaries would use the economic scenarios as of the valuation date if the economic conditions have changed materially.

Some actuaries apply a high-level adjustment to the overall reserve amount or to each of several portions of the reserve. The adjustment may be based on analysis of past trends in the reserve, including "roll-forward" analysis of the change in the reserve balance. Such analysis would typically isolate the main drivers of the reserve change and would enable the actuary to estimate short-term changes in the reserve after the projection start date based on correlation with those drivers. This could include using some characteristic of the group of policies in the calculation (e.g., face amount for a group of term insurance policies) and a ratio method to modify the Scenario Reserve for the stochastic calculation or the Deterministic Reserve for the group of policies actually in force on the valuation date. Other actuaries calculate the Stochastic and Deterministic Reserves on a small, representative sample of policies from the group of policies on the valuation date and compare this amount to the Stochastic and Deterministic Reserves for those policies as of the earlier projection start date. This information could be used in a number of ways to modify the calculations made using the earlier projection start date to the valuation date. Of course, the actuary would need to be prudent in determining the number of representative samples that are appropriate and which policies to use in this calculation.

The actuary will typically confirm that the approach used is appropriate for the group of policies being valued. If the policy characteristics or economic environment have changed materially, most actuaries would consider a projection start date prior to the valuation date to not be appropriate. Other actuaries would provide additional disclosures to explain why they felt a prior start date was appropriate.

## $Q$ 10.4: Should changes in economic conditions from the projection start date also be incorporated in the adjustment of the reserves?

A: Some actuaries performing the calculations would modify the reserve calculations to take into account the economic conditions as of the valuation date if the valuation date is different from the projection start date. This adjustment would take into consideration both the impact on the liability cash flows and the net asset earned rate.

For products whose liability cash flows are dependent on changes in the economic environment, such as current assumption universal life products, some actuaries would reflect the economic conditions on the valuation date (if there have been material changes) and adjust the liability cash flows accordingly. This may require a re-computation of the reserve amounts or could include high-level adjustments reflecting expected changes to the liability cash flows. Some actuaries would apply adjustments that were based on sample calculations or prior sensitivity testing.

For products whose future expected liability cash flows are not sensitive to changes in market conditions, it is expected that some actuaries would not make modifications to the liability calculation. It is likely that these actuaries would disclose their rationale in the documentation of the calculation. An example would be no or very low Cash Surrender Value term policies with fixed premiums. The liability cash flows would not be dependent on a change in the economic environment, so no adjustments would generally be made. Some actuaries might make adjustments in order to reflect the impact of changes in interest rates on discount rates.

Some actuaries believe that actuarial judgment should be used to determine whether adjustments to the reinvestment assumptions and the projected net asset earned rate used in the calculation are needed. Those actuaries would modify the asset projection based on updated economic conditions as of the valuation date if the changes would lead to materially different reserves.

It is anticipated that some actuaries would include a specific description and discussion of how the asset and liability cash flows were adjusted in the documentation supporting the calculation per the requirements in VM-31 Section 3.D.11.i.

## $Q$ 10.5: Will actuaries adjust the calculation for new business and lapses if company inforce data from prior to the valuation date is used?

A: If policy inforce data from a date prior to the valuation date is used, it is expected that some actuaries would make no adjustments to the models to recognize changes in the inforce data between the projection start date and the valuation date. If large volumes of new business have been issued, some actuaries would estimate the additional reserves from the new issues. It is also expected that some actuaries would have a lapse and new business assumption to reflect changes in the inforce data between the projection start date and the valuation date.

Some actuaries would analyze whether including policies no longer in force as of the valuation date in the Stochastic Reserve modeling would materially affect the reserves. If there were a material difference in actual to expected terminations, some actuaries would make modifications to the models to take into account the
changes. Some actuaries would include a specific description and discussion of how the inforce policies were modified to take into account changes up to the valuation date in the documentation supporting the calculation and why it was determined to be material or immaterial.

$Q$ 10.6: Does the calculation need to be adjusted for policyholder actions such as additional premium payments, taking or repayment of a policy loan, partial withdrawals, face amount adjustments, and other policy changes that have occurred since the projection start date but prior to the valuation date?

A: It is expected that some actuaries would not make adjustments to the reserve for policyholder actions between the projection start date and the valuation date. However, if there have been policyholder actions that would materially affect the minimum reserve, some actuaries would make modifications.

$Q$ 10.7: Are there other types of changes occurring between the projection start date and the valuation date that could lead to adjustments in the calculations?

A: In addition to those items addressed above, some actuaries would consider the impact of changes to the business's risk profile, such as:

- Significant changes in asset allocation or mix of assets (by quality, duration, or other characteristics);
- New, terminated, or recaptured reinsurance;
- Changes in counterparty risk;
- Changes in non-guaranteed elements; and
- Merger and acquisition activity.


## 11. Details on Starting Assets and Asset Modeling

## $Q$ 11.1: How are due premiums reflected in the starting assets?

A: The due premium asset associated with expected future due premium cash flows should not be included in the level of starting assets used when calculating the DR and SR. This is consistent with the following two VM-20 requirements. First, VM-20 requires that due premiums be included in the expected future cash flows when calculating the DR and SR. Second, the definition of the minimum reserve includes an adjustment to the aggregate Net Premium Reserve for any due and deferred premium held on account of those policies. See Q 3.3 for more detail.

Q 11.2: If the company passes the Stochastic Exclusion Test and Deterministic Exclusion Test, does the actuary still have to model assets?

A: Assets do not need to be modeled to determine the Net Premium Reserve. However, assets may still need to be modeled to perform the Stochastic Exclusion Test. Some actuaries performing the Stochastic Exclusion Test would conclude that they need to model assets, while others may find alternative methods per Section 6.A.1.a.iii to certify that they would pass this test if it were performed.

$Q$ 11.3: What is the level of starting assets required in the calculation of the Deterministic and Stochastic Reserve, and how does an actuary set an initial estimate of the starting assets?

A: Section 7.D. 1 states that the level of starting assets shall be selected based on an iterative process. An iteration may continue until the asset collar of Section 7.D.3 is satisfied. If the company stops an iteration and for all model segments combined, the value of starting assets - using asset valuation methods consistent with their annual statement values - is less than $98 \%$ of the final reserve or greater than the larger of zero, the NPR less the due and deferred premium asset, or $102 \%$ of the final reserve (where the final reserve is the final aggregate modeled reserve, whether stochastic or deterministic), the company must supply documentation in the PBR Actuarial Report that provides reasonable assurance that the aggregate modeled reserve is not materially understated as a result of the estimate of starting assets.

A typical initial estimate could be a) the estimated modeled reserve plus the associated PIMR on the projection start date, or b) the NPR for the same set of policies plus the due and deferred premium asset, or c) an amount between a) and b). For example, some actuaries will set the level of starting assets equal to their best estimate of what the modeled reserve will end up being on the valuation date based on historical reserve patterns and trends, and the impact of such things as new sales, new products, and new reinsurance agreements since the prior valuation date, or any other items that impact the expected reserve level.

Other actuaries target starting assets to be within $2 \%$ of the final aggregate modeled reserve but set starting assets to NPR if larger than the final aggregate modeled reserve. Some actuaries using the Direct Iteration Method for the Deterministic Reserve do an additional run with starting assets bumped up to the NPR, if larger than the final aggregate modeled reserve, as part of their documentation.

## $Q$ 11.4: How does the actuary meet the 98 percent to 102 percent corridor required in Section 7.D.3?

A: If the starting assets used in the initial reserve calculation fall outside the prescribed corridor, some actuaries perform iterative calculations for each model segment until the starting assets used meets the asset corridor requirements to ensure that additional recalculations are not required. Other actuaries evaluate the asset corridor across all model segments and make adjustments as necessary. However, VM-20 does not require either method to be used. Therefore, some actuaries choose other methods to demonstrate that the reserve is adequate if the starting asset level falls outside of the required corridor. These might be based on additional calculations that have been performed historically or showing that the reserve change is immaterial if the starting assets were changed. The latter might be used in particular if the reserve amount is quite small.

## $Q$ 11.5: How does the actuary choose which assets to include in the calculation?

A: Model segments are needed to determine the group of policies and associated assets that are modeled together to determine the path of net asset earned rates. Section 7.A.1.b states that model segments should be selected that are consistent with the company's asset segmentation plan, or the approach used to allocate investment income for statutory purposes. Further, Section 7.D. 4 outlines the required selection of assets for each model segment at the Projection Start Date should include:

- All Separate Account assets supporting the policies;
- Policy loans, if they are explicitly modeled per Section 7.F.3.b.
- Due, accrued, or unearned investment income;
- All derivative investments held at the projection start date that are part of a derivative program and can appropriately be allocated to the model segment; and
- General Account assets that result in the sum of all starting assets equal to the estimated value of the modeled reserves plus the PIMR balance on the projection start date.

Regarding the last bullet point above, some actuaries choose General Account assets that, for management purposes, are generally associated with policies modeled. For example, where asset segmentation is used, the starting assets are selected from the asset segment that supports the block of policies subject to PBR (i.e., the asset segment that is used to track investment strategies and allocation of investment income to the policies they support).

In other cases, the assets may not be clearly defined to support policies subject to VM-20 Sections 4 and 5, versus those that are not, and other approaches will be used. Section 7.D. 2 requires that for an asset portfolio that supports policies both subject and not subject to VM-20, an equitable method to apportion the total amount of starting assets shall be determined. Additionally, per Section 7.D.4.e., the assets shall generally be selected on a consistent basis from one reserve valuation to the next.

## $Q$ 11.6: If a company doesn't have enough real assets in a portfolio, and the Stochastic or Deterministic Reserve calculation requires more assets to get within the 2 percent collar, how is this handled? Can the actuary add more assets to the projection if they do not actually exist?

A: Some actuaries would proportionally increase the assets in the portfolio to equal the starting asset amount under the assumption that assets would be transferred into the portfolio with the same average characteristics of the existing portfolio if more assets are deemed to be required.

Other actuaries would identify specific assets in the surplus portfolio or in other portfolios (e.g., corporate) so there are enough assets for the projection.

$Q$ 11.7: To the extent that starting assets have unstable market values, what impact would this have on the projected cash flows?

A: Per Section 7.D.6, the projected value of starting assets shall be determined in a manner consistent with their values at the start of the projection. Assets are selected at the projection start date such that the aggregate annual statement value of the assets equals the estimated value of the modeled reserve plus the PIMR balance. Section 7.F.1.c also requires modeling the proceeds arising from modeled asset sales, and determining the portion representing realized capital gains and losses.

During any projection interval, Section 7.F.1.d requires the actuary to reflect any uncertainty in the timing and amounts of asset cash flows related to the paths of interest rates, equity returns or other economic values.

In considering this requirement, actuaries would not make any modification to prescribed asset assumptions or the modeled interest rates or equity returns because they are generated stochastically using a prescribed generator.

Some actuaries take into account market instability by making modifications to nonprescribed assumptions, where appropriate, using actuarial judgment.

## $Q$ 11.8: Is it possible for the General Account portion of starting assets to be negative?

A: Yes. The Guidance Note following Section 7.D.5 indicates that the General Account starting assets described in Section 7.D.4.e may be negative. The Guidance Note also states that for the General Account starting assets described in Section 7.D.4.e, negative assets or short-term borrowing can be used, resulting in a projected interest expense.

An example of this situation is when a substantial portion of policyholder funds are allocated to Separate Accounts and the modeled reserve is less than the Separate Account Value.

## $Q$ 11.9: How will the actuary choose assets to include in the model if there are more General Account assets associated with the modeled policies than are needed as starting assets?

A: Some actuaries would choose a pro-rata portion of a segmented portfolio or other grouping of assets. Some actuaries would follow how assets are assigned for determining credited rates. Some actuaries might choose specific assets based on modeling constraints. However, the same asset would not be included in the starting assets of different model segments where the total amount of such asset is more than what the company owns.

## $Q$ 11.10: What types of grouping of assets might be used in the projection?

A: Section 7.F.1.a states that grouping of assets is allowed if the company can demonstrate that grouping does not materially understate the minimum reserve that would have been obtained using a seriatim approach. Some assets may be similar enough in nature that some actuaries might reasonably expect their cash flows and valuations to react in similar fashions as economic conditions change and therefore would group them together for modeling purposes. For grouping of fixed-income investments, some actuaries might assess whether parameters such as credit quality, time to maturity, duration, and interest and principal patterns are similar before considering grouping of individual securities. Simplification of cash flow modeling, including asset modeling, is discussed in Section 7.A.2, which references Section 2.G. Other actuaries would still model assets on a seriatim basis.

## $Q$ 11.11: How are investment cash flows (returns and principal repayments) for general account fixedincome assets modeled?

A: VM-20 states that fixed-income assets include public bonds, convertible bonds, preferred stocks, private placements, asset-backed securities, commercial mortgage loans, residential mortgage loans, mortgagebacked securities, and collateralized mortgage obligations. (See Guidance Note after Section 7.F.1.c.)

Investment cash flows on fixed-income assets are modeled for each projection interval per Section 7.F. 1 as follows:

- Project the gross investment income and principal repayments for each asset (or grouping of assets).
- Subtract prescribed default costs from gross investment income.
- Subtract investment expenses, using prudent estimate assumptions, from gross investment income.
- Project the proceeds from asset sales, and determine the portion representing any realized capital gains and losses.
- Reflect any uncertainty in the timing and amounts of the asset cash flows (calls, puts, prepayments, extensions, etc.).
- Model the impact of the derivative asset programs (if any) associated with these assets.

For starting assets, gross investment income shall be modeled in accordance with the contractual provisions of each asset and in a manner that is consistent with each economic scenario. For reinvestment assets, gross investment income is determined by adding a prescribed spread (see Tables F through I on the Related Documents tab of the LATF page of the NAIC website [https://naic.org/cmte a latf.htm], updated on a
monthly basis for current spreads, and quarterly basis for long-term spreads) to the prescribed Treasury rate in each projection interval (where the prescribed Treasury rate comes from the economic scenario).

## $Q$ 11.12: How are investment cash flows for general account total return equity investments modeled, such

 as money market funds, diversified bond funds, real estate, U.S. or international equity, private equity, etc.?A: VM-20 states that equity assets are non-fixed-income investments having substantial volatility of return, such as common stocks and real estate investments.

Investment cash flows on equity assets are modeled per Section 7.F. 2 as follows:

- Determine the grouping for equity asset categories (called "proxy funds" in VM-20) that reflect the types of equity assets of the company (e.g., large-cap stocks, international stocks, owned real estate, etc.) as described in Section 7.I of VM-20. Each proxy fund is typically expressed as a linear combination of recognized market indices.
- Allocate specific equity assets to each asset category (i.e., each proxy fund).
- Project the future gross investment return, including realized and unrealized capital gains, for each proxy fund in a manner that is consistent with the prescribed general account equity returns from the economic scenario as described in Section 7.G.
- Model the timing of asset sales in a manner that is consistent with the investment policy of the company for that type of asset.
- Reflect investment expenses through a deduction to the gross investment return using prudent estimate assumptions.

This process involves actuarial judgment to determine the appropriate proxy funds and methodology to "map" the return from proxy funds to the prescribed general account equity returns from the prescribed economic scenario. See Q12.1 for details on the different returns produced by the prescribed generator.

Actuaries might wish to effect modeling of proxy funds in different ways. For example, some actuaries might perform a regression of past fund performance against past performance of market indices consistent with the scenario generator classifications, and develop a scenario set for each proxy fund that is consistent with an appropriate weight of such scenario returns derived from the regression. Alternatively, funds might be decomposed using regression techniques into funds corresponding to each of the indices, or some other way could be used. Whatever method is used, the actuary must be able to document that the projected returns for the proxy funds are not overly optimistic.

VM-20 provides a Guidance Note (after Section 7.G.2.b) to assist actuaries in performing this mapping process. The goal of mapping the proxy funds to the prescribed funds is to generate consistent scenarios, i.e., higher expected returns for higher risk, and lower expected returns for lower risk. Risk is often measured as standard deviation of log returns. One approach to establish consistent scenarios would set the model parameters to maintain a near-constant market price of risk. Another closely related method would assume some form of "mean-variance efficiency", i.e. to establish and adjust the parameters of the proxy fund such that it lies on or within a corridor of the efficiency frontier, which can be constructed by standard curve fitting or regression techniques. The underlying principle and treatment of proxy funds mapping is consistent between VM 20 and VM 21.

## $Q$ 11.13: How are investment returns on Separate Account assets modeled?

A: Per Section 7.F.5, investment cash flows on Separate Account assets are modeled as follows:

- Determine the number and type of Separate Account funds (called "proxy funds" in VM-20) that reflect the types of variable subaccounts in the Separate Account assets (e.g., large-cap stocks, international stocks, owned real estate, etc.) as described in Section 7.J. Each proxy fund is typically expressed as a linear combination of recognized market indices.
- Allocate specific variable subaccounts to each asset category (i.e., each proxy fund).
- Project the future total investment return, including realized and unrealized capital gains, for each proxy fund in a manner that is consistent with the prescribed return from the economic scenario as described in Section 7.G.

Thus, investment returns on Separate Account assets follow the same modeling process used to determine the investment returns on General Account equity investments described above. Similar to the process for General Account equity investments, actuarial judgment is used to determine the appropriate proxy fund and determine the methodology to "map" the return from proxy funds to the prescribed returns from the prescribed economic scenario. A Guidance Note after Section 7.G.2.b may assist actuaries in performing this mapping process.

Note that Separate Accounts may also include fixed-income funds, but the same mapping process is used.

## Q 11.14: How are policy loans modeled?

A: Section 7.F. 3 defines two different approaches to modeling policy loans, explicitly or by proxy:

- Explicit modeling. A direct approach is to treat policy loan activity as an aspect of policyholder behavior as described in Section 7.F.3.b. This approach models policy loan activity explicitly by modeling all future policy loan activity in each projection period (i.e., interest, principal repayments, new principal amounts, etc.) as liability cash flows in the Deterministic Reserve and Stochastic Reserve calculations. Thus, policy loan interest and loan principal repayments are excluded from the Net Asset Earned Rate (NAER) calculation. Policy loans at the policy level can then be handled based on each policy's situation based on policyholder behavior assumptions subject to the requirements of Section 9.D. Additional requirements for explicit modeling of policy loans, covered in Section 7.F of VM-20, are below:

o Section 7.F.3.b.i requires that policy loan activity is treated as an aspect of policyholder behavior.

o Section 7.F.3.b.ii requires loan balances are assigned to either exactly match each policy's loan utilization or reflect average utilization over a model segment or sub-segments.

o Section 7.F.3.b.iii requires that policy loan interest rates be modeled in a manner that is consistent with policy provisions and with the economic scenario. Interest paid in cash is treated as a policyholder cash flow (not as investment income cash inflow), but interest added to the loan balance is ignored. This is because the increased balance will require increased repayment in future periods.

o Section 7.F.3.b.iv requires policy loan principal repayments be modeled as a cash inflow, including those which occur automatically upon death or surrender.

o Section 7.F.3.b.v requires that additional policy loan principal be modeled as a negative policy loan cash flow.
o Section 7.F.3.b.vi requires any investment expenses allocated to policy loans be modeled with policy loan cash flows or insurance expense cash flows (not as an investment expense).

- Proxy. This approach substitutes assets that are a proxy for policy loans (e.g., a bond) in the starting asset amount, and then includes the investment income from the proxy assets in the NAER (used in the Deterministic Reserve calculation), and as an investment cash flow in the Stochastic Reserve calculation. If this approach is followed, Section 7.F.3.a.i requires the company to demonstrate that the resulting reserve is not less than what would be produced by modeling policy loan activity explicitly under the first approach.

Regardless of which approach is used, the policy loan activity must reflect the company's expected utilization of policy loans by policyholders and comply with the policyholder behavior requirements stated in Section 9.D.

Some actuaries will choose to follow the explicit modeling approach and thus not undertake the demonstration that is required under the proxy approach and to more directly satisfy the policyholder behavior requirement that may be difficult to replicate without modeling policy loan activity explicitly.

If the explicit modeling approach is selected, Section 4 and Section 7.F describe the approach to reflect policy loan activity in the modeled reserve calculation. The treatment of the various policy loan items can be summarized as follows:

1. If the Deterministic Reserve is calculated as the present value of cash flows (Section 4.A):

a. The initial policy loan balance is included in the Deterministic Reserve. Section 4.A defines the Deterministic Reserve as the actuarial present value of benefits and expenses, less the actuarial present value of premiums, less the PIMR balance, plus separate account assets, plus the policy loan balance at the valuation date, with appropriate reflection of any relevant due, accrued, or unearned policy loan interest present value of benefits. In effect, this is equivalent to adding the initial policy loan balance to the reserve that is determined by taking the present value of cash flows.

b. Section 4.A.4.c requires that future net policy loan cash flows are included the actuarial present value of premiums in the Deterministic Reserve calculation if policy loans are explicitly modeled.

c. The Guidance Note after 4.A.4.c states that future net policy loan cash flows include policy loan interest paid in cash, plus repayments of policy loan principal, including repayments occurring at death or surrender (note that the future benefits in Section 4.A.3.a. are before consideration of policy loans), less additional policy loan principal. These following items are modeled as future cash flows, either increasing or decreasing the amount of invested reinvestment assets and present value of future cash flows:

i. New additional loan principal amounts are treated as negative cash flows in future projection periods (Section 7.F.3.b.v).

ii. Loan principal repayments are treated as positive cash flows in future projection periods. Principal repayments from death claims and surrenders are included (Section 7.F.3.b.iv).

iii. Future policy loan interest (if paid in cash) is treated as a positive cash flow in future projection periods (Section 7.F.3.b.iii).

iv. Future policy loan interest that is assumed to be added to the loan balance is not treated as a cash flow (Section 7.F.3.b.iii).
d. Any investment expenses allocated to policy loans shall be modeled, either with loan cash flows or insurance expense cash flows (Section 7.F.3.b.vi).

2. If the Deterministic Reserve is calculated under the Direct Iteration Method, where the reserve equals the amount of starting assets that produces an ending accumulated asset amount of zero (Section 4.B.):

a. The initial policy loan balance on the valuation date is projected forward using the projected additional loan principal amounts, loan principal repayments, and future policy loan interest added to the loan balance.

b. The future policy loan cash flows are reflected in the projection of the amount of non-policy loan reinvestment assets.

3. Per Section 5.B.1, the projected assets used to calculate the Stochastic Reserve follow the same approach to project assets described in item 2 for calculating the Deterministic Reserve under the Direct Iteration Method above.

Under explicit modeling, the net impact of policy loan activity on the Deterministic Reserve will vary depending on the relationship between the policy loan interest rate and the emerging NAERs.

## Q 11.15: How are derivative programs modeled?

A: Section 7.K. 1 requires that the cash flow model reflect the appropriate costs and benefits of derivatives currently held for the Deterministic Reserve and the Stochastic Reserve.

The requirements for the modeling of future derivative program transactions, however, vary by the type of derivative program.

If the company has a clearly defined hedging strategy (CDHS), the model must reflect appropriate costs and benefits of future derivative transactions associated with its execution. Additionally, Section 6.A.1.b excludes any group of policies for which there is a CDHS from the stochastic exclusion tests, so a Stochastic Reserve must be calculated for these groups of policies.

- CDHS requirements are similar to Actuarial Guideline XLIII \& C3 Phase II. Some actuaries consider examples of CDHS associated with VM-20 products to include:

o Hedging for equity-indexed products

o Hedging variable life long-term guarantees

o Rebalancing portfolio using derivatives to meet ALM targets

The Guidance Note after Section 7.K. 1 clarifies that the modeled reserve requirements prohibit projection future hedging transactions other than those associated with a clearly defined hedging strategy CDHS. This prohibition was added to address concerns that reserves could be unduly reduced by including programs that may or may not actually be executed.

Section 7.K. 1 also requires that the model reflect appropriate costs and benefits of future derivative transactions associated with non-hedging derivative programs (e.g. replication, income generation) if they are part of the company's risk assessment and evaluation processes. The company may choose whether or not to reflect non-hedging programs that are not part of the regular risk assessment process.

For each derivative program that is modeled, the company shall reflect any established investment policies and procedures for that program, project expected program performance along each scenario, and recognize all benefits, residual risks, and associated frictional costs:

- Residual risks include basis, gap, price, parameter estimation, and variation in actuarial assumptions.
- Frictional costs include transaction costs, opportunity cost of margin requirements, and administrative costs.
- Also, an addition to the Stochastic Reserve is required to reflect material derivative risks not fully captured within the "CTE 70" cash flow model. Emerging actuarial practice would ideally produce sound approaches.

Reflection of a qualified CDHS in the model may either increase or decrease the reserve. Not reflecting a hedging program similar to a qualified CDHS can also increase or decrease the reserve relative to what would be held if the program qualified as a CDHS. The direction of such impact can vary with economic conditions. The Guidance Note in VM-20 encourages future consideration of a graded approach for recognizing the impact of non-qualifying hedging strategies.

Each derivative program must be classified as associated with assets or with liabilities for purposes of calculating reserves, especially the Deterministic Reserve:

- “Asset-associated derivatives” or “derivative asset programs” are included in the net asset earned rates.
- "Liability-associated derivatives" or "derivative liability programs" are included in the liability cash flows.

Some actuaries will conclude that if derivative cost and payoff generate relatively smooth increments to the net asset earned rate (more "bond-like"), it is a good candidate for asset treatment. Otherwise, liability treatment may be more appropriate.

## $Q$ 11.16: What investment strategies for modeling reinvestment assets are permitted?

A: Section 7.E. 1 provides the following requirements for modeling of reinvestment assets:

- The modeled investment strategy may incorporate a representation of the actual investment policy that ranges from relatively complex to relatively simple.
- The PBR Actuarial Report shall include documentation supporting the appropriateness of the representation relative to the actual investment policy. The final maturities and cash-flow structures of assets purchased in the model, such as the pattern of gross investment income and principal repayments on a fixed or floating rate interest basis, shall be determined by the company as part of the model representation.
- The combination of price and structure of for fixed income investments and derivative instruments associate with fixed income securities shall be based on the then-current U.S. Department of Treasury curve along the relevant scenario. The annual default cost and gross asset spread assumptions for reinvested assets should follow the requirements specified in Section 9.F. 6 and Sections 9.F.8.

Many actuaries find it advantageous to start the modeling of reinvestment assets by having a thorough discussion with the company's investment department or external investment advisors, if necessary, to
understand the company's actual investment strategy. If the investment strategy used for asset adequacy analysis is a reasonable representation of the company's actual investment strategy, the assumed investment strategy for AAA might also be a reasonable starting point.

Some actuaries will use a mix of asset types and final maturities that produce a desired pattern of gross investment income and principal repayments. Other actuaries will assume fixed or floating rate coupons, or zero coupons. Other actuaries will prefer to utilize a complex model representation for reinvestment assets, which might include, for example, illiquid or callable assets. Other actuaries will prefer a simple model representation, which may involve mapping of more complex assets to combinations of asset types, such as combinations of public non-callable corporate bonds, U.S. Treasuries, and cash.

Whatever the approach, Section 7.E.1.a requires that the actuarial report includes documentation supporting the appropriateness of the assumptions relative to actual investment policy.

Furthermore, the requirement in Section 7.E.1.g, which is covered in more detail in the following question, may also affect the modeled investment strategy. The modeled investment strategy may be altered to achieve compliance with the floor or reduce the need to calculate the modeled reserve twice to demonstrate compliance.

## Q 11.17: How are gross spreads determined for reinvestment assets?

A: Section 7.E.1.d states that the gross spreads on public non-callable corporate bonds purchased in the model subsequent to the valuation date are determined by a prescribed methodology. The methodology is based on current and historical spread levels relative to U.S. Treasuries and is consistent with the prescribed approach to determine default costs on existing assets. For these bonds:

- Gross spreads are determined based on actual current and historical market data, using the same tables used in the calculation of default costs.
- The prescribed gross spreads start at current average market spreads in effect at the valuation date (published by the NAIC from a market source on a monthly basis) and grade linearly in yearly steps to the long-term benchmark spreads (derived and published by the NAIC based on actual historical data from the same market source on a quarterly basis) by the start of projection year four.
- Prescribed default costs are then deducted explicitly for purchased assets, using the same approach to calculate default costs as for existing assets (but ignoring the maximum net spread adjustment factor).

For investments other than public, non-callable corporate bonds, gross spreads are not prescribed, but are to be consistent with and in reasonable relationship to the prescribed spreads for public, noncallable corporate bonds. As each bond or security is unique due to its contractual provisions (callability, prepayment priority, sinking fund etc.) and other features (ratings, public, liquidity etc.), there is no general rule of thumb for setting a spread for each individual bond or security.

Some actuaries consult with an investment professional (internal or external) to obtain a general framework on the current spreads and historical long-term average spreads. The actuary might select a sample of recently purchased assets, compute their option-adjusted spreads (OAS) and compare them with the current and long-term market observed spreads.

Section 9.F.2.b provides a definition of option adjusted spread. Actuaries might keep in mind that the OAS for bonds and securities other than non-callable bonds is based on arbitrage-free stochastic interest rate scenarios rather than the scenarios for PBR.

With respect to grading from the current spread to the ultimate long-term spread, Section 9.F. 8 prescribes a 4-year grading period for non-callable bonds. Some actuaries consider using the same or shorter grading periods for bonds and securities other than non-callable bonds.

Per Section 7.E.1.g., the methodology also incorporates a floor on the modeled reserve.

- The modeled reserve cannot be less than would be obtained by substituting an alternative investment strategy in which all fixed income reinvestment assets are public non-callable corporate bonds with a credit quality blend of $50 \%$ "A2/A" and $50 \%$ "Aa2/AA".
- The blend of 50 percent $\mathrm{A}$ and 50 percent $\mathrm{AA}$ is intended to represent an approximate equivalent of the industry average asset allocation. This is based in part on data incorporated in a NAIC Rating Agency Work Group report.

The VM-20 Actuarial Report requires that the actuary provide documentation demonstrating compliance with the minimum floor requirement. Some actuaries decide to run the reserve calculation twice, the first using spreads following the company's investment strategy, and a second calculation assuming a strategy following the 50/50 mix of A2/A and Aa2/AA bonds. However, if the model investment strategy does not involve callable assets, some actuaries will conclude that demonstration of compliance will not require running the reserve calculation twice. For example, an analysis of the weighted average net reinvestment spread on new purchases by projection year (gross spread minus prescribed default costs minus investment expenses) of the model investment strategy compared to the weighted average net reinvestment spreads by projection year of the alternative strategy may suffice.

Some actuaries will conclude that they need to adjust the assumed mix of asset types, asset credit quality, or the levels of nonprescribed spreads for other fixed-income investments to achieve compliance.

## Q 11.18: How are asset market values modeled when assets are sold?

The modeling of market value of assets being sold is to be consistent with the modeling of market value of assets being purchased.

Per Section 7.E.2, gross spread assumptions are needed to compute market values when modeling the sale of

starting assets as well as the purchase and sale of reinvestment assets. As there could be ask-bid spread, the spreads used in calculating the market value when assets are sold are to be consistent with, but not necessarily the same as, the spreads used for purchases, recognizing that specific starting assets may have different characteristics than the modeled reinvestment assets.

Some actuaries consider that gross spreads for starting assets might revert to long-term average spreads and be different from assumed gross spreads for reinvestment assets due to different characteristics.

## Q 11.19: What is the Pretax IMR (PIMR) and why is it used instead of the IMR?

A: The PIMR is the statutory interest maintenance reserve (IMR) adjusted to a pretax basis for each model segment. It is adjusted to a pretax basis because the minimum reserve calculation in VM-20 ignores the impact of income taxes. The PIMR is recognized as a reduction to the present value of cash flows in the Deterministic Reserve determination and as a reduction to the CTE 70 amount in the Stochastic Reserve determination.

## $Q$ 11.20: Are the assets backing the PIMR included in the starting assets?

A: The PIMR liability is described as a negative asset that equals the portion of the total company PIMR allocable to each model segment. The PIMR may be positive or negative. Section 7.D. 1 notes that the value of the starting assets on the projection start date equals the estimated value of the modeled reserve plus the PIMR balance on the projection start date. Thus, assets supporting PIMR are included as a part of the starting assets. Note that the Deterministic and Stochastic Reserves already deduct the PIMR balance allocated to the group of policies at the valuation date allocated to the group of policies, as defined in Section 4.A and Section 5.F.

Conditions for allocating PIMR balances to the policies being modeled are provided in Section 7.D.7. Some actuaries will use the same approach to allocate the PIMR that is used for cash flow testing. Simplified approaches are explicitly allowed if the impact of the PIMR on the minimum reserve is minimal.

## Q 11.21: How will the actuary model negative assets when they arise in the projections?

A:

When performing financial projections, cash outflows can exceed cash inflows. If the amount of net cash outflows is below certain corporate cash management threshold (e.g., $4 \%$ of reserves), the business could resolve the negative cashflow issue with short-term borrowing or other disinvestment strategies such as purchasing negative assets or selling existing assets. The Asset Adequacy Analysis Practice Note published by the American Academy of Actuaries has additional information about modeling disinvestment cash flows.

Negative assets may also be used to support the general account liability of separate account business at the beginning of the projection.

VM-20 Section 7.E requires the actuary to model a disinvestment strategy in accordance with the corporate disinvestment guideline. If short-term borrowing is involved, some actuaries assume the cost of borrowing to be no less than the average yield rate of re-investment assets in order to avoid an arbitrage free opportunity for the insurer.

If the assumed disinvestment strategy is "purchasing negative assets" and the negative assets are assumed to be borrowed from other lines of business or the corporate, the lender's investment strategy could be used as the guidance for the assumed negative assets portfolio.

As the line of business becomes the pseudo-issuer of the negative assets, asset risks (such as default risk and prepayment risk) of the negative assets are likely to be based on the insurer's risk profile rather than the issuers of re-investment assets.

- Default Risk - The default risk of a negative asset could be based on the credit rating of the insurer. If the insurer is a B-rated company, it would not borrow negative assets as if it is an A-rated company.
- Salvage Value - The assumed salvage value may be reduced.
- Prepayment Risk - Some actuaries use a different prepayment assumption for negative assets because the line may not have the ability to redeem the negative assets until maturity. Even when the line intends to redeem, the corporate internal transaction provisions may deny the line from redeeming the negative assets without the consent of the lender (i.e., other lines or surplus).

If the amount of negative assets is immaterial, modeling negative assets is a viable disinvestment strategy. However, if the projected cash outflows exceed cash inflows for an extended period, some actuaries would use other disinvestment strategies (e.g., selling existing assets) to satisfy the net cash outflows as the alternatives may be closer to the insurer's actual cash management practice.

## $Q$ 11.22: What approaches are acceptable to model asset disinvestments?

A: Section 7.E. 2 of VM-20 requires that negative cash flows be modeled in a manner that is consistent with the company's investment policy, and that reflects the company's borrowing cost, if applicable.

Spreads used in calculating the market value of assets sold are to be consistent with but not necessarily the same as the spreads used for purchases, recognizing that specific starting assets may have different characteristics than the modeled reinvestment assets. However, buying negative assets or other techniques for modeling disinvestment are not prohibited.

Some actuaries model negative cash flows by selling assets. Other actuaries model buying negative assets (i.e., borrow money) that reflects the company's borrowing cost.

## Q 11.23: What approach is used to model asset defaults?

A: As described in section 9.F.1, a three-step process is required to determine default costs for fixed-income assets with an NAIC designation or NAIC commercial mortgage designation (i.e., corporate bonds, preferred stocks, residential mortgage-backed securities (RMBS), commercial mortgage-backed securities (CMBS), and commercial mortgages). Total annual default cost factors are calculated by projection year for each asset, and are expressed as a percentage of the statement value each year. The default cost factors are the sum of three components:

- Baseline annual default cost factor. Cost factors are based on historical corporate default and recovery experience and include a margin for conservatism. Factor is a table "look-up" based on a "PBR credit rating" and weighted average life (WAL) of the asset.
- Spread related factor. Based on the corporate bond spread environment as of the valuation date. Adjustment can be positive or negative, and grades off over three years (subject to a floor and a cap).
- Maximum net spread adjustment factor. Portfolio-wide upward adjustments, graded off over three years, if the net spread of the portfolio exceeds the net spread of a "regulatory threshold" index bond.

A different prescribed methodology applies to fixed-income assets that lack an NAIC designation. This may include but is not limited to, some commercial mortgage loans, CMBS, RMBS, and residential mortgages
(whole loans). Section 9.F. 5 provides the requirements for default cost factors for such assets without an NAIC designation.

With respect to reinvestment of fixed income security assets, Section 9.F.6 provides guidance for their default determination process.

## $Q$ 11:24: What company inputs are needed to determine the prescribed asset default rates for assets with an NAIC designation?

A: Per Section 9.F.2, there are three items that need to be provided from company records:

- Investment expense assumption for each asset type.

o This is the company's anticipated experience assumptions (with no margin).

o Expressed as an annual percentage of statement value.

- Option adjusted spread (OAS) for each asset.

o Average spread over zero coupon Treasury bonds that equates a bond's market price as of the valuation date with its modeled cash flows across an arbitrage free set of stochastic interest rate scenarios.

o For floating rate bonds, the OAS equals the equivalent spread over Treasuries if the bonds were swapped to a fixed rate.

o VM-20 allows for market conventions and other approximations.

- Weighted Average Life (WAL).

o WAL equals the weighted average number of years until 100 percent of the outstanding principal is expected to be repaid (rounding to the term available in the WAL column).

o For bonds or preferred stocks that are perpetual or mature after 30 years, the WAL shall be 30 .

o VM-20 allows for market conventions and other approximations.

o WAL as commonly understood by investment professionals is the weighted average of the times of the principal repayments, weighted by the amount of principal repayment; it's the weighted average time until a dollar of principal is repaid.

## $Q$ 11.25: How is the PBR credit rating used to determine asset default rates?

A: Section 9.F. 3 summarizes the determination of PBR credit rating to calculate asset default rates. VM-20 uses a numeric rating system from 1 to 21 to determine the credit quality of each asset. Table $\mathrm{K}$, referenced in Appendix 2 in VM-20 and found on the Related Documents tab of the LATF page of the NAIC website (https://naic.org/cmte_a_latf.htm), converts the ratings of NAIC Approved Ratings Organizations (AROs), NAIC designations, and NAIC commercial mortgage designations to this numeric rating system. A rating of 21 applies for any ratings of lower quality than those shown in the table.

The 1-21 PBR credit rating system attempts to provide a more granular assessment of credit risk than has been used for establishing NAIC designations for risk-based capital (RBC) and asset valuation reserve (AVR) purposes. Unlike for RBC and AVR, the VM-20 reserve cash flow models start with the gross yield of each asset and make deductions for asset default costs. The portion of the yield represented by the purchase spread over Treasuries is often commensurate with the more granular rating assigned, such as A+ or A-. Thus, use of the PBR credit rating system may provide a better match of risk and return for an overall portfolio in the
calculation of VM-20 reserves. However, for assets that have an NAIC designation that does not rely directly on ARO ratings, a more granular assessment consistent with the designation approach is not currently available.

For an asset with an NAIC designation that is derived solely by reference to underlying ARO ratings without adjustment, the PBR credit rating is determined by taking the average of the numeric ratings corresponding to each available ARO rating, rounded to the nearest whole number. Corporate bonds are in this category.

For example, for a bond with an NAIC designation of 1 that is rated A+ by S\&P and A3 by Moody's, the PBR rating is 6 , determined as follows:

S\&P rating of $\mathrm{A}+\quad \rightarrow$ PBR numeric rating of 5 (from Table $\mathrm{K}$ )

Moody's rating of $\mathrm{A} 3 \rightarrow$ PBR numeric rating of 7 (from Table $\mathrm{K}$ )

PBR rating $=$ average of 5 and $7=6$

For a bond with an NAIC designation of 5 that is rated CCC by S\&P and Caa3 by Moody's, the PBR rating is 19, determined as follows:

$$
\begin{array}{ll}
\text { S\&P rating of CCC } & \rightarrow \text { PBR numeric rating of } 18 \text { (from Table K) } \\
\text { Moody's rating of Caa3 } & \rightarrow \text { PBR numeric rating of } 19 \text { (from Table K) } \\
\text { PBR rating = average of } 18 \text { and } 19=18.5=19 \text { (rounded) }
\end{array}
$$

For an asset with an NAIC designation that is not derived solely by reference to underlying ARO ratings without adjustment, the PBR credit rating is determined by taking the second least favorable numeric rating associated with the NAIC designation. Non-agency RMBS and traditional private placements fall into this category. For example, for a private placement designated NAIC 1, there are seven potential PBR ratings shown in Table K, 1 through 7. So the PBR rating is the second least favorable, that is, a PBR rating of 6.

For commercial mortgage assets with an NAIC commercial mortgage designation, Table $\mathrm{K}$ is used to look up the corresponding PBR credit rating.

Once the PBR credit rating is determined for each asset, the baseline default cost is a table "look-up" based on the PBR credit rating and the WAL of the asset.

## $Q$ 11.26: What is the purpose of the spread related factor, and how is it used to determine asset default rates?

A: The purpose is to incorporate in the default cost the impact of current market spreads (i.e., spreads over Treasuries) on the valuation date, based on the premise that a portion of the difference between the current spread and historical spreads represents near-term expected default experience (could be a positive or a negative adjustment). That is, abbreviate short term fluctuation of default spreads due to severe market conditions such as the financial crisis in 2008.

A floor and cap have been provided to assure that this component cannot reduce the total default cost factor in year one by more than the baseline default cost factor and cannot increase the total default cost factor in year one by more than two times the baseline default cost factor. The cap is intended to help limit reserve volatility, which remains a concern for both the spread related factor and the maximum net spread adjustment
factor. The spread related factor grades linearly from the prescribed amount in year one to zero in years four and after.

Per Section 9.F.1.b, the prescribed amount in year one may be positive or negative and is calculated as follows:

- Multiply $25 \%$ by the result of (a) minus (b), where:

(a) equals the current market benchmark spread published by the NAIC consistent with the PBR credit rating and WAL of the asset on the valuation date (see Tables F and G on the Related Documents tab of the LATF page of the NAIC website (https://naic.org/cmte_a_latf.htmwww.naic.org), updated by NAIC on a monthly basis).

(b) equals the most current available historical mean benchmark spread published by the NAIC consistent with the PBR credit rating and WAL of the asset on the valuation date (see Tables $\mathrm{H}$ and I on the Related Documents tab of the LATF page of the NAIC website (https://naic.org/cmte_a_latf.htmwww.naic.org), updated by NAIC on a quarterly basis)

- The resulting amount shall not be less than the negative of the baseline annual default cost in year one and shall not be greater than 2 times the baseline annual default cost in year one.


## $Q$ 11.27: What is the maximum net spread adjustment and how it is used to determine asset default rates?

A: The maximum net spread adjustment increases the required assumed default costs in the VM-20 calculations if the average credit quality of the company's asset portfolio falls below the targeted threshold. The targeted threshold is a Baa2/BBB Bond (NAIC 2, PBR credit rating of 9).

Per Section 9.F.1.c, for each model segment, a comparison is to be made of two spread amounts, both being net of the default costs calculated thus far and net of investment expenses. In each case, the gross option adjusted spread is based on current market prices at the valuation date.

- The first spread amount in the comparison represents the weighted average net spread of all the assets in the model segment, as if all the assets were purchased at their current market spreads.
- The second spread amount in the comparison represents the net spread for a portfolio of index Baa2/BBB bonds (NAIC 2, PBR credit rating of 9), as if the index Baa2/BBB portfolio were purchased at the current average market spread.

If the first result is higher than the second, additional default costs must be added to each asset until the two results are equal for the first projection year. This additional amount of default cost on each asset then grades off linearly in the model until it reaches zero in year four and after. This process is repeated each actual valuation date.

A company that invests in an asset mix earning an average gross spread greater than Baa2/BBB bonds initially, or an asset mix whose average market spread could widen significantly relative to market spreads for Baa2/BBB bonds, are examples of situations likely to trigger additional assumed default costs either initially or in the future.

The calculation is as follows:

The prescribed amount in year one shall be the excess, if any, of (a) over (b):

(a) Weighted average net spread for the asset portfolio, calculated as follows:

1. For each asset, calculate a preliminary year one net spread equal to the option adjusted spread of the asset on the valuation date less the sum of the amounts from Sections 9.F.1.a and 9.F.1.b (baseline and spread related factor) and less the investment expense for the asset.
2. Calculate a weighted average preliminary year one net spread for the total asset portfolio (i.e., assets subject to this section) using weights equal to each asset's statement value on the valuation date multiplied by the lesser of three years and the asset's WAL on the valuation date.

(b) The net spread for a "hypothetical asset," which is called the "regulatory threshold asset."

The regulatory threshold asset is determined as follows:

- Calculate the preliminary year one net spread for a hypothetical asset with the following assumed characteristics (the regulatory threshold asset):

o A PBR credit rating of 9 (equivalent to Baa2/BBB).

o A WAL equal to the average WAL on the valuation date for the assets in the portfolio.

o An option adjusted spread equal to the current market benchmark spread published by the NAIC for the assumed PBR credit rating and WAL (see Table F on the Related Documents tab of the LATF page of the NAIC website (www.naic.orghttps://naic.org/cmte_a_latf.htm), updated by NAIC on a monthly basis).

o Investment expense of 0.10 percent.

- The preliminary year one net spread is equal to the option adjusted spread of the hypothetical asset on the valuation date less the sum of the baseline and spread related factor for the hypothetical asset, and less the investment expense for the hypothetical asset.

$Q$ 11.28: What are the default rates required in the VM-20 calculation for commercial mortgages, CMBS and RMBS investments, and residential whole loans?

A: If the asset does not have an NAIC designation or an NAIC commercial mortgage designation, per Section 9.F.5, a prescribed default assumption is established such that the net yield shall be capped at 104 percent of the applicable historical U.S. Treasury yield rate most closely coinciding with the purchase date and maturity structure, plus 25 basis points. If the assets have an NAIC designation or an NAIC commercial mortgage designation, their default assumptions are determined according to Sections 9.F.3 and 9.F.4.

Section 9.F. 5 only provides the cap on the net yield, and many actuaries seek additional advice from internal or external investment professionals.

Q 11.29: If a company is using nontraditional assets (e.g., letters of credit, contingent notes, etc.) as part of a reserve financing arrangement, how are these nontraditional assets handled in the VM-20 calculation?

A:

VM-20 is silent on the use of non-traditional assets such as letter of credit or contingent notes. However, Actuarial Guideline XLVIII section 4.F(2) limits the use of any synthetic letter of credit, contingent note, credit-linked noted or other similar securities as forms of Primary Securities to support actuarial reserves determined using the Actuarial Method.

Section 5 of Actuarial Guideline XLVIII provides additional guidance on the definition of the Actuarial Method and its relationship with Net Premium Reserve, Deterministic Reserve and Stochastic Reserve. Thus, some actuaries use Section 4.F(2) of Actuarial Guideline XLVIII as the guidance for non-traditional assets.

Some actuaries who intend to use these non-traditional assets as a part of the starting assets for VM-20 valuation choose to obtain approval from the domiciliary regulator in advance.

## 12. Details on Scenarios / Scenario Generators / Economic Assumptions

## $Q$ 12.1: What economic assumptions are stochastically generated?

A: The prescribed economic scenario generator produces the following economic parameters:

- Treasury rates at maturities of $0.25,0.50,1,2,3,5,7,10,20$, and 30 years. (Filename: UST)
- The following equity return indices, with file names shown in parentheses

o Aggressive or specialized equity (AGGR)

o Diversified international equity (INT)

o Diversified large-cap U.S. equity (US)

o Intermediate-risk equity (SMALL)

o Money market / Short term (MONEY)

o Intermediate-term U.S. government bond (INTGOV)

o U.S. long-term corporate bonds (LTCORP)

o Diversified fixed income (FIXED)

o Diversified balanced (BALANCED)

Treasury rates may be generated either as bond equivalent rates or annual effective rates.

Equity return indices are total returns, with one row for each scenario and one column for each time period.

Actuaries may or may not choose to generate other measures stochastically, including inflation rates, or currency exchange rates, or dividend and volatility rates for the equity return indices. Consideration should be given to the internal consistency of other stochastic quantities with the scenario data.

## $Q$ 12.2: How would actuaries generate the scenarios for the VM-20 calculations?

A: VM-20 prescribes an economic scenario generator (ESG) to generate scenarios for VM-20 calculations. For the purposes of calculating the Stochastic Reserve, Section 7.G. 2 requires the actuary to use (i) U.S. Treasury interest rate curves following the prescribed economic scenario generator with prescribed parameters, as described in Appendix 1; and (ii) total investment return paths for general account equity assets and separate account fund performance generated from a prescribed economic generator with prescribed
parameters, as described in Appendix 1. In Appendix 1, the link to the prescribed economic scenario generator website is provided: https://www.soa.org/tables-calcs-tools/research-scenario/.

Similarly, Sections 7.G. 1 and 6.A. 2 prescribe the same ESG to generate the scenario used to calculate the Deterministic Reserve, and the scenarios used to perform the Stochastic Exclusion Ratio Test, respectively.

This website also contains relevant documentation on the scenario generator, including how to select the appropriate options on the main Scenario Generator tab to produce the scenarios in the desired format, and how to maintain the Historical Curves tab by entering the last daily yield curve for each month using data available from the U.S. Treasury, found at: https://www.treasury.gov/resource-center/data-chartcenter/interest-rates/Pages/TextView.aspx?data=yield.

The prescribed ESG is updated periodically, and users typically verify that they have the current version of the ESG prior to use. In recent years, an updated ESG has been released each year. Release notes provided with each update document any changes to the ESG. After an update to the ESG, some actuaries generate scenarios using the prior and updated ESG to assess the impact of any changes.

## $Q$ 12.3: How many scenarios are run to determine the Stochastic Reserve?

A: The current version of VM-20 does not define the appropriate number of scenarios to run. The prescribed scenario generator allows the user to choose the "full set of 10,000 scenarios," as well as representative scenario subsets of 1,000, 500, 200, and 50 scenarios. From this, some actuaries would run all 10,000 scenarios to meet the regulatory requirements under VM-20, while some actuaries would use fewer than the 10,000 scenarios. See Q 12.4 for additional details.

## $Q$ 12.4: How would the actuary determine the appropriate number of scenarios if less than the full 10,000 scenario set is used?

## A:

There are many reasons an actuary chooses to use fewer scenarios than the full 10,000 scenario set, including managing model run time or reducing the complexity of sensitivity tests.

Section 7.G.2.c indicates that the use of fewer scenarios rather than a higher number of scenarios is permissible as a model efficiency technique provided scenario that:

- The smaller set of scenarios is generated using the scenario picker tool provided within the prescribed scenario generator; and
- The use of the technique is consistent with Section 2.G.

Section 2.G states that a company may use simplifications, approximations and modeling efficiency techniques provided that:

- The company can demonstrate that the use of such techniques does not understate the reserve by a material amount, and
- The expected value of the reserve calculated using simplifications, approximations, and modeling efficiency techniques is not less than the expected value of the reserve calculated that does not use them.

The scenario picker tool relies solely on the 20-year Treasury rate for scenario selection. Thus, for products that are sensitive to equity performance or other maturities, the scenario picker may not be an effective scenario reduction technique, and testing will be required to demonstrate compliance with the requirements of Section 2.G. Further information on the methods used in the scenario picker tool can be found in the frequently asked questions (FAQ) document provided with each update of the ESG.

VM-20 Section 7.G.2.e also requires the company to perform a periodic analysis of the impact of using a different number of scenarios on the Stochastic Reserve, noting the difference in results as the number of scenarios is increased. An appropriate subset of the inforce block can be used for this analysis.

VM-20 does not specify how to demonstrate compliance with Section 2.G or how to perform the periodic analysis of different numbers of scenarios. Some actuaries might follow a process similar to the following:

1. Select a subset of the scenarios.
2. Select a representative subset of the liabilities.
3. Calculate reserves across the subset of scenarios using the tentatively selected subset of the liabilities and also using the entire inforce business population. If these results are similar, then the actuary might reasonably conclude that the subset of the liabilities (i.e., the smaller or representative model) is appropriate to use to measure the appropriateness of a scenario subset. If reserves are materially smaller using the subset of liabilities, repeat steps 2 and 3 using a different or larger subset of liabilities.
4. Finally, calculate reserves for the subset of the liabilities across both the reduced set of scenarios and the full set of scenarios. If the reserves calculated for the subset of liabilities using the scenario subset are not materially smaller than the reserves calculated for the subset of liabilities using all the scenarios, then the actuary might reasonably conclude that the subset of scenarios is appropriate to use.
5. If reserves are materially smaller using the subset of scenarios, repeat step 3 using a larger subset of scenarios to determine if an appropriate subset can be selected.

Some actuaries might conclude that if the same technique is used to pick a representative subset of the liabilities in successive periods, then it is not necessary to revalidate the appropriateness of that liability subset for use in validating scenario subsets. Some actuaries might conclude that it is necessary to repeat this process only when the characteristics of the liabilities, the assets backing them, or the economic environment have materially changed.

## $Q$ 12.5: What if there are a lower number of scenarios that results in a higher reserve than a greater number of scenarios?

A: VM-20 does not prevent the actuary from selecting a scenario subset that produces a reserve that is greater than that produced using the full set of 10,000 scenarios. Some actuaries would hold the lower reserve based on the larger number of scenarios to take into account the additional credibility of the larger scenario set. Other actuaries would hold the higher reserve based on the smaller scenario set (if in the actuary's judgment the number of scenarios in the smaller scenario set is reasonable for the purpose of calculating the Stochastic Reserve requirement).

## $Q$ 12.6: Can the actuary use scenarios other than prescribed scenarios for calculating the Stochastic Reserve?

A: Yes, if the scenarios produce a more conservative Stochastic Reserve. Section 1.A states that the VM-20 requirements establish the minimum reserve valuation standard. Although Section 7.G. 2 specifically requires use of the "prescribed economic scenario generator with prescribed parameters, as described in Appendix 1", this does not prevent the actuary from using scenarios that produce a result in excess of the minimum requirement. Some actuaries wishing to use different scenarios would review the decision with their state regulators, as well as work with their tax department to understand any implications for the calculation of tax reserves.

$Q$ 12.7: How are separate account funds mapped into the specific equity return indices of the prescribed economic scenario generator?

A: Per Section 7.J. 2 of VM-20, the company shall design an appropriate proxy for each variable subaccount in order to develop the investment return paths and map each variable account to an appropriately crafted proxy fund normally expressed as a linear combination of recognized market indices.

A Guidance Note in Section 7.G.2.b states that:

Mapping of the returns on the proxy funds to the prescribed fund's returns is left to the judgment of the qualified actuary to whom responsibility for this group of policies is assigned, but the returns so generated must be consistent with the prescribed returns. This does not imply a strict functional relationship between the model parameters for various markets/funds, but it would generally be inappropriate to assume that a market or fund consistently “outperforms" (lower risk, higher expected return relative to the efficient frontier) over the long term.

Actuaries might wish to effect modeling of funds in different ways. For example, some actuaries might perform a regression of past fund performance against past performance of market indices consistent with the scenario generator classifications and develop a scenario set for each such fund that is consistent with an appropriate weight of such scenarios derived from the regression.

Alternatively, funds might be decomposed using regression techniques into funds corresponding to each of the indices.

## $Q$ 12.8: How can the actuary obtain the scenarios used for the Stochastic Exclusion Ratio Test?

A: VM-20 Section 6.A. 2 requires that the same prescribed economic scenario generator used for stochastic scenario generation be used to generate the 16 scenarios used for the Stochastic Exclusion Ratio Test. These are produced by selecting the "Stochastic Exclusion Test Scenarios" on the Scenario Generator tab of the workbook.

## $Q$ 12.9: How can the actuary obtain the scenario used for the Deterministic Reserve?

A: VM-20 Section 4.A. 1 specifies that the Deterministic Reserve is to be calculated using scenario 12 from the set of prescribed scenarios used in the Stochastic Exclusion Ratio Test.

## $Q$ 12.10: What changes are made to the prescribed economic stochastic scenario generator parameters for non-U.S. economies?

A: Section 7.G. 2 requires the actuary to use the prescribed economic scenario generator provided by the American Academy of Actuaries, with prescribed parameters. That said, some actuaries might conclude that it
is unreasonable to use these parameters for non-U.S. interest rates. In a situation where non-U.S. interest rates are required, some actuaries would deem it appropriate to:

- Use historical interest rates in that market, in the same formula used in the United States, to determine the mean reversion target appropriate for that market; and
- Update the starting yield curve to match government bond yields in that market.

In addition, some actuaries might wish to update volatility, correlation, and other parameters to be consistent with the market in question.

For equity returns in non-U.S. markets, the actuary might want to use techniques similar to what is used for U.S. funds to map each fund into one or more of the funds generated by the prescribed economic scenario generator. Section 7.G.2.b states that if a proxy fund cannot be appropriately mapped to some combination of the prescribed returns, the company shall determine an appropriate return and disclose the rationale for determining such return.

The Guidance Note in Section 7.G.2.b states that it would generally be inappropriate to assume that a market or fund consistently outperforms (lower risk, higher expected return relative to the efficient frontier) over the long term.

## $Q$ 12.11: How does the actuary generate interest rates for maturities not generated by the economic scenario generator?

A: The prescribed economic scenario generator only generates interest rates for selected terms to maturity. For some purposes, the actuary might need a full set of interest rates at other maturities. A range of options is available for this. VM-20 gives no guidance.

Techniques some actuaries might find reasonable could include, but would not be limited to, the following:

- Linear interpolation;
- Bootstrapping the curve to find forward rates that increase linearly between the given maturity points and are consistent with the given rates;
- Using the Nelson-Siegel parameters and formulas documented in the scenario generator release notes; or
- Cubic spline interpolation.


## Q 12.12 How are scenarios generated for VM-20 calculations?

A: Per Section 2.E of VM-20, the calculation of the Stochastic and Deterministic Reserves can be performed as of a date up to three months prior to the valuation date as long as an appropriate method is used to adjust the reserves to the valuation date.

Some actuaries generate refreshed scenarios as of each valuation date. Others use scenario data from up to three months prior to the valuation date, although in this case, the actuary will need to use an appropriate method to adjust the reserves to the valuation date. If a model segment is not sensitive to the economic environment, some actuaries choose to generate new scenarios on a less frequent basis, keeping in mind the requirements for making simplifications in Section 2.G.

If fewer scenarios than the full set of 10,000 scenarios are used, then the subset of scenarios are reproduced each time scenarios are generated. Question 11 of the Academy Interest Generator FAQ document, which is provided on the SOA website with each update of the ESG, indicates that if the start date, projection length, or other parameters of the generator are updated, then the actuary would generate a full set of 10,000 scenarios before generating a subset of scenarios in order to stratify the scenarios correctly.

See Question 12.2 for more details on documentation on the prescribed generator provided on the SOA website.

## 13. Setting Prudent Estimate and Anticipated Experience Assumptions

## $Q$ 13.1: How are prudent estimate assumptions determined?

A: VM-01 defines margins and prudent estimate assumptions, where prudent estimate assumptions equal anticipated experience assumptions plus a margin. The margin may increase or decrease the assumption as appropriate to cover adverse deviations and estimation error of the assumed risk factors. The margin should result in a larger reserve than would otherwise result without it. There is no requirement in VM-20 to add a margin to assumptions that are stochastically modeled because the applicable conditional tail expectation (CTE) measure provides a margin.

VM-20 requires a margin for each material risk factor. If sensitivity testing shows that the risk factor does not have a material impact on the reserve, some actuaries will establish the prudent estimate assumption for this risk factor without separately identifying a margin.

Section 4.3 of ASOP No. 1, Introductory Actuarial Standard of Practice, states: "Actuaries are responsible for determining which ASOPs apply to the task at hand." Relevant actuarial standards of practice may include, but are not limited to, the following:

ASOP No. 2 Nonguaranteed Charges or Benefits for Life Insurance Policies and Annuity Contracts

ASOP No. 7 Analysis of Life, Health, or Property/Casualty Insurer Cash Flows

ASOP No. 11 Financial Statement Treatment of Reinsurance Transactions Involving Life or Health Insurance

ASOP No. 15 Dividends for Individual Participating Life Insurance, Annuities, and Disability Insurance

ASOP No. 22 Statements of Opinion Based on Asset Adequacy Analysis by Actuaries for Life and Health Insurers

ASOP No. 23 Data Quality

ASOP No. 25 Credibility Procedures

ASOP No. 52 Principle-Based Reserves for Life Products under the NAIC Valuation Manual

## $Q$ 13.2: How are material risk factors assessed?

A: Section $2 . H$ requires the company to establish a standard containing the criteria for determining whether an assumption, risk factor, or other data element has a material impact on the size of the reserve. VM-20 further states within this section that this standard must consider the impact relative to the size of the NPR, DR, and SR and not of the overall financial statement. Although an actuary might use a broader view of materiality when assessing assumption setting for alternative purposes or bases, this may not be appropriate for VM-20.

VM-20 also provides guidance that each component of the reserve to be assessed independently when determining the material risk factors. Though the final reported reserve at the valuation date could be the NPR, the actuary must still make an assessment of material risk factors based on the modeled reserve, where applicable. The guidance note in Section 2.H states that the criteria of assessing material risk factors apply to the NPR, DR, and SR, and not just based on the final reported reserve.

The standard also applies to exclusion tests.

## $Q$ 13.3: Are the same prudent estimate assumptions used for deterministic and stochastic calculations?

A: Section 9.A.5 of VM-20 requires prudent estimate assumptions to be consistent for the two calculations. Some actuaries would use the same assumptions except where the risk factor is scenario-dependent.

## $Q$ 13.4: Which risk factors do not require a prudent estimate assumption?

A: According to Sections 9.A. 1 and 9.A.4, the company is not required to develop prudent estimates for assumptions that are stochastically modeled. Per Section 9.A.3, risk factors that must be stochastically modeled, and therefore do not require prudent estimate assumptions, include interest rate movements (i.e., Treasury interest rate curves) and equity performance.

Some actuaries might not develop a prudent estimate assumption for risk factors that do not materially affect modeled reserves as permitted by Sections 9.A. 1 and 9.B.4. In this case, anticipated experience assumptions should be used pursuant to Section 9.A.6.

## $Q$ 13.5: How will actuaries set anticipated experience assumptions?

A: Per Section 9.A.6, the actuary shall use company experience, if relevant and credible, to establish the anticipated experience assumption for any risk factor, if such risk factor has been categorized as a material risk. To the extent the company experience is not available or credible, the actuary may use industry experience or other data to establish the anticipated experience assumption, making modifications as needed to reflect the circumstances of the company.

Some actuaries develop anticipated experience assumptions based on the assumptions used for pricing and development of the product. Many actuaries consider whether it is necessary to work closely with the product development actuary to understand the basis for assumptions and review the studies performed prior to using them in the reserve calculations to assure they meet the criteria set in Section 9.A.6.

## $Q$ 13.6: Can actuaries use company experience if it predates the effective date of VM-20?

A: Some actuaries will use company experience that predates the effective date of VM-20 if it is relevant and credible for the assumption or margin that is being determined. There is no requirement in VM-20 that the experience data used to determine anticipated experience assumptions and/or margins for prudent estimate assumptions has to occur on and after the effective date of VM-20.

## $Q$ 13.7: When will the actuary update the anticipated experience assumptions?

A: Section 9.A.6.d requires the actuary to annually review relevant emerging experience, and Section 9.A. 2 requires that the assumptions be periodically reviewed and updated. Therefore, it is expected that actuaries
will update assumptions if there is new experience data or other information that changes the actuary's assumptions of anticipated experience. Actuaries will evaluate the materiality of the assumptions using the results of sensitivity tests, company practice for updating assumptions, and the credibility of the new data and other information in determining whether to update the experience assumptions. Experience assumptions are not locked in at issue.

## $Q$ 13.8: What data sources are used to set anticipated experience assumptions?

A: Per Section 9.A.6, the company shall use its own experience, if relevant and credible, to set anticipated experience assumptions. In instances where company-specific data is not available or credible, actuaries might wish to consider looking to alternative sources as discussed in Section 9.A.6.a, Section 9.A.6.b, and Section 9.A.6.c.

A non-exhaustive list of possible data sources to consider for developing anticipated experience assumptions is listed below:

- Company data on the same or similar products
- Industry or reinsurer data on the same or similar products
- General population data
- Predictive models or algorithms
- Statistical methods such as conservation of deaths or the "Dukes-MacDonald" method
- Sound actuarial judgment, if risk factors have limited or no experience, or other applicable data available

For assumptions that are established based on limited data, Section 9.A.6.d requires the actuary to sensitivity test the assumption chosen to ensure the assumption is set at the conservative end of the plausible range.

## $Q$ 13.9: What other issues would the actuary take into account when setting anticipated experience assumptions?

A: The actuary may wish to consider whether anticipated experience assumptions developed from the data should be modified as needed to reflect the circumstances of the company. For example, if the data from alternative sources includes mortality experience based on three underwriting classes, and the company has just two underwriting classes, then adjustments to the assumptions may be needed to make them appropriate for the company's underwriting classes.

The actuary may wish to consider adjusting assumptions that are based on historical experience to consider contractual guarantees that are present in the contracts being valued that were not present in the contracts that contributed to the experience base. The actuary may also wish to consider the possibility of antiselection affecting assumptions. For example, antiselection may involve a combination of lapses, persistency, mortality, and the level of guarantees.

The actuary may also wish to consider reviewing contractual guarantees to determine whether and to what degree these contractual guarantees will impact future cash flows of the model.

## Q 13.:10 When might it be appropriate to represent extreme or catastrophic behavior?

A: Section 9.D.2.c states that the company is not required to model extreme or "catastrophic" forms of behavior in the absence of evidence to the contrary.

## $Q$ 13.11: How do trends in data affect the anticipated experience assumption?

A: Some actuaries assess a granular subset of data for comparison to experience of other exposure periods An example of this analysis would be in comparing lapse data for a certain product over calendar years 2000 2004 to the same grouping over calendar years 2005-2009. For these comparisons, the actuary would confirm the data used continues to be relevant and credible at this level, as stated in Section 9.A.6.

Some actuaries project trends that in their judgment are likely to be sustained in the future in the anticipated experience assumption, subject to any applicable restrictions. Some actuaries make a judgment on the uncertainty surrounding the projection of the trend and increase the margin as uncertainty increases, such as in later durations.

Trends to improve mortality cannot be reflected as the company is prohibited from reflecting mortality improvement beyond the valuation date, as stated in Section 9.C.2.h. This is further described at Q15.18. The VM-20 restrictions on mortality improvement do not preclude the use of a mortality dis-improvement assumption beyond the valuation date. Some actuaries might consider this when establishing a mortality trend anticipated experience assumption or any applicable margins for this assumption.

In Section 9.A.6.d, the last paragraph states that "the qualified actuary, to whom responsibility for this group of policies is assigned, shall annually review relevant emerging experience for the purpose of assessing the appropriateness of the anticipated experience assumption. If the results of statistical or other testing indicate that previously anticipated experience for a given factor is inadequate, then the qualified actuary shall set a new, adequate, anticipated experience assumption for the factor."

## $Q$ 13.12: How does the actuary determine whether company experience data is credible?

A: A discussion of credibility in the context of the mortality assumption is found in Section 15 of this practice note. ASOP No. 25, Credibility Procedures, is available on the Actuarial Standards Board's website. To make a determination on the level of credibility of company experience data may have, some actuaries might use concepts from classical credibility theory. In this sense, the actuary may determine that full credibility (i.e., the subject experience will have full predictive value) will be established when enough observations of an event occur so that the actual result of its frequency will be within a defined percentage of the expected results with a specified probability. Additional adjustments to the definition of full credibility may be used in cases where the actual observed events can range in their magnitude of severity. The Credibility practice note ${ }^{2}$ has further details on this subject.

If the number of observations is fewer than the amount needed for full credibility, partial credibility of the data may be established. This can be done by using information such as the expected number of observations and the number of observations needed for full credibility.[^1]

Some actuaries with data that is only partially credible might use actuarial judgment to combine partially credible data with other industry experience to determine their anticipated experience assumptions. Some actuaries also increase the margin where company experience data is only partially credible.

## $Q$ 13.13: Would the actuary perform sensitivity testing to set anticipated experience assumptions or prudent estimate assumptions?

A: Yes. Section 9.A. 7 requires sensitivity testing for assumptions that are not stochastically modeled to understand the impact this testing has on the modeled reserve. The sensitivity testing shall be updated periodically as appropriate. Section 9.A.7 states that the company may test less frequently when the tests show less sensitivity of the modeled reserve to changes in the assumptions being tested or that the experience is not changing rapidly. Section 9.A.7 provides a guidance note that clarifies sensitivity analysis is not required on an annual basis.

To perform the sensitivity testing, some actuaries use anticipated experience assumptions. Other actuaries instead perform the sensitivity testing using prudent estimate assumptions.

If sensitivity testing shows that an assumption is material to the modeled reserve, Section 9.B.3 states that greater analysis and more detailed justification are needed to determine the level of uncertainty when establishing margins for risk factors that produce greater sensitivity on the modeled reserve. Therefore, it might be prudent for the actuary to review the credibility of the data used to set the assumption and whether the assumption is set at the appropriate level.

## 14. Setting Margins

## $Q$ 14.1: What types of risks require margins?

A: Material risks require margins. Section 9.A. 1 states that the company shall use prudent estimate assumptions for each risk factor that is not stochastically modeled by applying a margin to the anticipated experience assumption for the risk factor, if such risk factor has been categorized as a material risk. Section 9.B. 1 categorizes risks as summarized below.

1. Risks that shall be considered material risks

- Risks that are stochastically modeled (e.g., interest rates, equity returns)
- Risks that have prescribed margins (e.g., mortality, revenue sharing)

2. Risks that are generally considered material risks. These include but are not limited to:

- lapses/premium persistency
- YRT premiums
- maintenance expenses
- inflation

3. Risks that may be considered material risks in some cases. These risks include:

- morbidity
- acquisition expenses
- partial withdrawals
- policy loans
- term conversions
- non-guaranteed elements, and/or option elections that contain an element of anti-selection


## $Q$ 14.2: Is there a standard for determining which risks are categorized as material risks?

A: Yes. VM-20 Section 2.H requires the company to establish for the DR and SR, a standard containing the criteria for determining whether an assumption, risk factor or other element of the principle-based valuation has a material impact on the size of the reserve. Such a standard shall also apply to the NPR with respect to VM-20 Section 2.G. This standard must be applied when identifying material risks, and is based on the impact relative to the size of the NPR, DR, and SR, as opposed to the impact relative to the overall financial statement (e.g., total company reserves or surplus). For example, the standard may be expressed as an impact of more than $\mathrm{X}$ dollars or $\mathrm{Y} \%$ of the reserve, whichever is greater.

Note that VM-31 Section 3.C. 1 requires disclosure of the standard established by the company, and Section

3.D.1.a requires, for each material risk, the anticipated experience assumptions, margins, and prudent estimate assumptions used in the model, in Excel format.

## $Q$ 14.3: What are the VM-20 requirements when determining appropriate margins?

A: Section 9.B. 1 states that the company shall determine an explicit set of initial margins for each material risk independently. If applicable, the actuary may apply an adjustment to take in to account the fact that risk factors are not normally $100 \%$ correlated. Section 9.B. 1 states that it is not permissible to adjust the initial margin to recognize, in whole or in part, implicit or prescribed margins that are present, or are believed to be present, in other risk factors. For example, if lapses are a material risk, it is not permissible to reduce or eliminate the lapse margin because the prudent estimate mortality assumptions are conservative. Per Section 9.B.4, a margin is permitted but not required for assumptions that do not represent material risks.

Section 9.B. 2 states that higher margins should be used when:

- The experience data has less relevance or lower credibility;
- The experience data are of lower quality, such as incomplete, internally inconsistent, or not current;
- There is doubt about the reliability of the anticipated experience assumption, such as, but not limited to, recent changes in circumstances or changes in company policies; or
- There are constraints in the modeling that limit an effective reflection of the risk factor.

Greater analysis and more detailed justification are required when establishing margins for risk factors that produce greater sensitivity on the modeled reserve.

Section 9.B.5 states that a margin should reflect the magnitude of fluctuations in the historical experience of the company for that risk factor, as appropriate.

Section 9.B. 6 states that the company shall apply the method used to determine the margin consistently on each valuation date, but is permitted to change the method from the prior year if the rationale for the change and the impact on modeled reserve is disclosed.

Sections 9.C.6 and 9.D. 3 provide specific requirements for setting margins for mortality and policyholder behavior, respectively.

## $Q$ 14.4: What other references are available when determining appropriate margins?

A: Many actuaries use the following:

- Life Principle-Based Reserves (PBR) Assumptions Resource Manual
- A Society of Actuaries research paper titled Analysis of Methods for Determining Margins for Uncertainty Under a Principle-Based Framework for Life Insurance and Annuity Products (March 31, 2009).
- $\quad$ ASOP No. 52, Principle-Based Reserves for Life Products under the NAIC Valuation Manual, adopted September 2017.
- The C3 Phase III Report and associated practice note.
- The AG-43 / C3 Phase II practice note.
- Internal documentation of margins used for other financial reporting methods, for example, U.S. GAAP FAS 60 margins.
- Various Canadian valuation technique papers and educational notes
- ASOP No. 25, Credibility Procedures


## $Q$ 14.5: What general method are used in setting margins?

A: Some actuaries focus on the key assumptions (those that are most material) for the underlying product first and then analyze how those margins affect other assumptions. For example, for an annually renewable term product, the actuary might initially focus on setting the anticipated mortality experience and margin assumptions (because it is likely the most material risk factor) and then set other assumptions such as lapse rates and expenses such that these assumptions are internally consistent with the mortality assumption. One advantage of concentrating on the key assumptions is avoiding the situation where the application of a margin to one assumption affects the direction of the appropriate margin to apply to another assumption (e.g., a high mortality margin may cause lower rather than higher lapses to be conservative).

Some actuaries would develop an approach to setting margins in a manner consistent with the underlying principle of reflecting the underlying risk characteristics of the product.

## $Q$ 14.6: When can and how does the actuary apply an adjustment in setting the margins to account for risk

 factors not being $100 \%$ correlated?A: Per Section 9.B.1, the initial level of a particular margin may be adjusted to take into account the fact that risk factors are not normally $100 \%$ correlated. The initially determined margin may only be reduced to the extent the company can demonstrate that the method used to justify such a reduction is reasonable considering the range of scenarios contributing to the CTE calculation, recognizing that risk factors may become more correlated in adverse circumstances, or considering the scenario used to calculate the Deterministic Reserve as applicable or considering appropriate adverse circumstances for risk factors not stochastically modeled.

Industry practice determining covariance adjustments is expected to evolve over time.

## $Q$ 14.7: Does the sensitivity of an assumption's impact on the overall reserve level affect how the margin is set?

A: Yes. Section 9.A. 7 requires companies to sensitivity test risk factors that are not stochastically modeled and examine the impact on the modeled reserve. Section 9.B.3 states that in complying with these sensitivity testing requirements, greater analysis and more detailed justification are needed to determine the level of uncertainty when establishing margins for risk factors that produce greater sensitivity on the modeled reserve. One approach to determine the uncertainty of a risk factor is to measure the standard deviation around the mean or other standard statistical measure (if meaningful historical experience data is available for the risk factor).

For discussion of practical issues, see Q 14.13.

## $Q$ 14.8: Are there instances where it may be appropriate to use no margin, or to use a small margin?

A: Yes. Section 9.B. 4 indicates that a margin is not required for assumptions that do not represent material risks.

In addition, since VM-20 Section 9.B. 2 indicates that margins must increase the reserve, it would be appropriate to use no margin if the anticipated experience assumption (before margin) produces the most conservative result. In these instances, either increasing or decreasing the anticipated experience assumption (before margin) would decrease the reserve. An example of this situation might be the anticipated assumption for ULSG paid premium timing and/or amount.

It could be appropriate to use a small margin for some assumptions. Some actuaries use small margins for risk factors having a material impact on the reserves but little uncertainty. For example, if an expense assumption has a large impact on the reserve but is known with certainty (it has been outsourced for a fixed contractual cost), then a smaller margin could be appropriate.

## $Q$ 14.9: Are there additional considerations for setting margins for specific assumptions?

A: Yes. The specific considerations for mortality, policyholder behavior, and expense margins are discussed in the respective sections of this practice note covering those items.

Per VM-20 Section 9.B.1, it is also important to note that recognition of an implicit margin (e.g., mortality improvement after the valuation date) in the anticipated experience mortality assumption is only appropriate for the disclosures referenced in VM-31 Section 3.D.11.c, and is not appropriate for a principle-based valuation in VM-20.

## $Q$ 14.10: Can the actuary use Canadian prescribed margins?

A: Some actuaries might use Canadian prescribed margins, but VM-20 does not prescribe their use, therefore the actuary would need to determine whether they are appropriate for use in the reserve calculation as set forth in $\mathrm{VM}-20$.

VM-20 Section 9.D. 5 prescribes the use of the Lapse Experience Under Term to 100 Insurance Policies published by the Canadian Institute of Actuaries, but this is not considered a margin.

## $Q$ 14.11: To what extent does the size of the company affect the size of the margins used?

A: Some actuaries would not modify the size of the margins based solely on the size of the company. For example, smaller margins generally coincide with a reduction in uncertainty that might be due to a large number of observations, but is not necessarily dependent on company size because a large number of observations could be generated over time from a smaller company.

## $Q$ 14.12: What are the considerations for setting margins across blocks of business?

A: Some actuaries would assess whether the margins were appropriate by product as well as adequate over a broad set of policies. This assessment would be particularly useful for products with uncertain risks or particularly unique characteristics. Some actuaries would review the margins in aggregate, particularly where policy characteristics are similar or have homogeneous risks.

VM-31 Section 3.D.11.d requires disclosure of the specific sensitivity tests performed for each risk factor or combination of risk factors and an explanation of how the results of sensitivity tests were used or considered in developing assumptions. If a model segment contains multiple distinct product types (e.g. Annually Renewable Term and Level Term), this is done for each product type.

## $Q$ 14.13: How are margins set when the impact of assumption movements changes over the duration of the business?

A: For some products, the impact on the aggregate reserve of increasing or decreasing an assumption may vary according to the duration of the business. For example, the lapse rate margins on a level term plan could increase lapses in the first few years but decrease lapses for the remainder of the level term period. VM-20 Section 9.D. 3 states that the company shall perform testing to determine whether the modeled reserve is materially impacted by variations in the size and direction of the margin and shall do so using a methodology that recognizes that the appropriate size and/or direction of a margin in the early durations may be quite different from that in later durations. If the impact on the modeled reserve is material, the company shall establish margins accordingly

Where there is a clear change in the policy, such as a dramatic change in premiums or surrender charges, some actuaries will develop a margin that differs before and after this point.

VM-31 Section 3.D.4.d requires disclosure of the rationale for the particular margins used and a description of testing performed to determine the size and direction of the margins by duration, including how the results of sensitivity testing were used in connection with setting the margins. Also, as noted earlier in this question, VM-31 Section 3.D.11.d requires disclosure of the specific sensitivity tests performed for each risk factor and an explanation of how the results of sensitivity tests were used or considered in developing assumptions. If a model segment contains multiple distinct product types (e.g., Annually renewable Term and Level Term), this should be done for each product type.

## Q 14.14: How are margins determined for dynamic assumptions?

A: As implied by Sections 9.A.3 and 9.A.4, where an assumption is dependent on interest rates or equity returns and a dynamic formula is included in the modeling, some actuaries would not add an additional margin to the calculation, on the basis that conservatism is provided by the conservatism inherent in the tail measure (i.e., CTE) and in their judgment this implicit margin would satisfy the requirements of Section 9.B.

However, other actuaries add additional conservatism, as they feel that the use of the tail measure will only inject conservatism regarding the interest rate or equity risk, but not necessarily the dynamically related risk, which they might see as a distinct risk. Some of these actuaries would add conservatism by making the dynamic formula slightly more or less dynamic (depending on what would be more conservative) than anticipated.

Some actuaries consider margins on the base underlying assumption to be applicable to the resulting assumption including dynamic components, so would not add an additional margin.

## $Q$ 14.15: How often are margins be updated?

A: Section 9.A. 2 states that the company shall establish the prudent estimate assumption for each risk factor in compliance with the requirements in Section 12 of Model \#820 and must periodically review and update the assumptions as appropriate in accordance with these requirements. Section 12.A.4 of Model \#820 requires that a principle-based valuation must provide margins for uncertainty including adverse deviation and estimation error, such that the greater the uncertainty the larger the margin and resulting reserve.

Some actuaries would use consistent margins or the same margins from one reporting date to the next unless there is a particular reason the actuary believes the credibility, quality, or reliability of the assumption has changed. Most actuaries review and update their margins as needed as part of their review of the assumptions used in the principle-based valuation.

## 15. Setting Mortality Assumptions

## $Q$ 15.1: What are the steps to determining mortality assumptions for the Deterministic Reserve and/or Stochastic Reserve?

A: For these reserves, mortality assumptions are discussed in Section 9.C of VM-20. (For the Net Premium Reserve, mortality assumptions are provided in Section 3.C.1.) The following approach is defined for determining the prudent estimate mortality assumption:

1. Determine mortality segments as provided in Section 9.C.1.a.
2. Determine company experience rates as provided in Section 9.C.2, or, if company experience data is limited or not available, use an applicable industry basic table or other applicable experience in lieu of company experience as provided in Section 9.C.3.
3. Use the procedure described in Section 9.C. 3 to determine the applicable industry table for each mortality segment. If the company is using an applicable industry basic table in lieu of company experience as provided in Section 9.C.3, skip to step 5.
4. Determine the anticipated experience assumptions as provided in Section 9.C.4.
5. Determine the level of credibility of the underlying company experience as provided in Section 9.C.5. Per Section 9.C.5.b, credibility may be determined at either the mortality segment level or at a more aggregate level if the mortality for the individual mortality segments was determined using an aggregate level of mortality experience pursuant to Section 9.C.2.d.
6. Determine the prescribed mortality margins as provided in Section 9.C.6. Separate mortality margins are determined for company experience mortality rates and the applicable industry basic tables.

Prescribed margin percentages shall be increased, as appropriate, to reflect the level of uncertainty related to situations, including, but not limited to, those described in Section 9.C.6.d.

7. Use the procedure described in Section 9.C. 7 to determine the prudent estimate mortality assumption.

## $Q$ 15.2: How are the applicable industry basic tables chosen?

A: A company may use the Relative Risk Tool described in Section 9.C.3.d to choose the industry basic tables. However, in determining the applicable industry basic table, a company must take into account factors not recognized in the Relative Risk Tool that may be applicable. To reflect factors not recognized in the Relative Risk Tool, the company may, to the extent it can justify, adjust industry basic tables up or down two tables from that determined by the Relative Risk Tool, as noted in Section 9.C.3.d.iii. As an alternative, a company may use other actuarially sound methods to determine the applicable basic tables.

## $Q$ 15.3: In what circumstances is a modified industry basic table permitted?

The actuary may wish to consider whether the industry basic table developed pursuant to Section 9.C.3.a should be modified as needed to reflect the circumstances of the company. This is only allowed in a limited number of situations as discussed in Section 9.C.3.b:

A modified industry basic table is permitted in a limited number of situations where an industry basic table does not appropriately reflect the expected mortality experience, such as joint life mortality, simplified underwriting, or substandard or rated lives. In cases other than modification of the table to reflect joint life mortality, the modification must not result in mortality rates lower than those in the industry basic table without approval by the commissioner.

## $Q$ 15.4: For what purposes may the Relative Risk Tool be used?

A: The Relative Risk Tool may be used to determine the industry basic table that can serve as industry experience rates. These can be used when company experience data is limited or not available as well as for grading from company experience to industry experience mortality.

## $Q$ 15.5: How are risk classes scored under the Relative Risk Tool?

A: The Relative Risk Tool adopted by the Life Actuarial (A) Task Force contains an algorithm that scores every risk class in a preferred risk class structure and is maintained on the Society of Actuaries website. ${ }^{3}$ Risk classes are scored based on the specific underwriting criteria used by a company.

## $Q$ 15.6: How does the actuary take into consideration factors not recognized in the Relative Risk Tool?

A: Such factors can be taken into account to the extent these can be justified by adjusting the industry tables up or down two tables from that determined by the application of the Relative Risk Tool. Further adjustments to reflect risk characteristics not captured by the Relative Risk Tool may be allowed upon approval by the commissioner.[^2]

## $Q$ 15.7: Can the Relative Risk Tool be used to determine the applicable industry basic tables for policies

with simplified or no underwriting?

A: No. The Relative Risk Tool is applicable only to underwriting systems with a preferred class structure, and not to underwriting systems utilizing simplified issue or guaranteed issue methodologies. Alternative methods are allowed. Section 9.C.3.e of VM-20 states that the company shall document the analysis performed to demonstrate the applicability of the chosen method and resulting choice in tables and reasons why the results using the Relative Risk Tool may not be suitable. (For these programs, the company would develop an alternative method for determining a prudent estimate for mortality and might consult with the commissioner prior to implementation.)

Q 15.8: How does the applicable industry basic table be determined for policies that were rated substandard but issued as standard?

A: Some actuaries might use the results of the Relative Risk Tool for the rated substandard class to determine the applicable industry basic table. Other actuaries might use the results of the Relative Risk Tool and adjust upward by up to two tables to the extent this can be justified.

## $Q$ 15.9: What procedure is used if the actuary believes it is appropriate to make a greater adjustment?

A: If adjustments greater than two tables up or down are felt to be appropriate, Section 9.C.3.d.iii indicates the actuary must obtain the approval of the commissioner.

## $Q$ 15.10: What alternatives may be used to the Relative Risk Tool and what is required to use such alternatives?

A: Some companies may use other actuarially sound methods to determine the applicable basic tables. The company must document the analysis performed to demonstrate the applicability of the chosen method and the resulting choice in tables and reasons why the results using the Relative Risk Tool may not be suitable.

## $Q$ 15.11: What is done if no industry basic table appropriately reflects the risk characteristics of the

 mortality segment?A: Per Section 9.C.3.f, if there is no appropriate basic industry table, a company may use any well-established industry table that is based on the experience of policies having the appropriate risk characteristics for the mortality segment. This might be the case when the policies involve group-type mortality; there are possibly other situations.

$Q$ 15.12: Is the company required to determine its own company experience mortality rates, or can it just use an industry mortality table?

A: Section 9.A. 6 states that the company shall use its own experience, if relevant and credible, to establish an anticipated experience assumption for any risk factor. Per Section 2.G, a company may use simplifications, approximations and modeling efficiency techniques to calculate the PBR reserve components if the company can demonstrate that the use of such techniques does not understate the reserve by a material amount. Additionally, Section 9.B. 2 notes that the actuary should reflect the degree of uncertainty in the anticipated experience assumption by using a larger required margin to produce a larger modeled reserve than would otherwise result. Given these considerations, VM-20 does not explicitly prohibit the use of an
industry mortality table in lieu of relevant and credible company experience; however, the company should provide a demonstration around the materiality of this simplification as part of their PBR Actuarial Report.

Section 9.C.7.a states that if the credibility of company's data is less than $20 \%$, the company cannot use its own experience; $100 \%$ of the applicable industry tables should be used instead.

## Q 15.13: What is the Applicable Industry Table?

A: The Applicable Industry Table is the most recent valuation basic table listed in VM-M Section 2, including the Primary, Limited Underwriting, and RR Table form, if available.

## Q 15.14: Are the mortality rates based on experience for each cell, for each mortality segment, or for the company?

A: Section 9.C.2.b states that company experience data shall be based on experience from the following sources:

- Actual company experience for books of business within the mortality segment.
- Experience from other books of business within the company with similar underwriting.
- Experience data from other sources, if available and appropriate, such as actual experience data of one or more mortality pools in which the policies participate under the term of a reinsurance agreement. Data from other sources is appropriate if the source has underwriting and expected mortality experience characteristics that are similar to policies in the mortality segment.

VM-20 states that company experience mortality rates shall be determined for each mortality segment (Section 9.C.2.a), but the rates can be based on the aggregate company experience for a group of mortality segments if the mortality segments were subject to the same or similar underwriting processes, as defined in Section 9.C.2.d.

If experience is aggregated, Section 9.C.2.d states that the company should either use techniques to further subdivide the aggregate class into various mortality segments, or use techniques to adjust the experience of each mortality segment to reflect the aggregate experience for the group. In doing so, the company must ensure that when the mortality segments are weighted together, the total number of expected claims is not less than the aggregate company experience data for the group.

## $Q$ 15.15: How are the mortality rates that were established based on the aggregate company experience be subdivided into sub-classes (mortality segments)?

A: VM-20 does not specify a method for subdividing aggregate company experience into sub-classes or mortality segments. However, Section 9.C.2.d does state that the company must ensure that when the mortality segments are weighted together, the total number of expected claims is not less than the company experience data for the aggregate class.

Some actuaries use the Conservation of Deaths and / or the Preservation of Total Deaths methods to subdivide aggregate mortality rates into sub-classes, however, other approaches may be acceptable.

Please see the following source documents for more information on each method.

## Conservation of Deaths

Society of Actuaries Study Note ILA-D107-07; Experience Assumptions for Individual Life Insurance and Annuities; Richard F. Lambert; page 25.

## Preservation of Total Deaths

Life Insurance Products and Finance; Section 3.2.4.3, "Effect of Selective Lapses”; David B. Atkinson and James W. Dallas; pages 149-151.

This is an area where VM-20 requirements are expected to evolve in the coming years. Recent regulatory discussions have raised concerns with companies aggregating mortality experience across dissimilar mortality segments (e.g. underwriting process), and an evaluation is underway to determine if changes to the regulation are needed in order to address this concern.

## $Q$ 15.16: How long of an exposure period is used in the experience study used to determine the mortality assumptions?

A: Section 9.C.2.e.ii states that the company experience should be based on the most recent experience study and the exposure period should be at least three exposure years, but not more than 10 exposure years.

## $Q$ 15.17: How often do experience studies need to be updated?

A: Section 9.C.2.e indicates that the company shall review the mortality experience (in a mortality segment), based on either an updated company mortality study or updated mortality study data from other sources, at least once every three years and update as needed. Some companies review their experience every year, while others establish a rotating basis for annual reviews of experience across mortality segments so that each segment is reviewed at least every three years. Some companies leverage experience studies that are being performed for other purposes within the company, or the experience reporting for VM-51, and perform reviews at that time.

Section 9.C.2.e indicates that the company shall reflect changes that are implied by any updated experience data to the extent that such changes are significant and are expected to continue into the future. Such changes should be reflected in the current year.

## $Q$ 15.18: Can mortality improvement be used?

A: Section 9.C.2.h indicates that the company may reflect mortality improvement from the central point of the underlying company experience data to the valuation date. The mortality rates from the applicable industry basic table may be improved from the year of the table (Jan. 1, 2008 for the 2008 VBT Table and July 1, 2015 for the 2015 VBT Table) to the valuation date, as indicated in Section 9.C.3.g. The company is prohibited by VM-20 from reflecting mortality improvement beyond the valuation date.

Some actuaries use published mortality improvement rates to incorporate mortality improvement into the company experience mortality rates and update the improvement factors every year. Other actuaries only update the projected improvement factors in conjunction with the review of underlying experience and updates of the experience mortality. Actuaries might use improvement factors for the applicable industry table, applied to the industry table that will be determined and published by the Society of Actuaries.

When determining the credibility of company experience data, the actuary will adjust expected mortality rates in a manner consistent with the experience used for assumption setting processes for historical mortality improvement.

## Q 15.19: Would the actuary need to use a specific credibility method to determine the credibility of the mortality experience used to develop the mortality assumption?

A: Section 9.C. 5 requires the use of the Limited Fluctuation Method or the Bühlmann Empirical Bayesian Method to be used to determine credibility of mortality experience for valuations in which the 2015 VBT is the industry basic mortality table. Please see Q 15.20 for additional details on choosing a method and/or changing the method.

The following are additional resources on credibility methods:

- American Academy of Actuaries, Credibility practice note, at http://www.actuary.org/files/publications/Practice_note_on_applying_credibility_theory_july2008.pdf ;
- The Society of Actuaries Research Department, Credibility Theory Practices, at https://www.soa.org/Files/Research/Projects/research-cred-theory-pract.pdf; and
- The Canadian Institute of Actuaries, Expected Mortality Educational Note, at http://www.ciaica.ca/docs/default-source/2002/202037e.pdf?sfvrsn=2.


## $Q$ 15.20: How would the actuary determine whether company mortality experience data is credible?

A: Section 9.C.5.a provides the requirements for the credibility calculation:

- For valuations in which the industry basic table is the 2008 VBT, an aggregate level of credibility over the entire exposure period must be determined using a methodology that follows common actuarial practice as published in actuarial literature (for example, but not limited to, the Limited Fluctuation Method or Bühlmann Empirical Bayesian method).
- For valuations in which the industry basic table is the 2015 VBT, an aggregate level of credibility over the entire exposure period must be determined using either the Limited Fluctuation Method by amount, such that the minimum probability is at least $95 \%$ with an error margin of no more than $5 \%$, or the Bühlmann Empirical Bayesian Method by amount. Once chosen, the credibility method must be applied to all business subject to VM-20 and requiring credibility percentages. A company seeking to change credibility methods must request and subsequently receive the approval of the commissioner. The request must include the justification for the change and a demonstration of the rationale supporting the change.

To make a determination on the level of credibility that a set of company experience may have, actuaries will look to the credibility procedure selected.

Section 9.C.5.a provides the formula to determine the credibility level by amount under the Limited Fluctuation Method.

$$
\begin{aligned}
& \text { Limited Fluctuation } \mathrm{Z}=\min \{1, \mathrm{rm} / \mathrm{z} \sigma\} \\
& \text { where, } \\
& \qquad \begin{array}{l}
r=\text { error margin } \leq 5 \% \\
z=\text { normal distribution quantile } \geq 95 \% \\
m=\text { mortality ratio; i.e., A/E ratio by amount } \\
\sigma=\text { standard deviation of the mortality ratio }
\end{array}
\end{aligned}
$$

Section 9.C.5.a also provides a formula the actuary can use in conjunction with the 2015 VBT industry basic table to compute an approximation to the Bühlmann Empirical Bayesian Method.

$$
\text { Bühlmann } \mathrm{Z}=\frac{\mathrm{A}}{\mathrm{A}+\frac{(109 \% * \mathrm{~B})-(120.4 \% * C)}{(0.019604 * A)}}
$$

The numerical result under either of these methods are rounded to the nearest whole integer.

## Q 15.21: Can company mortality experience be aggregated to establish credibility?

A: VM-20 states the following with respect to establishing the level of credibility of the company experience:

Section 9.C.5.b: Credibility may be determined at either the mortality segment level or at a more aggregate level if the mortality for the sub-classes (mortality segments) was determined using an aggregate level of mortality experience.

Section 9.C.5.b: A single level of credibility shall be determined over the entire exposure period, rather than for each duration within the exposure period.

## $Q$ 15.22: There are five prescribed mortality margin tables in VM-20. Which tables apply to the experience mortality rates and which to the industry table?

A: The table in Section 9.C.6.b.i applies to the margin for company experience mortality rates for valuations in which the industry mortality table is the 2008 VBT limited underwriting table (the 2015 VBT does not have a limited underwriting table). The table in Section 9.C.6.b.ii applies for valuations in which the industry mortality table is the 2015 VBT and where the credibility is determined using the Bühlmann Empirical Bayesian Method by amount. The table in Section 9.C.6.b.iii applies for valuations in which the industry mortality table is the 2015 VBT and where the credibility is determined using the Limited Fluctuation Method. The margin could vary by credibility level, credibility method, valuation basis, and attained age.

The table in Section 9.C.6.c.i applies to the applicable industry table for valuations in which the industry mortality table is the 2008 VBT limited underwriting table. The table in Section 9.C.6.c.ii applies to the applicable industry table for valuations in which the industry mortality table is the 2015 VBT. The margin could vary by attained age and valuation basis.

The margins need to be added to company experience mortality and to the applicable industry table before the grading process takes place. The margin is in the form of a percentage increase applied to each mortality rate.

Per Section 9.C.2.d.v, the prescribed margin percentages should be increased pursuant to Section 9.C.6.d, to the extent that the judgment of the similarity of expected mortality or the estimate of the expected change to mortality increases uncertainty in the mortality assumption.

## $Q$ 15.23: How are the prescribed mortality margin tables used in VM-20?

A: Section 9.C.6.a indicates that there are two separate sets of prescribed margins. One set of prescribed margins is for company experience mortality rates. The tables in Section 9.C.6.b show the margin to be used for company experience mortality rates. Another set of prescribed margins is for the applicable industry basic tables. The tables in Section 9.C.6.c apply to the margin for the applicable industry table. In addition, many actuaries view the lack of future mortality improvement allowed (see Q 15.18) as a source of prescribed margin.

The prescribed margin percentages for the company experience mortality rates vary by the valuation's applicable industry basic tables, credibility method, level of credibility, and attained age. The prescribed margin percentages for the applicable industry basic tables vary by attained age. Based on these factors, the prescribed margin percentages for the company experience mortality rates can range from $0.6 \%$ to $21.0 \%$, whereas they can range from $5.3 \%$ to $21 \%$ for the industry basic tables.

Pursuant to Section 9.C.6.a of VM-20, the mortality margin shall be in the form of a prescribed percentage increase applied to each mortality rate.

Section 9.C.6.d states that the prescribed margin percentages shall be increased, as appropriate. The section provides a possible list of situations to consider in making adjustments to the prescribed margin percentages.

## $Q$ 15.24: Does the actuary apply a margin in addition to the prescribed margins?

A: Some actuaries apply a margin in addition to the prescribed margins to reflect the level of uncertainty in the company mortality experience. Section 9.C.6.d requires that the prescribed margins be increased in situations that include, but are not limited to, the following:

- The reliability of the company's experience studies is low due to imprecise methodology, length of time since the data was updated, or other reasons.
- The length of time since the experience data was updated.
- The underwriting or risk selection risk criteria associated with the mortality segment have changed since the experience on which the company experience mortality rates are based was collected.
- The data underlying the company experience mortality rates lacks homogeneity.
- Unfavorable environmental or health developments are unfolding and are expected to have material and sustained impact on the insured population.
- Changes to the company's marketing or administrative practices or market forces expose the policies to the risk of antiselection.
- Underwriting is less effective than expected.


## $Q$ 15.25: What other considerations should be taken into account in setting margins for the mortality assumption?

A: Some actuaries would include additional margins to reflect uncertainty in antiselection under the following circumstances:

- Term plans with low initial premiums followed by substantially higher premiums;
- Extended term insurance as the nonforfeiture option;
- Conversion at the expiry or very close to expiry of the term coverage period;
- Policies that have elected to exercise a guaranteed purchase option; and
- Products that offer composite rates (i.e., same rate for male/female, various issue/attained ages, underwriting classes, etc.).


## $Q$ 15.26: How does the actuary grade the experience mortality rates into industry rates?

A: Section 9.C.7.b states that if the company uses company experience mortality rates as the anticipated experience assumptions, the prudent estimate assumptions will be determined as follows:

- For each mortality segment, use the company experience mortality rates for policy durations in which there exists sufficient company experience data plus the prescribed margin as provided in Section 9.C.6.b. and any additional margin as provided in Section 9.C.6.d.
- The company shall determine the sufficient data period by identifying the last policy duration at which sufficient company experience data exists (using all the sources defined in Section 9.C.2.b). This period ends at the last policy duration that has 50 or more claims, not counting riders (i.e., no duration beyond this point has 50 claims or more) subject to the limits provided in Section 9.C.7.b.vi. The sufficient data period may be determined at either the mortality segment level or at a more aggregate level if the mortality for the individual mortality segments was determined using an aggregate level of mortality experience pursuant to Section 9.C.2.d.
- Beginning in the first policy duration after the sufficient data period, use the guidelines in the table referenced in Section 9.C.7.b.i to linearly grade from the company experience mortality rates with margins to $100 \%$ of the applicable industry table with margins. (The determination of the applicable industry table is described in Section 9.C.3). Grading must begin and end no later than the policy durations shown in the table referenced in Section 9.C.7.b.i, based on the level of credibility of the data as provided in Section 9.C.5. If the credibility level is less than $20 \%$, the company is not allowed to use their company experience and must use $100 \%$ of the applicable industry table.

$Q$ 15.27: Over how many years would the actuary completely grade the experience mortality rates into the industry table?

A: Section 9.C.7.b describes the limits and requirements for the grading period used for grading experience mortality rates to the industry table. This section is quite extensive, including an example in the guidance note after Section 9.C.7.b.vii, and will not be repeated in this practice note.

$Q$ 15.28: How is "sufficient data" defined for the purposes of grading into the industry table in Section 9.C.6.b? Can the actuary aggregate data across policy durations, mortality segments, and/or issue ages to determine the sufficiency of data?

A: Section 9.C.7.b.ii indicates that the "sufficient data period" is the last policy duration that has 50 or more claims, subject to limits provided in Section 9.C.7.b.vi. This precludes a company from aggregating data across policy durations to determine the sufficient data period. However, Section 9.C.7.b.ii allows a company to determine the "sufficient data period" by aggregating mortality segments if the company based its mortality on aggregate experience and then used a methodology to subdivide the aggregate class into various subclasses or mortality segments. Based on this VM-20 guidance, some actuaries would aggregate data across mortality segments and/or issue ages to determine the sufficient data period.

## $Q$ 15.29: Can the mortality rates produced by following the VM-20 procedure be adjusted?

A: Section 9.C.7.b.vii.d indicates that the company may adjust the resulting mortality rates within each mortality segment to ensure the resulting prudent estimate rates reflect reasonable relationships with assumptions in other mortality segments. The adjustment to the mortality rates must be done in a manner that does not result in a material change in the total expected claims for all mortality segments in the aggregate.

Section 9.C.7.b.vii.c indicates that smoothing may be utilized within each mortality segment to ensure a reasonable relationship exists by attained age within each mortality segment. However, Section 9.C.7.c notes that any use of smoothing should not result in a material change in total expected claims for the mortality segment. Per Section 9.C.2.g, this does not preclude actuarially appropriate adjustments to company experience mortality rates for catastrophic, non-recurring events, even if such adjustments result in a material change in total expected claims.

## Q 15.30: How are mortality assumptions modified for impaired lives?

A: Section 9.C.7.b.vii.e requires adjustments to the mortality assumption for impaired lives if the assumption does not appropriately reflect the expected mortality experience. If the block has an immaterial amount of impaired lives, some actuaries would choose to include the substandard experience in their mortality study, hence developing a combined mortality assumption for the mortality segment. Alternatively, some actuaries exclude the impaired lives from the mortality segment and later include an adjustment for them. This method is described in Section 9.C.2.f. Some actuaries will make this adjustment in the form a percentage or flat addition to standard mortality experience. Where there is sufficient credibility of experience, some actuaries might make a more complex adjustment that changes the shape of the mortality curve.

Where there is a significant amount of substandard business, some actuaries would determine a mortality segment and assumption for substandard business separately (i.e., develop a prudent estimate assumption for mortality specifically for substandard policies).

Section 9.B. 2 requires a larger margin where there is greater uncertainty in the anticipated experience assumption. Therefore, some actuaries also increase the margin on the mortality assumption that applies to impaired lives (in addition to the higher base assumption) because there is more uncertainty regarding the assumption.

## $Q$ 15.31: Is policyholder behavior taken into account in setting the mortality assumption?

A: Actuaries may wish to consider making adjustments for policyholder behavior when the product design leads to potential antiselection from policyholder behavior. This is required by Sections 9.C.2.f and 9.C.7.e if the actuary expects the results to vary due to the behavior. An example of this would be a term product with dramatic increases in tail premiums and the assumption of less than $100 \%$ lapse after the premium increase.

Other areas where an actuary may consider making adjustments due to policyholder behavior include where there is a guaranteed purchase option, guaranteed renewability, or similar features where the mortality expectation of those electing the option would be different than the base assumption.

Whether a company chooses to set its anticipated experience assumptions equal to company experience mortality rates or an applicable industry basic table, Section 9.C.4.c states that the mortality rates from the resulting anticipated experience assumptions must be no lower than the mortality rates that are actually expected to emerge and that the company can justify.

## $Q$ 15.32: Is the use of stochastic mortality allowed under VM-20?

A: VM-20 does not specifically allow the use of stochastic mortality. However, Sections 9.A. 1 and 9.A. 4 imply that assumptions can be stochastically modeled, and if mortality is stochastically modeled, the requirements of Section 9 relating to prudent estimate assumptions are not applicable. Therefore, some actuaries would choose to model mortality stochastically. If the election is made to model mortality stochastically, there is no guidance in VM-20 on how to do this and very little established actuarial practice around stochastic modeling of mortality experience.

$Q$ 15.33: Are there any specific considerations for handling joint life insurance in determining mortality assumptions for the Deterministic Reserve and/or Stochastic Reserve?

A: Actuaries model joint life mortality by applying margins to the individual lives before blending the single life mortality rates. Actuaries will also consider whether to include a contagion assumption in the resulting mortality rate.

## Q 15.34: Is capping allowed in mortality-related calculations?

A: Per Section 9.C.2.g, a ceiling on the amount of insurance for a given policy is not permitted. However, it is also stated that this does not preclude actuarially appropriate adjustments to company experience mortality rates (e.g., in the case of catastrophic, non-recurring events).

Section 9.C.5.a clarifies that the credibility percentage shall be based on uncapped amounts of insurance for both the Limited Fluctuation method and Buhlmann Empirical Bayesian method.

While some companies may cap amounts of insurance in their experience studies for determining anticipated mortality experience to limit large claims volatility, they must use the uncapped insurance amount for each policy when determining credibility.

## Q 15.35: How are mortality rates adjusted when the mortality experience for a mortality segment is worse than the industry basic table for a given mortality segment?

A: Per Section 9.C.3.h, a test should be performed to ensure that the anticipated mortality experience is not worse than the industry table for a given mortality segment. This test is performed by comparing the present value of projected claims using company and industry mortality at the duration that the grading to the industry
table starts. If the test is not met initially, then the industry mortality rates will need to be increased by an appropriate scalar and capped at 1,000 per 1,000, such that the revised comparison of expected claims passes the test.

Both the company experience and industry mortality rates used in this test should be consistent with those used in the Deterministic Reserve mortality assumption.

The language does not specify the discount rate used in the present value calculations, so the actuary may wish to perform the test using a range of rates, including those obtained from their Deterministic and Stochastic Reserve projections.

The language does not state if the mortality rates used in the test should contain the prescribed margins, however the background section of the amendment proposal that led to this requirement implies that the test would be performed using mortality rates prior to the application of margins.

## 16. Setting Premium Assumptions

## Q 16.1: What are some of the general considerations that actuaries may take into account in setting premium assumptions for flexible premium products under VM-20?

A: According to Section 9.A.6.b, for risk factors that do not lend themselves to the use of statistical credibility theory (such as a flexible premium pattern), a company shall establish an anticipated premium assumption in a manner that is consistent with accepted actuarial practice and that reflects any available relevant company experience, any available relevant industry experience, or any other experience data that is available and relevant. In addition to duration, some actuaries vary the premium assumption by one or more of the following factors: product type (e.g., cash-value accumulation products vs. protection-only products), year of issue, issue age, premium funding level, underwriting risk class, distribution channel, and gender.

Note that some actuaries model cash flows in a manner that reflects the actual modal premium distribution using average factors in the aggregate.

Section 9.A.6.d requires that the actuary use sensitivity testing and disclose such analysis to assure that assumptions set using these approaches are set at the conservative end of the plausible range.

## Q 16.2: Are there any other areas where sensitivity testing may be done?

A: According to Section 9.D.4, a company shall, at a minimum, examine the sensitivity of the minimum reserve to changes in premium payment patterns, premium persistency, surrenders, partial withdrawals, allocations between available investment and crediting options, benefit utilization, and other option elections if relevant to the risks in the product. Section 9.D. 4 requires the following sensitivity tests to be performed, at a minimum, for policies that offer policyholders flexibility in the timing and amount of premium payments:

i. Minimum premium scenario;

ii. No further premium payment scenario;

iii. Prepayment of premiums-Single premium scenario; and

iv. Prepayment of premiums-Level premium scenario

For flexible premium products with both primary and secondary guarantees, some actuaries define the above premium payment patterns in light of the primary guarantee, whereas some others would consider them in light of the secondary guarantee. Some actuaries define the premium assumption to encompass both the primary guarantee as well as the secondary guarantee. Some actuaries use the above scenarios to examine the sensitivity of the reserve to the premium payment pattern assumption. If there is uncertainty about the level of future premiums and the reserve is sensitive to the premium payment pattern, then some actuaries would use the sensitivity test results in the determination of the prudent estimate premium assumption. At a minimum, VM-31 requires disclosure of these results.

## $Q$ 16.3: How might the actuary model the four required premium payment pattern sensitivities required by

 Section 9.D.4?A: Some actuaries would interpret these premium sensitivity tests as illustrations of minimum premium patterns that would keep the policies in force until the end of the insurance period (with the exception of ii). Some actuaries would model the minimum premium on a cell-by-cell basis but might combine cells or use a subset of the policies to complete these sensitivities in a timely manner.

## Q 16.4: For dividend-paying business, how would the modeling account for dividends used to reduce premium?

A: It is expected that some actuaries will model based on how policies are actually utilizing dividends to pay premiums by including both the dividend and the implicit premium account. However, it is also likely that some actuaries would model based on a net basis (fixed premium minus dividend used to pay premium) because the cash flow impact is similar. In that circumstance, those actuaries make other adjustments where necessary so that other projected items that are based on premium (e.g., premium taxes) or dividends are captured correctly. Many actuaries also consider how dividends that are used to reduce premiums will impact lapses and other policyholder behavior assumptions. The actuary using the net basis would typically provide additional documentation of the methods and assumptions related to this.

## $Q$ 16.5: Flexible premium products often have minimum required premium payments, excess premium payments, cessation of premium payments, and irregular premium payments. How does one capture this flexibility in the cash flow model if the underlying experience is not fully credible?

A: Section 9.A.6.b discusses risk factors that do not lend themselves to credibility theory, such as flexible premium patterns. Some actuaries would determine the premium assumption on flexible premium policies taking into account how the product was marketed and sold, if such information is available. However, as there is flexibility in payment of premiums, historical payment patterns likely would also be taken into account. Some actuaries would review policy features that would impact premium payments in the future. For example, if a policy has a guarantee that would expire if a specific premium is not paid in a period, then some actuaries would look at historical or expected experience for similar policies with that feature in setting the expected future premium payments.

Additionally, some actuaries model flexible premium products based on how the products are expected to be used by policyholders. For example, one could have a separate assumption for policies expected to be used for accumulation compared to those expected to be used for protection.

## 17. Setting Policyholder Behavior Assumptions Other Than Premiums

## $Q$ 17.1: What policyholder behaviors other than premiums might be considered in the calculation of reserves?

A: Section 9.D.4.a requires sensitivity tests of at least the following policyholder behavior assumptions:

Premium payment patterns, premium persistency, surrenders, partial withdrawals, allocations between available investment and crediting options, benefit utilization, and other option elections that could contain an element of antiselection and are relevant to the risks in the product.

Because sensitivity testing of these behaviors is required, these behaviors will need to be captured in the model or will need to be sensitivity-tested in some other manner.

Some actuaries would also consider the election of dividend, conversion, guaranteed purchase, and

nonforfeiture options to the extent these options are relevant to the risks in the product and are material. Note that the standard for identifying material risks depends on their impact and relative size as compared to the Net Premium Reserve, Deterministic Reserve, and Stochastic Reserve rather than the total company reserve, see Section 2.H in VM-20 for additional context.

Alternatively, risks that do not contain elements of anti-selection are not considered as relevant policyholder behavior for determining the Deterministic and Stochastic Reserves. Some examples of these risks include modeling the exercising of contractual rights to decrease and/or increase face amount (subject to evidence) or to change UL death benefit options.

Section 7.F.3.b provides guidance on how to model policy loan behavior when policy loans are modeled explicitly, but explicit modeling of policy loans is not mandatory. However, the requirements in Section 7.F.3.a must be met if policy loans are not explicitly modeled. In this case, the reserves can't be less than those produced when modeling loans explicitly and policyholder behavior must comply with Section 9.D.

## $Q$ 17.2: When are dynamic policyholder behavior assumptions used?

A: Section 9.D.2.a requires that the company shall use a dynamic model or other scenario-dependent formulation to determine anticipated policyholder behavior unless the behavior can be appropriately represented by static assumptions. No guidance is given as to how to determine when an assumption can be represented "appropriately" by static assumptions. Most actuaries document the rationale for using static assumptions if static assumptions are used in place of dynamic policyholder behavior.

Some actuaries use dynamic policyholder behavior assumptions in instances where an external environment or actions of the company, which can be reflected in the model, affect policyholder behavior.

Some examples the actuary may wish to consider include, but are not limited to, the following:

- If a company raises non-guaranteed premiums or cost of insurance rates, more policyholders could surrender / lapse / convert (especially the healthy lives), which could worsen the overall mortality of the remaining lives.
- Under decreasing- / low-interest scenarios, the guarantees may become attractive, possibly leading to lower lapses or additional premium payments or exercise of guaranteed settlement options.
- Reductions to interest crediting rates or dividend scales may lead to additional lapses or premiums for certain specific policy forms, such as those with premium expectations based on higher illustrated interest rate or dividend levels.
- For interest-sensitive products, when interest rate change (in particular, under increasing-interest scenarios), the assumption of how credited rates are set (i.e., how fast they increase) might be assumed to affect the lapse assumption, which may affect other assumptions such as mortality and premiums.
- For policies with secondary guarantees, lapses might be modeled to significantly decrease when the guarantee is in the money. Section 9.D.5 of VM-20 gives specific guidance on this topic.


## $Q$ 17.3: Are there specific considerations in setting margins on assumptions for policyholder behavior?

A: Section 9.D. 3 states that to the extent that there is an absence of relevant and fully credible data, the company shall determine the margin such that the policyholder behavior assumption is shifted toward the conservative end of the plausible range of behavior, which is the end of the range that serves to increase the reserve. Margins should reflect an increase in policyholder efficiency over time, unless the company has relevant and credible experience or clear evidence to the contrary. Also, the margin for surrender or partial withdrawal should be higher in the case where the company's marketing or administrative practices encourage antiselection. Note, the company must reflect the data uncertainty when using assumptions from similar but not identical blocks of business.

Given the level of uncertainty in the estimation of policyholder behavior, especially when there are valuable contract options, some actuaries would increase margins for these risk factors as compared to risk factors where fewer policyholder options exist. Some actuaries would look to the credibility of experience data in setting the margins around this assumption using the considerations summarized above.

## $Q$ 17.4: How would the actuary reflect nonforfeiture options in the cash flow projections?

A: Some actuaries would assume that all nonforfeiture benefits are cash surrenders. If various nonforfeiture options are not equivalent, then some actuaries might use the greatest of the values of the nonforfeiture options similar to the taking the highest value under the Commissioner's Annuity Reserve Valuation Methodology. Other actuaries would model a nonforfeiture option cost that is consistent with an expected level of nonforfeiture option utilizations.

Another approach may be to project the cash flows under the various nonforfeiture paths with expected election rates that vary by path.

## $Q$ 17.5: How are dividend options considered in performing the VM-20 projections?

A: Some actuaries model dividend options explicitly in the cash flow projections, especially if the election of particular dividend options is integral to how a policy was marketed and sold. This would include dividends used to pay premiums and the purchase of paid-up additions or one-year term. Alternatively, when the minimum reserve is not materially affected by the choice of dividend options, some actuaries adopt a more simplified approach, such as modeling all dividends as paid in cash.

Section 7.C. 6 discusses the liability for dividends declared but not yet paid as of the valuation date. It states that this liability may or may not be included in the Cash Flow model at the company's discretion. According to statutory accounting principles, dividends are reported separately from the statutory reserve. Therefore, if
the policyholder dividends that give rise to the dividend liability are not included in the cash flow model, then no adjustment is needed to the resulting aggregate modeled (whether deterministic or stochastic) reserve. If the policyholder dividends that give rise to the dividend liability are included in the cash flow model, then the resulting aggregate modeled (whether stochastic or deterministic) reserve should be reduced by the amount of the dividend liability.

## $Q$ 17.6: How might policyholder behavior assumptions differ between the various exclusion tests and projections required under VM-20?

A: Some actuaries would conclude that the Deterministic Reserve and Stochastic Reserve calculations as well as the Stochastic Exclusion Ratio Test use the same assumptions, except that margins are not included in the Stochastic Exclusion Ratio Test per Section 6.A.2.b.i.a.1, and prudent estimate assumptions will vary dynamically for the 16 scenarios to reflect scenario-dependent risks.

If the qualified actuary chooses to pass the Stochastic Exclusion Test by certifying that a group of policies are not subject to material interest rate or asset return volatility risk, then different assumptions may be used, for example results of the New York seven scenarios from cashflow testing, as opposed to the 16 scenarios from Appendix 1.

Per section 6.B.5, for the Deterministic Exclusion Test, if the Net Premium Reserve follows Section 3.A.1, then the lapse rates are $0 \%$ when calculating the valuation premiums for this comparison. Per Section 6.B.5.d, if the anticipated mortality exceeds the valuation mortality, then the anticipated mortality will be used to calculate the net valuation premium.

In the case of policies issued on a substandard basis, the CSO mortality rates used in the Net Premium Reserve (NPR) must reflect the substandard rating, subject to a cap that ensures mortality rates do not exceed 1000 per 1000 . As an alternative, the substandard mortality extra may be reserved for separately as a Miscellaneous Reserve under Exhibit 5 for groups of policies where the NPR dominates the Deterministic Reserve and Stochastic Reserve. This could eliminate the impact of a substandard rating on the exclusion tests.

## $Q$ 17.7: How are policyholder options such as term conversion options and guaranteed purchase options be treated in determining reserves?

A: Section 9.D.1.e states that the actuary must reflect the likelihood that policyholder behavior will be affected by any significant increase in the value of a product option, such as term conversion privileges or policy loans.

Some actuaries will take into account the potential exercise of policyholder options in their policyholder behavior assumptions for those options that have value. However, some actuaries would use a simplified model for companies where the impact of term conversions and exercise of the guaranteed purchase options is not material.

Section 2.G indicates that:

A company may use simplifications, approximations and modeling efficiency techniques to calculate the Net Premium Reserve, the Deterministic Reserve and/or the Stochastic Reserve required by this section if the company can demonstrate that the use of such techniques does not understate the reserve
by a material amount and the expected value of the reserve calculated using simplifications, approximations and modeling efficiency techniques is not less than the expected value of the reserve calculated that does not use them.

For companies for which term conversions are significant, some actuaries would include additional decrements in the term line to take into account policies converting to whole life policies. The impact (i.e., additional cash flows from the conversion or purchase) would be included in the cash flow projection to take into account the impact of the policies converting. Some actuaries would reflect this impact using a "cost of conversion or purchase" charge or credit from studies on the cost of term conversions.

The cost / credit of conversion or purchase could be determined by projecting some typical post-conversion or -issue policies using appropriate prudent estimate assumptions and including this cost / credit at the point of conversion or purchase. Some actuaries reflect the potential of mortality antiselection and other optionspecific behavior.

Some actuaries consider the impact from more than one possible post-conversion product type. Term policies converting to newer products such as a universal life with secondary guarantees could theoretically generate a significantly different cost of conversion or purchase than those converting to a traditional whole life product.

Some actuaries include a separate reserve for projected new policies arising from term conversions with their own respective cash flow projections as a Miscellaneous Reserve in Exhibit 5., This would avoid the complexities of modeling the new policies that convert from term to whole life separately in the "All OtherVM-20 Reserving Category" independent from their originating “Term Reserving Category”. Other actuaries might include the present value of the cost / credit of conversion in conjunction with the election rate in the term projection to affect the cash flows at the time of the expected election of an option.

## $Q$ 17.8: Could the existence of a guaranteed purchase option lead to a reduction in the VM-20 reserves?

A: Yes. A guaranteed purchase option is simply a charge being made for a potential future exercise of the purchase of additional insurance. Prior to the exercise of any remaining future options, the impact to reserves would be negative if the actuary projects (using Prudent Estimate Assumptions, including any applicable antiselection and margins) that the present value of expected profits from future exercised policies plus the present value of guaranteed purchase option premiums less guaranteed purchase option commissions and guaranteed purchase option expenses is greater than zero.

## $Q$ 17.9: What are some things actuaries consider for policies that have already converted?

A: Some actuaries model policies based on the status of the policy on the valuation date. However, other actuaries take into account expected future experience that may be based on a policy coming into its current status from another policy type. When considering conversion options, some actuaries will reflect expected mortality antiselection arising from converted term policies, either explicitly for these policies, or as part of the aggregate experience for the block.

## $Q$ 17.10: Are there any additional considerations related to policyholder behavior assumptions for term policies with premium increases after the end of the level term period?

A: Section 9.D. 6 provides guidance on the treatment of policyholder behavior assumptions in calculating the reserves for term policies with material premium increases at the end of the level term period.

For the calculation of the Stochastic Reserve for a term life policy subject to Section 9.D.6.a and for the calculation of the Deterministic Reserve and the Stochastic Reserve for a term policy issued before Jan. 1, 2017 valued using Actuarial Guideline XXXVIII in which level or near level premiums are guaranteed or expected for a specified duration followed by a substantial premium increase, for the period following that substantial premium increase, the lapse and mortality assumptions shall be adjusted or margins added such that the policy's present value of cash inflows in excess of cash outflows assumed shall be limited to reflect the relevance and credibility of the experience, approaching zero for periods where the underlying data has low or no credibility or relevance.

In other words, in this situation, Section 9.D. 6 requires that the calculation of the Deterministic Reserve not include any post-level term period positive net cash flows.

Note that a seriatim comparison of the present value of post-level term cash inflows and outflows must be performed. For policies subject to Section 9.D.6.a, the $100 \%$ lapse rate assumption at the end of the level term period applies only to those policies with post-level term profits. Similarly, for policies subject to Section 9.D.6.b, adjustments to limit post-level term profits must be made at a seriatim level, and post-level term losses must be reflected in the reserve calculations.

## 18. Setting Expense Assumptions

## $Q$ 18.1: What types of expenses are included in the models for determining reserves?

A: Section 7.B.1.e provides that all types of expenses-including but not limited to overhead expenses, commissions, fund expenses, contractual fees and charges, and taxes (excluding federal income taxes and expenses paid to provide fraternal benefits in lieu of federal income taxes)—be reflected in the modeling. Per Section 7.H.2.c.i, investment expenses are considered as a part of the net asset earned rate calculation. Some actuaries consider ASOP No. 2, Nonguaranteed Charges or Benefits for Life Insurance Policies and Annuity Contracts, and ASOP No. 7, Analysis of Life, Health, or Property/Casualty Insurer Cash Flows, when determining the expenses included in the projections where it is not specifically addressed in VM-20. Specific guidance is provided in Section 7.H.2 for reflecting investment expenses and in Section 9.G for expenses (and expense reimbursements) related to revenue-sharing agreements.

Section 9.E.1.c requires prudent estimate expense assumptions to assume that the company is a going concern.

## $Q$ 18.2: Must acquisition expenses be included?

A: Per Section 9.E.1.m, acquisition costs associated with the business in force as of the valuation date and significant nonrecurring expenses that are expected to be incurred after the valuation date shall be included in the reserve calculation.

## $Q$ 18.3: How are overhead expenses reflected and allocated in the calculation?

A: Per Section 9.E.1.l, an appropriate portion of indirect costs and overhead expenses should be included along with other expenses consistent with the block of policies being modeled.

Some actuaries would use the company's practices of expense allocation among lines of business if it includes overhead expenses and is reasonable for the specific cohorts of business in scope for VM-20. Some actuaries develop an allocation specifically for reserve modeling that might be based on pricing or the Illustration Actuary methodology.

Section 9.E.1.j states that allocations must be determined in a manner that is within the range of actuarial practice and methodology and consistent with applicable actuarial standards of practice and may not be done for the purpose of decreasing the modeled reserve.

## $Q$ 18.4: How is inflation be reflected?

A: Section 9.E.1.e requires that expense assumptions reflect the impact of inflation, and Section 9.E.1.a states that expense assumptions for the stochastic scenarios may differ from expense assumptions for the deterministic scenario due to the application of inflation rates. Some actuaries would thus make an assumption for inflation that is related to the scenarios being modeled. One way to do this is to base the rate of inflation on the interest rate scenario being projected, such as assuming a base real rate of return with some portion of the additional amount assumed to be inflation. Some actuaries model inflation separately.

## Q 18.5: What future improvements in expenses may be included?

A: Under Section 9.E.1.f, prudent estimate expense assumptions may not assume future expense improvements. However, according to Section 9.E.1.k, expense efficiencies that are derived and realized from the combination of blocks of business only can be assumed when the costs of achieving these efficiencies are also recognized.

## $Q$ 18.6: How is federal income taxes reflected in the calculation?

A: Section 9.E.1.g, the following shall not be included in the calculation:

- federal income taxes;
- expenses paid to provide fraternal benefits in lieu of income taxes; and
- foreign income taxes.

$Q$ 18.7: How would expense assumptions be set for new products or new lines of business where there is no experience within the company?

A: Section 9.E.1.n provides that the company should review expense factors used to determine anticipated experience for an existing block of mature policies and adjust those factors for any differences in long-term expense factors that would be expected between the new product and existing mature block of business, taking steps to ensure that all expenses are fully allocated.

Some actuaries would look to pricing assumptions; expense experience for other similar products within the company; or to studies done by industry groups, reinsurers, or consultants for similar products to adjust the anticipated experience assumption. Some actuaries would increase the margin on this assumption compared to other expense assumptions to reflect the greater uncertainty in the anticipated experience assumption.

## $Q$ 18.8: How would the actuary set margins for an expense assumption?

A: A process that some actuaries might use would be to review the historical experience data (for example, unit costs for the last five years) for the line of business or relevant block. Assuming the actuary is comfortable that the level of expenses will not significantly increase or decrease in the future, the actuary would then determine what type of modification to this assumption would increase the reserve (likely an increase to expenses). Then, taking into account the criteria above for determining margins, including the uncertainty, credibility, quality of experience data, and the level of the anticipated experience assumption relative to the historical values, the actuary would develop a range of potential outcomes for future expenses. This range could vary by duration with a tighter range expected in the next few projection years and a wider range further out in the projection. The margin would be set so that in the actuary's judgment, the range of the prudent estimate assumption includes the potential deviations from the anticipated experience in a manner consistently conservative as the CTE requirement for the entire reserve. See Section 9.B for general guidance on assumption margins.

## $Q$ 18.9: How is capital expenditures, such as technology investment costs, considered in the expense assumptions?

A. Section 9.E.1.b and the subsequent Guidance Note provide that certain capital expenditures may be spread over a reasonable number of years in accordance with statutory accounting principles as defined in the Statements of Statutory Accounting Principles but that care should be taken with regard to the potential interaction with other assumptions.

## $Q$ 18.10: Can expenses for items like death claim processing and loan processing be included with maintenance expenses?

A. Section 9.E.1.d states that an actuary shall choose an appropriate expense basis that properly aligns an expense with the assumption. For example, the Guidance Note states that the expense assumption for handling death benefit payments should be allocated per death incurred. Section 9.E.1.d also states that costs that are not significant can be aggregated into another base assumption. The actuary would use judgment to decide which assumptions can be aggregated and which would be separated.

## 19. Setting Non-Guaranteed Element Assumptions

## Q 19.1: What are non-guaranteed Elements ("NGEs") and how should they be included in the models under VM-20?

A: Non-guaranteed elements ("NGEs”), as defined in VM-01, refer to charges or credits to a policyholder's account value, benefit, premium, or consideration that are both established and which may be adjusted at the discretion of an insurance company. NGEs include, for example, policyholder dividends for participating policies, and participation rates and asset fee charges for equity-indexed universal life policies. Section 7.C provides guidance on how NGEs should be modeled. In addition, Section 8.C.7 outlines items that companies should include in setting assumptions for the NGE in reinsurance cash flows. Section 8.C.8 provides that certain actions under reinsurance agreements may be thought of as comparable to NGEs.

$Q$ 19.2: Can the actuary modify (up or down) the assumed NGEs scale or spread in response to the experience unfolding in the scenario?

A: Section 7.C. 3 and 7.C. 4 indicate that projected levels of NGEs in the cash flow model must be consistent with how actual NGEs are determined (7.C.3) and consistent with the experience assumptions used in each scenario (7.C.4). Policyholder behavior assumptions in the model must be consistent with the NGE assumed in the model.

$Q$ 19.3: What are some of the factors that are considered when deciding to include NGE in reserves covered by VM-20?

A: According to Section 7.C.2, the projected NGE shall reflect factors that include, but are not limited to, the following:

- The nature of the contractual guarantees;
- The company's past NGE practices and policies;
- The timing of any change in NGE relative to the date of recognition of a change in experience; and
- The benefits and risks to the company of continuing to authorize the NGE.

$Q$ 19.4: When determining the NGE assumptions for each scenario, what considerations might the actuary take into account when modifying the current NGE scale or spread?

A: Examples of considerations about NGEs include:

- Existence of contract guarantees;
- The company's ability to modify its non-guaranteed dividend scale and/or non-guaranteed elements on items such as credited rates, expense charges, COIs, etc.;
- Effect on policyholder behavior of maintaining the current non-guaranteed dividend scale and/or nonguaranteed elements under the scenario;
- Effect of the NGE assumptions on the competitive position of the product under the scenario;
- The extent to which a change in experience is recognized in the non-guaranteed dividend scale or nonguaranteed elements;
- The timing lag from when a change in experience occurs to when it is recognized in the nonguaranteed dividend scale or non-guaranteed elements; and
- Management philosophy.


## $Q$ 19.5: What adjustments to the model can be made to take into account lags in the changing of NGEs?

A: Some actuaries may find it difficult to model lags in changing NGEs in these calculations. One technique that some actuaries use is to assume that NGEs are determined based on last year's values, or the last period if quarterly or monthly time steps are used in the model. Some actuaries would consider whether the modeled timing of changes to NGEs materially distorts the minimum reserve.

$Q$ 19.6: Can the actuary just review the NGE impact for the tail scenarios, because those scenarios are the only ones that go into the Stochastic Reserve calculation?

A: Some actuaries would pay particular attention to how the model assumes NGEs are modified as the market conditions change across all scenarios. This would include scenarios outside of the tail scenarios where NGEs play a significant part in risk mitigation because an error or misstatement in one of those scenarios could lead to that scenario (that was not previously in the tail) now becoming part of the tail. This is particularly true for blocks where changes to NGEs are likely to have a significant impact on calculation of reserves.

## $Q$ 19.7: Will actuaries assume the prudent estimate assumptions or anticipated experience assumptions actually occur when projecting the NGEs as part of VM-20?

A: Section 7.C. 4 states that projected levels of NGEs in the cash flow model must be consistent with the experience assumptions used in each scenario. Some actuaries interpret this to imply the NGEs be established based on the prudent estimate assumption set.

Like all other assumptions, VM-20 requires that the NGEs include a margin. Hence, some actuaries will not assume that the company will fully reflect the projected experience in the model, because doing so could eliminate the margin built into the prudent estimate assumption. As an example, if future policyholder dividends are reduced to exactly offset the projected higher claims due to the margin in the mortality assumption, the mortality margin is essentially eliminated. Some actuaries will delay the timing of when the dividend scale changes are implemented in the model as the NGE margin. Other actuaries will not fully reflect the needed dividend scale change in future dividends as the NGE margin.

## $Q$ 19.8: Are there situations where an NGE may be excluded in the determination of the Deterministic or Stochastic Reserves?

A: According to Section 7.C.5, the actuary may exclude any portion of the NGE that:

- is not based on some aspect of the policy's or contract's experience; and
- is authorized by the board of directors and documented in the board's minutes where the documentation includes the amount of NGE that arises from other sources.

However, if the board has guaranteed a portion of the NGE into the future, the company must model that amount (unless excluded by Section 7.C.6, which discusses policyholder dividends declared but not yet paid).

Some actuaries believe that, if the board has identified a distribution to policyholders like a special dividend, (e.g., arising from a sale of a company or block of business unrelated to the specific block of business) but that special dividend is not guaranteed, then the language in Section 7.C. 6 would allow them to exclude it from the model.

## $Q$ 19.9: Are dividends declared but not yet paid allowed to be included in the cash flow model?

## A: This topic is covered in Section 7.C.6.

Some actuaries do not model payment of dividends declared but not yet paid to the extent a separate dividend liability exists as required by statutory accounting principles. Doing so would have the dividends captured in both the dividend liability reserve and the Deterministic or Stochastic Reserve.

Some actuaries include all dividend payments due to system constraints, or in recognition of second-order impacts, and then remove the declared but unpaid dividends via a top-side adjustment, such as subtracting the dividend liability from the Deterministic or Stochastic Reserve.

## 20. Treatment of Reinsurance

## $Q$ 20.1: When would the actuary include a reinsurance agreement in the calculation?

A: Section 8.A. 3 states that a company shall include a reinsurance agreement in calculating the minimum reserve if under the terms of the Accounting Practices and Procedures Manual the agreement or amendment qualifies for credit for reinsurance.

Section 8.A. 4 and the accompanying Guidance Note state that if a reinsurance agreement or amendment does not qualify for credit for reinsurance, but treating the reinsurance agreement or amendment as if it did so qualify would result in a reduction to the company's surplus, then the company shall increase the minimum reserve by the absolute value of such reductions in surplus.

Some actuaries would include a reinsurance agreement that has an effective date after the valuation date in the future valuation cash flows if the treaty had been signed by both parties on or prior to the valuation date and it qualifies for reinsurance credit under the terms of the Accounting Practices and Procedures Manual.

$Q$ 20.2: Can the actuary rely on calculations performed by the other party to the reinsurance transaction?

A: The Guidance Note in Section 8.A. 1 states that an actuary can rely on calculations performed by the other party, but the reserve calculation must be rerun, or appropriate adjustments must be made if different assumptions are chosen.

When relying on another actuary's calculations, many actuaries consider whether the margins set by the other party satisfy the requirement that margins are conservative with respect to their reserve amount. The margins from the other party's perspective may not necessarily meet that requirement.

$Q$ 20.3: How is reinsurance reflected in the Net Premium Reserve?

A: Section 8.B. 1 states the determination of a credit to the Net Premium Reserve to reflect reinsurance ceded is done in accordance with SSAP No. 61R. Some actuaries would perform this calculation for each policy and then aggregate based on Section 8.B.3.

$Q$ 20.4: How is the reinsurance credit for the Net Premium Reserve calculated when a company cedes a portion of the policy under multiple reinsurance agreements?

A: Section 8.B. 2 states that if a company cedes a portion of a policy under more than one reinsurance agreement, then the company shall calculate a credit separately for each such agreement. The credit for reinsurance ceded for the policy shall be the sum of the credits for all such agreements.

Q 20.5: When calculating the ratio for the Stochastic Exclusion Ratio Test (SERT), the company can get a dramatically different result before reinsurance and after reinsurance when the reinsurance is nonproportional (e.g., YRT mortality risk reinsurance). What approach are companies taking to properly reflect non-proportional reinsurance in the SERT calculation?

A: The Stochastic Exclusion Ratio Test (SERT) is defined as: SERT $=(b-a) / c$

Where:
$\mathrm{a}=$ the adjusted Deterministic Reserve described in Section 6.A.2.b.i using the baseline economic scenario described in VM-20 Appendix 1.

$\mathrm{b}=$ the largest adjusted Deterministic Reserve described in Section 6.A.2.b.i under any of the other 15 economic scenarios described in VM-20 Appendix 1.

$\mathrm{c}=$ an amount calculated from the baseline economic scenario described in Appendix 1 that represents the present value of benefits for the policies, adjusted for reinsurance by subtracting ceded benefits.

If SERT $<0.060$, SERT is "Passed."

In many, but not all cases, quota-share coinsurance scales "b," "a," and "c" roughly in proportion to 1- QS\%, leaving the SERT result similar both pre- and post-quota share coinsurance.

However, under non-proportional reinsurance, "a" is likely to be of similar magnitude pre- and postreinsurance, as is "b," but "c" will be reduced by the ceded mortality benefits. As a result, the SERT ratio post-YRT reinsurance is likely to be larger than pre-YRT reinsurance-perhaps significantly so, if a large percentage of the mortality risk is ceded out. The SERT may "Fail" simply because of the YRT cession, even though actual reserves, and reserve sensitivity to yield rates, might be similar pre- and post-YRT reinsurance.

If a reserve calculation segment passes SERT pre-YRT reinsurance but fails SERT post-YRT reinsurance, some actuaries attempt to demonstrate that sensitivity of the adjusted Deterministic Reserve to economic scenarios is comparable pre- and post-YRT and thus argue that the SERT result should be determined to be a "Pass" both pre-YRT reinsurance and post-YRT reinsurance. One form of such a demonstration that some actuaries use is as follows (and is found in Section 6.A.2.c.i).

For convenience in notation, call the pre-YRT reinsurance results "gross of YRT," with a subscript "gy," and the post-YRT results "net of YRT," with subscript "ny." If a block of business being tested is subject to one or more YRT reinsurance cessions as well as other forms of reinsurance, such as coinsurance, take "gross of YRT" to mean net of all non-YRT reinsurance but ignoring the YRT contract(s), and "net of YRT" to mean net of all reinsurance contracts. That is, treat YRT reinsurance as the last reinsurance in, and compute certain values below with and without that last component.

So, if we have

$\mathrm{SERT}_{\text {gy }} \leq 0.060$ but $\mathrm{SERT}_{\mathrm{ny}}>0.060$, then move to a second-stage test as follows:

Compute the Largest Percent Increase in Reserve = LPIR = $(b-a) / a$, both "gross of YRT" and "net of YRT."

$\operatorname{LPIR}_{\mathrm{gy}}=\left(\mathrm{b}_{\mathrm{gy}}-\mathrm{agy}_{\mathrm{gy}}\right) / \mathrm{ag}_{\mathrm{gy}}$

$\operatorname{LPIR}_{\mathrm{ny}}=\left(\mathrm{b}_{\mathrm{ny}}-\mathrm{a}_{\mathrm{ny}}\right) / \mathrm{a}_{\mathrm{ny}}$

If SERT ${ }_{\text {gy }} \times \mathrm{LPIR}_{\mathrm{ny}} / \mathrm{LPIR}_{\mathrm{gy}}<0.060$, then declare the Stochastic Exclusion Ratio Test result to be a "Pass" on the post-reinsurance basis.

Note that the scenario underlying $b_{g y}$ could be different than the scenario underlying $b_{n y}$.

For quota-share coinsurance and non-proportional reinsurance arrangements some actuaries might consider another more qualitative demonstration as provided in Section 6.A.2.c.ii. This qualitative approach is to
calculate the adjusted Deterministic Reserves for the 16 scenarios of the Stochastic Exclusion Ratio Test both gross and net. Array the results in table and chart, demonstrating a similar pattern of sensitivity by scenario.

## Q20.6: For non-guaranteed YRT reinsurance ceded or assumed, how are Reinsurance Cash Flows in the Deterministic Reserve and Stochastic Reserve reflected?

A: For policies issued on or after 1/1/2020, and optionally for policies issued on or after 1/1/2017 and before 1/1/2020 non-guaranteed YRT reinsurance ceded or assumed do not need to be modeled for purposes of applying Sections 8.C.1 through 8.C.14. It should be noted that this treatment of YRT is intended to be an interim solution that will be replaced by a longer term solution once regulators and the industry have had more time to evaluate a variety of approaches.

Drafters Note: There are currently three potential solutions to modeling YRT reinsurance being considered by regulators. Currently, a field study is being performed by a collaboration of industry members and regulators led by the American Academy of Actuaries to help regulators understand these solutions. Each are in the form of an Amendment Proposal Form (APF) suggesting how the Valuation Manual would be amended to accommodate the particular solution. As the results from the field study are finalized, revisions may be made to the APFs. The intention is for revised APFs to be exposed by the NAIC regulators in May 2020 with regulators selecting the most appropriate APF by June 2020. The NAIC adoption of the selected method is planned for August 2020 for use in 2021 and later editions of the Valuation Manual. The Valuation Manual and related tables and documents are published under the Industry tab on the NAIC website home page (www.naic.org).

Q20.7: Do the assumptions used by both the assuming and ceding company have to be the same for a specific block of business subject to a reinsurance agreement?

A: Section 8.C. 1 of VM-20 states that the ceding and assuming companies are not required to use the same assumptions and margins for the reinsured policies.

$Q$ 20.8: How might non-proportional reinsurance (e.g., YRT, stop loss, or limits on benefits receivable) be reflected in the cash flow projections used to determine the Deterministic and Stochastic Reserves?

A: Some actuaries would not include non-proportional reinsurance ceded benefits in the cash flows if such benefits are immaterial.

Some actuaries would include non-proportional reinsurance cash flows in the projections directly where possible (e.g., YRT).

Other actuaries will perform separate stochastic analysis as discussed in Section 8.C.2.b to quantify the impact where a single deterministic valuation assumption for a risk factor will not adequately capture the risk (e.g., mortality on a stop-loss reinsurance agreement). Some actuaries would consider stochastic analysis to be essential for assumed non-proportional reinsurance.

$Q$ 20.9: What does VM-20 mean by treating counterparties to a reinsurance treaty as "knowledgeable counterparties"?

A: Section 8.C. 7 addresses knowledgeable counterparties in the following way:

Assume that the counterparties to a reinsurance agreement are knowledgeable about the contingencies involved in the agreement and thus likely to exercise the terms of the agreement to their respective advantage, taking into account the context of the agreement in the entire economic relationship between the parties. In setting assumptions for the non-guaranteed elements in reinsurance cash flows, the company shall include, but not be limited to the following:

- The usual and customary practices associated with such agreements.
- Past practices by the parties concerning the changing of terms, in an economic environment similar to that projected.
- Any limits placed upon either party's ability to exercise contractual options in the reinsurance agreement.
- The ability of the direct-writing company to modify the terms of its policies in response to changes in reinsurance terms.
- Actions that might be taken by a party if the counterparty is in financial difficulty.


## $Q$ 20.10: Will actuaries assume 100 percent selection against the company by knowledgeable counterparties in all instances?

A: Some actuaries set assumptions for non-guaranteed elements in reinsurance agreements taking into account expected experience based on their actuarial judgment informed by historical experience.

Some actuaries assume less than 100 percent selection against the company, but these actuaries consider the financial impacts to the counterparty when setting these assumptions, including, for example:

- The estimated level of profit being earned (or losses experienced) on the reinsurance agreement in the year of the setting of any non-guaranteed element;
- The dollar amount of cumulative losses assumed not to be passed on through increased reinsurance costs; and
- Expected future profitability of the agreement with a higher likelihood of changes in any nonguaranteed elements by the counterparty if the future profitability is low or negative.

Some actuaries assume significantly higher likelihood of selection against the company if the financial impact to the counterparty is significant.

Sections 8.C. 11 through 8.C. 17 provide specific considerations for setting these assumptions.

## $Q$ 20.11: How are assets that support the reserve modeled when held by another party?

A: Section 8.C. 14 provides considerations for when these assets should be modeled and how it must be done.

## $Q$ 20.12: How does the actuary reflect the creditworthiness of a reinsurance counterparty?

A: Sections 8.C. 15 and 8.C. 16 require a margin for the risk of default to be included when the one party has knowledge that the other party is financially impaired. However, if there is no known financial impairment, then there is no requirement to establish a margin for the risk of default.

Industry practice regarding the definition of financial impairment is expected to develop over time.

$Q$ 20.13: How is creditworthiness of the ceding company modeled if on assumed business the assuming company may terminate the reinsurance upon nonpayment by the ceding company?

A: Section 8.C. 16 states that the margin for default risk otherwise established for the risk of default may be reduced or eliminated in this circumstance.

## $Q$ 20.14: Is there a difference in the modeling or reporting of authorized versus unauthorized reinsurers?

A: Section 8.C. 17 requires the actuary to take into account the ratings, risk-based capital ratio, or other available information related to the probability of the risk of default of any counterparty. Only if there were some difference in the probability of the risk of default would there be a difference in the modeling.

## $Q$ 20.15: How is the reinsurance reserve credit determined for the DR and SR?

A: Per Section 8.C.18, for policies issued on or after 1/1/2020, and optionally for policies issued on or after $1 / 1 / 2017$ and before $1 / 1 / 2020$, when the reinsurance ceded or assumed is on a non-guaranteed YRT or similar basis, the post-reinsurance-ceded DR or SR shall be the pre-reinsurance-ceded DR or SR pursuant to Section 8.D. 2 plus any applicable provision pursuant to Section 8.C. 15 and Section 8.C.17, minus the NPR reinsurance credit from Section 8.B.

Per Section 8.D, the reinsurance reserve credit is the excess of the pre-reinsurance-ceded minimum reserve over the post-reinsurance-ceded minimum reserve.

## $Q$ 20.16: How is the pre-reinsurance-ceded reserve determined?

A: Section 8.D. 1 requires the minimum reserve be recalculated, ignoring the impact of any reinsurance ceded.

Section 3.E states that the policy minimum Net Premium Reserve is defined to be the policy Net Premium Reserve determined in sections 3.A through Section 3.D, less a credit for reinsurance ceded as defined in Section 8. The Deterministic and Stochastic pre-reinsurance-ceded reserves are determined by excluding all of the ceded reinsurance cash flows. Section 8.D.2.a requires the Stochastic Exclusion Test and Deterministic Exclusion Test to be performed, ignoring ceded reinsurance.

Section 8.D.2.b allows the actuary to adjust assumptions to reflect company experience in the absence of reinsurance such as assuming, for example, that the business was managed in a manner consistent with the manner that retained business is managed. Some actuaries believe this would include assumptions regarding asset modeling for the assets backing reserves no longer ceded unless directly addressed in VM-20. Some actuaries would do this by grossing up the existing asset models.

$Q$ 20.17: For policies issued on or after $1 / 1 / 2017$ and before 1/1/2020, if a company opts to model a nonguaranteed YRT reinsurance treaty, how does it model reinsurance rates when calculating reserves based on prudent estimate mortality?

A: For reinsurance-ceded cash flows, the direct company must determine the appropriate assumption for the reinsurance premium rates when projected mortality is based on a prudent estimate. The reinsurer likely did
not establish its premiums using VM-20 prudent estimate mortality. If the treaty allows for premiums or expense allowances to be adjusted and modeled reinsurance premiums are not adjusted, the modeled reinsurance cash flows may be less of a net cost and potentially a net benefit to the ceding company. Some actuaries would consider the following sections of VM-20 as relevant to this issue.

- Section 8.C. 10 requires the company to use assumptions that account for any actions that the assuming company (the reinsurer) has taken or is likely to take. This requirement is followed by a Guidance Note that puts reinsurance premiums and expense allowances in the category of assumptions that qualify for this treatment.
- Assuming the reinsurer can contractually change premiums or expense allowances, then Section 8.C. 11 requires the company to treat reinsurance premiums and expense allowances as similar to nonguaranteed elements and subject to the requirements in Section 7.C (non-guaranteed elements section). Within Section 7.C, one of the requirements (7.C.4) is to project NGEs in the cash flow model consistent with the experience assumptions used in each scenario. Some actuaries interpret this language to imply that the modeled reinsurance premiums be consistent with the modeled mortality assumption, potentially with a timing lag consistent with similar NGE management lags.

Section 8.C. 1 requires the company to use assumptions and margins appropriate for each reinsurance agreement. There are no specific Guidance Notes, practice notes, or established practice to draw upon that indicate how such margins are applied to reinsurance premiums, particularly after consideration for the NGE nature of the reinsurance premiums. If the reinsurance premiums have already been modified to align with the prudent estimate mortality such that the modeled reinsurance cash flows are reflecting an ultimate net cost in the model similar to the net cost the company expects to actually emerge, some actuaries consider this to be sufficient. It is not clear in reading VM-20 whether the regulators expect a separate margin to be added to the now-adjusted reinsurance gross premiums. If so, then this additional margin layer would further increase the net cost of reinsurance in the model.

## 21. Treatment of Hedging / Derivative Programs

## $Q$ 21.1: Do the terms "derivative instrument," "derivative program," and "hedging program" all mean the same thing as used in VM-20?

A: These terms do not have similar meanings. The terms "derivative instrument" and "derivative program" are defined in VM-01.

The term "derivative instrument" includes, but is not limited to, an option, warrant, cap, floor, collar, swap, forward, or future, or any other agreement or instrument substantially similar thereto or any series or combination thereof. Each derivative instrument shall be viewed as part of a specific derivative program.

The term "derivative program” means a program to buy or sell one or more derivative instruments or open or close hedging positions to achieve a specific objective, and includes both hedging programs (derivative programs used to reduce risk) and non-hedging programs (derivative programs used for replication or income generation objectives).

$Q$ 21.2: Are there limitations on including the impact of derivative programs in the minimum reserve calculation?

A: Section 7.K.1 of VM-20, "Modeling of Derivative Programs," states that when determining the Deterministic Reserve and the Stochastic Reserve, the company shall include in the projections (i) the appropriate costs and benefits of derivative instruments that are currently held by the company in support of the policies in the calculation; (ii) the appropriate costs and benefits of anticipated future derivative instrument transactions associated with the execution of a clearly defined hedging strategy (CDHS); and (iii) the appropriate costs and benefits of anticipated future derivative instrument transactions associated with nonhedging derivative programs (e.g., replication, income generation) undertaken as part of the investment

strategy supporting the policies, provided they are normally modeled as part of the company's risk assessment and evaluation processes. However, Section 4.A.5 states that if a group of policies is excluded from the Stochastic Reserve requirements, the company may not include future transactions associated with nonhedging derivative programs in determining the Deterministic Reserve for those policies.

## Q 21.3: What is a CDHS?

A: Section 7.L states that a CDHS must identify:

- The specific risks being hedged (e.g., cash flow, policy interest credits, delta, rho, vega, etc.).
- The hedge objectives.
- The risks that are not hedged (e.g., variation from expected mortality, withdrawal, and other utilization or decrement rates assumed in the hedging strategy, etc.).
- The financial instruments used to hedge the risks.
- The hedge trading rules including the permitted tolerances from hedging objectives.
- The metrics for measuring hedging effectiveness.
- The criteria used to measure effectiveness.
- The frequency of measuring hedging effectiveness.
- The conditions under which hedging will not take place.
- The person or persons responsible for implementing the hedging strategy.
- Areas where basis, gap, or assumption risk related to the hedging strategy have been identified.
- The circumstances under which hedging strategy will not be effective in hedging risks.

Section 7.L also states that a hedging strategy involving the offsetting of the risks associated with other products outside of the scope of these requirements is not considered a CDHS.

## $Q$ 21.4: Are costs and benefits of a hedging program that does not qualify as a CDHS included in the cash flow model in some way?

A: Section 7.K. 1 states that the company shall include in the projections the appropriate costs and benefits of derivative instruments that are currently held by the company in support of the policies subject to VM-20 requirements. Some actuaries would conclude this includes derivative instruments currently held regardless of whether these are part of a CDHS. For an anticipated future derivative instrument transaction, however, Section 7.K. 1 requires inclusion if the transaction is associated with the execution of a CDHS, or with a nonhedging derivative program that is normally modeled as part of the company's risk assessment and evaluation processes.

## Q 21.5: How will actuaries determine a hedging program's expected future cash flows?

A: Per Section 7.K.2, the company shall reflect the company's established investment policy and procedures for that program, project expected program performance along each scenario, and recognize all benefits, residual risks, and associated frictional costs.

Some actuaries run their hedging model to project the hedging cash flows (costs and benefits) under each scenario included as part of the VM-20 stochastic projection. These hedging cash flows would be included as an offset to the cost of the guaranteed benefits projected in the cash flow model that are being hedged.

## $Q$ 21.6: If a derivative program is going to be revised or changed in the future, is this change included in the calculation?

A: Section 7.K. 1 states that the company shall also include in the cash flow projections the appropriate costs and benefits of anticipated future derivative instrument transactions associated with the execution of a CDHS and the appropriate costs and benefits of anticipated future derivative instrument transactions associated with non-hedging derivative programs (e.g., replication, income generation) undertaken as part of the investment strategy supporting the policies, provided they are normally modeled as part of the company's risk assessment and evaluation processes.

If changes are going to be made to a derivative program, some actuaries include the changes in the model, while other actuaries wait until the changes are implemented to the derivative program, particularly if the changes to the program are not final or approved.

If future changes or revisions are going to be included in the model, it would be prudent for the actuary to document the basis for including changes to derivative programs included in the reserve model.

## $Q$ 21.7: Do the limitations of projected hedge effectiveness in other reserve and capital calculations such as Actuarial Guideline XLIII and C3 Phase II apply to the minimum reserve calculation in VM-20?

A: There are no required limits to hedge effectiveness in VM-20. Section 7.K. 2 states that for clearly defined hedging strategies, the company may not assume that residual risks and frictional costs have a value of zero, unless the company demonstrates in the PBR Actuarial Report that "zero" is an appropriate expectation.

Also, Section 7.K. 3 states that where one or more material risk factors related to a derivative program is not fully captured within the cash flow model used to calculate CTE 70, the company shall reflect such risk factors by increasing the Stochastic Reserve as described in Section 5.E.

Some actuaries choose not to use any effectiveness measures because they are not required in VM-20. Other actuaries use effectiveness measures consistent with the hedge effectiveness factors used in their Actuarial Guideline XLIII and C3 Phase II calculations if they have variable annuity business. Other actuaries develop hedge effectiveness factors specifically for the business being modeled for VM-20. Many actuaries consider whether hedge effectiveness will vary under extremely adverse or favorable scenarios.

## $Q$ 21.8: Are there other things that the actuary takes into account when modeling a derivative program?

A: As discussed in Section 7.K.2, some actuaries would aim to fully capture the practical realities associated with the program and the modeling of the program-frequency of rebalancing, transaction costs, margin costs, basis risk, gap risk, pricing risk, parameter estimation, assumption limitations, and trading limits. These actuaries would determine these other costs and limitations in the framework of the tail scenarios that end up determining the Stochastic Reserve.

With dynamic hedging strategies, in some cases the cash flow model supporting the CTE calculation may be able to adequately reflect residual risks through margins in program assumptions, adjustments to costs and benefits, etc. In other cases, reference to additional external models or analyses may be necessary where such results cannot be readily expressed in a format directly amenable to a CTE calculation. In such cases, some actuaries combine the results of such models by a method that is consistent with the objectives of VM-20 requirements.

## $Q$ 21.9: Is there a certification needed if a derivative program is included in the calculation?

A: There is no explicit requirement in VM-20 for certification regarding any derivative program included in the calculation. Section 3.C.5 of VM-31 requires a brief description of the approach used to model derivative programs in VM-20 calculations and a description of any CDHS. Section 3.D.6.f of VM-31 requires a detailed description of model risk management strategies (e.g., hedging) and other derivative programs, including any CDHS, specific to the groups of policies in scope and not already covered in 3.C.5 Section 3.D.14.a of VM-31 requires a certification from a duly authorized investment officer that the modeled asset investment strategy is representative of and consistent with the company's investment policy. Section 3.D.14.b requires a certification by a qualified actuary that the modeling of any clearly defined hedging strategies was performed in accordance with VM-20 and in compliance with all applicable ASOPs.

## $Q$ 21.10: What are the Valuation Manual definitions of derivative asset program and derivative liability program, and what VM-20 guidance distinguishes between these programs?

A: Section 7.B.1.h states that the cash flows projected by the company shall include "cash flows from derivative liability and derivative asset programs, as described in Section 7.K.” For the Valuation Manual that is effective on Jan. 1, 2020, these terms are not defined in VM-01, "Definitions for Terms in Requirements." Some actuaries believe that an appropriate definition for derivative asset program would be similar to a definition for "asset-associated derivative" (which is defined in VM-01 but not used in VM-20), which is a derivative program whose derivative instrument cash flows are combined with asset cash flows in performing the reserve calculations. Some actuaries believe that an appropriate definition for derivative liability program would be a derivative program whose derivative instrument cash flows are combined with liability cash flows in performing the reserve calculations.

Section 7.F. 1 of VM-20 specifies that cash flows from invested assets includes cash flows from derivative asset programs. Likewise, for the calculation of the net asset earnings rate, Section 7.H.2.c.ii specifies that net investment earnings shall include income from derivative asset programs. Also, Section 4.A.4.e specifies that, for the calculation of the Deterministic Reserve, the actuarial present value of premiums and related amounts includes the present value of future derivative liability program net cash flows.

Thus, although not articulated by the Valuation Manual effective on Jan. 1, 2020, some actuaries may conclude that VM-20 implicitly requires that each derivative program must be classified as a derivative asset program or a derivative liability program, depending on how the program is modeled for purposes of the Deterministic Reserve calculation and for each scenario for the Stochastic Reserve calculation.


[^0]:    ${ }^{1}$ Where 3.B. 5 is calculated assuming the policy has no secondary guarantee(s).

[^1]:    ${ }^{2}$ Available on the Academy's website at

    http://www.actuary.org/files/publications/Practice_note_on_applying_credibility_theory_july2008.pdf.

[^2]:    ${ }^{3}$ https://www.soa.org/research/topics/indiv-val-exp-study-list/.


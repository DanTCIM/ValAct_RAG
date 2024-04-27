# A PUBLIC POLICY PRACTICE NOTE 

## Principle-Based Approach Projections Practice Note

## December 2019

Developed by the PBA Projections Practice Note Work Group, a joint effort between the Life Valuation Committee, the PBR Governance Work Group, and the Life Product Committee of the American Academy of Actuaries

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-01.jpg?height=266&width=721&top_left_y=2098&top_left_x=694" alt="image" style="width:100%;height:auto;">

Objective. Independent. Effective. ${ }^{\text {m }}$

This practice note is not a promulgation of the Actuarial Standards Board, is not an actuarial standard of practice, is not binding upon any actuary, and is not a definitive statement as to what constitutes generally accepted practice in the area under discussion. Events occurring subsequent to this publication of the practice note may make some of the practices described in this practice note irrelevant or obsolete.

## Principle-Based Approach Projections Practice Note Work Group

Benjamin Slutsker, MAAA, FSA, Chairperson

Dylan Strother, MAAA, FSA

Grace Senat, MAAA, FSA

Cindy McGovern, MAAA, FSA

Ross Zilber, MAAA, FSA

Kevin Piotrowski, MAAA, FSA

Jennifer Frasier, MAAA, FSA

Chris Whitney, MAAA, FSA

Chuck Ritzke, MAAA, FSA

Karen Rudolph, MAAA, FSA

Jason Kehrberg, MAAA, FSA

Andy Smith, MAAA, FSA

Ben Taylor, MAAA, FSA

Gary Osterhout, MAAA, FSA

Tim Cardinal, MAAA, FSA

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-02.jpg?height=344&width=696&top_left_y=1576&top_left_x=709" alt="image" style="width:100%;height:auto;">

1850 M Street NW, Suite 300

Washington, D.C. 20036-5805

The American Academy of Actuaries is a 19,500-member professional association whose mission is to serve the public and the U.S. actuarial profession. For more than 50 years, the Academy has assisted public policymakers on all levels by providing leadership, objective expertise, and actuarial advice on risk and financial security issues. The Academy also sets qualification, practice, and professionalism standards for actuaries in the United States.

## TABLE OF CONTENTS

Introduction ..... 4
PBR Projection Demonstration of Nested Modeling for VM-20 ..... 6
List of Acronyms ..... 7
Definitions and Overview ..... 8

1. Definitions ..... 8
2. Overview of Nested Modeling and Inner/Outer Loops ..... 11
High Level Subject Areas ..... 16
3. General PBA Projections ..... 16
4. Analysis and Reporting ..... 19
5: Governance and Validation ..... 25
6: Pricing ..... 29
5. Model Efficiency and Reserve Estimation ..... 32
Specific Topics ..... 39
6. Mortality ..... 39
7. Policyholder Behavior and Non-Guaranteed Elements ..... 44
8. Reinsurance ..... 47
9. Economic Scenario Generation ..... 53
10. Assets ..... 57
Appendix - External References ..... 61

## Introduction

## Description of Work Group

This practice note was developed by the American Academy of Actuaries ("Academy") PrincipleBased Approach (PBA) Projections Practice Note Work Group. This work group coordinated efforts with the Academy's PBR Governance Work Group, Life Valuation Committee, and Life Product Committee.

## Purpose and Scope

The PBA Projections Practice Note contains questions and answers related to common practice for projecting future principle-based reserve and risk-based capital calculations. Although this practice note focuses on projecting future VM-20 reserves, some sections are also applicable to VM-21 and other relevant frameworks. The considerations included for PBA projections could be relevant for projections such as pricing, asset adequacy testing, and business planning.

One reason for creating this practice note is to develop a central resource to find PBA projection topics related to nested modeling techniques, asset projection topics, modeling simplifications, analysis and reporting, and governance and controls.

This document does not contain a comprehensive list of all PBA projection topics and applications. In addition, this practice note only attempts to discuss common actuarial practices at the time of authorship and does not contain any guidance.

## Comment About VM Being a Living Document

The Valuation Manual (VM) is a living document that is subject to change. Therefore, any references made to the Valuation Manual, either directly or indirectly through other practice notes or references, are based on the content available at the time of this publication and might become out of date. Direct references made to the Valuation Manual in this practice note are those from the January 1, 2019, version.

## Comment About Emerging Nature of PBA Practices

Principle-based approaches for reserves and other purposes are an emerging practice area that will continue to develop and evolve over time. This practice note addresses concepts that are known by the work group to be currently in use or in discussion. There could be other procedures employed for PBA projections that are not discussed within this practice note. Also, as technology advances and practices mature, new techniques will develop.

## Applicability and Limitations

The purpose of this practice note is to provide information to actuaries who are implementing PBA projections. This practice note is not a promulgation of the Actuarial Standards Board, is not an actuarial standard of practice, is not binding upon any actuary, and is not a definitive statement
as to what constitutes generally accepted practice in this area. No representation of completeness is made; other approaches may be reasonable and may be in or may gain common use. Events occurring subsequent to this publication of the practice note may make the practices described in this practice note irrelevant or obsolete.

## PBR Projection Demonstration of Nested Modeling for VM-20

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-06.jpg?height=912&width=1757&top_left_y=242&top_left_x=493" alt="image" style="width:100%;height:auto;">

The "PBR Projection Demonstration of Nested Modeling for VM-20" graphic above shows a visual representation of what a VM-20 projection might look like as of the valuation date and at future re-valuation points. The red line in the diagram represents an outer loop scenario, which could represent a business forecasting or pricing projection scenario, and the blue dots on the line are valuation nodes. The blue lines at each node represent reserves calculations in inner loop projections, where each inner loop is a projection of PBR cashflows supporting the reserve calculation at the valuation node.

At each valuation node in the inner loop graphic, VM-20 calculations are determined based on the in-force business mix, economic conditions, and inner loop assumptions assumed at that valuation node. The net premium reserve (NPR) is calculated using the prescribed formula and assumptions. The deterministic reserve (DR) is calculated using a projection of the prescribed deterministic economic scenario, where the scenario is parameterized as of the valuation node based on the outer loop scenario economics. A separate projection over stochastic scenarios is run to generate stochastic cashflows for the stochastic reserve (SR) inner loop calculation.

At each valuation node in the graphic, cash flows are discounted to reflect the appropriate reserve calculation at the valuation node. A balance sheet and income statement can be constructed at each valuation node. In addition, there is an interdependency between the NPR, DR, and SR at each valuation node due to starting assets required in the modeled reserve. The starting assets for both the DR and the SR at each valuation node depends on the final reserve calculated at that node, so the DR and SR inner loops are dependent on the other inner loop calculations at that node.

## List of Acronyms

| AAT | Asset Adequacy Testing |
| :--- | :--- |
| A/E | Actual to Expected Ratio |
| ALM | Asset Liability Management |
| CDHS | Clearly Defined Hedging Strategy |
| COI | Cost of Insurance |
| CTE | Conditional Tail Expectation |
| CRVM | Commissioners Reserve Valuation Method |
| CSO | Commissioner's Standard Ordinary |
| CTE | Conditional Tail Expectation |
| DR | Deterministic Reserve |
| FIT | Federal Income Tax |
| GAAP | Generally Accepted Accounting Principles |
| GPU | Graphics Processing Unit |
| GPV | Gross Premium Valuation |
| GPVAD | Greatest Present Value of Accumulated Deficiency |
| IFRS | International Financial Reporting Standards |
| IRR | Internal Rate of Return |
| MAR | Model Audit Rule |
| NPR | Net Premium Reserve |
| ORSA | Own Risk and Solvency Assessment |
| RBC | Risk-Based Capital |
| PBA | Principle-Based Approach |
| PBR | Principle-Based Reserves |
| SOE | Source of Earnings |
| SOX | Sarbanes-Oxley |
| SR | Stochastic Reserve |
| VaR | Value at Risk |
| VM | Valuation Manual |
| YRT | Yearly Renewable Term |
|  |  |

## Definitions and Overview

## 1. Definitions

## $Q$ 1.1: What is nested modeling?

A: Nested modeling occurs when the projected values of one or more components of a model are themselves a modeled value. An example is the use of future projections of reserves under a principlebased approach when the statutory reserve is based upon a deterministic or stochastic model. If an actuary needs to determine the future VM-20 or VM-21 statutory reserves, a nested model may be required.

Some actuaries consider nested modeling whenever modeling components under each scenario are themselves determined by scenarios in the future. Please refer to the Society of Actuaries' Nested Stochastic Modeling Report (2016) for more details:

https://www.soa.org/Files/static-pages/research/nested-stochastic-modeling-report.pdf

## $Q$ 1.2: What is an outer loop and inner loop?

A: The outer loop determines the projection path for which expected cash flows are being estimated. The inner loop calculates modeled values at various re-valuation points, using the outer loop result as the starting point for each of the inner loop scenarios. Assumptions and scenarios may differ between the inner and outer loops. For instance, the outer loop could contain best estimate assumptions required for forecasting the expected cash flows arising from a block of business, while the inner loop could contain assumptions required in accordance with a specific valuation standard, such as prudent estimate assumptions for a principle-based reserve calculation.

## $Q$ 1.3: What is a node, re-valuation point, or pivot point?

A: The user defines the points at which an inner loop projection is performed, and each point is referred to as a node, re-valuation point, or pivot point. For the purposes of this practice note, these terms can be used interchangeably.

## $Q$ 1.4: What is the difference between prescribed, best estimate, and prudent estimate assumptions?

A: Best estimate assumptions are the assumptions defined by the actuary in an expected outcome, reflecting anticipated experience with no provision for risk of adverse deviation. These assumptions are often used when communicating the results anticipated to most likely occur. Examples that use best estimate assumptions could include pricing and U.S. GAAP.

Prudent estimate assumptions are best estimate assumptions with added margins for conservatism or provisions for adverse deviation. The margins are typically determined by the actuary and can require sensitivity testing to determine the appropriate level and direction for a margin. For PBR reserves, prudent estimate assumptions are defined in VM-01 and further described in VM-20 and VM-21.

Prescribed assumptions are assumptions required by regulation. For instance, formulaic statutory reserves are calculated using assumptions that are required by regulations. In some circumstances, the experience
assumption may not be prescribed, but the margin is prescribed. One example in VM-20 is the requirement to use a mortality assumption based on company anticipated experience, plus a prescribed margin based on the credibility of the experience and number of years of sufficient data.

## Q 1.5: What is a deterministic reserve?

A: The deterministic reserve (DR) is the present value of outflows less inflows using a cash flow model with balance sheet items projected under a single scenario or a limited number of predefined scenarios. These scenarios can be based on an actuary's best estimate of what might occur in the future, as could be the case for a pricing or forecasting exercise. Alternatively, the scenario(s) used may be prescribed by regulation.

## Q 1.6: What is a stochastic reserve?

A: The stochastic reserve (SR) is based on accumulated losses or deterministic reserves generated across a risk distribution, targeting a desired point in the risk distribution through a chosen risk metric. For example, the VM-20 and VM-21 SR amounts are based on CTE calculations at the $70^{\text {th }}$ percentile. Stochastic Reserves use an actuarial projection model to generate cash flows and balance sheet items under many scenarios. These scenarios are typically determined using a scenario generator, which could be based on an underlying statistical distribution or model. The scenario generator may contain parameters defined by the actuary, or parameters prescribed by regulation.

## $Q$ 1.7: What is the net premium reserve?

A: The net premium reserve (NPR) is a reserve calculation defined in VM-20 that serves as a minimum reserve floor for life insurance PBR reserves. It uses prescribed assumptions and methodologies, which vary by product type.

## Q 1.8: What is a PBR Reserve?

A: A PBR Reserve refers to a statutory reserve calculated using a principle-based approach. For life insurance, this is calculated according to VM-20 requirements. The VM-20 PBR Reserve is defined as the greater of the NPR, the DR (plus due and deferred premium asset), and the SR (plus due and deferred premium asset). There are optional tests in VM-20 that allow the actuary to skip the DR and SR calculations if certain criteria are met. For variable annuities, the PBR Reserve is calculated according to VM-21 requirements, based on a standard projection amount and a stochastic reserve. VM-21 does not allow companies to avoid either reserve calculation, but it does allow an alternative method for the SR.

## Q 1.9: What is a Gross Premium Valuation Reserve?

A: A Gross Premium Valuation (GPV) Reserve is calculated as the actuarial present value of benefits, expenses, and related amounts less the actuarial present value of premiums and related amounts. The deterministic reserve under VM-20 is a specific example of a GPV calculated using a prescribed scenario. The cash flows are projected under the prescribed economic scenario and discounted using the Net Asset Earned Rate, as defined in VM-20. Assumptions for GPV calculations in actuarial practice can use best estimate assumptions, depending on the intended objective, but for statutory reserve calculations (such as VM-20 or VM-21), liability assumptions can include margins or be prescribed.

## Q 1.10: What is the Greatest Present Value of Accumulated Deficiencies?

A: The stochastic reserve under VM-20 is determined using the CTE 70 of the distribution of scenario reserves calculated using prescribed economic scenarios. Each scenario reserve is based on the Greatest Present Value of Accumulated Deficiencies (GPVAD), plus the statement value of starting assets at the valuation node. The GPVAD for each scenario in VM-20 is determined using three steps.

1. Project the cash flows for the model segment under the given economic scenario. At the projection start date and the end of each projection year, determine the value of the negative of the projected general account and separate account assets.
2. Discount the negative projected asset value at each year. For VM-20, use a discount rate equal to $105 \%$ of the one-year Treasury rate from the corresponding economic scenario. Use the net asset earned rate for each path as the discount rate for VM-21.
3. The greatest of these present values represents the GPVAD.

A similar requirement exists for calculating the stochastic reserve in accordance with VM-21 for variable annuity statutory reserves.

## $Q$ 1.11: What is a clearly defined hedging strategy?

A: The term clearly defined hedging strategy (CDHS) means a strategy undertaken by a company to manage risks that meet the criteria specified in the applicable requirement. CDHS criteria are specified in the NAIC Valuation Manual and used in both VM-20 and VM-21. The reporting requirements are discussed in VM-31. VM-01 outline specific requirements for a hedging strategy to qualify as a CDHS. If the requirements are met, then the company may reflect the costs and benefits of the CDHS in the calculation of the modeled reserve.

## $Q$ 1.12: What is asset adequacy testing?

A: Asset adequacy testing (AAT) is an analysis of the adequacy of reserves and other liabilities being tested, in light of the assets supporting such reserves and other liabilities, as specified in the statement of actuarial opinion. This analysis might be done on an after-tax basis using best estimate assumptions with margins. Some companies in the U.S. satisfy AAT by projecting future assets and liabilities using a set of seven deterministic scenarios prescribed by the state of New York. These scenarios are referred to as the "New York 7." Some actuaries will run additional scenarios determined by their company. Other actuaries run stochastically generated scenarios. As a result of AAT, the actuary might determine that an additional reserve above the calculated reserve (e.g., Commissioners' Reserve Valuation Method) is necessary. For more information on AAT, please refer to the American Academy of Actuaries' Asset Adequacy Analysis practice note.

## 2. Overview of Nested Modeling and Inner/Outer Loops

## $Q$ 2.1: When are projections with outer loops and inner loops applicable?

A: Outer loops and inner loops can be used for projecting future reserves or risk-based capital that require a different assumption basis than that used for the broader projection purpose (e.g., when performing a projection using best estimate assumptions where the reserve or RBC requires the use of prudent estimate assumptions). Some examples of applications include projecting VM-20, VM-21, RBC C3 Phase II, GAAP for fixed indexed annuities, or economic reserves within broader projection functions such as product pricing, cash flow appraisals, or business forecasts and planning projections. These applications can be used to produce projected outer loop values, such as distributable earnings or a statement of financial position, which are dependent on inner loop calculations. Assumptions for these inner loop calculations can use prudent estimates or prescribed, whereas an outer loop for pricing or plan projection can use best estimate assumptions.

## $Q$ 2.2: Is nested modeling the same as nested stochastic calculations?

A: Nested stochastic calculations are a subset of nested modeling. Nested modeling might not require stochastic projections at all. Nested modeling could be a combination of an outer loop projection and inner loop projection, and the nested modeling type is commonly defined by the type of projection within each. Some examples are included in the following table:

| Nested Modeling <br> Type | Outer Loop / Inner Loop | Example |
| :--- | :--- | :--- |
| Deterministic on <br> Deterministic | Deterministic Outer Loop, <br> Deterministic Inner Loop | Forecast of a term product under a best estimate scenario (outer <br> loop), with a VM-20 DR calculation for reserves (inner loop) at <br> each projected re-valuation point in the outer loop. |
| Stochastic on <br> Deterministic | Deterministic Outer Loop, <br> Stochastic Inner Loop | Forecast of a universal life with secondary guarantee (ULSG) <br> product under a best estimate scenario (outer loop), with a <br> VM-20 SR calculation for reserves (inner loop) at each <br> projected re-valuation point in the outer loop using multiple <br> stochastic scenarios to calculate the SR. |
| Stochastic | Stochastic Outer Loop, <br> Deterministic Inner Loop | Risk-based pricing analysis over stochastic economic scenarios <br> (outer loop) for a term product, with a VM-20 DR calculation <br> (inner loop) at each projected re-valuation point in the outer <br> loop. |
| Stochastic on | Risk-based pricing analysis over stochastic economic scenarios <br> (outer loop) for a UL product, with aVM-20 SR calculation for <br> Stochastic | Stochastic Inner Loop (inner loop) at each projected re-valuation point in the <br> outer loops using multiple stochastic scenarios to calculate the <br> SR. |


| Stochastic on <br> Stochastic on <br> Stochastic | Stochastic Outer Loop, <br> Stochastic Inner Loop, <br> Stochastic calculations <br> required within the inner <br> loop | Risk-based pricing analysis over stochastic economic scenarios <br> (outer loop) for a UL product under VM-20 with a clearly <br> defined hedging strategy on interest rate guarantees, requiring a <br> stochastic projection to calculate reserves at every future time <br> point (inner loop) as well as a stochastic calculation of hedging <br> values (stochastic calculation within the inner loop) in each <br> scenario in the stochastic reserve. In this example, the value of <br> the hedge is projected using stochastic calculations within each <br> inner loop. |
| :---: | :---: | :---: |

# Visual example of nested modeling at a single node 

Deterministic-onDeterministic

Stochastic-on-

Deterministic

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-13.jpg?height=91&width=343&top_left_y=481&top_left_x=1200" alt="image" style="width:100%;height:auto;">

Stochastic

Stochastic-onStochastic ${ }^{1}$
<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-13.jpg?height=422&width=890&top_left_y=618&top_left_x=1614" alt="image" style="width:100%;height:auto;">

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-13.jpg?height=228&width=1098&top_left_y=1114&top_left_x=784" alt="image" style="width:100%;height:auto;">

${ }^{1}$ For visualization purposes only three stochastic outer loop scenarios are shown

## Q 2.3: What actuarial exercises could benefit from nested modeling analysis?

A: Nested modeling analysis can be useful whenever a financial statement is being projected. Examples include business forecasting, capital projections, pricing, or hedging. Nested modeling may become more relevant in light of emerging valuation methodologies such as PBR for statutory reserves, Long-Duration Targeted Improvements for U.S. GAAP, and IFRS17.

## $Q$ 2.4: Is it possible to avoid doing nested modeling calculations?

A: It could be possible to avoid nested modeling calculations, depending on the intended purpose of the projection. For modeling purposes where using an approximation might be acceptable, such as in short-term business forecasting, actuaries can choose to approximate an inner loop calculation in order to avoid nested modeling. See the sections within this practice note on Model Efficiency and Reserve Estimates (Section 7) for further discussion on approximations and reserve estimates.

## Q 2.5: Visually, what might a nested modeling projection look like with respect to VM-20?

A: The diagram introduced prior to the first section, labeled "PBR Projection Demonstration of Nested Modeling for VM-20," shows a visual representation of what a VM-20 reserve projection might look like as of the valuation date and at future re-valuation points. The red line in the diagram represents an outer loop scenario, perhaps a business forecasting or pricing projection, and the blue dots on the line are re-valuation points. At each re-valuation point, VM-20 calculations are commonly run based on the in-force business mix, economic conditions, and inner loop assumptions assumed at the re-valuation point. The NPR can be calculated using the prescribed formula and assumptions. At the same re-valuation point, a projection over the prescribed deterministic scenario is typically needed for the DR, where the scenario is parameterized at the re-valuation point based on the outer loop scenario economics. A separate projection over stochastic scenarios is normally run for the SR inner loop. At each re-valuation point, the cash flows are typically discounted or adjusted to reflect the appropriate reserve calculation (for example, a gross premium valuation (GPV) reserve or a CTE70 is computed), and the final reserve is determined.

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-14.jpg?height=805&width=1561&top_left_y=1638&top_left_x=344" alt="image" style="width:100%;height:auto;">

## Q 2.6: How frequently does an actuary perform nested modeling?

A: The frequency of nested modeling will vary by application. Some applications, such as business planning, might use a process in which a nested model is run once a year. In other applications, such as risk-based pricing, the outer loop projections might need to be run multiple times and each run could involve new inner loop calculations. In some cases, an actuary might perform nested modeling until an approximation or an understanding of the sensitivity of results can be constructed. If a reliable proxy is developed for the application, nested modeling might not need to be performed often.

## High-Level Subject Areas

## 3. General PBA Projections

## Q 3.1: How might valuation assumptions used in the inner loop change as the model progresses along the outer loop, and what is considered when determining the changes required?

A: When projecting future reserves, the actuary could consider changing future valuation assumptions consistent with the projection assumptions assumed. Examples of changes to the valuation assumptions along the projection path are described below.

## Projecting Reserves

## Example: 10 \& 20 Year Term PBR block: 2017-19 issues

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-16.jpg?height=789&width=1678&top_left_y=923&top_left_x=256" alt="image" style="width:100%;height:auto;">

## Mortality

The mortality assumption in the VM-20 DR and SR is developed using a blend of prudent estimate company experience mortality rates and industry mortality rates, with no future mortality improvement assumed beyond the valuation date. Prescribed margins are required for prudent estimate company experience mortality rates, which are based on credibility of the underlying experience. The maximum number of years in which the company experience mortality rates can be used is based on the credibility and number of years of "sufficient data" underlying the experience.

The actuary might consider projecting increased credibility and years of "sufficient data" at future revaluation points to reflect additional years of experience, as well as reflecting the impact of unlocking the company experience and industry tables for changes in mortality experience, such as mortality improvement. Some actuaries might consider using the mortality improvement assumption up to future re-valuation points to unlock the company experience portion of the valuation mortality
assumption. For further discussion, please consult the Mortality section (Section 8) of this practice note.

## Expenses

The expense assumption used in the determination of VM-20 and VM-21 modeled reserves is a prudent estimate assumption based on fully allocated company expenses with a margin.

In nested models, it might be internally consistent to assume that expense assumptions are subject to the outer loop projection inflation assumption up to future valuation dates, and are subject to the valuation inflation assumption for the purposes of calculating reserves in the inner loops.

Additionally, the actuary might consider reflecting the impact of any future expense efficiencies, such as an efficiency, consistent with the outer loop up to the projected valuation node. Under this approach, the inner loop assumption would reflect both the outer loop assumption at the valuation node and the valuation requirements. Part of this consideration is whether the statutory reserve requirement does not allow the use of expense efficiencies in the projected cash flows.

## Projected Valuation Assumptions: Expenses

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-17.jpg?height=488&width=1643&top_left_y=1179&top_left_x=249" alt="image" style="width:100%;height:auto;">

## Economic scenarios and assets

The historical interest rate environment drives the starting yield curve, or seed curve, and the mean reversion parameter used in generating the required deterministic and stochastic scenarios. Some actuaries might use the outer loop economic assumption in order to determine, node-by-node, the conditions available to project asset performance and scenarios. Some actuaries might estimate or project the economic environment at a future node as well as the characteristics of the supporting assets at the future node, in order to have the "A" component of a full ALM projection.

The required inputs for the American Academy of Actuaries' interest and equity scenario generator include the starting yield curve and historical 20-year Treasury rates, which will change as the economic environment changes in a scenario. Therefore, some actuaries could decide to reflect the impact of changes in the projected yield curve on the valuation scenarios. This could be accomplished through inner loop scenario generation or by predetermining the valuation scenarios at each future valuation date as part of the model setup.

VM-20 and VM-21 credit spreads and defaults are prescribed in tables provided by the NAIC and updated over time. The assumptions can differ between short-term and long-term periods, in which case some actuaries might assume some convergence of short-term and long-term rates over the projection horizon (for example, VM-20 and VM-21 require grading from short-term to long-term spreads for fixed income assets in the projection).

For further discussion on nested modeling for asset assumptions, please consult the Economic Scenario Generation section (Section 11) and Assets section (Section 12) of this practice note.

## $Q$ 3.2: What is different in the projected balance sheet under pre-PBR requirements, where reserve and risk-based capital components are mostly formulaic?

A: The difference in the projected balance sheet under PBR requirements is that assumptions vary with both time and future economic conditions. Assumptions for PBR requirements might be more dynamic than those previously used pre-PBR.

Projecting formulaic balance sheet amounts can be more straightforward than projecting modeled reserves, because the underlying assumptions for these amounts can be known in advance and are less likely to change over time. Take, for example, the rate of interest used in the discounting process as defined by the formulaic Commissioners’ Reserve Valuation Method (CRVM). This rate is locked in at issue and identical for all companies. In comparison, modeled reserves under a principle-based approach require that the rate of interest used in the discounting process is dependent upon the company's prudent estimate of its investment earnings and are unlocked as economic conditions change. Assets can therefore have a significant place in the determination of liability amounts in a principle-based method. The concept of unlocking introduces the exercise of determining available assets at future valuation nodes-not an integral component of a formulaic approach.

Under formulaic reserving approaches, assumptions are prescribed and locked in at issue. For example, mortality rates used in the CRVM method are prescribed as the current Commissioners' Standard Ordinary (CSO) table, and this assignment is locked in at issue. Compare this to a principle-based approach, which uses company experience for the subject group of policies. Uncertainty is introduced in forecasting PBR reserves because the future states of company mortality experience are not known with certainty. Therefore, the actuary might estimate those future states of experience to determine the reserve at the future node. The same is true of future states of company expenses and all aspects of policyholder behavior (persistency, policy loan activity, benefit utilization, etc.). Even if future projection elements are certain, there could still be an increase in the number of actuarial assumptions and, therefore, a need to make structural changes to actuarial models.

Turning to other balance sheets amounts that are dependent upon reserve balances creates second-order impacts to the balance sheet. For example, certain required risk-based capital amounts are dependent upon reserve balances. Although these risk-based capital amounts might not be principle-based in nature, their underlying reserve balance basis is, thus introducing a degree of uncertainty to the surplus line as well.

## $Q$ 3.3: How can the impact of future new business be incorporated into projections, and how does this differ from current approaches using formulaic reserves?

A: Under a formulaic reserve framework, the reserves for a block of business are equal to the sum of the reserves for the individual policies. Independence between the reserves for inforce and future
business might allow for the use of simplified methods to create pro-rata income statement and balance sheet projections by scaling and layering together model output based on the purpose of the projection (e.g., sales plan, etc.)

Under a PBR framework, the modeled reserves are calculated in aggregate, based on the characteristics of the in-force block as of the valuation date. Some actuaries reflect the impact of the aggregation of all inforce business when performing reserve projections. Doing so can simplify the calculations required. For example, if the DR tends to prevail at most durations for a particular business segment, the actuary might rationalize that the DR will always be the dominant reserve in a forecast involving future new business at increasing volumes, even if the NPR were to dominate at some durations when only looking at a single issue-year of business on a stand-alone basis. The intended use of projections and disclosure to the end-user might be used to determine the appropriateness of using such simplifications.

## $Q$ 3.4: To what extent are assumption sensitivity tests and shocks on projection assumptions carried through to valuation assumptions?

A: The actuary might carefully consider both the intent and effect of sensitivity tests or shocks on projection assumptions when determining the extent to which they may be used to determine the valuation assumptions.

The actuary might wish to make changes to the valuation assumptions to be internally consistent with the changes to the projection assumptions. This can become complex when considering the emergence of experience up to future valuation dates and the extent to which changes in experience would lead to a change in the valuation assumptions. For more complex sensitivities/shocks, bifurcating the impact of the sensitivities/shocks into impacts from projection assumption changes and valuation assumption changes will separate the impact into more manageable pieces for understanding, explaining, and confirming the results.

For example, if the intention is to fully capture the impact of a shock to an outer loop best estimate assumption, a projection that allows the shocked assumption to impact inner loop assumptions could be appropriate. However, the actuary might also consider freezing the valuation assumption in the inner loop so that it is not affected by the shock to the outer loop in order to isolate the impact to only the outer loop assumption.

## 4. Analysis and Reporting

## Q 4.1: What types of period-to-period analysis might an actuary be interested in for PBA projections?

A: When considering period-to-period analysis for changes to the values calculated by the inner loop (e.g., analyzing a change in the projected reserve), some actuaries might consider treating each inner loop as if it were its own actuarial model. The same techniques an actuary might use to compare two actuarial models can be used to compare two re-valuation nodes within a nested model. For example, for PBA projections, assume an analysis is focused on interest rates and equity markets. The outer loop interest rate scenario can be used to determine the starting point for the interest rate scenario used for each inner loop node, so the biggest driver of changes to the PBA reserve will be the outer loop interest rate scenario. Some actuaries might consider becoming familiar with the interest rate generator used in the model and understanding how the parameters might change over time. In particular, the mean reversion parameter set in the prescribed scenario generator for VM-20 is a
function of past Treasury rates (see Economic Scenario Generators, Section 11, of this practice note for further discussion). Within a given outer loop projection, the actuary might wish to consider whether there could be impacts to the inner loop calculations due to the differences between the assumptions in the outer and inner loops. Analyzing the differences in the assumptions can be useful in understanding the projection results.

When comparing projections between two time periods, the actuary might consider the changes to the inforce population between the two periods. If a model run includes projected new business, then the actuary could consider how the actual new business compares to the assumed new business. This could include both the volume and distribution of the new business. If the model is not projecting new business, then the actuary might consider whether it is useful to exclude the newly issued policies from the future period model in order to have a more consistent inforce comparison. Some actuaries also compare the starting interest and equity markets in the future period with the projected markets from the prior time period.

The methods described in this section can be shown through an attribution analysis for changes in reserves. An example is shown in Q4.4 later in this section.

## $Q$ 4.2: What reporting values might actuaries be interested in when projecting principle-based reserves specifically?

A: The reporting values to be analyzed depend upon the purpose of the outer loop projection. The challenge introduced by PBR is that the reserves needed for projections are based upon an assetliability actuarial cash flow model, which can use different assumptions than the outer loop for the broader projection.

When analyzing the change in reserves under PBR, the actuary might consider an initial analysis that focuses on the aspect of PBR that is driving results. If the DR is being analyzed, primary elements to analyze might include the projected cash flows and net asset earned rate. If the SR is being analyzed, the projected asset balance and asset-liability interactions may be the focus. To understand changes to investment rates, the actuary might use detailed projections of asset balances, purchases, and asset cash flows. For deeper analysis of the SR, some actuaries develop a report showing all of the scenario reserves, as well as the underlying details for each stochastic scenario (e.g., such as the Treasury rate for a particular time-to-maturity).

The actuary might consider developing reports that can identify moving parts, illustrate cause-effect relationships, and highlight driving forces. As the complexity in a model grows, some actuaries build a collection of reports to aid analysis, communication, and decision-making. For example, when adding PBR reserve projections to a model, reporting elements that might be useful include:

1) Informative Graphics-Visual diagrams or charts that show which factors at each valuation node initiate a change in the PBR reserve calculation
2) Analysis-Specific details of model results that illustrate calculations and relationships, outputs of what-if scenarios, and findings that foster understanding or spark further evaluation
3) Impact-Summaries of metrics and demonstrations showing how key drivers of the PBR reserves change the metrics
4) Validation-Comparisons that confirm the integrity of results

## Q 4.3: How might changes in prescribed, company experience, and prudent estimate assumptions in future inner loop calculations be analyzed or attributed?

A: Attribution analysis for an inner loop calculation can be handled in a similar manner as attribution analysis for a valuation date reserve calculation. Some assumptions used for inner loop calculations could vary at each re-valuation point based on the outer loop projection. For example, it might be the case that the outer loop projection on a best estimate basis assumes some amount of mortality improvement. Likewise, as an outer loop moves throughout time, there might be more credible data. These situations would result in a different mortality assumption at each re-valuation point, instead of the same inner loop assumption at all revaluation points.

To analyze and attribute the impact of the updated inner loop assumptions, an actuary might run a series of projections and review results before and after the change in assumptions. This can be run-time-intensive depending on the number of re-valuation points. Therefore, the actuary might find it to be beneficial to test subsets of the business at a time or only at select revaluation nodes (such as every three to five years), and use the findings to approximate the attribution of changing inner loop assumptions that are dependent on outer loop projections.

## $Q$ 4.4: What types of templates for reports might be useful?

A: The reports used for analysis of projected PBR reserves could build upon reports used for pointin-time valuation model analysis. This can include projections of the inforce movements, fund value rollforwards, and asset rollforwards, as well as changes in assumptions. These reports can be used to for informational, analytical, or validation purposes for projection calculations that employ nested modeling. Some examples shown below of inforce movements and graphs of changes in reserves are discussed in the SOA paper Understanding VM-20 Results (2017).

VM-20 Reserve Movement Analysis

Term Life - 10yr/20yr, \$1.2MM/\$0.35MM Face

(\$ thousands)

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-22.jpg?height=1583&width=1849&top_left_y=317&top_left_x=130" alt="image" style="width:100%;height:auto;">

(1) Anticipated Reserve Change: change in reserves due to anticipated experience in inforce demographics and anticipated economic/non-economic assumptions (2) Reserve Volatility: deviations from anticipated reserve changes due to emerging experience, or due to unexpected changes in economic/non-economic assumptions

Copyright (C) 2017 by the Society of Actuaries, Schaumburg, Illinois. Reprinted with permission https://www.soa.org/Files/Research/Projects/2017-understand-vm-20-results.pdf

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-23.jpg?height=1540&width=2448&top_left_y=170&top_left_x=130" alt="image" style="width:100%;height:auto;">

Copyright (C) 2017 by the Society of Actuaries, Schaumburg, Illinois. Reprinted with permission https://www.soa.org/Files/Research/Projects/2017-understand-vm-20-results.pdf

Some actuaries set up a projection model to automatically generate these reports with varying frequency. Some actuaries might decide to only export such reports quarterly or annually so that output data is kept to a manageable size.

Not all data may be available to compute an income statement or balance sheet at each re-valuation node, in which case it may be useful to produce a short-range projection with all data, perform analysis, and extend that analysis out to future projection points.

To build on attribution analysis in the outer loop, some actuaries construct source of earnings (SOE) reports. These reports assign sources of cash flows to various categories, such as mortality, investment, and expense margins, to explain differences between actual and expected earnings. Note that while a decomposition of reserves (splitting the change in reserves into mortality, lapses, etc.) can help understand the movement between projected reserves, an SOE analysis helps decompose the earnings in the entire outer loop, not just the reserves. Adjustments may be made to cash flows to better align with an SOE framework, such as decomposing the components of the reserve and assigning them to designated sections of the SOE report.

## Q 4.5: How is analysis performed on projected reserves when the prevailing reserve component (e.g., for VM20: DR, SR, NPR) changes throughout the projection? What ways do actuaries consider for reporting / computing reserves in between re-valuation points for a given outer loop projection?

A: When projecting VM-20 or VM-21 reserves, the prevailing reserve component might be different at future re-valuation points. It could also be the case that exclusion tests are passed or failed at revaluation points and a reserve component at that re-valuation point does or does not need to be calculated. Some actuaries might consider projecting the various components and even conducting exclusion tests periodically at select future re-valuation nodes to detect whether these events occur. If they do occur, one method might be to quantify the impact to the reserves in a distinct category of an attribution analysis.

Some actuaries construct a vector for each reserve component at each re-valuation node for the purposes of producing the final reserve at each time-step. Other actuaries calculate reserves at only for a subset of the future re-valuation points, and instead interpolate reserves between re-valuation points.

When computing PBR reserves at future re-valuation nodes, the actuary could consider linear interpolation. For the modeled reserve, linear interpolation might not always be appropriate, in which case other relationships can be used to interpolate between re-valuation points. Some examples include cubic-spline or parameterization techniques. In addition, factors based on other reserve proxies (e.g., NPR, GPV) can be used for interpolating the modeled reserve between re-valuation points. Refer to Q7.4 for further discussion on these methods. Once a full vector of reserves is computed, adjustments for due and deferred premium can be made and maximums can be computed.

Part of an attribution analysis could include attributing reserve movement to a change in the prevailing reserve component. This can include a determination of whether it is due to change in exclusion test results or a change in the maximum reserve. Similar analysis done as of the valuation date can be utilized at re-valuation points. As previously mentioned, additional information about attribution analysis can be found in the SOA-sponsored paper, Understanding VM-20 Results.

## Q 4.6: How much weight might an actuary put into inner loop results far into the projection timeline?

A: Like many other applications that make use of models, estimates produced by the model are only as good as the input data and calculation specifications of the model. To the extent that, as an outer loop moves forward in time and an inner loop projection is computed based on assumptions inferred from outer loop activity, inner loops far into the projection timeline may become more reliant on assumptions in outer durations. An actuary might consider this when determining the number and distribution of re-valuation points. There could be more accurate results for re-valuation points early in the outer loop projection and less reliable results for re-valuation points later in the projection. Some actuaries therefore consider more revaluation points early in an outer loop projection and fewer re-valuation points in later years of the projection, dependent on the intended purpose and available computing power.

## 5: Governance and Validation

Q 5.1: Does VM-G apply to the projection of principle-based reserves (e.g., for pricing, capital forecasting, business strategy)?

A: VM-G is only required for point-in-time valuations and not for future PBR projections. However, some actuaries choose to follow the requirements of VM-G as a guideline to ensure consistency of governance standards. Additionally, although VM-31 is only required for point-in-time valuation, it could prove useful as a documentation template for projection purposes.

The American Academy of Actuaries’ Model Governance Checklist (2016) also outlines general governance considerations that would prove useful in all aspects of modeling, including the projection of principle-based reserves.

Some actuaries leverage existing governance and documentation procedures pertaining to VM-G and VM-31 for PBR reserve projections. In addition, the actuary may wish to consider whether existing governance and documentation pertaining to pricing and cash flow testing may be applicable to the outer loop. This may include documentation that exists for MAR, SOX, AAT, ORSA, and internal purposes. See the following diagram of possible governance and documentation frameworks applicable to PBR.

| Requirement | Assumption Methodology | Governance \& Documentation |
| :--- | :--- | :--- |
| PBR: <br> VM-20 \& VM-21 | Best Estimate + PBR Margins | PBR Actuarial Report |
| Statutory Reporting | Moderately Advserse <br> (Prescribed \& PBR) | Model Audit Rule |
|  |  |  |
| GAAP Reporting | Best Estimate | SOX Controls |
| Own Risk and Solvency | N/A | ORSA Report |
| Assessment (ORSA) |  | Cash Flow Testing Memo |
| Cash Flow Testing | Best Estimate + CFT Margins |  |

In addition, some actuaries follow corporate governance standards and apply these to projections of PBR (data, model, and assumptions).

## $Q$ 5.3: Which subject matter experts are consulted in the validation process?

A: There are several elements of a PBR projection that actuaries consider validating. Some examples include:

- Data elements
- Inner loop liability assumptions
- Inner loop asset assumptions
- Future economic scenarios
- $\quad$ Outer loop assumptions
- Model integrity and simplifications
- Reporting and analysis

Each of these areas can require certain subject matter expertise. Examples include employees from valuation, pricing, modeling, risk management, investments, and corporate governance. It may help to leverage work or validation tools that these other areas have provided. Additionally, some actuaries might consider an independent third-party review to validate the projections, which can be considered either a peer review or an expert review.

## $Q$ 5.4: What are some techniques that may be used to validate projected PBR reserves?

A: Some actuaries independently validate the projection model's calculations. The robustness of this validation might fall anywhere between spot-checking cash flows in inner loop projections to performing a ground-up recalculation of modeled results for a subset of polices. Specifically, for
nested modeling, some actuaries compare the cash flows from the inner loop to cash flows from the outer loop and verify that the differences are attributable to margins, prescribed assumptions, or any other expected differences.

The level of transparency and comfort in the model's calculations can drive the amount of independent validation performed, with additional validation for models where the results will be used to make business decisions, such as pricing. Some items to validate and review include the aggregate reserve, single/sample cell calculations, single/sample scenarios calculations, and assumptions. The following describes some techniques that are used.

## Static and dynamic validation

Static validation compares inforce counts, face amounts, asset values, and reserves produced by the model at the valuation date to the actual amounts to check the reasonableness of the model.

Dynamic validation compares future cash flows, including premiums, investment income, death benefits, surrender benefits, dividends, and expenses to the actual amounts for the prior year and the projected or budgeted amounts for future years to check the reasonableness of the model.

## Data and assumption validation

Data and assumptions can be validated using static validations as appropriate. In addition, two separate data sources can be compared for inventory count, to ensure data was not lost in a system exchange process. For assumptions, the actuary might use trends and $\mathrm{A} / \mathrm{E}$ ratios to track the development of experience compared to an assumption over time. In addition, some actuaries spotcheck assumptions and other data inputs against documentation.

## Ratio comparison across reserve methods

Some actuaries evaluate the SR at each projection node along the outer loop. They might also evaluate the relationship of the SR to the DR along each path and compare to actual results, sensitivity tests of actual results, and pricing results as applicable. Ratios can be developed for the NPR, DR, and SR relative to an underlying measure such as a GPV or face amount, which can then be compared to each other. For example, the DR and SR are expected to be greater than the GPV due to reflecting margins. In addition, the actuary could have preconceived expectations of which component prevails for certain populations or product types. Other ratio comparisons can include PBR statutory reserve projections to GAAP reserves projections, especially for instances where GAAP calculations are based on best estimate assumptions and PBR calculations are based on prudent estimate assumptions.

Scenarios with larger amounts of SR in excess of the DR can be further evaluated by the actuary to understand what kind of scenarios lead to larger excess deficiencies. Some actuaries calculate the GPVAD at each node, examining the distribution as well as the maximum, minimum, and mean for reasonableness. In addition, some actuaries analyze how different types of scenarios drive the GPVAD.

## Comparing models results

Some actuaries compare the results from one model run to another to help get comfortable with the relative difference between the two runs. Some items compared could include cash flows, number of policies, or $\mathrm{A} / \mathrm{E}$ ratios. Using a static earned rate can be useful for comparing differences in liability assumptions within the DR, as it eliminates any noise caused by asset differences between two runs. For example, reserve calculations may be compared between pricing and reserve models.

Comparing implied rates (i.e., lapse, mortality, COI charges, yearly renewable term [YRT] reinsurance) is a method that some actuaries use to confirm the assumptions are behaving consistently across valuation dates, or that the level of margin relative to the projection assumption seems reasonable. Creating graphs of reserve balances, earned rates, and distributable earnings can also be useful for analyzing the reasonableness of results. For stochastic calculations, some actuaries consider comparing the minimum, maximum, mean, and distribution of results.

Some actuaries also perform an attribution analysis to ascribe differences in the reserves between models to various sources. These sources can include modeling changes, assumption updates, and economic factors. To see an example of an attribution analysis for a comparison between reserves at different time periods, refer to Q4.4 in this practice note.

## Sample cell recalculation

Some actuaries use sample cell recalculation, which consists of selecting sample cells for which to reproduce the calculation in an independent model. This can then be used to validate another model. These sample cells either are randomly selected or intentionally selected to test different policy and product attributes.

## Standardized process controls

Some actuaries use standardized process controls to maintain the integrity of the system and to meet auditor requirements such as SOX/MAR mandates. Some actuaries incorporate flags, indicators, and metrics into the administrative system to enable types of process controls. Flowcharts can summarize the entirety of a process and flow, especially for reviewers and newcomers. For software systems and models, security logs and access restrictions could help provide controls from a technology and systems governance perspective.

## Reasonableness checking

Some actuaries confirm that model results, sensitivity tests, and validation tests meet reasonable expectations based on product features, demographic mix, investment strategy, and economic scenarios. These may be established by validation or governance committees beforehand.

## $Q$ 5.5: What are some techniques actuaries use to communicate projected reserve results to others?

A: The actuary might communicate projected reserves to the appointed and/or qualified actuary, senior management, internal auditors, external auditors, rating agencies, and regulators. When communicating projected reserve results, the actuary typically considers the perspective and knowledge of the intended audience. Some actuaries provide items such as assumption documentation, an attribution of reserve changes, SOE analysis, financial statements (e.g., income
statement and balance sheet), and a control executive summary. Documentation of the decisionmaking process underlying assumptions and approximations might also be provided. The actuary might consider data visualizations, such as graphs and charts, if deemed appropriate. ASOP No. 41, Actuarial Communications, may be applicable.

## 6: Pricing

## $Q$ 6.1: What are some challenges for the pricing actuary that $P B R$ creates regarding communication practices with the valuation actuary and company management?

A: Because PBR reserves are not set at issue like traditional prescribed CRVM reserves, reserves could become estimated assumptions in pricing (similar to estimated assumptions for mortality, lapse, and expenses). For example, the VM-20 reserve is calculated as the greater of the NPR, DR, and SR, creating layers of the PBR reserve that often requires an assumption as to the projected ongoing volume of new and inforce business for both the policy being priced as well as for the group of policies with which the new policy may be aggregated.

The pricing actuary might find that under one set of assumptions, the SR does not dominate. However, under another set of assumptions, the SR may dominate in some or all time periods. As a result, higher or lower reserves might emerge depending on the level and sales mix of new business for the group. The pricing actuary might consider whether it is important to clearly communicate the valuation actuary and to company management the additional pricing risks created by these uncertain pricing PBR assumptions, and the impact of decisions regarding what existing group of policies a new product might be included with as well as the assumptions made for that existing group.

Additional communication might be needed with the valuation actuary and company management to ensure that other assumptions (e.g., lapse, mortality, interest, expenses, etc.) are consistent for PBR in pricing vs. valuation. PBR might introduce more volatility in reserves compared to pre-PBR formulaic reserves. The actuary might consider whether sensitivity testing can be helpful in capturing varying levels or patterns of PBR reserves under different scenarios. Sensitivity testing can also be used as a tool to communicate the potential volatility of future reserves and pricing results.

## $Q$ 6.2: What are specific pricing challenges for projecting future PBR?

A: Pricing actuaries might consider some of the following in projecting future PBR when pricing products:

a) Finding practical methods for projecting PBR in pricing models that take run-time and cost constraints into consideration. A primary practical issue is the potential need to estimate the results of the inner loop projections using a simpler proxy calculation estimate, given the large number of future valuations inherent in the pricing projection.

b) Allocating projected reserves modeled on a group of policies to a seriatim basis for pricing purposes.

c) Accounting for the impact of the inforce business on the projected reserves allocated to the new plan. This could be the case when PBR reserves for a new plan are dependent upon the inforce and projected sales of all the plans in the PBR reserve group.
d) Balancing the practical simplifying methods and uncertainty built into the pricing model against the desire to be as consistent as possible with actual valuation results as they emerge.

e) Validating that PBR reserves in pricing are consistent with actual PBR reserve levels.

## $Q$ 6.3: What are the ways in which pricing actuaries could reflect $P B R$ in pricing, given that $P B R$ consists of modeled reserves on groups of policies as opposed to seriatim reserves?

A: Some actuaries might price using stand-alone reserves. While marginal pricing is the practice of setting product prices equal to the extra cost of producing an extra unit of output and not reflecting fixed costs or other units of output, some actuaries will extend this concept to reserves. A stand-alone reserve is the reserve for the product unit under consideration and does not reflect other units. When projecting PBR reserves in pricing, an actuary might consider using stand-alone reserves to varying degrees of granularity. At the most granular level, an additional unit is an individual policy or each pricing cell. At lower levels of granularity, an additional unit could be one year of planned issues for the product(s) under consideration. Other granularity levels could be one year's issues along a product parameter or population characteristic. Examples include level term period, gender, risk class, issue age band, face band, or market. An actuary could consider reflecting one or more levels of granularity in pricing, and allocating reserves at lower granularity levels to individual pricing cells.

Other actuaries might price using aggregate reserves estimated by some other approach. Fully allocated is the practice of reflecting all units of output. Because PBR reserves are modeled reserves on groups of policies, a PBR reserve projected as of a future valuation date may reflect policies issued in both the past and up to the projected valuation date. A fully allocated method can include an approach to allocate a portion of the fully allocated PBR on a seriatim or segmented basis to the plan cells or segments being priced.

The pricing actuary, in collaboration with the valuation actuary, might conduct ongoing analysis to ensure that overall future PBR reserves are adequately "covered" by the sum of the reserves allocated to any particular plan on an ongoing basis.

## Q 6.4: Is it reasonable for the pricing actuary to include discretionary margins in pricing as a method to adequately cover uncertainty in future reserves?

A: Some pricing actuaries might consider adding an explicit margin in pricing assumptions to cover an allocated portion of overhead expenses for the company or other sources of uncertainty in future reserves such as regulatory changes, worsening liability assumption experience, worsening economic environment, unattained sales, or others. This can take the form of a percent of new or inforce premium projected for the plan but, alternatively, could be allocated using other approaches. By definition, overhead expenses are not associated with a particular plan, pricing cell, premium income, or any other element of the plan being priced. So this “discretionary margin” becomes a strategic decision in deciding how to allocate a portion of company overhead expenses to the product being priced. The pricing actuary might consider including provisions for how best to ensure that the reserves projected in pricing will be sufficient to cover future reserves as required by company objectives. Hence, some pricing actuaries assume a discretionary margin to allocate all or part of company reserves to a particular plan or pricing cell.

## $Q$ 6.5: What are methods for allocating aggregate PBR reserves to specific policies or segments for pricing purposes?

The following are some examples of methods for allocating aggregate modeled reserves to a particular plan or pricing cells:

- NPR- Allocating modeled reserves in pricing based on the proportion of NPR might be more consistent with VM-20 point-in-time valuation. In addition, if the pricing model already calculates the NPR on a plan/cell level, this can be a convenient method to implement. One disadvantage is that the NPR can be less aligned with how the company perceives policy risk and does not appropriately capture which policies generate the excess modeled reserves.
- GPV-The GPV reserve can have a more similar shape to the modeled reserve than the NPR, as it is similar to an "unmargined" modeled reserve, and therefore could also be a good candidate to serve as the allocation basis. For a pricing model that uses best estimate assumptions, the present value of existing pricing assumptions may be leveraged to calculate the GPV reserve.
- Actuarial or Business Judgment-The pricing actuary might decide to allocate using a separate method based on actuarial judgment or business judgment in deciding how to best charge certain plans/policies for the reserve charge.

Relevant discussion to reserve allocation for pricing can be found in the Model Efficiency and Reserve Estimation section of this practice note, which discusses possible bases to use for reserve proxies.

## Q 6.6: Given the uncertainties that are common with respect to Federal Income Tax (FIT) treatment when reserve methods change, what are some of the ways a pricing actuary might adequately reflect FIT in their PBR pricing models?

A: Each company generally develops its own strategy when making assumptions about FIT. Where issues with respect to FIT and PBR have not been settled, some pricing actuaries conduct sensitivity testing under different tax interpretations and determine which is consistent with the company tax strategy.

$Q$ 6.7: Do actuaries need to change their pricing programs under PBR in order to properly reflect selfsupport and lapse-support testing for compliance with Life Insurance Illustrations Model Regulation \#582 (the Model)?

A: Some actuaries might test compliance with the Model during the pricing process (e.g., in setting nonguaranteed elements that are intended to be illustrated). The self-support and lapse-support tests under the Model require projection of policy cash flows without specific regard to funding statutory reserves. However, statutory reserves can affect the cash flows indirectly when determining some elements of policy cash flow, such as federal income taxes, reinsurance, and expenses.

The illustration actuary could assume historical improvements in assumptions from the date of an experience study up until the effective date of the illustrated scale, but no future improvement, among other requirements. As illustration actuaries might use the pricing program to perform these tests, they could consider whether the assumptions used in the pricing programs are consistent with those required by the Model, or if changes are appropriate for this purpose.

Q 6.8: A plan being priced will often be grouped with other inforce plans for the purpose of setting PBR reserves. These groups may or may not be required to perform DR or SR reserve calculations depending upon the results of the exclusion tests under VM-20. When pricing a new or changed plan to be included in a group under PBR, what are some of the approaches that can be used to demonstrate that the group will or will not qualify for the exclusion test?

A: Performing an exclusion test is distinct from pricing at an individual cell level. Exclusion tests are performed on groups of policies, possibly from multiple products (e.g., universal life without secondary guarantees might be combined with whole life). Although policy parameters and associated pricing metrics are determined at a cell level, pricing metrics can also be calculated at a cohort level. In a similar manner, exclusion tests can be performed on a group of policies using a representative mix of cells.

When the pricing of a new plan changes the exclusion test result for a group of plans, pricing actuaries might consider being in close communication with the valuation actuary, because the pricing of the new plan could affect the reserves for the entire group of plans. If reviewing exclusion testing during pricing, some actuaries test not only at issue but also at future valuation points to make sure the exclusion test results hold over time.

Q 6.9: With traditional pre-PBR pricing, the pricing actuary might price riders and supplemental benefits separately from the base policy or combined with the base policy. What are some of the special considerations for pricing riders/supplemental benefits, and how might the pricing approach differ under PBR?

A: The pricing actuaries might consider professional judgment in determining whether to price riders together with or separately from the base product. Some pricing actuaries could decide to price riders and supplemental benefits separately from base plan pricing, often based on an estimate of the materiality of such supplemental reserves.

To determine whether the rider or supplement benefit follows the same reserve methodology as the base policy under PBR, some actuaries might consider whether the rider and base policy features influence each other or act independently after the point of issue. Actuaries can refer to the "Riders and Supplemental Benefits" section of the NAIC Valuation Manual for guidance.

## 7. Model Efficiency and Reserve Estimation

## $Q$ 7.1: What constitutes a model efficiency technique, and why are these techniques used?

A: The goal of a model efficiency technique is to produce adequately accurate results in an understandable manner while reducing processing time. Such a technique recognizes a trade-off between accuracy, complexity, and time to produce results. As actuarial models have grown in complexity, model efficiency techniques can be used to keep model run-times within a manageable range. Model characteristics that might cause actuaries to consider the use of model efficiency techniques include models with a large number of stochastic scenarios, models with complex liabilities and/or assets, and models with dynamic asset-liability interaction. In addition, nested models can significantly increase run-time, necessitating the need to consider model efficiency techniques.

Some actuaries consider the following characteristics for model efficiency techniques:

- Requires less time and/or fewer resources
- Is understandable to management
- $\quad$ Performs well under stressed conditions
- $\quad$ Produces reproducible results
- $\quad$ Allows for all desired output (e.g., full income statement and balance sheet)

Additional information on the use of model efficiency techniques by actuaries can be found at webpage of the American Academy of Actuaries’ Model Efficiency Working Group.

## Q 7.2: What are types of model efficiency techniques that actuaries use?

A: Actuaries use many different types of model efficiency techniques, which may be categorized as follows:

- $\quad$ Mathematical and/or Model Design Techniques-These techniques focus on mathematical approaches to simplify and speed up calculations. This can include the use of closed form solutions such as Black-Scholes solutions, which use market observables of asset values, interest rates, and volatility metrics instead of using first-principles modeling to value specific assets.
- $\quad$ Scenario Design and Selection Techniques (Scenario Reduction)-These techniques address the choice and design of scenarios and are often used when actuarial models involve the use of large sets of stochastic scenarios. An example is the use of representative scenarios, which is described in the Economic Scenario Generation section (Section 11) of this practice note.
- $\quad$ Model Data-Building Techniques (Cell Reduction and Proxy Modeling)-These techniques involve compressing the number of liability and/or asset model points (cells) and include traditional model point compression (e.g., bucketing seriatim data by homogenous groupings such as issue age and duration) as well as newer techniques such as cluster modeling, replicating portfolios, and proxy modeling. Cluster modeling focuses on identifying and leveraging "important" data points. Replicating portfolios can be used to replace a complex set of liabilities with a replicating set of assets that is easier to model. Proxy modeling aims to fit a proxy function to estimate the liabilities relative to underlying risks.
- Technological Techniques (Technology Solutions)-These techniques use the latest cutting-edge technology to reduce model run-time. Hardware-based techniques include leveraging additional computing power using grid, cloud, and GPU computing. Software-based techniques include optimizing programming code for efficient use of memory and other hardware, as well as finetuning model precision criteria, such as the criteria for convergence during solve routines.

No single model efficiency technique is best in every situation. A combination or hybrid approach might be optimal, depending on the intended purpose.

## $Q$ 7.3: What are some model efficiency techniques that are utilized to speed up run-times for PBA projections, and particularly nested stochastic models?

A: Of the many model efficiency techniques available, there are some that may have larger impacts on the overall model run-time than others. In particular, model efficiency techniques that are applied to inner loop calculation processes may have larger overall impacts than efficiency techniques applied to outer loop processes due to the number of times the inner loop processing occurs relative to each outer loop. Some of the model efficiency techniques the actuary might consider include:

- Scenario reduction techniques include any method that reduces the total number of scenarios being run in a stochastic model. This can be applied in VM-20 by scaling back on the number of economic scenarios used to generate the SR component. An actuary might use the prescribed generator's scenario picking tool, for example, to find a smaller scenario set that does not materially understate the SR. Another idea is to additionally scale back on the number of economic scenarios used for the inner loop as the projection gets further from the time zero date. For example, if the projection is running the subset of 500 scenarios for the first three nodes, an actuary may drop this to the subset of 100 scenarios for nodes beyond the third.
- Cell reduction techniques involve reducing the number of cells or asset or liability model points being processed, which in turn reduces overall calculation load for a projection. See question Q7.6 later in this section for more details on these techniques.
- Re-valuation node reduction techniques consist of reducing the number of time points at which inner loop projections are initiated. For example, the actuary might only process inner loop projections at time points 1, 2, 5, and 10 years after the outer loop start date, respectively. The selection of which time points the inner loop projections occur may vary depending on the purpose and business use of the projection results.
- Proxy modeling consists of creating a simplified, and more efficient version of a model, process, or component of a model that produces a result that is similar to the original full calculation. This simplification of calculations can result in reduced processing time but might come at the risk of additional variance in model results, especially when estimating the tail of a distribution. For different types of proxy estimates that could be used for VM-20 and VM-21 reserves, refer to Q7.4.
- Technology solutions include ways in which model efficiency can be obtained through changes to the specific software solutions, hardware modifications, and network infrastructure. For software, the actuary might look at options to improve software performance within the specific software solution being used. For example, there could be parameters that impact tolerances, rates of convergence, or run-time optimization that are software-specific. For hardware efficiency, the actuary might consider increasing the hardware capacity for processing calculations through the use of more powerful computers or an increased number of computers. This could include solutions such as grid or cloud computing. For infrastructure, the actuary might consider how aspects of the hardware and network setup could impact run-times for a model. This could include items such as network bandwidth, colocation of data and hardware, database or hard disk throughput connection limits, and other related limitations that could affect data read and/or write speeds.
- Limiting projection length of the nested inner loops and compensating by using an adjustment in the last projection time step can also reduce run-time. The adjustment would reflect the present value of liability cash flows that remain at the end of the shortened projection period.
- Calculating only the prevailing reserve component is another simplification technique that can be used for frameworks that require the maximum between multiple reserve components, such as VM-20 and VM-21. If the forecast includes only a subset of the policies in the VM-20 product group, the forecast might not provide an accurate representation of what the prevailing reserve would be if all policies in the product group were included. For these calculations, aggregation concepts are important if differences between reserve components for one set of policies could be more than offset by differences in another. For example, a stand-alone policy group might have the NPR prevail for

VM-20, but the SR may prevail when all policies within the product group are combined. In this case, some actuaries might assume that the SR prevails when running a subset of policies within the product group, regardless of whether the NPR is greater than the SR for a specific subset of policies within the model. This simplification becomes complex if the prevailing reserve component can change from node-to-node, in which case actuaries can consider presetting models to assume which reserve component prevails in which node.

The actuary might consider whether the modeling efficiency produces results within a reasonable range of the analysis that results without the efficiency. Another consideration for actuaries is determining how the simplification holds up for small and large shocks to assumptions. Some actuaries might find this especially pertinent if the simplifications are derived for a baseline set of results, with the intention of using a relationship to a reserve proxy. If a simplification is validated assuming one set of conditions, some actuaries would consider additional testing to ensure that the model works as intended under other sets of conditions.

## Q 7.4: What variables can serve as a proxy estimate to project VM-20 and VM-21 modeled reserves to avoid nested modeling?

A: It can be complex and time-consuming to forecast modeled reserves, such as the DR in VM-20, SR in VM20 and VM-21, and the CTE calculation in C3 Phase II. One technique described as a model efficiency in Q7.3 is to use a proxy amount to estimate the reserve. A baseline analysis where the modeled reserve is forecasted at periodic intervals could be used to estimate modeled reserves by developing factors expressed as a ratio to the proxy amount. Such factors can vary based on policy characteristics (gender, class, funding level, etc.) and policy year. The following could be used as a proxy formula to estimate modeled reserves:

- $\quad$ NPR-For VM-20, the NPR might not require nested modeling and projection at all future nodes, making it a good candidate to estimate the DR and/or SR for VM-20. Actuaries might consider exercising caution in using this as a proxy if the shape of the NPR is materially different than the shape of the DR and SR.
- $\mathbf{G P V}$-The GPV reserves can serve as a potential candidate to proxy the modeled reserves for VM-20 and VM-21, as the modeled reserve could be analogous to a margined GPV reserve. Therefore, the shape and peak might be similar between both reserves, but the GPV reserve does not require nested modeling (assuming that both the outer loop and inner GPV loops are using the same assumption vectors). For functions such as pricing, some actuaries might decide to align the projection of the reserve with the economic cost charged to policyholders, which could potentially be accomplished by allocating the reserve based on GPV. The downside to using the GPV reserve might be that this may not already be part of the model projection, and may need to be added to the model.
- Inforce Metrics-Some actuaries employ inforce or investment metrics to serve as a proxy for the modeled reserves. This can include face amount, net amount of risk, premiums paid, assumed interest earnings, or investment spread. Some actuaries already have inforce proxy formulas in place for RBC requirements, which can be leveraged for reserve projection purposes.

In some situations, particularly when first implementing PBR, there might be little actual experience to test the accuracy of proxy formulas against. Some actuaries might perform simplified PBR calculations on a hypothetical inforce block or develop a single-cell model in these situations. In addition, some actuaries might
perform one or more actual hypothetical PBR valuations for the new plan on a stand-alone basis as a gauge to evaluate the reasonableness of the proxy formulas.

Pricing actuaries might consider performing sensitivity tests to the proxy formulae assumptions to see how sensitive premium rates and profitability are relative to changes in reserve levels. To monitor the reasonableness of proxy formulas, some actuaries prepare ongoing actual-to-expected studies that compare the results of ongoing actual PBR results to the results by PBR proxy formulas and then adjust proxy formulae as needed.

## Q 7.5: What are some model efficiency considerations given differences between projecting PBA values vs. calculating a single point-in-time value, between inner and outer loop projections?

A: Even if an actuary establishes a process to determine prescribed PBA assumptions for the time zero calculation, a different process might be necessary to determine what these prescribed assumptions should be for future valuation dates in the projection when market observables are not available.

Upon considering model efficiency techniques for nested PBA models, actuaries might consider downstream impacts on projections at future nodes. This consideration might not be necessary for time zero calculations whose prescribed assumptions can be based on market observables for asset values, interest rates, and other economic variables.

Although time zero valuation assumptions can be determined manually, the actuary might consider automating the evolution of these assumptions from one node to the next as a model efficiency consideration, regarding both the outer and inner loop. It could take significantly longer to produce projected PBA amounts when one or more future valuation assumptions needs to be set up manually for each future node ahead of time. As an example, embedding the prescribed scenario generator logic in the projection model in an automated fashion can considerably speed up the time it takes to produce results compared to manually using the prescribed scenario generator to prepare scenario sets for each of the nodes ahead of time.

## Q 7.6: How is a test of model simplifications done and how frequently?

A: One way to determine the error introduced by a model simplification is by performing additional runs using the full methodology. If such an exercise can be performed in a timely manner, there could be no need for the simplification in the first place. When this is not practical, the actuary can gain confidence in the simplification by performing a comparison of the full model and simplified model using a variety of commonly applied model validation techniques, such as static tests of individual values and simplification methodologies, single cell testing, back testing, and stress testing. In particular, an actuary might consider performing additional validations for simplifications on CTE or VaR calculations.

The frequency of model validation can vary with the riskiness of the model, in which greater model risk may warrant more frequent validation tests. Actuaries may consider the frequency of external audits and regulatory reviews when determining the level of model validation. Additional validation may be warranted when a failure of the model occurs or when material changes are made to the model, model inputs, assumptions, or efficiency techniques being utilized.

## Q 7.7 What options are available for liability or asset grouping to improve efficiency?

A: Liability and asset grouping can be performed utilizing common cell reduction techniques such as grouping of model points or clustering. For both of these techniques, the parameters upon which the grouping
or clustering is performed can vary from one product to another, as well as from one model purpose to another. Two common clustering algorithms are K-means and hierarchical agglomerative clustering. A Kmeans clustering algorithm partitions the data into a well-distributed set of clusters when " $\mathrm{k}$ " data points is a relatively small number. However, this technique can be sensitive to outliers and initial assignment of the " $\mathrm{k}$ " data points. In contrast, hierarchical agglomerative clustering treats every individual data point as a cluster and merges the closest pair of clusters until a target clustering level is reached. These techniques are further illustrated in the diagrams below; more information can be found in "Getting the Most of Axis," Volume 9, in the link below:

https://www.oliverwyman.com/content/dam/oliver-

wyman/v2/publications/2018/october/OliverWymanAXISVol9_Fall\%202018.pdf

K-means clustering algorithm

Copyright @ 2018 Oliver Wyman

Randomly select $k$ data points as

Step 1 centroids, where $\mathrm{k}$ represents the desired number of clusters

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-37.jpg?height=230&width=349&top_left_y=931&top_left_x=1208" alt="image" style="width:100%;height:auto;">

Step 2

Assign every data point to its nearest centroid
<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-37.jpg?height=584&width=1438&top_left_y=1274&top_left_x=218" alt="image" style="width:100%;height:auto;">

Repeat steps 2 and 3 until clusters

Step 4 reach their target state, which is when additional iterations have no impact on the cluster selection

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-37.jpg?height=255&width=352&top_left_y=1886&top_left_x=1209" alt="image" style="width:100%;height:auto;">

## Treat every data point as an individual Step 1 cluster. Calculate the distance between each cluster

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-38.jpg?height=766&width=372&top_left_y=404&top_left_x=1191" alt="image" style="width:100%;height:auto;">

Step 4

The result is a set of clusters meeting the target clustering level

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-38.jpg?height=209&width=359&top_left_y=1240&top_left_x=1203" alt="image" style="width:100%;height:auto;">

The actuary might also consider how the method being used for cell reduction and the calibration of such method may need to change over time. As inforce blocks age, particular cells or clusters can become larger and more significant than at the start of the outer loop projection. Therefore, the actuary might consider using different criteria for cell reduction for future inner loops. In addition, some actuaries test to see how this approach holds up when introducing shocks to various model inputs.

## Q 7.8: What risks might be associated with using model efficiency techniques in a nested model?

A: One risk associated with using model efficiency techniques is managing the trade-off between accuracy, complexity, and run-time. The risk of unnecessary complexity can be magnified in a nested modeling context where techniques might transition between outer and inner loop projections. Examples include sourcing and determining assumptions for future nodes based on current and average experience in the outer loop.

Good design and communication can be used to mitigate model risk of efficiency techniques. For example, when designing model efficiency techniques for nested models, some actuaries consider the ability of inner loop models to handle extreme outer loop scenarios with limited extrapolation. Grid/cloud availability could also be a risk for nested models given their relatively longer run-times compared to stand-alone models. No single model efficiency technique is best in every situation. A combination or hybrid approach might be optimal.

## Specific Topics

## 8. Mortality

## $Q$ 8.1: What components of the VM-20 mortality assumption might require nested modeling in a projection of $\mathrm{PBR}$ reserves?

A: Mortality improvement is typically a component of the mortality assumption that can require nested modeling when projecting future PBR reserves. Per VM-20, mortality improvement for both company and industry mortality rates can only be modeled up until the valuation date, but not into the future beyond the valuation date. This means, for each valuation node in the projection, there could be a different and unchanging cumulative mortality improvement factor used to project inner loop cash flows beyond the valuation date. In other words, each projected reserve calculation may use a distinct vector of mortality rates.

Other components of the mortality calculation could also employ nested modeling for projecting PBR reserves. Examples include underwriting modifications and mortality segments with little historical data for which credibility is expected to build over time. Another reason to use nested modeling for mortality might be to reflect the wear-off of an additional mortality margin beyond the minimum VM-20 requirement that varies based on projection year.

## $Q$ 8.2: What techniques are available when the practitioner needs to project historical mortality improvement up to the valuation date for each valuation node, but no future improvement beyond that point?

A: The following techniques are commonly considered when modeling historical mortality improvement up to the valuation date but not beyond that point:

i. Nested Modeling-Each valuation may contain mortality improvement that accumulates for a specified number of future years in the inner loop calculation. For example, a mortality table with a 2018 central date used to project PBR reserves in year 2020 could use two years of mortality improvement to calculate the inner loop cash flows in years 2021, 2022, etc. Then to project the PBR reserve in year 2021, three years of mortality improvement could be applied to the mortality to calculate inner loop cash flows in years 2022, 2023, etc. This process would keep repeating to project PBR reserves for all valuation nodes within the projection. While this example is given in terms of whole calendar years, improvement factors can be designed to reflect any partial calendar year and/or off-year end valuation date refinements.

The following provides a visual example of nested modeling for an outer and inner loop of mortality, in which the outer loop assumes $1 \%$ future mortality improvement and the inner loop represents a PBR projection. In addition, this example demonstrates the impact of a mortality assumption update on the inner and outer loop mortality assumptions of a $1 \%$ multiplicative reduction in mortality:

## Projected Valuation Assumptions: Mortality

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-40.jpg?height=615&width=1854&top_left_y=392&top_left_x=144" alt="image" style="width:100%;height:auto;">

## Updating Assumptions

Example: Mortality assumption is updated in 2019 , resulting in a $5 \%$ reduction in best estimate.

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-40.jpg?height=805&width=1830&top_left_y=1365&top_left_x=183" alt="image" style="width:100%;height:auto;">

## Mortality Assumption Update

## Impact on Inner and Outer Loop Assumptions

7.00

6.00

5.00

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-41.jpg?height=347&width=52&top_left_y=758&top_left_x=88" alt="image" style="width:100%;height:auto;">

- 2015 VBT

-BE Mortality (pre-update)

--BE Mortality (post-update)

-DR Mortality (pre-update)

--DR Mortality (post-update)

DR Mortality = BE Mortality + Margin, with Grading

The inner loop (DR) mortality is similar to the outer loop (BE) mortality in early durations, but grades into industry experience in later durations. As a result, the impact of the assumption update is reflected fully in the DR mortality assumption in early durations, but the impact of the assumption update eventually wears off. In later durations, where the DR mortality assumption is fully based on industry experience, the

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-41.jpg?height=453&width=776&top_left_y=412&top_left_x=1892" alt="image" style="width:100%;height:auto;">
assumption update has no impact.
ii. Distinct Modeling Calculations-This is similar to nested modeling, but it is done using separate and distinct model runs for each valuation year, with results individually transferred to a projection (e.g., outer loop) type run. This option could potentially be a more manually and computationally intensive process than using a nested model, but some actuaries find it useful for products with a small set of projection years, such as term products with 20-year level term periods or less.

iii. One Vector Approach-This method uses an average cumulative mortality improvement factor that is representative of all inner loops, and all valuation nodes use the same vector of mortality improvement. So, for example, instead of performing nested modeling for mortality improvement on 20 years of valuation nodes, only one average mortality improvement factor accumulated over a 10year period is used for all valuation nodes. It is suggested to exercise caution around using this approach, as it can affect the slope of reserve increases throughout the projection, which could have an impact on some modeling purposes, such as pricing. It is important to run preliminary testing to confirm that the one vector method can reasonably approximate results produced by more robust methods. The advantage is that complexity can be reduced when building inner loops in a nested model, which could also reduce model run-time and complexity.

## $Q$ 8.3: Why would an actuary project different credibility levels at different valuation nodes?

A: For a newer mortality segment with limited historical experience, there might be a low level of credibility and short sufficient data period for the associated experience. For a VM-20 PBR calculation, this can result in a higher prescribed minimum margin initially for valuations. However, for mortality segments that are expected to grow over time and collect more experience in the future, there may be a higher level of credibility and longer sufficient data period projected at future valuation nodes. Depending on the projection purpose, some actuaries might consider reflecting the higher credibility and longer sufficient data period to project a lower VM-20 minimum mortality margin in future years.

## Q 8.4: What techniques are available for an actuary projecting different credibility levels at each valuation node?

A: Some actuaries might forecast credibility and sufficient data period over time for a given mortality segment. An actuary can accomplish this by first projecting the segment's future inforce size assuming new sales (estimates can be acquired from a new business function within the organization) and then calculating expected claims. This projection of future claims could then be used to calculate the changing credibility metrics over time and determine the minimum set of margins required at future valuation nodes. Along with the credibility forecast, an actuary can also determine the anticipated changes to the VM-20 sufficient data period at each valuation node.

An actuary might use the VM-20 prescribed margins associated with the credibility level at each valuation node to determine the mortality margins for company experience within each inner loop. Similarly, once the sufficient data period is forecasted, the associated VM-20 prescribed grading calculation can be reflected for each inner loop.

## Q 8.5: What are considerations for aggregating credibility for future PBR projections compared to pointin-time valuations?

A: Point-in-time valuations could consider VM-20 requirements to aggregate mortality segments for credibility. This might include considerations such as whether mortality segments are similar in nature and
contain relevant characteristics for aggregation purposes-please refer to VM-20 and the American Academy of Actuaries' VM-20 practice note for discussion on VM-20 valuation requirements for aggregating credibility.

If forecasting credibility to determine mortality margins for each inner loop, an actuary might consider whether mortality segments aggregated for the point-in-time valuation will continue to be aggregated in the future, as well as any expected changes to the level of aggregation in the future. If multiple segments are currently aggregated, then an actuary might decide whether to forecast credibility growth for the aggregate segment or reflect some degree of disaggregation at a future node.

## $Q$ 8.6: What are some additional challenges for projecting PBR reserves for accelerated underwriting and simplified issue life insurance policies?

A: As of the time of drafting this practice note, definitions for simplified issue and accelerated underwriting do not exist in the NAIC Valuation Manual, nor are there designated valuation mortality tables or functionality within the SOA Relative Risk Tool for mapping to a designated industry mortality table. Thus, actuarial judgment is considered for both valuation and projection purposes. In particular, for the purposes of grading to an industry table in determining the VM-20 prudent estimate mortality at future re-valuation nodes, an actuary might consider whether the 2008 Valuation Basic Table (VBT) Limited Underwriting or another table is appropriate as an industry table. For more information, please consult VM-20 or the American Academy of Actuaries' VM-20 practice note.

If a company introduces a new accelerated underwriting program, then for projection purposes, an actuary might consider whether to forecast credibility and employ a nested modeling technique to determine the mortality assumption at future valuation points. In addition, an actuary might need to consider VM-20 guidance regarding the aggregation of mortality segments prior to deciding whether accelerated underwriting experience is aggregated with traditional underwriting experience (again refer to VM-20 and American Academy of Actuaries' VM-20 practice note). This is a relevant issue for valuations, projections, and nested modeling techniques.

## Q 8.7: How does an actuary reflect anticipated mortality trends due to changes in underwriting processes for projecting $P B R$ reserves?

A: VM-20 allows reflection of adjustments to mortality following incremental changes in underwriting, if complying with Section 9 in VM-20. Please refer to VM-20 and the American Academy of Actuaries’ VM-20 practice note for further discussion on these requirements.

If incremental underwriting changes are reflected in the mortality assumption, some actuaries would include them in all projection years. However, if certain incremental underwriting adjustments do not meet the VM20 valuation criteria (for example, lack necessary documentation or support), then some actuaries reflect these adjustments in the outer loop but not in the inner loop. Nested modeling might be used to accomplish this dichotomy.

If a company has multiple incremental changes to an underwriting program, it is possible for some changes to comply with VM-20 (and therefore be reflected in the inner loop for all projection years) and some changes to not comply with VM-20 (and therefore not be reflected in any inner loops).

## $Q$ 8.8: Do actuaries unlock the NPR mortality table to reflect future updates to the CSO table for inforce policies?

A: While VM-20 allows for the possibility of future modifications to the valuation mortality table used to calculate the NPR for inforce business, an actuary might consider whether reflecting this for projection purposes, such as pricing, is appropriate.

Although the NAIC Valuation Manual allows the NPR valuation mortality to be updated for inforce policies in the future, any future proposals for such updates would still be subject to the regulatory approval at that point in time. Therefore, some actuaries might not assume any unlocking of the NPR valuation mortality in future projections.

## Q 8.9: How would an actuary project stochastic mortality for calculating future principle-based calculations for purposes such as economic capital?

A: Some actuaries consider whether to unlock the VM-20 mortality experience assumptions used in the inner loop and, if so, whether to employ nested modeling. As future experience is projected in the outer loop, some actuaries reflect that such experience will form the basis for inner loops at future re-valuation dates based on experience studies. One approach is to set a dynamic mortality assumption for the inner loop that depends on the outer loop mortality scenario. An actuary might also consider reflecting a lag in updating the inner loop mortality to account for any delays before changes in actual experience affect the anticipated experience mortality assumption. In addition, some actuaries might consider whether historical mortality events (e.g., pandemics, trends) will continue or change in the future when projecting the future anticipated experience mortality assumption.

## 9. Policyholder Behavior and Non-Guaranteed Elements

## $Q$ 9.1: What policyholder behavior assumptions and non-guaranteed elements (NGEs) might be projected into the future when projecting future PBR reserves?

A: Policyholder behavior assumptions that might be reflected in a cash flow projection include:

- Lapses
- Surrenders
- Timing and amounts of withdrawals
- Benefit utilization and efficiency
- Conversions and annuitizations
- Policy loan activity
- Premium and deposit pattern and persistency
- Investment decisions including transfers among accounts and rebalancing
- Dividend election
- Increases or decreases to the face amount or coverage

A cash flow projection model might also reflect NGEs, which could include:

- Non-guaranteed premiums or COIs
- Non-guaranteed interest crediting, interest bonuses, persistency credits, and dividends
- Non-guaranteed revenue sharing and spreads
- Exchange and retention programs
- Non-guaranteed reinsurance premiums and recapture of ceded business
- Management actions around NGEs


## Q 9.2: What can cause assumptions on NGEs to change?

A: Possible drivers of assumption changes to NGEs include company management actions, competitor behavior and pressures, economic conditions, emerging experience, and pending regulatory policy changes.

Q 9.3: Should anticipated or pending regulatory (e.g., stat, tax), governmental, and corporate policy changes, in addition to the associated impact on reserve calculations, be embedded in the projections?

A: The actuary might consider the extent that such changes are certain or consider the impact of these changes based on sensitivity testing, to determine whether such changes could be embedded in the projection. This could also depend on the purpose of the projection exercise. For context, these changes could include the following:

a) Reserve changes-Statutory updates to life/annuity PBR, GAAP accounting, tax reserves

b) Tax changes-Dividends Received Deduction (DRD), Required Minimum Distributions (RMD), 1035 exchanges (note federal income tax, or "FIT," does not impact the VM-20 and VM-21 modeled reserves)

c) Other federal policy changes-Department of Labor (DOL) and Securities and Exchange Commission (SEC) requirements

d) Policy retention programs - Incentives for persistency, premium bonuses, agent/broker outreach, inforce exchange programs, surrender incentives

e) Legislation related to non-guaranteed elements-premiums, cost of insurance rates, credited interest rates, dividend scales

If appropriate, the impact of any single change and/or combination of changes could be tested:

- For multiple changes, some actuaries might layer changes in one at a time to determine the incremental impact of each step.
- The actuary might consider sensitivity testing the remaining anticipated changes in different possible/probable combinations.

The impact of the pending change on the policyholder behavior assumptions, NGEs, or reserves may be determined as part of the exercise. Due to the uncertainty associated with some of these types of changes and their potential secondary effects, the actuary might consider a wide and conservative range of outcomes rather than a single point estimate.

Q 9.4: How might NGEs or other assumption changes affect policyholder behaviors that are used in the forecast projection?

A: Some actuaries might integrate changes to NGEs with more complex policyholder behavior assumptions. Some examples include:

- Link between non-guaranteed premiums and lapses
- Link between lapses/conversions and mortality (e.g., mortality deterioration)
- Link between interest rate scenarios and lapses

Some actuaries might incorporate dynamic assumptions to maintain a set relationship between the different risk factors. In many cases, these dynamic formulas might remain unchanged between experience assumptions and valuation assumptions. However, if they are different between the two assumption sets, then this may create an additional need for nested modeling for a projection framework.

## Q 9.5: How do margins change on policyholder behavior over time?

A: VM-20 requires the reflection of an increase in policyholder efficiency over time. Margins on a given risk factor might decrease over time if credibility of company experience for that risk is projected to improve. In order to reduce complexity, some actuaries choose to hold margins constant at each future reserve projection node to reflect the offsetting impact of improved experience and increased policyholder efficiency. Margins also depend on how material the risk is to the modeled group of policies, which could be determined through sensitivity testing and assessment of risk as product designs change.

## Q 9.6: What are some of the ways that the modeling actuary might reflect conversion options in term life insurance or other contracts in the actuarial projection model?

A: The actuary might consider the following when reflecting the impact of conversion options in their actuarial projection model:

- Purpose of the projection: The manner by which conversion options are modeled can vary based on the purpose of the projection. For example:

o Pricing: In a pricing projection, the actuary might include a "conversion cost" in the projected cashflows for the product with the conversion option to ensure this privilege is appropriately included in premiums and charges.

o Forecast: In a financial forecast, the actuary might exclude these "conversion costs," as they are not a cost that will be incurred by the company for that particular product. They might instead reflect conversions by adjusting assumptions to appropriately reflect the different cashflow economics of converted policies as compared to standard issues. Assumptions requiring adjustment could include mortality, lapse, reinsurance retention, and commissions/underwriting costs.

- PBR methodology decisions: When reflecting conversions in PBR reserves, the actuary might consider methodology decisions the company has made around reflecting conversion options within the principle-based valuation and consider incorporating this approach into the forecast reserve calculations. Methodology decisions could include the approach to pre- and post-conversion reserves and whether converted policies will be implicitly or explicitly recognized in reserving assumptions. More information can be found in the links at the bottom of this response, in addition to VM-20 and the American Academy of Actuaries' VM-20 practice note.
- Projection modeling challenges and assumptions: Some actuaries include post-conversion policies in their experience data, implicitly reflecting the impact of conversions in their baseline assumptions. Others could exclude these policies and evaluate assumptions for these policies on their own unique experience. Based on the approach, modeling challenges can exist for projection purposes. For
example, using post-conversion assumption vectors of mortality and lapse assumptions for multiple permanent products at each projection node could present pressure on model run-time. Some actuaries consider estimating conversion costs for projection purposes by either using only one set of assumption vectors rather than vectors for multiple permanent products or by pre-loading a conversion cost table into the projection model based on a preliminary run. Another consideration is whether to model new business in future years to capture conversion costs at future projection nodes.
- Company strategy: The actuary might consider the corporate strategy related to conversion options, which can vary by company. For example, some companies incentivize early-duration conversions by providing conversion credits and other incentives; other companies only allow conversions to certain products.

There are several considerations an actuary might evaluate when determining whether and how to model conversions: utilization; mortality anti-selection; inherent costs of conversion; materiality of conversions; etc. Many of these concepts are covered in actuarial literature. Two sources are provided here:

- Product Matters, Issue 83, “Term Conversions-A Reinsurer's Perspective”
- Product Matters, Issue 106, “Term Conversions: Pricing and Reserves” (pages 20-23)


## Q 9.7: Are margins included in projected NGEs and, if so, how?

A: Some actuaries will include margins on projected NGEs. Examples of this could be limiting COI increases to cover only a portion of the increase in prudent estimate mortality, or not raising COI rates up to the guaranteed level. The actuary also might project a "review" of COI rates less frequently and project delays before any increases occur. Alternatively, no COI increases might be projected. Differences in treatment of COI rates and other NGEs between experience assumptions and prudent estimate assumptions is another reason why some actuaries employ nested modeling.

## Q 9.8: At what point might modeling NGEs and/or policyholder behavior assumptions become onerous, and what are appropriate model/assumption simplifications when projecting them?

A: As with any decision, a cost/benefit analysis can be made to see whether the additional accuracy in the modeling outweighs the potential modeling challenges. Some actuaries only model first-order NGEs. For example, for reinsurance rate increases or COI rate increases, some actuaries choose to not model the associated second-order impacts of these changes including potential recapture of business and potential additional administrative expenses for implementing the change.

Actuaries might consider second-order impacts as they relate to policyholder behavior. Changes in lapse rates and premium funding behavior can have a significant impact on a projection-and there could be little data to support changes to these assumptions after a change in NGEs. Sensitivity testing can be helpful in determining whether the added expense of modeling these provides value.

Some actuaries consider the impact of contractual options (term conversions, policy loans, etc.) on policyholder behavior. These options may be reflected through the use of scenario-dependent withdrawal and surrender formulas. Such formulas may be responsive to projected interest rates/markets, funding levels, premium levels, and benefit amounts.

Some actuaries use predictive modeling to develop formulas for lapse and withdrawals/benefits that are based on historical relationships to predict future policyholder behavior. Predictors may include age, gender, time
since issue, surrender charge, product features, tax status, scheduled changes to benefit/premium amounts, changes in NGEs, and interest/market environment (or “in-the-moneyness” of guarantees).

## 10. Reinsurance

## Q 10.1: What approaches might be used to model future YRT reinsurance rate increases?

A: During the time of this practice note's development, an amendment was adopted for VM-20 that requires non-guaranteed YRT reinsurance to follow pre-PBR requirements, consistent with Statement of Standard Accounting Practice (SSAP) 61, for reinsurance reserves/credit for policies issues on or after $1 / 1 / 2020$.

However, VM-20 still provides guidance for companies projecting future non-guaranteed rate increases on YRT arrangements for policies issued between 1/1/2017 and 12/31/2019. In addition, actuaries might consider how to set the premium increase assumptions for modeling non-guaranteed YRT arrangement cash flows in the outer loop. This response focuses on those instances.

If the company's PBR valuation mortality assumption significantly exceeds the current YRT scale offered by the reinsurer, some actuaries might assume that the reinsurer would raise rates in order to offset some of the reinsurer's projected losses, subject to guarantees and contractual provisions.

Some of the methods that have been discussed include the following:

i. Assume that rates never increase and use the current YRT scale.

ii. Assume that the reinsurer immediately raises rates to offset any losses that they would otherwise incur within the projection.

iii. Assume that the reinsurer immediately raises rates so that the margin between the resulting rate scale and the company's prudent estimate valuation mortality is the same as the margin between the current scale and the company's expected mortality.

iv. Use either of the two preceding methods but assume there is a delay before the reinsurer raises rates. The delay could be intended to allow time for the reinsurer to develop credible experience on the block of business before raising rates, and/or to allow time for negotiation between the ceding company and the reinsurer before rate increases go into effect.

v. Use the current scale and add a margin to it, where this margin is unrelated to the margin discussed in iii above.

In setting a rate increase assumption for a particular reinsurance treaty in an outer loop or in inner loops associated with future re-valuation nodes, the actuary might consider any of the following:

i. The historical frequency of YRT rate increases.
ii. The economic relationship between the ceding company and the reinsurer, including the existence of other reinsurance agreements with the reinsurer.

iii. The presence of any rate guarantee provisions in the reinsurance treaty.

iv. The level of conservatism of the rate increase assumption embedded in the company's calculated reserve.

v. Additional contractual language or provisions, such as a requirement for reinsurers to raise premium rates on all similar business, not just a single company.

It should be noted that some actuaries might not set a rate increase assumption for each reinsurance treaty individually, but rather set an aggregate rate increase assumption for a particular block of the company's business, taking into account all of the reinsurance treaties in effect on this block of business. For further discussion on considerations for modeling an increase to reinsurance premiums, please refer to Section 20 in the American Academy of Actuaries’ VM-20 practice note.

Q 10.2: If a margin is applied to the current YRT reinsurance scale, what approaches might a company take to determine this margin?

A: Some actuaries might consider the following factors in determining an appropriate margin to be applied to the current YRT scale:

i. The likelihood of rate increases-Treaties deemed more likely to be subject to future rate increases could get a higher margin.

ii. The expected timing of rate increases-Some actuaries might delay the application of the margin to reflect that rate increases might not be expected to occur instantaneously.

iii. A minimum threshold for rate increases-If the projected mortality only exceeds the current YRT scale by a very small amount (e.g. 2\%), some actuaries might consider whether the reinsurer would actually raise rates to offset such a small loss.

iv. The mortality margin-Some actuaries might use the effective mortality margin as the margin to be applied to the current YRT scale, so that the inner loop reinsurance margin is roughly the same as the outer loop reinsurance margin.

v. Sensitivity of results-Consideration might be given to the sensitivity of the calculated PBR reserves to changes in the level of margin applied to the YRT scale. When results are highly sensitive to changes in the margin, some actuaries might set the margin at the higher end of the plausible range.

$Q$ 10.3: If YRT rates are assumed to increase above the current scale, what changes might be made to other assumptions to maintain consistency with the YRT rate scale?

A: Some actuaries might reflect whether the selected approach to model future non-guaranteed reinsurance premium rates generates increases that are large enough for the direct-writing company to consider recapturing mortality risk. If such is the case, some actuaries might consider modeling future recaptures rather than reflecting the full reinsurance premium increase using the selected method. This can vary by reinsurer and reinsurance arrangement, depending on treaty provisions and the circumstances in which recapture is permitted, as well as reflecting whether management would be willing to make such a decision. If recapture is modeled, any associated changes in other nonguaranteed elements, such as expenses, could be considered (refer to the Policyholder Behavior \& Non-Guaranteed Elements section of this practice note for more discussion on NGE considerations).

The actuary might consider monitoring the mortality assumption in association with reinsurance cash flows. For example, he/she might consider whether it is reasonable for projected reinsurance premium rates to increase to a level higher than company anticipated mortality, assuming the company anticipated mortality actually emerges in the future.

Another consideration is whether non-guaranteed COI charges would increase to maintain the company mortality net spread if future non-guaranteed reinsurance premiums increased. This has been a heavily debated topic in the regulatory space in recent years. Some actuaries might not feel comfortable projecting commensurate increases in non-guarantees COI charges as reinsurance rates increase if they believe certain jurisdictions would not permit such increases, or management would resist taking such actions in anticipation of policyholder and/or regulator reactions. VM-20 refers to considerations of whether such increases have occurred in the past and whether there is a non-guaranteed element policy approved by the board of directors for the company.

Some actuaries could assume that relatively small or moderate increases to reinsurance premiums might not be significant enough to warrant other management actions. Companies might consider regulatory elements and whether such actions would be realistic in an emerging scenario (refer to the Policyholder Behavior \& Non-Guaranteed Elements section of this practice note for more discussion on NGE considerations).

## $Q$ 10.4: Why would an actuary consider using a different approach for projecting future YRT rate increases at each valuation node that differs from the approach used at point-in-time valuation?

A: When projecting future PBR reserves for purposes such as pricing or cash flow testing, some actuaries use a more simplified method to project future YRT rate increases for the inner loop than what they use for a point-in-time valuation. Some instances where an actuary might consider using a more simplified approach for future reserve projections include:

i. Simplifications across treaties-If, for point-in-time valuation purposes, the company uses a different rate increase assumption for each of its reinsurers and/or reinsurance treaties, the actuary might decide to instead apply an aggregate rate increase assumption for forecasting purposes. The aggregate rate increase assumption could be calibrated to result in reserve levels comparable to those achieved by applying a different rate increase assumption for each reinsurer and/or treaty.

ii. Simplifications for aggregation-Suppose the company sets its rate increase assumption by comparing the current YRT rates from the reinsurer to the company's anticipated mortality, in
aggregate (i.e., across all model cells). For forecasting purposes, this may require a preliminary model run to solve for the increase in aggregate. Any changes to the model that result in a change in the aggregate reinsurance premium or the aggregate mortality can result in a need to reset the rate increase assumption.

For more discussion on simplifications and estimates of the reserve, please refer to the Model Efficiency and Reserve Estimation section (Section 7) in this practice note.

## $Q$ 10.5: How does an actuary allocate a reinsurance reserve credit to individual policies for projection purposes, such as pricing?

A: The NAIC Valuation Manual requires both pre-reinsurance and post-reinsurance modeled reserves to be allocated to policies using the NPR as the basis, with actuarial judgement to assign modeled reserves in excess of the NPR to the model segment that is driving this excess amount. Then the postreinsurance less the pre-reinsurance reserve for each policy would equal the reserve credit for that policy.

For the purposes of projecting future PBR reserves for pricing purposes, the actuary might consider the following approaches for allocating the reinsurance reserve credit:

i. Allocate the reserve credit using the same allocation method as the underlying pre-reinsurance modeled reserve for projection purposes-For example, if the gross premium reserve is used to allocate the modeled reserve at the policy level, assume the GPV reserve allocation method also extends to the reinsurance component of the modeled reserve. Regardless of the required valuation allocation method, projected reserves may use differing allocation methods, such as the NPR, GPV, or DR.

ii. Allocate the reserve using the same method required in valuation-As discussed above, VM-20 refers to the NPR for allocating the reinsurance reserve credit to the policy level, which is done separately for the pre-reinsurance and post-reinsurance reserves. A consequence of this method is that policies without reinsurance inforce may possibly be allocated an implied reinsurance credit amount. However, an amendment has been adopted by the NAIC for 2020 valuations that allows actuarial judgment to be used for allocating reserves in excess of the NPR, which may help alleviate this issue.

iii. Allocate the reserve credit using the NPR reserve credit (not the entire NPR) as the basis-The NPR reserve credit is equal to the mean reserve, or unearned YRT premium. For YRT treaties, depending on contract provisions, this is commonly equal to one half the tabular mortality rate used as the basis of contract guarantees (i.e., $1 / 2$ $\mathrm{C}_{\mathrm{x}}$ ).

The actuary might take the modeling purpose and practical considerations such as model run-time into account when selecting an approach for allocating the reinsurance reserve credit for future projected PBR reserves.

## $Q$ 10.6: Why would nested modeling techniques potentially be used for modeling reinsurance cash flows when projecting $P B R$ reserves?

A: For future PBR reserve projections, the inner loop reinsurance assumptions can vary for each projected valuation date. This could be due to assuming that recapture or non-guaranteed reinsurance premium rate increases occur in varying projection years across inner loops. For instance, let's assume that a company's projection methodology for non-guaranteed premium is to increase the YRT premiums once the company prudent estimate mortality exceeds the YRT premiums for five years. In this example, the inner loop projection for the first projection year assumes the reinsurer increases non-guaranteed premiums in year 11 after taking losses in years 6-10. But for the inner loop for the 10th projection year, the reinsurer instead increases the premium in year 21 because losses are not expected until years $16-20$ of the treaty.

This example shows one way that nested modeling provides the ability to reflect different premium increases at different times/levels for each inner loop. In particular, this case contains a different set of reinsurance premium rates for each inner loop, which requires a nested modeling technique. The following table is a visual demonstration of the described example:

| Year | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Current YRT Scale | 3.0 | 32 | 3.4 | 3.6 | 3.8 | 4.0 | 4.2 | 4.4 | 4.6 | 4.8 | 5.0 | 5.2 | 5.4 | 5.6 | 5.8 | 6.0 | 6.2 | 6.4 | 6.6 | 6.8 | 7.0 | 7.2 | 7.4 | 7.6 | 7.8 |
| Rsv Calc at $\mathrm{t}=0$ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Inner loop mortality | 2.5 | 2.8 | 3.1 | 3.5 | 3.8 | 4.1 | 4.5 | 4.8 | 5.1 | 5.4 | 5.8 | 6.1 | 6.4 | 6.8 | 7.1 | 7.4 | 7.7 | 8.1 | 8.4 | 8.7 | 9.1 | 9.4 | 9.7 | 10.1 | 10.4 |
| YRT premium | 3.0 | 32 | 3.4 | 3.6 | 3.8 | 4.0 | 4.2 | 4.4 | 4.6 | 4.8 | 5.8 | 6.1 | 6.4 | 6.8 | 7.1 | 7.4 | 7.7 | 8.1 | 8.4 | 8.7 | 9.1 | 9.4 | 9.7 | 10.1 | 10.4 |
| Rsv Calc at $\mathrm{t}=10$ <br> Inner loop mortality |  |  |  |  |  |  |  |  |  |  | 4.5 | 4.8 | 5.1 | 5.4 | $5 . \pi$ | 6.1 | 6.4 | 6.7 | 7.0 | 7.3 | 7.6 | 7.9 | 8.2 | 8.5 | 8.8 |
| YRT premium |  |  |  |  |  |  |  |  |  |  | 5.0 | 5.2 | 5.4 | 5.6 | 5.8 | 8.0 | 6.2 | 6.4 | 6.6 | 6.8 | 7.6 | 7.9 | 8.2 | 8.5 | 8.8 |

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-52.jpg?height=128&width=400&top_left_y=1519&top_left_x=726" alt="image" style="width:100%;height:auto;">

<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-52.jpg?height=129&width=388&top_left_y=1519&top_left_x=1363" alt="image" style="width:100%;height:auto;">

Another example of when nested modeling techniques might be used for modeling reinsurance cash flows is when a margin is applied to the current YRT scale, and this margin is tied in some way to the effective mortality margin (i.e., the total difference between the inner loop and outer loop mortality). In this case, the YRT margin applied may decrease at each re-valuation point as the effective mortality margin decreases due to the following factors:

i. Projected increases in the credibility of the company's mortality experience. This is particularly applicable for newer blocks of business for which the company does not have credible experience.

ii. Projected increases in the amount of sufficient data for company experience.

iii. If an additional mortality margin beyond the VM-20 minimum prescribed margin is tied to each projection year (not necessarily each policy year or an age), in which case a nested modeling approach may be required.

## Q 10.7: What are considerations for modeling coinsurance or modified coinsurance (Modco) within future projected $P B R$ reserves?

A: An actuary who models coinsurance or Modco within PBR projections might use a technique similar to point-in-time valuation, such as applying the percentage quota share to reduce all cash flow components across both the inner and outer loop. Additional considerations could exist for modeling a different mortality margin based on the level/timing of coinsurance (due to having more access to mortality experience from the reinsurer), interest adjustments on modified coinsurance or funds withheld agreements, or non-guaranteed elements/charges. The presence of any or all of these elements can be addressed by using nested modeling based on the desired projection methodology.

## 11. Economic Scenario Generation

## $Q$ 11.1: What resources are available on the use of economic scenario in actuarial models?

A: General actuarial resources on the use of economic scenarios in actuarial models include the following:

- American Academy of Actuaries practice note, Scenario and Cell Reduction, 2010
- American Academy of Actuaries practice note, Life Principle-Based Reserves Under VM-20, 2017 (updated 2019)
- SOA white paper, Economic Scenario Generators: A Practical Guide, 2016

The May 2019 version of the PBA prescribed scenario generator spreadsheet (7.1.201905) and accompanying FAQ document, along with release notes for the last major version release (version 7) can be found at https://www.soa.org/tables-calcs-tools/research-scenario/.

Selected articles in past SOA section newsletters on the use of economic scenarios in actuarial models:

- "Real-World Interest Rate Models and Current Practices," The Modeling Platform, July 2015
- "PBA Corner," The Financial Reporter, March 2013

For an additional list of references and associated links, refer to the appendix of this practice note.

Q 11.2: How do economic scenarios (e.g., number, distribution, economic variables contained within) differ between outer and inner loop projections? How are the number of scenarios chosen?

A: There are multiple approaches to economic scenario generators, efficiencies, and scenario reduction techniques. There is not a "one-size-fits-all" type or number of scenarios. The "right" scenarios and "right" number of outer and inner loop scenarios will likely reflect the business purpose and the nature of the assets, liabilities, and risks. The number of scenarios selected can increase with increasing policyholder optionality (i.e., where policyholder behavior is expected to vary by economic scenario) and with the number of underlying risk factors. One question the actuary might address in determining an adequate number of scenarios to use is, "How many scenarios must be used before adding more does not materially change the conclusion of the analysis?” In particular, the NAIC

Valuation Manual requires that a sufficient number of scenarios is used to ensure that stochastic reserves are not understated.

Various technical research papers illustrate convergence requiring 10,000, 50,000, or more scenarios. Even with reduction techniques, run-times are problematic for projecting balance sheet items, especially reserves. Some actuaries might include a smaller subset of intentionally selected "representative scenarios" to reduce modeling run-time for projections, such as 1,000 scenarios. Even fewer (e.g., 200 or 500) may be used for pricing purposes, depending on the level of desired risk tail metric in the reserve or capital framework. Determining the number of scenarios in large, complex models often involves trade-offs between convergence, run-time practicality, usefulness, resource constraints, timeliness, fidelity, and accuracy. The actuary might consider these tradeoffs when determining the appropriate number of scenarios for a particular purpose.

Inner loops for reserves and capital might reflect a prescribed tool to select scenarios. At a given projection node, some actuaries would use inner loop scenarios and assumptions that are consistent with the path of the outer-loop variables up to the projection node. However, proxies for the number, distribution, and economic variables of inner loop scenarios chosen might require analysis and judgment evaluating the aforementioned trade-offs.

For more information, please refer to Varnell, E.M., Economic Scenario Generators and Solvency II, Institute of Actuaries, November 23, 2009.

## $Q$ 11.3: What role does the prescribed scenario generator play in projecting PBR reserves?

A: VM-20 requires a prescribed scenario generator be used to generate scenarios for point-in-time valuation. There is no regulatory requirement when it comes to the scenarios used to project PBR reserves. Some actuaries split the scenarios used to project PBR reserves into scenarios for the outer loops and inner loops (as the two may contain different scenario sets).

The outer loop scenarios used to project PBR reserves can be determined by the company based on the modeling task at hand (e.g., forecasting, pricing, risk modeling). Some modeling tasks might only use a single (e.g., deterministic) outer loop scenario whereas others might use multiple (e.g., stochastic) outer loop scenarios. Outer loop scenarios are generally real-world scenarios (vs. riskneutral) determined independently of the VM-20 prescribed scenario generator and can include additional risk factors besides those present in the prescribed scenarios for the time zero valuation run. Additional information on common scenario generation techniques can be found in the resources listed in Q11.1 earlier in this section and the appendix.

Each future valuation date could have its own set of inner loop scenarios. Some actuaries use the same generator prescribed for the point-in-time valuation run to produce scenarios for a future inner loop run, but with the generator's starting yield curve set to the outer loop's yield curve on the future valuation date, and the generator's mean reversion parameter for the Treasury rate updated to reflect the Treasury rates experienced by the outer loop up to the future valuation date.

## $Q$ 11.4: How are economic scenarios produced for the inner loop projections used at each future valuation date in the outer loop projection?

A: The actuary might consider both the economic state of the outer loop on the future valuation date as well as any prescriptive elements from the associated reserves or capital requirement for projection of economic variables within future inner loop runs.

Some actuaries determine interest rate and equity return scenarios for future inner loop valuation runs using the same prescribed scenario generator used for the time zero valuation run. To generate inner loop scenarios for a future valuation date, the prescribed scenario generator uses a starting yield curve (i.e., 0.25-, 0.5-, 1-, 2-, 3-, 5-, 7-, 10-, 20- and 30-year Treasury rates) and a mean reversion parameter. The starting yield curve may then be set to the outer loop's current yield curve on the valuation date. Some actuaries might then determine the mean reversion parameter at each annual revaluation node in the projection using the history of interest rates in the outer loop up to that point. The ESG for VM-20 and VM-21 relies on the 20-year Treasury rate, based on 50\% of the 36-month rolling average plus $30 \%$ of the 120 -month rolling average plus $20 \%$ of the 600 -month rolling median (rounded to the nearest quarter percent). Other ESGs may use different parameters.

The following figure shows a visual example of how both historical and outer loop projected interest rates can determine the mean reversion parameter for generating inner loop PBR stochastic scenarios at various re-valuation nodes. In the graphic, the blue line shows actual 20-year historical interest rates and the green line shows the projected 20-year interest rates in the outer loop. The path up to each point influences the reversion parameter around which the stochastic scenarios are centered around. At each re-valuation node, there might be different stochastic scenarios projected, based on the projected history up to that point—even when using the same ESG.

## Inner Loop Scenario Generation

- Inner loop scenarios are dependent on the outer loop scenario path.
- Inner Loops are generated based on the yield curve at each re-valuation date and a mean reversion parameter
- The mean reversion parameter will change over time based on a combination of historical actual rates and projected rates from the output loop scenario
<img src="https://cdn.mathpix.com/cropped/2024_03_15_4f09c645f1955e5c0e52g-55.jpg?height=1170&width=1824&top_left_y=1334&top_left_x=80" alt="image" style="width:100%;height:auto;">

Regulatory requirements have implications on the number of scenarios used for the point-in-time valuation run. However, some actuaries might decide to use fewer scenarios for forecasting future valuation date amounts while considering trade-offs between run-time and convergence.

Although scenarios can be manually generated for the point-in-time valuation run by using the Excel spreadsheet provided for the prescribed ESG, when it comes to projecting PBR reserves, some actuaries might decide to consider automating the generation of prescribed scenarios for future inner loop valuation runs (e.g., by embedding the prescribed scenario generator logic in the projection model). Automating the generation of scenarios for future inner loop valuation runs could save time and reduce errors compared to manually using the Excel spreadsheet to create scenario sets for each future valuation date in the projection.

In addition to interest and equity rate scenarios, some actuaries use current outer loop asset credit spreads as the basis for starting spreads in the inner loop valuation run that takes place at that node. Ultimate spreads for the point-in-time valuation run are prescribed in the NAIC Valuation Manual based on long-term average spreads. Some actuaries might simply reuse time zero ultimate spreads for all future valuation dates as well. Others might reset ultimate spreads for each future valuation date using long term average spreads that have been updated based on the spreads experienced in the outer loop up to each future valuation date. Similar considerations apply for determining ultimate (baseline/long-term average) default rates for future inner loop valuation runs. For example, some actuaries simply reuse time zero ultimate default rates for all future valuation dates, whereas others may reset ultimate default rates for each future valuation date. If resetting the ultimate default rates for each future VM-20 valuation, this implies not only updating the ultimate default rate, but also the second-order impacts to the spread-related factor, and maximum net spread adjustment. In addition, some actuaries also consider updating these second-order impacts, even if the ultimate rates are not updated, as the spread-related factor will change as current spreads change and the maximum net spread adjustment will change as the projected portfolio composition changes.

For randomly selected subsets of scenarios, some actuaries refer to a method for estimating the CTE amount published by Manistre and Hancock. ${ }^{1}$ However, it is important to understand this test can have limitations and might be appropriate only when using randomly selected subsets of a pool of scenarios.

## Q 11.5: How can scenarios for future valuation dates be validated?

A: Some actuaries validate inner loop scenarios using output from a separate source using the same scenario generator and compare the results. For the ESG prescribed in the NAIC Valuation Manual, the Excel spreadsheet model available on the NAIC website can generate a corresponding set of scenarios from the outer loop yield curve and mean reversion parameter on the valuation date. The two sets of scenarios might be similar depending on how the ESG logic is embedded in the projection model. Other actuaries create a scatter plot that compares the projected interest rate to reserves within each scenario and review outliers. For general discussion on validation techniques for projections, refer to Section 5 of this practice note.[^0]

## 12. Assets

## $Q$ 12.1: How does an actuary ensure that asset projections for future valuation nodes are in line with VM20 and VM-21 prescription?

A: There are a number of VM-20 and VM-21 prescriptions related to projecting assets for time zero valuation, such as the collar test on starting assets, the use of prescribed spreads, methods for projecting market and book values, and the requirement to adjust reinvestments and/or any non-prescribed asset spreads related to the alternative (or guardrail) reinvestment strategy requirement.

For future inner loop runs, when projecting variables that have prescribed components (e.g., spreads and asset defaults), some actuaries consider the inner loop/outer loop relationship described in this note. As a simplification for re-projecting spreads and default rates, the actuary might freeze the initial projection of spreads and default rates and use them as point-in-scale in the projection. Additional detail related to spreads and asset defaults for future inner loop valuation runs can be found in Q11.4 of this practice note.

VM-20 and VM-21's alternative (or guardrail) fixed income reinvestment strategy requirement states that the modeled reinvestment strategy shall be adjusted so that the modeled reserve is not less than when assuming all fixed income is reinvested in public non-callable corporate bonds, $50 \%$ with a PBR credit rating of 3 and 50\% with a PBR credit rating of 6 . In determining whether a company is required to use the alternative reinvestment, the reserve calculation might be performed twice (once with the company assumption, once with the alternative), or by demonstrating the weighted average company net spread on reinvestment assets is lower or higher than the net spread under the alternative (or guardrail) assumption. Such a demonstration might not be necessary for future valuation nodes, but the actuary might want to consider whether it can help in understanding how a company's investment strategy may change (or not) on an ongoing basis in relation to the VM-20 alternative investment strategy.

## $Q$ 12.2: How does an actuary ensure that the asset mix in future durations is still representative of and consistent with the company's investment policy?

A: The mix of assets in the portfolio can change over the course of the projection as existing assets run off and new assets are purchased. Some actuaries validate changes in the asset mix over time by reviewing balance sheet projections. For example, changes in the mix between public bonds and mortgages, or pre-tax interest maintenance reserve (PIMR) balances, can be expected to be consistent with the liability cash flows and anticipated impact of investment strategy given the projected economic scenario. Depending on the projection purpose, the outer loop might reflect the actual investment strategy and projected liability profile of the block, whereas the inner loop is intended to reflect relevant asset assumptions for valuation purposes.

As with the time zero valuation runs, the actuary might consider whether the projection of derivatives in future inner loop runs is expected to be consistent with the company's hedging strategy and derivatives policy given the projected scenario and valuation requirements.

The actuary might consider whether the inner loop disinvestment strategy needs to be consistent with the company's investment policy and not expected to produce bias or arbitrage in the models. For example, by always selling shorter-duration assets, the projected asset portfolio could become duration mismatched relative to liabilities and produce distorted VM-20 modeled reserves as a result. The borrowing assumption might be another potential source of bias in the disinvestment strategy for the actuary to consider. Borrowing rates can be set up dynamically in the model relative to scenario rates to keep borrowing consistent with the company's actual borrowing strategy.

## $Q$ 12.3: How does an actuary implement VM-20's starting asset collar for each of the future inner loop projections nested within the outer loop?

A: VM-20 requires the starting value of assets in the model to be within $98 \%$ of the modeled reserve (i.e., max of the DR and SR) and the maximum of $102 \%$ of the modeled reserve, NPR (net of due and deferred premiums), and zero in aggregate across all model segments. Many commercial modeling platforms have procedures to automatically iterate time zero VM-20 valuation runs until starting assets are within the collar. Some actuaries use such procedures to automatically establish starting assets within the collar for the inner loop projections beginning at each future valuation date in the projection. Note that VM-20 allows either the Gross Premium Valuation (GPV) or Direct Iteration Method (DIM) method to be used for calculating the DR. The DIM method solves for the amount of starting assets to settle all liabilities or, in other words, result in an ending surplus of zero. If the SR is not being projected, then using the DIM method to calculate future DRs might eliminate the need to perform the collar test for future inner loop projections.

Because the iterative process of solving for the starting assets can be time-consuming, especially when liability cash flows depend on asset cash flows, some actuaries might consider using a wider collar for future valuation dates in order to lower run-time. However, future reserves may become distorted as the collar is widened, particularly when the SR is being forecasted. Actuaries might also consider using a simplification approach to lower run-times associated with asset/liability interdependencies, such as using linear regression to link credited rates to economic scenarios while accounting for the liability duration of the block. The actuary might consider whether all simplifications, even those only used for projected reserves, should be validated. For example, the linear regression approach described could be validated by back-testing against actual credited rates.

## $Q$ 12.4: What approaches are used to re-scale starting assets for the future inner loop projections used to determine future modeled reserves in the outer loop projection?

A: Two approaches for re-scaling assets (e.g., to satisfy the VM-20 collar requirement) used by some actuaries are the pro-rata and cash/disinvestment approaches. The pro-rata approach implicitly assumes that either (i) the company has available comparable assets outside of the segment being modeled that are similar in nature to those available to the segment being modeled (i.e., the assets are "grossed-up"), or (ii) the assets available to the segment being modeled are all reduced in a pro-rata manner so the ending asset amount is consistent with the needs of the segment (i.e., the assets are "scaled-down"). The cash/disinvestment approach assumes the company would not move assets into or out of the modeling segment as needed, but would add cash to the starting asset balance or sell assets as needed. When using the cash/disinvestment approach the actuary might consider whether adding cash or disinvestment does generate excessive trading in the model.

## Q 12.5: What are some other considerations when modeling PBR assets in nested models?

A: The actuary might consider calculating and projecting PBR reserves using an integrated asset-liability model or separate liability and asset models. Integrated models can be more complex but more accurate as they allow for the natural, dynamic interaction between assets and liabilities. Some actuaries might find the simplified approach of using distinct liability and asset models to be appropriate in some instances, such as those involving products that are not interest-sensitive.

Another consideration is the economic scenario for the outer loop and its impact on economic scenarios for future inner loop runs and projected reserves. Running sensitivities on the outer loop economic scenario might be used to better understand how future scenarios and future reserves can change depending on the scenario.

See Q11.4 in this practice note for more detail on how economic scenarios for future inner and outer loop runs can be kept consistent.

## $Q$ 12.6: What methods are used to project future hedging programs?

A: The actuary might consider the purpose of the projected PBR reserves and any applicable regulations when determining how future hedges should be modeled, as certain regulations can limit the actuary's ability to reflect the existence of hedges in the projected reserves. For instance, VM-20 and VM-21 allow for future hedging programs to be reflected in the reserve calculation if they are part of a CDHS (refer to Q1.11 for a description of a CDHS).

Other factors some actuaries might consider in determining whether to model future hedging programs include materiality and modeling complexity. Some actuaries choose to model a future hedging program only if it is deemed to be a key component of the company's strategy for managing the risks associated with that product.

To reflect the impact of future hedging programs, the actuary might include all expected costs and benefits associated with the hedging program within the projection scenario. This can include such things as residual risks and frictional costs, such as transaction costs and administrative fees. Some actuaries run a separate hedging model to determine the expected costs and benefits of the hedging program within each scenario and then feed these costs and benefits into the PBR projection model. For the purposes of determining the expected cost of future derivative instruments, any number of derivative pricing frameworks might be used, including Black-Scholes.

If anticipating future changes to the modeled hedging program, some actuaries might decide to model the hedging program as it is expected to exist at each point in the future. Other actuaries might choose to model the hedging program in its current form for the entire projection horizon.

## $Q$ 12.7: How should nontraditional assets be included in projections?

A: If nontraditional assets are to be included in the projection, some actuaries give additional scrutiny to the methodology and assumptions being used to model these assets. Depending on the projection purpose, the outer loop assumptions might reflect best-estimate nontraditional asset assumptions, whereas inner loop projections may need additional care to ensure compliance with valuation requirements. For example, any asset class not specifically identified in VM-20 can be modeled so that investment returns are consistent with methods described for the other types of assets included in the NAIC Valuation Manual.

Some actuaries consider how these assets are reflected in the starting asset balances for inner loop projections. When included, the starting balances used for these nontraditional assets might be based on appropriate annual statement values.

## $Q$ 12.8: What is considered when using externally projected asset cash flows or balances?

A: If models rely on cash flows that are being calculated by an external source, the actuary may wish to consider the assumptions being used to produce those cash flows and how they interact with the inner and outer loop projections.

When asset cash flows are generated from a separate source, the actuary might consider how the scenario generation process for inner loops impacts the projections for each asset type being externally projected. The actuary could also want to consider ways in which to ensure consistent economic scenario data are applied in the external system, as well as the external system output being applied in the model as intended.

Some of the factors that can vary across projection paths for externally projected assets include assumptions of yield curves, default rates, and spreads. This could include multiple cash flow projections produced for the inner loop and outer loop projections. In addition, different cash flow projections may be needed for future reinvestment points if the externally projected assets are part of the investment strategy being modeled.

## $Q$ 12.9: How does the model handle negative cash flows and negative overall asset balances?

A: When negative net cash flows occur in the projection, some actuaries assume that the company borrows to cover the shortfall, while others assume that the company sells existing assets. When modeling negative assets, the actuary might reflect the company's expected cost of borrowing. When selling assets at market value, the actuary might consider whether the assumptions used to determine the market value of the assets sold are consistent with the market value of assets purchased.

Some actuaries ensure to model assets adequacy to back projections of PBR reserves over the entire projection horizon. In particular, once the portfolio of assets has exhausted, the actuary might find that not enough assets remain later in the projection horizon to support the modeled reserve. Some actuaries will assume that the company borrows assets in this scenario, while others might assume that the assets needed to back the reserve come from the company's surplus portfolio. Some actuaries might consider scenario, duration matching strategy, or potential company limits on the borrowing (either as an absolute dollar amount or a percentage of assets in the portfolio).

## Appendix - External References

## Definitions and Overview

## 1) Definitions \& 2) Overview

i. Society of Actuaries; Nested Stochastic Modeling for Insurance Companies (November 2016). https://www.soa.org/research/nested-stochastic-modeling-report.pdf

ii. Society of Actuaries; Impact of VM-20 on Life Insurance Product Development (November 2016).

https://www.soa.org/Files/Research/Projects/2016-impact-vm20-life-insurance-product.pdf

iii. American Academy of Actuaries; Asset Adequacy Analysis (September 2017).

https://www.actuary.org/files/publications/Asset_Adequacy_PN_092517.pdf

## High-Level Subject Areas

## 3) General PBA Projections

i. National Association of Insurance Commissioners; Valuation Manual (January 2018). https://www.naic.org/documents/prod_serv_2018_valuation_manual.pdf

ii. American Academy of Actuaries, Actuarial Standards Board; Principle-Based Reserves for Life Insurance Products under the NAIC Valuation Manual (September 2017); Actuarial Standard of Practice No. 52.

http://www.actuarialstandardsboard.org/asops/principle-based-reserves-life-productsnaic-valuation-manual/

iii. American Academy of Actuaries; Life Principle-Based Reserves (PBR) Under VM-20 (January 2019).

https://www.actuary.org/sites/default/files/files/publications/VM_20_PN_Revised_Jan uary_2019_Final.pdf

iv. Society of Actuaries; Understanding VM-20 Results (August 2017). https://www.soa.org/globalassets/assets/Files/Research/Projects/2017-understand-vm20-results.pdf

v. National Association of Insurance Commissioners; "Additional Valuation Manual Q\&A for LATF Consideration” (August 2017).

https://www.naic.org/documents/cmte a latf exposure vm questions\&responses.doc $\underline{\mathrm{X}}$
vi. The University of Illinois at Urbana-Champaign, Department of Mathematics; Term NPR and DR Exploration in VM-20 Reserves.

https://math.illinois.edu/system/files/inline-files/Proj3AY1516-

report.pdf?_sm_au_iVVQSFJSOJtRwrDM

vii. Laguerre; "Implementing VM-20" (July 2016); Society of Actuaries Product Development Section, Product Matters, pages 32-25.

https://www.soa.org/globalassets/assets/library/newsletters/product-developmentnews/2016/july/pro-iss104.pdf

viii. Slutsker, Piotrowski and Lankowski; "The Details Behind Principle-Based Reserving Implementation” (May 2017); American Academy of Actuaries, Contingencies, May/June 2017 issue.

http://contingencies.org/details-behind-principle-based-reserving-implementation/

## 4) Analysis and Reporting

i. Society of Actuaries; Understanding VM-20 Results (August 2017). https://www.soa.org/globalassets/assets/Files/Research/Projects/2017-understand-vm-20results.pdf

## 5) Governance and Validation

i. American Academy of Actuaries; Model Governance, Some Considerations for Practicing Life Actuaries (April 2017). https://www.actuary.org/files/publications/Model_Governance_PN_042017.pdf

ii. American Academy of Actuaries; Life Principle-Based Reserves (PBR) Under VM-20 (January 2019).

https://www.actuary.org/sites/default/files/files/publications/VM_20_PN_Revised_Jan uary_2019_Final.pdf

iii. National Association of Insurance Commissioners; Valuation Manual (January 2018); VM-31, pages 227-250; VM-G, pages 293-296. https://www.naic.org/documents/prod_serv_2018_valuation_manual.pdf

iv. Society of Actuaries; Impact of VM-20 on Life Insurance Product Development (November 2016). https://www.soa.org/Files/Research/Projects/2016-impact-vm20-life-insurance-product.pdf

v. Society of Actuaries; Impact of VM-20 on Life Insurance Product DevelopmentPhase 2 (July 2017). https://www.soa.org/globalassets/assets/files/research/projects/2017-impact-vm20-lifeinsurance-product-phase-2.pdf
vi. American Academy of Actuaries, Actuarial Standards Board; Principle-Based Reserves for Life Insurance Products under the NAIC Valuation Manual (September 2017); Actuarial Standard of Practice No. 52.

http://www.actuarialstandardsboard.org/asops/principle-based-reserves-life-productsnaic-valuation-manual/

vii. American Academy of Actuaries, Actuarial Standards Board; Actuarial Communications (December 2010); Actuarial Standard of Practice No. 41. http://www.actuarialstandardsboard.org/asops/actuarial-communications/

viii. American Academy of Actuaries, Actuarial Standards Board; Responding to or Assisting Auditors or Examiners in Connection with Financial Audits, Financial Reviews, and Financial Examination; (September 2016); Exposure Draft, Proposed Revision of Actuarial Standard of Practice No. 21. http://www.actuarialstandardsboard.org/asops/responding-assisting-auditorsexaminers-connection-financial-statements/

ix. American Academy of Actuaries "Model Governance Checklist,” (August 2016) https://www.actuary.org/files/publications/PBRChecklist Final.pdf

x. Rudolph; "Understanding VM-20 Results—Research summary" (December 2017); Society of Actuaries Financial Reporting Section, The Financial Reporter, pages 1719. https://www.soa.org/globalassets/assets/library/newsletters/financialreporter/2017/december/fr-2017-iss111.pdf

## 6) Pricing

i. Society of Actuaries; Impact of VM-20 on Life Insurance Product Development (November 2016). https://www.soa.org/Files/Research/Projects/2016-impact-vm20-life-insurance-product.pdf

ii. Society of Actuaries; Impact of VM-20 on Life Insurance Product DevelopmentPhase 2 (July 2017). https://www.soa.org/globalassets/assets/files/research/projects/2017-impact-vm20-lifeinsurance-product-phase-2.pdf

## 7) Model Efficiency and Reserve Estimation

i. Modeling Efficiency Work Group, American Academy of Actuaries; "Model Efficiency Bibliography for Practicing Actuaries” (December 2011). http://dev.actuary.org/files/Modeling\ Efficiency\ Bibliography\ \ Update\ 12-11.pdf

ii. American Academy of Actuaries, Scenario and Cell Model Reduction (September 2010).

https://www.actuary.org/files/Scenario\ and\ Cell\ Model\ Reduction\  PN\%20Final\%20092210.4.pdf/Scenario\%20and\%20Cell\%20Model\%20Reduction\%2 0PN\%20Final\%20092210.4.pdf

iii. Dardis; "Model Efficiency in the U.S. Life Insurance Industry" (April 2016); Society of Actuaries Modeling Section, The Modeling Platform. https://www.soa.org/globalassets/assets/Library/Newsletters/The-ModelingPlatform/2016/april/mp-2016-iss3-dardis.pdf

iv. Dardis and Motiwalla; "Model Governance: Is YOUR Company There Yet? Intersection of Model Governance and Model Efficiency” (August 2016); Society of Actuaries Valuation Actuary Symposium. https://www.soa.org/Files/Pd/2016/model-gov/pd-2016-model-gov-intersectionmodel-efficiency.pdf

v. American Academy of Actuaries; Model Governance, Some Considerations for Practicing Life Actuaries (April 2017).

https://www.actuary.org/files/publications/Model_Governance_PN_042017.pdf

vi. Craighead; "PBA Reserves and Capital Modeling Efficiency: Representative Scenarios and Predictive Modeling” (June 2008); Society of Actuaries Financial Reporting Section, The Financial Reporter, pages 17-24. https://www.soa.org/globalassets/assets/library/newsletters/financialreporter/2008/june/frn-2008-iss73.pdf

vii. Zajac; “Term Conversions - A Reinsurer’s Perspective” (June 2012); Society of Actuaries Product Development Section, Product Matters, pages 32-25. https://www.soa.org/globalassets/assets/Library/Newsletters/Product-DevelopmentNews/2012/june/pro-2012-iss83-zajac.pdf?_sm_au_=iVVjr5ZscH7JcS5V

viii. Hezhong; "Term Conversions: Pricing and Reserves” (March 2017); Society of Actuaries Product Development Section, Product Matters, pages 20-23. https://www.soa.org/globalassets/assets/Library/Newsletters/Product-DevelopmentNews/2017/pro-2017-iss106.pdf

## Specific Topics

8) Mortality

i. Slutsker, Piotrowski and Lankowski; "The Details Behind Principle-Based Reserving Implementation” (May 2017); American Academy of Actuaries, Contingencies, May/June 2017 issue. http://contingencies.org/details-behind-principle-based-reserving-implementation/

## 9) Policyholder Behavior and Non-Guaranteed Elements

i. Society of Actuaries; Modeling of Policyholder Behavior for Life Insurance and Annuity Products: A Survey and Literature Review (2014). https://www.soa.org/Files/Research/Projects/research-2014-modeling-policy.pdf

ii. American Academy of Actuaries; Life Principle-Based Reserves (PBR) Under VM-20 (January 2019).

https://www.actuary.org/sites/default/files/files/publications/VM_20_PN_Revised_Jan uary 2019 Final.pdf

iii. Gagnon, Cardinal, Steenman and Zhang; "PBR Stochastic Reserve—Challenges and Possible Solutions” (October 2017); Society of Actuaries, Annual Meeting \& Exhibit. https://www.soa.org/Files/e-business/pd/events/2017/annual-meeting/pd-2017-10annual-session-030.pdf

iv. American Academy of Actuaries, Actuarial Standards Board; Principle-Based Reserves for Life Insurance Products under the NAIC Valuation Manual (September 2017); Actuarial Standard of Practice No. 52.

http://www.actuarialstandardsboard.org/asops/principle-based-reserves-life-productsnaic-valuation-manual/?_sm_au_=iVVQSFJSOJtRwrDM

v. Society of Actuaries; Nested Stochastic Modeling for Insurance Companies (November 2016).

https://www.soa.org/research/nested-stochastic-modeling-report.pdf

vi. Rudolph; "Understanding VM-20 Results-Research summary" (December 2017); Society of Actuaries Financial Reporting Section, The Financial Reporter, pages 1719.

https://www.soa.org/globalassets/assets/library/newsletters/financial-

reporter/2017/december/fr-2017-iss111.pdf

## 10) Reinsurance

i. American Academy of Actuaries; Life Principle-Based Reserves (PBR) Under VM-20 (January 2019).

https://www.actuary.org/sites/default/files/files/publications/VM_20_PN_Revised_Jan uary_2019_Final.pdf

ii. Life Reinsurance Working Group, American Academy of Actuaries; "Work Group Comment Letter to LATF on YRT Reinsurance Premiums” (November 2017). https://www.actuary.org/sites/default/files/files/publications/Academy_Reinsurance_ WG_YRT_Comments_to_LATF_110717.pdf

## 11) Economic Scenarios

i. Varnell; Economic Scenario Generators and Solvency II (November 2009); Institute of Actuaries.

https://www.actuaries.org.uk/documents/economic-scenario-generators-and-solvencyii

ii. Society of Actuaries, "Economic Scenario Generators” (May 2019); Academy Scenario Generator (AIRG); Frequently Asked Questions-May 2019. https://www.soa.org/tables-calcs-tools/research-scenario/

iii. Society of Actuaries; Economic Scenario Generators, A Practice Guide (July 2016). https://www.soa.org/globalassets/assets/Files/Research/Projects/research-2016economic-scenario-generators.pdf

iv. American Academy of Actuaries, Scenario and Cell Model Reduction (September 2010).

https://www.actuary.org/files/Scenario\ and\ Cell\ Model\ Reduction\  PN\%20Final\%20092210.4.pdf/Scenario\%20and\%20Cell\%20Model\%20Reduction\%2

OPN\%20Final\%20092210.4.pdf

v. Rudolph; "PBA Corner” (March 2013); Society of Actuaries Financial Reporting Section, The Financial Reporter, page 1.

https://www.soa.org/globalassets/assets/Library/Newsletters/Financial-

Reporter/2013/march/fr-2013-iss92.pdf

vi. Orduña, Lin and Larochelle; "Real-World Interest Rate Models and Current Practices" (July 2015); Society of Actuaries Modeling Section, The Modeling Platform, pages 1, $4-10$;

https://www.soa.org/globalassets/assets/Library/Newsletters/The-Modeling-

Platform/2015/july/modeling-platform-2015-vol-1-iss-1.pdf

vii. The Proxy Model Working Party, Institute and Faculty of Actuaries; Heavy Models, Light models and Proxy Models: A Working Paper (February 2014). https://www.actuaries.org.uk/documents/heavy-models-light-models-and-proxymodels-working-paper

## 12) Assets

i. Slutsker, Kehrberg and Nicholsen; “Asset Modeling Challenges for VM-20" (March 2018); Society of Actuaries Financial reporting Section, The Financial Reporter. https://www.soa.org/Library/Newsletters/Financial-Reporter/2018/march/fr-2018iss112.pdf

ii. American Academy of Actuaries; Asset Adequacy Analysis (September 2017). https://www.actuary.org/files/publications/Asset Adequacy PN 092517.pdf
iii. Patel and Sarfatti; "AG-43 and C3 Phase 2 Proposed Revisions: Overview and Quantitative Impact Study Results” (May 2017); Society of Actuaries, Life \& Annuity Symposium.

https://www.soa.org/pd/events/2017/val-act/pd-2017-august-vas-session-025.pdf


[^0]:    ${ }^{1}$ Manistre and Hancock; "Variance of the CTE Estimator”; NAAJ; Vol 9, No. 2 (April 2005); pages 129-156.


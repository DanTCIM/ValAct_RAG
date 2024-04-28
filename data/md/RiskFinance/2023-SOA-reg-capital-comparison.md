
## Regulatory Capital Adequacy for Life Insurance Companies <br> A Comparison of Four Jurisdictions

JULY | 2023

AUTHORS Ben Leiser, FSA, MAAA

Janine Bender, ASA, MAAA

Brian Kaul
Society of Actuaries Corporate Finance \& Enterprise Risk Management (CFE track) Curriculum Committee

Society of Actuaries Individual Life \& Annuities (ILA track) Curriculum Committee

Society of Actuaries Research Institute

Caveat and Disclaimer

The opinions expressed and conclusions reached by the authors are their own and do not represent any official position or opinion of the Society of Actuaries Research Institute, the Society of Actuaries or its members. The Society of Actuaries Research Institute makes no representation or warranty to the accuracy of the information.

Copyright (C) 2023 by the Society of Actuaries Research Institute. All rights reserved.

## CONTENTS

	Executive Summary ..... 4
	Section 1: Introduction ..... 5
	Section 2: Overview of Capital ..... 6
	Section 3: Regulatory Approaches to Capital ..... 8
	Section 4: US Capital Requirements ..... 10
	4.1 Regulatory Action ..... 12
	4.2 Group Level Capital ..... 12
	4.3 Future Updates ..... 13
	Section 5: Canadian Solvency Requirements ..... 14
	5.1 Regulatory Action ..... 15
	5.2 Future updates ..... 15
	Section 6: Solvency II ..... 16
	6.1 Regulatory Action ..... 19
	6.2 Future Updates ..... 19
	Section 7: Bermuda Solvency Requirements ..... 19
	7.1 Regulatory Action ..... 22
	7.2 Future Updates ..... 22
	Section 8: Model Results and Comparison ..... 23
	Section 9: Conclusion ..... 29
	Section 10: Acknowledgments ..... 30
	Appendix A: Solvency II Formulas ..... 31
	Appendix B: Bermuda Solvency Capital Requirement Formulas ..... 33
	Appendix C: Model Simplifications ..... 37
	C. 1 Simplifications that apply to all jurisdictions ..... 37
	C. 2 Simplifications specific to US RBC ..... 37
	C. 3 Simplifications specific to Canadian LICAT ..... 37
	C. 4 Simplifications specific to SOLVENCY II. ..... 38
	C. 5 Simplifications specific to Bermuda Insurance Solvency.... ..... 38
	Glossary ..... 39
	References ..... 41
	About The Society of Actuaries Research Institute ..... 43

## Regulatory Capital Adequacy for Life Insurance Companies A Comparison of Four Regimes

## Executive Summary

The purpose of this paper is to introduce the concept of capital and key related terms, as well as to compare and contrast four key regulatory capital regimes. Not only is each regime's methodology explained with key terms defined and formulas provided, but illustrative applications of each approach are provided via an example with a baseline scenario. Comparison among these capital regimes is also provided using this same model with two alternative scenarios.

The four regulatory required capital approaches discussed in this paper are National Association of Insurance Commissioners' (NAIC) Risk-Based Capital (RBC; the United States), Life Insurer Capital Adequacy Test (LICAT; Canada), Solvency II (European Union), and the Bermuda Insurance Solvency (BIS) Framework which describes the Bermuda Solvency Capital Requirement (BSCR). These terms may be used interchangeably. These standards apply to a large portion of the global life insurance market and were chosen to give the reader a better understanding of how required capital varies by jurisdiction, and the impact of the measurement method on life insurance company capital.

All of these approaches are similar in that they identify key risks for which capital should be held (e.g., asset default and market risks, insurance risks, etc.). However, they differ in significant ways too, including their defined risk taxonomy and risk diversification / aggregation methodologies, as well as required minimum capital thresholds and corresponding implications. Another key difference is that the US's RBC methodology is largely factor-based, while the other methodologies are model-based approaches. For the model-based approaches, Solvency II and BIS allow for the use of internal models when certain conditions are satisfied. Another difference is that the RBC methodology is largely derived using book values, while the others use economic-based measurements.

As mentioned above, this paper provides a model that calculates the capital requirements for each jurisdiction. The model is used to compare regulatory solvency capital using identical portfolios for both assets and liabilities. For simplicity, we have assumed that all liabilities originated in the same jurisdiction as the calculation. As the objective of the model is to illustrate required capital calculation methodology differences, a number of modeling simplifications were employed and detailed later in the paper. The model considers two products - term insurance and payout annuities, approximately equally weighted in terms of reserves. The assets consist of two non-callable bonds of differing durations, mortgages, real estate, and equities. Two alternative scenarios have been considered, one where the company invests in riskier assets than assumed in the base case and one where the liability mix is more heavily weighted to annuities as compared to the base case.

<img src="https://cdn.mathpix.com/cropped/2024_04_13_59edaaf1c3ec26f7eb72g-04.jpg?height=244&width=1521&top_left_y=2120&top_left_x=234" alt="image" style="width:100%;height:auto;">

## Section 1: Introduction

On the surface, "capital" is an easy concept, both to calculate and to understand.

$$
\text { Capital = Assets }- \text { Liabilities }
$$

However, beyond this basic definition, the concept of capital is quite complex. Capital can be subdivided into various components, such as required and available capital, so context is critical for interpreting the meaning of the word capital when not using additional descriptors. The method under which assets and liabilities are valued must be considered. Are the liabilities valued using formulaic methods and prescribed assumptions or principles-based methods and best estimate assumptions? How much conservatism is embedded in the liabilities and is this implicit or explicit? Are assets valued on a book or market basis? How severe a stress does the regulator assume when setting required capital level? Is the binding capital constraint regulatory required capital or some other basis such as rating agency capital or an internal capital model?

Life insurance companies are regulated by the jurisdiction in which the company transacts business. Regulations in each jurisdiction are intended to protect the public and the policyholders in that jurisdiction. Regulators will choose a methodology for determining regulatory required capital and corresponding thresholds that fit the unique needs of their jurisdiction. The amount of regulatory capital to be held depends on the jurisdiction's methodology, as well as any prescribed requirements for assumptions and valuation methods.

This paper will provide a brief overview of regulatory required capital, explain four (4) regulatory capital regimes, and highlight the differences among them. The four regimes discussed in this paper are RBC, LICAT, Solvency II, and BSCR, and apply to a large portion of the global life insurance market. These capital regimes were chosen to give the reader an understanding of how required capital varies by regime, and the impact of the measurement method on life insurance company capital. While there are similarities between the approaches (e.g., specific risks identified for which measurement methodologies are prescribed), there are also key differences, such as accounting method used as a starting point, being model-based or factor-based, and applicability of standards at the group level versus the entity level.

This paper will provide brief descriptions of proposed changes to regulatory capital frameworks and reflects information as of October 2022, but not necessarily beyond. The examples provided herein, using simplistic asset and liability portfolios, are meant to be illustrative and demonstrate differences between the regime requirements.

The focus is on the long-term commitments made in connection with life insurance and annuities, although health insurance and property and casualty risks are mentioned where they are part of regulatory formulas. Capital requirements for short-term insurance have several conceptual distinctions not addressed in this paper.

## Section 2: Overview of Capital

The simplest concept of capital is total capital - this is simply the difference between assets held by the company and liabilities owed by the company. However, components of this quantity deserve discussion. Total capital can be divided into "required" capital and "available" capital. Required capital is capital that must be set aside to meet targeted regulatory minimum thresholds, and typically held in relatively safe investments to cover the potential for future adverse events. Available capital can be used for growth of the current business, expansion into new business opportunities, enhancement of operational effectiveness and efficiency, competitive positioning, and other strategic purposes. Although they have slightly different meanings amongst industry professionals and across jurisdictions, the terms "capital" and "surplus" are used interchangeably within this paper.

In general, capital is a positive amount, with the company considered insolvent otherwise. However, as a number, capital isn't particularly meaningful, other than to determine if the company is solvent at the moment the balance sheet was created. Once the uses for capital are understood, the level of capital takes on meaning. Capital is needed to cover adverse business cash flows over a specified period, but can also be used to expand the business by investing into current lines of business or new business opportunities.

Measurement of both assets and liabilities depends on the accounting system being used, and the capital measurements may depend on these as well. In the United States, statutory accounting focuses on the balance sheet, with both assets and liabilities held at Book Value ${ }^{1}$, with liabilities generally held at a conservative level. Publicly held insurers in the US are subject to Generally Accepted Accounting Principles (US GAAP) for public financial reporting purposes, where assets and liabilities are held at either Book Value or Market Value depending on the company's intended use of the assets, and income is recognized (amortized) over the life of the insurance policy. For the same company, the dollar amount of capital would likely be different between Statutory and GAAP financial statements. European and Canadian insurers are subject to International Financial Reporting Standards (IFRS) accounting methods, so it is possible that an insurance company operating in the US will be subject to multiple accounting methodologies and calculating three different measures for capital. In addition, rating agencies have their own perspectives and measurement systems for capital adequacy. Multiple measurement systems are not unique to the US. Each company will decide which accounting/financial statement will drive internal decisions, but, since the regulatory capital requirements are generally published values, the company may need to consider regulatory capital requirement disclosures as part of its overall assessment of capital needs.

Insurance company stakeholders may have different views of how capital should be allocated. One stockholder may want short term gains and expect as much capital as possible to be returned in dividends. Another will want a longterm return on investment and expect capital to be used to expand the company's presence in existing lines of business or enter new profitable markets. Those who hold company debt want to be paid the promised amounts, so prefer a conservative level of capital held to better ensure the receipt of coupons and return of principal. The regulator and policyholder will want to ensure that the company is around long enough to pay claims on their policies, so also prefers conservative levels of capital held. Company management will have balancing perspectives of having enough capital to maintain operational flexibility, withstand adverse scenarios and enhance the company's marketing profile from higher ratings, but not excessive amounts that result in financial inefficiency and reduced product competitiveness due to the cost of capital.

All of these capital needs and perspectives must be considered in determining target capital. If capital exceeds targeted amounts, it may be returned to the owners via dividends. If it is deficient relative to targeted thresholds, there may be a desire to raise additional amounts. The varying perspectives of different stakeholders extend not just[^0]to the dollar amount of capital but also to the quality. Tiered capital such as debentures and hybrid debt can be used to address the risk tolerances of policyholders at a lower cost than shareholder equity. Regulators might allow the use of lower capital tiers to meet regulatory required capital. Debt rating agencies would be less tolerant of a situation in which a company would protect policy benefits by defaulting on debentures.

Many companies consider amounts between total capital and either target capital or regulatory capital as "surplus", but this definition is not universal, and varies by jurisdiction.

A company may determine its capital needs based on an "economic" view of its business, in which both assets and liabilities are valued on a best estimate basis including consideration for the cost to bear capital relating to retained risks. "Economic capital" is the difference between the assets and liabilities. The required economic capital is often determined such that the organization maintains a specified level of confidence in remaining solvent.

Policyholders may not have the knowledge or information to determine whether an insurance company will be able to pay the benefits being promised. Instead, these consumers are represented by regulators who do have that knowledge and focus on policyholder protection. The policyholder protection concern takes the form of ensuring the company's ability to pay current and future claims. The regulators are also concerned about systemic risks to the insurance or financial services markets, and the capital requirements are meant to mitigate the possibility of failure of both individual companies and the market as a whole.

The term "regulatory required capital" describes the amount of capital regulators require the company to maintain for policyholder protection purposes and provides a key signal to the regulator of when to step in. This is the focus of this paper.

## Section 3: Regulatory Approaches to Capital

The four regulatory required capital approaches discussed in this paper are model-based (i.e., required capital is calculated based on projections of future cash flows) or factor-based (i.e., required capital is calculated based on applying factors to business attributes). LICAT, Solvency II, and BIS generally require modeling of assets and liabilities to determine required capital and may also involve some factor-based components. NAIC RBC is primarily factorbased, with some model-based components. In a strictly factor-based approach, financial statement line items or other business quantities are multiplied by factors specific to that item to arrive at the pre-diversified, individual risk required capital amount. It is noted however that the factors themselves may have been determined using industrywide models. Many of the regulatory required capital methods involve determining risk capital for individual risks, and then combining the individual risk capital amounts to arrive at an aggregate required capital amount using a correlation matrix approach. Model-based approaches tend to leave more judgment to the actuary but are subject to regulatory review and approval of their assumptions and methodology. None of the regulatory approaches discussed in this paper are strictly model-based or strictly factor-based; all use a combination of the two.

The risks considered for solvency capital requirements fall into several broad categories - liability risks, investment risks, and operational risks. Most of these risks are further subdivided. For example, the investment risk may have separate calculations for:

- Borrower default (which may vary by credit quality and duration)
- Asset type (including equities, real estate and mortgages)
- Assets issued by affiliated companies
- Interest rate
- Concentration
- Spread
- Trading counterparty default
- Liquidity

Insurance or liability risks may have separate calculations for:

- Mortality
- Longevity
- Morbidity
- Policyholder behavior
- Expenses
- Catastrophe

Depending upon the jurisdiction, the investment risks may be separated into credit risks and market risks. Credit risks are those related to risk of default on principal and income from the asset, such as bond coupons or mortgage payments, and may also include risk associated with the impact on the balance sheet associated with movements in credit spreads. Market risks are related to the other drivers of change in price, such as changes in the level of interest rates and equity market and exchange rate movements, which may include views of future credit risk. Market risks often involve liability risks as well as asset performance. Policyholders may vary their premium payments, withdrawal, loan and lapse behavior, and similar actions related to their policies as investment markets change. The changes to policy cash flows impact investment and reinvestment cash flows. The combination of both policyholder behavior and investment cash flows impacts market risk to the company.

As described above, correlation (or lack thereof) among different asset and liability risks is considered in determining the aggregate amount of required regulatory capital. Companies who have a diversified portfolio of insurance products will generally calculate a lower required capital amount than companies with single lines of
business, all else equal. For example, mortality improvement would lead to later death benefit payments, but longer annuity benefit payments. The risks are not completely offsetting, but the more diversified the liability portfolio is, the less chance that a single risk will cause a company to fail. Correlation factors used in the different jurisdictions are not exact figures but are generally created as round numbers (such as positive or negative $0.25,0.50,0.75)$. The factors are typically applied after analyzing modeled results. These vary by jurisdiction and the granularity of risks being measured.

All jurisdictions discussed in this paper require calculations be completed net of reinsurance. Companies that cede business through coinsurance agreements no longer retain either the assets or the liabilities on their books, so these amounts are excluded from the capital calculations. If the reinsurance is ceded through a Yearly Renewable Term (YRT) arrangement, the assets remain with the company, but the ceded liability risk does not, so this is excluded from the capital calculations. For the assuming reinsurer, the assumed business is treated as if it were written directly. The risk associated with the potential default of the reinsurer is considered in the required capital calculation,

It is beyond the scope of this paper to provide further details related to the risks being measured in the capital calculations.

Most jurisdictions established a level of required capital as the level which corresponds to some corrective regulatory action. Companies will typically target holding a greater amount to avoid any material possibility of attracting such regulatory action as well as positioning themselves at the desired level within the range of capital levels for their peer company group.

## Section 4: US Capital Requirements

In the US, insurance companies are regulated by each of the states in which they do business, rather than a federal entity. The National Association of Insurance Commissioners, the NAIC, develops model laws and regulations in order to promote uniformity among state regulators. Such model laws and regulations must be approved by the individual states in order for them to take effect.

The RBC formula used in the US is generally formulaic (factor-based), rather than model-based, although certain market risk factors have recently been calculated using model-based components. Additional model-based calculations may be added in the future.

In the US, the accounting for statutory reporting uses an accrual basis, and primarily a book value model. For the most part, both assets and liabilities are held at a book value, providing stability in balance sheets. In general, liabilities are held on a conservative basis. Formulaic reserves are calculated using a discount rate set at issue of the policy, which is presumably when assets to back the risk are purchased. To the extent the discount rate is lower than the yield on initial assets, conservatism is introduced. It does not, however, consider reinvestment rates, which may be different than at initial sale. A further level of conservatism is provided by prescribed mortality and morbidity assumptions. More recently, reserves ${ }^{2}$ are determined using a modeling approach, and modeled reserves use "prudent estimate assumptions" which include margins on each individual risk factor to cover moderately adverse deviations from best estimate assumptions. Finally, reserves must be annually tested for adequacy, and the testing is done under moderately adverse conditions.

The NAIC RBC formula for life insurance companies provides four categories of risk - asset risk (C-1), insurance risk $(\mathrm{C}-2)$, interest rate and market risk ( $\mathrm{C}-3$ ), and business risk (C-4). There is also a provision for default of an affiliated company or off-balance sheet items such as derivative instruments (C-0). The calculations are generally after-tax factors applied to defined balance sheet items of an insurance company, and readily calculated. C-3 risks are the one exception which call for a model-based approach to products with long-dated interest rate guarantees such as variable annuities and certain fixed annuities and single premium life insurance policies.

C-1 Asset Risk covers the risk of default of the issuer or other non-performance of the assets and is applied to all book value assets held by the company, such as equities, bonds, mortgages, and real estate. Bonds are further broken into 20 categories, based on published credit ratings. The factors range from 0.0 for US Treasury bonds to 0.30 for those in the "junk bond" (very low-quality bond) category. Preferred stock is treated as bonds. Beyond the factor applied to individual holdings, there is an asset concentration factor which is applied to the 10 largest holdings. Finally, there is a diversification factor applied to the bond portfolio to account for the additional volatility risk when a portfolio holds relatively few bonds. The factor decreases as the number of bond issuers increases in the portfolio. C-1 is further subdivided into C-1cs (unaffiliated common stock) and C-10 (all other excluding common stock).

C-2 Insurance Risk applies to mortality and longevity risk. C-2 mortality risk (the risk that mortality worsens, and death benefits are paid earlier than originally expected) is determined based on application of a factor to net amount at risk (death benefit less account value, if any) of all life insurance products. Factors vary based on individual life versus group life, and within individual life whether the company has the ability to change amounts charged to policyholders, either through increasing charges, reducing interest credits, or making other changes to[^1]non-guaranteed elements of life insurance products. The factors also vary by portfolio size, since smaller portfolios will have more variability in total claims than will larger portfolios.

C-2 longevity risk is meant to cover the risk of additional benefits payments in case mortality experience is better than the reserves assume. This factor is applied to life contingent annuities - annuities in payout status, and those with payout guarantees. Annuities with only term certain guarantees, or those where the policyholder has the right but not a requirement to annuitize are excluded from this risk. The required amount of capital is based on a sliding scale factor based on total annuity reserves. Since mortality and longevity risks are negatively correlated (mortality will not worsen and improve at the same time), there is a correlation factor applied to the calculated values for $\mathrm{C}-2$ mortality and C-2 longevity in order to determine an overall C-2 insurance risk charge.

$$
C 2=\sqrt{C 2_{\text {mortality }}^{2}+C 2_{\text {longevity }}^{2}+2 \times C 2_{\text {mortality }} \times C 2_{\text {longevity }} \times \text { CorrFactor }}
$$

C-3 Interest Rate Risk covers the possibility that asset values and policy cash flows change due to market movements. C-3a covers interest rate changes (as a factor multiplied by reserves), C-3b covers health care capitation risk, and C-3c covers market risk. This market risk category has been subdivided into C-3 Phase I and C-3 Phase II. This risk is not strictly based on investment returns, as it also covers the possibility of disintermediation risk - policyholders withdrawing money when it is advantageous to them, leading the insurer to liquidate assets at a loss to meet cash flows.

C-3 Phase I applies to certain fixed annuity products and single premium life insurance products. It uses a stochastic cash flow projection process with prescribed scenarios, and the capital amount is based on a subset of the worst scenario results.

C-3 Phase II applies to variable annuity products and is calculated as part of a process to determine both reserves and capital requirements. Variable annuity products are often sold with guarantees that are highly sensitive to market movements. Capital and reserves are modeled using stochastic processing and a conditional tail expectation (CTE) measurement. Reserves are held at the CTE 70 level (the average of the $30 \%$ worst scenario results). The C-3 Phase II capital requirement is calculated based on the difference between CTE 98 and reserves (CTE 70).

Life insurance death benefit products, other than single premium policies, have a C-3 charge based on reserves held. The calculation is a single factor times the total reserves amount. Although recent changes to reserve calculations for life insurance products require modeling for reserve calculations, the majority of life insurance reserves are based on tabular calculations.

C-4 Business Risk is meant to cover operational risks and any other risk not discussed above. The amount of C-4 capital charge is based on annual premiums and the separate account value as of the valuation date and is not dependent upon reserves. This is the only part of the RBC calculation that is gross of reinsurance, as all business sold or assumed by the company is subject to this capital charge, gross of reinsurance.

Once the individual components of the RBC are determined, the calculation has additional correlation adjustments (called a covariance adjustment) and adjustments for federal taxes. The Authorized Control Level (ACL) RBC is as follows

$$
A C L R B C=C 0+C 4 a+\sqrt{(C 1 o+C 3 a)^{2}+(C 1 c s+C 3 c)^{2}+C 2^{2}+C 3 b^{2}+C 4 b^{2}}
$$

where:

- C0: Asset Risk-Affiliates
- C1cs: Unaffiliated common stock and affiliated noninsurance common stock
- C1o: Asset Risk-Other (excluding common stock)
- $\quad C 2$ : Insurance Risk
- $\quad C 3 a$ : Interest Rate Risk
- $\quad C 3 b$ : Health Credit Risk
- $\quad C 3 c$ : Market Risk
- $C 4 a$ : Business Risk
- $\quad C 4 b$ : Health Administrative Expense Business Risk

All of these calculations lead to an RBC amount that is published in the statutory annual statement. Also found in the annual statement is the Total Adjusted Capital (TAC), which is a balance sheet item. The RBC ACL ratio is calculated as the TAC divided by the ACL RBC. Regulators take various actions based on this ratio as explained further in the next section. This focus in the US of using an objective formula helps give some clear guidelines to enable any needed regulatory action for working with a company facing potential solvency issues.

### 4.1 REGULATORY ACTION

Company Action Level (CAL) RBC is twice the ACL. Regulatory Action Level (RAL) is 1.5 times the ACL. And Mandatory Control Level (MCL) is 0.70 times the $A C L$. The following table summarizes the actions that will be taken by the Company or the Regulator as a company's RBC ratio is reduced to each of these levels:

## Table 2

## US REGULATORY ACTIONS

| Level | RBC ACL Ratio | Action |
| :---: | :---: | :---: |
| Trend Test Corridor | $200 \%<=$ ratio $<250 \%$ | Company must perform trend test ${ }^{3}$ |
| Company Action Level | $150 \%<=$ ratio $<200 \%$ | Company must prepare and submit RBC plan to regulator |
| Regulator Action Level | $100 \%<=$ ratio $<150 \%$ | Company must submit (or revise) RBC plan and regulator will <br> issue an order of corrective action |
| Authorized Control Level | $70 \%<=$ ratio $<100 \%$ | Authorizes regulator to take actions necessary to protect <br> stakeholders |
| Mandatory Control Level | ratio $<70 \%$ | Requires regulator to put Company under regulatory control |

A company with a TAC above CAL with positive trend is considered to be healthy. Should the company's TAC fall below CAL or be below 3 times ACL with negative trend, the company will need to notify the regulator of this situation, but specific actions are not required. Should the Company's TAC fall between CAL and RAL, the company will need to file a plan to be approved by the regulator to bring the TAC up to a higher level.

In the case where the TAC is below RAL, the regulator is authorized to take action, which may mean placing the company into rehabilitation.

In the extreme case, where TAC has fallen below MCL, the regulator is required to place the company under regulatory control, as the company is then deemed insolvent.

### 4.2 GROUP LEVEL CAPITAL

All of the above NAIC RBC discussion relates to a single company, and actions the regulator may take to deal with a single company's solvency situation. Recent changes in the US require regulators to view solvency of the enterprise

${ }^{3}$ Trend Test can be found in LR035 of the RBC Calculation file
as a whole (the group) instead of simply the insurance entity(ies) within the group. At the time of writing this report, there are Group Capital Calculations, liquidity stress tests and Own Risk Solvency Assessment (ORSA) filings which are part of this oversight. The group oversight rules are still evolving.

### 4.3 FUTURE UPDATES

At some point, there may be new requirements for using a model-based approach to determine C-3 capital for life insurance products. Changes have also been proposed to C-1 factors for specific assets, and more complex changes are being considered for complex assets which include structured securities, asset-backed securities and CLOs, as well as assets originated by the insurance company or its affiliates or related entities.

## Section 5: Canadian Solvency Requirements

In Canada, the Office of the Superintendent of Financial Institutions (OSFI) regulates insurance companies. OSFI also supervises banks, pension plans, and insurance companies. It uses audited financial statements of insurers prepared in accordance with IFRS to perform solvency supervision of life insurance companies. OSFI utilizes several indicators to assess the financial condition of an insurer. A significant one is LICAT which involves application of stress events to a starting economic-based balance sheet (which is determined in accordance with Canadian Generally Accepted Accounting Principles, or Canadian GAAP) ${ }^{4}$.

In Canada, capital is considered to be either Tier 1 or Tier 2. Tier 1 capital is generally shareholder equity and retained earnings and there are no rules limiting the amount of Tier 1 capital that a company can recognize in capital. If a company holds assets on its balance sheet that do not meet the criteria for Tier 1 , such as hybrid capital instruments or subordinated debt, these amounts are considered to be Tier 2 capital. The limit of Tier 2 capital that can be recognized is that it cannot be less than zero or greater than the Net Tier 1 capital. For the purposes of this paper, for simplicity, we assume that the company holds no Tier 2 capital. The sum of the Tier 1 and Tier 2 capital amounts is known as "Available Capital" and is used in determining the Total Ratio as shown in the formula below. The tiering terminology here is different from the tiering terms used for Solvency II described below.

Reserves must be computed in accordance with the Canadian Institute of Actuaries (CIA) Standards of Practice. These standards describe the requirement of adverse scenarios developed by stress testing and the assumptions used for forecasting the business plan. The number of adverse scenarios may vary among insurers and can change over time.

The valuation of invested assets under IFRS depends on their classification as either fair value through profit or loss (FVPL), fair value through other comprehensive income (FVOCI) and Amortized Cost.

A life insurer's minimum capital requirement, referred to as the Base Solvency Buffer (BSB) is aimed to be aligned with the 99\% Conditional Tail Expectation (CTE99) over a one-year period. The BSB is the sum of the capital requirements for each of the following five risk components:

- Asset default risk - risk of loss resulting from on-balance sheet asset default and from off-balance sheet items (labeled as Credit risk in the BSB calculation); loss of market value of equities and corresponding loss of income (labeled as Market Risk in the BSB calculation)
- Mortality/morbidity/lapse risks - risks that the company's assumptions prove incorrect
- Change in interest rate risk - risk of loss resulting from changes in the interest rate environment other than asset default
- Segregated funds risk - risk of loss arising from guarantees embedded in segregated funds ${ }^{5}$
- Foreign exchange risk - risk of loss from fluctuations in currency exchanges

There are two ratios that are calculated and analyzed based on the results: Total Ratio, and the Core Ratio. Total Ratio focuses on policyholder and creditor protection. The formula for Total Ratio is:[^2]

## Available Capital + Surplus Allowance + Eligible Deposits <br> Base Solvency Buffer

The Core Ratio focuses on financial strength. The formula for Core Ratio is:

$$
\frac{\text { Tier } 1 \text { Capital }+70 \% \text { of Surplus Allowance }+70 \% \text { of Eligible Deposits }}{\text { Base Solvency Buffer }}
$$

The amount of the Surplus Allowance included in the numerator of the Total and Core Ratios is based on provisions for adverse deviations (PfADs) calculated under the old Canadian Asset Liability Method (CALM) for years through 2022 and new methods developed for use with IFRS 17 for 2023 and subsequent years.

Eligible Deposits include amounts that will only be made available to the insurer if they are needed and the criteria for their use are met, such as collateral and letters of credit placed by unregistered reinsurers and claims fluctuation reserves for group insurance underwritten on a refund accounting basis.

The BSB is determined by summing the aggregate capital requirement net of credits, separately for each of six geographical regions (Canada, US, UK, EU, Japan, and Other) where business is sold, multiplied by a scalar of 1.0 (as of $1 / 1 / 2023$ ). The aggregate capital requirement within a geography comprises requirements for each of the following five risk components: credit; market; insurance; segregated funds guarantee; and operational. The capital requirements for each geography are based upon the same calculation.

Aggregate requirements are reduced by credits for qualifying in-force participating and adjustable products, as well as for risk diversification, reinsurance, collateral, guarantees, credit, or other derivatives that serve as hedges and asset securitization.

### 5.1 REGULATORY ACTION

OSFI has established a Supervisory Target Total Ratio of 100\% and a Supervisory Target Core Ratio of 70\%. The Supervisory Targets provide cushions above the minimum requirements, provide a margin for other risks, and facilitate OSFI's early intervention process. When the ratio decreases to near the Supervisory Target Ratios, OSFI will assess any necessary actions to be taken to remediate.

Insurers are required, at minimum, to maintain a Total Ratio of $90 \%$ or a Core Ratio of $55 \%$.

Regulated insurance holding companies and non-operating insurance companies are required to maintain a minimum Core Ratio of $50 \%$. Companies are further required to hold a minimum capital of $\$ 5$ million.

### 5.2 FUTURE UPDATES

The formulae and methods discussed above will become effective in early 2023. Regulators are expected to review results for several years before making further changes.

## Section 6: Solvency II

Within the European Union, each country regulates companies domiciled within that country. The organization of European Insurance and Occupational Pensions Authority (EIOPA) is an independent advisory body to the European Commission, the European Parliament, and the Council of the European Union. EIOPA sets standards for insurance company regulation within member countries. EIOPA provides guidance regarding Solvency II calculations and related technical processes. Under Solvency II, regulatory required capital is set at a level such that a company would be expected to remain solvent (i.e., sufficient assets to cover liabilities) over the next year even if a 1-in-200year adverse event occurred. The process is meant to be transparent to all users of the financial statements reporting the capital requirements.

Solvency II establishes two levels of capital requirements:

- The Solvency Capital Requirement (SCR) - the level of capital at which a company would be expected to be solvent over the next year with a 99.5\% (1-in-200) probability
- Minimum Capital Requirement (MCR) - the level of capital under which the regulator would have to intervene. This is set at a level where the company would be expected to remain solvent over the next year with $85 \%$ probability.

Similar to LICAT discussed in the prior section, Solvency II involves application of stresses to a starting economicbased balance sheet. In that starting balance sheet, when possible, assets/liabilities should be marked to market, but otherwise "marked to model". In other words, the market values are determined using a model calibrated to market data rather than directly from market data. This approach is often necessary for non-traded assets and liabilities.

Insurance liabilities are assessed at their current exit value, which is the value they could be transferred or settled by two willing parties with equal information. This exit value is often difficult to determine, as life insurance portfolios are not traded in a regulated exchange, nor are mergers and acquisitions of insurance companies happening on a regular enough basis for market values to be determined. In order to determine the value of insurance liabilities, companies often run models to project and discount cash flows, using best estimate assumptions plus a risk premium which would be required by a potential buyer. Discounting is based on the risk-free rate, with certain adjustments for long-duration guarantee life and annuity products. Alternatively, marking to model can be used where the calculation could include risk premium within the assumptions, depending upon the view of how a willing buyer would determine a purchase price.

The SCR can be determined using a standard, Basic Solvency Capital Calculation, or a company can determine it using their own internal model. If the internal model approach is used, detailed information regarding the internal model and its calibration must be submitted to the regulator who then, in turn, assesses whether it is acceptable for the SCR calculation. Our description of the SCR calculation is focused on the Basic Solvency Capital Calculation. The overall structure is illustrated in the figure below.

<img src="https://cdn.mathpix.com/cropped/2024_04_13_59edaaf1c3ec26f7eb72g-17.jpg?height=930&width=1612&top_left_y=240&top_left_x=251" alt="image" style="width:100%;height:auto;">

The Solvency II framework is set for all insurance entities and is not specific to life insurance companies. There are three underwriting risk factor categories and two other risk categories that are used:

- Non-life underwriting risk
- $\quad$ Life underwriting risk
- Health underwriting risk
- Market risk
- Counterparty default risk

Non-life underwriting risks are for general insurance (property and casualty coverages). Health underwriting risks are those for both short term (e.g., major medical coverage) and long-term (e.g., disability income) health coverages. Both are important to the calculation, but since the focus of this paper is life insurance risks, neither nonlife underwriting risks nor health underwriting risks are covered in this paper.

Life underwriting risks fall into an additional seven categories:

1. Mortality risk - the risk that mortality is higher than expected. This is generally a negative situation for life insurance death benefits. The stress test is $15 \%$ worsening of mortality.
2. Longevity risk - the risk that mortality is lower than expected. This is generally a negative situation for annuities in payout status. The stress test is a 20\% decrease to mortality.
3. Disability-morbidity risk - the risk that morbidity claims are worse than expected. The stress includes both an increase in initial claims, and a lengthening of time on claim, due to a decrease in recovery rates.
4. Lapse risk - the risk that policyholders change their lapse profile either permanently or in a mass event. Since the impact of a change in lapse rates may vary by product, the company must test a $50 \%$ permanent increase in lapse rates, a 50\% permanent decrease in lapse rates, and a 40\% immediate reduction of policies in force. The company takes the maximum or most conservative risk charge for each policy. While
these calculations can be performed on an individual policy level, companies may also group policies to determine the lapse risk so long as the policies are homogenous.
5. Expense risk - the risk that expenses exceed best estimates. The shock is a $10 \%$ increase in expenses for all years, plus an additional $1 \%$ increase to the expense inflation factor.
6. Revision risk - the risk that annuity payments increase due to changes in either the legal environment or health of the annuitant. The stress is a 3\% permanent increase in benefits payable.
7. Catastrophe risk - for life contracts, this is the risk of a short term (one year) increase in mortality of $0.15 \%$ (additive to the one-year mortality rate)

Although the life risks are generally calculated based on fair market value assumptions, the insurer is allowed to add a spread adjustment (either a matching adjustment or volatility adjustment) to the discount rate used in determining best estimate liabilities for long-term guarantee products (e.g., life insurance and annuity payouts). This spread adjustment is meant to account for the irrational movements in the market - such as low liquidity or widening bond spreads.

Market risks fall into six categories and apply to the asset portfolio:

1. Interest rate risk - the risk that the value of an asset or liability will change due to a change in term structure of interest rates or interest rate volatility
2. Equity Risk - the risk that equities held by the insurer have an immediate decrease in market value. The decrease for exchange traded stocks is $39 \%$. All other equities are stressed at $49 \%$.
3. Property risk - the risk that real estate prices immediately drop $25 \%$
4. Spread risk - The risk that bonds have a change to level or volatility of credit spreads (spreads over the risk-free rates). the risk is based on duration and type of asset held. This applies to bonds, debt instruments, mortgage-backed securities, credit derivatives, and similar assets.
5. Market risk concentration - the risk that a single counterparty can have a significant impact on investment returns
6. Currency risk - the risk that foreign exchange rates will change over the course of the projections. The stress is a $25 \%$ change in the exchange rate.

Finally, Counterparty default risk is the risk that a counterparty will not be able to pay its debts to the insurer. There are two types of counterparties - Type 1 includes all risk mitigation exposures, such as reinsurers, and Type 2 includes future receivables from policyholders and mortgage loans.

Solvency II does not treat these risks as being completely independent, and correlation factors are used to account for dependencies between risk categories. The correlation factors are applied, both between major risk categories, and within the major risk categories. The formulas to determine the Solvency II capital requirements can be found in Appendix A.

The Basic Solvency Capital formula is

$$
\text { Basic SCR }=\sqrt{\sum_{i, j} \operatorname{Corr}_{i, j} \times S C R_{i} \times S C R_{j}}
$$

where Corr $\mathrm{i}_{\mathrm{i}, \mathrm{j}}$ represents the correlation factor associated with each of the five Solvency Capital Risks (Market Risk, Default Risk, and the three underwriting risks).

The MCR is no less than $25 \%$ and no more than $45 \%$ of the Basic SCR. There is also a 1.2 million Euro floor.

### 6.1 REGULATORY ACTION

Under Solvency II, capital available within the company is "own funds", which is further divided into basic and auxiliary own funds. Basic own funds exist within the particular entity. Auxiliary own funds may be called upon under specific circumstances but do not currently exist within the entity, such as funds that may be available from a parent. Own funds are further broken into Tiers, based on availability to absorb losses. Tier 1 capital is highest quality, and Tier 3 lowest (for example, subordinated debt). A company must have no less than 50\% of SCR backed by Tier 1 capital, and no more than 15\% of Tier 3. MCR must be backed by at least 80\% Tier 1 capital and no Tier 3 capital. The tiering terminology here is different from the tiering terms used for LICAT.

A company approaching minimum capital levels will be required to submit a plan to remedy the situation, and the regulator will have to approve the plan. Should a company not have enough of the proper level of capital to cover SCR or MCR, the regulator will require a capital add-on. Each EU supervisor has latitude related to the remedy and further actions.

### 6.2 FUTURE UPDATES

Our research did not identify any significant updates planned with respect to the required capital calculation.

## Section 7: Bermuda Solvency Requirements

In Bermuda, capital requirements are prescribed by the Insurance Act and life insurance companies are overseen by the Bermuda Monetary Authority (BMA). Companies calculate a Target Capital Level (TCL) and a Minimum Margin for Solvency (MSM). These quantities are different Bermuda Solvency Capital Requirement (BSCR) capitalization levels. The Enhanced Capital Requirement (ECR) is the greater of the MSM and the BSCR. While companies may use an approved internal proprietary capital model to calculate BSCR, the focus of this paper will be the "standard model".

To understand the key differences between the different capitalization level calculations mentioned above, it is important to understand the different accounting frameworks used in Bermuda to define available capital.

Companies are required to calculate "Bermuda Statutory" financial statements and "Economic Balance Sheet" (EBS) financial statements. For the purposes of measuring solvency, the key item of note is that the MSM's definition of available capital is based on the Bermuda Statutory financial statements and the TCL's definition of available capital is based on the EBS financial statements. Required capital for both calculations is based on the BSCR, which is discussed below. The overall structure is illustrated in the figure below.

<img src="https://cdn.mathpix.com/cropped/2024_04_13_59edaaf1c3ec26f7eb72g-20.jpg?height=935&width=1694&top_left_y=281&top_left_x=259" alt="image" style="width:100%;height:auto;">

Bermuda Statutory is required to be based on a widely accepted accounting measure, for example US GAAP or IFRS. The exact accounting measure used is a decision that the company makes at the time of their business license application and cannot be changed after the BMA has approved their license. EBS is a BMA prescribed accounting framework. EBS assets are based on market value. EBS liabilities use a fair value approach that is the sum of the "Best Estimate Liability" and a "Risk Margin" (i.e., Reserves equal Best Estimate Liability plus Risk Margin). The Best Estimate Liability is composed of best estimate liability cashflows discounted at either of (A) the "Standard Approach" which uses a market representative portfolio or (B) a "Scenario Based Approach" which derives yields from a company's underlying assets after making various prescribed prudential adjustments based primarily on the predictability of the underlying assets' cashflows and the degree of cashflow matching between the assets and liabilities. The use of the Standard Approach or the Scenario Based Approach is an election that each company makes, similar to Solvency II in the sense that a company can use Solvency II's Standard Approach discount rates or a "Matching Adjustment" methodology that references a company's underlying assets. The Risk Margin uses a "Cost of Capital" approach similar to Solvency II; i.e. insurance risk capital based on BSCR capital charges is projected over the life of the liability, the resulting risk capital amounts are multiplied by a 6\% "cost of capital" charge, and the resulting "cost of capital" amounts are discounted at prescribed discount rates based on market value risk-free rates.

Required capital is referred to as BSCR, with the Group BSCR formula (see Appendix B) aggregating various risks calibrated to a 1-in-200 risk level using a correlation matrix similar to the previously described frameworks (i.e., it assumes the risks are partially independent of one another, providing some diversification benefit when the risk charges are combined). There are 4 risk factor categories used to determine the BSCR:

- Market risk - the risk arising from fluctuations in values of, or income from, assets or in interest rates or exchange rates. This risk covers fixed income, equity, interest, currency and concentration risks.

o For fixed income and equity risk, prescribed factors are multiplied by asset market value.

o For interest rate risk, one of two approaches can be used.

- The "duration-based approach" multiplies a percentage times market value of assets. The percentage is the product of $(A)$ the absolute value of the duration of the underlying assets minus the duration of the liabilities, (B) $2 \%$, and (C) a potential reduction to the $2 \%$ charge based on various qualitative considerations that are primarily related to the robustness of a company's ALM management.
- The "shock-based approach" applies prescribed interest rate shocks to the assets and liabilities. The size of the shock varies by currency.

o For currency risk, the amount of assets and liabilities in each currency is measured. The difference in the by-currency amount of assets and liabilities is then shocked, where the prescribed shocks vary by currency, and the post-shock amount is then held as currency risk capital.

o For concentration risk, the ten largest asset holdings from a single issuer are determined and then the fixed income and equity risk capital amounts are doubled for those issuers' investments.

- Long-Term risk - the risk arising from fluctuation in values from long-term liabilities. This includes mortality, stop loss, morbidity, longevity, variable annuity and other long-term insurance risk.

o For mortality risk, the difference in face amount and EBS Best Estimate Liability is multiplied by a "Net Amount at Risk" factor. The Net Amount at Risk factor decreases as the size of the exposure gets larger to recognize the benefit of insuring different lives with differing mortality risk factors

o For stop loss risk, a prescribed percentage is multiplied by premium.

o For morbidity risk, a prescribed percentage is multiplied by premium. The factor varies by the type of morbidity coverage provided.

o For longevity risk, a prescribed percentage is multiplied by EBS Best Estimate Liability. The factor varies by age of the underlying insured.

o For variable annuity risk, one of two approaches can be used.

- A standard approach which bases capital charges on type of guarantee provided and the in-themoneyness of the guarantee
- An internal capital model approach which uses a company's internal capital model and determines capital based on CTE(95). The internal capital model must be submitted to the BMA for approval.

o For other long-term insurance risk, the EBS Best Estimate Liability is multiplied by a prescribed factor. The factor varies depending on which insurance risk classification is used for a liability. That is, a different factor will apply if a liability is categorized as mortality risk rather than a fixed annuity.

- Credit risk - the risk of loss arising from an insurance group's inability to collect funds from debtors.

o This risk category is primarily counter-party risk.

o The counter-party risk calculation takes into account a net exposure, i.e., the exposure to a counterparty after taking into considering eligible collateral or other forms of credit protection provided by an entity to which the insurer has an exposure.

- $\quad$ P\&C risk - the risk arising from fluctuations in values of property and casualty insurance. This includes premium, reserve, and catastrophe risk.

The BMA may also impose a capital charge adjustment, which would either reduce or increase capital assessments if the regulator determines that an insurer's risk profile differs from the assumptions underlying the ECR or through analysis of the company's risk management policies and practices. These may be made due to items such as "provisions for reserve deficiencies, significant growth in premiums, and quality of risk management surrounding /operational risk." ${ }^{6}$[^3]

Once the Group BSCR has been calculated, including an operational risk capital charge that is a percentage of the post-diversification BSCR required capital and any other capital adjustments as discussed above, the Total Statutory Economic Capital and Surplus is calculated.

The ECR is a measure of solvency capital used to monitor capital adequacy of insurance groups domiciled in Bermuda. It is the maximum of the BSCR and MSM.

The MSM is calculated on an aggregate level. This is set at the maximum of $25 \%$ of ECR and either $\$ 1,000,000$ BMD (Class 3A and 3B insurers ${ }^{7}$ ) or $\$ 100,000,000$ BMD (Class 4 insurer). The MSM's definition of available capital is based on an entity's "Bermuda Statutory" financials. Bermuda Statutory financials are required to be based on a commonly accepted GAAP, such as USGAAP or IFRS, in lieu of the EBS financials that form the basis of the BSCR required capital calculation.

The TCL is $120 \%$ of ECR and, while it is not a capital requirement, insurance companies are expected to hold eligible capital sources to cover the TCL.

Group BSCR ratio equals Available Capital and Surplus divided by Group BSCR.

The BSCR and ECR ratios are used by the BMA to evaluate the financial strength of an insurance group. These ratios and the TCL are used to monitor capital adequacy.

### 7.1 REGULATORY ACTION

In addition to the BSCR, ECR and TCL, the BMA also requires a Solvency Capital Distribution chart, which displays the relative contribution of each risk charge to the BSCR prior to the adjustment for correlation, and a Regulatory Action Level graph showing Available Statutory Capital and Surplus relative to BMA's regulatory action guidelines. The ECR is considered as Regulatory Action Level 1 whereas Regulatory Action Level 2 is the TCL. The BMA determines the appropriate course of action and appropriate allocation of resources. The greater the level of risk detected, the more supervisory review that is required.

### 7.2 FUTURE UPDATES

The BMA regularly reviews capital requirements (calculation and action requirements) and makes changes when it deems necessary to ensure requirements are appropriately calibrated and reflect the risks of industry participants.[^4]

## Section 8: Model Results and Comparison

In this section of the paper, we compare regulatory solvency capital using identical portfolios for both assets and liabilities. The regulatory solvency capital for the four jurisdictions were calculated using a Microsoft Excel workbook called "SOA Capital Adequacy Example.xlsm." For simplicity, we have assumed that all liabilities originated in the same jurisdiction as the calculation.

As the objective of the model is to illustrate required capital calculation methodology differences, a number of modeling simplifications were employed. There are only two products - term insurance and payout annuities, approximately equally weighted in terms of reserves. We assume the company has no health or general insurance liabilities to consider. The model does not project liabilities using a yield curve but does perform simple adjustments to determine the impact of interest rate shocks. Although in reality, life insurance and annuity products experience different mortality patterns, the model uses a single base mortality table for both products, for simplicity.

For liabilities, we assume the business is written in the jurisdiction being considered. We also assume all assets and asset cash flows are denominated in that jurisdiction's currency. This removes currency risk from the calculations for all jurisdictions. There is also an assumption that none of the liabilities are held in separate accounts.

The insurance portfolio consists of two types of policies - 30-year term insurance and a payout annuity. The following assumptions are listed on the "Inputs-Liabilities" worksheet of "SOA Capital Adequacy Example.xlsm". We also created a scenario where the liability mix is more heavily weighted to annuities while keeping the asset mix the same. This is shown in the second table below. For simplification, we assume that market value of liabilities and assets are the same for Solvency II and BMA when they typically vary due to different discount rates.

Table 3

LIABILITY PRODUCT MIX - BASE SCENARIO

| Product | Average <br> Attained Age | Face Amount | US Statutory <br> Reserves | Market <br> Value | Annual Premium |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Life (30-year Term) | 50 | $\$ 175,000,000$ | $\$ 7,118,016$ | $\$ 6,189,579$ | $\$ 609,546$ |
| Payout Annuity | 70 | $\$ 7,500,000$ | $\$ 7,125,000$ | $\$ 7,500,000$ | $\$ 1,000,000$ |
| Total |  | $\$ 182,500,000$ | $\$ 14,243,016$ | $\$ 13,689,579$ | $\$ 1,609,546$ |

## Table 4

LIABILITY PRODUCT MIX - CHANGED LIABILITY MIX SCENARIO

| Product | Average Attained <br> Age | Face Amount | US Statutory Reserves | Market Value | Annual <br> Premium |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Life (30-year Term) | 50 | $\$ 87,542,924$ | $\$ 3,560,754$ | $\$ 3,096,308$ | $\$ 304,923$ |
| Payout Annuity | 70 | $\$ 11,244,487$ | $\$ 10,682,262$ | $\$ 11,244,487$ | $\$ 1,499,265$ |
| Total |  | $\$ 98,787,411$ | $\$ 14,243,016$ | $\$ 14,340,794$ | $\$ 1,804,187$ |

The assets consist of two non-callable bonds of differing durations, mortgages, real estate, and equities. We assume the life insurance company stands alone, and is not part of a larger group, so affiliated amounts are not considered for required capital purposes. There are no "non-admitted" assets on the statutory financial statement. The initial asset amount was set such that it was greater than the liabilities and required capital for the base scenario.

As listed on the "Inputs-Assets" worksheet of "SOA Capital Adequacy Example.xlsm" we have two sets of asset assumptions - one for the base scenario and the second for a scenario where the company invests in riskier assets while the liability mix remains the same.

Table 5

ASSET PORTFOLIO

|  | Base Scenario |  | Riskier Asset Scenario |  |  |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Asset | Book Value | Market <br> Value | Book Value | Market <br> Value | Duration <br> (years) |
| Fixed Income 1 | $\$ 7,000,000$ | $\$ 7,525,000$ | $\$ 1,820,000$ | $\$ 1,956,500$ | 5 |
| Fixed Income 2 | $\$ 7,000,000$ | $\$ 7,525,000$ | $\$ 1,820,000$ | $\$ 1,956,500$ | 20 |
| Mortgages | $\$ 2,500,000$ | $\$ 2,500,000$ | $\$ 3,640,000$ | $\$ 3,640,000$ | 10 |
| Real Estate | $\$ 1,000,000$ | $\$ 1,000,000$ | $\$ 3,640,000$ | $\$ 3,640,000$ |  |
| Equity (Stocks in OECD or EEA countries) | $\$ 500,000$ | $\$ 500,000$ | $\$ 3,640,000$ | $\$ 3,640,000$ |  |
| Equity (Stocks in Emerging Markets) | $\$ 200,000$ | $\$ 200,000$ | $\$ 3,640,000$ | $\$ 3,640,000$ |  |
| Total | $\$ 18,200,000$ | $\$ 19,250,000$ | $\$ 18,200,000$ | $\$ 18,473,000$ |  |

There are four worksheets called "2.a.[x]Inputs-[jurisdiction] Factors" in "SOA Capital Adequacy Example.xlsm", where $[\mathrm{x}]$ is $\mathrm{i}$ through iv, that contain the solvency factors used to determine solvency for each jurisdiction.

Any conclusions made regarding capital differences amongst the different jurisdictions are specific to the asset and liability mix selected as well as the simplifications made. Therefore, caution should be used in generalizing these conclusions.

## Capital Requirements

The following table shows the balance sheet between the three financial reporting methods - US Statutory, Market Value and Economic Value for the base scenario

## Table 6

BALANCE SHEET BY REPORTING METHOD

| Balance Sheet | US Statutory | Market Value | Economic Value |
| :--- | :---: | :---: | :---: |
| Assets | $\$ 18,200,000$ | $\$ 19,250,000$ | $\$ 19,250,000$ |
| Liabilities | $\$ 14,323,016$ | $\$ 13,689,579$ | $\$ 13,689,579$ |
| Capital | $\$ 3,876,984$ | $\$ 5,560,421$ | $\$ 5,560,421$ |

The remainder of this section shows the capital requirements for the four jurisdictions for the base, riskier asset and changed liability mix scenarios.

The Solvency II, LICAT and BSCR capital requirements show that market risk is the dominant risk in the capital calculations indicating the importance of invested assets to the insurance company. Under all 4 jurisdictions, the insurance company has more than two times the amount of required capital the regulators require the insurance company to hold.

If the asset mix is changed to have a heavier weighting on riskier assets, the required capital amounts for all 4 jurisdictions increase, leading to decreases in capital ratios. In some cases, this requires some form of action by the company, such as submission of a plan to improve capital. For the US, since the RBC ratio is $179 \%$, the insurance company is required to prepare and submit an RBC plan to the regulator. For Canada, the decreased Total Ratio leads to increased supervisory attention that would include early warning intervention status. For Bermuda, the decreased TCL Ratio leads to the requirement of the company improving its capital position and facing wind-up of the business. Overall, the solvency ratios worsen and decrease from the $130-425 \%$ range for the base scenario to the $70-180 \%$ range, caused by the increase in market risk for all 4 jurisdictions.

For the changed liability mix scenario, the solvency ratios improve and increase from the 130 - $425 \%$ range for the base scenario to the 280 - 540\% range for the changed liability mix scenario. This indicates that a shift in product mix from a relatively equal mix of life and annuity reserves to one where there are more annuity reserves than life reserves could provide a large positive impact (i.e., lower capital requirement and higher ratio) on the capital requirement ratio, caused mainly by the decrease in insurance risk for all 4 jurisdictions.

## Table 7

US RBC POST-TAX CAPITAL REQUIREMENTS

| Capital Charges | Base | Riskier Assets | Changed Liability Mix |
| :--- | :---: | :---: | :---: |
| Asset Risk (C-0) | $\$ 0$ | $\$ 0$ | $\$ 0$ |
| Asset Risk (C-1) | $\$ 490,393$ | $\$ 2,219,126$ | $\$ 490,393$ |
| Insurance Risk (C-2) | $\$ 305,042$ | $\$ 305,042$ | $\$ 152,596$ |
| Interest Rate Risk (C-3) | $\$ 519,672$ | $\$ 519,672$ | $\$ 346,561$ |
| Business Risk (C-4) | $\$ 39,163$ | $\$ 39,163$ | $\$ 43,899$ |
| ACL | $\$ 466,014$ | $\$ 1,100,299$ | $\$ 366,448$ |
| TAC | $\$ 3,941,984$ | $\$ 3,941,984$ | $\$ 3,941,984$ |
| RBC Ratio | $423 \%$ | $179 \%$ | $538 \%$ |

Table 8

CANADIAN LICAT CAPITAL REQUIREMENTS

| Capital Charges | Base | Riskier Assets | Changed Liability Mix |
| :--- | :---: | :---: | :---: |
| Credit Risk | $\$ 253,750$ | $\$ 118,300$ | $\$ 253,750$ |
| Market Risk | $\$ 1,675,360$ | $\$ 5,022,954$ | $\$ 819,399$ |
| Insurance Risk | $\$ 1,626,964$ | $\$ 1,626,964$ | $\$ 650,000$ |
| Segregated Funds | $\$ 0$ | $\$ 0$ | $\$ 0$ |
| Credits | $\$ 0$ | $\$ 0$ | $\$ 0$ |
| Operational Risk | $\$ 257,261$ | $\$ 441,960$ | $\$ 124,525$ |
| Base Solvency Buffer | $\$ 4,316,917$ | $\$ 7,540,759$ | $\$ 2,070,581$ |
| Total Ratio | $139 \%$ | $82 \%$ | $299 \%$ |
| Core Ratio | $132 \%$ | $77 \%$ | $282 \%$ |

## Table 9

SOLVENCY II CAPITAL REQUIREMENTS

| Capital Charges | Base | Riskier Assets | Changed Liability Mix |
| :--- | :---: | :---: | :---: |
| Life Underwriting Risk | $\$ 1,945,334$ | $\$ 1,945,334$ | $\$ 1,058,025$ |
| Market Risk | $\$ 1,773,897$ | $\$ 5,650,444$ | $\$ 974,974$ |
| Basic SCR | $\$ 2,942,184$ | $\$ 6,419,333$ | $\$ 1,608,031$ |
| Capital | $\$ 5,560,421$ | $\$ 4,783,421$ | $\$ 4,909,206$ |
| Solvency Ratio | $189 \%$ | $75 \%$ | $305 \%$ |

Table 10

BERMUDA CAPITAL REQUIREMENTS

| Capital Charges | Base | Riskier Assets | Changed Liability <br> Mix |
| :--- | :---: | :---: | :---: |
| Market Risk | $\$ 1,646,821$ | $\$ 5,383,086$ | $\$ 1,015,017$ |
| Long-Term Risk | $\$ 588,913$ | $\$ 588,913$ | $\$ 495,671$ |
| Credit Risk | $\$ 100,000$ | $\$ 100,000$ | $\$ 100,000$ |
| Operational Risk | $\$ 0$ | $\$ 0$ | $\$ 0$ |
| BSCR | $\$ 1,830,974$ | $\$ 5,501,051$ | $\$ 1,198,792$ |
| ECR | $\$ 1,830,974$ | $\$ 5,501,051$ | $\$ 1,198,792$ |
| TCL | $\$ 2,197,169$ | $\$ 6,601,261$ | $\$ 1,438,551$ |
| TCL Ratio | $253 \%$ | $72 \%$ | $341 \%$ |

The next three tables compare the balance sheets on a market value and book value basis as well as the capital requirements by jurisdiction. Each table shows the results for each scenario. While the charts show that the US has the highest capital ratio and the lowest required capital amount, the numbers do not mean that the US has lower standards. All four requirements are different, due to different accounting methods, required capital calculations, and regulatory view of risk. The values are based on one simplified example and are not meant to be representative of overall industry results.

Table 11

COMPARISON OF CAPITAL REQUIREMENTS - BASE SCENARIO

| Jurisdiction | US | Canada | Europe | Bermuda |
| :--- | :---: | :---: | :---: | :---: |
| Method | RBC | LICAT | Solvency II | TCL |
| Market Value of Assets | $\$ 19,250,000$ | $\$ 19,250,000$ | $\$ 19,250,000$ | $\$ 19,250,000$ |
| Market Value of |  |  |  |  |
| Liabilities | N/A | N/A | $\$ 13,689,579$ | $\$ 13,689,579$ |
| Market Value of Surplus | N/A | N/A | $\$ 5,560,421$ | $\$ 5,560,421$ |
| Book Value of Assets | $\$ 18,200,000$ | $\$ 18,200,000$ | $\mathrm{~N} / \mathrm{A}$ | $\mathrm{N} / \mathrm{A}$ |
| Book Value of Liabilities | $\$ 14,243,016$ | $\$ 14,323,016$ | $\mathrm{~N} / \mathrm{A}$ | $\mathrm{N} / \mathrm{A}$ |
| Book Value of Surplus | $\$ 3,956,984$ | $\$ 3,956,984$ | $\mathrm{~N} / \mathrm{A}$ | $\mathrm{N} / \mathrm{A}$ |
| Base Capital | $\mathrm{N} / \mathrm{A}$ | $\$ 6,000,000$ | $\mathrm{~N} / \mathrm{A}$ | $\mathrm{N} / \mathrm{A}$ |
| Adjusted Capital | $\$ 3,941,984$ | $\$ 5,700,000$ | $\$ 5,560,421$ | $\$ 5,560,421$ |
| Required Capital | $\$ 932,028$ | $\$ 4,316,917$ | $\$ 2,942,184$ | $\$ 2,197,169$ |
| Total Ratio | $\mathrm{N} / \mathrm{A}$ | $139 \%$ | $\mathrm{~N} / \mathrm{A}$ | $\mathrm{N} / \mathrm{A}$ |
| Capital Ratio ${ }^{1}$ | $423 \%$ | $132 \%$ | $189 \%$ | $253 \%$ |

${ }^{1}$ For Canada, the Capital Ratio is actually the Core Ratio.

Table 12

COMPARISON OF CAPITAL REQUIREMENTS - RISKIER ASSETS SCENARIO

| Jurisdiction | US | Canada | Europe | Bermuda |
| :--- | :---: | :---: | :---: | :---: |
| Method | RBC | LICAT | Solvency II | TCL |
| Market Value of Assets | $\$ 18,473,000$ | $\$ 18,473,000$ | $\$ 18,473,000$ | $\$ 18,473,000$ |
| Market Value of <br> Liabilities |  |  |  |  |
| Market Value of Surplus | N/A | N/A | $\$ 13,689,579$ | $\$ 13,689,579$ |
| Book Value of Assets | $\$ 18,200,000$ | $\$ 18,200,000$ | N/A | $\$ 4,783,421$ |
| Book Value of Liabilities | $\$ 14,243,016$ | $\$ 14,243,016$ | $\mathrm{~N} / \mathrm{A}$ | $\mathrm{N} / \mathrm{A}$ |
| Book Value of Surplus | $\$ 3,956,984$ | $\$ 3,956,984$ | $\mathrm{~N} / \mathrm{A}$ | $\mathrm{N} / \mathrm{A}$ |
| Base Capital | $\mathrm{N} / \mathrm{A}$ | $\$ 6,200,000$ | $\mathrm{~N} / \mathrm{A}$ | $\mathrm{N} / \mathrm{A}$ |
| Adjusted Capital | $\$ 3,941,984$ | $\$ 5,840,000$ | $\$ 4,783,421$ | $\$ 4,783,421$ |
| Required Capital | $\$ 2,200,597$ | $\$ 7,540,759$ | $\$ 6,419,333$ | $\$ 6,601,261$ |
| Total Ratio | $\mathrm{N} / \mathrm{A}$ | $82 \%$ | $\mathrm{~N} / \mathrm{A}$ | $\mathrm{N} / \mathrm{A}$ |
| Capital Ratio ${ }^{1}$ | $179 \%$ | $77 \%$ | $75 \%$ | $72 \%$ |

${ }^{1}$ For Canada, the Capital Ratio is actually the Core Ratio.

## Table 13

COMPARISON OF CAPITAL REQUIREMENTS - CHANGED LIABILITY MIX SCENARIO

| Jurisdiction | US | Canada | Europe | Bermuda |
| :--- | :---: | :---: | :---: | :---: |
| Method | RBC | LICAT | Solvency II | TCL |
| Market Value of Assets | $\$ 19,250,000$ | $\$ 19,250,000$ | $\$ 19,250,000$ | $\$ 19,250,000$ |
| Market Value of |  |  |  |  |
| Liabilities | N/A | N/A | $\$ 14,340,794$ | $\$ 14,340,794$ |
| Market Value of Surplus | N/A | N/A | $\$ 4,909,206$ | $\$ 4,909,206$ |
| Book Value of Assets | $\$ 18,200,000$ | $\$ 18,200,000$ | $\mathrm{~N} / \mathrm{A}$ | $\mathrm{N} / \mathrm{A}$ |
| Book Value of Liabilities | $\$ 14,243,016$ | $\$ 14,323,016$ | $\mathrm{~N} / \mathrm{A}$ | $\mathrm{N} / \mathrm{A}$ |
| Book Value of Surplus | $\$ 3,956,984$ | $\$ 3,956,984$ | $\mathrm{~N} / \mathrm{A}$ | $\mathrm{N} / \mathrm{A}$ |
| Base Capital | $\mathrm{N} / \mathrm{A}$ | $\$ 6,200,000$ | $\mathrm{~N} / \mathrm{A}$ | $\mathrm{N} / \mathrm{A}$ |
| Adjusted Capital | $\$ 3,941,984$ | $\$ 5,840,000$ | $\$ 4,909,206$ | $\$ 4,909,206$ |
| Required Capital | $\$ 732,895$ | $\$ 2,070,581$ | $\$ 1,608,031$ | $\$ 1,438,551$ |
| Total Ratio | $\mathrm{N} / \mathrm{A}$ | $299 \%$ | $\mathrm{~N} / \mathrm{A}$ | $\mathrm{N} / \mathrm{A}$ |
| Capital Ratio ${ }^{1}$ | $538 \%$ | $282 \%$ | $305 \%$ | $341 \%$ |

${ }^{1}$ For Canada, the Capital Ratio is actually the Core Ratio.

The following table shows the required actions to be taken by the regulator based on each jurisdiction's ratio. In our example, the Base Scenario and the Changed Liability Scenario results show that none of the four jurisdictions require regulatory actions. Under the Riskier Asset Scenario, all but Solvency II require the regulatory intervention.

## Table 14

CAPITAL REQUIREMENT ACTIONS BY JURISDICTION

| Jurisdiction and Ratio |  | Required Action |
| :---: | :---: | :---: |
| US |  |  |
| $200 \%<=$ RBC Ratio < 250\% | Trend Test Corridor | Company must perform trend test |
| $150 \%<=$ RBC Ratio $<200 \%$ | Company Action Level | Company must prepare and submit RBC plan to regulator |
| $100 \%<=$ RBC Ratio $<150 \%$ | Regulator Action Level | Company must submit (or revise) RBC plan and regulator will issue an <br> order of corrective action |
| $70 \%<=$ RBC Ratio $<100 \%$ | Authorized Control Level | Authorizes regulator to take actions necessary to protect stakeholders |
| RBC Ratio $<70 \%$ | Mandatory Control Level | Requires regulator to put Company under regulatory control |
| Canada |  |  |
| $70 \%<=$ Total Ratio $<100 \%$ OR <br> $55 \%<=$ Core Ratio $<90 \%$ | Early Intervention Process | OSFI may impose business restrictions as necessary and/or issue <br> directions of compliance |
| Total Ratio $<70 \%$ OR Core <br> Ratio $<55 \%$ | Minimum Required Level | Below this level, the OSFI may temporarily place the company under <br> regulatory control. |
| Europe |  |  |
| $25 \%<=$ Basic SCR Ratio < 45\% | Early Intervention Process | Increasingly severe prescribed supervisory actions will be taken as capital <br> decreases toward $25 \%$ |
| Basic SCR Ratio < 25\% | Minimum Required Level | Below this level, Company loses its authorization to operate |
| Bermuda |  |  |
| 100\% <= ECR Ratio < 120\% | Early Intervention Process | Company must submit a remediation plan and provide additional <br> reporting for enhanced monitoring |
| ECR Ratio $<100 \%$ | Minimum Required Level | Below this level, the Company must improve its capital position and faces <br> wind-up of business |

Changes to asset or liability mix will generally change the required capital in each jurisdiction, and the direction of the changes will generally be the same in all four jurisdictions. The changes are not as similar in amounts or as ratios, but further review of the results shows that regulatory action may be more similar than the ratios themselves. For example, while the base scenario shows the US RBC ratio of $423 \%$ and the Solvency II Solvency ratio is $189 \%$, the US regulator would begin requiring company action under $200 \%$, while the European regulator would not act until the level of capital fell below MCR, which is between $25 \%$ and $45 \%$ of BSR. Likewise in Canada the capital level would have to fall to the point where the Core Ratio falls below $55 \%$ for a company to be deemed insolvent.

We have chosen an extreme scenario for the risky assets example. Instead of bonds being $75 \%$ of the portfolio, they are reduced to $20 \%$. Two of the four jurisdictions would require the company to submit a plan for rehabilitation of the capital adequacy. Under LICAT and Solvency II, the company would not be required to do so.

When the insurance portfolio mix is changed to weight annuities at $75 \%$ of the reserves, the capital levels remain healthy in all jurisdictions, but the capital requirements are affected differently. Under Solvency II, required capital is reduced by $45 \%$ and has the largest change in required capital, while in the US the required capital is reduced by only $21 \%$.

## Section 9: Conclusion

As discussed in this paper, each jurisdiction has its own set of capital requirements. Capital requirements and ratios will depend on the insurance company's mix of assets and liabilities, as well as corresponding underlying assumptions, methodologies and models.

The model results presented in this paper illustrate how a company may change its capital (required and available) by changing its product or asset mix. However, it is important to note that many of these types of changes are not instantaneous. For instance, changing product mix may involve changes to sales goals, marketing, and pricing, which is a gradual process. Alternatively, other types of changes to the risk profile may be implemented more quickly. Reinsurance may be used to assume or cede a particular liability risk, which will have a more immediate impact on the balance sheet and capital position.

Likewise, changes to asset mix may be made to either better align asset and liability cash flows or to increase yields on the asset portfolio. Required capital formulas recognize that these changes will impact the probability of solvency. Capital requirements are higher when assets carry more risk, but regulators in different jurisdiction view the risk of particular assets (or asset management practices) differently than their peers.

This paper has demonstrated similarities and differences in four jurisdictions. An Excel tool supplements this paper by illustrating the capital requirements for the four jurisdictions as well as two alternative scenarios. The reader should have attained an understanding of the methodology variations between jurisdictions and general implications of modifications to asset or liability mix on required capital for each of these jurisdictions.

## Section 10: Acknowledgments

The researchers acknowledge the support of those without whose efforts this project could not have come to fruition: the volunteers who generously shared their wisdom, insights, advice, guidance, and arm's-length review of this study prior to publication. Any opinions expressed may not reflect their opinions nor those of their employers. Any errors belong to the authors alone.

Project Oversight Group members:

Ravi Bhandari, FSA, MAAA, CFA, CIA

Nancy Davis, FSA

John Di Meo, FSA, CERA, MAAA

Maambo Mujala, FSA, MAAA

Sean Voien, FSA, CERA, MAAA

At the Society of Actuaries Research Institute:

Doug Chandler, FSA, FCIA, Canadian Retirement Research Actuary

Dale Hall, FSA, CERA, CFA, MAAA, Managing Director of Research

## Appendix A: Solvency II Formulas

For the 5 major categories, the correlation matrix is:

where:

$$
\text { Basic SCR }=\sqrt{\sum_{i, j} \operatorname{Corr}_{i, j} \times S C R_{i} \times S C R_{j}}
$$

## Table A. 1

BASIC SCR CORRELATION FACTORS (CORR $\left.\mathrm{I}_{1}, \mathrm{~J}\right)$

| i | Market | Default | Life | Health | Non-Life |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Market | 1.00 | 0.25 | 0.25 | 0.25 | 0.25 |
| Default | 0.25 | 1.00 | 0.25 | 0.25 | 0.50 |
| Life | 0.25 | 0.25 | 1.00 | 0.25 | 0.00 |
| Health | 0.25 | 0.25 | 0.25 | 1.00 | 0.00 |
| Non-Life | 0.25 | 0.50 | 0.00 | 0.00 | 1.00 |

The life risk and market risk have their own correlation calculations:

$$
S C R_{l i f e}=\sqrt{\sum_{i, j} \operatorname{Corr}_{i, j} \times S C R_{i} \times S C R_{j}}
$$

Table A. 2

LIFE RISK CORRELATION FACTORS (CORR ${ }_{\mathrm{l}}, \mathrm{j}$ )

| i | Mortality | Longevity | Disability | Lapse | Expense | Revision | Catastrophe |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Mortality | 1.00 | -0.25 | 0.25 | 0.00 | 0.25 | 0.00 | 0.25 |
| Longevity | -0.25 | 1.00 | 0.00 | 0.25 | 0.25 | 0.25 | 0.00 |
| Disability | 0.25 | 0.00 | 1.00 | 0.00 | 0.50 | 0.00 | 0.25 |
| Lapse | 0.00 | 0.25 | 0.00 | 1.00 | 0.50 | 0.00 | 0.25 |
| Expense | 0.25 | 0.25 | 0.50 | 0.50 | 1.00 | 0.50 | 0.25 |
| Revision | 0.00 | 0.25 | 0.00 | 0.00 | 0.50 | 1.00 | 0.00 |
| Catastrophe | 0.25 | 0.00 | 0.25 | 0.25 | 0.25 | 0.00 | 1.00 |

$$
S C R_{\text {market }}=\sqrt{\sum_{i, j} \operatorname{Corr}_{i, j} \times S C R_{i} \times S C R_{j}}
$$

Table A. 3

MARKET RISK CORRELATION FACTORS (CORR ${ }_{\mathrm{l}, \mathrm{j}}$ )

| I | Interest <br> Rate | Equity | Property | Spread | Concentration | Currency |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Interest Rate | 1.00 | A | A | A | 0.00 | 0.25 |
| Equity | A | 1.00 | 0.75 | 0.75 | 0.00 | 0.25 |
| Property | A | 0.75 | 1.00 | 0.50 | 0.00 | 0.25 |
| Spread | A | 0.75 | 0.50 | 1.00 | 0.00 | 0.25 |
| Concentration | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| Currency | 0.25 | 0.25 | 0.25 | 0.25 | 0.00 | 1.00 |

For Market Risks, A denotes the value of 0.5 if the market is "up" and 0 if down.

Companies subject to Solvency II are also required to calculate a Risk Margin (RM), which is meant to consider a longer-term solvency standpoint.

$$
R M=\operatorname{CoC} \times \sum_{t} \frac{S C R(t)}{(1+r(t+1))^{t+1}}
$$

Where:

- $\quad$ CoC denotes the Cost-of-Capital rate;
- $\quad \mathrm{SCR}(\mathrm{t})$ denotes the Solvency Capital Requirement after $\mathrm{t}$ years;
- $r(t+1)$ denotes the basic risk-free interest rate for the maturity of $t+1$ years.

The basic risk-free interest rate $(r(t+1))$ shall be chosen in accordance with the currency used for the financial statements of the insurance and reinsurance undertaking.

## Appendix B: Bermuda Solvency Capital Requirement Formulas

The Group BSCR uses the following formula

BSCR

$=\sqrt{C_{f i}^{2}+C_{e q}^{2}+C_{\text {int }}^{2}+C_{\text {curr }}^{2}+C_{\text {conc }}^{2}+C_{\text {prem }-g b}^{2}+\left[1 / 2 C_{\text {cred }}+C_{\text {rsvs }-g b}\right]^{2}+\left[1 / 2 C_{\text {cred }}\right]^{2}+\left(C_{L T m o r t}+C_{L T s l}+C_{L T r}\right)^{2}}$

Cont'd

$\sqrt{-0.5 \times\left(C_{\text {LTmort }}+C_{\text {LTsl }}+C_{\text {LTr }}\right) \times C_{\text {LTlong }}+C_{\text {LTlong }}^{2}+C_{\text {LTmorb }}^{2}+C_{\text {LTVA }}^{2}+C_{\text {LTother }}^{2}+C_{\text {cat-gb }}^{2}+C_{o p}+C_{\text {adj }}}$

$+\left[B S C R_{\text {corr }}\right.$

$-\left(\sqrt{C_{f i}^{2}+C_{e q}^{2}+C_{\text {int }}^{2}+C_{\text {curr }}^{2}+C_{\text {conc }}^{2}+C_{\text {prem }-g b}^{2}+\left[1 / 2 C_{\text {cred }}+C_{\text {rsvs }-g b}\right]^{2}+\left[1 / 2 C_{\text {cred }}\right]^{2}+\left(C_{L T m o r t}+C_{L T s l}+C_{L T r}\right)^{2}}\right.$

Cont'd

$\left.\left.\sqrt{-0.5 \times\left(C_{\text {LTmort }}+C_{L T S l}+C_{L T r}\right) \times C_{\text {LTlong }}+C_{\text {LTlong }}^{2}+C_{\text {LTmorb }}^{2}+C_{\text {LTVA }}^{2}+C_{\text {LTother }}^{2}+C_{\text {cat-gb }}^{2}+C_{o p}+C_{a d j}}\right)\right]$

where:

$\mathrm{C}_{\mathrm{fi}}=$ capital charge in respect of fixed income investment risk;

$\mathrm{C}_{\text {eq }}=$ capital charge in respect of equity investment risk capital;

$\mathrm{C}_{\text {int }}=$ capital charge in respect of interest rate and liquidity risk;

$\mathrm{C}_{\text {curr }}=$ capital charge in respect of currency risk;

$\mathrm{C}_{\text {conc }}=$ capital charge in respect of concentration risk;

$\mathrm{C}_{\text {prem }}=$ capital charge in respect of general business premium risk;

$C_{\text {rsvs }}=$ capital charge in respect of general business reserve risk;

$\mathrm{C}_{\text {cred }}=$ capital charge in respect of credit risk capital;

$\mathrm{C}_{\mathrm{cat}}=$ capital charge in respect of catastrophe risk;

$\mathrm{C}_{\text {LTmort }}=$ capital charge in respect of Long-Term - mortality;

$C_{\text {LTSI }}=$ capital charge in respect of Long-Term - stop loss;

$C_{L T r}=$ capital charge in respect of Long-Term- riders;

$C_{\text {LTmorb }}=$ capital charge in respect of Long-Term - morbidity \& disability;

$\mathrm{C}_{\text {LTlong }}=$ capital charge in respect of Long-Term - longevity;

$C_{\text {LTVA }}=$ capital charge in respect of Long-Term - variable annuity guarantee risk;

$\mathrm{C}_{\text {LToth }}=$ capital charge in respect of Long-Term - other insurance risk;
$\mathrm{C}_{\mathrm{op}}=$ capital charge in respect of operational risk; and

$C_{\text {adj }}=$ capital charge adjustment, calculated as the sum of (a), (b) and (c) where:

(a) Regulatory capital requirement for regulated non-insurance financial operating entities;

(b) Regulatory capital requirement for unregulated entities; and

(c) Capital adjustment for the loss absorbing capacity of deferred taxes.

<img src="https://cdn.mathpix.com/cropped/2024_04_13_59edaaf1c3ec26f7eb72g-34.jpg?height=49&width=1166&top_left_y=737&top_left_x=477" alt="image" style="width:100%;height:auto;">

where:

Basic BSCR = Basic BSCR Risk Module charge

<img src="https://cdn.mathpix.com/cropped/2024_04_13_59edaaf1c3ec26f7eb72g-34.jpg?height=49&width=482&top_left_y=978&top_left_x=369" alt="image" style="width:100%;height:auto;">

$\mathrm{C}_{\text {regulatory adj }}=$ regulatory capital requirement for non-insurance financial operating entities

Cother adj $=$ adjustment for the loss absorbing capacity of technical provisions

$\mathrm{C}_{\text {Adjp }}=$ adjustment for the loss absorbing capital of deferred taxes

$$
\text { Basic BSCR }=\sqrt{\sum_{i, j} \operatorname{CorrBBSCR} R_{i, j} \times C_{i} \times C_{j}}
$$

where:

CorrBBSCR $_{i, j}$ - the correlation factors of the Basic BSCR correlation matrix from Table A

$C_{i}$ and $C_{j}$ are risk module charges which should be replaced with $C_{\text {Market }}, C_{P \& C}, C_{L T}$, or $C_{\text {credit }}$

$\mathrm{C}_{\text {Market }}=$ capital charge for Market Risk

$C_{P \& C}=$ capital charge for $P \& C$ risk

$C_{L T}=$ capital charge for Long-term Risk, and

$\mathrm{C}_{\text {Credit }}=$ capital charge for credit risk

Table B. 1

BASIC BSCR CORRELATION MATRIX

| CorrBBSCR $\mathbf{R}_{\mathbf{i}, \mathrm{j}}$ | $\mathbf{C}_{\text {Market }}$ | $\mathbf{C}_{\text {P\&C }}$ | $\mathbf{C}_{\mathbf{L T}}$ | $\mathbf{C}_{\text {Credit }}$ |
| :--- | :--- | :--- | :--- | :--- |
| $\mathrm{C}_{\text {Market }}$ | 1.000 |  |  |  |
| $\mathrm{C}_{\text {P\&C }}$ | 0.250 | 1.000 |  |  |
| $\mathrm{C}_{\mathrm{LT}}$ | 0.125 | 0.500 | 1.000 |  |
| $\mathrm{C}_{\text {Credit }}$ | 0.125 | 0.250 | 0.000 | 1.000 |

$$
C_{\text {Market }}=\sqrt{\sum_{i, j} \text { CorrMarket }_{i, j} \times C_{i} \times C_{j}}
$$

CorrMarket represents market risk, and in Table 5 (below), $A=$ zero if the interest rate and liquidity risk charge is calculated using the shock-based approach, or $A=0.25$ is using the interest rate up shock

$\mathrm{C}_{\text {fixedlncome }}=$ capital charge for fixed income investment risk (factor-based charges)

<img src="https://cdn.mathpix.com/cropped/2024_04_13_59edaaf1c3ec26f7eb72g-35.jpg?height=46&width=685&top_left_y=709&top_left_x=243" alt="image" style="width:100%;height:auto;">

$\mathrm{C}_{\text {interest }}=$ capital charge for interest rate and liquidity risk

$\mathrm{C}_{\text {currency }}=$ capital charge for currency risk

$\mathrm{C}_{\text {concentration }}=$ capital charge for concentration risk

Table B. 2

MARKET RISK CORRELATION MATRIX

| CorrMarket $_{\mathrm{i}, \mathrm{j}}$ | <img src="https://cdn.mathpix.com/cropped/2024_04_13_59edaaf1c3ec26f7eb72g-35.jpg?height=46&width=141&top_left_y=1128&top_left_x=609" alt="image" style="width:100%;height:auto;"> | $\mathrm{C}_{\text {Equity }}$ | $\mathbf{C}_{\text {Interest }}$ | C $_{\text {Currency }}$ | $\mathrm{C}_{\text {Concentration }}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $C_{\text {Fixedincome }}$ | 1.00 |  |  |  |  |
| <img src="https://cdn.mathpix.com/cropped/2024_04_13_59edaaf1c3ec26f7eb72g-35.jpg?height=46&width=231&top_left_y=1209&top_left_x=261" alt="image" style="width:100%;height:auto;"> | 0.50 | 1.00 |  |  |  |
| $\mathrm{C}_{\text {Interest }}$ | A | A | 1.00 |  |  |
| <img src="https://cdn.mathpix.com/cropped/2024_04_13_59edaaf1c3ec26f7eb72g-35.jpg?height=46&width=231&top_left_y=1288&top_left_x=261" alt="image" style="width:100%;height:auto;"> | 0.25 | 0.25 | 0.25 | 1.00 |  |
| $\mathrm{C}_{\text {Concentration }}$ | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |

Where $\mathrm{A}$ is 0 if the interest rate and liquidity risk charge is calculated using the shock-based approach and the risk charge is based on the interest rate up shock; $A$ is 0.25 otherwise.

This paper will not discuss the P\&C Risk Module charge as the focus of this paper is on life insurance companies.

$$
C_{L T}=\sqrt{\sum_{i, j} \operatorname{Corr} L T_{i, j} \times C_{i} \times C_{j}}
$$

CorrLT $T_{i, j}$ represents the long-term risk correlations

$C_{\text {LTmortality }}=$ Capital charge for mortality risk

$C_{\text {LTstoploss }}=$ Capital charge for stop loss risk

$C_{L T r i d e r}=$ Capital charge for riders risk (risks not covered in the other LT categories)

$\mathrm{C}_{\text {LTmobidity }}=$ Capital charge for morbidity risk

$C_{L T \text { longevity }}=$ Capital charge for longevity risk

$C_{\text {LTVariableAnnutiy }}=$ Capital charge for variable annuity risk

$C_{\text {LTotherrisk }}=$ Capital charge for other long-term insurance risk (policyholder behavior, expenses, and guarantees).

Table B. 3

LONG-TERM RISK MODULE CORRELATION MATRIX

| CorrLT ${ }_{i, j}$ | $\mathbf{C}_{\text {LTmortality }}$ | $\mathbf{C}_{\text {LTstoploss }}$ | $\mathbf{C}_{\text {LTrider }}$ | $\mathbf{C}_{\text {LTmobidity }}$ | $\mathbf{C}_{\text {LTlongevity }}$ | $\mathbf{C}_{\text {LTVariableAnnutiy }}$ | $\mathbf{C}_{\text {LTotherrisk }}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\mathrm{C}_{\text {LTmortality }}$ | 1.00 |  |  |  |  |  |  |
| $\mathrm{C}_{\text {LTtoploss }}$ | 0.75 | 1.00 |  |  |  |  |  |
| $\mathrm{C}_{\text {LTrider }}$ | 0.75 | 0.75 | 1.00 |  |  |  |  |
| $\mathrm{C}_{\text {LTmobidity }}$ | 0.25 | 0.00 | 0.00 | 1.00 |  |  |  |
| $\mathrm{C}_{\text {LTIongevity }}$ | -0.50 | -0.50 | -0.50 | 0.00 | 1.00 |  |  |
| $\mathrm{C}_{\text {LTVariableAnnutiy }}$ | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |  |
| $\mathrm{C}_{\text {LTotherrisk }}$ | 0.125 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 1.00 |

The operational risk charge under BIS is a charge multiplied by the gross BSCR after correlation adjustment and the loss -absorption adjustment. The charge ranges from $1 \%$ to $20 \%$ and is based on the insurance group's selfassessment of this risk.

## Appendix C: Model Simplifications

## C. 1 SIMPLIFICATIONS THAT APPLY TO ALL JURISDICTIONS

- All assets are denominated in the jurisdiction being modeled and assume that currency risk is zero.
- All liabilities were issued in the jurisdiction being modeled, and cross border risk profile differences are zero.


## C. 2 SIMPLIFICATIONS SPECIFIC TO US RBC

- Tax Rate is $21 \%$
- Statutory reserves are $15 \%$ greater than model reserves for life insurance, and $95 \%$ of annuity model reserves.
- Book value of bonds is assumed to be $7.5 \%$ lower than market value; for all other assets, Book Value equals Market Value


## C. 3 SIMPLIFICATIONS SPECIFIC TO CANADIAN LICAT

For the Canadian LICAT calculations, some of our model simplifications are significantly simpler than the actual calculation. For example, the Basic Capital requirement for currency risk $B C R_{\text {currency }}$ is the sum of the following amounts that are denominated in the currency under consideration:

1. $2.8 \%$ of all liabilities;
2. $0.24 \%$ of the net amount at risk for term products and other life products that do not have significant cash values;
3. $2.4 \%$ of liabilities for:

i. life products that have significant cash values;

ii. participating contracts; and

iii. accident, health, and disability coverage;
4. $4.8 \%$ of annuity liabilities;
5. $4.4 \%$ of liabilities for GICs, or of notional value for synthetic GICs (e.g., wraps); and
6. $4.8 \%$ of guaranteed value for segregated funds.

In deciding that all assets and liabilities are denominated in the jurisdiction being modeled, we have eliminated all of this calculation, and assume that currency risk is zero.

In addition to assuming no currency risk, the following simplifications have been made:

- There are no Deferred Tax Assets and off-balance sheet activities
- $\quad$ No preferred shares or convertible bonds
- Canadian interest rate risk is the same value as the Solvency II interest rate risk
- There are no Mutual Funds, Index-Linked product, unregistered reinsurance
- Mortality risk has been set to $\$ 2.5 \mathrm{M}$ for base and riskier asset scenario and $\$ 1.0 \mathrm{M}$ for changed liability mix scenario
- $\quad$ Longevity risk has been set to \$25K for base and riskier asset scenario and \$75K for changed liability mix scenario
- Lapse and Policyholder Behavior Risk is $\$ 10,000$
- Expense Risk is $\$ 10,000$
- Assume no guaranteed minimum death and maturity benefits offered for segregated fund guaranteed products
- Assume no segregated fund guarantees and no reinsurance
- The only Tier 1 capital is contributed surplus and adjusted retained earnings

o Adjusted Retained Earnings $\$ 120,000$

- $\quad$ No Tier 1 deductions
- No Tier 2 capital
- Surplus Allowance is $\$ 1,000,000$ and there are no eligible deposits


## C. 4 SIMPLIFICATIONS SPECIFIC TO SOLVENCY II

- Asset and liability market values and risk margins are an input, rather than a calculation. Liabilities are input as total technical provisions, without a split between best estimate and risk margin
- Calculation shows the Basic Solvency Capital Requirement using the "standard formula" only, i.e., no internal model and no Minimum Capital Requirement (MCR) calculation
- While available capital ("own funds") is shown, there is no classification of own funds by tier (in other words, it will be inherently assumed that all own funds are tier 1 capital)
- Expense component of the SCR is a fixed input (i.e., it is be calculated based on the Solvency II rules, since doing so would just require a judgement-based input for expense levels anyway)
- Other components of the SCR (mortality, longevity, interest, equity, property, spread) use the SII "simplified calculation" (more factor-based than model-based)


## C. 5 SIMPLIFICATIONS SPECIFIC TO BERMUDA INSURANCE SOLVENCY

- Adjustment for the loss absorbing capacity of technical provisions and adjustment for the loss absorbing capital of deferred taxes are assumed to zero
- Equity capital charge has been set to $45 \%$ of equity assets
- Interest rate and liquidity risk charge has been set to $1 \%$ of total assets
- Capital charge for credit risk is assumed to be $\$ 100,000$
- Market value of assets and liabilities are assumed to be the same as those used for Solvency II even though the two jurisdictions use different discount rates


## Glossary

Asset Default Risk (LICAT): risk of loss resulting from on-balance sheet asset default and from off-balance sheet exposure; loss of market value of equities and corresponding loss of income.

Available capital: used by companies for growth of the current business, expansion into new business opportunities, investment in enhanced operational effectiveness and efficiency, and other strategic purposes.

Catastrophe Risk: for life contracts, this is the risk of a short term (one year) increase in mortality (additive to the one-year mortality rate)

Change in Interest Rate Risk (LICAT): the risk of loss resulting from changes in the interest rate environment other than asset default.

Counterparty Default Risk: the risk that a counterparty will not be able to pay its debts to the insurer. Under Solvency II, these are further divided into two types of counterparties - Type 1 includes all risk mitigation exposures, such as reinsurers, and Type 2 includes future receivables from policyholders, and mortgage loans.

Credit Risk: the risk of default on principal and income from the asset, such as bond coupons or mortgage payments. May also include risk associated with the impact on the balance sheet associated with movements in credit spreads.

Credit Risk (Bermuda): the risk of loss arising from an insurance group's inability to collect funds from debtors.

Currency Risk: the risk that foreign exchange rates will change over the course of the projections.

Disability-Morbidity Risk: the risk that morbidity claims are worse than expected.

Disintermediation Risk: the risk that policyholders relinquish policies faster than expected due to rising interest rates.

Economic Capital: a company calculation of the difference between best estimate assets and best estimate liabilities.

Equity Risk: the risk that equities held by the insurer have an immediate decrease in market value.

Expense Risk: the risk that expenses exceed best estimates.

Foreign Exchange Risk (LICAT): risk of loss from fluctuations in currency exchanges.

Interest Rate Risk: the risk that the value of an asset or liability will change due to a change in term structure of interest rates or interest rate volatility.

Lapse Risk: the risk that policyholders change their lapse profile either permanently or in a mass event.

Long-Term Risk (Bermuda): the risk arising from fluctuation in values from long-term liabilities. This includes mortality, stop loss, morbidity, longevity, variability annuity and other long-term insurance risk.

Longevity Risk: the risk that mortality is lower than expected. This is generally a negative situation for annuities in payout status.

Market Risk: the risk of change in price, such as changes in the level of interest rates and equity market and exchange rate movements, which may include views of future credit risk.

Market risk (Bermuda): the risk arising from fluctuations in values of, or income from, assets or in interest rates or exchange rates. This risk covers fixed income, equity, interest, current and concentration risks.

Market Risk Concentration: the risk that a single counterparty can have a significant impact on investment returns.

Morbidity Risk: the risk policyholders develop covered illnesses or diseases beyond that assumed in pricing or valuation. This may be due to extended duration of illness, earlier onset, or additional instances of illness or disease.

Mortality Risk: the risk that mortality is higher than expected and death benefits are paid earlier than originally expected.

Mortality/Morbidity/Lapse Risks (LICAT): risks that the company's assumptions prove incorrect.

P\&C Risk: the risk arising from fluctuations in values of property and casualty insurance. This includes premium, reserve, and catastrophe risk.

Property Risk: the risk that real estate prices immediately drop.

Regulatory Required Capital: the amount of capital regulators requires the company to maintain for policyholder protection purposes.

Revision Risk: the risk that annuity payments increase due to changes in either the legal environment or health of the annuitant.

Required Capital: the capital that must be set aside, and typically held in relatively safe investments, to cover the potential for future adverse events.

Risk Margin: For Solvency II, this is meant to consider a longer-term solvency standpoint.

Segregated Funds (Canada) or Separate Account (US): a separate set of financial statements held by a life insurance company, maintained to report assets and liabilities for specific products that are separated from the insurer's general account.

Segregated Funds Risk (LICAT): risk of loss arising from guarantees embedded in segregated funds.

Spread Risk: the risk that bonds have a change to level or volatility of credit spreads (spreads over the risk-free rates). The risk is based on duration and type of asset held. This applies to bonds, debt instruments, mortgagebacked securities, credit derivatives, and similar assets.

Total Capital: the difference between assets held by the company and liabilities owed by the company.

## References

The following documents have been reviewed to prepare portions of the information provided in this report (along with links, if available).

Bermuda Monetary Authority. 2021. The Bermuda Capital and Solvency Return - 2021 Instruction Handbook for Insurance Groups.

2021-12-06-09-04-38-2021-Year-End-Insurance-Group-Instructions-Handbook.pdf (bma.bm)

Bermuda Monetary Authority. 2021. 2021 Stress and Scenario Instructions for class 4 3B and Insurance Groups. https://cdn.bma.bm/documents/2022-03-08-09-47-15-2021-Year-End-Stress-and-Scenario-Instructions-for-Class-43B-and-Insurance-Groups.pdf

Bipartisan Policy Center. 2015. Global Insurance Regulatory Issues: Implications for U.S. Policy and Regulation https://bipartisanpolicy.org/download/?file=/wp-content/uploads/2019/03/Global-Insurance-RegulatoryIssues.pdf

European Actuarial Journal. 2016. Solvency II, Solvency Capital Requirement for Life Insurance Companies Based on Expected Shortfall

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5744639/pdf/13385 2017 Article 160.pdf

European Insurance and Occupational Pensions Authority. 2020. Opinion on the 2020 Review of Solvency II https://www.eiopa.europa.eu/sites/default/files/solvency ii/eiopa-bos-20-749-opinion-2020-review-solvencyii.pdf

European Union Law: EUR LEX. 2021. Directive 2009/138/EC of the European Parliament and of the Council of 25 November 2009 on the taking-up and pursuit of the business of Insurance and Reinsurance (Solvency II) https://eurlex.europa.eu/legal-content/EN/TXT/?uri=CELEX\%3A02009L0138-20210630

Farr, Kourasaris, Mennemeyer. 2016. Economic Capital for Life Insurance Companies.

https://www.soa.org/globalassets/assets/files/research/projects/research-2016-economic-capital-lifeinsurance-report.pdf

Hardy, Saunders, Sharara. 2010. A Comparative Analysis of U.S., Canadian and Solvency II Capital Adequacy

Requirements in Life Insurance

https://www.soa.org/globalassets/assets/files/research/projects/research-2010-08-comparative-analysis.pdf

Herzog. 2011. Summary of CEIOPS Calibration Work on Standard Formula

https://www.naic.org/documents/index smi solvency ii calibration.pdf

Institute and Faculty of Actuaries. 2016. SOLVENCY II - LIFE INSURANCE

https://www.actuaries.org.uk/system/files/field/document/landF SA2 Solvencyll 2016.pdf

Lombardi. 2006. Valuation of Life Insurance Liabilities (Fourth Edition)

Office of the Superintendent of Financial Institutions Canada. 2022. Life Insurance Capital Adequacy Test https://www.osfi-bsif.gc.ca/Eng/fi-if/rtn-rlv/fr-rf/Pages/licat23 inst.aspx

Office of the Superintendent of Financial Institutions Canada. 2017. Regulatory Capital and Internal Capital Targets Regulatory Capital and Internal Capital Targets (osfi-bsif.gc.ca)

Office of the Superintendent of Financial Institutions Canada. Guide to Intervention for Federally Regulated Life Insurance Companies

Guide to Intervention for Federally Regulated Life Insurance Companies (osfi-bsif.gc.ca)

Thoren. 2015. Introduction to Solvency II SCR Standard Formula for Market Risk. https://www.casact.org/sites/default/files/2021-10/C-14-Thoren.pdf

About The Society of Actuaries Research Institute

Serving as the research arm of the Society of Actuaries (SOA), the SOA Research Institute provides objective, datadriven research bringing together tried and true practices and future-focused approaches to address societal challenges and your business needs. The Institute provides trusted knowledge, extensive experience and new technologies to help effectively identify, predict and manage risks.

Representing the thousands of actuaries who help conduct critical research, the SOA Research Institute provides clarity and solutions on risks and societal challenges. The Institute connects actuaries, academics, employers, the insurance industry, regulators, research partners, foundations and research institutions, sponsors and nongovernmental organizations, building an effective network which provides support, knowledge and expertise regarding the management of risk to benefit the industry and the public.

Managed by experienced actuaries and research experts from a broad range of industries, the SOA Research Institute creates, funds, develops and distributes research to elevate actuaries as leaders in measuring and managing risk. These efforts include studies, essay collections, webcasts, research papers, survey reports, and original research on topics impacting society.

Harnessing its peer-reviewed research, leading-edge technologies, new data tools and innovative practices, the Institute seeks to understand the underlying causes of risk and the possible outcomes. The Institute develops objective research spanning a variety of topics with its strategic research programs: aging and retirement; actuarial innovation and technology; mortality and longevity; diversity, equity and inclusion; health care cost trends; and catastrophe and climate risk. The Institute has a large volume of topical research available, including an expanding collection of international and market-specific research, experience studies, models and timely research.


[^0]:    ${ }^{1}$ Certain assets are held at market value.

[^1]:    ${ }^{2}$ Variable annuity reserves are based on modeled values. Certain life insurance reserves require modeling, and the NAIC is currently contemplating modeled reserves for fixed annuities.

[^2]:    ${ }^{4}$ Solvency II uses a similar method as discussed in the next Section of this paper.

    ${ }^{5}$ Segregated Funds are a separate set of financial statements held by a life insurance company, maintained to report assets and liabilities for specific products that are separated from the insurer's general account.

[^3]:    ${ }^{6}$ Section D1.5 of Bermuda Monetary Authority, The Bermuda Capital and Solvency Return, 2021 Instruction Handbook for Insurance Groups

[^4]:    ${ }^{7}$ Bermuda has a multi-license system of regulation, which categorizes licensees into general insurance company classes, long-term insurance company classes, special purpose insurer classes, innovative classes, collateralized insurer classes and intermediaries.


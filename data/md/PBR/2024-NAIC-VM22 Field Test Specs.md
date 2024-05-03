# Annuity Reserves and Capital Subcommittee Reserves \& Capital Field Testing Description \& Specifications March 6, 2024 

Primary Contacts:
- Steve Jackson (sjackson@actuary.org)
- Amanda Barry-Moilanen (barrymoilanen@actuary.org)

## Section I: Field Study Overview

### Objectives

1) Measure the impact on actual business of the proposed reserve and capital frameworks relative to the current standards to ensure frameworks are working as intended.

- Conduct field test to inform decisions related to the proposed fixed annuity principlebased reserving (PBR) methodology:
    - Test exclusion testing, allocation, proposed treatment for hedging indexed credit, aggregation, and other methodology elements.
    - Whenever this document references the PBR methodology, it means the framework documented in the most recent exposure draft: VM-22 Draft - July 2023 (https://content.naic.org/sites/default/files/inline-files/VM-22%20Subgroup%20Draft%20July%202023%20Clean%20%281%29.docx).

2) At a high-level, ensure pillars of framework are met:

- **Appropriate Reflection of Risk** - All else equal, greater risk in adverse conditions requires greater statutory reserves/capital, and vice-versa.
- **Comprehensive** - The statutory reserve accounts for all material risks covered in the Valuation Manual and inherent in product features and potential management actions associated with the policies or contracts being valued.
- **Consistency Across Products** - Statutory reserves between two contracts with similar features and risks are consistent given the same anticipated experience, regardless of product type.
- **Practicality and Appropriateness** - Balance principles above with an approach that is practical, auditable, and able to be implemented.

3) Test the impact of key open $V M$ - 22 design decisions:

- Aggregation
- Reinvestment guardrails
- Exclusion test
- Standard Projection Amount assumptions

### Tentative Timeline: July-September 2024

### Structure

- Propose exploring a coordinated effort between Academy, the National Association of Insurance Commissioners (NAIC), and American Council of Life Insurers (ACLI)
    - Propose to hire an external consultant who can:
    - Provide companies, collectively and individually, with information on calculations requested;
    - Help design field test and communicate with companies;
    - Work with Academy Research staff to help aggregate and summarize results; and
    - Potentially supplement the analysis of the field test results with analysis of factors affecting certain calculations, and/or assessing separate impacts on elements that are less feasible for companies to test.
- These specifications, and associated appendices, serve as a guide for purposes of responding to the RFP.

**Products Covered (companies can choose which of their products to field test)**

- Deferred Annuities
    - Fixed Indexed Annuities (FIAs) with Guaranteed Living Benefits (GLBs)
    -  FIAs without GLBs
    - Fixed Deferred Annuities (FDAs) with GLBs (if at least five participating companies to ensure anonymity)
    - FDAs without GLBs (if at least five participating companies to ensure anonymity)
- Payout Annuities
    - Single Premium Immediate Annuities (SPIAs)
    - Pension Risk Transfer (PRT)
    - Deferred Income Annuities (DIAs) (if at least five participating companies to ensure anonymity)
    - Structured Settlement Contracts (SSCs) (if at least five participating companies to ensure anonymity)
- Potential Survey Questions
    - Does your company have "longevity reinsurance," as defined in VM-01?
    - Does your company have "modified guaranteed annuities," as defined in VM-A-255? If so, would you value them as variable or fixed annuities?
    - Are you planning on providing projected reserve results as part of your field test submission?


### Population

- For time $=0$, test at least 10 years of inforce for all non-variable annuity products included in your testing scope
- Participants must provide output by policy duration or issue year to provide a sense of the durational impact.
- At option of the participant, may test using all past inforce business.

### Time Zero Valuation Date

- $12 / 31 / 2023$ valuation date


### Model Type

- Use a model that can project future cash flows over the contract life for the modeled block.
    - Can be based on valuation model or pricing model.
- Encourage use of a model that can re-project reserves at future time periods if possible.
    - See Section $\mathrm{V}$ in this document for additional requirements on projecting future reserves.
    - If unable to project, proxy future durations by considering historical inforce product calculations for similar products at the associated duration.
    - Seek feedback from potential participants and consider recommendations from consultant.


## Section II: Assumption Specifications

### Asset Assumptions

- Use asset assumptions found in Valuation Manual (VM)-22 draft instructions.
- Participants should disclose methodology for asset allocation when providing results.
- Investment guardrail for fixed income investment strategy set to $5 \%$ Treasury, $15 \%$ AA, $40 \%$ AAA, $40 \%$ BBB, unless company-specific investment strategy would result in a higher reserve.
    - Set index-based hedging program error to the maximum of the company assumption and $1.5 \%$, which is deducted from hedge payoffs relative to index credits.
    - All other hedging program error set to $5 \%$ of the difference between "best efforts" run and the "adjusted run" Conditional Tail Expectation (CTE)70 amounts. This amount is added to the CTE70 "best efforts" run.
- Include margins on company experience assumptions (see subsection below).


### Liability Assumption \& Margin Requirements

- Prudent estimate assumptions for the VM-22 deterministic reserve.
    - Set, and disclose with results, margins on mortality, policyholder behavior, expenses, hedging, non-guaranteed elements (NGEs), withdrawals, and other assumptions as deemed necessary.
    - If a company does not wish to use its own margins, then use margins below:
        - +/-10\% mortality on plus/minus segments, $+5 \%$ maintenance expenses, $+/-10 \%$ on lapses (depending on lapse-supportedness), $150 \%$ dynamic lapses (capped at $100 \%$ lapse), $5 \%$ shift from no withdrawals to 10 -year GLB withdrawals, index hedging error at $5 \%$ ? Each margin must increase the reserve.


### Metrics / Output

- Provide following metrics at time zero:
    - Scenario level reserves
    - Commissioners' Annuity Reserve Valuation Method (CARVM) at valuation (VM-22, Actuarial Guideline (AG) 33, AG35, etc.)
    - C3P1 at valuation date
    - Standard Projection Amount
    - Exclusion test results by scenario


### Aggregation

- Calculate in the following three buckets, if possible:
    1. Deferred annuities with GLBs (FIAs or FDAs)
    2. Deferred annuities without GLBs (FIAs or FDAs)
    3. Payout annuities (SPIAs, DIAs, SSC, PRT, longevity reinsurance as applicable)
        - Optional: Split out SPIAs and PRT if not managed together
    4. Longevity reinsurance
- Provide mapping for which blocks meet aggregation criteria in current VM-22 framework draft.
- If unable to supply results in this manner, please provide a detailed explanation about why.


## Section III: Supplemental Testing

### Exclusion test exercise

- Time points tested: Year 0 (required) and year 10 (optional).
- For time $=0$, test at least 10 years of inforce for all non-variable annuity products included in your testing scope.
- For time $=10$, test the same population used for projected results described in section IV below.
- Scenarios Tested: 16 VM-20 economic scenarios for each mortality scenario specified below.
- Mortality Scenarios: +/-5\%.
- Exclusion Testing Aggregation: For only the exclusion test, test each of the following subcategories and provide mapping for how products would be aggregated in current VM-22 framework draft:
    - Deferred Annuities
        - a. FIAs with GLBs
        - b. FIAs without GLBs
        - c. FDAs with GLBs
        - d. FDAs without GLBs
    - Payout Annuities
        - e. Individual and joint life-contingent SPIA/DIAs
        - f. Individual non-life-contingent SPIA
        - g. Pension risk transfer contracts (split out as a separate group for deferred benefits as deemed appropriate)
        - h. Optional to test structured settlements separately or combine into above sections
    - Longevity reinsurance
    - All other
        - i. Please provide brief description of product for other in-scope products not specified above for which results are provided.

Indicate whether or not a hedging program exists for each block, and if so provide responses to the hedging survey questions below for each block.

### Survey Questions

- Hedging
    - Identify the type of hedging you do for products in VM-22 scope, for example,
        - hedge only index credits for index products;
            - For index credit hedging, are the hedges static, dynamic, or a blend of the two?
        - hedge GLBs and/or other guaranteed benefits;
        - other hedging (e.g., asset-liability matching (ALM) interest rate risk hedging);
        - type of hedging strategic objective or target (GAAP / Stat / Economic);
        - use of capital preservation hedges (i.e. macro hedges);
    - Do you have any concerns with following the VM-21 hedging approach for VM-22?
- Allocation
    - Confirm whether you are able apply the allocation methodology as described in VM-22 for all products in scope.
    - Identify any concerns with this allocation methodology.


### Standard Projection Amount (SPA)

Test the SPA as described in the latest exposure draft:

- Follow same aggregation approach as above.
- Test current draft VM-22 proposed assumptions and inputs to ensure the calculation is working as intended and producing reasonable results.


## Section IV: Projections

### Projection Metrics and Future Valuation Nodes

- Project following metrics at projection years 10 and 20 :
    - Account value and cash surrender value
    - CARVM (VM-22, AG33, AG35, etc.)
    - CTE70, CTE90, CTE95, CTE98, Median (specify whether margins are included)
    - For value at risk (VaR)/CTE runs, if available, provide:
        - Actuarial present value of benefits, expenses, and related amounts less the actuarial present value of premiums and related amounts plus the balance of any separate account assets at each valuation time node.
        - Present values are calculated using the discount factors implied by the NAER vector under the path of discount rates specified by the economic scenario.
- For shorter-duration contracts, such as deferred annuities without guarantees and surrender charges $<10$ years or annuities certain $<10$ years, request projection years 5 and 10 . If run-time is hindered, optionally provide only year 10 (year 5 for shorter-duration contracts).


### Population

- For projections, either create a population using inforce population based on the most recent issue year or use a pricing population (pricing cells) for a single year of issue business based on recent historical inforce business.


## Outer Loop Scenario Requirements

- The outer loop requirements should be based on unmargined PBR experience assumptions.
- Use scenario 9 for interest rates and equities from scenario generator for outer loop assumptions:
    - Interest rate and equity scenario assumptions will be provided to field testing participants.
    - Three sets of 200 scenarios, 600 in total (if including time 0 , time 10 , time 20 ), will be provided for field testing participants at each valuation point.
- Assume $0.5 \%$ mortality improvement and $2 \%$ expense inflation.
- Assume the company's inforce portfolio mix and reinvestment strategy (ignoring any VM guardrails).
- Use VM prescribed long-term spreads and defaults.


## Section V: Sensitivities

- Remove each assumption margin (mortality, lapse, withdrawal, expense and other) and provide results (summary at minimum, but all detail including capital is preferred).


## Appendix 1: Instructions for Life Risk Based Capital Formula

### Scope: 

All products in scope for the VM22 field test are also in scope for the C-3 RBC field test. GICs, Funding Agreements, Stable Value Contracts and Single Premium Life Insurance are not in scope for the field test. Use, at minimum, the same issue years tested for reserves should be in scope (participants may test more years if desired).

### Disclosure: 

Guidance is provided for the purposes of the Field Test, but these changes below do not represent an exposure draft. Any changes to LRO27 after or during the field test should supersede the guidance herein.

### Methodology:

The C-3 RBC is calculated as follows:

A. CTE ( $\underline{X}$ ) is calculated as follows (please see the field test specifications for $\mathrm{XX}$ testing values): Apply the CTE methodology described in NAIC Valuation Manual VM-22 and calculate the CTE (XX) as the numerical average of the (100-XX) percent largest values of the Scenario Reserves, as defined by Section 4 of VM-22. In performing this calculation, the process and methods used to calculate the Scenario Reserves use the requirements of VM-22 and should be the same as used for the reserve calculations. The effect of Federal Income Tax should be handled following one of the following two methods:

1. If using the Macro Tax Adjustment (MTA): The modeled cash flows will ignore the effect of Federal Income Tax. As a result, for each individual scenario, the numerical value of the scenario reserve used in this calculation should be identical to that for the same scenario in the Aggregate Reserve calculation under VM-22. Federal Income Tax is reflected later in the formula in paragraph B.1.
2. If using Specific Tax Recognition (STR): At the option of the company, CTE After-Tax (XX) (CTEAT (XX)) may be calculated using an approach in which the effect of Federal Income Tax is reflected in the projection of Accumulated Deficiencies, as defined in Section 4.A. of VM-22, when calculating the Scenario Reserve for each scenario. To reflect the effect of Federal Income Tax, the company should find a reasonable and consistent basis for approximating the evolution of tax reserves in the projection, taking into account restrictions around the size of the tax reserves (e.g., that tax reserve must equal or exceed the cash surrender value for a given contract). The Accumulated Deficiency at the end of each projection year should also be discounted at a rate that reflects the projected after-tax discount rates in that year. In addition, the company should add the Tax Adjustment as described below to the calculated CTEAT $(X X)$ value.
3. A company that has elected to calculate CTEAT (XX) using STR may not switch back to using MTA in the projection of Accumulated Deficiencies without prominently disclosing that change in the certification and supporting memorandum. The company should also disclose the methodology adopted, and the rationale for its adoption, in the documentation required by paragraph J below.
4. Application of the Tax Adjustment: Under the U.S. IRC, the tax reserve is defined. It can never exceed the statutory reserve nor be less than the cash surrender value. If a company is using STR and if the company's actual tax reserves exceed the projected tax reserves at the beginning of the projection, a tax adjustment is required.

The CTEAT (XX) must be increased on an approximate basis to correct for the understatement of modeled tax expense. The additional taxable income at the time of claim will be realized over the projection and will be approximated using the duration to worst, i.e., the duration producing the lowest present value for each scenario. The method of developing the approximate tax adjustment is described below.

The increase to CTEAT ( $X X$ ) may be approximated as the corporate tax rate times $f$ times the difference between the company's actual tax reserves and projected tax reserves at the start of the projections. For
this calculation, $\mathrm{f}$ is calculated as follows: For the scenarios reflected in calculating CTE (98), the Scenario Greatest Present Value scenario reserve is determined and its associated projection duration is tabulated. At each such duration, the ratio of the number of contracts in force (or covered lives for group contracts) to the number of contracts in force (or covered lives) at the start of the modeling projection is calculated. The average ratio is then calculated over all CTE (XX) scenarios and $\mathrm{f}$ is one minus this average ratio..

B. Determination of RBC amount using stochastic modeling:

1. If using the MTA: Calculate the RBC Requirement by the following formula in which the statutory reserve is the actual reserve reported in the Annual Statement. in the second term - i.e., the difference between statutory reserves and tax reserves multiplied by the Federal Income Tax Rate - may not exceed the portion of the company's non-admitted deferred tax assets attributable to the same portfolio of contracts to which VM21 is applied in calculating statutory reserves:

YY\% x ((CTE (XX) + [Additional Standard Projection Amount] - Statutory Reserve) x (1 - Federal Income Tax Rate) - (Statutory Reserve - Tax Reserve) x Federal Income Tax Rate)

2. If the company elects to use the STR: The C-3 RBC is determined by the following formula:

YY\% x (CTEAT (XX) + [Additional Standard Projection Amount] - Statutory Reserve)

(TBD) The Additional Standard Projection Amount is calculated using the methodology outlined in Section TBD of VM-22.If the Statutory Reserve does not include an Additional Standard Projection Amount then the calculation above will also omit that amount.

### Aggregation

Aggregation levels should be the same as those used for reserves.

### Interest Rate Risk vs. Market Risk

The objective is to assign a value for the risk of unexpected market shocks comparable to that assigned to variable products. This risk may result from optionality in either the product or the supporting assets.

The C-3 RBC amount above should be split into interest rate risk and market risk components using a method developed by the company, and sample methods are listed below. If the method was developed by the company, please provide details.

Method 1: Perform a single model run that reflects both (a) and (b) below:

- (a) Model no interest rate variation, by either (1) holding the Treasury curve on the valuation date constant over the projection for all scenarios or (2) use the expected forward curve for all scenarios or (3) use identical interest rate scenarios corresponding to the AIRG with all random variables set to zero

- (b) Model stochastic separate account returns in the usual way across all scenarios.

Compute the resulting C-3 RBC TAR and call this the C-3c component (market risk). Subtract this value from the true C-3 RBC TAR to determine the C-3a component (interest rate risk).

Method 2: Companies could also consider applying Stochastic Exclusion Test scenarios to bifurcate market and interest rate risk. The model run approach would be similar as Method 1.

## Appendix 2: VM-22 Field Test Template Definitions 

Unless otherwise specified, the section references below are from Valuation Manual VM-22.

### Reserves - Summary 

Commissioners Annuity Reserve Valuation Method (CARVM) Reserve $=$ the current minimum reserve valuation standard for non-variable annuities as determined by CARVM

CSV = Cash Surrender Value means, the amount available to the contract holder upon surrender of the contract. Generally, it is equal to the account value less any applicable surrender charges, where the surrender charge reflects the availability of any free partial surrender options. However, for contracts where all or a portion of the amount available to the contract holder upon surrender is subject to a market value adjustment, the cash surrender value shall reflect the market value adjustment consistent with the required treatment of the underlying assets. That is, the cash surrender value shall reflect any market value adjustments where the underlying assets are reported at market value, but it shall not reflect any market value adjustments where the underlying assets are reported at book value.


VM-22 Reserve = the upcoming minimum reserve valuation standard for non-variable annuity contracts as defined by the Valuation Manual (VM-22). It is equal to the aggregate reserve as defined in Section 3.A. The aggregate reserve for contracts falling within the scope of these requirements shall equal the stochastic reserve (following the requirements of Section 4) plus the additional standard projection amount (following the requirements of Section 6) less any applicable pretax interest maintenance reserve (PIMR) for all contracts not valued under applicable requirements in VM-A and VM-C the Alternative Methodology (Section 7), plus the reserve for any contracts determined using the Alternative Methodology valued under applicable requirements in VM-A and VM-C (following the requirements of Section 7).

### Reserves - Detail Segment

FIA = Fixed Indexed Annuity as defined in Section 1.D. An annuity with an account value where the contract holder has the option for a portion or all of the account value to grow at a rate linked to an external index, typically with guaranteed principal.

FA = Fixed Annuity: Flexible Premium Deferred Annuity (FPDA), Multiple Year Guaranteed Annuity (MYGA) and Single Premium Deferred Annuity (SPDA), all as defined in Section 1.D. 

FPDA = An annuity with an account value established with a premium amount but allows for additional deposits to be paid into the annuity over time, resulting in an increase to the account value. The contract also has a guaranteed interest rate during the accumulation phase and has guaranteed mortality and interest rates applicable at the time of conversion to the payout phase. 

MYGA = A type of fixed annuity that provides a pre-determined and contractually guaranteed interest rate for specified periods of time, after which there is typically an annual reset or renewal of a multipleyear guarantee period. 

SPDA = An annuity with an account value established with a single premium amount that grows with a guaranteed interest rate during the accumulation phase and has guaranteed mortality and interest rates applicable at the time of conversion to the payout phase. May also include cases where the premium is accepted for a limited amount of time early in the contract life, such as only in the first duration.

SPIA = Single Premium Immediate Annuity as defined in Section 1.D. An annuity purchased with a single premium amount which guarantees a periodic payment for the life of the annuitant or a term certain and payments begin within one year after (or from) the issue date.

PRT = Pension Risk Transfer Annuity as defined in Section 1.D. An annuity, typically a group contract or reinsurance agreement, issued by an insurance company providing periodic payments to annuitants receiving immediate or deferred benefits from one or more retirement plans. Typically, the insurance company holds the assets supporting the benefits, which may be held in the general or separate account, and retains not only longevity risk but also asset risks (e.g., credit risk and reinvestment risk).

DIA = Deferred Income Annuity as defined in Section 1.D. An annuity which guarantees a periodic payment for the life of the annuitant or a term certain and payments begin one year or later after (or from) the issue date if the contract holder survives to a predetermined future age.

SSC = Structured Settlement Contract as defined in Section 1.D. A contract that provides periodic benefits and is purchased with a single premium amount stemming from various types of claims pertaining to court settlements
or out-of-court settlements from tort actions arising from accidents, medical malpractice, and other causes. Adverse mortality is typically expected for these contracts.

### Type

- Base (Non-GLB) = contracts without guaranteed living benefits

- GLB - All $=$ GLB - SL + GLB $-J L=$ contracts with guaranteed living benefits, both single and joint life

- $G L B-S L=$ contracts with guaranteed living benefits that do not have a joint life option

- GLB - JL = contracts with guaranteed living benefits that have a joint life option

Add additional categories for material benefits.

For each Segment/Type category, the calculations below should be performed only across the policies in that specific category.

Total Account Value = represents the current value of the contract, and it includes both the fixed account value, and any index account values, as applicable. It is generally equal to the premium paid net of any premium taxes minus any gross withdrawals, plus any earned interest credited by the fixed account and any index accounts. It is the contract value prior to application of surrender charges or market value adjustment. For GLB riders, this will be the Account Value of the base contract. For SPIAs, or other products that offer no surrender benefits, no value is expected.

Fixed Account = an option under the contract funded by the general account of the company offering guaranteed interest rates. Not an explicit field.

Index Account = an option under the contract funded by the general account of the company offering crediting of earnings at specified times based upon the performance of an index. Not an explicit field.

Fixed Account Value $=$ the account value of the fixed account.

Cash Surrender Value - See Reserves Summary above

Market Value Adjustment (MVA) = an adjustment paid at the time of a withdrawal or surrender based on, typically, interest rates or index returns. It can be positive (increasing the value of a withdrawal/surrender) or negative.

Policies In Force $=$ the total number of policies in force as of the valuation date

CARVM Reserve - See Reserves Summary above for definition

VM-22 Reserve - See Reserves Summary above for definition

Average Years In Force $=$ the average policy duration at the valuation date across all policies in force within the category as of the valuation date

Average Issue Age = the average issue age across all policies in force within the category as of the valuation date

Average Attained Age = the average attained age as of the valuation date across all policies in force within the category as of the valuation date

\% Female = the percent of single policies, female, among all the policies in force as of the valuation date

$\% \boldsymbol{J L}=$ the percent of joint-life policies among all the policies in force as of the valuation date

Income Base (should this be average?) = the total benefit base as of valuation date for policies with a guaranteed living benefit in force as of valuation date, where

Benefit Base = the amount used to calculate the maximum lifetime income benefit payments for policies with a guaranteed living benefit rider

Average In-The-Moneyness (ITM-ness) = the average ITM-ness as of the valuation date for all policies with a guaranteed living benefit rider in force as of the valuation date, where ITM-ness is defined as either (please note the method used): Benefit Base/AV - 1 or PV(GLWB)/AV-1.

\% Contracts Receiving Withdrawals/Payouts = percent of policies with a living benefit rider that took a withdrawal under the rider in the past 12 months.

Weighted Average Withdrawal/Payout Amt = the average income as of the valuation date across all policies with a living benefit rider that are in income phase as of the valuation date, weighted by the benefit base and expressed as an amount.

Weighted Average Credited Rate / Option Budget = the weighted average across all fixed account credited rates and hedge budgets as of the valuation date across all policies in force as of the valuation date using total account value as weight. If a policy has both a fixed account and/or one or more index account, first calculate the Weighted Average Credited Rate / Option Budget for that policy using the fixed account value and/or each index account value as weights, then use this calculated value and the total account value in the weighted average across all policies.

### Reserves - Detail Stoch.

CTExx = Conditional Tail Expectation is equal to the numerical average of the ( $100-\mathrm{xx}$ ) percent worst values of a set of values.

CTExx Amount = is the CTExx of the Scenario Reserve across all scenarios following the requirements of Section 4 Median Amount = is the median Scenario Reserve across all scenarios following the requirements of Section 4 

CTExx APV Benefits \& Expense = for each scenario that comprises the CTExx Amount, the average of each's scenario's greatest present value of benefits and expenses that are part of the CTExx Amount calculation above CTE xx 

APV Premiums, etc. = average of the present value of premiums that are part of the CTExx Amount calculation above

Asset Balance $=$ starting asset amount

### Capital

The following terms are defined in the NAIC Life Risk-Based Capital (RBC) formula instructions under LR027, section Cash Flow Modeling for C-3 RBC Requirements for Variable Annuities and Similar Products:

Macro Tax Adjustment (MTA) = If using the MTA, the modeled cash flows will ignore the effect of Federal Income Tax. As a result, for each individual scenario, the numerical value of the scenario reserve used in this calculation should be identical to that for the same scenario in the Aggregate Reserve calculation under VM-22. Federal Income Tax is reflected later in the formula.

Specific Tax Recognition (STR) = If using STR, CTE After-Tax (98) (CTEAT (98)) may be calculated using an approach in which the effect of Federal Income Tax is reflected in the projection of Accumulated Deficiencies, as defined in Section 4 of VM-22, when calculating the Scenario Reserve for each scenario. To reflect the effect of Federal Income Tax, the company should find a reasonable and consistent basis for approximating the evolution of tax reserves in the projection, taking into account restrictions around the size of the tax reserves (e.g., that tax reserve must equal or exceed the cash surrender value for a given contract). The Accumulated Deficiency at the end of each projection year should also be discounted at a rate that reflects the projected after-tax discount rates in that year. In addition, the company should add the Tax Adjustment as described below to the calculated CTEAT (98) value.

Additional Standard Projection Amount (ASPA) = is calculated using the methodology outlined in Section 6 of VM22.

OLD Factor-Based Calculation (enter after-tax amounts) = Lines 2-32 of the NAIC RBC instructions under LR027.

- For company results, use line 32 (but enter an after-tax amount)
- For individual product results, use the individual lines 2-31, as appropriate (after-tax)

OLD C3P1 (enter after tax amounts) = C-3 RBC Cash Flow Testing Interest Rate Risk as defined in the NAIC RBC instructions under LRO27.

- For company results, use line 33 (but enter an after-tax amount)
- For individual product results, redo the calculation from line 33 assuming that particular product is the only product subject to C-3 RBC cash flow testing, so there is no aggregation benefit with other products (enter an after-tax amount)


# Implementation Considerations For VA Market Risk Benefits

https://sections.soa.org/publication/?m=59605&i=614324&view=articleBrowser&article_id=3465172

Dylan Strother, John Adduci, Janelle Kern  
September 2019
Editor’s note: The views expressed in this article are those of the authors and do not necessarily reflect the views of the authors’ firms.

In August 2018, the Financial Accounting Standards Board (FASB) introduced a new standard (ASU 2018-12) that made “targeted improvements” to the accounting for long-duration insurance contracts. The new standard changed the accounting for the future policyholder benefits liability and the amortization of deferred acquisition costs, established a new accounting classification and measurement for certain insurance benefits now referred to as market risk benefits (MRBs), and expanded the disclosure requirements associated with financial statements.

This article will focus on what companies need to know about MRBs and important implementation considerations when complying with the new standard.


## WHAT IS AN MRB?
FASB defines an MRB as a benefit in addition to the account balance that protects a policyholder from “other than nominal capital market risk” and exposes the insurance company to “other than nominal capital market risk” (ASU 944-40-25-25C).

Generally, guaranteed minimum benefits (GMxBs) on variable, indexed and fixed annuities are considered MRBs under the new standards, if the capital market risk is “other than nominal.” Annuitization guarantees on deferred annuities also may be considered MRBs.

Common features that are not in scope are the death benefits that exist on life insurance products, such as the death benefit on a variable universal life contract. Also out of MRB scope is any amount that “credits” the account value, such as a guaranteed minimum credited rate or the index credits on a fixed indexed annuity. While the index credits on a fixed indexed annuity would still be considered an embedded derivative, the feature would not be considered an MRB, since it is a crediting mechanism to the account value.

One challenge in identifying an MRB is the assessment of “other than nominal capital market risk,” which includes a moderate amount of judgment. The ASU states that a risk could be nominal if it has a small chance or “remote probability of occurring.” Additionally, the Update provides that the risk is other than nominal if “the benefit would vary by more than an insignificant amount in response to capital market volatility” (ASU 944-40-25-25D-c).

The assessment of “other than nominal capital market risk” occurs at contract inception based on the economic environment at that time. The same guarantee could be an MRB in certain economic environments but not in others. This is true for in-force at transition as well, since the assessment (and the calculation) is performed on a retrospective basis. In performing this assessment, the actuary would likely want to look at the risk over a range of probable capital market scenarios to determine whether the benefit amount in excess of account value would vary by more than an “insignificant amount.” Note that the new standard focuses on the risk being other than nominal, not the expected value of the benefit that would incorporate the utilization of the benefit or the likelihood of exercise. Therefore, utilization assumptions should not be used in the assessment of other than nominal risk. It is possible for a benefit feature that has other than nominal capital market risk to be classified as an MRB but for the fair value of the benefit to be immaterial initially due to the lack of assumed utilization. The fair value of the MRB could become material at a later date based on updated assumptions.


## METHODOLOGY CONSIDERATIONS
Once the scope has been decided, MRBs should follow fair value accounting. FASB requires that a contract with multiple MRBs should be valued together as a compound MRB (ASU 944- 40-30-19D). An example of a compound MRB would be a variable annuity with a guaranteed minimum living benefit and a guaranteed minimum death benefit.

Two methods of calculating the fair value are mentioned in the new standard: a non-option method and an option method. This article discusses the non-option method, which is commonly used by variable annuity carriers. 

The non-option method generally calculates an “attributed fee” such that the MRB value is zero at inception using present value of benefits minus present value of ascribed fees. The attributed ee method is the most common for fair valuing certain GMxBs under current GAAP for many variable annuity carriers.

In addition to the in-force file with policy level information, the following other inputs are needed for valuation:
- Risk-neutral interest and equity scenarios
- Own credit risk
- Policyholder behavior assumptions
- Risk margins

Risk-neutral scenarios are commonly used by market participants to fair value capital market risk. Fair value calculations performed over stochastic economic scenarios may use scenario-specific, stochastic, risk-neutral interest rates for the discounting of benefits and fees. In such cases, equity and interest scenarios should be correlated to give meaningful results. Other dynamic assumptions connected to economic scenarios should be reviewed and validated if stochastic scenarios were not utilized under the prior reserve method.

For fair value calculations, a company’s own credit spread is a component of instrument-specific credit risk. ASU 2018-12 requires that changes in the liability due to changes in instrument- specific credit risk be recognized below the line in other comprehensive income. Therefore, instrument-specific credit risk needs to be an explicit component of the discount rate so this measurement can be performed.

Policyholder behavior such as lapse, partial withdrawal and benefit utilization needs to be modeled across scenarios. These assumptions can be static, if not dependent on economic scenarios, or dynamic. The transition from best estimate to risk-neutral scenarios, when combined with dynamic policyholder behavior assumptions, can result in unintuitive results. It is good practice to establish a procedure to validate results and verify that there are no unintended consequences.

Risk margins are adjustments to account for uncertainty in cash flows and reflect assumptions that market participants would use to price the benefit. Many capital market assumptions are observable and do not require a risk margin. However, policyholder behavior assumptions are unobservable, so a risk margin is generally applied. A common way to reflect a risk margin is to explicitly adjust assumption parameters.

The non-option market risk benefit liability is calculated as follows:
1. Step 1: Project all excess benefits and contract fees across each riskneutral scenario.
2. Step 2: Calculate the present value (PV) of excess benefits and contract fees in each scenario. The present value is determined by discounting back to the valuation date at the risk-neutral interest rate plus instrument-specific credit risk.
3. Step 3: Average the present value of excess benefits and contract fees across all scenarios.
4. Step 4: For newly issued policies, calculate the attributed fee percentage (AF%):

AF% = min (100%, Average PV of excess benefits / Average PV of associated fees)

This formula produces zero gain or loss at issue as long as the AF% is not capped at 100 percent. If contract fees are not enough to cover the MRB benefits, a loss could occur at issue. The AF% is locked in at issue and used at all future valuation dates.

5. Step 5: Calculate the market risk benefit (MRB) balance using the AF% locked in at issue and the following formula:
MRB(t) = (Average PV of excess benefits) − AF% × (Average PV of associated fees).

Policyholder behavior such as lapse, partial withdrawal and
benefit utilization needs to be modeled across scenarios.


## OPERATIONAL CONSIDERATIONS
Once a methodology is determined, there are some operational implementation considerations,including building a process to support disclosure requirements and applying the guidance retroactively.

The disclosure requirements (ASU 944-40-50-7B), among other items, include aggregating the MRBs with similar characteristics into categories to present a disaggregated and detailed roll forward of each category’s reserves from the beginning of the reporting period to the end. This type of analysis often requires many successive layered valuation runs to quantify the reserve movements due to changes in calculation inputs, such as changes in economic environment or actuarial assumptions. ASU 944-40-55-13K lists items that may be included in such an analysis. Additionally, ASU 944-40-50-7B lists certain items that are required in the disclosures, such as net amount at risk and weighted attained age. Actuaries should be working with their accounting counterparts to understand the level of disaggregation desired internally versus the level desired to be disclosed externally. Fair value disclosure requirements (ASU 820-10-50) should be considered as well in identifying the roll forward components, so that both requirements will be satisfied in a single disclosure.

Companies currently reporting fair value reserves for these benefits can leverage their current fair value disclosure. Companies that accounted for only riders under SOP 03-1 will likely require significant changes to their existing attribution process. In both cases, valuation, modeling, accounting and IT will need to collaborate to set requirements for disclosures. Analysis should be performed to determine whether the current modeling platform and IT infrastructure can support the anticipated runs and level of detail required. Companies may need to increase computing power to meet financial reporting close timelines.

Much of the operational challenge in implementing the new calculation regime for MRBs will be related to meeting the retrospective transition adjustment. As of the transition date, the difference between the fair value and carrying value for an MRB is recognized as an adjustment to retained earnings. The cumulative effect of changes in instrument-specific credit risk between contract issuance and the transition date is recognized as an adjustment to accumulated other
comprehensive income (AOCI).

The attributable fee percentage and AOCI adjustment require assumptions and calculations as of contract issuance (or acquisition). This likely means a company will need to resurrect models from the past, retrofit current models to represent the past or use a practical expedient.

Resurrecting a model from the past may seem like the best path at first. However, for most companies, this option is unrealistic, unless they are going only a few years back. Many blocks of business containing MRBs have been acquired over the years. In addition, the increased complexity of benefits and guarantees on equity-based annuities and extra attention around model governance for these products has resulted in many companies converting to new software. Simply pulling the model off the shelf and rerunning it may not be a realistic option.

Retrofitting a current model to represent an older model is another option that has its own set of challenges. Policyholder data as of issuance are required to calculate the attributable fee percentage, but due to data retention policies and changes in modeling platforms, obtaining and using the data is challenging. A company may retrieve old data extracts and adjust the data to be compatible with current models, roll back elements of the current in-force data to mimic at-issue data, or create pricing cells that are representative of the company’s assumed sales. Assumptions as of the policy issuance are also required. These assumptions may not be available for older vintages, which will require the company to use judgment and hindsight. When the assumption documentation does exist, the current model will have to be updated to use the retrieved assumptions, and the structure of legacy assumptions may no longer be supported.

Finally, a company may be able to use a practical expedient to comply with transition requirements (such as the ratio approach presented in “Transition Expedient for Market Risk Benefits Under GAAP Targeted Improvements” in the December 2018 issue of The Financial Reporter). If the company plans to use practical expedients, it is worthwhile to have discussions with auditors to ensure there is an understanding of the acceptable circumstances and documentation requirements of using a practical expedient. Simply pulling the model off the shelf and rerunning it may not be a realistic option.


## CONCLUSION
There are a number of challenges associated with ASU 2018- 12 related to the measurement of market risk benefits. Setting new accounting policies and changing infrastructure will take time and resources. Each company needs to review the facts and circumstances of its own situation to determine how difficult the implementation efforts will be.

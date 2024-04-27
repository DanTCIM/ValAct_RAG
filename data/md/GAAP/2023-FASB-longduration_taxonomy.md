GAAP Financial Reporting Taxonomy and SEC Reporting Taxonomy (collectively referred to as the "GAAP Taxonomy") Implementation Guide Series

The GAAP Taxonomy Implementation Guide is not authoritative; rather, it is a document that communicates how the GAAP Financial Reporting Taxonomy (GRT) and the SEC Reporting Taxonomy (SRT) (collectively referred to as the "GAAP Taxonomy" are designed. It also provides other information to help a user of the GAAP Taxonomy understand how elements and relationships are structured.

Copyright (C) 2023 by Financial Accounting Foundation. All rights reserved. Content copyrighted by Financial Accounting Foundation may not be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of the Financial Accounting Foundation. Financial Accounting Foundation claims no copyright in any portion hereof that constitutes a work of the United States Government.

## GAAP Taxonomy Implementation Guide on Insurance-Long-Duration Contracts

## Overview

The purpose of this GAAP Taxonomy Implementation Guide (Guide) is to demonstrate the modeling for disclosures related to long-duration insurance contracts. These examples are not intended to encompass all of the potential modeling configurations or to dictate the appearance and structure of an entity's extension taxonomy or its financial statements. The examples are provided to help users of the GAAP Financial Reporting Taxonomy and the SEC Reporting Taxonomy (collectively referred to as the "GAAP Taxonomy") understand how the modeling for disclosures of long-duration insurance contracts in FASB Accounting Standards Codification ${ }^{\circledR}$ Topic 944 is structured within the Taxonomy. The examples are based on the assumption that an entity meets the criteria for reporting disclosures of long-duration insurance contracts under Generally Accepted Accounting Principles (GAAP) and/or U.S. Securities and Exchange Commission (SEC) authoritative literature. In addition, the reported line items within the examples do not include all reporting requirements and represent only partial disclosures and statements for illustrative purposes.

While constituents may find the information in the Guide useful, users looking for guidance to conform to SEC eXtensible Business Reporting Language (XBRL) filing requirements should look to the SEC EDGAR Filer Manual and other information provided on the SEC's website at www.sec.gov/structureddata.

This Guide focuses on detail tagging only (Level 4); it does not include any elements for text blocks, policy text blocks, and table text blocks (Levels 1 through 3).

Two sections are included in this Guide:

- Section 1: Overview of Modeling: This section provides an overview of the modeling for reporting disclosures of long-duration insurance contracts.
- Section 2: Examples of Modeling: This section includes examples of the modeling for reporting disclosures of long-duration insurance contracts.


## - Deferred Acquisition Costs

- Example 1-Disclosure of Information about Deferred Acquisition Costs
- Liability for Future Policy Benefits
- Example 2a-Disclosure of Information about the Liability for Future Policy Benefits
- Example $2 b-$ Reconciliation of Liability for Future Policy Benefits to the

Consolidated Statement of Financial Position

- Example 2c-Disclosure of Ending Balance-Undiscounted Expected Future Benefits and the Discounted and Undiscounted Expected Future Gross Premiums
- Example 2d-Disclosure of Gross Premium and Interest Expense
- Example 2e-Disclosure of Weighted-Average Interest Rate
- Example 3a-Disclosure of Information about the Liability for Policyholders' Account Balances
- Example 3b-Disclosure of the Balances of and Changes in Policyholders' Account Balances
- Example 3c-Reconciliation of Policyholders' Account Balances to the Policyholders' Account Balances' Liability
- Market Risk Benefits
- Example 4a-Disclosure of the Balances of and Changes in Market Risk Benefits
- Example 4b-Reconciliation of Market Risk Benefits by Asset and Liability Positions
- Separate Account Liabilities
- Example 5a-Disclosure of the Balances of and Changes in Separate Account Liability
- Example 5b-Reconciliation of Separate Account Liability
- Transition Disclosures
- Example 6a-Statement of Stockholders' Equity with Transition Adjustments on Initial Application of the New Guidance
- Example 6b-Disclosure of Reconciliation of Liability for Future Policy Benefits with Incremental Effects of Modified Retrospective Transition Method under Retrospective Transition Method on Initial Application of the New Guidance


## General Information

(1) A legend for dimensions and domain members has been provided to associate with facts contained in the notes to the financial statements. Extension elements are coded using "Ex." Legends specific to the examples are provided in Figure x. 2 of each example.

| Coding | Standard Label | Element Name |
| :---: | :---: | :---: |
| A1 | Product and Service [Axis] | ProductOrServiceAxis |
|  | Product and Service [Domain] | ProductsAndServicesDomain |
| M1 | Term Life Insurance [Member] | TermLifeInsuranceMember |
| M2 | Whole Life Insurance [Member] | WholeLifeInsuranceMember |
| M3 | Universal Life [Member] | UniversalLifeMember |
| M4 | Fixed Annuity [Member] | FixedAnnuityMember |
| M5 | Variable Annuity [Member] | VariableAnnuityMember |
| M6 | Long-Duration Insurance, Other [Member] | OtherLongdurationInsuranceProductLineMember |
| M7 | Variable Universal Life [Member] | VariableUniversalLifeMember |
| M8 | Indexed Annuity [Member] | IndexedAnnuityMember |
| A2 | Statistical Measurement [Axis] | RangeAxis |
|  | Statistical Measurement [Domain] | RangeMember |
| M9 | Minimum [Member] | MinimumMember |
| M10 | Maximum [Member] | MaximumMember |
| A3 | Policyholder Account Balance, Guaranteed <br> Minimum Crediting Rate Range [Axis] | PolicyholderAccountBalanceGuaranteedMini <br> mumCreditingRateRangeAxis |
|  | Policyholder Account Balance, Guaranteed <br> Minimum Crediting Rate Range [Domain] | PolicyholderAccountBalanceGuaranteedMinimumC <br> reditingRateRangeDomain |
|  | Policyholder Account Balance, Guaranteed <br> Minimum Crediting Rate, Range from 0200 to <br> 0299 [Member] | PolicyholderAccountBalanceGuaranteedMinimum <br> CreditingRateRangeFromo200To0299Member |
| M12 | Policyholder Account Balance, Guaranteed <br> Minimum Crediting Rate, Range from o300 to <br> O399 [Member] | PolicyholderAccountBalanceGuaranteedMinimum <br> CreditingRateRangeFromo30oToo399Member |
| M13 | Policyholder Account Balance, Guaranteed <br> Minimum Crediting Rate, Range from 0400 and <br> Greater [Member] | PolicyholderAccountBalanceGuaranteedMinimum <br> CreditingRateRangeFromo40oAndGreaterMembe <br> r |
| A4 | Policyholder Account Balance, above <br> Guaranteed Minimum Crediting Rate [Axis] | PolicyholderAccountBalanceAboveGuaranteed <br> MinimumCreditingRateAxis |
|  | Policyholder Account Balance, above Guaranteed <br> Minimum Crediting Rate [Domain] | PolicyholderAccountBalanceAboveGuaranteedMini <br> mumCreditingRateDomain |
| M14 | Policyholder Account Balance, at Guaranteed <br> Minimum Crediting Rate [Member] | PolicyholderAccountBalanceAtGuaranteedMinimu <br> mCreditingRateMember |
| M15 | Policyholder Account Balance, above Guaranteed <br> Minimum Crediting Rate, Range from ooo1 to <br> o050 [Member] | PolicyholderAccountBalanceAboveGuaranteedMini <br> mumCreditingRateRangeFromooo1Tooo5oMemb <br> er |
| M16 | Policyholder Account Balance, above Guaranteed <br> Minimum Crediting Rate, Range from o051 to <br> 0150 [Member] | PolicyholderAccountBalanceAboveGuaranteedMini <br> mumCreditingRateRangeFromoo51Too150Membe <br> r |
| M17 | Policyholder Account Balance, above Guaranteed <br> Minimum Crediting Rate, Range from 0151 and <br> Greater [Member] | PolicyholderAccountBalanceAboveGuaranteedMini <br> mumCreditingRateRangeFromo151AndGreaterMe <br> mber |

## (Continues)

| Coding | Standard Label | Element Name |
| :---: | :---: | :---: |
| A5 | Equity Components [Axis] | StatementEquityComponentsAxis |
|  | Equity Component [Domain] | EquityComponentDomain |
| M18 | AOCI Attributable to Parent [Member] | AccumulatedOtherComprehensiveIncomeMember |
| M19 | Common Stock [Member] | CommonStockMember |
| M20 | Additional Paid-in Capital [Member] | AdditionalPaidInCapitalMember |
| M21 | Retained Earnings [Member] | RetainedEarningsMember |
| M22 | Noncontrolling Interest [Member] | NoncontrollingInterestMember |
|  |  |  |
| A6 | Revision of Prior Period [Axis] | RestatementAxis |
|  | Revision of Prior Period [Domain] | RestatementDomain |
| M23 | Previously Reported [Member] | ScenarioPreviouslyReportedMember |
|  | Revision of Prior Period, Accounting Standards | RevisionOfPriorPeriodAccountingStandardsUpdat |
| M24 | Update, Adjustment [Member] | eAdjustmentMember |
|  | Effect of Retrospective Application of Accounting | EffectOfRetrospectiveApplicationOfAccountingSt |
| M25 | Standards Update 2018-12 [Member] | andardsUpdate201812Member |
|  | Effect of Modified Retrospective Application | EffectOfModifiedRetrospectiveApplicationAccou |
| M26 | Accounting Standards Update 2018-12 [Member] | ntingStandardsUpdate201812Member |

## (Continued)

(2) Elements that have an instant period type and elements that have a duration period type are indicated as such in Figure x. 2 of each example. Instant elements have a single date context (such as December 31, 20XX) and duration elements have a starting and ending date as their context (such as January 1 to December 31, 20XX).

(3) The XBRL report view (Figure $x .3$ in each example) does not include all information that may appear in an entity's instance document. The XBRL report view is provided for illustrative purposes only.

(4) For elements contained in the GAAP Taxonomy, the standard label is as it appears in the Taxonomy. For extension elements, the standard label corresponds to the element name. For information about structuring extension elements, refer to the SEC EDGAR Filer Manual.

(5) Values reported in XBRL are generally entered as positive, with the exception of certain concepts such as net income (loss) or gain (loss).

(6) Preferred labels (Figure x. 3 in each example) are the labels created and used by the entity to show the line item captions in its financial statements.

(7) Additional information for values reported using extensible enumerations can be found in the GAAP Taxonomy Implementation Guide, Extensible Enumerations: A Guide for Preparers.

## Section 1: Overview of Modeling

In modeling the new disclosure requirements within the Taxonomy, this Guide illustrates dimensional modeling that includes the use of "Statistical Measurement [Axis]" (A2) for a range of values. Specifically, in Example 3a, the "Minimum [Member]" (M9) has been used to convey the values for the start of the two ranges and the "Maximum [Member]" (M10) to convey the values for the end of the two ranges.

Additionally, this Guide illustrates dimensional modeling with the "Product and Service

[Axis]" (A1) because the information in the disclosures are disaggregated by more than one product line. If the information in the disclosures are not disaggregated (i.e., there is one product line or one segment provided), then extensible enumeration elements are intended to be used. For instance, if Example 3a included information in the disclosure about the policyholders' account balances for one product or one segment, then the "Policyholder Account Balance, Product and Service [Extensible Enumeration]" element or "Policyholder Account Balance, Segment [Extensible Enumeration]" element are intended to be used for tagging and not the "Product and Service [Axis]" (A1) or "Segments [Axis]."

## Section 2: Examples of Modeling

## Example 1-Disclosure of Information about Deferred Acquisition Costs

This example illustrates the modeling for disclosures of the beginning to the ending balance of unamortized deferred acquisition costs in tabular form.

<img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-09.jpg?height=949&width=1458&top_left_y=607&top_left_x=325" alt="image" style="width:100%;height:auto;">

## Figure 1.1

The legend for the elements used to tag these facts follows:

|  | Standard Label | Balance Type | Period Type | Element Name |
| :---: | :---: | :---: | :---: | :---: |
| A1 | Product and Service [Axis] |  | Duration | ProductOrServiceAxis |
|  | Product and Service [Domain] |  | Duration | ProductsAndServicesDomain |
| M2 | Whole Life Insurance [Member] |  | Duration | WholeLifeInsuranceMember |
| M3 | Universal Life [Member] |  | Duration | UniversalLifeMember |
| M7 | Variable Universal Life [Member] |  | Duration | VariableUniversalLifeMember |
| L1 | Deferred Policy Acquisition Cost | Debit | Instant | DeferredPolicyAcquisitionCosts |
| $\mathbf{L 2}$ | Deferred Policy Acquisition Cost, Capitalization | Debit | Duration | DeferredPolicyAcquisitionCostsAdditions |
| $\mathbf{L} 3$ | Deferred Policy Acquisition Costs, Amortization Expense | Debit | Duration | DeferredPolicyAcquisitionCostAmortizationExpense |
| $\mathbf{L 4}$ | Deferred Policy Acquisition Cost, Experience Adjustment | Debit | Duration | DeferredPolicyAcquisitionCostExperienceAdjustment |

## Figure 1.2

The XBRL report view created using the modeling structure is provided here:

| Standard Label |  | Preferred Label |  |  |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  | $20 X_{3}$ |  |  |  | $20 X 2$ |  |  |  |
|  | Product and Service [Axis] <br> A1 |  | Whole Life <br> Insurance <br>  <br> M2 | Universal <br> Life <br> M3 $_{3}$ | Variable <br> Universal <br> Life <br>  <br> M7 | Report- <br> wide <br> Value | Whole Life <br> Insurance <br>  <br> M2 | Universal <br> Life <br> M3 $_{3}$ | Variable <br> Universal <br> Life <br>  <br> M7 $_{7}$ | Report- <br> wide <br> Value |
|  | Deferred Policy Acquisition Cost, <br> Capitalization | Deferred acquisition cost, Capitalizations | 1870000 | 1550000 | 4100000 | 7520000 | 4800000 | 4000000 | 10560000 | 19360000 |
| כ | Deferred Policy Acquisition Costs, <br> Amortization Expense | Deferred acquisition cost, Amortization <br> expense | 670000 | 555000 | 1470000 | 2695000 | 480000 | 400000 | 1060000 | 1940000 |
|  | Deferred Policy Acquisition Cost, <br> Experience Adjustment | Deferred acquisition cost, Experience <br> adjustment | 150000 | 250000 | 900000 | 1300000 | 275000 | 200000 | 500000 | 975000 |
|  | Deferred Policy Acquisition Cost | Deferred acquisition cost, Balance, end of <br> year | 9095000 | 6645000 | 15230000 | 30970000 | 8045000 | 5900000 | 13500000 | 27445000 |

Figure 1.3

## Notes:

- The modeling for the disclosures related to deferred sales inducements would be similar to the modeling in this example with the use of the same dimensions; however, the deferred sales inducement cost line items (e.g., "Deferred Sale Inducement Cost") would be used in place of the deferred policy acquisition costs line items.
- The XBRL report view represents the date context for the years ended December $31,20 X_{3}$ and 20X2, and at December 31, $20 \mathrm{X}_{3}$ and 20X2, respectively; therefore, the beginning balance for the "Deferred Policy Acquisition Cost" (L1) element for the period ending December $31,20 \mathrm{X} 2$ is not presented because it would appear in a separate date context.


## Example 2a-Disclosure of Information about the Liability for Future Policy Benefits

This example illustrates the modeling for the information that an insurance entity with two long-duration product lines (term life and whole life) discloses in its financial statements for a disaggregated tabular roll forward of the beginning to the ending balance for the liability for future policy benefits, with separate presentation for expected future net premiums and expected future benefits.

<img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-12.jpg?height=1707&width=1612&top_left_y=735&top_left_x=251" alt="image" style="width:100%;height:auto;">

### Figure 2a. 1

The legend for the elements used to tag these facts follows:

|  | Standard Label | Balance Type | Period Type | Element Name |
| :---: | :---: | :---: | :---: | :---: |
| A1 | Product and Service [Axis] |  | Duration | ProductOrServiceAxis |
|  | Product and Service [Domain] |  | Duration | ProductsAndServicesDomain |
| M1 | Term Life Insurance [Member] |  | Duration | TermLifeInsuranceMember |
| M2 | Whole Life Insurance [Member] |  | Duration | WholeLifeInsuranceMember |
| $\mathbf{L} 5$ | Liability for Future Policy Benefit, Expected Net Premium, before <br> Reinsurance, after Discount Rate Change | Debit | Instant | LiabilityForFuturePolicyBenefitExpectedNetPremiumBeforeReinsuran <br> ceAfterDiscountRateChange |
| L6 | Liability for Future Policy Benefit, Expected Net Premium, Original <br> Discount Rate, before Cash Flow and Reinsurance | Debit | Instant | LiabilityForFuturePolicyBenefitExpectedNetPremiumOriginalDiscount <br> RateBeforeCashFlowAndReinsurance |
| $\mathbf{L} 7$ | Liability for Future Policy Benefit, Expected Net Premium, Cumulative <br> Increase (Decrease) from Cash Flow Change | Debit | Instant | LiabilityForFuturePolicyBenefitExpectedNetPremiumCumulativeIncre <br> aseDecreaseFromCashFlowChange |
| L8 | Liability for Future Policy Benefit, Expected Net Premium, Cumulative <br> Increase (Decrease) of Actual Variance from Expected Experience | Debit | Instant | LiabilityForFuturePolicyBenefitExpectedNetPremiumCumulativeIncre <br> aseDecreaseOfActualVarianceFromExpectedExperience |
| L9 | Liability for Future Policy Benefit, Expected Net Premium, Original <br> Discount Rate, before Reinsurance, after Cash Flow Change | Debit | Instant | LiabilityForFuturePolicyBenefitExpectedNetPremiumOriginalDiscount <br> RateBeforeReinsuranceAfterCashFlowChange |
| L1o | Liability for Future Policy Benefit, Expected Net Premium, Issuance | Debit | Duration | LiabilityForFuturePolicyBenefitExpectedNetPremiumIssuance |
| L11 | Liability for Future Policy Benefit, Expected Net Premium, Interest <br> Income | Credit | Duration | LiabilityForFuturePolicyBenefitExpectedNetPremiumInterestIncome |
| L12 | Liability for Future Policy Benefit, Expected Net Premium, Net <br> Premium Collected | Debit | Duration | LiabilityForFuturePolicyBenefitExpectedNetPremiumNetPremiumColl <br> ected |
| L13 | Liability for Future Policy Benefit, Expected Net Premium, <br> Derecognition | Credit | Duration | LiabilityForFuturePolicyBenefitExpectedNetPremiumDerecognition |
| L14 | AOCI, Liability for Future Policy Benefit, Expected Net Premium, <br> before Tax | Credit | Instant | AociLiabilityForFuturePolicyBenefitExpectedNetPremiumBeforeTax |
| $\mathbf{L 1 5}$ | Liability for Future Policy Benefit, Expected Future Policy Benefit, <br> before Reinsurance, after Discount Rate Change | Credit | Instant | LiabilityForFuturePolicyBenefitExpectedFuturePolicyBenefitBeforeRei <br> nsuranceAfterDiscountRateChange |
| L16 | Liability for Future Policy Benefit, Expected Future Policy Benefit, <br> Original Discount Rate, before Cash Flow and Reinsurance | Credit | Instant | LiabilityForFuturePolicyBenefitExpectedFuturePolicyBenefitOriginalD <br> iscountRateBeforeCashFlowAndReinsurance |
| $\mathbf{L 1 7}$ | Liability for Future Policy Benefit, Expected Future Policy Benefit, <br> Cumulative Increase (Decrease) from Cash Flow Change | Credit | Instant | LiabilityForFuturePolicyBenefitExpectedFuturePolicyBenefitCumulativ <br> eIncreaseDecreaseFromCashFlowChange |
| L18 | Liability for Future Policy Benefit, Expected Future Policy Benefit, <br> Cumulative Increase (Decrease) of Actual Variance from Expected <br> Experience | Credit | Instant | LiabilityForFuturePolicyBenefitExpectedFuturePolicyBenefitCumulativ <br> eIncreaseDecreaseOfActualVarianceFromExpectedExperience |
| L19 | Liability for Future Policy Benefit, Expected Future Benefit, Original <br> Discount Rate, before Reinsurance, after Cash Flow Change | Credit | Instant | LiabilityForFuturePolicyBenefitExpectedFutureBenefitOriginalDiscoun <br> tRateBeforeReinsuranceAfterCashFlowChange |
| L2o | Liability for Future Policy Benefit, Expected Future Policy Benefit, <br> Issuance | Credit | Duration | LiabilityForFuturePolicyBenefitExpectedFuturePolicyBenefitIssuance |

### Figure 2a.2 (continues)

|  | Standard Label | Balance Type | Period Type | Element Name |
| :---: | :---: | :---: | :---: | :---: |
| L21 | Liability for Future Policy Benefit, Expected Future Policy Benefit, <br> Interest Expense | Debit | Duration | LiabilityForFuturePolicyBenefitExpectedFuturePolicyBenefitInterest <br> Expense |
| L22 | Liability for Future Policy Benefit, Expected Future Policy Benefit, <br> Benefit Payment | Credit | Duration | LiabilityForFuturePolicyBenefitsPaymentForBenefits |
| L23 | Liability for Future Policy Benefit, Expected Future Policy Benefit, <br> Derecognition | Debit | Duration | LiabilityForFuturePolicyBenefitExpectedFuturePolicyBenefitDerecog <br> nition |
| L24 | AOCI, Liability for Future Policy Benefit, Expected Future Policy <br> Benefit, before Tax | Credit | Instant | AociLiabilityForFuturePolicyBenefitExpectedFuturePolicyBenefitBefo <br> reTax |
| L25 | Liability for Future Policy Benefit, before Reinsurance | Credit | Instant | LiabilityForFuturePolicyBenefits |
| L26 | Liability for Future Policy Benefit, Reinsurance Recoverable, after <br> Allowance | Debit | Instant | LiabilityForFuturePolicyBenefitReinsuranceRecoverableAfterAllowan <br> ce |
| L27 | Liability for Future Policy Benefit, after Reinsurance | Credit | Instant | LiabilityForFuturePolicyBenefitAfterReinsurance |

### Figure 2a. 2 (continued)

The XBRL report view created using the modeling structure is provided here:

|  | Standard Label | Preferred Label |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  | 20 |  | 201 |  |
|  | Product and Service [Axis] <br> A1 |  | Term Life <br> Insurance <br>  <br> M1 | Whole Life <br> Insurance <br>  <br> M2 | Term Life <br> Insurance <br>  <br> M1 | Whole Life <br> Insurance <br>  <br> M2 |
| L7 | Liability for Future Policy Benefit, Expected Net Premium, <br> Cumulative Increase (Decrease) from Cash Flow Change | Expected net premiums, change in cash flow <br> assumptions |  |  | 13400000 | 51300000 |
| $\mathbf{L 8}$ | Liability for Future Policy Benefit, Expected Net Premium, <br> Cumulative Increase (Decrease) of Actual Variance from <br> Expected Experience | Expected net premiums, effect of actual variances <br> from expected experience |  |  | 7500000 | 10000000 |
| L9 | Liability for Future Policy Benefit, Expected Net Premium, <br> Original Discount Rate, before Reinsurance, after Cash Flow <br> Change | Expected net premiums, adjusted beginning of year <br> balance |  |  | 569300000 | 1907100000 |
| L10 | Liability for Future Policy Benefit, Expected Net Premium, <br> Issuance | Expected net premiums, issuances | 105000000 | 300000000 | 396400000 | 1420000000 |
| L11 | Liability for Future Policy Benefit, Expected Net Premium, <br> Interest Income | Expected net premiums, interest accrual | 14300000 | 60000000 | 16000000 | 71300000 |
| L12 | Liability for Future Policy Benefit, Expected Net Premium, Net <br> Premium Collected | Expected net premiums, net premiums collected | 57100000 | 142000000 | 58000000 | 150000000 |
| L13 | Liability for Future Policy Benefit, Expected Net Premium, <br> Derecognition | Expected net premiums, derecognition (lapses) | 30000000 | 25000000 | 20000000 | 15000000 |
| L6 | Liability for Future Policy Benefit, Expected Net Premium, <br> Original Discount Rate, before Cash Flow and Reinsurance | Expected net premiums, ending balance at original <br> discount rate | 601500000 | 2100100000 | 548400000 | 1845800000 |
| L14 | AOCI, Liability for Future Policy Benefit, Expected Net <br> Premium, before Tax | Expected net premiums, effect of new discount rate <br> assumption | 1500000 | 3000000 | 800000 | 1500000 |
| $\mathbf{L}_{5}$ | Liability for Future Policy Benefit, Expected Net Premium, <br> before Reinsurance, after Discount Rate Change | Expected net premiums, balance, end of year | 603000000 | 2103100000 | 549200000 | 1847300000 |
| L17 | Liability for Future Policy Benefit, Expected Future Policy <br> Benefit, Cumulative Increase (Decrease) from Cash Flow <br> Change | Expected future policy benefits, change in cash flow <br> assumptions |  |  | 18678000 | 63400000 |
| L18 | Liability for Future Policy Benefit, Expected Future Policy <br> Benefit, Cumulative Increase (Decrease) of Actual Variance <br> from Expected Experience | Expected future policy benefits, effect of actual <br> variances from expected experience |  |  | 11000000 | 21000000 |
| L19 | Liability for Future Policy Benefit, Expected Future Benefit, <br> Original Discount Rate, before Reinsurance, after Cash Flow <br> Change | Expected future policy benefits, adjusted beginning of <br> year balance |  |  | 768528000 | 2605400000 |
| L20 | Liability for Future Policy Benefit, Expected Future Policy <br> Benefit, Issuance | Expected future policy benefits, issuances | 90000000 | 300000000 | 369200000 | 1420000000 |

### Figure 2a.3 (continues)

| Standard Label |  | Preferred Label |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  | $20 X_{3}$ |  | $20 X 2$ |  |
|  | Product and Service [Axis] <br> A1 |  | Term Life <br> Insurance <br>  <br> M1 | Whole Life <br> Insurance <br>  <br> M2 | Term Life <br> Insurance <br>  <br> M1 | Whole Life <br> Insurance <br>  <br> M2 |
| L21 | Liability for Future Policy Benefit, Expected Future Policy <br> Benefit, Interest Expense | Expected future policy benefits, interest accrual | 25000000 | 95000000 | 20000000 | 88300000 |
| L22 | Liability for Future Policy Benefit, Expected Future Policy <br> Benefit, Benefit Payment | Expected future policy benefits, benefit payments | 4000000 | 4100000 | 8350000 | 8300000 |
| L23 | Liability for Future Policy Benefit, Expected Future Policy <br> Benefit, Derecognition | Expected future policy benefits, derecognition <br> (lapses) | 22750000 | 27000000 | 25000000 | 15000000 |
| L16 | Liability for Future Policy Benefit, Expected Future Policy <br> Benefit, Original Discount Rate, before Cash Flow and <br> Reinsurance | Expected future policy benefits, ending balance at <br> original discount rate | 856778000 | 2969300000 | 738850000 | 2521000000 |
| L24 | AOCI, Liability for Future Policy Benefit, Expected Future <br> Policy Benefit, before Tax | Expected future policy benefits, effect of new discount <br> rate assumption | -2000000 | -4000000 | -1250000 | -3000000 |
| L15 | Liability for Future Policy Benefit, Expected Future Policy <br> Benefit, before Reinsurance, after Discount Rate Change | Expected future policy benefits, balance, end of year | 858778000 | 2973300000 | 740100000 | 2524000000 |
| L25 | Liability for Future Policy Benefit, before Reinsurance | Net liability for future policy benefits | 255778000 | 870200000 | 190900000 | 676700000 |
| L26 | Liability for Future Policy Benefit, Reinsurance Recoverable, <br> after Allowance | Reinsurance recoverable | 10800000 | 30000000 | 5200000 | 14150000 |
| L27 | Liability for Future Policy Benefit, after Reinsurance | Net liability for future policy benefits, after <br> reinsurance recoverable | 244978000 | 840200000 | 185700000 | 662550000 |

Figure 2a. 3 (continued)

## Notes:

- The date contexts for the line items "Liability for Future Policy Benefit, Expected Net Premium, Cumulative Increase (Decrease) from Cash Flow Change" (L7), "Liability for Future Policy Benefit, Expected Net Premium, Cumulative Increase (Decrease) of Actual Variance from Expected Experience" (L8), "Liability for Future Policy Benefit, Expected Future Policy Benefit, Cumulative Increase (Decrease) from Cash Flow Change" (L17) and "Liability for Future Policy Benefit, Expected Future Policy Benefit, Cumulative Increase (Decrease) of Actual Variance from Expected Experience" (L18) for adjustments to the opening balances of present value of expected net premiums and present value of expected future policy benefits are at December 31, 20X2 and 20X1; respectively.
- The remaining line items shown in the XBRL report view represent the date context for the years ended December 31, 20X3 and 20X2 and at December 31, 20X3 and 20X2, respectively; therefore, the beginning balances for the period ending December 31, 20X2 are not presented because they would appear in a separate date context.
- The element "AOCI, Liability for Future Policy Benefit, Expected Net Premium, before Tax" (L14) is modeled from the accumulated other comprehensive income perspective. For the calculation to work with the appropriate positive and negative values, the calculation summation parent is "Liability for Future Policy Benefit, Expected Net Premium, Original Discount Rate, before Cash Flow and Reinsurance" (L6) with children of "AOCI, Liability for Future Policy Benefit, Expected Net Premium, before Tax" (L14) and "Liability for Future Policy Benefit, Expected Net Premium, before Reinsurance, after Discount Rate Change" (L5). In this example, "AOCI, Liability for Future Policy Benefit, Expected Net Premium, before Tax" (L14) is a credit to accumulated other comprehensive income and a debit to "Liability for Future Policy Benefit, Expected Future Policy Benefit, Original Discount Rate, before Cash Flow and Reinsurance" (L16) and the XBRL value will be positive because it is from the accumulated other comprehensive perspective.
- The element "AOCI, Liability for Future Policy Benefit, Expected Future Policy Benefit, before Tax" (L24) is modeled from the accumulated other comprehensive income perspective. For the calculation to work with the appropriate positive and negative values, the calculation summation parent is "Liability for Future Policy Benefit, Expected Future

Policy Benefit, Original Discount Rate, before Cash Flow and Reinsurance" (L16) with children of "AOCI, Liability for Future Policy Benefit, Expected Future Policy Benefit, before Tax" (L24 ) and "Liability for Future Policy Benefit, Expected Future Policy Benefit, before Reinsurance, after Discount Rate Change" (L15 ). In this example, "AOCI, Liability for Future Policy Benefit, Expected Future Policy Benefit, before Tax” (L24) is a debit to the accumulated other comprehensive income and a credit to "Liability for Future Policy Benefit, Expected Future Policy Benefit, Original Discount Rate, before Cash Flow and Reinsurance" (L16) and the XBRL value will be negative because it is from the accumulated other comprehensive perspective.

## Example 2b-Reconciliation of Liability for Future Policy Benefits to the Consolidated Statement of Financial Position

This example illustrates the modeling of the reconciliation of the liability for future policy benefits in the consolidated statement of financial position.

| The reconciliation of the net liability for futu <br> statement of financial position at December <br> Liability for Future Policy Benefits <br> (in thousands) |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Term Life | L25, A1:M1 | $\$$ | 255,778 | $\$$ | 190,900 |
| Whole Life | L25, A1:M2 |  | 870,200 |  | 676,700 |
| Other | L25, A1:M6 |  | 50,000 |  | 55,000 |
| Balance, End of Year | L25 | $\$$ | $1,175,978$ | $\$$ | 922,600 |

### Figure $2 b .1$

The legend for the elements used to tag these facts follows:

| Standard Label | Balance Type | Period Type | Element Name |  |
| :--- | :---: | :---: | :---: | :---: |
| A1 | Product and Service [Axis] |  | Duration | ProductOrServiceAxis |
|  | Product and Service [Domain] |  | Duration | ProductsAndServicesDomain |
| M1 | Term Life Insurance [Member] |  | Duration | TermLifeInsuranceMember |
| M2 | Whole Life Insurance [Member] | Duration | WholeLifeInsuranceMember |  |
| M6 | Long-Duration Insurance, Other [Member] | Duration | OtherLongdurationInsuranceProductLineMember |  |
|  |  |  |  |  |
| L25 | Liability for Future Policy Benefit, before Reinsurance | Credit | Instant | LiabilityForFuturePolicyBenefits |

## Figure $2 b .2$

The XBRL report view created using the modeling structure is provided here:

| Standard Label | Preferred Label |  |  |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | $20 X_{3}$ |  |  |  | $20 X 2$ |  |  |  |
| Product and Service [Axis] <br> A1 |  | Term Life <br> Insurance <br>  <br> M1 | Whole Life <br> Insurance <br>  <br> M2 | Long- <br> Duration <br> Insurance, <br> Other <br>  <br> M6 | <img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-20.jpg?height=182&width=177&top_left_y=1111&top_left_x=1626" alt="image" style="width:100%;height:auto;"> | Term Life <br> Insurance <br>  <br> M1 | Whole Life <br> Insurance <br>  <br> M2 | Long- <br> Duration <br> Insurance, <br> Other <br>  <br> M6 | Report- <br> wide Value |
| Liability for Future Policy <br> Benefit, before Reinsurance | Liability for future policy <br> benefits | 255778000 | 870200000 | 50000000 | 1175978000 | 190900000 | 676700000 | 55000000 | 922600000 |

Figure $2 b .3$

## Example 2c-Disclosure of Ending Balance-Undiscounted Expected Future Benefits and the Discounted and Undiscounted Expected Future Gross Premiums

This example illustrates the modeling for the amount of undiscounted expected future benefit payments and both discounted and undiscounted expected gross premiums.

| The amount of undiscounted expected future benefit payments and both discounted and undiscounted <br> expected gross premiums at December 31, for the years ended: |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: |
| Term Life |  |  |  |  |
| Expected future benefit payments, undiscounted | L28, A1:M1 \$ | $1,200,000$ | $\$$ | 950,000 |
| Expected future gross premiums, undiscounted | L29, A1:M1 \$ | 875,000 | $\$$ | 750,000 |
| Expected future gross premiums, discounted | L30, A1:M1 \$ | 780,000 | $\$$ | 590,000 |
| Whole Life |  |  |  |  |
| Expected future benefit payments, undiscounted | L28, A1:M2 \$ | $4,768,000$ | $\$$ | $3,200,000$ |
| Expected future gross premiums, undiscounted | L29, A1:M2 \$ | $5,550,000$ | $\$$ | 5,000,000 |
| Expected future gross premiums, discounted | L30, A1:M2 \$ | $4,950,000$ | $\$$ | $3,970,000$ |

### Figure 2c. 1

The legend for the elements used to tag these facts follows:

| A1 | Standard Label | Balance Type | Period Type | Element Name |
| :---: | :---: | :---: | :---: | :---: |
|  | Product and Service [Axis] |  | Duration | ProductOrServiceAxis |
|  | Product and Service [Domain] |  | Duration | ProductsAndServicesDomain |
| M1 | Term Life Insurance [Member] |  | Duration | TermLifeInsuranceMember |
| M2 | Whole Life Insurance [Member] |  | Duration | WholeLifeInsuranceMember |
| L28 | Liability for Future Policy Benefit, Expected Future Policy <br> Benefit, Undiscounted, before Reinsurance | Credit | Instant | LiabilityForFuturePolicyBenefitExpectedFuturePolicyBenefitUndisc <br> ountedBeforeReinsurance |
| L29 | Liability for Future Policy Benefit, Expected Future Gross <br> Premium, Undiscounted, before Reinsurance | Debit | Instant | LiabilityForFuturePolicyBenefitExpectedFutureGrossPremiumUndi <br> scountedBeforeReinsurance |
| L3o | Liability for Future Policy Benefit, Expected Future Gross <br> Premium, Discounted, before Reinsurance | Debit | Instant | LiabilityForFuturePolicyBenefitExpectedFutureGrossPremiumDisco <br> untedBeforeReinsurance |

Figure 2c. 2

The XBRL report view created using the modeling structure is provided here:

| Standard Label |  | Preferred Label |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  | $20 X_{3}$ |  | $20 X 2$ |  |
|  | Product and Service [Axis] <br> A1 |  | Term Life <br> Insurance <br>  <br> M1 | Whole Life <br> Insurance <br>  <br> M2 | Term Life <br> Insurance <br>  <br> M1 | Whole Life <br> Insurance <br>  <br> M2 |
| L28 | Liability for Future Policy Benefit, Expected Future Policy <br> Benefit, Undiscounted, before Reinsurance | Expected future benefit payments, <br> undiscounted | 1200000000 | 4768000000 | 950000000 | 3200000000 |
| L29 | Liability for Future Policy Benefit, Expected Future Gross <br> Premium, Undiscounted, before Reinsurance | Expected future gross premiums, <br> undiscounted | 875000000 | 5550000000 | 750000000 | 5000000000 |
| L3o | Liability for Future Policy Benefit, Expected Future Gross <br> Premium, Discounted, before Reinsurance | Expected future gross premiums, discounted | 780000000 | 4950000000 | 590000000 | 3970000000 |

Figure 2c. 3

## Example 2d-Disclosure of Gross Premium and Interest Expense

This example illustrates the modeling for the amount of gross premium income and interest expense recognized in the statement of operations.

| Total gross premium income and interest expense at December 31, for the years ended: |  |  |  |  |  |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| (in thousands) |  |  | $\mathbf{2 0 X 3}$ |  | $20 X 2$ |  |  |  | $20 X_{3}$ |  | $20 X 2$ |
| Term Life | L31, A1:M1 | $\$$ | 76,000 | $\$$ | 81,300 | Term Life | L32, A1:M1 | $\$$ | 10,700 | $\$$ | 4,000 |
| Whole Life | L31, A1:M2 |  | 160,000 |  | 168,000 | Whole Life | L32, A1:M2 |  | 35,000 |  | 17,000 |
| Other | L31, A1:M6 |  | 20,000 |  | 25,000 | Other | L32, A1:M6 |  | 2,000 |  | 1,000 |
| Total | L31 | $\$$ | 256,000 | $\$$ | 274,300 | Total | $\mathbf{L} 32$ | $\$$ | 47,700 | $\$$ | 22,000 |

### Figure 2d. 1

The legend for the elements used to tag these facts follows:

| Standard Label | Balance Type | Period Type |  | Element Name |
| :--- | :--- | :---: | :---: | :---: |
| A1 | Product and Service [Axis] |  | Duration | ProductOrServiceAxis |
|  | Product and Service [Domain] |  | Duration | ProductsAndServicesDomain |
| M1 | Term Life Insurance [Member] |  | Duration | TermLifeInsuranceMember |
| M2 | Whole Life Insurance [Member] |  | Duration | WholeLifeInsuranceMember |
| M6 | Long-Duration Insurance, Other [Member] |  | Duration | OtherLongdurationInsuranceProductLineMember |
|  |  |  |  |  |
| L31 | Liability for Future Policy Benefit, Gross Premium Income | Credit | Duration | LiabilityForFuturePolicyBenefitGrossPremiumIncome |
| L32 | Liability for Future Policy Benefit, Interest Expense | Debit | Duration | LiabilityForFuturePolicyBenefitInterestExpense |

Figure 2d. 2

The XBRL report view created using the modeling structure is provided here:

<img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-24.jpg?height=424&width=2501&top_left_y=1086&top_left_x=139" alt="image" style="width:100%;height:auto;">

Figure 2d.3

## Example 2e-Disclosure of Weighted-Average Interest Rate

This example illustrates the weighted-average interest rate information about the liability for future policy benefits.

| The weighted-average interest rate follows. |  |  |  |
| :---: | :---: | :---: | :---: |
| Term Life |  |  |  |
| Interest accretion rate | L33, A1:M1 | $3.65 \%$ | $3.65 \%$ |
| Current discount rate | L34, A1:M1 | $3.89 \%$ | $3.69 \%$ |
| Whole Life |  |  |  |
| Interest accretion rate | L33, A1:M2 | $5.05 \%$ | $5.05 \%$ |
| Current discount rate | L34, A1:M2 | $5.40 \%$ | $5.20 \%$ |

## Figure 2e. 1

The legend for the elements used to tag these facts follows:

|  | Standard Label | Balance Type | Period Type | Element Name |
| :---: | :---: | :---: | :---: | :---: |
| A1 | Product and Service [Axis] |  | Duration | ProductOrServiceAxis |
|  | Product and Service [Domain] |  | Duration | ProductsAndServicesDomain |
| Mi | Term Life Insurance [Member] |  | Duration | TermLifeInsuranceMember |
| M2 | Whole Life Insurance [Member] |  | Duration | WholeLifeInsuranceMember |
| L33 | Liability for Future Policy Benefit, Weighted-Average Interest <br> Accretion Rate |  | Instant | LiabilityForFuturePolicyBenefitWeightedAverageInterestAccretionR <br> ate |
| L34 | Liability for Future Policy Benefit, Current Weighted-Average Discount <br> Rate |  | Instant | LiabilityForFuturePolicyBenefitCurrentWeightedAverageDiscountR <br> ate |

## Figure 2e. 2

The XBRL report view created using the modeling structure is provided here:

<img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-26.jpg?height=372&width=2340&top_left_y=968&top_left_x=219" alt="image" style="width:100%;height:auto;">

Figure 2e. 3

## Example 3a-Disclosure of Information about the Liability for Policyholders' Account

## Balances

This example illustrates the modeling for the information of the policyholders' account balance by range of guaranteed minimum crediting rates and the related range of difference, in basis points, between rates being credited to policyholders and the respective guaranteed minimums.

<img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-27.jpg?height=1528&width=1848&top_left_y=632&top_left_x=144" alt="image" style="width:100%;height:auto;">

Figure 3a. 1 (continues)

<img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-28.jpg?height=1458&width=1870&top_left_y=239&top_left_x=125" alt="image" style="width:100%;height:auto;">

### Figure 3a. 1 (continued)

The legend for the elements used to tag these facts follows:

|  | Standard Label | Balance Type | Period Type | Element Name |
| :---: | :---: | :---: | :---: | :---: |
| A1 | Product and Service [Axis] |  | Duration | ProductOrServiceAxis |
|  | Product and Service [Domain] |  | Duration | ProductsAndServicesDomain |
| M3 | Universal Life [Member] |  | Duration | UniversalLifeMember |
| $\mathbf{M}_{4}$ | Fixed Annuity [Member] |  | Duration | FixedAnnuityMember |
| A2 | Statistical Measurement [Axis] |  | Duration | RangeAxis |
|  | Statistical Measurement [Domain] |  | Duration | RangeMember |
| M9 | Minimum [Member] |  | Duration | MinimumMember |
| M10 | Maximum [Member] |  | Duration | MaximumMember |
| A3 | Policyholder Account Balance, Guaranteed Minimum Crediting Rate Range |  | Duration | PolicyholderAccountBalanceGuaranteedMinimumCreditingRateRange <br> Axis |
|  | Policyholder Account Balance, Guaranteed Minimum Crediting Rate <br> Range [Domain] |  | Duration | PolicyholderAccountBalanceGuaranteedMinimumCreditingRateRang <br> eDomain |
| M11 | Policyholder Account Balance, Guaranteed Minimum Crediting Rate, <br> Range from 0200 to 0299 [Member] |  | Duration | PolicyholderAccountBalanceGuaranteedMinimumCreditingRateRan <br> geFromo200Too299Member |
| M12 | Policyholder Account Balance, Guaranteed Minimum Crediting Rate, <br> Range from o300 to 0399 [Member] |  | Duration | PolicyholderAccountBalanceGuaranteedMinimumCreditingRateRan <br> geFromo300Too399Member |
| M13 | Policyholder Account Balance, Guaranteed Minimum Crediting Rate, <br> Range from 0400 and Greater [Member] |  | Duration | PolicyholderAccountBalanceGuaranteedMinimumCreditingRateRan <br> geFromo400AndGreaterMember |
| A4 | Policyholder Account Balance, above Guaranteed Minimum Crediting Rate |  | Duration | PolicyholderAccountBalanceAboveGuaranteedMinimumCreditingRateA <br> xis |
|  | Policyholder Account Balance, above Guaranteed Minimum Crediting <br> Rate [Domain] |  | Duration | PolicyholderAccountBalanceAboveGuaranteedMinimumCreditingRat <br> eDomain |
| M14 | Policyholder Account Balance, at Guaranteed Minimum Crediting Rate |  | Duration | PolicyholderAccountBalanceAtGuaranteedMinimumCreditingRateM <br> ember |
| M15 | Policyholder Account Balance, above Guaranteed Minimum Crediting <br> Rate, Range from ooo1 to 0050 [Member] |  | Duration | PolicyholderAccountBalanceAboveGuaranteedMinimumCreditingRa <br> teRangeFromooo1Tooo50Member |
| M16 | Policyholder Account Balance, above Guaranteed Minimum Crediting <br> Rate, Range from oo51 to 0150 [Member] |  | Duration | PolicyholderAccountBalanceAboveGuaranteedMinimumCreditingRa <br> teRangeFromoo51Too15oMember |
| M17 | Policyholder Account Balance, above Guaranteed Minimum Crediting <br> Rate, Range from 0151 and Greater [Member] |  | Duration | PolicyholderAccountBalanceAboveGuaranteedMinimumCreditingRa <br> teRangeFromo151AndGreaterMember |
| L35 | Policyholder Account Balance | Credit | Instant | PolicyholderFunds |
| L36 | Policyholder Account Balance, Guaranteed Minimum Credit Rating |  | Instant | PolicyholderAccountBalanceGuaranteedMinimumCreditRating |
| L37 | Policyholder Account Balance, above Guaranteed Minimum Crediting <br> Rate |  | Instant | PolicyholderAccountBalanceAboveGuaranteedMinimumCreditingRat <br> e |

### Figure 3a. 2

The XBRL report view created using the modeling structure is provided here:

| Standard <br> Label | Product <br> and Service <br>  <br> A1 | Policyholder Account <br> Balance, Guaranteed <br> Minimum Crediting Rate <br> Range [Axis] <br> A3 | Policyholder Account Balance, <br> above Guaranteed Mimimum <br> Crediting Rate [Axis] <br> A4 | Statistical Measurement <br>  <br> A2 | $20 X_{3}$ |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  |  |  | Policyholder <br> Account <br> Balance <br> L35 | Policyholder Account <br> Balance, Guaranteed <br> Minimum Credit Rating <br> L36 | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate <br> L37 |
| Preferred <br> Label |  |  |  |  | Policyholder <br> account <br> balance | Policyholder account balance <br> at guaranteed minimum <br> credit rate | Policyholder account balance <br> above guaranteed minimum <br> crediting rate |
|  | Universal <br> Life <br>  <br> $\mathbf{M}_{3}$ |  |  |  | 21540000 |  |  |
|  |  |  | Policyholder Account Balance, at <br> Guaranted Minimum Crediting <br> Rate [Member] <br> M14 |  | 1650000 |  |  |
|  |  |  |  | Maximum [Member] <br> M10 |  |  | 0 |
|  |  |  |  | Minimum [Member] <br> M9 |  |  | $\mathrm{O}$ |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from ooo1 to <br> oo50 [Member] <br> M15 |  | 3675000 |  |  |
|  |  |  |  | Maximum [Member] <br> M10 |  |  | 0.0050 |
|  |  |  |  | Minimum [Member] <br> M9 |  |  | 0.0001 |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from oo51 to <br> o150 [Member] <br> M16 |  | 10500000 |  |  |
|  |  |  |  | Maximum [Member] <br> M10 |  |  | 0.0150 |
|  |  |  |  | Minimum [Member] <br> M9 |  |  | 0.0051 |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from o151 <br> and Greater [Member] <br> M17 |  | 5715000 |  |  |
|  |  |  |  | Maximum [Member] <br> M10 |  |  | nil |
|  |  |  |  | Minimum [Member] <br> M9 |  |  | 0.0151 |
|  |  | Policyholder Account <br> Balance, Guaranteed <br> Minimum Crediting Rate, <br> Range from o200 to 0299 <br>  <br> M11 |  |  | 9600000 |  |  |
|  |  |  |  | Maximum [Member] <br> M10 |  | 0.0299 |  |
|  |  |  |  | Minimum [Member] <br> M9 |  | 0.0200 |  |

Figure 3a.3 (continues)

| Standard <br> Label | Product <br> and Service <br>  <br> A1 | Policyholder Account <br> Balance, Guaranteed <br> Minimum Crediting Rate <br> Range [Axis] <br> A3 | Policyholder Account Balance, <br> above Guaranted Minimum <br> Crediting Rate [Axis] <br> A4 | Statistical Measurement <br>  <br> A2 | $20 X_{3}$ |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  |  |  | Policyholder <br> Account <br> Balance <br> L35 | Policyholder Account <br> Balance, Guaranteed <br> Minimum Credit Rating <br> L36 | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate <br> L37 |
| Preferred <br> Label |  |  |  |  | Policyholder <br> account <br> balance | Policyholder account balance <br> at guaranteed minimum <br> credit rate | Policyholder account balance <br> above guaranteed minimum <br> crediting rate |
|  | Universal <br> Life <br>  <br> M3 | Policyholder Account <br> Balance, Guaranteed <br> Minimum Crediting Rate, <br> Range from o20o to 0299 <br>  <br> M11 | Policyholder Account Balance, at <br> Guaranteed Minimum Crediting <br> Rate [Member] <br> M14 |  | 1000000 |  |  |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from ooo1 to <br> oo5o [Member] <br> M15 |  | 2000000 |  |  |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from 0051 to <br> o150 [Member] <br> M16 |  | 3100000 |  |  |
|  |  |  | Policyholder Account Balance, <br> above Guaranted Minimum <br> Crediting Rate, Range from 0151 <br> and Greater [Member] <br> M17 |  | 3500000 |  |  |
|  |  | Policyholder Account <br> Balance, Guaranteed <br> Minimum Crediting Rate, <br> Range from o300 to 0399 <br>  <br> M12 |  |  | 4365000 |  |  |
|  |  |  |  | Maximum [Member] <br> M10 |  | 0.0399 |  |
|  |  |  |  | Minimum [Member] <br> M9 |  | 0.0300 |  |
|  |  |  | Policyholder Account Balance, at <br> Guaranteed Minimum Crediting <br> Rate [Member] <br> M14 |  | 500000 |  |  |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from ooo1 to <br> oo50 [Member] <br> M15 |  | 350000 |  |  |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from o051 to <br> o15o [Member] <br> M16 |  | 3400000 |  |  |

### Figure 3a. 3 (continues)

| Standard <br> Label | Product <br> and Service <br>  <br> A1 | Policyholder Account <br> Balance, Guaranteed <br> Minimum Crediting Rate <br> Range [Axis] <br> A3 | Policyholder Account Balance, <br> above Guaranted Minimum <br> Crediting Rate [Axis] <br> A4 | Statistical Measurement <br>  <br> A2 | $20 X_{3}$ |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  |  |  | Policyholder <br> Account <br> Balance <br> L35 | Policyholder Account <br> Balance, Guaranteed <br> Minimum Credit Rating <br> L36 | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate <br> L37 |
| Preferred <br> Label |  |  |  |  | Policyholder <br> account <br> balance | Policyholder account balance <br> at guaranteed minimum <br> credit rate | Policyholder account balance <br> above guaranteed minimum <br> crediting rate |
|  | Universal <br> Life <br>  <br> $\mathbf{M}_{3}$ | Policyholder Account <br> Balance, Guaranteed <br> Minimum Crediting Rate, <br> Range from o300 to 0399 <br>  <br> M12 | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from o151 <br> and Greater [Member] <br> M17 |  | 115000 |  |  |
|  |  | Policyholder Account <br> Balance, Guaranteed <br> Minimum Crediting Rate, <br> Range from o4oo and <br> Greater [Member] <br> M13 |  |  | 7575000 |  |  |
|  |  |  |  | Maximum [Member] <br> M10 |  | nil |  |
|  |  |  |  | Minimum [Member] <br> M9 |  | 0.0400 |  |
|  |  |  | Policyholder Account Balance, at <br> Guaranteed Minimum Crediting <br> Rate [Member] <br> M14 |  | 150000 |  |  |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from ooo1 to <br> oo5o [Member] <br> M15 |  | 1325000 |  |  |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from o051 to <br> o150 [Member] <br> M16 |  | 4000000 |  |  |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from o151 <br> and Greater [Member] <br> M17 |  | 2100000 |  |  |
|  | Fixed <br> Annuity <br> $[$ Member] <br> M4 |  |  |  | 19270000 |  |  |
|  |  |  | Policyholder Account Balance, at <br> Guaranteed Minimum Crediting <br> Rate [Member] <br> M14 |  | 2910000 |  |  |
|  |  |  |  | Maximum [Member] <br> M10 |  |  | $\mathrm{O}$ |
|  |  |  |  | Minimum [Member] <br> M9 |  |  | o |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from ooo1 to <br> oo50 [Member] <br> M15 |  | 5810000 |  |  |
|  |  |  |  | Maximum [Member] <br> M10 |  |  | 0.0050 |

### Figure 3a.3 (continues)

| $\underset{\text { Label }}{\text { Standard }}$ | Product <br> and Service <br>  <br> A1 | Policyholder Account <br> Balance, Guaranteed <br> Minimum Crediting Rate <br> Range [Axis] <br> A3 | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate [Axis] <br> A4 | Statistical Measurement <br>  <br> A2 | $20 \times 3$ |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  |  |  | Policyholder <br> Account <br> Balance <br> L35 | Policyholder Account <br> Balance, Guaranteed <br> Minimum Credit Rating <br> L36 | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate <br> L37 |
| Preferred <br> Label |  |  |  |  | Policyholder <br> account <br> balance | Policyholder account balance <br> at guaranteed minimum <br> credit rate | Policyholder account balance <br> above guaranteed minimum <br> crediting rate |
|  | Fixed <br> Annuity <br>  <br> M4 | Policyholder Account <br> Balance, Guaranteed <br> Minimum Crediting Rate, <br> Range from o200 to 0299 <br>  <br> M11 | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from ooo1 to <br> oo50 [Member] <br> M15 | Minimum [Member] <br> M9 |  |  | 0.0001 |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from oo51 to <br> o150 [Member] <br> M16 |  | 5675000 |  |  |
|  |  |  |  | Maximum [Member] <br> M10 |  |  | 0.0150 |
|  |  |  |  | Minimum [Member] <br> M9 |  |  | 0.0051 |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from o151 <br> and Greater [Member] <br> M17 |  | 4875000 |  |  |
|  |  |  |  | Maximum [Member] <br> M10 |  |  | nil |
|  |  |  |  | Minimum [Member] <br> M9 |  |  | 0.0151 |
|  |  |  |  |  | 5350000 |  |  |
|  |  |  |  | Maximum [Member] <br> M10 |  | 0.0299 |  |
|  |  |  |  | Minimum [Member] <br> M9 |  | 0.0200 |  |
|  |  |  | Policyholder Account Balance, at <br> Guaranteed Minimum Crediting <br> Rate [Member] <br> M14 |  | 750000 |  |  |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from ooo1 to <br> oo50 [Member] <br> M15 |  | 1475000 |  |  |
|  |  |  | <img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-33.jpg?height=161&width=465&top_left_y=1603&top_left_x=827" alt="image" style="width:100%;height:auto;"> |  | 1350000 |  |  |

### Figure 3a.3 (continues)

| Standard <br> Label | Product <br> and Service <br>  <br> A1 | Policyholder Account <br> Balance, Guaranteed <br> Minimum Crediting Rate <br> Range [Axis] <br> A3 | Policyholder Account Balance, <br> above Guaranted Minimum <br> Crediting Rate [Axis] <br> A4 | Statistical Measurement <br>  <br> A2 | $20 X_{3}$ |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  |  |  | Policyholder <br> Account <br> Balance <br> L35 | Policyholder Account <br> Balance, Guaranteed <br> Minimum Credit Rating <br> L36 | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate <br> L37 |
| Preferred <br> Label |  |  |  |  | Policyholder <br> account <br> balance | Policyholder account balance <br> at guaranteed minimum <br> credit rate | Policyholder account balance <br> above guaranteed minimum <br> crediting rate |
|  | Fixed <br> Annuity <br> $[$ Member] <br> M4 | Policyholder Account <br> Balance, Guaranteed <br> Minimum Crediting Rate, <br> Range from o20o to 0299 <br>  <br> M11 | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from o151 <br> and Greater [Member] <br> M17 |  | 1775000 |  |  |
|  |  | Policyholder Account <br> Balance, Guaranteed <br> Minimum Crediting Rate, <br> Range from o300 to 0399 <br>  <br> M12 |  |  | 7015000 |  |  |
|  |  |  |  | Maximum [Member] <br> M10 |  | 0.0399 |  |
|  |  |  |  | Minimum [Member] <br> M9 |  | 0.0300 |  |
|  |  |  | Policyholder Account Balance, at <br> Guaranteed Minimum Crediting <br> Rate [Member] <br> M14 |  | 980000 |  |  |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from ooo1 to <br> oo5o [Member] <br> M15 |  | 2160000 |  |  |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from o051 to <br> o150 [Member] <br> M16 |  | 1875000 |  |  |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from o151 <br> and Greater [Member] <br> M17 |  | 2000000 |  |  |
|  |  | Policyholder Account <br> Balance, Guaranteed <br> Minimum Crediting Rate, <br> Range from o4oo and <br> Greater [Member] <br> M13 |  |  | 6905000 |  |  |
|  |  |  |  | Maximum [Member] <br> M10 |  | nil |  |
|  |  |  |  | Minimum [Member] <br> M9 |  | 0.0400 |  |
|  |  |  | Policyholder Account Balance, at <br> Guaranteed Minimum Crediting <br> Rate [Member] <br> M14 |  | 1180000 |  |  |

Figure 3a. 3 (continues)

| Standard <br> Label | Product <br> and Service <br>  <br> A1 | Policyholder Account <br> Balance, Guaranteed <br> Minimum Crediting Rate <br> Range [Axis] <br> A3 | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate [Axis] <br> A4 | Statistical Measurement <br>  <br> A2 | $20 X_{3}$ |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  |  |  | Policyholder <br> Account <br> Balance <br> L35 | Policyholder Account <br> Balance, Guaranteed <br> Minimum Credit Rating <br> L36 | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate <br> L37 |
| Preferred <br> Label |  |  |  |  | Policyholder <br> account <br> balance | Policyholder account balance <br> at guaranteed minimum <br> credit rate | Policyholder account balance <br> above guaranteed minimum <br> crediting rate |
|  | Fixed <br> Annuity <br> $[$ Member] <br> M4 | Policyholder Account <br> Balance, Guaranteed <br> Minimum Crediting Rate, <br> Range from o4oo and <br> Greater [Member] <br> M13 | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from ooo1 to <br> oo5o [Member] <br> M15 |  | 2175000 |  |  |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from oo51 to <br> o15o [Member] <br> M16 |  | 2450000 |  |  |
|  |  |  | Policyholder Account Balance, <br> above Guaranteed Minimum <br> Crediting Rate, Range from o151 <br> and Greater [Member] <br> M17 |  | 1100000 |  |  |

Figure 3a.3 (continued)

## Notes:

- "Policyholder Account Balance, Guaranteed Minimum Credit Rating" (L36), "Policyholder Account Balance, Guaranteed Minimum Crediting Rate Range [Axis]" (A3), and "Statistical Measurement [Axis]" (A2) are used to convey the range of the guaranteed minimum crediting rates. Utilizing the line item, the start of the range is entered in a decimal format (e.g., o.02) and is tagged with "Minimum [Member]" (M9). The related end of the range is entered in a decimal format (e.g., 0.0299) and is tagged with "Maximum [Member]" (M10).
- "Policyholder Account Balance, above Guaranteed Minimum Crediting Rate" (L37), "Policyholder Account Balance, above Guaranteed Minimum Crediting Rate [Axis]" (A4), and "Statistical Measurement [Axis]" (A2) are used to convey the range for the at or above guaranteed minimum crediting rates. Utilizing that line item, the start of the range is entered in a decimal format (e.g., o.0oo1) and is tagged with "Minimum [Member]" (M9). The related end of the range is entered as a decimal format (e.g., 0.0050) and is tagged with "Maximum [Member]" (M10).
- As an example of the dimension modeling, fact value $\$ 1,000,000$ (under Universal Life Product) is tagged with the "Policyholder Account Balance" (L35) line item and the respective "Universal Life [Member]" (M3) under the "Product and Service [Axis]" (A1). Additionally, that line item is tagged with members "Policyholder Account Balance, Guaranteed Minimum Crediting Rate, Range from 0200 to 0299 [Member]” (M11) and "Policyholder Account Balance, at Guaranteed Minimum Crediting Rate [Member]" (M14) for the associated ranges.
- To convey "Greater than" in both "Policyholder Account Balance, Guaranteed Minimum Crediting Rate, Range from 0400 and Greater [Member]" (M13) and "Policyholder Account Balance, above Guaranteed Minimum Crediting Rate, Range from 0151 and Greater [Member]" (M17), the respective line items ("Policyholder Account Balance, Guaranteed Minimum Credit Rating" (L36) and "Policyholder Account Balance, above Guaranteed Minimum Crediting Rate" (L37)) are tagged with "nil" values and "Maximum [Member]" (M10). Additionally, to convey the start of the ranges for "Policyholder Account Balance, Guaranteed Minimum Crediting Rate, Range from 0400 and Greater [Member]" (M13) and "Policyholder Account Balance, above Guaranteed Minimum Crediting Rate, Range from 0151 and Greater [Member]" (M17), these line items would
also be tagged with "Minimum [Member]" (M9) and values of 0.0400 and 0.0151 , respectively.
- This example is not intended to be all inclusive due to variations for the ranges of guaranteed minimum crediting rates and the related ranges of difference, in basis points, between rates being credited to policyholders and the respective guaranteed minimums.
- Only the current period $\left(20 \mathrm{X}_{3}\right)$ is provided in the illustration of the XBRL report view due to size constraints.


## Example 3b-Disclosure of the Balances of and Changes in Policyholders' Account

Balances

This example illustrates the modeling for the balances of and changes in policyholders' account balances.

<img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-38.jpg?height=1171&width=1553&top_left_y=561&top_left_x=278" alt="image" style="width:100%;height:auto;">

### Figure 3b. 1

The legend for the elements used to tag these facts follows:

|  | Standard Label | Balance Type | Period Type | Element Name |
| :---: | :---: | :---: | :---: | :---: |
| A1 | Product and Service [Axis] |  | Duration | ProductOrServiceAxis |
|  | Product and Service [Domain] |  | Duration | ProductsAndServicesDomain |
| M3 | Universal Life [Member] |  | Duration | UniversalLifeMember |
| M4 | Fixed Annuity [Member] |  | Duration | FixedAnnuityMember |
| L35 | Policyholder Account Balance | Credit | Instant | PolicyholderFunds |
| L38 | Policyholder Account Balance, Premium Received | Debit | Duration | PolicyholderAccountBalancePremiumReceived |
| L39 | Policyholder Account Balance, Policy Charge | Debit | Duration | PolicyholderAccountBalancePolicyCharge |
| L40 | Policyholder Account Balance, Surrender and Withdrawal | Debit | Duration | PolicyholderAccountBalanceSurrenderAndWithdrawal |
| L41 | Policyholder Account Balance, Benefit Payment | Credit | Duration | PolicyholderAccountBalanceBenefitPayment |
| L42 | Transfer to (from) Policyholder Account Balance (to) from <br> Separate Account | Credit | Duration | TransferToFromPolicyholderAccountBalanceToFromSeparateAccou <br> $\mathrm{nt}$ |
| L43 | Policyholder Account Balance, Interest Expense | Debit | Duration | InterestCreditedToPolicyholdersAccountBalances |
| L44 | Policyholder Account Balance, Increase (Decrease) from Other <br> Change | Credit | Duration | PolicyholderAccountBalanceIncreaseDecreaseFromOtherChange |
| L45 | Policyholder Account Balance, Weighted Average Crediting Rate |  | Instant | PolicyholderAccountBalanceWeightedAverageCreditingRate |
| L46 | Policyholder Account Balance, Net Amount at Risk | Credit | Instant | PolicyholderAccountBalanceNetAmountAtRisk |
| L47 | Policyholder Account Balance, Cash Surrender Value | Credit | Instant | CashSurrenderValueDuePolicyholdersAmount |

### Figure 3b. 2

The XBRL report view created using the modeling structure is provided here:

| Standard Label |  | Preferred Label |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  | $\mathbf{2 0 X 3}$ |  | $20 X 2$ |  |
|  | Product and Service [Axis] <br> A1 |  | Universal Life <br>  <br> $\mathrm{M}_{3}$ | Fixed Annuity <br>  <br> M4 | Universal Life <br>  <br> M3 $_{3}$ | Fixed Annuity <br>  <br> M4 |
| L38 | Policyholder Account Balance, Premium <br> Received | Policyholder account balances, Premiums | 6900000 | 4990000 | 6545000 | 5100000 |
| L39 | Policyholder Account Balance, Policy Charge | Policyholder account balances, Policy charges | <img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-40.jpg?height=45&width=212&top_left_y=590&top_left_x=1605" alt="image" style="width:100%;height:auto;"> | 100000 | 150000 | 100000 |
| L40 | Policyholder Account Balance, Surrender and <br> Withdrawal | Policyholder account balances, Surrenders and <br> withdrawals | 500000 | 750000 | 450000 | 50000 |
| L41 | Policyholder Account Balance, Benefit Payment | Policyholder account balances, Benefit payments | 2000000 | 900000 | 1000000 | 450000 |
| L42 | Transfer to (from) Policyholder Account Balance <br> (to) from Separate Account | Policyholder account balances, Net transfers (from) to <br> policyholder account balance | 1640000 | 1900000 | 3250000 | 3750000 |
| L43 | Policyholder Account Balance, Interest Expense | Policyholder account balances, Interest credited | 855000 | 450000 | 555000 | 200000 |
| L44 | Policyholder Account Balance, Increase <br> (Decrease) from Other Change | Policyholder account balances, Other | 500000 | 95000 | 95000 | 60000 |
| $\mathbf{L} 35$ | Policyholder Account Balance | Policyholder account balances, Balance, end of year | 21540000 | 19270000 | 14445000 | 13585000 |
| $\mathbf{L 4 5}$ | Policyholder Account Balance, Weighted Average <br> Crediting Rate | Policyholder account balances, Weighted average <br> crediting rate | 0.0600 | 0.0600 | 0.0500 | 0.0500 |
| L46 | Policyholder Account Balance, Net Amount at <br> Risk | Policyholder account balances, Net amount at risk | 150000000 | 100000000 | 74000000 | 45000000 |
| L47 | Policyholder Account Balance, Cash Surrender <br> Value | Policyholder account balances, Cash surrender value | 11000000 | 7000000 | 5900000 | 3800000 |

Figure 3b. 3

## Notes:

- "Policyholder Account Balance, Surrender and Withdrawal" (L40) is used as part of the reconciliation because the company has disclosed the amount for these two types of reductions against the policyholder account balances as one amount. The following two alternative elements may be used if the amounts of surrenders and withdrawals are separately disclosed: "Policyholder Account Balance, Surrender" and "Policyholder Account Balance, Withdrawal."
- "Transfer to (from) Policyholder Account Balance (to) from Separate Account" (L42) is intended for use in both the policyholder account balance roll forward (shown in this example for one filer) and in the separate account liability roll forward (shown in Example 5a for a different filer). This line item element is modeled from the policyholder perspective with a transfer to the policyholder account as a positive (or credit) and a transfer from the policyholder account balance to a separate account as a negative (or debit) which represents movement of funds out of the policyholder account.
- The XBRL report view represents the date context for the years ended December $31,20 X_{3}$ and 20X2, and at December 31, 20X3 and 20X2, respectively; therefore, the beginning balances for the "Policyholder Account Balance" (L35) element for the period ending December 31, 20X2 are not presented because they would appear in a separate date context.


## Example $3^{\mathbf{c}-\text { Reconciliation }}$ of Policyholders' Account Balances to the Policyholders' Account Balances' Liability

This example illustrates the modeling for the reconciliation of policyholders' account balances to the policyholders' account balances' liability in the consolidated statement of financial position.

| The reconciliation <br> balances' liability in <br> the years ended: <br> (in thousands) |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Universal Life | L35, A1:M3 | $20 X_{3}$ |  | $20 X 2$ |  |
|  |  | $\$$ | 21,540 | $\$$ | 14,445 |
| Fixed Annuity | L35, A1:M4 |  | 19,270 |  | 13,585 |
| Other | L35, A1:M6 |  | 2,500 |  | 2,250 |
| Balance, end of year | L35 | $\$$ | 43,310 | $\$$ | 30,280 |

### Figure 3c. 1

The legend for the elements used to tag these facts follows:

|  | Standard Label | Balance Type | Period Type | Element Name |
| :--- | :--- | :---: | :---: | :---: |
| A1 | Product and Service [Axis] |  | Duration | ProductOrServiceAxis |
|  | Product and Service [Domain] |  | Duration | ProductsAndServicesDomain |
| M3 | Universal Life [Member] |  | Duration | UniversalLifeMember |
| M4 | Fixed Annuity [Member] |  | Duration | FixedAnnuityMember |
| M6 | Long-Duration Insurance, Other [Member] |  | Duration | OtherLongdurationInsuranceProductLineMember |
|  |  | Credit | Instant | PolicyholderFunds |
| L35 | Policyholder Account Balance |  |  |  |

Figure 3c. 2

The XBRL report view created using the modeling structure is provided here:

| Standard Label | Preferred Label |  |  |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | $20 X_{3}$ |  |  |  | $20 X 2$ |  |  |  |
| Product and Service <br>  <br> A1 |  | <img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-43.jpg?height=179&width=164&top_left_y=1179&top_left_x=1056" alt="image" style="width:100%;height:auto;"> | Fixed <br> Annuity <br>  <br> M4 | Long- <br> Duration <br> Insurance, <br> Other <br>  <br> M6 | Report- <br> wide Value | Universal Life <br>  <br> $\mathrm{M}_{3}$ | Fixed Annuity <br>  <br> M4 | <img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-43.jpg?height=179&width=164&top_left_y=1176&top_left_x=2164" alt="image" style="width:100%;height:auto;"> | Report- <br> wide value |
| Policyholder Account <br> Balance | Policyholders account <br> balances, Balance, end of year | 21540000 | 19270000 | 2500000 | 43310000 | 14445000 | 13585000 | 2250000 | 30280000 |

Figure 3c. 3

## Example 4a-Disclosure of the Balances of and Changes in Market Risk Benefits

This example illustrates the modeling for the balances of and changes in market risk benefits disaggregated by product.

| The balances of and changes in market risk <br> (in thousands) |  |  |  |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Balance, beginning of year | L48 | {A1:M5 <br> Variable Annuity} |  | {A1:M8 <br> Indexed Annuity} |  | {A1:M5 <br> Variable Annuity} |  | {A1:M8 <br> Indexed Annuity} |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  | $\$$ | 7,875 | $\$$ | 1,760 | $\$$ | 5,825 | $\$$ | 1,350 |
| Balance, beginning of year, before effect of <br> changes in instrument-specific credit risk | L49 |  | 8,275 |  | 2,110 |  | 5,990 |  | 1,200 |
| Issuances | L50 |  | 550 |  | 390 |  | 450 |  | 300 |
| Interest accrual | $\mathbf{L} 51$ |  | 1,700 |  | 250 |  | 500 |  | 250 |
| Attributed fees collected | L52 |  | 2,200 |  | 90 |  | 80 |  | 95 |
| Benefit payments | L53 |  | $(1,000)$ |  | $(800)$ |  | $(500)$ |  | (275) |
| Effect of changes in interest rates | L54 |  | 2,475 |  | 475 |  | 165 |  | 50 |
| Effect of changes in equity markets | L55 |  | 2,250 |  | 750 |  | 375 |  | 145 |
| Effect of changes in equity index volatility | L56 |  | 2,490 |  | 250 |  | 200 |  | 165 |
| Actual policyholder behavior different <br> from expected behavior | $\mathbf{L} 57$ |  | 6,500 |  | 100 |  | 820 |  | 105 |
| Effect of changes in future expected <br> policyholder behavior | L58 |  | 4,500 |  | 75 |  | 100 |  | 50 |
| Effect of change in other future expected <br> assumptions | L59 |  | 1,275 |  | 25 |  | 95 |  | 25 |
| Balance, end of year, before effect of <br> changes in instrument-specific credit risk | L49 |  | 31,215 |  | 3,715 |  | 8,275 |  | 2,110 |
| Effect of changes in instrument-specific <br> credit risk | L6o |  | $(540)$ |  | $(1,090)$ |  | $(400)$ |  | $(350)$ |
| Balance, end of year, net of effect of changes <br> in instrument-specific credit risk | L48 |  | 30,675 |  | 2,625 |  | 7,875 |  | 1,760 |
| Reinsurance recoverable, end of year | L61 |  | 2,200 |  | 425 |  | 100 |  | 150 |
| Balance, end of year, net of reinsurance | L62 | $\$$ | 28,475 | $\$$ | 2,200 | $\$$ | 7,775 | $\$$ | 1,610 |

## Figure 4a.1

The legend for the elements used to tag these facts follows:

|  | Standard Label | Balance Type | Period Type | Element Name |
| :---: | :---: | :---: | :---: | :---: |
| A1 | Product and Service [Axis] |  | Duration | ProductOrServiceAxis |
|  | Product and Service [Domain] |  | Duration | ProductsAndServicesDomain |
| M5 | Variable Annuity [Member] |  | Duration | VariableAnnuityMember |
| M8 | Indexed Annuity [Member] |  | Duration | IndexedAnnuityMember |
| L48 | Market Risk Benefit, after Increase (Decrease) from Instrument- <br> Specific Credit Risk | Credit | Instant | MarketRiskBenefitAfterIncreaseDecreaseFromInstrumentSpeci <br> ficCreditRisk |
| L49 | Market Risk Benefit, before Reinsurance and Cumulative Increase <br> (Decrease) from Instrument-Specific Credit Risk Change | Credit | Instant | MarketRiskBenefitBeforeReinsuranceAndCumulativeIncreaseD <br> ecreaseFromInstrumentSpecificCreditRiskChange |
| L50 | Market Risk Benefit, Issuance | Credit | Duration | MarketRiskBenefitIssuance |
| $\mathbf{L} 51$ | Market Risk Benefit, Interest Expense | Debit | Duration | MarketRiskBenefitInterestExpense |
| $\mathbf{L} 52$ | Market Risk Benefit, Attributed Fee Collected | Debit | Duration | MarketRiskBenefitAttributedFeeCollected |
| L53 | Market Risk Benefit, Benefit Payment | Credit | Duration | MarketRiskBenefitBenefitPayment |
| L54 | Market Risk Benefit, Increase (Decrease) from Interest Rate <br> Change | Credit | Duration | MarketRiskBenefitIncreaseDecreaseFromInterestRateChange |
| L55 | Market Risk Benefit, Increase (Decrease) from Equity Market <br> Change | Credit | Duration | MarketRiskBenefitIncreaseDecreaseFromEquityMarketChange |
| L56 | Market Risk Benefit, Increase (Decrease) from Volatility | Credit | Duration | MarketRiskBenefitIncreaseDecreaseFromVolatility |
| $\mathbf{L} 57$ | Market Risk Benefit, Increase (Decrease) from Actual Policyholder <br> Behavior Different from Expected | Credit | Duration | MarketRiskBenefitIncreaseDecreaseFromActualPolicyholderBe <br> haviorDifferentFromExpected |
| $\mathbf{L} 58$ | Market Risk Benefit, Increase (Decrease) from Future Expected <br> Policyholder Behavior Assumption | Credit | Duration | MarketRiskBenefitIncreaseDecreaseFromFutureExpectedPolicy <br> holderBehaviorAssumption |
| L59 | Market Risk Benefit, Increase (Decrease) from Other Assumption | Credit | Duration | MarketRiskBenefitIncreaseDecreaseFromOtherAssumption |
| L6o | AOCI, Market Risk Benefit, Instrument-Specific Credit Risk, <br> before Tax | Credit | Instant | AociMarketRiskBenefitInstrumentSpecificCreditRiskBeforeTax |
| L61 | Market Risk Benefit, Reinsurance Recoverable, after Allowance | Debit | Instant | MarketRiskBenefitReinsuranceRecoverableAfterAllowance |
| L62 | Market Risk Benefit, after Reinsurance and Cumulative Increase <br> (Decrease) from Instrument-Specific Credit Risk Change | Credit | Instant | MarketRiskBenefitAfterReinsuranceAndCumulativeIncreaseDe <br> creaseFromInstrumentSpecificCreditRiskChange |

### Figure 4a. 2

The XBRL report view created using the modeling structure is provided here (and continues on the following page):

|  | Standard Label | Preferred Label |  |  |
| :---: | :---: | :---: | :---: | :---: |
|  |  | $20 X_{3}$ |  |  |
|  | Product and Service [Axis] <br> A1 |  | Variable Annuity <br>  <br> M5 $_{5}$ | Indexed Annuity <br>  <br> M8 |
| L50 | Market Risk Benefit, Issuance | Market risk benefits, Issuances | 550000 | 390000 |
| $\mathbf{L} 51$ | Market Risk Benefit, Interest Expense | Market risk benefits, Interest accrual | 1700000 | 250000 |
| L52 | <img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-46.jpg?height=48&width=913&top_left_y=603&top_left_x=270" alt="image" style="width:100%;height:auto;"> | Market risk benefits, Attributed fees collected | 2200000 | 90000 |
| L53 | Market Risk Benefit, Benefit Payment | Market risk benefits, Benefit payments | 1000000 | 800000 |
| L54 | Market Risk Benefit, Increase (Decrease) from Interest Rate Change | Market risk benefits, Effect of changes in interest rates | 2475000 | 475000 |
| L55 | Market Risk Benefit, Increase (Decrease) from Equity Market Change | Market risk benefits, Effect of changes in equity markets | 2250000 | 750000 |
| L56 | Market Risk Benefit, Increase (Decrease) from Volatily | Market risk benefits, Effect of changes in equity index volatility | 2490000 | 250000 |
| L57 | Market Risk Benefit, Increase (Decrease) from Actual Policyholder <br> Behavior Different from Expected | Market risk benefits, Actual policyholder behavior different from <br> expected behavior | 6500000 | 100000 |
| L58 | Market Risk Benefit, Increase (Decrease) from Future Expected <br> Policyholder Behavior Assumption | Market risk benefits, Effect of changes in future expected <br> policyholder behavior | 4500000 | 75000 |
| L59 | Market Risk Benefit, Increase (Decrease) from Other Assumption | Market risk benefits, Effect of changes in other future expected <br> assumptions | 1275000 | 25000 |
| L49 | Market Risk Benefit, before Reinsurance and Cumulative Increase <br> (Decrease) from Instrument-Specific Credit Risk Change | Market risk benefits, Balance, end of year, before effect of changes <br> in instrument-specific credit risk | 31215000 | 3715000 |
| L6o | AOCI, Market Risk Benefit, Instrument-Specific Credit Risk, before Tax | Market risk benefits, Effect of changes in instrument-specific credit <br> risk | 540000 | 1090000 |
| L48 | Market Risk Benefit, after Increase (Decrease) from Instrument- <br> Specific Credit Risk | Market risk benefits, Balance, end of year, net of effect of changes in <br> instrument-specific credit risk | 30675000 | 2625000 |
| L61 | Market Risk Benefit, Reinsurance Recoverable, after Allowance | Market risk benefits, Reinsurance recoverable, end of year | 2200000 | 425000 |
| L62 | Market Risk Benefit, after Reinsurance and Cumulative Increase <br> (Decrease) from Instrument-Specific Credit Risk Change | Market risk benefits, Balance, end of year, net of reinsurance | 28475000 | 2200000 |

Figure 4a. 3

## Notes:

- The XBRL report view represents the date context for the year ended December 31, 20X3, and at December 31, 20X3; therefore, the beginning balances for the "Market Risk Benefit, after Increase (Decrease) from Instrument-Specific Credit Risk" (L48) and "Market Risk Benefit, before Reinsurance and Cumulative Increase (Decrease) from Instrument-Specific Credit Risk Change" (L49) elements for the period ending December 31, 20X2 are not presented because the amounts would appear in a separate date context.
- The element "AOCI, Market Risk Benefit, Instrument-Specific Credit Risk, before Tax" (L60) is modeled from the accumulated other comprehensive income perspective. For the calculation to work with the appropriate positive and negative values, the calculation summation parent is "Market Risk Benefit, before Reinsurance and Cumulative Increase (Decrease) from Instrument-Specific Credit Risk Change” (L49) with children of "AOCI, Market Risk Benefit, Instrument-Specific Credit Risk, before Tax" (L60) and "Market Risk Benefit, after Increase (Decrease) from Instrument-Specific Credit Risk" (L48). In this example, “AOCI, Market Risk Benefit, Instrument-Specific Credit Risk, before Tax" (L6o) is a credit to accumulated other comprehensive income and a debit to "Market Risk Benefit, before Reinsurance and Cumulative Increase (Decrease) from Instrument-Specific Credit Risk Change" (L49) and the XBRL value will be positive because it is from the accumulated other comprehensive perspective.


## 4b.1,Example 4b-Reconciliation of Market Risk Benefits by Asset and Liability Positions

This example illustrates the modeling for the reconciliation of market risk benefits by amounts that are in an asset position and those that are in a liability position to the market risk benefits amount in the consolidated statement of financial position.

<img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-48.jpg?height=534&width=1648&top_left_y=633&top_left_x=236" alt="image" style="width:100%;height:auto;">

## Figure 4b.1

The legend for the elements used to tag these facts follows:

|  | Standard Label | Balance Type | Period Type | Element Name |
| :---: | :---: | :---: | :---: | :---: |
| A1 | Product and Service [Axis] |  | Duration | ProductOrServiceAxis |
|  | Product and Service [Domain] |  | Duration | ProductsAndServicesDomain |
| M5 | Variable Annuity [Member] |  | Duration | VariableAnnuityMember |
| M8 | Indexed Annuity [Member] |  | Duration | IndexedAnnuityMember |
| L48 | Market Risk Benefit, after Increase (Decrease) from Instrument- <br> Specific Credit Risk | Credit | Instant | MarketRiskBenefitAfterIncreaseDecreaseFromInstrumentSpecific <br> CreditRisk |
| L63 | Market Risk Benefit, Asset, Amount | Debit | Instant | MarketRiskBenefitAssetAmount |
| L64 | Market Risk Benefit, Liability, Amount | Credit | Instant | MarketRiskBenefitLiabilityAmount |

Figure $4 \mathrm{~b} .2$

The XBRL report view created using the modeling structure is provided here:

| Standard Label |  | Preferred Label |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | $20 X_{3}$ |  |  |  | $20 X 2$ |  |  |
|  | Product and Service [Axis] <br> A1 |  | Variable Annuity <br>  <br> M5 | Indexed Annuity <br>  <br> M8 | Report-wide <br> Value | Variable Annuity <br>  <br> M5 | Indexed Annuity <br>  <br> M8 | Report-wide <br> Value |
| $\mathbf{L 6 3}$ | Market Risk Benefit, Asset, Amount | Market risk benefits, Asset | 2925000 | 1000000 | 3925000 | 2225000 | 40000 | 2265000 |
| L64 | Market Risk Benefit, Liability, <br> Amount | Market risk benefits, Liability | 33600000 | 3625000 | 37225000 | 10100000 | 1800000 | 11900000 |
| L48 | Market Risk Benefit, after Increase <br> (Decrease) from Instrument- <br> Specific Credit Risk | Market risk benefits, Net | 30675000 | 2625000 | 33300000 | 7875000 | 1760000 | 9635000 |

Figure 4b. 3

## Example 5a-Disclosure of the Balances of and Changes in Separate Account

## Liability

This example illustrates the modeling for the balances of and changes in separate account balances.

| The balances of and changes ir <br> (in thousands) |  |  |  |  |  |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  | Variable <br> Jniversal Life |  | Variable <br> Annuity |  | Other | Variable <br> Universal Life | Variable Annuity |  | Other |
|  |  |  | A1:M7 |  | A1:M5 |  | A1:M6 | A1:M7 | A1:M5 |  | A1:M6 |
| Balance, beginning of year | L65 | $\$$ | 47,400 | $\$$ | 890,640 | $\$$ | 19,510 | 25,000 | 550,000 | $\$$ | 15,000 |
| Premiums and deposits | L66 |  | 65,880 |  | 489,550 |  | 2,000 | 23,410 | 318,200 |  | 5,000 |
| Policy charges | $\mathbf{L 6 7}$ |  | $(6,000)$ |  | $(75,000)$ |  | (880) | $(1,600)$ | $(30,000)$ |  | (675) |
| Surrenders and withdrawals | L68 |  | $(1,000)$ |  | $(2,000)$ |  | $(560)$ | $(900)$ | $(2,100)$ |  | $(400)$ |
| Benefit payments | L69 |  | $(5,000)$ |  | $(10,000)$ |  | (350) | $(2,500)$ | $(7,500)$ |  | $(300)$ |
| Invested performance | L7o |  | 14,360 |  | 110,000 |  | 1,125 | 3,600 | 70,000 |  | 900 |
| Net transfers (from) to separate <br> account | L42 |  | $(4,300)$ |  | 760 |  | - | 500 | $(7,510)$ |  | 10 |
| Other charges | L71 |  | (90) |  | $(750)$ |  | $(85)$ | $(110)$ | $(450)$ |  | $(25)$ |
| Balance, end of year | L65 | $\$$ | 111,250 | $\$$ | $1,403,200$ | $\$$ | 20,760 | 47,400 | 890,640 | $\$$ | 19,510 |
| Cash surrender value | $\mathbf{L} 72$ | \$ | 104,480 | $\$$ | $1,113,832$ | $\$$ | 12,750 | 43,000 | 600,000 | $\$$ | 11,000 |

### Figure 5a. 1

The legend for the elements used to tag these facts follows:

|  | Standard Label | Balance Type | Period Type | Element Name |
| :---: | :---: | :---: | :---: | :---: |
| A1 | Product and Service [Axis] |  | Duration | ProductOrServiceAxis |
|  | Product and Service [Domain] |  | Duration | ProductsAndServicesDomain |
| M5 | Variable Annuity [Member] |  | Duration | VariableAnnuityMember |
| M6 | Long-Duration Insurance, Other [Member] |  | Duration | OtherLongdurationInsuranceProductLineMember |
| $\mathbf{M}_{7}$ | Variable Universal Life [Member] |  | Duration | VariableUniversalLifeMember |
| L42 | Transfer to (from) Policyholder Account Balance (to) from <br> Separate Account | Credit | Duration | TransferToFromPolicyholderAccountBalanceToFromSeparateA <br> ccount |
| L65 | Separate Account, Liability | Credit | Instant | SeparateAccountsLiability |
| L66 | Separate Account, Liability, Premium and Deposit | Debit | Duration | SeparateAccountLiabilityPremiumAndDeposit |
| L67 | Separate Account, Liability, Policy Charge | Debit | Duration | SeparateAccountLiabilityPolicyCharge |
| L68 | Separate Account, Liability, Surrender and Withdrawal | Debit | Duration | SeparateAccountLiabilitySurrenderAndWithdrawal |
| L69 | Separate Account, Liability, Benefit Payment | Credit | Duration | SeparateAccountLiabilityBenefitPayment |
| L7o | Separate Account, Liability, Increase (Decrease) from <br> Invested Performance | Credit | Duration | SeparateAccountLiabilityIncreaseDecreaseFromInvestedPerfor <br> mance |
| $\mathbf{L 7 1}$ | Separate Account, Liability, Increase (Decrease) from Other <br> Change | Credit | Duration | SeparateAccountLiabilityIncreaseDecreaseFromOtherChange |
| L72 | Separate Account, Liability, Cash Surrender Value, Amount | Credit | Instant | SeparateAccountLiabilityCashSurrenderValueAmount |

### Figure 5a.2

The XBRL report view created using the modeling structure is provided here:

| Standard Label |  | Preferred Label |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  | $20 X_{3}$ |  |  | $20 \times 2$ |  |  |
|  | Product and Service [Axis] <br> A1 |  | Variable <br> Universal Life <br>  <br> M7 $_{7}$ | Variable Annuity <br>  <br> M5 | Long-Duration <br> Insurance, Other <br>  <br> M6 | Variable <br> Universal Life <br>  <br> M7 | Variable Annuity <br>  <br> M5 | Long-Duration <br> Insurance, Other <br> M6 |
| L66 | Separate Account, Liability, <br> Premium and Deposit | Separate account liabilities, <br> Premiums and deposits | 65880000 | 489550000 | 2000000 | 23410000 | 318200000 | 5000000 |
| L67 | Separate Account, Liability, Policy <br> Charge | Separate account liabilities, <br> Policy charges | 6000000 | 75000000 | 880000 | 1600000 | 30000000 | 675000 |
| L68 | Separate Account, Liability, <br> Surrender and Withdrawal | Separate account liabilities, <br> Surrenders and withdrawals | 1000000 | 2000000 | 560000 | 900000 | 2100000 | 400000 |
| L69 | Separate Account, Liability, <br> Benefit Payment | Separate account liabilities, <br> Benefit payments | 5000000 | 10000000 | 350000 | 2500000 | 7500000 | 300000 |
| L7o | Separate Account, Liability, <br> Increase (Decrease) from Invested <br> Performance | Separate account liabilities, <br> Invested performance | 14360000 | 110000000 | 1125000 | 3600000 | 70000000 | 900000 |
| L42 | Transfer to (from) Policyholder <br> Account Balance (to) from <br> Separate Account | Separate account liabilities, <br> Net transfers (from) to <br> separate account | 4300000 | -760000 | 0 | -500000 | 7510000 | -10000 |
| L71 | Separate Account, Liability, <br> Increase (Decrease) from Other <br> Change | Separate account liabilities, <br> Other charges | -90000 | -750000 | -85000 | -110000 | -450000 | -25000 |
| L65 | Separate Account, Liability | Separate account liabilities, <br> Balance, end of year | 111250000 | 1403200000 | 20760000 | 47400000 | 890640000 | 19510000 |
| $\mathrm{L}^{72}$ | Separate Account, Liability, Cash <br> Surrender Value, Amount | Separate account liabilities, <br> Cash surrender value | 104480000 | 1113832000 | 12750000 | 43000000 | 600000000 | 11000000 |

Figure 5a.3

## Notes:

- "Separate Account, Liability, Premium and Deposit" (L66) is used in the reconciliation because the company has disclosed the amount for these two types of additions to the separate account balances as one amount. The following two alternative elements may be used if the amounts of premiums and deposits are separately disclosed: "Separate Account, Liability, Premium" and "Separate Account, Liability, Deposit."
- "Separate Account, Liability, Surrender and Withdrawal" (L68) is used in the reconciliation because the company has disclosed the amount for these two types of reductions to the separate account balances as one amount. The following two alternative elements may be used if the amounts of surrenders and withdrawals are separately disclosed: "Separate Account, Liability, Surrender" and "Separate Account, Liability, Withdrawal."
- "Transfer to (from) Policyholder Account Balance (to) from Separate Account" (L42) is intended for use in both the separate account liability roll forward (shown in this example for one filer) and in the policyholder account balance roll forward (shown in Example 3b for a different filer). This line item element is modeled from the policyholder perspective with a transfer from the separate account as a positive (credit to policyholder account) which represents a movement of funds out of the separate account and a transfer to the separate account as a negative (or debit to policyholder account) which represents movement of funds into the separate account.
- The XBRL report view represents the date context for the years ended December $31,20 X_{3}$ and 20X2, and at December 31, $20 \mathrm{X}_{3}$ and 20X2, respectively; therefore, the beginning balances for the "Separate Account, Liability" (L65) element for the period ending December 31, 20X2 are not presented because they would appear in a separate date context.


## Example 5b-Reconciliation of Separate Account Liability

This example illustrates the modeling for the reconciliation of separate account liabilities to the separate account liability balance in the consolidated statement of financial position.

| The reconciliation of $\mathrm{S}$ <br> position as of Decemb <br> (in thousands) |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Variable Universal Life | L65, A1:M7 | $20 X_{3}$ |  | $20 X 2$ |  |
|  |  | $\$$ | 111,250 | $\$$ | 47,400 |
| Variable Annuity | L65, A1:M5 |  | $1,403,200$ |  | 890,640 |
| Other | L65, A1:M6 |  | 20,760 |  | 19,510 |
| Balance, end of year | L65 | $\$$ | $1,535,210$ | $\$$ | 957,550 |

## Figure 5b. 1

The legend for the elements used to tag these facts follows:

|  | Standard Label | Balance Type | Period Type | Element Name |
| :---: | :---: | :---: | :---: | :---: |
|  | Product and Service [Axis] |  | Duration | ProductOrServiceAxis |
|  | Product and Service [Domain] |  | Duration | ProductsAndServicesDomain |
| M5 | Variable Annuity [Member] |  | Duration | VariableAnnuityMember |
| M6 | Long-Duration Insurance, Other [Member] |  | Duration | OtherLongdurationInsuranceProductLineMember |
| M7 | Variable Universal Life [Member] | Duration | VariableUniversalLifeMember |  |
|  |  | Credit | Instant | SeparateAccountsLiability |
| L65 | Separate Account, Liability |  |  |  |

Figure 5b. 2

The XBRL report view created using the modeling structure is provided here:

| Standard Label | Preferred Label |  |  |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | $20 X_{3}$ |  |  |  | $20 X 2$ |  |  |  |
| Product and Service [Axis] <br> A1 |  | Variable <br> Universal Life <br>  <br> $\mathrm{M}_{7}$ | Variable <br> Annuity <br>  <br> M5 | Long- <br> Duration <br> Insurance, <br> Other <br>  <br> M6 | <img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-55.jpg?height=176&width=176&top_left_y=1138&top_left_x=1678" alt="image" style="width:100%;height:auto;"> | Variable <br> Universal <br> Life <br>  <br> M7 | Variable <br> Annuity <br>  <br> M5 | Long- <br> Duration <br> Insurance, <br> Other <br>  <br> M6 | Report-wide <br> Value |
| Separate Account, Liability | Separate accounts liabilities, <br> Balance, end of year | 111250000 | 1403200000 | 20760000 | 1535210000 | 47400000 | 890640000 | 19510000 | 957550000 |

Figure 5b. 3

## Example 6a-Statement of Stockholders' Equity with Transition Adjustments on Initial Application of the New Guidance

This example provides a Statement of Stockholders' Equity to illustrate the modeling for the values for transition adjustments to retained earnings and Accumulated Other Comprehensive Income (AOCI) for application to the earliest period presented.

<img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-56.jpg?height=944&width=2396&top_left_y=482&top_left_x=170" alt="image" style="width:100%;height:auto;">

Legend: This legend is provided to illustrate the elements associated with values or to provide context. This information is not part of disclosure.

[1] XL78

## Figure 6a. 1

The legend for the elements used to tag these facts follows:

|  | Standard Label | Balance Type | Period Type | Element Name |
| :---: | :---: | :---: | :---: | :---: |
| A5 | Equity Components [Axis] |  | Duration | StatementEquityComponentsAxis |
|  | Equity Component [Domain] |  | Duration | EquityComponentDomain |
| M18 | AOCI Attributable to Parent [Member] |  | Duration | AccumulatedOtherComprehensiveIncomeMember |
| M19 | Common Stock [Member] |  | Duration | CommonStockMember |
| M20 | Additional Paid-in Capital [Member] |  | Duration | AdditionalPaidInCapitalMember |
| M21 | Retained Earnings [Member] |  | Duration | RetainedEarningsMember |
| M22 | Noncontrolling Interest [Member] |  | Duration | NoncontrollingInterestMember |
| A6 | Revision of Prior Period [Axis] |  | Duration | RestatementAxis |
|  | Revision of Prior Period [Domain] |  | Duration | RestatementDomain |
| M23 | Previously Reported [Member] |  | Duration | ScenarioPreviouslyReportedMember |
| M24 | Revision of Prior Period, Accounting Standards Update, Adjustment |  | Duration | RevisionOfPriorPeriodAccountingStandardsUpdateAdjustmentMember |
| L73 | Net Income (Loss), Including Portion Attributable to Noncontrolling <br> Interest | Credit | Duration | ProfitLoss |
| L74 | Other Comprehensive Income (Loss), Net of Tax | Credit | Duration | OtherComprehensiveIncomeLossNetOfTax |
| L75 | Equity, Including Portion Attributable to Noncontrolling Interest | Credit | Instant | StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest |
| L76 | APIC, Share-Based Payment Arrangement, Increase for Cost Recognition | Credit | Duration | AdjustmentsToAdditionalPaidInCapitalSharebasedCompensationRequisite <br> ServicePeriodRecognitionValue |
| L77 | Common Stock, Shares, Outstanding |  | Instant | CommonStockSharesOutstanding |
| XL78 | Accounting Standards Update [Extensible Enumeration] |  | Duration | AccountingStandardsUpdateExtensibleList |

## Figure 6a.2

The XBRL report views created using the modeling structure are provided here:

<img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-58.jpg?height=687&width=2644&top_left_y=330&top_left_x=53" alt="image" style="width:100%;height:auto;">

Figure 6a.3a (continues)

<img src="https://cdn.mathpix.com/cropped/2024_03_24_0f01d25a9b12156dd6b8g-58.jpg?height=656&width=2630&top_left_y=1138&top_left_x=67" alt="image" style="width:100%;height:auto;">

Figure 6a.3a (continued)

| Preferred <br> Label |  |
| :--- | :---: |
| Date Context 20X0-01-01 to 20X0-12-31  <br> XL78 http:/fasb.org/us-  <br> Accounting Standards Update [Extensible Enumeration]  gaap/20Xo\#AccountingStandardsUpdate201812Member |  |

Figure 6a.3b

## Notes:

- The XBRL report views represent the date context for 20Xo and 20X1. The other reporting periods would be similarly structured.
- The example would apply to either transition method-Retrospective Transition Method or Modified Retrospective Transition Method because the guidance is applied to beginning of the earliest period presented under both transition methods.
- An extensible enumeration element is used to convey the amendment from one ASU. "Accounting Standards Update [Extensible Enumeration]" (XL78) is used to tag the fact value indicating which ASU is affecting retained earnings in the Statement of Shareholders' Equity. The value of the extensible enumeration element is the member representing the specific ASU. If a filer reports values from more than one ASU within the filing, then the "Accounting Standards Update [Axis]" is intended to be used.


## Example 6b-Disclosure of Reconciliation of Liability for Future Policy Benefits with Incremental Effects of Modified Retrospective Transition Method under Retrospective Transition Method on Initial Application of the New Guidance

This example illustrates the modeling for the disaggregation of the liability for future policy benefits with the incremental effects of the modified retrospective transition method if a filer elects the retrospective transition method.

| Sample of liabili <br> (in thousands) |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: |
| Present <br> Value of <br> Expected <br> Net <br> Premiums | Adoption of ASU 2018-12 | [1]{} |  |  |
|  | Balance, end of year December 31, $20 X 0$ |  | L5, A6:M23 \$ | 195,000 |
|  | Effect of changes in cash flow assumptions, effect of <br> retrospective application |  | L7, A6:M25 | 3,000 |
|  | Effect of changes in cash flow assumptions, effect of modified <br> retrospective application |  | L7, A6:M26 | 2,000 |
|  | Effect of changes in cash flow assumptions, total |  | L7, A6:M24 | 5,000 |
|  | Adjusted Balance, end of year December 31, 20Xo |  | $\mathbf{L} 5 \$$ | 200,000 |
| Present <br> Value of <br> Expected <br> Future <br> Policy <br> Benefits | Balance, end of year December 31, 20Xo | [1]{} | L15, A6:M23 \$ | 330,000 |
|  | Effect of changes in cash flow assumptions, effect of <br> retrospective application |  | L17, A6:M25 | 18,000 |
|  | Effect of changes in cash flow assumptions, effect of modified <br> retrospective application |  | L17, A6:M26 | 27,000 |
|  | Effect of changes in cash flow assumptions, total |  | L17, A6:M24 | 45,000 |
|  | Adjusted Balance, end of year December 31, 20Xo |  | $\mathbf{L 1 5} \$$ | 375,000 |

Legend: This legend is provided to illustrate the elements associated with values or to provide context. This information is not part of disclosure.

[1] XL78

### Figure 6b. 1

The legend for the elements used to tag these facts follows:

|  | Standard Label | Balance Type | Period Type | Element Name |
| :---: | :---: | :---: | :---: | :---: |
| A6 | Revision of Prior Period [Axis] |  | Duration | RestatementAxis |
|  | Revision of Prior Period [Domain] |  | Duration | RestatementDomain |
| M23 | Previously Reported [Member] |  | Duration | ScenarioPreviouslyReportedMember |
| M24 | Revision of Prior Period, Accounting Standards Update, Adjustment |  | Duration | RevisionOfPriorPeriodAccountingStandardsUpdateAdjustmentMem <br> ber |
| M25 | Effect of Retrospective Application of Accounting Standards <br> Update 2018-12 [Member] |  | Duration | EffectOfRetrospectiveApplicationOfAccountingStandardsUpdate2 <br> 01812Member |
| M26 | Effect of Modified Retrospective Application Accounting Standards <br> Update 2018-12 [Member] |  | Duration | EffectOfModifiedRetrospectiveApplicationAccountingStandardsU <br> pdate201812Member |
| L5 | Liability for Future Policy Benefit, Expected Net Premium, before <br> Reinsurance, after Discount Rate Change | Debit | Instant | LiabilityForFuturePolicyBenefitExpectedNetPremiumBeforeReinsura <br> nceAfterDiscountRateChange |
| $\mathbf{L} 7$ | Liability for Future Policy Benefit, Expected Net Premium, <br> Cumulative Increase (Decrease) from Cash Flow Change | Debit | Instant | LiabilityForFuturePolicyBenefitExpectedNetPremiumCumulativeIncr <br> easeDecreaseFromCashFlowChange |
| L15 | Liability for Future Policy Benefit, Expected Future Policy Benefit, <br> before Reinsurance, after Discount Rate Change | Credit | Instant | LiabilityForFuturePolicyBenefitExpectedFuturePolicyBenefitBeforeRe <br> insuranceAfterDiscountRateChange |
| L17 | Liability for Future Policy Benefit, Expected Future Policy Benefit, <br> Cumulative Increase (Decrease) from Cash Flow Change | Credit | Instant | LiabilityForFuturePolicyBenefitExpectedFuturePolicyBenefitCumulati <br> veIncreaseDecreaseFromCashFlowChange |
| XL78 | Accounting Standards Update [Extensible Enumeration] |  | Duration | AccountingStandardsUpdateExtensibleList |

### Figure 6b. 2

The XBRL report view created using the modeling structure is provided here:

| Standard Label | Preferred Label |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  |  | $20 X 0$ |  |  |
| Revision of Prior Period <br>  <br> A6 |  | Previously Reported <br>  <br> M23 | Revision of Prior Period, <br> Accounting Standards <br> Update, Adjustment <br>  <br> M24 | Effect of Retrospective <br> Application of Accounting <br> Standards Update 2018-12 <br>  <br> M25 | Effect of Modified <br> Retrospective Application <br> Accounting Standards <br> Update 2018-12 [Member] <br> M26 | Report- <br> wide Value |
| Liability for Future Policy <br> Benefit, Expected Net <br> Premium, before <br> Reinsurance, after <br> Discount Rate Change | Present value of <br> expected net <br> premiums, balance, <br> end of year | 195000000 |  |  |  | 200000000 |
| Liability for Future Policy <br> Benefit, Expected Net <br> Premium, Cumulative <br> Increase (Decrease) from <br> Cash Flow Change | Present value of <br> expected net <br> premiums, effect of <br> changes in cash flow <br> assumptions, total |  | 5000000 | 3000000 | 2000000 |  |
| Liability for Future Policy <br> Benefit, Expected Future <br> Policy Benefit, before <br> Reinsurance, after <br> Discount Rate Change | Present value of <br> expected future policy <br> benefits, balance, end <br> of year | 330000000 |  |  |  | 375000000 |
| Liability for Future Policy <br> Benefit, Expected Future <br> Policy Benefit, <br> Cumulative Increase <br> (Decrease) from Cash <br> Flow Change | Present value of <br> expected future policy <br> benefits, effect of <br> changes in cash flow <br> assumptions, total |  | 45000000 | 18000000 | 27000000 |  |

### Figure 6b.3a

| XL78 | {Standard Label <br> Date Context} |  |  |
| :---: | :---: | :---: | :---: |
|  |  |  | 20X0-01-01 to 20Xo-12-31 |
|  | Accounting Standards Update [Extensible Enumeration] |  | http://fasb.org/us- <br> gaap/20Xo\#AccountingStandardsUpdate201812Member |

Figure 6b.3b

## Notes:

- The example includes only a portion of the disaggregated roll forward for the liability for future policy benefits to illustrate the intended modeling for the transition effects. The date context would be expected to be consistent with a revision of a prior period and be the ending of the reporting period before the beginning of the earliest period presented.
- If the information in the example was disaggregated by multiple product lines, the "Product and Service [Axis]" may be used.
- An extensible enumeration element is used to convey the amendment from one ASU. "Accounting Standards Update [Extensible Enumeration]" $(\mathbf{X L 7 8})$ is used to tag the fact value indicating which ASU is affecting the financial statements. The value of the extensible enumeration element is the member representing the specific ASU. If a filer reports values from more than one ASU within the filing, then the "Accounting Standards Update [Axis]" is intended to be used.


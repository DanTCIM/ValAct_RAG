# Measuring Impact of Reinsurance on Earnings under IFRS 17
https://www.soa.org/sections/financial-reporting/financial-reporting-newsletter/2023/september/fr-2023-09-zhang/

By Hui Shan, Tianchi (Paul) Zhang and Wenzhen Wu

The Financial Reporter, September 2023

The implementation of the IFRS 17 insurance accounting standard has brought significant changes to the financial reporting landscape of insurance companies. With new disclosure requirements and altered profit analysis, understanding and interpreting future profitability have become a topic of concern for the industry. While stability remains a key objective for insurance companies, the earning patterns might become more volatile especially when the contractual service margin (CSM) is exhausted, and a loss component (LC) needs to be established. Reinsurance, a common risk mitigation tool, can play a pivotal role in managing earnings volatility and minimizing losses for onerous measurement units. In this article, we propose a new key performance indicator (KPI) called “loss recoverability” to assess the performance of reinsurance treaties in achieving these objectives. We explain how this KPI can be utilized in multiple scenarios to evaluate the effectiveness of reinsurance strategies and pursue stability in earning patterns.

## Earning Pattern and Volatility
With the completion of the implementation of IFRS 17, insurance companies are now shifting their attention to understanding and explaining earning patterns. Under the new standard, maintaining a stable and predictable earning trajectory becomes a primary focus within the industry. However, it’s important to recognize that companies can experience earnings fluctuations when the measurement unit is onerous, with the establishment of the LC, as opposed to non-onerous groups where the CSM is established. This discrepancy primarily arises from the different sources of earnings.

### Earning Patterns for Non-Onerous
For non-onerous groups, earnings[1] are solely from the current service. Any changes related to future service do not directly impact current-period earnings but are absorbed by the CSM, as per IFRS 17 Paragraph 44(c). The intention is to reflect adjustments related to future services in the balance sheet rather than immediately impacting the income statement. This provision prevents changes related to future services within non-onerous groups from resulting in significant earnings volatility in the current reporting period.

Let’s consider the following illustration example:

For the non-onerous group, the income is derived from current service only:

|Insurance Service Result | Amount |
|---|---|
|Current Service||
|Release of Risk Adjustment|100|
|CSM amortization|200|
|Release of Expected Cash Flow[2]|100|
|Actual Cash flow|-150|
|Total|250|

Assuming there is an increase of $1,000 in the fulfillment of cash flow (FCF) due to assumption unlocking and CSM amortization ratio of 10% for the current period, the impact of $1000 is absorbed by the CSM and the CSM amortization amount decreases by $100. Although the assumption unlocking leads to a $1,000 increase in FCF, the impact on the earning statement in the current period is only $100 through CSM amortization.

### Earning Patterns for Onerous
In contrast, for onerous groups, earnings are impacted by future service as well. As per IFRS 17 Paragraph 48 and 49, when a group becomes onerous, changes in FCF related to future service are recorded in the LC and recognized in Profit & Loss (P&L) immediately.

Back to the previous example, when assumption unlocking increase FCF $1,000 for an onerous group, the income statement looks as follows:

|Insurance Service Result|Amount|
|---|---|
|Current Service||
|Release of Risk Adjustment|100|
|Release of Expected Cash Flow|100|
|Actual Cash flow|-150|
|Future Service||
|FCF Impacts relate to future service|-1,000|
|Total|-950|

In this example, the current service contributes a $50 gain while the future service contributes a $1,000 loss, which results in the total earning as a $950 loss.

Consequently, IFRS 17 earnings volatility becomes more pronounced in onerous groups, as the impact related to future service is included.

In short, irrespective of whether the impacts pertain to future services or not, when groups are in a loss status, the entire amounts associated with changes related to future services are recognized as IFRS 17 earnings for the current period. This requirement can significantly increase the volatility of the earnings patterns compared to when the groups are in a profitable status. Therefore, by understanding the differential impact on earnings volatility between onerous and non-onerous groups, companies can attenuate the impact of earnings fluctuations and strive for a more stable earnings pattern over time.

### Solution: Reinsurance
According to the IFRS 17 standard, insurance companies are required to report reinsurance contracts separately. Similar to direct business, the sources of IFRS 17 earnings for the reinsurance groups differ when the underlying direct group switches between onerous and non-onerous.

When a direct group is non-onerous, the earnings of the reinsurance group are determined solely by reinsurance cash flows. However, in the case of the direct group being onerous, the earnings of the reinsurance group are also impacted by the direct group. This is due to the regulation outlined in IFRS 17 Paragraph 66(c) and 66B, which establishes a Loss Recovery Component (LRC) when the underlying direct group becomes onerous. The purpose of the LRC is to monitor and offset direct losses related to future service by releasing earnings immediately. This reduction in earnings also impacts the CSM balance for the reinsurance group. Thus, it can be understood that the reinsurance group releases earnings from future profits to counterbalance direct losses related to future service.

To illustrate this point, let’s refer to the previous example:

Assuming there is a reinsurance treaty to cover this direct business with onerous status, the IFRS 17 income of this reinsurance group will look like the following:

Ceded Earning Statement:

|Insurance Service Result|Amount|
|--|--|
|Reinsurance Group Itself||
|Release of Risk Adjustment|-30|
|Release of CSM|-20|
|Release of Expected Cash Flow|-80|
|Actual Cash flow|110|
|Underlying Direct Group|| 
|Reimbursed Direct loss related to future service|300|
|Total|280|

In this example, the reinsurance group itself contributes a loss of $20. Meanwhile, a $300 gain is recognized through the LRC, aimed at offsetting the future service losses from direct. Consequently, the total earnings of the reinsurance group for this period are $280.

Direct Earning Statement:

|Insurance Service Result|Amount|
|Current Service||
|Release of Risk Adjustment|100|
|Release of Expected Cash Flow|100|
|Actual Cash flow|-150|
|Future Service||
|FCF Impacts relate to future service|-1,000|
|Total|-950|

Note: On ceded side, there are $300 earnings to reimburse this additional loss related to future service.

As illustrated, reinsurance could be utilized as a robust and effective tool to mitigate the additional losses related to future service and manage the earnings volatility for direct onerous business. If IFRS 17 financials form the key basis for an insurer’s performance management, a deep understanding of the impact of reinsurance would empower the insurer to effectively redefine their reinsurance strategies and optimize their risk management practices. Ultimately, this approach enhances financial stability.

## New KPI: Loss Recoverability
Reinsurance could be a useful tool to mitigate direct losses, including the additional loss related to future service. However, measuring the effectiveness of reinsurance contracts in achieving this goal is not a straightforward task. Traditional KPIs, such as comparing actual claims between direct and ceded, are inadequate as both direct and ceded earnings are impacted by future service.

I, therefore, propose a new KPI “loss recoverability,” which takes into consideration the impacts of both future and current services. The formula for calculating this KPI is as follows (AvE is actual versus expected, and in this article we are focused on claims experience only, while in reality expenses may be included too):

Loss recoverability = (reinsurance AvE for claims in current period + reimbursement for future service) / (Direct AvE for claims in current period + losses from changes related to future service)

Let’s revisit the earlier example:

Assuming an expected claim is $40 while an actual claim is $50 for the direct group, with an expected claim reimbursement of $20 and an actual claim reimbursement of $25 from reinsurance. For the direct group, the AvE for claim in the current period is $10 and the loss related to future service is $1,000. For the ceded group, the AvE for claim is $5 and the recovery for direct future loss related to future service is $300.

Consequently, the loss recoverability ratio in this example is calculated as:
Loss recoverability = (5+300) / (10+1000) = 30.19%
Calculation of loss recoverability, resulting in 30.19%

The loss recoverability ratio is affected by various factors outlined in the reinsurance agreement:

- Scope: Reinsurance contracts provide recovery for certain types of claims from an underlying direct business.
- Balance: Reinsurance contracts provide recovery with a minimum retention, a maximum limit, or both.

When the ratio falls below expectations, insurance companies should consider the following actions:

1. Re-evaluate the coverage scope, as it may exclude the type of claim that contributes significantly to losses in the current reinsurance contract.
2. Increase the coverage balance when the current utilization has reached its limit. In the event of future adverse events resulting in increased claims for the direct business, the reinsurance contract may not provide sufficient recovery for the additional losses.

Therefore, it is crucial for insurance companies to conduct a thorough assessment of reinsurance contracts, considering the terms and limitations, to ensure adequate coverage and effective risk management practices.

### Potential Applications
With the loss recoverability to reflect the capability of reinsurance contracts for loss mitigation and volatility control, the company could leverage this KPI in multiple scenarios:

1. Prioritize onerous groups—When multiple groups turn to onerous, a loss recoverability KPI can identify the onerous groups that need an immediate redesign or reprice of the current reinsurance treaties.
2. Optimize existing reinsurance treaties—With multiple reinsurance contracts, especially multiple reinsurance contracts for same direct business, the company could leverage loss recoverability ratios to assess how each reinsurance contract is performing and optimize current reinsurance portfolio.
3. Support new reinsurance strategy—Loss recoverability ratios could be treated as a reference to support the company to pursue new reinsurance contracts. By leveraging the loss recoverability ratio from old policies, leadership could customize the reinsurance agreement to better fit the underlying direct business.
4. Integration with other IFRS 17 KPIs—A forward-looking and comprehensive future strategy could be developed by integrating the loss recoverability KPI with other IFRS 17 KPIs. One such KPI is the profit margin, which measures in-force business profitability by comparing insurance service earnings with insurance service revenue. Utilizing the profit margin, companies can analyze the impact of reinsurance profit by comparing the ratio before and after reinsurance. This integrated approach enables companies to identify the optimal reinsurance solution from an enterprise-wide perspective, aligning financial gains with risk exposure and supporting robust risk management practices to enhance overall financial performance.

Overall, loss recoverability provides a valuable metric for assessing the efficiency of reinsurance arrangements under IFRS 17. It helps insurance companies understand the financial implications of their reinsurance strategies, optimize risk mitigation efforts, and achieve more stable and predictable earnings over time.

### Implementation
For actuaries, the practical implementation of loss recoverability as a new KPI entails several important considerations:

- Data Granularity: A crucial element of the implementation involves determining the appropriate level of data granularity for analysis. This involves breaking down the data to differentiate between losses and recoveries covered by different reinsurance treaties. By adopting a company-wide agreed approach to data analysis, the company can gain deeper insights into the efficacy of the reinsurance risk mitigation strategy.
- Addressing Challenges:
    - One such challenge is how to effectively manage profitability flips between periods, from onerous to non-onerous and vice versa.
    Potential financial impacts such as the misalignment of ceded CSM amortization with direct amortization need to be understood given that the ceded CSM is often tied to reinsurance price rather than the direct CSM. Such misalignment may need to be included in the loss recoverability KPI as an adjustment to fully understand the impact of reinsurance.
    - Obtaining accurate and reliable data for the analysis could be one of the challenges.
    - Insurance companies could have complicated reinsurance structures, for example, many-to-many reinsurance setup, not a straightforward one-to-one relationship. Managing and analyzing data would require additional effort and decision making.
    - In short, by recognizing and addressing these challenges, the company can enhance the effectiveness of explaining and managing its performance, thereby maximizing the value derived from the new KPI in evaluating reinsurance arrangements and driving informed decision-making.

## Conclusion
The implementation of IFRS 17 has introduced new challenges related to earnings volatility and risk mitigation for insurance companies. By leveraging the reinsurance strategies and measuring their effectiveness using the loss recoverability KPI, insurers can enhance their ability to control earnings volatility and minimize the loss impact of onerous groups. This proactive approach to risk management can contribute to long-term financial stability and improved profitability in the evolving landscape of insurance accounting.
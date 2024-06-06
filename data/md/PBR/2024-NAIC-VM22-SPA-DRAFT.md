# VM-22 Section 6: Requirements for the Additional Standard Projection Amount
June 2024, NAIC

> Exposure Note: For partial withdrawals, surrenders, and mortality assumptions in the June 2024 exposed draft, please provide comments on the structure and methodology within the additional standard projection amount calculation, as well as specific values (which were updated by the NAIC drafting groups).

# Section 6: Requirements for the Additional Standard Projection Amount
## A. Overview
1. Determining the Additional Standard Projection Amount
    - a. The additional standard projection amount shall be the larger of zero and an amount determined in aggregate for all contracts within each reserving category falling under the scope of these requirements, excluding those contracts that pass the exclusion tests in Section 7 and to which VM-A, VM-C, and VM-V are applied, by calculating the Prescribed Projections Amount under the CTE with Prescribed Assumptions (CTEPA) method. The company shall assess the impact of aggregation on the additional standard projection amount.

> Guidance Note: The following outlines one method that may be used to assess the impact of aggregation. If a company plans to use a different method, they should discuss that method with their domiciliary commissioner.   
> The benefit of aggregation is determined using the following steps, using the same scenario used for the cumulative decrement analysis, and using prescribed assumptions and discount rates:
> 1. Calculate the present value of each contract’s accumulated deficiency up through the duration of the aggregate GPVAD. When determining the contract accumulated deficiency: (a) contract starting assets equal CSV; (b) contract level starting assets include both separate account and general account assets, and exclude any hedge assets; (c) discount rate for the PVAD is the NAER; and (d) for a contract that terminates prior to the duration of the GPVAD, there will no longer be liability cash flows, but assets (positive or negative) continue to accumulate. 
> 2. The impact of aggregation is the sum of the absolute value of the negative amounts from step 1 above.  
> Apply steps 1 and 2 above to each model point .

1. 
    - b. The additional standard projection amount shall be calculated based on the scenario reserves, as discussed in Section 4.B, with certain prescribed assumptions replacing the company prudent estimate assumptions. As is the case in the projection of a scenario in the calculation of the DR and SR, the scenario reserves used to calculate the additional standard projection amount are based on an analysis of asset and liability cash flows produced along certain equity and interest rate scenario paths.

## B. Additional Standard Projection Amount 
1.	General  
Where not inconsistent with the guidance given here, the process and methods used to determine the additional standard projection amount under the CTEPA method shall be the same as required in the calculation of the DR and SR as described in Section 3.D and Section 3.E of these requirements. Regarding groups of contracts for which a DR is calculated, any references to CTE in this section (e.g., CTE70 (adjusted) and CTE70 (best efforts)) shall instead follow a scenario reserve calculation, pursuant to the requirements in Section 7.E.2. Any additional assumptions needed to determine the additional standard projection amount shall be explicitly documented.

2.	The company shall determine the Prescribed Projections Amount by following the CTEPA Method below. 

3.	For determining the CTE70 (adjusted), the assumptions for hedging programs with hedge payoffs that offset interest credits associated with indexed interest strategies (indexed interest credits) shall be the same as those used for the CTE70 (best efforts), following the requirements in Section 4.A.4.b.

4.	Calculation Methodology
    
    - a.	CTEPA Method:  
        - i. If the company used a model office to calculate the CTE Amount, then the company may continue to use the same model office, or one that is no less granular than the model office that was used to determine the CTE Amount, provided that the company shall maintain consistency in the grouping method used from one valuation to the next.
        - ii. Calculate the Prescribed Projections Amount as the CTE70 (adjusted) using the same method as that outlined in Section 9.C (which is the same as the DR and SR following Section 4.A.4.b for a company that does not have a future hedging strategy supporting the contracts other than those supporting index interest credits) but substituting the assumptions prescribed by Section 6.C. The calculation of this Prescribed Projections Amount also requires that the scenario reserve for any given scenario be equal to or in excess of the cash surrender value in aggregate on the valuation date for the group of contracts modeled in the projection. 
    - b.	Once the Prescribed Projections Amount is determined by the method above, then the company shall reduce the Prescribed Projections Amount by the CTE70 (adjusted). The difference shall be referred to as the Unbuffered Additional Standard Projection Amount.
    - c.	Reduce the Unbuffered Additional Standard Projection Amount by an amount equal to the difference between (i) and (ii), where (i) and (ii) are calculated in the following manner:
        - i. Calculate the Unfloored CTE70 (adjusted), using the same procedure as CTE70 (adjusted) but without requiring that the scenario reserve for any scenario be no less than the cash surrender value in aggregate on the valuation date.  
        - ii. Calculate the Unfloored CTE65 (adjusted), which is calculated in the same way as Unfloored CTE70 (adjusted) but averaging the 35% (instead of 30%) largest values.
    - d.	The additional standard projection amount shall subsequently be the larger of the quantity calculated in Section 6.B.4.c and zero. 

5.	Modeled Reinsurance  
Cash flows associated with reinsurance shall be projected in the same manner as that used in the calculation of the DR and SR as described in Section 3.

6.	Modeled Hedges  
Cash flows associated with hedging shall be projected in the same manner as that used in the calculation of the CTE70 (adjusted) as discussed in Section 9.C or Section 4.A.4.b for a company without a future hedging strategy supporting the contracts other than a future hedging strategy with hedge payoffs that offset interest credits associated with indexed interest strategies.

## C. Prescribed Assumptions
### 1.	Assignment of Guaranteed Benefit Type  
- a. Assumptions shall be set for each contract in accordance with the contract’s guaranteed benefit type, where a number of common benefit types are specifically defined in VM-01 (e.g., GMDB, GMWB, etc.). 

- b. Certain guaranteed living benefit products have features that can be described by multiple types of guaranteed benefits. If the guaranteed living benefit can be described by more than one of the definitions in VM-01 for the purpose of determining the additional standard projection amount, the company shall select the guaranteed benefit type that it deems best applicable and shall be consistent in its selection from one valuation to the next. For instance, if a guaranteed living benefit has both lifetime GMWB and non-lifetime GMWB features and the company determines that the lifetime GMWB is the most prominent component; assumptions for all contracts with such a guaranteed living benefit shall be set as if the guaranteed living benefit were only a lifetime GMWB and did not contain any of the non-lifetime GMWB features. If the company determines that the non-lifetime GMWB is the most prominent component; assumptions for all contracts with such a guaranteed living benefit shall be set as if the guaranteed living benefit were only a non-lifetime GMWB and did not contain any of the lifetime GMWB features. 

- c. Certain Group Annuity or Pension Risk Transfer contracts may contain multiple types of guaranteed benefits. For example, a Pension Risk Transfer contract may provide guaranteed benefits comprised of a combination of payout annuities, account value-based benefits, life-contingent lump sum payouts, and/or death benefits if the original pension plan that purchased the contract provided a range of benefit types to its participants. For such contracts, the company shall use the corresponding prescribed Group Annuity or Pension Risk Transfer assumptions consistently for all guaranteed benefits valued under the contract regardless of the nature of the benefits. For Group Annuity or Pension Risk Transfer contracts containing multiple types of guaranteed benefits, a description of the various guaranteed benefits included within the contracts and their prevalence and materiality should be disclosed in the PBR Actuarial Report.

- d. If a contract cannot be classified into any categories within a given assumption, the company shall determine the defined benefit type with the most similar benefits and risk profile as the company’s benefit and utilize the assumption prescribed for this benefit.

### 2.	Maintenance Expenses  
Maintenance expense assumptions shall be determined as the sum of (a) plus (b) if the company is responsible for the administration or (c) if the company is not responsible for the administration of the contract:  
- a. Each contract for which the company is responsible for administration incurs an annual expense equal to the Base Maintenance Expense Assumption shown in the table below for each product type multiplied by [1.025]^(valuation year – 2015) in the first projection year, and increased by an assumed annual inflation rate of [2%] for subsequent projection years.

Table 6.1: Base Maintenance Expense Assumptions

|Contract Type|Base Maintenance Expense Assumption|
|--|--|
|Contracts in the Payout Annuity Reserving Category	|$50|
|Fixed Indexed Annuities and other contracts in the Accumulation Reserving Category with guaranteed living benefits	|$100|
|All other contracts|$75|

> Drafting Note: The expense assumptions may be updated closer to adoption, such that the base maintenance expense assumptions are higher and the starting calendar year for accumulating inflation is updated to be more in line with the effective year of VM-22 PBR.

- b. Seven basis points of the projected account value for each year in the projection.

- c. Each contract for which the company is not responsible for administration (e.g., if the contract were assumed by the company in a reinsurance transaction in which only the risks associated with a guaranteed benefit rider were transferred) incurs an annual expense equal to $35 multiplied by [1.025]^(valuation year – 2015) in the first projection year, increased by an assumed annual inflation rate of [2%] for subsequent projection years.

### 3.	Guarantee Actuarial Present Value  
The Guarantee Actuarial Present Value (GAPV) is used in the determination of the  full surrender rates (Section 6.C.5) and other voluntary contract terminations (Section 6.C.10). The GAPV represent the integrated actuarial present value of the lump sum or income payments associated with all guaranteed living and death benefits, including account value, within the policy. For the purpose of calculating the GAPV, such payments shall include the portion that is paid out of the contract holder’s Account Value. Regarding contracts for which there is no account value or surrender benefit, such as some contracts within the Payout Annuity Reserving Category and Longevity Reinsurance Reserving Category, the GAPV requirements are not applicable.  
The calculation of an integrated benefit, for a future projection period can be expressed as:
tpx * Living Benefit (survival to receive benefit at time t and associated amount) + qx * Death Benefit (then current probability of death multiplied by any death benefit)  
The GAPV shall be calculated in the following manner:  
- a. 	The GAPV shall be determined by setting the guaranteed benefit exercise timing in a prudent matter, such that the policyholder realizes the value and broader efficiency of the product (i.e., elect immediate, defer until a significant deferral credit or attained age band break, etc.). Note that it is generally prudent to assume immediate election, unless there are other product feature considerations that make immediate election unavailable or significantly less valuable than waiting for a preset period of time
- b. 	Once a GMWB is exercised, the contract holder shall be assumed to withdraw in each subsequent contract year an amount equal to no less than the initial percentage taken of the GMWB’s guaranteed maximum annual withdrawal amount in that contract year (and 100% when the account value is depleted). 
- c. 	If account value growth is required to determine projected benefits or product features, then the account value growth shall either be assumed to be the current fixed index credited interest rate or the current option budget, by strategy, reduced by fees chargeable to the account value.
- d. 	For a GMDB that terminates at a certain age or in a certain contract year, the GAPV shall be calculated as if the GMDB does not terminate. Benefit features such as guaranteed growth in the GMDB benefit basis may be calculated so that no additional benefit basis growth occurs after the GMDB termination age or date defined in the contract.
- e. 	The mortality assumption used shall be the following:  
    - i. For Individual Annuity contracts within the Accumulation Reserving Category, the mortality rate for a contract holder with age x in year (2012 + n) shall be calculated using the following formula, where qx denotes mortality from the 2012 IAM Basic Mortality Table multiplied by the appropriate factor (Fx) from Table 6.2 and G2x denotes mortality improvement from Projection Scale G2:  
q_x^(2012+n)=q_x^2012 (1-〖G2〗_x )^n*F_x  

Table 6.2: Fx for Individual Annuities in Accumulation Reserving Category  

|Attained Age (x)	|For Contracts Without Guaranteed Living Benefits||For Contracts With Guaranteed Living Benefits||
|-|-|-|-|-|
| |Female	|Male	|Female	|Male|
|<=50	|150.0%	|120.0%	|125.0%	|105.0%|
|51	|150.0%	|120.0%	|125.0%	|105.0%|
|52	|150.0%	|120.0%	|125.0%	|105.0%|
|53	|150.0%	|118.0%	|125.0%	|101.6%|
|54	|150.0%	|116.0%	|125.0%	|98.2%|
|55	|150.0%	|114.0%	|125.0%	|94.8%|
|56	|150.0%	|112.0%	|125.0%	|91.4%|
|57	|150.0%	|110.0%	|125.0%	|88.0%|
|58	|144.0%	|107.0%	|119.0%	|86.0%|
|59	|138.0%	|104.0%	|113.0%	|84.0%|
|60	|132.0%	|101.0%	|107.0%	|82.0%|
|61	|126.0%	|98.0%	|101.0%	|80.0%|
|62	|120.0%	|95.0%	|95.0%	|78.0%|
|63	|117.6%	|97.0%	|94.0%	|80.0%|
|64	|115.2%	|99.0%	|93.0%	|82.0%|
|65	|112.8%	|101.0%	|92.0%	|84.0%|
|66	|110.4%	|103.0%	|91.0%	|86.0%|
|67	|108.0%	|105.0%	|90.0%	|88.0%|
|68	|110.0%	|105.6%	|92.6%	|89.0%|
|69	|112.0%	|106.2%	|95.2%	|90.0%|
|70	|114.0%	|106.8%	|97.8%	|91.0%|
|71	|116.0%	|107.4%	|100.4%	|92.0%|
|72	|118.0%	|108.0%	|103.0%	|93.0%|
|73	|119.4%	|108.0%	|104.4%	|94.0%|
|74	|120.8%	|108.0%	|105.8%	|95.0%|
|75	|122.2%	|108.0%	|107.2%	|96.0%|
|76	|123.6%	|108.0%	|108.6%	|97.0%|
|77	|125.0%	|108.0%	|110.0%	|98.0%|
|78	|123.6%	|108.0%	|110.0%	|99.0%|
|79	|122.2%	|108.0%	|110.0%	|100.0%|
|80	|120.8%	|108.0%	|110.0%	|101.0%|
|81	|119.4%	|108.0%	|110.0%	|102.0%|
|82	|118.0%	|108.0%	|110.0%	|103.0%|
|83	|116.4%	|108.4%	|110.0%	|104.4%|
|84	|114.8%	|108.8%	|110.0%	|105.8%|
|85	|113.2%	|109.2%	|110.0%	|107.2%|
|86	|111.6%	|109.6%	|110.0%	|108.6%|
|87	|110.0%	|110.0%	|110.0%	|110.0%|
|88	|109.6%	|110.0%	|109.6%	|110.0%|
|89	|109.2%	|110.0%	|109.2%	|110.0%|
|90	|108.8%	|110.0%	|108.8%	|110.0%|
|91	|108.4%	|110.0%	|108.4%	|110.0%|
|92	|108.0%	|110.0%	|108.0%	|110.0%|
|93	|107.8%	|110.0%	|107.8%	|110.0%|
|94	|107.6%	|110.0%	|107.6%	|110.0%|
|95	|107.4%	|110.0%	|107.4%	|110.0%|
|96	|107.2%	|110.0%	|107.2%	|110.0%|
|97	|107.0%	|110.0%	|107.0%	|110.0%|
|98	|106.2%	|109.0%	|106.2%	|109.0%|
|99	|105.4%	|108.0%	|105.4%	|108.0%|
|100	|104.6%	|107.0%	|104.6%	|107.0%|
|101	|103.8%	|106.0%	|103.8%	|106.0%|
|102	|103.0%	|105.0%	|103.0%	|105.0%|
|103	|102.0%	|103.3%	|102.0%	|103.3%|
|104	|101.0%	|101.7%	|101.0%	|101.7%|
|>=105	|100.0%	|100.0%	|100.0%	|100.0%|

- e. 	The mortality assumption used shall be the following: 
    - ii. For Individual Annuity contracts within the Payout Annuity Reserving Category other than Structured Settlement Contracts, the mortality rate for a contract holder age x in year (2012 + n) shall be calculated using the following formula, where qx denotes mortality from the 2012 IAM Basic Mortality Table multiplied by the appropriate factor (Fx) from Table 6.3 and G2x denotes mortality improvement from Projection Scale G2:  
q_x^(2012+n)=q_x^2012 (1-〖G2〗_x )^n*F_x

Table 6.3: Fx for Individual Annuities in Payout Annuity Reserving Category

|Attained Age (x)|Female|Male|
|----------------|------|-----|
|<=50|125.0%|100.0%|
|51|125.0%|100.0%|
|52|125.0%|100.0%|
|53|125.0%|100.0%|
|54|125.0%|100.0%|
|55|125.0%|100.0%|
|56|125.0%|100.0%|
|57|125.0%|100.0%|
|58|120.6%|99.0%|
|59|116.2%|98.0%|
|60|111.8%|97.0%|
|61|107.4%|96.0%|
|62|103.0%|95.0%|
|63|101.0%|95.4%|
|64|99.0%|95.8%|
|65|97.0%|96.2%|
|66|95.0%|96.6%|
|67|93.0%|97.0%|
|68|94.4%|98.6%|
|69|95.8%|100.2%|
|70|97.2%|101.8%|
|71|98.6%|103.4%|
|72|100.0%|105.0%|
|73|101.6%|107.0%|
|74|103.2%|109.0%|
|75|104.8%|111.0%|
|76|106.4%|113.0%|
|77|108.0%|115.0%|
|78|108.0%|116.0%|
|79|108.0%|117.0%|
|80|108.0%|118.0%|
|81|108.0%|119.0%|
|82|108.0%|120.0%|
|83|108.0%|120.0%|
|84|108.0%|120.0%|
|85|108.0%|120.0%|
|86|108.0%|120.0%|
|87|108.0%|120.0%|
|88|109.0%|119.0%|
|89|110.0%|118.0%|
|90|111.0%|117.0%|
|91|112.0%|116.0%|
|92|113.0%|115.0%|
|93|113.0%|115.0%|
|94|113.0%|115.0%|
|95|113.0%|115.0%|
|96|113.0%|115.0%|
|97|113.0%|115.0%|
|98|111.4%|113.0%|
|99|109.8%|111.0%|
|100|108.2%|109.0%|
|101|106.6%|107.0%|
|102|105.0%|105.0%|
|103|103.3%|103.3%|
|104|101.7%|101.7%|
|>=105|100.0%|100.0%|

- e. 	The mortality assumption used shall be the following: 
    - iii. For Structured Settlement contracts for Standard lives, the mortality rate for an annuitant age x in year (2011 + n) shall be calculated using the following formula, where qx denotes mortality from the 1983 IAM Table ‘A’ multiplied by the appropriate factor (Fx) from Table 6.4 and G2x denotes mortality improvement from Projection Scale G2:

q_x^(2011+n)=q_x^2011 (1-〖G2〗_x )^n*F_x

Table 6.4: Fx for Structured Settlement Contracts with Standard lives

|Attained Age|Durations 1 to 5||Durations 6 to 10||Durations >=11||
|---|---|---|---|---|---|---|
||Female|Male|Female|Male|Female|Male|
|<=2|300.0%|300.0%|300.0%|300.0%|365.0%|375.0%|
|3|306.0%|306.0%|307.0%|306.0%|374.0%|381.0%|
|4|312.0%|312.0%|314.0%|312.0%|383.0%|387.0%|
|5|318.0%|318.0%|321.0%|318.0%|392.0%|393.0%|
|6|324.0%|324.0%|328.0%|324.0%|401.0%|399.0%|
|7|330.0%|330.0%|335.0%|330.0%|410.0%|405.0%|
|8|335.0%|330.0%|339.0%|330.0%|415.0%|405.0%|
|9|340.0%|330.0%|343.0%|330.0%|420.0%|405.0%|
|10|345.0%|330.0%|347.0%|330.0%|425.0%|405.0%|
|11|350.0%|330.0%|351.0%|330.0%|430.0%|405.0%|
|12|355.0%|330.0%|355.0%|330.0%|435.0%|405.0%|
|13|355.0%|331.0%|355.0%|331.0%|435.0%|407.0%|
|14|355.0%|332.0%|355.0%|332.0%|435.0%|409.0%|
|15|355.0%|333.0%|355.0%|333.0%|435.0%|411.0%|
|16|355.0%|334.0%|355.0%|334.0%|435.0%|413.0%|
|17|355.0%|335.0%|355.0%|335.0%|435.0%|415.0%|
|18|354.0%|335.0%|354.0%|335.0%|434.0%|414.0%|
|19|353.0%|335.0%|353.0%|335.0%|433.0%|413.0%|
|20|352.0%|335.0%|352.0%|335.0%|432.0%|412.0%|
|21|351.0%|335.0%|351.0%|335.0%|431.0%|411.0%|
|22|350.0%|335.0%|350.0%|335.0%|430.0%|410.0%|
|23|350.0%|338.0%|350.0%|338.0%|429.0%|414.0%|
|24|350.0%|341.0%|350.0%|341.0%|428.0%|418.0%|
|25|350.0%|344.0%|350.0%|344.0%|427.0%|422.0%|
|26|350.0%|347.0%|350.0%|347.0%|426.0%|426.0%|
|27|350.0%|350.0%|350.0%|350.0%|425.0%|430.0%|
|28|355.0%|358.0%|355.0%|358.0%|432.0%|440.0%|
|29|360.0%|366.0%|360.0%|366.0%|439.0%|450.0%|
|30|365.0%|374.0%|365.0%|374.0%|446.0%|460.0%|
|31|370.0%|382.0%|370.0%|382.0%|453.0%|470.0%|
|32|375.0%|390.0%|375.0%|390.0%|460.0%|480.0%|
|33|375.0%|392.0%|375.0%|392.0%|460.0%|482.0%|
|34|375.0%|394.0%|375.0%|394.0%|460.0%|484.0%|
|35|375.0%|396.0%|375.0%|396.0%|460.0%|486.0%|
|36|375.0%|398.0%|375.0%|398.0%|460.0%|488.0%|
|37|375.0%|400.0%|375.0%|400.0%|460.0%|490.0%|
|38|359.0%|387.0%|359.0%|387.0%|444.0%|478.0%|
|39|343.0%|374.0%|343.0%|374.0%|428.0%|466.0%|
|40|327.0%|361.0%|327.0%|361.0%|412.0%|454.0%|
|41|311.0%|348.0%|311.0%|348.0%|396.0%|442.0%|
|42|295.0%|335.0%|295.0%|335.0%|380.0%|430.0%|
|43|278.0%|312.0%|279.0%|312.0%|363.0%|404.0%|
|44|261.0%|289.0%|263.0%|289.0%|346.0%|378.0%|
|45|244.0%|266.0%|247.0%|266.0%|329.0%|352.0%|
|46|227.0%|243.0%|231.0%|243.0%|312.0%|326.0%|
|47|210.0%|220.0%|215.0%|220.0%|295.0%|300.0%|
|48|206.0%|213.0%|210.0%|213.0%|288.0%|291.0%|
|49|202.0%|206.0%|205.0%|206.0%|281.0%|282.0%|
|50|198.0%|199.0%|200.0%|199.0%|274.0%|273.0%|
|51|194.0%|192.0%|195.0%|192.0%|267.0%|264.0%|
|52|190.0%|185.0%|190.0%|185.0%|260.0%|255.0%|
|53|189.0%|185.0%|189.0%|185.0%|258.0%|254.0%|
|54|188.0%|185.0%|188.0%|185.0%|256.0%|253.0%|
|55|187.0%|185.0%|187.0%|185.0%|254.0%|252.0%|
|56|186.0%|185.0%|186.0%|185.0%|252.0%|251.0%|
|57|185.0%|185.0%|185.0%|185.0%|250.0%|250.0%|
|58|179.0%|180.0%|182.0%|183.0%|245.0%|246.0%|
|59|173.0%|175.0%|179.0%|181.0%|240.0%|242.0%|
|60|167.0%|170.0%|176.0%|179.0%|235.0%|238.0%|
|61|161.0%|165.0%|173.0%|177.0%|230.0%|234.0%|
|62|155.0%|160.0%|170.0%|175.0%|225.0%|230.0%|
|63|149.0%|154.0%|166.0%|172.0%|218.0%|224.0%|
|64|143.0%|148.0%|162.0%|169.0%|211.0%|218.0%|
|65|137.0%|142.0%|158.0%|166.0%|204.0%|212.0%|
|66|131.0%|136.0%|154.0%|163.0%|197.0%|206.0%|
|67|125.0%|130.0%|150.0%|160.0%|190.0%|200.0%|
|68|123.0%|128.0%|149.0%|158.0%|184.0%|193.0%|
|69|121.0%|126.0%|148.0%|156.0%|178.0%|186.0%|
|70|119.0%|124.0%|147.0%|154.0%|172.0%|179.0%|
|71|117.0%|122.0%|146.0%|152.0%|166.0%|172.0%|
|72|115.0%|120.0%|145.0%|150.0%|160.0%|165.0%|
|73|114.0%|118.0%|143.0%|148.0%|156.0%|161.0%|
|74|113.0%|116.0%|141.0%|146.0%|152.0%|157.0%|
|75|112.0%|114.0%|139.0%|144.0%|148.0%|153.0%|
|76|111.0%|112.0%|137.0%|142.0%|144.0%|149.0%|
|77|110.0%|110.0%|135.0%|140.0%|140.0%|145.0%|
|78|110.0%|110.0%|133.0%|137.0%|137.0%|141.0%|
|79|110.0%|110.0%|131.0%|134.0%|134.0%|137.0%|
|80|110.0%|110.0%|129.0%|131.0%|131.0%|133.0%|
|81|110.0%|110.0%|127.0%|128.0%|128.0%|129.0%|
|82|110.0%|110.0%|125.0%|125.0%|125.0%|125.0%|
|83|110.0%|110.0%|123.0%|123.0%|123.0%|123.0%|
|84|110.0%|110.0%|121.0%|121.0%|121.0%|121.0%|
|85|110.0%|110.0%|119.0%|119.0%|119.0%|119.0%|
|86|110.0%|110.0%|117.0%|117.0%|117.0%|117.0%|
|87|110.0%|110.0%|115.0%|115.0%|115.0%|115.0%|
|88|110.0%|110.0%|114.0%|114.0%|114.0%|114.0%|
|89|110.0%|110.0%|113.0%|113.0%|113.0%|113.0%|
|90|110.0%|110.0%|112.0%|112.0%|112.0%|112.0%|
|91|110.0%|110.0%|111.0%|111.0%|111.0%|111.0%|
|92|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|
|93|109.0%|109.0%|109.0%|109.0%|109.0%|109.0%|
|94|108.0%|108.0%|108.0%|108.0%|108.0%|108.0%|
|95|107.0%|107.0%|107.0%|107.0%|107.0%|107.0%|
|96|106.0%|106.0%|106.0%|106.0%|106.0%|106.0%|
|97|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|
|98|104.0%|104.0%|104.0%|104.0%|104.0%|104.0%|
|99|103.0%|103.0%|103.0%|103.0%|103.0%|103.0%|
|100|102.0%|102.0%|102.0%|102.0%|102.0%|102.0%|
|101|101.0%|101.0%|101.0%|101.0%|101.0%|101.0%|
|102|100.0%|100.0%|100.0%|100.0%|100.0%|100.0%|
|103|100.0%|100.0%|100.0%|100.0%|100.0%|100.0%|
|104|100.0%|100.0%|100.0%|100.0%|100.0%|100.0%|
|>=105|100.0%|100.0%|100.0%|100.0%|100.0%|100.0%|


Substandard lives shall use the mortality formula and terms described above for Standard lives, with such mortality reflecting the inclusion of the “Constant Extra Death” (CED) methodology described in Actuarial Guideline IX-A.  The CED shall be applied prior to the application of multiplicative Fx factor. The factors for Substandard lives differ by the extent of the age rate-up, and are as follows in Tables 6.5 and 6.6:

Table 6.5: Fx for Structured Settlement Contracts for Substandard lives with age rate-ups of 1-20 years

Here is the markdown table for the given data:

|Attained Age|Durations 1 to 10||Durations 11 to 20||Durations 21 to 30||Durations >=31||
|---|---|---|---|---|---|---|---|---|
||Female|Male|Female|Male|Female|Male|Female|Male|
|<=2|55.0%|55.0%|55.0%|55.0%|55.0%|55.0%|55.0%|55.0%|
|3|57.0%|57.0%|57.0%|57.0%|57.0%|57.0%|57.0%|57.0%|
|4|59.0%|59.0%|59.0%|59.0%|59.0%|59.0%|59.0%|59.0%|
|5|61.0%|61.0%|61.0%|61.0%|61.0%|61.0%|61.0%|61.0%|
|6|63.0%|63.0%|63.0%|63.0%|63.0%|63.0%|63.0%|63.0%|
|7|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|8|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|9|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|10|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|11|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|12|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|13|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|14|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|15|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|16|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|17|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|18|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|19|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|20|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|21|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|22|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|23|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|24|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|25|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|26|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|27|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|65.0%|
|28|66.0%|67.0%|66.0%|67.0%|66.0%|67.0%|66.0%|67.0%|
|29|67.0%|69.0%|67.0%|69.0%|67.0%|69.0%|67.0%|69.0%|
|30|68.0%|71.0%|68.0%|71.0%|68.0%|71.0%|68.0%|71.0%|
|31|69.0%|73.0%|69.0%|73.0%|69.0%|73.0%|69.0%|73.0%|
|32|70.0%|75.0%|70.0%|75.0%|70.0%|75.0%|70.0%|75.0%|
|33|71.0%|75.0%|71.0%|76.0%|72.0%|77.0%|72.0%|77.0%|
|34|72.0%|75.0%|72.0%|77.0%|74.0%|79.0%|74.0%|79.0%|
|35|73.0%|75.0%|73.0%|78.0%|76.0%|81.0%|76.0%|81.0%|
|36|74.0%|75.0%|74.0%|79.0%|78.0%|83.0%|78.0%|83.0%|
|37|75.0%|75.0%|75.0%|80.0%|80.0%|85.0%|80.0%|85.0%|
|38|75.0%|77.0%|81.0%|88.0%|90.0%|98.0%|93.0%|101.0%|
|39|75.0%|79.0%|87.0%|96.0%|100.0%|111.0%|106.0%|117.0%|
|40|75.0%|81.0%|93.0%|104.0%|110.0%|124.0%|119.0%|133.0%|
|41|75.0%|83.0%|99.0%|112.0%|120.0%|137.0%|132.0%|149.0%|
|42|75.0%|85.0%|105.0%|120.0%|130.0%|150.0%|145.0%|165.0%|
|43|75.0%|84.0%|107.0%|119.0%|134.0%|150.0%|149.0%|165.0%|
|44|75.0%|83.0%|109.0%|118.0%|138.0%|150.0%|153.0%|165.0%|
|45|75.0%|82.0%|111.0%|117.0%|142.0%|150.0%|157.0%|165.0%|
|46|75.0%|81.0%|113.0%|116.0%|146.0%|150.0%|161.0%|165.0%|
|47|75.0%|80.0%|115.0%|115.0%|150.0%|150.0%|165.0%|165.0%|
|48|76.0%|80.0%|116.0%|115.0%|150.0%|150.0%|166.0%|165.0%|
|49|77.0%|80.0%|117.0%|115.0%|150.0%|150.0%|167.0%|165.0%|
|50|78.0%|80.0%|118.0%|115.0%|150.0%|150.0%|168.0%|165.0%|
|51|79.0%|80.0%|119.0%|115.0%|150.0%|150.0%|169.0%|165.0%|
|52|80.0%|80.0%|120.0%|115.0%|150.0%|150.0%|170.0%|165.0%|
|53|82.0%|82.0%|123.0%|119.0%|155.0%|154.0%|174.0%|170.0%|
|54|84.0%|84.0%|126.0%|123.0%|160.0%|158.0%|178.0%|175.0%|
|55|86.0%|86.0%|129.0%|127.0%|165.0%|162.0%|182.0%|180.0%|
|56|88.0%|88.0%|132.0%|131.0%|170.0%|166.0%|186.0%|185.0%|
|57|90.0%|90.0%|135.0%|135.0%|175.0%|170.0%|190.0%|190.0%|
|58|90.0%|91.0%|135.0%|136.0%|175.0%|172.0%|191.0%|192.0%|
|59|90.0%|92.0%|135.0%|137.0%|175.0%|174.0%|192.0%|194.0%|
|60|90.0%|93.0%|135.0%|138.0%|175.0%|176.0%|193.0%|196.0%|
|61|90.0%|94.0%|135.0%|139.0%|175.0%|178.0%|194.0%|198.0%|
|62|90.0%|95.0%|135.0%|140.0%|175.0%|180.0%|195.0%|200.0%|
|63|89.0%|94.0%|133.0%|138.0%|172.0%|178.0%|192.0%|198.0%|
|64|88.0%|93.0%|131.0%|136.0%|169.0%|176.0%|189.0%|196.0%|
|65|87.0%|92.0%|129.0%|134.0%|166.0%|174.0%|186.0%|194.0%|
|66|86.0%|91.0%|127.0%|132.0%|163.0%|172.0%|183.0%|192.0%|
|67|85.0%|90.0%|125.0%|130.0%|160.0%|170.0%|180.0%|190.0%|
|68|84.0%|89.0%|124.0%|129.0%|159.0%|168.0%|178.0%|188.0%|
|69|83.0%|88.0%|123.0%|128.0%|158.0%|166.0%|176.0%|186.0%|
|70|82.0%|87.0%|122.0%|127.0%|157.0%|164.0%|174.0%|184.0%|
|71|81.0%|86.0%|121.0%|126.0%|156.0%|162.0%|172.0%|182.0%|
|72|80.0%|85.0%|120.0%|125.0%|155.0%|160.0%|170.0%|180.0%|
|73|80.0%|85.0%|119.0%|124.0%|153.0%|158.0%|168.0%|177.0%|
|74|80.0%|85.0%|118.0%|123.0%|151.0%|156.0%|166.0%|174.0%|
|75|80.0%|85.0%|117.0%|122.0%|149.0%|154.0%|164.0%|171.0%|
|76|80.0%|85.0%|116.0%|121.0%|147.0%|152.0%|162.0%|168.0%|
|77|80.0%|85.0%|115.0%|120.0%|145.0%|150.0%|160.0%|165.0%|
|78|84.0%|88.0%|114.0%|118.0%|140.0%|144.0%|153.0%|157.0%|
|79|88.0%|91.0%|113.0%|116.0%|135.0%|138.0%|146.0%|149.0%|
|80|92.0%|94.0%|112.0%|114.0%|130.0%|132.0%|139.0%|141.0%|
|81|96.0%|97.0%|111.0%|112.0%|125.0%|126.0%|132.0%|133.0%|
|82|100.0%|100.0%|110.0%|110.0%|120.0%|120.0%|125.0%|125.0%|
|83|102.0%|102.0%|110.0%|110.0%|118.0%|118.0%|122.0%|122.0%|
|84|104.0%|104.0%|110.0%|110.0%|116.0%|116.0%|119.0%|119.0%|
|85|106.0%|106.0%|110.0%|110.0%|114.0%|114.0%|116.0%|116.0%|
|86|108.0%|108.0%|110.0%|110.0%|112.0%|112.0%|113.0%|113.0%|
|87|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|
|88|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|
|89|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|
|90|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|
|91|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|
|92|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|110.0%|
|93|109.0%|109.0%|109.0%|109.0%|109.0%|109.0%|109.0%|109.0%|
|94|108.0%|108.0%|108.0%|108.0%|108.0%|108.0%|108.0%|108.0%|
|95|107.0%|107.0%|107.0%|107.0%|107.0%|107.0%|107.0%|107.0%|
|96|106.0%|106.0%|106.0%|106.0%|106.0%|106.0%|106.0%|106.0%|
|97|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|
|98|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|
|99|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|
|100|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|
|101|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|
|102|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|105.0%|
|103|103.3%|103.3%|103.3%|103.3%|103.3%|103.3%|103.3%|103.3%|
|104|101.7%|101.7%|101.7%|101.7%|101.7%|101.7%|101.7%|101.7%|
|>=105|100.0%|100.0%|100.0%|100.0%|100.0%|100.0%|100.0%|100.0%|


Table 6.6: Fx for Structured Settlement Contracts for Substandard lives with age rate-ups of >=21 years

Here is the markdown table for the given data:

|Attained Age|Structured Settlements – Substandard Lives, Rate-Ups >=21 Years||||||||
|---|---|---|---|---|---|---|---|---|
||Durations 1 to 10||Durations 11 to 20||Durations 21 to 30||Durations >=31||
||Female|Male|Female|Male|Female|Male|Female|Male|
|<=2|55.0%|55.0%|55.0%|55.0%|70.0%|75.0%|70.0%|70.0%|
|3|57.0%|57.0%|57.0%|57.0%|72.0%|76.0%|72.0%|72.0%|
|4|59.0%|59.0%|59.0%|59.0%|74.0%|77.0%|74.0%|74.0%|
|5|61.0%|61.0%|61.0%|61.0%|76.0%|78.0%|76.0%|76.0%|
|6|63.0%|63.0%|63.0%|63.0%|78.0%|79.0%|78.0%|78.0%|
|7|65.0%|65.0%|65.0%|65.0%|80.0%|80.0%|80.0%|80.0%|
|8|65.0%|65.0%|65.0%|65.0%|81.0%|80.0%|81.0%|80.0%|
|9|65.0%|65.0%|65.0%|65.0%|82.0%|80.0%|82.0%|80.0%|
|10|65.0%|65.0%|65.0%|65.0%|83.0%|80.0%|83.0%|80.0%|
|11|65.0%|65.0%|65.0%|65.0%|84.0%|80.0%|84.0%|80.0%|
|12|65.0%|65.0%|65.0%|65.0%|85.0%|80.0%|85.0%|80.0%|
|13|65.0%|65.0%|65.0%|65.0%|85.0%|80.0%|85.0%|80.0%|
|14|65.0%|65.0%|65.0%|65.0%|85.0%|80.0%|85.0%|80.0%|
|15|65.0%|65.0%|65.0%|65.0%|85.0%|80.0%|85.0%|80.0%|
|16|65.0%|65.0%|65.0%|65.0%|85.0%|80.0%|85.0%|80.0%|
|17|65.0%|65.0%|65.0%|65.0%|85.0%|80.0%|85.0%|80.0%|
|18|65.0%|65.0%|65.0%|65.0%|85.0%|80.0%|85.0%|80.0%|
|19|65.0%|65.0%|65.0%|65.0%|85.0%|80.0%|85.0%|80.0%|
|20|65.0%|65.0%|65.0%|65.0%|85.0%|80.0%|85.0%|80.0%|
|21|65.0%|65.0%|65.0%|65.0%|85.0%|80.0%|85.0%|80.0%|
|22|65.0%|65.0%|65.0%|65.0%|85.0%|80.0%|85.0%|80.0%|
|23|65.0%|65.0%|65.0%|65.0%|85.0%|81.0%|85.0%|81.0%|
|24|65.0%|65.0%|65.0%|65.0%|85.0%|82.0%|85.0%|82.0%|
|25|65.0%|65.0%|65.0%|65.0%|85.0%|83.0%|85.0%|83.0%|
|26|65.0%|65.0%|65.0%|65.0%|85.0%|84.0%|85.0%|84.0%|
|27|65.0%|65.0%|65.0%|65.0%|85.0%|85.0%|85.0%|85.0%|
|28|66.0%|67.0%|66.0%|67.0%|86.0%|87.0%|86.0%|87.0%|
|29|67.0%|69.0%|67.0%|69.0%|87.0%|89.0%|87.0%|89.0%|
|30|68.0%|71.0%|68.0%|71.0%|88.0%|91.0%|88.0%|91.0%|
|31|69.0%|73.0%|69.0%|73.0%|89.0%|93.0%|89.0%|93.0%|
|32|70.0%|75.0%|70.0%|75.0%|90.0%|95.0%|90.0%|95.0%|
|33|71.0%|76.0%|71.0%|76.0%|91.0%|96.0%|92.0%|97.0%|
|34|72.0%|77.0%|72.0%|77.0%|92.0%|97.0%|94.0%|99.0%|
|35|73.0%|78.0%|73.0%|78.0%|93.0%|98.0%|96.0%|101.0%|
|36|74.0%|79.0%|74.0%|79.0%|94.0%|99.0%|98.0%|103.0%|
|37|75.0%|80.0%|75.0%|80.0%|95.0%|100.0%|100.0%|105.0%|
|38|77.0%|83.0%|79.0%|85.0%|98.0%|105.0%|107.0%|115.0%|
|39|79.0%|86.0%|83.0%|90.0%|101.0%|110.0%|114.0%|125.0%|
|40|81.0%|89.0%|87.0%|95.0%|104.0%|115.0%|121.0%|135.0%|
|41|83.0%|92.0%|91.0%|100.0%|107.0%|120.0%|128.0%|145.0%|
|42|85.0%|95.0%|95.0%|105.0%|110.0%|125.0%|135.0%|155.0%|
|43|85.0%|94.0%|96.0%|104.0%|111.0%|123.0%|137.0%|154.0%|
|44|85.0%|93.0%|97.0%|103.0%|112.0%|121.0%|139.0%|153.0%|
|45|85.0%|92.0%|98.0%|102.0%|113.0%|119.0%|141.0%|152.0%|
|46|85.0%|91.0%|99.0%|101.0%|114.0%|117.0%|143.0%|151.0%|
|47|85.0%|90.0%|100.0%|100.0%|115.0%|115.0%|145.0%|150.0%|
|48|86.0%|90.0%|100.0%|100.0%|116.0%|115.0%|146.0%|150.0%|
|49|87.0%|90.0%|100.0%|100.0%|117.0%|115.0%|147.0%|150.0%|
|50|88.0%|90.0%|100.0%|100.0%|118.0%|115.0%|148.0%|150.0%|
|51|89.0%|90.0%|100.0%|100.0%|119.0%|115.0%|149.0%|150.0%|
|52|90.0%|90.0%|100.0%|100.0%|120.0%|115.0%|150.0%|150.0%|
|53|92.0%|92.0%|103.0%|103.0%|123.0%|119.0%|155.0%|154.0%|
|54|94.0%|94.0%|106.0%|106.0%|126.0%|123.0%|160.0%|158.0%|
|55|96.0%|96.0%|109.0%|109.0%|129.0%|127.0%|165.0%|162.0%|
|56|98.0%|98.0%|112.0%|112.0%|132.0%|131.0%|170.0%|166.0%|
|57|100.0%|100.0%|115.0%|115.0%|135.0%|135.0%|175.0%|170.0%|
|58|101.0%|101.0%|115.0%|116.0%|135.0%|136.0%|175.0%|172.0%|
|59|102.0%|102.0%|115.0%|117.0%|135.0%|137.0%|175.0%|174.0%|
|60|103.0%|103.0%|115.0%|118.0%|135.0%|138.0%|175.0%|176.0%|
|61|104.0%|104.0%|115.0%|119.0%|135.0%|139.0%|175.0%|178.0%|
|62|105.0%|105.0%|115.0%|120.0%|135.0%|140.0%|175.0%|180.0%|
|63|103.0%|104.0%|114.0%|118.0%|133.0%|138.0%|172.0%|178.0%|
|64|101.0%|103.0%|113.0%|116.0%|131.0%|136.0%|169.0%|176.0%|
|65|99.0%|102.0%|112.0%|114.0%|129.0%|134.0%|166.0%|174.0%|
|66|97.0%|101.0%|111.0%|112.0%|127.0%|132.0%|163.0%|172.0%|
|67|95.0%|100.0%|110.0%|110.0%|125.0%|130.0%|160.0%|170.0%|
|68|94.0%|99.0%|109.0%|109.0%|124.0%|129.0%|159.0%|168.0%|
|69|93.0%|98.0%|108.0%|108.0%|123.0%|128.0%|158.0%|166.0%|
|70|92.0%|97.0%|107.0%|107.0%|122.0%|127.0%|157.0%|164.0%|
|71|91.0%|96.0%|106.0%|106.0%|121.0%|126.0%|156.0%|162.0%|
|72|90.0%|95.0%|105.0%|105.0%|120.0%|125.0%|155.0%|160.0%|
|73|90.0%|94.0%|104.0%|104.0%|119.0%|124.0%|153.0%|158.0%|
|74|90.0%|93.0%|103.0%|103.0%|118.0%|123.0%|151.0%|156.0%|
|75|90.0%|92.0%|102.0%|102.0%|117.0%|122.0%|149.0%|154.0%|
|76|90.0%|91.0%|101.0%|101.0%|116.0%|121.0%|147.0%|152.0%|
|77|90.0%|90.0%|100.0%|100.0%|115.0%|120.0%|145.0%|150.0%|
|78|90.0%|90.0%|99.0%|99.0%|112.0%|116.0%|138.0%|142.0%|
|79|90.0%|90.0%|98.0%|98.0%|109.0%|112.0%|131.0%|134.0%|
|80|90.0%|90.0%|97.0%|97.0%|106.0%|108.0%|124.0%|126.0%|
|81|90.0%|90.0%|96.0%|96.0%|103.0%|104.0%|117.0%|118.0%|
|82|90.0%|90.0%|95.0%|95.0%|100.0%|100.0%|110.0%|110.0%|
|83|91.0%|91.0%|95.0%|95.0%|99.0%|99.0%|107.0%|107.0%|
|84|92.0%|92.0%|95.0%|95.0%|98.0%|98.0%|104.0%|104.0%|
|85|93.0%|93.0%|95.0%|95.0%|97.0%|97.0%|101.0%|101.0%|
|86|94.0%|94.0%|95.0%|95.0%|96.0%|96.0%|98.0%|98.0%|
|87|95.0%|95.0%|95.0%|95.0%|95.0%|95.0%|95.0%|95.0%|
|88|94.0%|94.0%|94.0%|94.0%|94.0%|94.0%|94.0%|94.0%|
|89|93.0%|93.0%|93.0%|93.0%|93.0%|93.0%|93.0%|93.0%|
|90|92.0%|92.0%|92.0%|92.0%|92.0%|92.0%|92.0%|92.0%|
|91|91.0%|91.0%|91.0%|91.0%|91.0%|91.0%|91.0%|91.0%|
|92|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|
|93|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|
|94|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|
|95|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|
|96|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|
|97|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|
|98|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|
|99|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|
|100|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|
|101|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|
|102|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|90.0%|
|103|93.3%|93.3%|93.3%|93.3%|93.3%|93.3%|93.3%|93.3%|
|104|96.7%|96.7%|96.7%|96.7%|96.7%|96.7%|96.7%|96.7%|
|>=105|100.0%|100.0%|100.0%|100.0%|100.0%|100.0%|100.0%|100.0%|


Group annuities (except for those contracts owned or purchased by retirement plans, which are covered immediately below), international business, and contracts within the Longevity Reinsurance Reserving Category shall use the lower of the 1994 GAM Table with Projection Scale AA applied to the valuation date and the company’s prudent estimate assumptions. The company prudent estimate assumptions for group annuities, international business, and contracts within the Longevity Reinsurance Reserving Category shall be developed separately from each other as appropriate.  

> Guidance Note: For certain Group Annuity and Longevity Reinsurance contracts, a single contract may contain annuitants drawn from multiple underlying sub-populations with materially different mortality characteristics (e.g., due to differences in geography, plan composition, industry collar, socioeconomic profile, etc.). For contracts containing multiple underlying sub-populations, both i.) the determination of prudent estimate assumptions and ii.) the comparison between the mortality rates under the company’s prudent estimate assumptions and under the prescribed table should be performed at a level of granularity that recognizes these material differences and that is at least as granular as the company uses for its own internal assumption development purposes (e.g., the level of granularity used when pricing the business or when periodically re-determining the company’s internal mortality assumptions).   
For example, if a Longevity Reinsurance contract contains annuitants drawn from two underlying pension plans, one of which is predominantly blue collar and lower income and the other of which is predominantly white collar and higher income, the prudent estimate assumptions should be determined separately for each of the two plans (or at a greater level of granularity if consistent with company practice), and the comparison between the company's prudent estimate assumptions and the prescribed table should be performed at either the individual annuitant level or at the plan level as opposed to the contract level.

- e. 	The mortality assumption used shall be the following:
    - iv. Group Annuities owned or purchased by retirement plans (as defined in the NAIC Model 820 – Standard Valuation Law) use the following mortality tables:  
PRI-2012 Private Retirement Plans Amount-Weighted Mortality Rates Table excluding the Upper and Lower Quartile Tables with the latest MP Scale (MP-2021 as of Jan 2023)

PRI-2012 for Blue Collar, White Collar, or Total* (mix of blue and white collar) Mortality Table can be used. Justification for the selection of the mortality table should be provided. 

*PRI-2012 Total Tables may not be appropriate for a company’s given group of annuitants if the assumed mix of blue/white collar annuitants is not consistent with the company’s annuitants.

> Guidance Note: Each company should use the most granular data available to it when assigning annuitants to the appropriate collar tables. In some cases, information on the annuitant collar, union status, hourly vs. salaries status, etc. may be available (e.g., from the contract pricing process) at the individual annuitant level. In other cases, information may be available only at the plan-level. Acknowledging that each company will face unique data availability, quality, and storage challenges unique to both their mix of business and system capabilities, companies should use reasonable efforts to acquire, store, and utilize available information in the collar assignment process.   
Annuitants classified as either “hourly waged earners” or “belonging to a union” can be considered “blue collar”; annuitants classified as either “salaried wage earner” or “no union affiliation” can be considered “white collar”.  All participants in a given plan may be classified as blue or white collar if at least 70% of the annuitants with the plan meet the criteria for either “blue collar” or “white collar”.   
If the company cannot determine the collar for a group of annuitants (e.g., because such information was never supplied to the company or because the company did not store such information or cannot use it in its valuation process), then the company should use the Total table.

Retirement tables should be used for in-pay annuities (retired annuitants) and Employee tables should be used for deferred annuities (active or term-vested annuitants).

Contingent survivor tables should be used for beneficiaries to the extent that beneficiaries can be identified, or the base tables should be weighted based on Company expectation of proportion of benefits associated with beneficiaries. Group Structured Settlement contracts use the mortality table consistent with the Individual Structured Settlement Mortality Assumptions (6.C.3.e).

- e. 	The mortality assumption used shall be the following:
    - v. Other Group Annuities use Individual Mortality Assumptions

> Guidance Note: The above tables include implicit historical mortality improvement until Dec 31, 2021. Projecting mortality to a specific date rather than the valuation date in the above step is a practical expedient to streamline calculations. This date should be considered an experience assumption to be periodically reviewed and updated as the Life Actuarial (A) Task Force reviews and updates the assumptions used in the Standard Projection.

- f. 	The discount rate used shall be the 10-year Treasury Department bond rate on the valuation date unless otherwise specified in a subsequent subsection of Section 6.C.3.

### 4.	Partial Withdrawals
Partial withdrawals required contractually or previously elected (e.g., a contract operating under an automatic withdrawal provision, or that has voluntarily enrolled in an automatic withdrawal program, on the valuation date) are to be deducted from the Account Value in each projection interval consistent with the projection frequency used, as described in Section 4.F, and according to the terms of the contract. However, if a GMWB contract’s automatic withdrawals results in partial withdrawal amounts in excess of the GMWB’s guaranteed maximum annual withdrawal amount, such automatic withdrawals shall be revised such that they equal the GMWB’s guaranteed maximum annual withdrawal amount. However, for tax qualified contracts with ages greater than or equal to the federal required minimum distribution (RMD) age, if the prescribed withdrawal amount is below the RMD amount, the withdrawal amount may be reset to the RMD amount. 

> Guidance Note: Companies are expected to model withdrawal amounts consistent with the RMD amount where applicable and where practically feasible; however, it is understood that this level of modeling sophistication may not be available for all companies. 

For any contract not on an automatic withdrawal provision as described in the preceding paragraph, depending on the guaranteed benefit type, other partial withdrawals shall be projected as follows but shall not exceed the free partial withdrawal amount above which surrender charges are incurred and may be floored at the RMD amount for tax qualified contracts with ages greater than or equal to the federal RMD age:

- a. 	For contracts in the Accumulation Reserving Category either without a guaranteed living benefit or prior to exercising a guaranteed living benefit, the partial withdrawal amount each year shall equal the following percentages of account value, based on the contract holder’s attained age: 

Table 6.5: Partial Withdrawals for Accumulation Reserving Category Contracts – Qualified 

|Attained Age|Contracts without GLBs|Contracts with GLBs prior to exercising|Contracts with GLBs after exercising and ITM ≤ 125%|Contracts with GLBs after exercising and ITM > 125%|
|------------|----------------------|----------------------------------------|---------------------------------------------------|--------------------------------------------------|
|59 and under|1.65%                 |0.95%                                   |0.75%                                             |0.75%                                            |
|60 – 64     |2.10%                 |1.15%                                   |5.00%                                             |8.25%                                            |
|65 – 69     |2.35%                 |1.40%                                   |14.50%                                            |21.50%                                           |
|70 – 74     |3.95%                 |2.70%                                   |25.00%                                            |36.75%                                           |
|75 – 79     |4.80%                 |4.30%                                   |29.50%                                            |43.50%                                           |
|80 and over |6.30%                 |5.80%                                   |29.50%                                            |43.50%                                           |

Table 6.6: Partial Withdrawals for Accumulation Reserving Category Contracts – Non-Qualified 

|Attained Age|Contracts without GLBs|Contracts with GLBs prior to exercising|Contracts with GLBs after exercising and ITM ≤ 125%|Contracts with GLBs after exercising and ITM > 125%|
|------------|----------------------|----------------------------------------|---------------------------------------------------|--------------------------------------------------|
|59 and under|1.60%                 |1.15%                                   |1.00%                                             |1.25%                                            |
|60 – 64     |1.60%                 |1.15%                                   |5.25%                                             |9.25%                                            |
|65 – 69     |1.60%                 |1.15%                                   |13.25%                                            |20.50%                                           |
|70 – 74     |1.60%                 |1.65%                                   |20.00%                                            |28.75%                                           |
|75 – 79     |1.60%                 |1.65%                                   |22.50%                                            |34.50%                                           |
|80 and over |1.60%                 |1.65%                                   |22.50%                                            |34.50%                                           |

𝐼𝑇𝑀 = GAPV ÷ 𝐴𝑐𝑐𝑜𝑢𝑛𝑡 𝑉𝑎𝑙𝑢𝑒


- b. 	For contracts in the Accumulation Reserving Category with a guaranteed living benefit and an account value of zero, the partial withdrawal amount shall be the guaranteed maximum withdrawal amount.

- c. 	For contracts in the Accumulation Reserving Category with lifetime guaranteed living benefits that, in the contract year immediately preceding that during the valuation date, withdrew a non-zero amount not in excess of the guaranteed living benefit’s guaranteed annual withdrawal amount, the partial withdrawal amount shall be  the guaranteed maximum annual withdrawal amount each year until the contract Account Value reaches zero.

- d. 	For other contracts in the Accumulation Reserving Category with lifetime guaranteed living benefits, partial withdrawals shall be projected to commence pursuant to the company’s own prudent best estimate assumptions, but ensuring that, at a minimum, guaranteed living benefit utilization rates in aggregate, measured by benefit base under the scenario that produces the scenario reserve that is closest to the CTE70 amount, are at least as high as the utilization rates shown in the table below. Once guaranteed living benefit withdrawals are projected to commence, the partial withdrawal amount shall be 100% of the guaranteed annual withdrawal amount each year until the contract’s account value reaches zero.

Table 6.8: Utilization Assumptions for Accumulation Reserving Category Contracts with Lifetime Benefits

|Qualification Status|Before 65|65 to 70|71 to 75|76 and above|
|--------------------|---------|--------|--------|------------|
|Qualified           |12%      |20%     |30%     |35%         |
|Non-Qualified       |15%      |40%     |80%     |95%         |

- e. 	For contracts in the Accumulation Reserving Category with Non-lifetime guaranteed living benefits that, in the contract year immediately preceding that during the valuation date, withdrew a non-zero amount not in excess of the guaranteed living benefits annual withdrawal amount, the partial withdrawal amount shall be 70% of the guaranteed living benefits guaranteed annual withdrawal amount each year until the contract Account Value reaches zero.

- f. 	For contracts in the Accumulation Reserving Category with Non-lifetime guaranteed living benefits, partial withdrawals shall be projected to commence pursuant to the Company’s own prudent best estimate assumptions, but ensuring that, at a minimum, guaranteed living benefit utilization rates in aggregate, measured by benefit base under the scenario that produces a scenario reserve closest to the CTE70 amount, are at least as high as the utilization rates shown in the table below. Once guaranteed living benefit withdrawals are projected to commence, the partial withdrawal amount shall be 70% of the guaranteed annual withdrawal amount each year until the contract’s account value reaches zero. 

Table 6.9: Utilization Assumptions for Accumulation Reserving Category Contracts with Non-Lifetime Benefits

|Qualification Status|Before 65|65 to 70|71 to 75|76 and above|
|--------------------|---------|--------|--------|------------|
|Qualified           |12%      |20%     |30%     |35%         |
|Non-Qualified       |15%      |40%     |80%     |95%         |

- g. 	For contracts with no minimum guaranteed benefits, the partial withdrawal amount each year shall equal 3.5% of the Account Value.

- h. 	There may be instances where the company has certain data limitations, (e.g., with respect to policies that are not enrolled in an automatic withdrawal program but have exercised a non-excess withdrawal in the contract year immediately preceding the valuation date. The company may employ an appropriate proxy method if it does not result in a material understatement of the reserve.

- i.	For contracts that do not offer withdrawal benefits, such as some contracts within the Payout Annuity Reserving Category and Longevity Reinsurance Reserving Category, this section is not applicable.   

### 5.	Full Surrenders
For contracts that offer surrender benefits, base lapse and full surrender rates shall be dynamically adjusted upward (or downward) when the actual credited rate is below (or above) the competitor rate. For contracts with a guaranteed living benefit, base lapse and full surrender rates shall be further adjusted based on the ITM of the rider value. The following formula shall be used:  

𝑇𝑜𝑡𝑎𝑙 Lapse = (𝐵𝑎𝑠𝑒 𝐿𝑎𝑝𝑠𝑒 x GMIR Factor + 𝑅𝑎𝑡𝑒 𝐹𝑎𝑐𝑡𝑜𝑟 x MVA Factor) × 𝐼𝑇𝑀 𝐹𝑎𝑐𝑡𝑜𝑟 

where:  
- ITM Factor  
𝐼𝑇𝑀 𝐹𝑎𝑐𝑡𝑜𝑟 = 1 				if ITM ≤ 1.25 and AV ≠ 0  
𝐼𝑇𝑀 𝐹𝑎𝑐𝑡𝑜𝑟 = (1.25 ÷ 𝐼𝑇𝑀)² 			if  ITM > 1.25 and AV ≠ 0  
ITM Factor = 0					if AV = 0  
𝐼𝑇𝑀 = GAPV ÷ 𝐴𝑐𝑐𝑜𝑢𝑛𝑡 𝑉𝑎𝑙𝑢𝑒

- Rate Factor  
𝑅𝑎𝑡𝑒 𝐹𝑎𝑐𝑡𝑜𝑟 = 𝑀𝑎𝑟𝑘𝑒𝑡 𝐹𝑎𝑐𝑡𝑜𝑟 × 𝑀𝑎𝑥(0, 1 – 5 × (1-CSV/AV))

- MVA Factor  
MVA Factor = 0 when MVA is in effect; 1 when MVA is not in effect

- GMIR Factor  
For fixed indexed annuities:  
GMIR Factor = None; N/A  
For non-indexed fixed deferred annuities:  
GMIR 𝐹𝑎𝑐𝑡𝑜𝑟 = 1.25 				if GMIR ≤ 1.0%  
GMIR 𝐹𝑎𝑐𝑡𝑜𝑟 = 1.00 				if 1.0% < GMIR ≤ 2.5%  
GMIR Factor = 0.70				if GMIR > 2.5%  

- Market Factor  
𝑀𝑎𝑟𝑘𝑒𝑡 𝐹𝑎𝑐𝑡𝑜𝑟 =  –1.25 × (𝐶𝑅 − 𝑀𝑅)^X		if CR ≥ MR  
M𝑎𝑟𝑘𝑒𝑡 𝐹𝑎𝑐𝑡𝑜𝑟 =  0				if MR > CR ≥ (MR − BF)  
𝑀𝑎𝑟𝑘𝑒𝑡 𝐹𝑎𝑐𝑡𝑜𝑟 =  1.25 × (𝑀𝑅 – 𝐵𝐹 − 𝐶𝑅)^X 	if CR < (MR − BF)  
X = 2.0 during Surrender Charge Period, 2.5 at Shock, and 2.5 thereafter  

- Minimum and Maximum Lapse  
Minimum Lapse = 0.5%  
Maximum Lapse = 90%  

- Crediting Rate (CR)  
CR = the options budget, at the time of the projection (for fixed indexed annuities)  
CR = the crediting rate, at the time of the projection (for non-indexed fixed deferred annuities)  

- Market Rate (MR)  
MR = the market competitor rate at the time of the projection  
For fixed indexed annuities and non-indexed fixed deferred annuities with Interest Guarantee Period < 2 Years:  
MR = Max (3-month Treasury rate, 5-year Treasury rate plus 50% A / 50% AA spread) minus Pricing Spread  
For non-indexed fixed deferred annuities with Interest Guarantee Period ≥ 2 Years:   
MR = N-year Treasury rate plus 50% A / 50% AA spread minus Pricing Spread  
    N = 5-year Treasury rate for 2 years ≤ Interest Guarantee Period < 5 years  
    N = 7-year Treasury rate for 5 years ≤ Interest Guarantee Period < 7 years  
    N = 10-year Treasury rate for Interest Guarantee Period ≥ 7 years  
Pricing Spread = 0% (since already reflected in selection of credit spread)  

- Buffer Factor (BF)  
BF = a buffer factor where dynamic lapses do not occur, 50bps

- Base Lapse  
Base Lapse = Determined using the following tables:

Table 6.9: Base Lapse Rates for Fixed Indexed Annuities with no Guaranteed Living Benefits

|Years Before or After Surrender Charge Expiration|Attained Age||||
|--------------------------------------------------|------------|-------|-------|------------|
||Before 60|60 to 69|70 to 79|80 and above|
|5 yrs or more after expiry|6.5%|7.0%|6.0%|5.0%|
|4 yrs after expiry|8.0%|8.5%|6.5%|5.0%|
|3 yrs after expiry|8.5%|9.5%|7.0%|5.5%|
|2 yrs after expiry|11.0%|12.0%|9.0%|7.0%|
|1 yr after expiry|15.0%|17.5%|13.5%|9.0%|
|Upon expiry|33.5%|41.5%|37.0%|23.5%|
|1 yr to expiry|4.5%|3.5%|4.0%|4.0%|
|2 yrs to expiry|4.0%|3.5%|3.0%|3.0%|
|3 yrs to expiry|2.5%|2.0%|2.0%|2.0%|
|4 yrs to expiry|3.0%|2.5%|2.5%|2.5%|
|5 yrs or more to expiry|2.0%|2.5%|2.0%|1.5%|

Table 6.10: Base Lapse Rates for Non-Indexed Fixed Deferred Annuities with no Guaranteed Living Benefits

|Years Before or After Surrender Charge (SC) Expiration|Interest Guarantee Period (IGP)|||
|------------------------------------------------------|------------------------------|--------------------------------|--------------------------|
||In Years where IGP <= 1 Year*|In Years where IGP > 1 Year, and not in Year of IGP Expiry|In Year of an IGP Expiry after IGP > 1 Year|
|3 yrs or more after expiry|3.0%|2.0%|55.0%|
|2 yrs after expiry|7.5%|2.0%|65.0%|
|1 yr after expiry|10.0%|2.0%|75.0%|
|Upon expiry|25.0%|6.0%|75.0%|
|1 yr to expiry|2.5%|1.0%|70.0%|
|2 yrs to expiry|2.5%|1.0%|70.0%|
|3 yrs or more to expiry|2.5%|1.0%|70.0%|

*includes floating rate structures

> Guidance Note: As an example, for a contract with an initial 3-year IGP and 3-year SC period, and renewing into 1-year IGPs with no SC, the base lapse rates in contract years 1 to 7+ would be 1%, 1%, 1%, 75%, 10%, 7.5%, 3%, etc. 

Table 6.11: Base Lapse Rates for Fixed Annuities with Guaranteed Living Benefits Prior to Utilization

|Surrender Charge Expiration Status and In-the-Moneyness (ITM)|Attained Age||||
|--------------------------------------------------------------|------------|-------|-------|------------|
||Before 60|60 to 69|70 to 79|80 and above|
|Prior to Expiry and ITM of:| | | | |
|Below 100%|2.0%|1.5%|3.5%|5.5%|
|100% to 124%|2.0%|1.5%|1.5%|2.0%|
|125% and over|1.5%|1.0%|1.5%|2.0%|
|At Expiry and ITM of:| | | | |
|Below 100%|91.5%|92.0%|90.0%|81.0%|
|100% to 124%|18.0%|16.0%|15.5%|11.0%|
|125% and over|5.5%|6.0%|7.5%|7.0%|
|After Expiry and ITM of:| | | | |
|Below 100%|69.5%|68.5%|58.5%|44.5%|
|100% to 124%|10.5%|8.0%|7.0%|5.0%|
|125% and over|3.0%|3.5%|4.5%|3.5%|

Table 6.12: Base Lapse Rates for Fixed Annuities with Guaranteed Living Benefits After Utilization

|Surrender Charge Expiration Status and In-the-Moneyness (ITM)|Attained Age||||
|--------------------------------------------------------------|------------|-------|-------|------------|
||Before 60|60 to 69|70 to 79|80 and above|
|Prior to Expiry and ITM of:| | | | |
|Below 100%|1.0%|1.0%|1.0%|5.5%|
|100% to 124%|1.0%|1.0%|1.0%|1.5%|
|125% and over|1.0%|1.0%|1.0%|5.5%|
|At Expiry and ITM of:| | | | |
|Below 100%|9.0%|32.5%|14.0%|0.0%|
|100% to 124%|2.0%|3.0%|2.5%|19.5%|
|125% and over|1.5%|1.0%|1.0%|4.0%|
|After Expiry and ITM of:| | | | |
|Below 100%|3.5%|10.5%|4.5%|0.0%|
|100% to 124%|1.5%|1.0%|1.5%|1.5%|
|125% and over|1.5%|1.0%|1.0%|3.0%|

For contracts in which there is no account value or surrender benefit, such as some contracts within the Payout Annuity Reserving Category and Longevity Reinsurance Reserving Category, this section is not applicable.

### 6.	Annuitizations

- a. The annuitization rate for contracts shall be 0% at all projection intervals. 

### 7.	Index Transfers and Future Deposits
- a.	No transfers between fixed and index strategies or accounts shall be assumed in the projection unless required by the contract (e.g., contractual rights given to the insurer to implement a contractually specified portfolio insurance management strategy). When transfers must be modeled, to the extent not inconsistent with contract language, the allocation of transfers to indices, accounts, or funds must be in proportion to the contract’s current allocation to funds.
- b.	No future deposits to account value shall be assumed unless required by the terms of the contract, in which case they must be modeled. When future deposits must be modeled, to the extent not inconsistent with contract language, the allocation of the deposit to funds must be in proportion to the contract’s current allocation to such funds.

### 8.	Mortality
The following mortality rates shall be used:
- a. Individual annuity contracts within the Accumulation Reserving Category shall use the mortality rates in Section 6.C.3.h.i with Projection Scale G2 mortality improvement factors applied from December 31, 2021 up until each future projection year.

- b. Individual annuity contracts within the Payout Annuity Reserving Category other than Structured Settlement Contracts shall use the mortality rates in Section 6.C.3.h.ii with Projection Scale G2 mortality improvement factors applied from December 31, 2021 up until each future projection year.

- c. Individual Structured Settlement Contracts shall use the mortality rates in Section 6.C.3.h.iii with the following mortality improvement factors applied from December 31, 2021 up until each future projection year.

[Future improvement]

- d. Group annuities, international business, and contracts within the Longevity Reinsurance Category shall use the mortality rates in Section 6.C.3.h.iv with Projection Scale AA mortality improvement factors applied from the valuation date up until each future projection year. However, if the company’s prudent estimate assumption is used in Section 6.C.3.h.iv and already reflects mortality improvement from December 31, 2021 up until the projection year, then Projection Scale AA mortality improvement factors shall not be used.

### 9.	Account Value Depletions  

The following assumptions shall be used when a contract’s Account Value reaches zero:
- a. 	If the contract has a guaranteed living benefit, the contract shall take benefits that are equal in amount each year to the guaranteed maximum annual withdrawal amount.

- b. 	If the contract has any other guaranteed benefits, including a GMDB, the contract shall remain in-force. If the guaranteed benefits contractually terminate upon account value depletion, such termination provisions are assumed to be voided in order to approximate the contract holder’s retaining adequate Account Value to maintain the guaranteed benefits in-force. At the option of the company, fees associated with the contract and guaranteed benefits may continue to be charged and modeled as collected even if the account value has reached zero. While the contract must remain in-force, benefit features may still be terminated according to contractual terms other than account value depletion provisions.

- c. 	If the contract has no minimum guaranteed benefits, the contract should be terminated according to contractual terms.

### 10.	Other Voluntary Contract Terminations  
For contracts that have other elective provisions that allow a contract holder to terminate the contract voluntarily, the termination rate shall be calculated as detailed above in Section 6.C.5 with the following adjustments:
- a. 	If the contract holder is not yet eligible to terminate the contract under the elective provisions, the termination rate shall be zero.

- b. 	After the contract holder becomes eligible to terminate the contract under the elective provisions, the termination rate shall be determined using assumptions in Section 6.C.5.

- c. 	In Section 6.C.5, the ITM of a contract’s guaranteed benefit shall be calculated based on the ratio of the guaranteed benefit’s GAPV to the termination value of the contract. The termination value of the contract shall be calculated as the GAPV of the payment stream that the contract holder is entitled to receive upon termination of the contract; if the contract holder has multiple options for the payment stream, the termination value shall be the highest GAPV of these options.

- d. 	For contracts with guaranteed living benefits, for all contract years in which a withdrawal is projected, the termination rate obtained from Section 6.C.5 shall be additionally multiplied by 60%.

### 11.	Crediting Rates and Investment Spread

- a. This section applies to all contracts that provide crediting rates after initial issuance.

- b. For Fixed Index Annuities, the option budget is the assumed crediting rate for quantifying the investment spread between the net portfolio earned rate and the crediting rate.

- c.	With respect to setting a limit on the annual spread between the net portfolio earned rate and the crediting rate:
   - i.	The maximum annual spread is [2.25%] for policies without an initial bonus.
   - ii.	For policies with an initial bonus of [0.5%], the maximum annual spread is [2.25%] + [0.5%]/SCP during the surrender charge period (SCP). The maximum annual spread is reduced back to [2.25%] after the SCP.
   - iii.	The extra maximum annual spread [0.5%]/SCP allows the insurer to recapture the initial bonus via higher spread during the SCP.

> Drafting Note: The NAIC VM-22 (A) Subgroup expressed openness to hearing any future proposals that address persistency bonuses in the requirements described above to limit the investment spread.

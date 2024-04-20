![](https://cdn.mathpix.com/cropped/2024_03_14_9aa67a64e4af0a42b65bg-1.jpg?height=295&width=586&top_left_y=221&top_left_x=1279)

# DETERMINATION OF DISCOUNT RATES FOR ECONOMIC BALANCE SHEET FRAMEWORK

BERMUDA MONETARY AUTHORITY, July 2015

## Contents
I. BACKGROUND ..... 3
II. DETERMINATION OF DISCOUNT RATES ..... 4
III. STANDARD APPROACH .....  .5
IV. SCENARIO BASED APPROACH .....  6

## I. BACKGROUND

1. The introduction of an Economic Balance Sheet (EBS) approach to the assessment of solvency is a key part of the Bermuda regime for commercial Insurers ${ }^{1}$ and insurance groups. An important component of this process is the determination of the appropriate discount rates. The instructions contained in Schedule XIV of the various Prudential Standards Rules affecting Form 1EBS and Form 4EBS identify the EBS Valuation Principles for Technical Provisions. These principles state that:

a. The valuation shall reflect the time value of money, using a risk free discount rate curve, which may be adjusted to reflect certain risk characteristics of the liability. The Bermuda Monetary Authority (the Authority or BMA) will supply risk free discount curves for a number of the major currencies, and these shall be used where appropriate. However commercial insurers and insurance groups may use alternative risk free curves (e.g. those approved for use in Solvency II) provided they obtain prior approval from the Authority. Details of the approach used for determining the risk free discount rate curves will be directed by the Authority.

b. Commercial insurers and insurance groups will be permitted to include an adjustment to the risk-free discount rate curve to partially reflect the illiquidity premium implicit in typical underlying assets, as well as making allowance for the prevention of pro-cyclical investment behaviour (the 'standard approach'). The Authority will supply discount curves including this adjustment for a number of major currencies, and provide further details of the approach adopted so that commercial insurers and insurance groups can produce rates for other currencies if needed. Details of the approach used for determining the 'standard approach' discount rate curves will be directed by the Authority.

c. Commercial insurers and insurance groups may also elect to adopt the 'scenario based approach' for some or all of their business. This approach is designed to capture both the sensitivity to interest rates and the degree to which assets and liabilities are cash flow matched. It consists of a base scenario using the actual portfolio of assets supporting the business (adjusted for expected default costs) and a range of interest rate stresses to determine the amount by which the market yield should be reduced to reflect interest rate risk and assetliability mismatching. Details of the approach, including the conditions under which it can be adopted will be directed by the Authority.

footnotetext: 1 Commercial Insurers are Class 3A, Class 3B, Class 4, Class C, Class D and Class E insurers.

## II. DETERMINATION OF DISCOUNT RATES

2. Supporting the above Principles, the Authority is using the following method to determine the risk free discount rates:

a. The risk-free yield curve is based on swap rates that are adjusted down by 10bp to reflect credit risk and that are extrapolated to an Ultimate Forward Rate (UFR) at duration 60 and then extended to a duration of 100 years. This curve will be provided quarterly by the BMA for eight major currencies (USD, CAD, GBP, CHF, EUR, JPY, AUD, NZD). The method will also be published so that companies will be able to generate the curve on interim dates for internal purposes, and also for other currencies that might be needed. The method has been selected to be fully automated (with all parameters disclosed) to facilitate this.

b. The UFR will be set at a single rate across all currencies in recognition of the difficulty of projecting national differences over such a long time span. The UFR will initially be set at $4.2 \%$. It is anticipated that the UFR may be recalibrated from time to time if there is a material change in long term expectations (such as occurred between the 1970's and the present date).

c. Interest rate swaps that cover a period no longer than a specified duration (the "Last Liquid Point", or LLP) are used to develop the yield curve. However, in recognition of the fact that the swap market is thin in certain jurisdictions, sovereign bonds are first used to establish the smooth shape of the curve before it is adjusted using the swap spreads.

d. The LLP will be set equal to 30 years for all currencies. The steps for producing each yield curve are as follows:

i. Sovereign bond prices as of the specified date (e.g. $31^{\text {st }}$ December) are input to a Nelson-Siegel-Svensson process with a pre-specified beta parameter (the UFR). This results in a preliminary yield curve of spot rates extending to 100 years where the corresponding year 100 forward rate is equal to beta.

ii. Spot rates corresponding to the selected swaps are estimated; if swaps are not available at the LLP, then that value is estimated using differences from the sovereign bond curve from the previous step.
iii. Spreads of the selected swaps over the preliminary yield curve are calculated and any missing values are estimated using linear interpolation (selected for its simplicity).

iv. The resulting spreads from duration 1 to the LLP are combined with a zero spread at year 60 and then smoothed and interpolated using cubic splines.

v. The smoothed and interpolated spreads are adjusted down to reflect a 10bp credit spread and added to the yield curve from the first step.

vi. A final linear adjustment is applied to the spot rates between the LLP and year 60 to ensure that the final UFR is equal to the pre-specified value.

## III. STANDARD APPROACH

3. In recognition of the fact that a significant number of commercial insurers and insurance groups have liabilities that are often not fully liquid, commercial insurers and insurance groups will be permitted to include an adjustment to the risk-free rate to partially reflect the illiquidity premium implicit in the underlying assets held and avoid artificial volatility on their balance sheets. This also has the aim of preventing procyclical investment behaviour by mitigating the effect of exaggerations of bond spreads.

4. Discount rates for this approach will be provided by the Authority for the same currencies as the risk-free rate. They will be determined as follows:

a. The starting point will be the risk-free yield curve as already described.

b. A liquidity adjustment will be added to these rates to reflect the fact that insurance liabilities are in practice not entirely liquid. This liquidity adjustment will be based on a representative asset portfolio and will be reduced to reflect the cost of defaults and ratings class transitions and multiplied by an uncertainty margin.
c. For simplicity, the representative asset portfolio will be based solely on corporate bonds of various ratings classes and durations. Published bond data will be used where it is readily available; for currencies where liabilities are much smaller, approximations may be used. The Authority currently uses Bloomberg as the source of data. The yield curve is built using the same Nelson-Siegel-Svensson method as was used to develop the yield curve for the starting risk-free rates.

d. The adjustment for cost of defaults and transitions will also be marketbased where feasible. Currently, this data is taken from the European Insurance and Occupational Pensions Authority (EIOPA) for different combinations of maturities, ratings classes and separately for financial and non- financial companies.

e. The uncertainty margin is currently $35 \%$.

f. The spread net of default costs and transitions is calculated as above for durations 1-15 and remains level thereafter. This approach mitigates against noise in the results.

## IV. SCENARIO BASED APPROACH

5. Bermuda has a number of Long-Term commercial insurers with a significant volume of highly bespoke reinsurance structures and asset portfolios. For these commercial insurers, the Standard approach may be too blunt an instrument to properly capture the market sensitivity of their business.

6. In many cases these commercial insurers are not exposed to the risk of changing spreads on the assets that they hold, even if strict cash flow matching requirements have not been fully achieved. Therefore, the Authority will permit the use of an alternative scenario-based approach that is designed to capture both the sensitivity to interest rates and the degree to which the assets and liabilities are cash-flow matched. The Authority may also consider requiring this method for lines of business that have significant optionality that would not be captured under the Standard approach.

a. The scenario based approach uses the actual portfolio of assets assigned to the block of business (as well as any projected reinvestments) to determine
market yields net of default costs. A "base scenario" is formed from the expected liability and interest rate assumptions.

b. A set of interest rate stresses are then applied to the base scenario to determine the amount by which the market yields must be adjusted up or down to reflect interest rate risk and asset-liability mismatching. The resulting interest rate curve is reflected in the reserves.

c. In cases where the assets and liabilities are perfectly matched with no reinvestment required, the stress scenarios would have no impact.

d. Specifics of the method are provided below.

7. The Authority has developed a set of interest rate scenarios that have been calibrated using an economic scenario generator to develop deviations that are approximately one standard deviation away from the mean so as to target events that may reasonably be expected to occur. More extreme scenarios would be captured in the capital requirement. These scenarios cover a number of different interest rate patterns (such as increasing, decreasing, increasing and decreasing, twists where the long and short term rates behave differently, etc.) The specific scenarios are as follows:

a. All rates decrease annually to total decrease of $1.5 \%$ in tenth year; unchanged thereafter.

b. All rates increase annually to total increase of $1.5 \%$ in tenth year; unchanged thereafter.

c. All rates decrease annually to total decrease of $1.5 \%$ in fifth year then back up again by tenth year.

d. All rates increase annually to total increase of $1.5 \%$ in fifth year then back down again by tenth year.

e. Decrease with positive twist to the following net change after ten years (interpolate for other durations):

i. Year 1 spot rate $-1.5 \%$

ii. Year 10 spot rate $-1.0 \%$

iii. Year 30 spot rate $-0.5 \%$
f. Decrease with negative twist to the following net change after for ten years (interpolate for other durations):

i. Year 1 spot rate $-0.5 \%$

ii. Year 10 spot rate $-1.0 \%$

iii. Year 30 spot rate $-1.5 \%$

g. Increase with positive twist to the following net change after ten years (interpolate for other durations):

i. Year 1 spot rate $+0.5 \%$

ii. Year 10 spot rate $+1.0 \%$

iii. Year 30 spot rate $+1.5 \%$

h. Increase with negative twist to the following net change after for ten years (interpolate for other durations):

i. Year 1 spot rate $+1.5 \%$

ii. Year 10 spot rate $+1.0 \%$

iii. Year 30 spot rate $+0.5 \%$

8. The reinvestment assumptions will reflect the company's investment guidelines and will be considered as part of the Approved Actuary Opinion and also be disclosed in an Actuarial Memorandum to accompany the submission. It is anticipated that the Actuarial Memorandum will incorporate a number of other pieces of information, including an assessment of the extent of asset liability matching in the portfolio. Detailed content of the Actuarial Memorandum will be developed, in consultation with industry, in the coming months.

9. The calculation steps would be as follows:

a. Using the asset portfolio, expected defaults and reinvestment guidelines backing the block of business, determine the amount of held assets required to cover the liability cash-flows for the base scenario. This in turn is used to determine the unadjusted market yields (net of default costs).

b. Under each alternative stress scenario, determine the revised amount of assets required to cover the liability cash-flows. Where the assets and liabilities are less than fully matched (and there is a corresponding reinvestment risk), the asset requirement may be higher than under the base scenario. As with the base
scenario, the revised asset requirement will be used to determine adjusted market yields (net of default costs).

c. The reserve is set equal to the highest asset requirement across all scenarios.

10. The Authority anticipates that different blocks of business will be evaluated separately for the purposes of determining the appropriate discount rate to be used.

11. The scenario-based method would not be available for blocks of business that fall below a certain level of matching, and the standard approach would need to be adopted. Based on results from the trial run, it is tentatively expected that where the difference between the final scenario-based result and the base scenario exceeds $10 \%$, then the Authority will have further discussions with the commercial insurer, and may require the standard approach to be adopted - this approach will be kept under review as experience with the scenario-based method grows.
A PUBLIC POLICY PRACTICE NOTE

# Quantifying Risk Exposures for 

## Own Risk and Solvency Assessment Reports

## June 2016

Developed by

the Risk Exposures Subgroup

of the ERM/ORSA Committee

of the American Academy of Actuaries

<img src="https://cdn.mathpix.com/cropped/2024_04_10_653bcc917ddcdf72dac6g-01.jpg?height=268&width=724&top_left_y=2116&top_left_x=711" alt="image" style="width:100%;height:auto;">

Objective. Independent. Effective. ${ }^{\text {TM }}$

# Quantifying Risk Exposures for Own Risk and Solvency Assessment Reports 

June 2016

Developed by<br>the Risk Exposures Subgroup<br>of the ERM/ORSA Committee<br>of the American Academy of Actuaries

<img src="https://cdn.mathpix.com/cropped/2024_04_10_653bcc917ddcdf72dac6g-02.jpg?height=306&width=832&top_left_y=1503&top_left_x=644" alt="image" style="width:100%;height:auto;">

Objective. Independent. Effective. ${ }^{\text {T }}$

The American Academy of Actuaries is an 18,500+ member professional association whose mission is to serve the public and the U.S. actuarial profession. For more than 50 years, the Academy has assisted public policymakers on all levels by providing leadership, objective expertise, and actuarial advice on risk and financial security issues. The Academy also sets qualification, practice, and professionalism standards for actuaries in the United States.

Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

## 2015-16 Risk Exposures Subgroup

Patricia Matson, MAAA, FSA

Chairperson

Mark Birdsall, MAAA, FSA

Wayne Blackburn, MAAA, CERA, FCAS

Ashlee Borcan, MAAA, FSA

Aaron Halpert, MAAA, ACAS

David Heppen, MAAA, FCAS

Shiraz Jetha, MAAA, CERA, FSA

Lesley Bosniack, MAAA, CERA, FCAS

David Schraub, MAAA, CERA, FSA, AQ

Special thanks to those who helped finalize the practice note: Daniel Hui, MAAA, CERA, FSA; Malgorzata Jankowiak-Roslanowska, MAAA, ASA; Joshua Liu, MAAA, FRM, FSA; and William Wilkins, MAAA, FCAS.

<img src="https://cdn.mathpix.com/cropped/2024_04_10_653bcc917ddcdf72dac6g-03.jpg?height=182&width=417&top_left_y=1351&top_left_x=735" alt="image" style="width:100%;height:auto;">

AMERICAN ACADEMy of ACTUARIES

Objective. Independent. Effective. ${ }^{\text {т }}$

1850 M Street N.W., Suite 300

Washington, D.C. 20036-5805

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

This practice note is not a promulgation of the Actuarial Standards Board (ASB), is not an actuarial standard of practice, is not binding upon any actuary, and is not a definitive statement as to what constitutes generally accepted practice in the area under discussion. Events occurring subsequent to this publication of the practice note may make the practices described in this practice note irrelevant or obsolete.

This practice note was prepared by the Risk Exposure Subgroup of the Enterprise Risk Management (ERM)/Own Risk and Solvency Assessment (ORSA) Committee of the Academy. The practice note represents a description of practices believed by the current work group to be commonly employed by actuaries in the United States in 2016 The purpose of the practice note is to assist regulators and actuaries in understanding how U.S. insurers might quantify company risk exposures (the potential financial loss associated with a specific risk event) for the purposes of Section 2 of the ORSA summary report. However, no representation of completeness is made; other approaches may also be in common use. In addition, practices are likely to vary significantly depending on the nature, scale, and complexity of each individual insurer.

For additional background information on ERM practices, including quantification of risk exposures, readers can review a 2014 Academy overview of how actuaries might approach an ORSA report, Actuaries and Own Risk and Solvency Assessment (ORSA) ${ }^{1}$.

Because this practice note is intended to cover a range of practices across different insurer types, sizes, and complexity, there is no single, standard set of risks or risk measurement methods that can be used consistently throughout. The authors deliberately used a range of risk types and quantification approaches covering a broad (but not complete) list of existing practices, because there is no single risk taxonomy or risk quantification method that applies across all companies.

This practice note is the work product of the ERM/ORSA Committee of the American Academy of Actuaries. The paper/presentation does not provide regulatory guidance and does not reflect the view of the NAIC or its regulatory members.

We welcome comments and questions. Please send comments to RMFRCPolicyAnalyst@actuary.org.[^0]

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

## Table of Contents

Introduction ..... 6
Background ..... 6
Risk Exposure Questions ..... 7
Q1. What risk categories are commonly considered in the ORSA report? What risks are quantified versus not quantified? ..... 7
Q2. How often is a formal enterprise risk identification or assessment process performed? What may cause monitoring frequency to change? ..... 10
Q3. How do companies quantify risk? What are the limitations of those efforts/methods? How does the approach differ between types of risk (catastrophe, operational, etc.)? ..... 11
Q4. What are companies using stress testing for? ..... 15
Q5. How do companies determine stress scenarios for purposes of risk quantification? Are the stress scenarios calibrated to the same degree of severity? ..... 16
Q6. How is inherent versus residual risk addressed, and how can management action be integrated into the risk quantification process? ..... 17
Q7. How are more challenging risks, such as emerging risks, being addressed? ..... 18
Q8. How do companies deal with risk interactions (across risk types, product lines, legal entities, etc.) in the risk assessment process? ..... 19

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

## Introduction

This practice note is intended to provide actuaries and regulators with information on the approaches used for quantification of risk exposures that may be included in Section 2 of an Own Risk and Solvency Assessment (ORSA) report.

The ORSA Guidance Manual states "Section 2 of the ORSA Summary Report should provide a high-level summary of the quantitative and/or qualitative assessments of risk exposure in both normal and stressed environments for each material risk category identified in Section 1. This assessment process should consider a range of outcomes using risk assessment techniques that are appropriate to the nature, scale, and complexity of the risks." ${ }^{2}$

This practice note represents a description of practices the subgroup believes to be common among many, but not all, U.S. actuaries; however, other approaches also may be appropriate. This practice note is also intended to encourage discussion on the issues set forth below, providing a framework to foster dialogue among the regulators and actuaries involved in the process.

## Background

Following the financial crisis, there was a global movement to better assess a holding company's financial condition. Established international standards-setting bodies were strengthened and charged with developing systems for assessing company risk and creating capital regulations to prevent global systemically important financial institutions, including a number of large insurers, from collapsing in the future. As part of these efforts in the United States, the National Association of Insurance Commissioners (NAIC) set up a Solvency Modernization Initiative and adopted a new risk management evaluation tool for U.S. insurance regulation - the Own Risk and Solvency Assessment (ORSA).

According to the NAIC, "An ORSA will require insurance companies to issue their own assessment of their current and future risk through an internal risk self-assessment process and it will allow regulators to form an enhanced view of an insurer's ability to withstand financial stress." ${ }^{3}$ The ORSA summary report has been incorporated into international standards-setting efforts and is in various stages of implementation in the United States, Europe, and other countries.

In 2014, over 25 insurers in 26 states participated in a pilot ORSA summary report program in the United States. The pilot participants submitted 210 reports and covered 77 percent of the total[^1]

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

estimated ORSA summary reports expected to be filed. ${ }^{4}$ That number is only expected to grow in 2015 and beyond.

As of June 2016, pursuant to Model \#505 adoptions, large- and medium-size U.S. insurance groups and/or insurers will be required to submit an ORSA summary report in 39 states. ${ }^{5}$ The NAIC has developed an education program for state regulators reviewing ORSA summary reports to aid in their review efforts.

As state regulators and NAIC began reviewing U.S. insurers' ORSA summary reports for 2015, they concluded that Section 2 of the reports might benefit from additional details on an insurer's process for quantifying risk exposures. The NAIC and regulators were particularly interested in how insurers quantify underwriting, market, credit, and operational risk, and other risks. This practice note is intended to provide information on the current practices of U.S. insurers when attempting to quantify risk exposures.

## Risk Exposure Questions

## Q1. What risk categories are commonly considered in the ORSA report? What risks are quantified versus not quantified?

Section 2 of the ORSA summary report guidance manual refers to the risk categories of credit, market, liquidity, underwriting, and operational risk. Other categories of risk that are often considered are strategic, reputational, and regulatory risk. These additional three risk categories might be considered segments of operational risk, but some companies' ORSA processes will have explicit recognition of these risks. In addition, companies often consider current risks as well as emerging risks in some or all of these categories. Insurance groups operating on an international basis or with foreign investments may also identify foreign exchange risks. Insurers with material other businesses beyond insurance may also need to cover other types of risks applicable to those businesses. Further discussion of these risks is outside the scope of this paper.

Many of the specific risks that tend to be quantified in Section 2 of the ORSA report are, in a broad sense, common to insurers, regardless of whether the insurers focus on health, life, property/casualty, or a combination of these businesses. Such risks often include:[^2]

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

- Mis-estimation of existing liabilities as reflected on the company's balance sheet;
- Mis-estimation of the profitability of the business;
- Aggregation of risks that could be impacted by single events, such as natural catastrophes or the emergence of a pandemic;
- Market/investment risk;
- Credit risk;
- Liquidity risk; and
- Operational risks.

Many of these risks can interact with one another. Some will be relatively more material than others for any given insurer. It should not be assumed that all will be quantified in Section 2 of an individual company's ORSA. However, all of these risks are typically considered, and those that are deemed to be material are typically included in Section 2, particularly when there is a reasonable basis for quantifying the risk.

An effective risk assessment process often requires risk quantification. Quantification can serve various purposes. With respect to ORSA Section 2, quantification is often done for purposes of prioritizing enterprise risks. Quantification may also be for operational or for capital planning purposes; the former refers to risk exposures for normal business planning needs while the latter typically considers capital adequacy in stress/tail regions. For each purpose, appropriate levels of stress for each quantifiable risk are typically developed to enable quantification. For risks that cannot easily be quantified, judgment may be used to try to develop a priority for the risk. For example, experts in the particular risk may judgmentally assign the risk to a likelihood and severity "bucket" based on defined criteria.

Qualitative assessment methods might serve to inform a company's board, senior management, and external stakeholders more successfully than insufficiently supported quantitative methods. Or, a qualitative assessment process could be used as an interim approach for ORSA reporting while a quantitative process is being researched and validated.

The predominant focus of an insurer (health vs. life vs. property/casualty) will often influence the manner in which these risks are evaluated, and the relative ranking of these risks in terms of their potential impact on the firm's financial health. The discussion below provides additional background on these nuances. Much of the terminology is practice-specific; this is not intended to suggest that the discussion is only applicable to the particular practice area, but rather is intended to use common parlance for the practice area for which the risk is typically a significant consideration.

For property/casualty ( $\mathrm{P} / \mathrm{C})$ insurers, reserve risk is a substantial risk category that is typically assessed. Reserve risk pertains to estimating a P/C insurer's unpaid claim liability. Since these estimates are developed from the insurer's claims history, the risk will be particularly significant if the insurers product portfolio is changing, or if claims practices are changing.

For life and health insurers, insurance risks typically include mortality/longevity, morbidity, and policyholder behavior.

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

All of these may be further evaluated based on the nature of the underlying driver. For example, mortality/longevity risk may be comprised of volatility, trend, and mis-estimation risk. Volatility risk is the short-term fluctuation in annual results. Trend is the risk that long-term (mortality/longevity in life or frequency/severity in P/C) do not adequately recognize changes in mortality improvement. Mis-estimation risk is the risk that the assumption-setting process is not operating correctly, resulting in a poor estimate of mortality/longevity.

A similar breakdown may apply for morbidity and behavior risk. In addition, for policyholder behavior risk, there may be separate considerations for "normal" economic conditions and policyholder response to changing economic conditions - in other words, dynamic behavior. Some or all of these types of risks are commonly quantified by insurers.

For life, annuity, and long-term care products with long-term premium guarantees at fixed (or relatively inflexible) rates, another risk to consider would be "expense risk," representing the inadequacy of expense margins in premiums. High inflation, low growth, automation, increased competitiveness, dividend scale concerns, accounting basis (e.g., recoverability in GAAP, statutory new business strain), etc. can impact outcomes on adequacy of expense margins in premiums and in some cases ongoing vitality of the insurer. In the past, expense risk has not factored materially in ERM work, especially in short-term solvency evaluations; however, it is a risk that may be quantified in the ORSA report.

Financial Markets risk is a very common insurer risk, and is typically quantified using individual or sets of economic scenarios. Market risk typically includes interest rate levels, interest rate volatility, equity levels, and equity volatility. It is common to quantify interest rate level risk and equity level risk when it is applicable to the company. Depending on the nature of the products, associated risks, and risk mitigation strategies, interest rate volatility and equity volatility may or may not be part of the risk assessment process; however, they can be significant for companies with hedging programs, derivative use, or liabilities with interest rate or equity guarantees.

Credit risk is also commonly quantified. It may be further evaluated based on specific categories, including the risk of default, the risk of ratings migration, and the risk of movements in credit spreads, though not all insurers quantify all of these components. For purposes of enterprise quantification, companies may consolidate default risk across investment counterparties, reinsurers, and potentially even vendors and suppliers.

Liquidity risk is usually addressed through the evaluation of cash inflows and outflows over short and medium time horizons, both in baseline and stress scenarios. Stress scenarios may consider items such as market and credit stresses impacting asset liquidity, as well as increases in outflows beyond expected due to items such as increased claims or lapses. Liquidity risk is likely to be quantified as part of ORSA.

Operational and emerging risk categories are difficult to assess and quantify. Operational risk is often divided into component subcategories, examples being reputational risk, cyber security risk, legal risk, regulatory risk, and strategic risk, etc. The identification process will likely describe the inherent risk with descriptions of mitigation and monitoring steps. Some companies may use historical operational risk event data, potentially combined with external data sources,

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

to quantify operational risk exposure. Other companies may place more effort on controls and monitoring rather than on a quantification process.

For some insurers, historical operational risk events are often contained in the historical data used for reserving. Thus, an explicit assessment and quantification of operational risk might be double-counting unexpected loss amounts quantified for reserving and underwriting risk.

## Q2. How often is a formal enterprise risk identification or assessment process performed? What may cause monitoring frequency to change?

Insurers may perform enterprise-wide identification or assessment processes annually, though some insurers use more or less frequent periods. Insurers also often re-evaluate individual risks on a more frequent basis.

Once risks are identified, insurers commonly place them into a consolidated risk listing, often called a risk register. After compiling an initial risk register, the insurer might amend it quarterly, or as infrequently as once a year. The frequency of the update is a function of the size and maturity of the ERM program and also the granularity of the listing / identification process.

Risk quantification on a consistent, defined basis is a key element to enabling proper prioritization and monitoring levels of risks. The defined basis could be the likelihood of an adverse result, the volatility of the risk, the severity of the risk, a calibration of stress tests across all risks to the same degree of confidence, or some combination of these.

If all significant enterprise risks are quantified using the same approach and scale, risks can then be prioritized according to impact. This prioritization enables the organization to focus on the most significant risks first, and potentially change the frequency of monitoring to focus more on the risks with the greatest impact.

Product line financial outcomes during the year may create the need for reassessment of a risk, the frequency of monitoring, and other changes to controls (such as exposures). Emerging risks (e.g., cyber threats) may require more frequent monitoring due to their evolving nature. The amount of company and/or industry data available to serve as a basis for the quantification of such risks is likely to change rapidly, and thus the company's view of the risk's impact may in turn change relatively quickly.

Both the timeframe and frequency of the risk update often depend on the risk considered, including items such as:

1. The time the risk first emerges to the time it could damage the company (fast vs. slow);
2. The materiality for the company (material vs. non-material); and
3. The availability of monitoring tools (available vs. non-available).

The following examples show a combination of these dimensions to help clarify:

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

- Market risks like interest rate, equity, foreign exchange (FX), credit quality, and default are typically monitored and managed multiple times per day through hedging programs at life insurance companies selling market-sensitive products; these are major risks, fastmoving risks, and risks for which there are existing tools to monitor (fast/material/available).
- A domestic-only company exposed to foreign exchange risk only through the cost of offshore staffing/contracting may monitor foreign exchange risk on an annual basis; this risk is a minor risk for that company (fast/non-material/available).
- Mortality trends are typically monitored less frequently; this is a slow-moving risk where monitoring tools are less abundant (slow/material/non-available).
- Court challenges to the Affordable Care Act (ACA) were a regulatory risk that had the potential for both an extreme and immediate impact on some health companies, but the monitoring process was limited (fast/material/non-available).


## Q3. How do companies quantify risk? What are the limitations of those efforts/methods? How does the approach differ between types of risk (catastrophe, operational, etc.)?

An effective risk assessment exercise process often requires risk quantification. Quantification can serve various purposes. With respect to ORSA Section 2, quantification is often done for purposes of prioritizing enterprise risks. Quantification may also be for operational or for capital planning purposes; the former refers to risk exposures for normal business planning needs while the latter typically considers capital adequacy in stress/tail regions. For each purpose, appropriate levels of stress for each quantifiable risk are typically developed to enable quantification.

Some potential approaches to quantification include:

| Method | Description | Example |
| :--- | :--- | :--- |
| Scenario or stress <br> testing | Running a model under a <br> "baseline" and "stressed" <br> scenario and evaluating the <br> change in a financial metric due <br> to the scenario or stress | Risk exposure equals the change in <br> available capital in the baseline financial <br> plan versus the financial plan after a <br> 100bps move in interest rates |
| Use of actual <br> historical <br> company data | Analyzing adverse results in the <br> company's own claims <br> experience | Risk exposure equals the worst historical <br> year of claim payments from a 30-year <br> history |
| Use of external <br> data | Looking at risk exposure values <br> from external databases or studies <br> for similar risk events | Cyber risk exposure equals the average <br> cost experienced by the industry from a <br> recent industry study |
| Use of capital <br> model results or <br> charges | Using the capital charge from an <br> internal or external capital model | Asset default risk exposure equals the C-1 <br> charge from Risk-Based Capital |
| Reverse stress <br> testing | Running a model under a stressed <br> scenario with the stress at a level | Risk exposure equals the change in <br> liquidity ratio after running a reverse |

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

|  | such that the financial results fall <br> outside of a predefined tolerance | stress test on liquidity risk |
| :--- | :--- | :--- |
| Judgmental <br> approaches | Experts weigh in on the <br> likelihood and severity of a hard- <br> to-quantify risk | Risk of a reputational event is expected to <br> cause a 20 percent decline in the customer <br> base, a revenue loss of \$50 million to 100 <br> million, and fines of \$3 million |

The most common method is typically scenario testing. Scenario testing involves quantifying the impact of an event. Identifying a relevant event often involves understanding the drivers of a particular risk (e.g., claims inflation, global warming, model error, etc.) and building a chain of events that is triggered by a particular driver or combination of drivers. The impact of an event on statutory capital, shareholder equity, and net income are typical measures upon which a risk assessment is made, but measures vary according to an insurer's focus. See Question 5 for more information on scenario testing.

An economic capital model's results can also be used to quantify risks. The likelihood and severity of a particular risk and underlying risk drivers may provide the necessary quantification to support an assessment. Economic capital models may identify risk interactions and be useful in measuring the value of mitigation effects. In addition, stressing capital model assumptions can lead to a better understanding of how sensitive the balance sheet is to movements in a risk driver.

Reverse scenario testing (RST) works through the impact of a driver from the opposite direction. RST answers the question, "What type of event or magnitude of a risk driver would deliver an outcome of a prescribed magnitude(s)?" Answering this question can be accomplished by backsolving for a particular risk driver or constructing events that would deliver the prescribed magnitude. Stochastic analysis, such as economic capital modeling, can be helpful for RST. Isolating and dissecting simulation trials that produce the targeted magnitude may aid in identifying events, underlying drivers, and related interactions contributing to or mitigating the severity of an event.

Another key consideration in risk quantification is the quantification metric-in other words, which financial or operational indicator is quantified. Typically, the metric evaluated will depend on the company's strategy and key performance indicators, for example capital, earnings, revenue, customer satisfaction, operational targets, etc.

Potential sources of information for the quantification of risks include:

| Internal data | Companies typically consider the extent to which its own data is reasonably <br> reflective of the exposure presented by any risk. For example, a history of low- <br> level cyber breaches should alert management to the potential for a more severe <br> event. In the case of an emerging risk, it is likely that the company's internal <br> data will be limited or nonexistent, and other sources of information will be <br> needed in the assessment of the potential impact the risk could have on the <br> company. |
| :--- | :--- |
| External data | When industry losses are used to help assess the potential magnitude of a risk, <br> typical considerations include: |

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

|  | - The relevance of the industry loss to the risk under consideration; <br> - The similarity between the company(ies) that experienced the industry loss <br> to the company(ies) under consideration, and any adjustments that may be <br> needed to appropriately reflect similarities/dissimilarities of the <br> organizations (e.g., impact on company's revenue, number of customers, <br> geography, etc.); or |
| :--- | :--- |
| Scenario <br> analysis | Scenario analysis used for other company purposes may provide insight into the <br> level of risk exposure. |
| Internal risk <br> assessments | Internal assessments may result from consideration of the data and scenario- <br> based approaches discussed previously. In addition, internal assessments will <br> often incorporate an element of expert judgment. For emerging and operational <br> risks in particular, it is likely that a relatively significant amount of expert <br> judgment will be included in the overall assessment of the risk. |

Most risk categories are assessed through risk quantification. Credit, market, and underwriting risks often have the benefit of historical data that can be used to develop stressed projections of risk drivers such as bond yields and default rates, reinsurer default rates, incidence rates, claim inflation, and catastrophes. These risks are typically assessed with the benefit of scenario and reverse tests, and potentially also through analysis of economic capital results.

While duration, convexity and "greeks" (other measures of the change in value based on specific changes in market parameters) are commonly used as risk drivers on the investment side, risk drivers should be tailored to the portfolio under consideration as well as the company's metric for measuring risk (capital, earning, new business capacity).

The key drivers for a risk can be influenced by the context in which that risk is viewed. As an example, loan-to-value could be treated as the key risk driver for a portfolio of commercial real estate investments. However, broader economic factors such as interest rates, local wages, or an overall economic index may instead be used as the primary risk drivers if real estate investment risk is quantified in conjunction with other risks, such as those associated with commercial mortgage-backed securities. A benefit of mapping risks back to common drivers is an improved ability to understand the enterprise financial impacts of movements in those drivers.

Liquidity risk quantification is often a direct outcome of measuring the cash flow effects of other risks such as market movements or unexpected liability outflows. Reverse stress testing may be helpful in understanding the magnitude of an event that would cause a liquidity issue.

Operational risk quantification can be a challenge because there is typically limited historical data regarding operational risks, and even when data does exist, it is from an environment that is not directly applicable to the current environment.

Several categories of insurance risk lend themselves to quantification. The approach varies by type of insurance.

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

A number of quantitative methodologies have been published on reserve risk, so several implementation paths exist. Adverse reserve risk outcomes (adverse reserve runoff for prior years) have been a common historical cause for P/C company impairment and insolvency; therefore, assessment and quantification are usually addressed in an ORSA report.

Usually, core elements of assessing P/C reserve risk translate into assessing and quantifying underwriting risk. Reserve risk quantification involves analysis of the volatility of unpaid claim liabilities from prior years' underwriting experience. Thus, historical underwriting outcome volatility measures would likely be a byproduct of reserve risk quantification. However, underwriting risk is typically assessed under a prospective point-of-view, which adds a level of uncertainty on top of the retrospective, reserve risk assessment process. Additional considerations for underwriting risk quantification include:

- The time horizon for the assessment;
- Company's exposure to catastrophic and pandemic risks;
- Possibility of expansion of business and the introduction of new products;
- Policyholder/contract-holder behavior stemming from uncertain pricing or economic outcomes; and
- Consideration of management reactions.

Quantification of life and health insurance risks such as mortality, morbidity, and policyholder behavior typically is based upon measuring the impact of assumption changes in the company's pricing or other projection models.

Potential ways to assess operational risk are generally consistent with overall risk assessment approaches, and include:

- Internal loss data-comprehensive collection of loss data for current and historical views and analysis of future exposure.
- External loss data-purchased data to supplement internal loss data, stimulate discussion, generate scenarios.
- Scenario analysis-probability and impact assessment of plausible, high-severity operational risk events.
- Business environment internal control factor-common risk infrastructure and assessment methodology through risk and control self-assessment and business environment assessment.

Regardless of the quantification approach, the quality and applicability of data sources, degree of judgment required in developing assumptions, and the risk being quantified will impact the usefulness of the risk quantification. For example, investment risk assumptions may be supported by a lengthy history of economic indicators such as bond yields, but the unprecedented prolonged low-interest-rate environment of 2011-2015 presents a challenge in using historical data to develop risk quantification assumptions for the future economic environment. Sensitivity testing assumptions can add a secondary dimension to risk quantification.

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

To the extent that quantitative analysis is not useful, qualitative analysis may inform the assessment of a risk. Many operational risks are addressed through qualitative analysis. Comparing such a risk to those that are measurable or ranking the risk relative to other risks can provide context. Scales spanning from highly unlikely to very likely (referred to as likelihood scales) or from minor to severe severity (severity scales) may be useful. A consistent scoring scale allows for the scoring of a risk analytically without formally quantifying a risk. For example, an insurer may define a risk as low if its financial impact is less than 5 percent of surplus, medium if its financial impact is 5 to 10 percent of surplus, and high if its impact is greater than 10 percent of surplus.

## Q4. What are companies using stress testing for?

Companies may use stress testing to determine risk exposures for the purposes of prioritizing risks. In such instances, it is common for the stress tests to be calibrated to a common level, so that risk exposure can be compared on the same basis to facilitate prioritization. For example, if all risks are calculated based on a financial loss over a one-year period based on a 1-in-100-year event, those producing the highest losses may be prioritized over those with lower losses for purposes of risk mitigation action and monitoring.

Moderately adverse stress tests may be used for assessing risk exposure relative to risk appetite. For example, if a company's risk appetite statement includes something related to maintaining a specific rating level, the company may use stress testing to assess whether its financial results under moderately adverse scenarios would still enable it to maintain a rating above its stated tolerance. These stresses are typically meant to be moderately adverse rather than extreme tail scenarios, because day-to-day management of the company and associated decisions (pricing, hedging, etc.) are intended to cover a range of scenarios around the mean, but not necessarily extreme tail events. For example, if pricing actions were based on tail events, it would be hard for a company to compete in the marketplace.

Stress testing is often used to assess solvency under extreme scenarios. The effects of such scenarios on solvency may be estimated both for short-term (one year or less) and longer-term (up to three years) periods. Companies may consider both individual extreme events and aggregations of events in stress testing. Scenarios may be based on a combination of deterministic and stochastic approaches. Scenarios may be based on a company's historical data, industry events, or hypothetical events that have not been observed but are believed to be possible.

Risk mitigation strategy is also typically influenced by stress testing. By considering the potential impact of a scenario over time, companies can consider various courses of action available to management to mitigate the risk(s) associated with the scenario both before and after it occurs. Should such an event or series of events take place, the company will be prepared to react quickly to mitigate the impact of the adverse situation (or to take advantage of a positive situation).

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

Stress testing may be used to assess the organization's overall capital planning and capital levels held, either economic or regulatory. By evaluating the sufficiency of capital under stress, insurers can understand the extent of "buffer" that capital provides.

Lastly, stress testing may be used as a tool to better assess the severity of risks, in instances in which limited data is available to calibrate specific scenarios. Running a series of stress tests may assist in determining how significant a risk is, and to better assign likelihood and severity levels.

## Q5. How do companies determine stress scenarios for purposes of risk quantification? Are the stress scenarios calibrated to the same degree of severity?

Stress scenarios begin with the identification of key risks that are material to the company's financial results and business objectives. Companies may consider both individual key risks (e.g., natural catastrophes, pandemic, equity market drop) and the interaction of multiple risks (e.g., unexpected medical inflation accompanied by a large increase in interest rates).

Stress scenarios may also consider large unexpected losses from multiple sources that do not necessarily have a causal relationship but rather occur independently; e.g., multiple large natural catastrophes occurring in the same year combined with an impairment of significant financial asset.

Sources of Information for Stress Testing

To quantify the potential magnitude of each risk, companies may consider one or more of the following sources of information:

a) Their own historical data, to the extent it exists;

b) Industry data or in some cases data from other industries, to the extent such data is reasonably reflective of the risk and can be normalized to the company risk profile;

c) Scenarios focused on the most material risks, as suggested by internal capital models;

d) Stress scenarios based on forecasts of economic conditions;

e) Expert judgment, particularly for highly uncertain risks such as reputational risk (for example, exploring in a multidisciplinary setting, a hypothetical stress event such as the impact of a catastrophic event); or

f) Specific scenarios requested by the regulator.

It is common for scenarios to be based on relatively more judgment where there is less relevant available data, for example in testing scenarios that have not previously occurred.

## Quantification Approach for Stress Testing

Methods that may be used include judgmental estimates of the impact of the stress, deterministic or single scenario modeling, and stochastic modeling. For example, mortality or natural catastrophe property risk could be stochastically modeled by simulating large historical events or

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

theoretical events against the profile of the inforce business. Unexpected medical inflation may be quantified based on deterministic stressed assumptions to estimate the potential impact on underwriting and investment results.

Some companies calibrate scenarios to the same degree of severity, so that all stress tests have similar likelihood. Some companies align stress tests with historical events, to make it easier for management and the board of directors to understand, and therefore stresses are not calibrated to the same level. Some companies use judgment to determine stress levels, without an attempt to calibrate the degree of severity. A range of approaches are appropriate; however, the use of the results is typically aligned with the method chosen. For example, if the stress events are not calibrated to the same level of severity, it is harder to use the results to prioritize risk exposures.

The magnitude of each scenario may be evaluated relative to key risk metrics (such as capital, earnings, revenue, customer satisfaction, operational targets, etc.) and overall enterprise risk management strategy. Conversely, stress scenarios may be set at a level such that the result of applying the scenario is capital depletion (in other words, a reverse stress test).

## Q6. How is inherent versus residual risk addressed, and how can management action be integrated into the risk quantification process?

Inherent risk measures risk before factoring in the controls that are in place, whereas residual risk considers those controls and the effectiveness of the controls. The concern about an inherent risk may be less when measuring the risk from a residual perspective, assuming controls are effective at mitigating risk. Conversely, if the controls fail, it is important for an organization to understand the inherent risk. In order to quantify either inherent or residual risk, it is necessary to understand the controls in place, their value, and their effectiveness. Such controls may be designated underwriting authority levels, investment guidelines, hedging, reinsurance protection, etc.

Viewing a risk as if no effective mitigation exists, or looking at actual historic events where no controls were in place are two possible approaches to measuring inherent risk. Sources of information used to assess risk may contain mitigation impacts, and as a result may be more appropriate for use in measuring residual risk. One example is the availability of data net of reinsurance but not gross. It is necessary to unwind the mitigation impacts to understand inherent risk. Conversely, sources containing no risk controls may only be available, and measuring the impact of a control and its effectiveness will allow the translation between inherent and residual risk.

Depending on the organization, management will have varied responses to a risk and have different options available in addressing them. Examples of such options include: selling or discontinuing a poorly performing line of business, issuing debt to raise capital, spreading a concentration of third-party exposure across multiple counterparties, etc. To the extent that management's actions to a risk can be anticipated, such information is valuable to the risk assessment. Tracking past behavior and outcomes of management action in containing a risk can often be helpful in assessing the residual risk. Documenting information — such as the length of

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

time to act, the action taken, the success of those actions, and the ultimate outcome - is important to the process of quantifying residual risk.

## Q7. How are more challenging risks, such as emerging risks, being addressed?

From an organization's perspective, the time horizon to full emergence and consequent business impact may be a factor in how it responds to the risk. For example, management may make risks with a longer germination period (e.g., beyond three years) a lower priority.

Emerging risks can originate both internally and externally; while in the former instance its impact is localized, in the latter the impact can be localized (e.g., supply chain) or sector-wide (e.g., driverless cars). Application of actuarial judgment, rather that more precise quantification techniques, may have a bigger role in emerging risk quantification - especially during the initial stages.

Trend identification techniques such as environmental scanning, data mining, etc. and ongoing monitoring of potential risks can provide useful information to evaluate emerging risks.

## Property \& Casualty

An example of a potentially significant emerging risk is driverless cars. Companies with significant books of automobile business may consider this developing technology to be a risk exposure, despite uncertainty as to the timing of its emergence into the mainstream. Companies may therefore include assessments of driverless car impacts under various sets of assumptions with respect to factors such as:

- Market share - for example, the possible emergence of new competitors (e.g., technology companies).
- Loss frequency-for example, the possible reduction in accidents attributable to human error.
- Loss severity-for example, the possibility of increases in severity due to more expensive equipment.
- New risks associated with the technology - for example, the possibility of computer hackers causing catastrophic accidents by overriding the navigation systems of driverless cars.

While all of these items may be estimates based on actuarial judgment, many companies may believe it is important to make such estimates as part of its overall ERM process in order to be prepared to adapt its strategy to the risk as it emerges.

## Health

An example of a potentially significant emerging risk in the health arena is the future evolution of the Affordable Care Act (ACA). While the ACA has already had a profound impact on health insurers, there is a great deal of uncertainty surrounding the program as well as potential changes in the future. Examples of risks that health care companies may identify as a result of ACA are:

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

1. Market structure risk-for example, the possibility that future changes in ACA will have an impact on the structure of the health insurance market and have an impact on the company's ability to earn sufficient profit margins while remaining price competitive.
2. Operational - for example, the possibility that future changes in ACA will create additional reporting requirements.
3. Loss frequency - for example, the possibility that future changes in ACA will create additional mandated benefits that increase loss frequency.
4. Regulatory risk - for example, the possibility policymakers alter or repeal ACA, causing significant instability in the market.
5. Pricing risk-for example, the possibility that the assumptions utilized in pricing are insufficient due to uncertainty in the market.
6. Cash flow risk - for example, the strain caused by ACA-related payments to or from the government.

## Life

An example of a potentially significant emerging risk in the life arena is rising interest rates. Due to the asset-intensive nature of a number of life insurance products, interest rate changes can cause significant issues for companies. Examples of risks that life insurance companies may identify as a result of rising interest rates are:

1. Market risk-for example, the possibility that the company's existing portfolio is earning less than current market rates, resulting in a less competitively priced product offering.
2. Liquidity risk-for example, the possibility that policyholders surrender their universal life or annuity policies in order to invest with competitors paying higher interest rates on their products.
3. Earnings risk - for example, the possibility that the company must sacrifice earnings in order to hedge against a rising interest rate environment.
4. Asset risk - for example, the possibility that higher interest rates affect prepayments on certain asset classes and result in deviations from the company's asset strategy.
5. Spread risk - for example, the possibility that higher interest rates adversely affect the investment spreads the company is able to earn in the market.

## Q8. How do companies deal with risk interactions (across risk types, product lines, legal entities, etc.) in the risk assessment process?

Risk interactions can be across lines of business, risk types, legal entities, etc. ("segments"). Risk interactions can be due to a single event's effect across multiple areas of the organization, such as medical inflation affecting multiple lines of business. It can also be due to the aggregated effect of a chain of events, such that through the path of that chain, there are compounding or diversifying effects across the balance sheet. A risk assessment contemplating these interactions provides information to identify risks that are similar, related, or diversifying.

In order to incorporate risk interactions into a risk assessment, a company may begin by aggregating the exposure data or analyze risk assessments across segments for commonalities and differences in risk and drivers of risk. Consideration for systematic (global economic and

## Practice Note on Quantifying Risk Exposures for Own-Risk and Solvency Assessment Reports

insurance related) and non-systematic (specific to the organization) effects provides a comprehensive view of related risks. Involving multiple business units or functional areas in the assessment of what types of risk exposures exist and how they may interact to impact the organization can help to give a more complete view.

As an example, if interest rates change significantly, it is important to understand what caused interest rates to rise and how might that cause might relate to other parts of the balance sheet. If the inflationary environment caused interest rates to change, the interest rate movement will impact bond values but could also drive claim inflation effects.

To highlight another example, if a company has a large real estate portfolio, and also issues property protection products, large natural catastrophes would impact both the assets held as well as the claim liabilities associated with the products written.

Stress testing provides an organization with a more comprehensive understanding of similarities or related risks and diversification opportunities across the balance sheet. These types of exercises encourage the implementation of efficient mitigation and effective business planning strategies such as reinsurance purchases, diversified investment portfolios, and profitable and diversified premium growth.

An important consideration in risk management is how risk interactions will play out in times of stress. Use of "normal" environment correlation data may not be appropriate for assessing the interaction of risks in a severe scenario.

In addition, when evaluating enterprise exposures, companies must consider constraints imposed at more granular levels. For example, there could be legal entity restrictions on movement of capital across entities, or specific limits on investment risk exposures in a given legal entity or general account. These limitations may impair the ability of the insurer to make the best enterprise decision with respect to risk and reward.


[^0]:    1 “Actuaries and Own Risk Solvency Assessment (ORSA),” American Academy of Actuaries, 2014.

[^1]:    2 "NAIC Own Risk and Solvency Assessment (ORSA) Guidance Manual" National Association of Insurance Commissioners (NAIC), 2010. As retrieved from http://www.naic.org/store/free/ORSA manual.pdf on Feb 10, 2016.

    3 "Own Risk and Solvency Assessment (ORSA)," Center for Insurance Policy and Research, NAIC, 2015. As retrieved from http://www.naic.org/cipr_topics/topic_own_risk_solvency_assessment.htm on Feb. 10, 2016.

[^2]:    4 "2014 Own Risk and Solvency Assessment (ORSA) Feedback Pilot Project Observations of the Group Solvency Issues (E) Working Group," NAIC, 2015. Retireved from http://www.naic.org/documents/committees_e_isftf_group_solvency_related_orsa_feedback_pilot_project.pdf on Feb. 10, 2016.

    ${ }^{5}$ Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Iowa, Illinois, Indiana, Kansas, Kentucky, Louisiana, Maine, Michigan, Minnesota, Missouri, Montana, North Dakota, Nebraska, New Hampshire, New Jersey, New York, Nevada, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode Island, Tennessee, Texas, Virginia, Vermont, Washington, Wisconsin, and Wyoming have all adopted Model \#505 as of June 2016. Hawaii and Massachusetts are still considering adopting Model \#505. http://www.naic.org/documents/committees_e_related_smi_dashboard.pdf?123


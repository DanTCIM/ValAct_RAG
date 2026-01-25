# Climate Anomalies' Enduring Impacts on U.S. Health Landscape

DECEMBER | 2025

AUTHORS Yanbin Xu, PhD, FRM<br>Wenjun Zhu, FSA, CERA, PhD<br>Tianxiang Shi, FSA, MAAA, PhD

SPONSOR<br>Catastrophe and Climate Strategic<br>Research Program, SOA

## Caveat and Disclaimer

The opinions expressed and conclusions reached by the authors are their own and do not represent any official position or opinion of the Society of Actuaries Research Institute, the Society of Actuaries, or its members. The Society of Actuaries Research Institute makes no representation or warranty to the accuracy of the information.

## CONTENTS

    Executive Summary ..... 4
    Section 1 Introduction ..... 5
    Section 2 Existing Evidence of ENSO Impacts on U.S. Public Health ..... 7
    Section 3 Methods ..... 8
    3.1 Data ..... 8
    3.1.1 Cause-Specific Mortality Data ..... 8
    3.1.2 Economic Control Data ..... 8
    3.1.3 Historical Meteorological Data ..... 8
    3.1.4 Climate Projection Data ..... 8
    3.1.5 Future Population and Production Projection Data ..... 9
    3.2 ENSO Measure ..... 9
    3.2.1 Intensity Measures ..... 9
    3.2.2 Teleconnections ..... 10
    3.3 Cause-Specific Mortality Improvement ..... 11
    3.4 Econometric Model ..... 12
    3.5 Projected Future Life Expectancy Loss ..... 12
    3.6 Monetize Life Expectancy Loss ..... 13
    3.7 Attribute Life Expectancy to Cause ..... 14
    Section 4 Results ..... 16
    4.1 ENSO's Cause-Specific Impact on Mortality Improvement ..... 16
    4.2 Further Breakdown for Circulatory System and External Causes of Disease ..... 17
    4.3 Age-Specific Vulnerability ..... 19
    4.4 Impact on Mental Health and Age/Gender-Specific Conditions ..... 21
    4.5 Cause-Specific Welfare Loss in the Past ..... 22
    4.6 Quantify Future Health Impact of ENSO ..... 23
    Section 5 Discussion and Policy Implications ..... 27
    5.1 Policy and Actuarial Implications ..... 27
    5.2 Limitations and Next Steps ..... 27
    Section 6 Acknowledgments ..... 29
    References ..... 30
    About The Society of Actuaries Research Institute ..... 34

## Executive Summary

This report establishes a U.S.-focused, policy-relevant framework to quantify how El Niño-Southern Oscillation (ENSO) anomalies affect public health, using cause-specific mortality as the primary outcome and a distributed-lag econometric design supplemented by life-table attribution and economic valuation. This framework measures both short-run and persistent effects in historical data, attributes life-expectancy changes to individual causes, monetizes welfare losses, and projects future burdens under alternative climate pathways.

Key findings are threefold. First, El Niño persistently impedes mortality improvement in major diseases, most notably circulatory system diseases and external causes, with effects that intensify among middle and older ages. Second, the 1982-83 and 1997-98 events produced substantial life-expectancy losses and multi-trillion-dollar welfare costs, concentrated in circulatory causes. Third, under intensified ENSO variability, mid-century to end-ofcentury projections indicate material erosion of U.S. life-expectancy gains, with growing scenario-dependent uncertainty under higher emissions.

The main insights and implications are summarized as follows:

- Interpretation and mechanisms. The pattern of ENSO-health links is consistent with climate and behavioral pathways: heat and humidity stress and degraded air quality elevating cardiovascular risks; and environmental and systemic stresses increasing injury and external-cause mortality. The signal is persistent, indicating that El Niño's health burden propagates beyond the event window rather than being fully offset by quick rebounds in mortality improvement.
- Position within the literature and actuarial insights. U.S.-based studies have reported ENSO associations with infectious disease hospitalizations and influenza mortality, but findings were episodic and diseasespecific. This study extends that line of work with a unified, quantitative national risk model that integrates multi-cause mortality analysis, scenario-based projections, and economic valuation with traditional actuarial framework. It provides the actuarial community with a quantitative evidence base for understanding how climate anomalies shape population mortality assumptions, health trajectories, and insurance exposures.
- Granularity and attribution. Through life-expectancy changes decomposition and sub-causes analysis (e.g., heart disease within circulatory; transport accidents within external causes), this study identifies dominant causal pathways and illustrates how age-specific vulnerabilities evolve from immediate to cumulative fiveyear horizons. These insights enable actuaries and health system planners to refine stress-testing frameworks, longevity models, and capital adequacy projections under climate risk scenarios.

Click Here

## Section 1 Introduction

Climate anomalies are multi-month departures from average climate conditions that span large regions. A leading example is the El Niño-Southern Oscillation (ENSO) (McPhaden et al., 2006; Zebiak et al., 2015), whose warm (El Niño) and cool (La Niña) phases arise from anomalous equatorial Pacific sea-surface temperatures and associated atmospheric changes (McPhaden et al., 2006; Philander et al., 1984; C. Wang \& Fiedler, 2006). Unlike short-lived, localized hazards (Marlier et al., 2013; Ward et al., 2014; Zhang et al., 2012) (e.g., cyclones, floods, and droughts), ENSO modulates the frequency and intensity of multiple hazards over wide areas and over extended periods (Marlier et al., 2013; Ward et al., 2014; Zhang et al., 2012).

ENSO anomalies generate material economic and health consequences via teleconnections (Cai et al., 2015; Kovats et al., 2003; McGregor \& Ebi, 2018), with direct implications for insurers and health systems (Serre, 2022). The 2015-16 El Niño has been linked to multi-trillion-dollar global losses (Liu et al., 2023). Health pathways include degraded air quality, heat and humidity stress, infectious-disease dynamics, and disaster-related injuries; for example, ENSO-related circulation can elevate particulate matter in parts of East and Southeast Asia (Marlier et al., 2013), and the 2015-16 El Niño coincided with increased child underweight in developing countries (Anttila-Hughes et al., 2021).

In the continental U.S., El Niño's teleconnection is strongest in winter and shows a north-south contrast, roughly divided around $38^{\circ} \mathrm{N}$ (Figure 1). Northern states tend to experience warmer, drier winters, whereas southern states are typically wetter and cooler.

Figure 1
EL NIÑO IMPACT ON CONTINENTAL U.S. DURING WINTER
<img src="https://cdn.mathpix.com/cropped/f88ee05a-e03b-4a22-b3f7-fb4de14dfd94-05.jpg?height=734&width=901&top_left_y=1280&top_left_x=247" alt="image" style="width:100%;height:auto;">

Winter teleconnections associated with El Niño across the continental United States. Colors indicate the typical temperature and precipitation anomalies during El Niño winters, with warmer and wetter conditions shown in red and blue shades, respectively. States south of approximately $38^{\circ} \mathrm{N}$ generally experience cooler and wetter winters, while northern states tend to experience warmer and drier conditions.

Despite these observations, most existing studies examine isolated mechanisms or single episodes of El Niño impacts, such as outbreaks of infectious diseases or localized mortality shocks, without establishing a comprehensive, quantitative framework that links ENSO variability to long-term health and cause-specific mortality risks.

Emerging evidence further indicates that El Niño impacts can persist well beyond the event window. For example, El Niño can depress economic output (Callahan \& Mankin, 2023) and slow down mortality improvement (Xu et al., 2025) for over a decade, and ENSO variability has been connected to delayed but severe outcomes such as the 2019-20 Australian "Black Summer" fires (Ehsani et al., 2020; G. Wang \& Cai, 2020). Yet, the extent to which such persistence propagates through health systems, insurance outcomes, and actuarial forecasts, remains weakly quantified.

This report addresses that gap. It quantifies the impact of ENSO-driven climate anomalies on U.S. health outcomes and healthcare demand. The health-specific impact of ENSO is evaluated using cause-specific mortality improvement as the primary outcome measure. This research uses cause-specific mortality improvement-defined as the first-order log difference of cause-specific mortality rates-as the health impact measure. This transformation reduces potential non-stationarity and yields a more stable, statistically robust specification, allowing identification of both short- and long-term ENSO effects more reliably. The research develops and applies an econometric framework to measure ENSO-related health losses in the past and to estimate the associated demand on healthcare expenditure under future climates. The analysis first quantifies the short-run and persistent effects of ENSO on mortality and health outcomes using historical data with explicit identification and robustness checks (Sections 4.14.4). It then monetizes the loss relevant for providers and insurers (Sections 4.5). Finally, it projects future losses and capacity demand under climate-change scenarios by combining the estimated relationships with modelled changes in ENSO and related anomalies under SSP1, SSP2, SSP3, and SSP5 (Section 4.6).

This report presents, to the authors' knowledge, the first U.S.-focused, policy-oriented modelling framework that jointly quantifies ENSO-driven health outcomes and future losses intensified by anthropogenic climate change. This study provides the actuarial community quantitative evidence linking climate anomalies to shifts in cause-specific mortality improvement and health-care cost trajectories. The findings underscore three key policy and actuarial priorities: (i) embedding climate-sensitive assumptions into mortality and morbidity models; (ii) integrating ENSO early-warning indicators into public-health preparedness and insurer stress-testing frameworks; and (iii) strengthening coordination between climate forecasting, actuarial modelling, and health-system resource planning.

The rest of the report is organized as follows. Section 2 reviews existing evidence on ENSO's effects on U.S. public health. Section 3 describes the data and actuarial methods. Section 4 presents the results. Section 5 concludes and discusses policy implications.

## Section 2 Existing Evidence of ENSO Impacts on U.S. Public Health

On the health and mortality front, research within the U.S. context is more limited but consistently indicates that ENSO influences a wide range of health outcomes. Fisman et al. (2016) found that, across multiple U.S. census regions, ENSO phases were associated with significant variations in hospitalizations for infectious diseases, suggesting that large-scale climate anomalies can shape national morbidity patterns. At the state level, Choi et al. (2006) reported a statistically significant link between El Niño conditions and elevated influenza-related mortality in California.

Building on these findings, Xu et al. (2025) provided the first quantitative national-level assessment of ENSO's impact on U.S. mortality and welfare loss. Using an econometric framework linking the ENSO E-index to age-specific mortality improvements, the study estimated that the five-year cumulative impact of El Niño events on all-cause mortality improvement was 2.1 percentage points (p.p.; $95 \% \mathrm{Cl}: 0.6-3.6$ ). The associated life-expectancy loss was 0.8 years for the 1982-83 event and 0.4 years for the 1997-98 event, corresponding to welfare losses of approximately USD 2.0 trillion and 3.6 trillion (2020 dollars), respectively. These results indicate that ENSO-induced health impacts can rival the scale of major macroeconomic shocks and underscore the persistence of their effects on population wellbeing.

Together, this body of evidence suggests that ENSO exerts measurable and economically significant influences on U.S. health outcomes, yet systematic assessments remain scarce. The present report extends this line of inquiry by developing a formal econometric framework to quantify these health losses, evaluate their implications for healthcare expenditure, and project their evolution under future climate scenarios.

## Section 3 Methods

### 3.1 DATA

#### 3.1.1 CAUSE-SPECIFIC MORTALITY DATA

The cause-specific mortality data is concluded from the state-level mortality data and the life-level cause-specific death dataset. State-level total population mortality data is obtained from the U.S. Human Mortality Database (United States Mortality DataBase, 2024). For all mortality tables, five-year age intervals and one-year time intervals (i.e., $5 \times 1$ ) are selected. Life-level cause-specific death data is obtained from 1981 to 2023 from the CDC Wonder database (Centers for Disease Control and Prevention, 2024).

Deaths are aggregated by state-year-age group, merged with the mortality tables, and cause-specific mortality rates are computed by allocating each state-year's total mortality rate across causes using that state-year's cause-ofdeath shares from CDC Wonder.

#### 3.1.2 ECONOMIC CONTROL DATA

Because El Niño significantly affects the macroeconomy (Burke et al., 2015; Callahan \& Mankin, 2023; Hsiang \& Meng, 2015), state-level macroeconomic conditions are controlled for using the Federal Reserve Economic Database (FRED Economic Data, 2024), specifically per-capita personal income and the unemployment rate.

#### 3.1.3 HISTORICAL METEOROLOGICAL DATA

Monthly land surface air temperature are used from Berkeley Earth (Rohde \& Hausfather, 2020), sea-surface temperature (SST) from HadISST (Rayner et al., 2003), and precipitation data from GPCC (Schneider et al., 2016). Data are used at the native $1^{\circ} \times 1^{\circ}$ latitude-longitude resolution. Berkeley Earth and GPCC are then summarized to state-level time series for analysis.

#### 3.1.4 CLIMATE PROJECTION DATA

Climate simulations for future sea surface temperature data are used from Coupled Model Intercomparison Project Phase 6 (CMIP6) (O'Neill et al., 2016). The data span from 1850 to 2099 covering historical simulations and Shared Socioeconomic Pathways (SSP) projections (SSPs; SSP1-2.6, SSP2-4.5, SSP3-7.0, and SSP5-8.5). These scenarios cover a broad spectrum of potential future policies, from significant mitigation efforts (SSP1-2.6) to scenarios of continued high emissions (SSP5-8.5). These scenarios span strong mitigation (SSP1-2.6) to continued high emissions (SSP5-8.5). By 2081-2100 relative to 1995-2014, the multimodel warming is on the order of $\sim 1.2^{\circ} \mathrm{C}$ (SSP1-2.6), $\sim 2.1^{\circ} \mathrm{C}$ (SSP24.5 ), ${ }^{\sim} 3.2^{\circ} \mathrm{C}$ (SSP3-7.0), and $\sim 4.0^{\circ} \mathrm{C}$ (SSP5-8.5) (O'Neill et al., 2016; Tebaldi et al., 2021).

Many CMIP6 models struggle to capture the physics of ENSO (Karamperidou et al., 2017; Seager et al., 2019). To screen for more realistic simulations, prior work is followed that quantifies ENSO nonlinearity using the quadratic coefficient ( $\alpha$ ) from a regression of first and second Principal Components (PC) (see Section 3.2 for details). Observations yield $\alpha \approx-0.34$, indicating strong nonlinearity and a clear separation between eastern-Pacific and central-Pacific El Niño flavors (Callahan \& Mankin, 2023). Following Cai et al. (2022), simulations with $\alpha<-0.17$ are retained. Starting from MIROC6 (Tatebe et al., 2019), this criterion yields 198 ensembles across four SSPs ( 48 for SSP1-2.6, 50 for SSP2-4.5, 50 for SSP3-7.0, and 50 for SSP5-8.5).

#### 3.1.5 FUTURE POPULATION AND PRODUCTION PROJECTION DATA

Following Xu et al. (2025), the national level future Gross Domestic production (GDP) and population projection data is obtained from the International Institute for Applied Systems Analysis (IIASA) SSP Database version 2. The IIASA database provides population projections by five-year age groups, which allows to account for future demographic shifts in estimates.

### 3.2 ENSO MEASURE

#### 3.2.1 INTENSITY MEASURES

To quantify ENSO, the E-C index framework is used (Cai et al., 2020, 2022; Callahan \& Mankin, 2023; Jia et al., 2021; Ng et al., 2021; Takahashi et al., 2011). The E index measures variability of SST anomalies in the eastern equatorial Pacific (the canonical EP type), while the C index measures variability in the central Pacific (the CP type). The two indices are constructed from a rotation of the first two PCs of tropical Pacific SST anomalies and are orthogonal by design (uncorrelated at zero lag). Positive E (C) denotes an EP-type (CP-type) El Niño, and negative values denote the corresponding La Niña. Unlike Niño-3/Niño-4, which can be correlated and partly redundant, the E and C indices provide separate, non-overlapping measures of eastern vs. central Pacific ENSO variability.

The E and C indices are derived from the first two PCs of an empirical orthogonal function analysis of tropical Pacific SST anomalies ( $20^{\circ} \mathrm{S}-20^{\circ} \mathrm{N}, 140^{\circ} \mathrm{E}-80^{\circ} \mathrm{W}$, shown in Figure 2) (Callahan \& Mankin, 2023; Takahashi et al., 2011) over 1960-2023. The PCs identify the dominant spatial modes and their associated time series: $E=(P C 1-P C 2) / \sqrt{2}$ and $C=(P C 1+P C 2) / \sqrt{2}$, isolate EP and CP ENSO variability, respectively.

Figure 2
REGION OF SEA SURFACE TEMPERATURE ESTIMATION
<img src="https://cdn.mathpix.com/cropped/f88ee05a-e03b-4a22-b3f7-fb4de14dfd94-09.jpg?height=824&width=1122&top_left_y=1439&top_left_x=249" alt="image" style="width:100%;height:auto;">

Global raster of sea surface temperature example. The black rectangle marks the SST study domain $\left(20^{\circ} \mathrm{S}-20^{\circ} \mathrm{N}, 140^{\circ} \mathrm{E}-80^{\circ} \mathrm{W}\right)$ spanning the Maritime Continent and equatorial Pacific used for the regional statistics/index calculations.

For each year, the E index over DJF (December-February) is averaged to target the season of peak ENSO influence (Ng et al., 2021). For climate projections, DJF E and C is computed analogously in CMIP6, using quadratically
detrended SST anomalies referenced to 1850-2014 monthly means. The DJF E-C indices obtained for each year are presented in Figure 3.

Figure 3
E-INDEX AND C-INDEX BY YEAR
<img src="https://cdn.mathpix.com/cropped/f88ee05a-e03b-4a22-b3f7-fb4de14dfd94-10.jpg?height=738&width=1331&top_left_y=470&top_left_x=242" alt="image" style="width:100%;height:auto;">

December-January-February E-C indices. (A) E-index and (B) C-index.
Previous analyses shows that the C index and its teleconnections have limited explanatory power for changes in mortality improvement compared with E (Xu et al., 2025), consistent with recent findings on the dominant impacts of EP-type El Niño on socioeconomic outcomes (Cai et al., 2022; Callahan \& Mankin, 2023). This research, therefore, focuses on E and omits C from the main model to conserve degrees of freedom.

#### 3.2.2 TELECONNECTIONS

To quantify spatial heterogeneity in ENSO sensitivity, state-specific teleconnection metrics are constructed. For each state, monthly surface temperature and precipitation are standardized by removing the 1960 to 2023 monthly climatology and dividing by the corresponding monthly standard deviation; the resulting anomalies are then linearly detrended to suppress warming and other low-frequency variability.

Teleconnections are computed by correlating these standardized anomalies with the DJF E-index month by month for each state (Callahan \& Mankin, 2023; Liu et al., 2023). Because El Niño typically develops in year $t-1$, peaks in the winter, and decays through spring-summer of year $t$, influence from June of $t-1$ through August of $t$ is allowed, yielding 15 monthly correlations per state for temperature and for precipitation (see Figure 4). The state teleconnection is the average of these 15 coefficients, denoted as $\tau^{\top}$ and $\tau^{\mathrm{P}}$, respectively.

Figure 4

STATE-LEVEL TEMPERATURE AND PRECIPITATION ENSO TELECONNECTIONS
<img src="https://cdn.mathpix.com/cropped/f88ee05a-e03b-4a22-b3f7-fb4de14dfd94-11.jpg?height=669&width=1620&top_left_y=352&top_left_x=247" alt="image" style="width:100%;height:auto;">

U.S. state-level teleconnections with the ENSO E-index. (A) Temperature and (B) precipitation.

### 3.3 CAUSE-SPECIFIC MORTALITY IMPROVEMENT

The effect of extreme ENSO events on cause-specific mortality improvement and life expectancy are studied using the observed cause- and age-specific mortality rate $m_{x t}^{c}$ for each cause $c$, year t and age $x$ (Dickson et al., 2009). The cause-specific mortality improvement for age $x$ from $t-1$ to $t$ is the log change in the observed rate:

$$
m i_{x t}^{c}=\log m_{x t}^{c}-\log m_{x(t-1)}^{c} .
$$

Using the econometric specification described below, the impact of extreme ENSO on the improvement rate, $\Delta_{x t}^{c}$ is estimated. A counter factual improvement is formed by removing this impact:

$$
\hat{m} i_{x t}^{c}=m i_{x t}^{c}-\Delta_{x t}^{c} .
$$

Next, the counterfactual mortality rate $\hat{\boldsymbol{m}}_{x t}$ is recovered by applying the counterfactual improvement forward from the baseline year $t_{0}$ :

$$
\hat{m}_{x t}^{c}= \begin{cases}\hat{m}_{x(t-1)}^{c} \cdot \exp \left[\hat{m} i_{x t}^{c}\right] & \text { for } t>t_{0}, \\ m_{x t}^{c} & \text { for } t=t_{0} .\end{cases}
$$

Finally, observed and counterfactual life expectancies are computed from their respective mortality schedules using standard life-table methods.

Mortality improvement is generally negative, reflecting ongoing advances in technology and economic development. Therefore, a positive shift in mortality improvement indicates an impediment to progress.

### 3.4 ECONOMETRIC MODEL

The lasting effect of ENSO on cause-specific mortality improvement is estimated using a distributed-lag regression with country-age fixed effects. The distributed lag regression model is extended with fixed effect employed by Xu et al. (2025) to cause-specified mortality improvement, estimated using Ordinary Least Squares (OLS):

$$
m i_{i x t}^{c}=\sum_{l=0}^{L}\left(\beta_{0 l}^{c}+\beta_{1 l}^{c} \cdot \tau_{\mathrm{i}}^{\mathrm{P}}+\beta_{2 l}^{c} \cdot \tau_{\mathrm{i}}^{\mathrm{T}}\right) E_{t-l}+\text { Controls }_{i t}+u_{i x}^{c}+\varepsilon_{i x t}^{c} .
$$

Here, the mortality improvement for cause $c$, state $i$, age group $x$, and year $t$ as $m i_{i x t}^{c}$ are indexed. $E_{t}$ represents the E-index in year $t$. The interaction of $E_{t}$ with $\tau_{\mathrm{i}}^{\mathrm{T}}$ and $\tau_{\mathrm{i}}^{\mathrm{P}}$ allows the effect of ENSO to vary by state via temperature and precipitation teleconnections. Fixed effect $\boldsymbol{U}_{i x}^{c}$ is used to capture time-invariant cause-state-age heterogeneity. A year-fixed effect is omitted in the model, because the E-index is a cross-sectional constant within each year. Instead, a pandemic dummy is included to account for the impact of COVID-19 from 2020 to 2022.

The distributed-lag structure distinguishes transient shocks from enduring changes. A purely short-lived disruption would be followed by a rebound in mortality improvement. Accordingly, the inference centers on the cumulative effect over $L$ years:

$$
\Theta_{i L}^{c}=\sum_{l=0}^{L}\left(\beta_{0 l}^{c}+\beta_{1 l}^{c} \cdot \tau_{\mathrm{i}}^{\mathrm{P}}+\beta_{2 l}^{c} \cdot \tau_{\mathrm{i}}^{\mathrm{T}}\right)
$$

If $\Theta_{i L}^{c} \neq 0$ is statistically significant, the hypothesis that El Niño has only a short-term effect is rejected. The interaction of the two variables enables the calculation of the cumulative effect for each state over lag length $L$.

To assess statistical significance and guard against occasional outliers or within-group correlation, bootstrap resampling with 1,000 iterations is used. The coefficients are estimated for each cause separately to control for cause heterogeneity.

### 3.5 PROJECTED FUTURE LIFE EXPECTANCY LOSS

To quantify the role of ENSO itself, an ENSO-neutral counterfactual was constructed. A scenario was imposed in which the ENSO is always neutral (E-index=0), from the historical baseline through 2099. This counterfactual removes all interannual ENSO variability while holding the rest of the climate projection fixed. This ENSO-neutral run is compared with the "realistic" scenario, in which the E-index is allowed to vary according to the model-projected future SSTs. For each year and realization (2020-2099), mortality improvements using the cause- and state-specific lag responses are computed, and the cumulative ENSO impact is defined as the difference between the ENSOvarying scenario and the ENSO-neutral counterfactual:

$$
\Delta_{i x(t+1)}^{c}=\left(\beta_{0 l}^{c}+\beta_{1 l}^{c} \cdot \tau_{\mathrm{i}}^{\mathrm{P}}+\beta_{2 l}^{c} \cdot \tau_{\mathrm{i}}^{\mathrm{T}}\right) \cdot\left(E_{t}-\hat{E}_{t}\right)
$$

The counterfactual mortality improvement is then calculated for year by removing $\Delta_{i x(t+1)}^{c}$ from the corresponding actual mortality improvement following Eq. (1.2).

Previous literature usually adjusts the ENSO amplitude to its historical level (as in Callahan \& Mankin, 2023; Xu et al., 2025), but this method gives a cleaner identification of the ENSO contribution. ENSO is removed altogether rather than making assumptions about how much its amplitude should be scaled, thus the difference is therefore fully attributable to "having ENSO vs. not having ENSO."

### 3.6 MONETIZE LIFE EXPECTANCY LOSS

The monetary burden of life expectancy loss from El Niño is estimated using a willingness-to-pay approach, specifically the Value of Statistical Life (VSL) method. VSL is a widely used concept in health economics and policy for quantifying the trade-off between income and the risk of death (Aldy \& Viscusi, 2008; Nandi et al., 2022; Scott et al., 2021; Viscusi \& Masterman, 2017).

VSL measures the marginal rate of substitution between wealth and the probability of dying. For example, if the average individual is willing to pay $\$ 1,000$ for a one in 10,000 reduction in their probability of death, then it would require 10,000 such individuals to make this payment collectively to reduce the expected number of deaths by one "statistical life." This corresponds to a collective willingness to pay (or VSL) of $\$ 10$ million.

The 2020 U.S. median VSL is taken as the baseline and project VSL in subsequent years using Gross National Income per Capita (GNIPC). According to the U.S. Department of Health and Human Services (HHS), the median VSL in 2020 was $\$ 11.4$ million (2020 dollars). Because VSL is positively correlated with income (Aldy \& Viscusi, 2008; Nandi et al., 2022; Scott et al., 2021; Viscusi \& Masterman, 2017), it is adjusted over time (and across countries) using GNIPC. After adjusting for inflation and expressing all values in constant 2020 dollars, the VSL for any country $i$ in year $t$ can be estimated as:

$$
V S L_{t}=V S L_{2020} \cdot\left(\frac{G N I P C_{t}}{G N I P C_{2020}}\right)^{\xi}
$$

The parameter $\xi$ represents the income elasticity of VSL, which measures the percentage change in VSL associated with a $1 \%$ change in real income. Following the literature convention (Nandi et al., 2022, Robinson et al., 2019; Xu et al., 2025) and recommendation of HHS, $\xi=1$ is chosen.

Following previous research on the valuation of changes in life expectancy (Nandi et al., 2022; Robinson et al., 2019; Xu et al., 2025), the concept of the value of a statistical life year (VSLY) is applied to estimate the economic value of life years lost due to El Niño for each age group. The VSLY is derived by distributing the VSL over the remaining life expectancy at the average age ( $e_{\bar{i} \bar{t}}$ ) without discounting:

$$
V S L Y_{i t}=V S L_{i t} / e_{i \bar{x} t}
$$

The country-age-year-specific per statistical life monetary value loss from El Niño is computed by multiplying the country-year-specific VSLY with the country-age-year-specific life expectancy loss, discounted over the remaining life expectancy:

$$
L o s s_{i x t}=V S L Y_{i t} \cdot\left(\hat{e}_{i x t}-e_{i x t}\right) \cdot \exp \left(-r e_{i x t}\right)
$$

Here, realized life expectancy $\boldsymbol{e}_{\text {ixt }}$ and counterfactual life expectancy $\hat{\boldsymbol{e}}_{\text {ixt }}$.
To estimate future VSL under each SSP, future GNIPC is projected. First a linear regression model is fit between historical national GNI and GDP of each year, then model is used to estimate projected GNI using the future GDP projection (see Section 3.1.5) under each scenario:

$$
G N I_{t}=\beta_{0}+\beta_{1} G D P_{t}+\varepsilon_{t}
$$

Combining the GNI projection with projected population, the GNIPC by year is obtained for each scenario. The future VSL under each SSP is then projected using Equation (1.7) with reference to VSL and GNIPC for year 2020.

### 3.7 ATTRIBUTE LIFE EXPECTANCY TO CAUSE

Changes in life expectancy at birth are attributed to each cause of death using the Pollard decomposition method (Pollard, 1982, 1988). This approach decomposes the total change in life expectancy between two time points into additive contributions from age- and cause-specific mortality differences. Specifically, Pollard showed that the difference in life expectancy between observed and counterfactual can be expressed as:

$$
\hat{e}_{0}-e_{0}=\int_{0}^{\infty}\left(m_{x}-\hat{m}_{x}\right) \cdot w(x) d x
$$

where $\hat{\boldsymbol{e}}_{0}$ and $\boldsymbol{e}_{0}$ denote the counterfactual and observed life expectancy at age 0 , and $\boldsymbol{w}(x)$ is a weighting function defined as

$$
w(x)=\frac{1}{2}\left(l_{x} \hat{e}_{x}-\hat{l}_{x} e_{x}\right)
$$

For an age specific interval $[x, x+n)$, the contribution to the change in life expectancy is calculated as:

$$
\Delta e_{x}=-\frac{n}{2}[w(x)+w(x+n)] \cdot\left(m_{x}-\hat{m}_{x}\right) .
$$

This decomposition provides a rigorous way to identify the contribution of each age and cause of death to the overall change in life expectancy. It allows for distinguishing whether observed life expectancy losses during El Niño years arise primarily from changes in chronic diseases, external causes, or other health categories, forming the basis for the cause-specific attribution.

Figure 5 reports the life expectancy at birth attribution to circulatory system, external causes, and other causes. The results show that over the past two decades, circulatory system mortality accounted for the largest share of life expectancy gains ( $\approx 1.34$ years), while improvements in other causes contributed an additional 1.19 years. In contrast, external causes exerted a negative contribution ( -0.38 years), partially offsetting overall health progress.

Figure 5
LIFE EXPECTANCY IMPROVEMENT ATTRIBUTION TO CAUSE OF DEATH
<img src="https://cdn.mathpix.com/cropped/f88ee05a-e03b-4a22-b3f7-fb4de14dfd94-15.jpg?height=728&width=1084&top_left_y=431&top_left_x=244" alt="image" style="width:100%;height:auto;">

Life expectancy improvement in the United States attributed to major causes of death from 2000 to 2019. The stacked areas show the cumulative contributions of circulatory system diseases (blue), external causes (red), and all other causes (light blue) to total life expectancy improvement, with the black line indicating the overall trend. The results show that over the past two decades, circulatory system mortality accounted for the largest share of life expectancy gains ( $\approx 1.34$ years), while improvements in other causes contributed an additional 1.19 years. In contrast, external causes exerted a negative contribution ( -0.38 years), partially offsetting overall health progress.

## Section 4 Results

### 4.1 ENSO'S CAUSE-SPECIFIC IMPACT ON MORTALITY IMPROVEMENT

El Niño events show a pronounced and statistically significant impediment to mortality improvement in circulatory system diseases, external causes, and endocrine/metabolic conditions (Figure 6a). Among these, circulatory system diseases exhibit the largest adverse effect 4.8 (Cl: 2.1 to 7.5), indicating that cardiovascular mortality improvement slows considerably during El Niño periods, consistent with the heightened cardiovascular stress associated with elevated temperatures (Chen et al., 2021) and air pollution (Cui \& Sinoway, 2014). External causes, which encompass accidental and injury-related deaths, also show substantial slowdown in mortality improvement 5.0 (Cl: 3.2 to 6.8), suggesting behavioral and environmental stress pathways linked to anomalous heat and precipitation patterns. Endocrine and metabolic diseases display a significant but less precisely estimated effect 11.5 (Cl: 2.0 to 20.1), while several other causes show positive but statistically insignificant coefficients, implying limited or uncertain benefits from El Niño conditions at the national level.

Figure 6
ENSO IMPACT ON CAUSE SPECIFIC MORTALITY IMPROVEMENT
<img src="https://cdn.mathpix.com/cropped/f88ee05a-e03b-4a22-b3f7-fb4de14dfd94-16.jpg?height=1118&width=1490&top_left_y=1022&top_left_x=242" alt="image" style="width:100%;height:auto;">

(a) presents estimates for the full sample period, and (b) shows results split by the 1999 ICD code transition from ICD-9 to ICD-10. Each row corresponds to a cause-of-death chapter, with the number in parentheses indicating the average annual number of deaths nationwide. Estimates represent the five-year cumulative effect of El Niño anomalies on mortality improvement (percentage points, p.p.), with $95 \%$ confidence intervals shown. In (a), darker red (blue) shading indicates that El Niño persistently impeded (enhanced) mortality improvement across the full sample period. In (b), lighter red and blue shades denote causes where El Niño effects were significant in only one of the two subperiods.

When the sample is divided by the 1999 ICD transition (Figure 6b), circulatory system diseases and external causes remain consistently impeded by El Niño across both the ICD-9 (1981-98) and ICD-10 (2000-23) periods, underscoring the robustness of these relationships. The impact on endocrine and metabolic diseases, however, emerges only in the post-ICD-10 period. While the impact of ICD transition cannot be ruled out, this discrepancy indicates a possible intensification of metabolic vulnerability in more recent decades, potentially linked to aging populations and lower resilience. Interestingly, respiratory system mortality shows a positive association with EI Niño during the ICD-9 period 5.4 (Cl: 1.9 to 11.0), suggesting temporary health benefits, but this effect disappears after the ICD-10 transition, implying that medical or reporting changes may have altered the observed sensitivity.

Previous studies generally find that El Niño tends to impede mortality improvement, whereas La Niña is associated with health benefits (Xu et al., 2025). However, the results if this study show that the benefit is not universal across causes. While La Niña phases are linked to improvements in several major disease categories, they correspond to increased mortality in infectious diseases (nationwide) and congenital disorders (in both subsamples). These findings suggest that La Niña can introduce specific health risks despite its overall moderating influence on temperature extremes. The heterogeneous responses across cause-of-death categories highlight the complex and asymmetric pathways through which ENSO phases shape population health in the United States.

Respiratory causes of death are likely to be regionally linked to ENSO. Previous studies have shown that wildfires in the U.S. Southwest are more strongly associated with La Niña conditions. A recent example is the 2025 Los Angeles fire (Becker, 2025). This is because La Niña tends to bring warmer, drier conditions to that region (see Figure 1), which increases fire risk and smoke exposure. In the results, respiratory mortality during La Niña was not statistically significant at the national level but was still measurable (Figure 6a), likely because the effect is concentrated in southwestern states rather than widespread. A more detailed, region-specific analysis would be needed to fully resolve this.

### 4.2 FURTHER BREAKDOWN FOR CIRCULATORY SYSTEM AND EXTERNAL CAUSES OF DISEASE

The two major causes most affected by El Niño (circulatory system and external causes) are broken down into their constituent sub-causes (Anderson et al., 2001) to better identify the drivers of the aggregate effects (Figure 7). Within circulatory diseases, the largest and most statistically significant impediment is observed for diseases of the heart. Cerebrovascular diseases also show a negative but less precisely estimated impact, while other sub-causes, such as hypertension and atherosclerosis, display positive yet statistically insignificant effects. This pattern suggests that El Niño primarily affects cardiovascular mortality through pathways related to heart disease rather than other circulatory conditions.

For clarity, Table 1 summarizes how each circulatory subcause in the analysis is defined in the mortality data.

Table 1
DEFINITION OF CIRCULATORY SUBCAUSES AND CORRESPONDING ICD CODES
| Subcause | Typical Conditions | ICD-10 Codes |
| :--- | :--- | :--- |
| Diseases of heart | Coronary/ischemic heart disease (MI, angina), heart failure, cardiomyopathy, arrhythmias, rheumatic/valvular and other structural heart disease; some hypertensive heart disease | I000-I099, I110-I119, I130-I139, I200-I519 |
| Essential (primary) hypertension \& hypertensive renal disease | Chronic high blood pressure; hypertension with kidney involvement | I100-I109, I120-I129 |
| Cerebrovascular diseases | Stroke and sequelae: hemorrhagic \& ischemic stroke, late effects | 1600-1699 |
| Atherosclerosis | Systemic arterial plaque/arteriosclerosis coded as underlying cause | 1700-1709 |
| Other diseases of circulatory system | Residual group | 1710-1789 |


Figure 7
SUB-CAUSE ANALYSES ON CIRCULATORY AND EXTERNAL CAUSE OF DEATH
<img src="https://cdn.mathpix.com/cropped/f88ee05a-e03b-4a22-b3f7-fb4de14dfd94-19.jpg?height=1193&width=1187&top_left_y=350&top_left_x=247" alt="image" style="width:100%;height:auto;">

Estimates represent the five-year cumulative effect of El Niño anomalies on mortality improvement (percentage points, p.p.), with $95 \%$ confidence intervals shown. Each row corresponds to a specific subcause within the broader circulatory (blue) or external (red) categories, with the number in parentheses indicating the average annual deaths nationwide. Within circulatory causes, the largest and most statistically significant impediment is observed for diseases of the heart, followed by cerebrovascular diseases. For external causes, the strongest effects occur in transport accidents and complications of medical and surgical care, both indicating substantial slowdowns in mortality improvement during El Niño periods.

Among external causes, the strongest adverse effects are found for transport accidents and complications of medical and surgical care.

Both categories exhibit significant slowdowns in mortality improvement, pointing to a combination of behavioral, environmental, and systemic stress factors, through acute disease systems.

### 4.3 AGE-SPECIFIC VULNERABILITY

The five-year cumulative effects (Figure 8a) show that El Niño exerts a persistent impediment to mortality improvement across multiple causes of death, with the strongest and most widespread effects observed for circulatory system diseases among middle-aged and older adults. The impact intensifies progressively with age, emerging around ages $30-34$ and peaking between 50 and 80 years (six to seven p.p.). External causes also exhibit broad age-specific effects, with the largest deterioration in mortality improvement occurring between 35 and 44 years (five to six p.p.). A few other causes, such as nervous system and digestive system diseases, show statistically significant but age-constrained impacts-the former peaking at older ages (65-89, nine to 10 p.p.) and the latter in
midlife (35-49, greater than nine p.p.). Overall, the long-term evidence indicates that El Niño events slows down mortality improvement primarily through prolonged health burdens on older populations.

In comparison, the immediate effects at year 0 (Figure 8b) reveal a more selective pattern. The strongest short-term deterioration also occurs in circulatory system diseases, but the scale (zero to two p.p.) is much lower than the longterm. However, unlike the cumulative estimates, several other causes-including respiratory, digestive, and endocrine/metabolic conditions-show transient or statistically insignificant responses, suggesting that many health impacts materialize only after lagged physiological or socioeconomic processes take effect.

Together, the contrast between the short- and long-term effects highlights the persistence of El Niño's influence on long-term health outcomes and suggests that much of its population-level burden arises from delayed and compounding pathways rather than immediate mortality shocks.

Figure 8
ENSO IMPACT ON CAUSE SPECIFIC MORTALITY IMPROVEMENT.
<img src="https://cdn.mathpix.com/cropped/f88ee05a-e03b-4a22-b3f7-fb4de14dfd94-21.jpg?height=1597&width=1494&top_left_y=348&top_left_x=247" alt="image" style="width:100%;height:auto;">

(a) shows the five-year cumulative effect, while panel (b) presents the immediate (year 0 ) effect. Colors represent the direction and magnitude of the estimated effect (percentage points, p.p.), with red indicating impeded mortality improvement during El Niño phases and blue indicating enhanced improvement. Each row corresponds to a cause-of-death chapter and each column to an age group. Black circles denote statistically significant effects at the $95 \%$ confidence level. Results indicate that El Niño predominantly impedes mortality improvement in circulatory system diseases among middle-aged and older adults, while short-term and younger-age effects are more heterogeneous across causes.

### 4.4 IMPACT ON MENTAL HEALTH AND AGE/GENDER-SPECIFIC CONDITIONS

Mortality related to mental health shows a significant and gradually propagating response to ENSO anomalies (Figure 9). Mental health related mortality refers to deaths coded under ICD-10 F01-F99, which include dementia and other organic mental disorders, substance-use disorders, schizophrenia and other psychotic disorders, and mood (affective) disorders. The cumulative effect increases steadily over the five-year horizon, suggesting that the
adverse impacts of El Niño on mental health emerge and intensify over time rather than appearing immediately. This persistence aligns with recent evidence from Latin America (Flores et al., 2025; Ortiz-Prado et al., 2023), where ENSO-related climatic disruptions have been associated with elevated mental health burdens and suicide rates following prolonged economic and environmental stress. The delayed and progressive deterioration observed here may reflect post-catastrophe trauma, chronic stress, and indirect socioeconomic effects that compound beyond the initial climate shock.

By contrast, no statistically significant associations are detected for pregnancy- and perinatal-related mortality. Although small short-term variations are visible, their magnitudes remain within confidence bounds, indicating that maternal and neonatal mortality are largely unaffected by ENSO variability at the national scale. These results suggest that while ENSO events can have lasting mental health implications, their direct influence on reproductive and early-life outcomes in the U.S. appears limited.

ENSO IMPACT ON MORTALITY IMPROVEMENT RELATED TO MENTAL HEALTH, PREGNANCY AND CHILDBIRTH, AND PERINATAL CONDITIONS

Figure 9
<img src="https://cdn.mathpix.com/cropped/f88ee05a-e03b-4a22-b3f7-fb4de14dfd94-22.jpg?height=878&width=1639&top_left_y=968&top_left_x=244" alt="image" style="width:100%;height:auto;">

(a-c) upper panels show the cumulative effects of El Niño anomalies over a five-year horizon (top) and the corresponding age-attribution patterns (bottom). Positive values indicate impeded mortality improvement. The box indicates the intra-quartile range, the middle black line shows the median, and error bars denote $95 \%$ confidence intervals. The lower panels attribute the impact to each age.

### 4.5 CAUSE-SPECIFIC WELFARE LOSS IN THE PAST

Welfare losses associated with major El Niño events are quantified using a Value of Statistical Life approach, based on the estimated per-cause life expectancy loss (Methods). The results show that both the 1982-83 and 1997-98 events led to substantial reductions in life expectancy and corresponding welfare losses. The estimated life expectancy loss at birth was 0.64 years ( $95 \% \mathrm{Cl}: 0.20-1.10$ ) in 1983 and 0.44 years ( $95 \% \mathrm{Cl}: 0.15-0.73$ ) in 1997, with circulatory diseases contributing most of the total decline in both events. External causes exhibited smaller but statistically significant effects only in 1983. Translating these health losses into economic terms, the total welfare cost reached approximately USD 2.1 trillion (Cl: 0.6 to 3.5 billion) for 1983 and USD 3.6 trillion (Cl: 1.2 to 6.0 trillion) for 1997. The rest of the monetary equivalent loss estimations are reported in Table 2. These findings highlight that

El Niño events impose sizable and persistent welfare burdens on the U.S. population, primarily through elevated circulatory mortality risks.

Table 2
CAUSE-SPECIFIC WELFARE LOSSES IN THE UNITED STATES ASSOCIATED WITH MAJOR EL NIÑO EVENTS
| Cause | 1982-83 Event |  | 1997-98 Event |  |
| :--- | :--- | :--- | :--- | :--- |
| Panel A: Life expectancy at birth loss (yr.) |  |  |  |  |
| Circulatory | 0.13 | [0.07, 0.20] | 0.04 | [0.03, 0.07] |
| External | 0.02 | [0.01, 0.02] | 0.00 | [0.00, 0.00] |
| Total | 0.64 | [0.20, 1.10] | 0.44 | [0.15, 0.73] |
| Panel B: Economic equivalent value loss, total population (\$b.) |  |  |  |  |
| Circulatory | 433 | [133, 631] | 371 | [126, 614] |
| External | 53 | [17, 77] | 33 | [11, 55] |
| Total | 2,093 | [662, 3,502] | 3,639 | [1,241, 6,028] |


Panel A reports the estimated life expectancy loss at birth (in years) attributable to El Niño events in 1982-83 and 1997-98, with 95\% confidence intervals shown in brackets. Panel B presents the corresponding economic valuation of these losses, expressed as total welfare loss (in 2020 U.S. dollars, billions). Estimates are based on cause-specific mortality impacts for circulatory and external causes, aggregated to the national level.

### 4.6 QUANTIFY FUTURE HEALTH IMPACT OF ENSO

This study evaluates how intensified El Niño conditions under different climate change pathways will affect future U.S. life expectancy, focusing on cause-specific contributions and scenario uncertainty. Using 198 climate simulation ensembles across four SSPs, the median projected loss in life expectancy improvement for the United States is presented, along with cause-specific losses attributed to circulatory and external causes (Figure 10). The full-time series of life expectancy projections from each climate simulation ensemble is reported (Figure 11).

Adaptation capacity differs across the SSPs. SSP1-2.6 describes a sustainable, high-cooperation world with strong institutions and social cohesion, so adaptive capacity is highest, and health systems are well equipped to cushion ENSO shocks. SSP2-4.5 reflects current trends and adaptation improves but unevenly, resulting in moderate, incomplete protection. SSP3-7.0 is the most vulnerable pathway: fragmented growth and weaker governance mean low investment in health and infrastructure, so ENSO impacts are more fully realized. SSP5-8.5 depicts a highincome and technology-driven world that could support strong adaptation, but higher warming and exposure increase the demands on those systems, so effective adaptation is not guaranteed.

Under the mid-range climate scenario (SSP2-4.5), El Niño-related intensification is projected to remove roughly 3.1 years of life expectancy improvement at birth for the U.S. by the end of the century (Figure 10b). This represents a reversal exceeding the total gain achieved from 2000 to 2020 . If the cause-specific mortality improvement trends persist, external causes are expected to account for about 1.4 years of these losses, while circulatory system diseases contribute approximately 0.5 years. These findings indicate that El Niño events, when amplified by moderate climate change, could substantially erode long-term health progress and shift the dominant drivers of mortality loss toward injury-related and cardiovascular causes.

Across the four climate scenarios, the magnitude of life expectancy loss increases sharply with emission intensity, ranging from -1.6 to -4.3 years, with the largest median loss observed under SSP3-7.0 (Figure 10c). High-emission scenarios lead to persistently elevated El Niño frequency and severity, amplifying cumulative health burdens from
circulatory and external causes. Conversely, under the low-emission pathway (SSP1-2.6), projected losses are smaller and largely transitory, reflecting the benefit of climate mitigation in stabilizing ENSO variability. The widening contrast across scenarios underscores that future ENSO-related health impacts are not predetermined but depend critically on global emission pathways and adaptive public health capacity.

Figure 10
LIFE EXPECTANCY LOSS ATTRIBUTION TO CAUSE OF DEATH
<img src="https://cdn.mathpix.com/cropped/f88ee05a-e03b-4a22-b3f7-fb4de14dfd94-24.jpg?height=1399&width=1488&top_left_y=567&top_left_x=244" alt="image" style="width:100%;height:auto;">

Projected life expectancy loss attribution by cause of death under four climate change scenarios (SSP1-2.6, SSP2-4.5, SSP3-7.0, and SSP5-8.5). Each panel shows the median cause-specific contribution (year) to changes in life expectancy from 2020 to 2100, based on simulated ENSO intensification and associated health impacts. The black line represents the total effect across all causes, while shaded areas indicate the relative contributions from circulatory system diseases (blue), external causes (orange), and other causes (light blue).

Figure 11
LIFE EXPECTANCY LOSS ACROSS EMISSION SCENARIOS BY EACH SIMULATION
<img src="https://cdn.mathpix.com/cropped/f88ee05a-e03b-4a22-b3f7-fb4de14dfd94-25.jpg?height=1318&width=1486&top_left_y=352&top_left_x=244" alt="image" style="width:100%;height:auto;">

Projected life expectancy loss at birth across emission scenarios based on climate simulation ensembles across SSPs. Each panel corresponds to one SSP (SSP1-2.6, SSP2-4.5, SSP3-7.0, and SSP5-8.5), showing the trajectory of life expectancy improvement loss (years) from 2020 to 2100 for the U.S. Thin gray lines represent individual climate simulation ensembles, while the solid line denotes the ensemble mean and dashed and dotted lines indicate the 25th and 75th percentiles, respectively.

The monetary equivalent welfare loss is projected to be substantial. Under the mid-range climate scenario (SSP24.5), a mean ENSO-related welfare loss is projected for its impact on human health of about $\$ 25$ trillion (2020 dollars) for the U.S. during the $21^{\text {st }}$ century, with a wide uncertainty range [Cl: -75.9 to 17.7]. This reflects not only the health effect of ENSO on mortality, but also the socioeconomic conditions embedded in SSP2, namely moderate population growth and income expansion, which raise the value of future life years. Across the four pathways, expected total losses range from about \$18.7 trillion under SSP1-2.6 to \$40 trillion under SSP5-8.5.

Figure 12
MONETARY EQUIVALENT WELFARE LOSS
<img src="https://cdn.mathpix.com/cropped/f88ee05a-e03b-4a22-b3f7-fb4de14dfd94-26.jpg?height=804&width=1196&top_left_y=653&top_left_x=244" alt="image" style="width:100%;height:auto;">

Projected monetary-equivalent welfare losses attributable to ENSO, by cause of death and SSP scenario. Bars show the mean loss decomposed into circulatory causes, external causes, and all other causes. Right-hand labels report the total national loss and $95 \% \mathrm{Cl}$.

## Section 5 Discussion and Policy Implications

This report develops and applies an econometric and actuarial framework to quantify ENSO-related health losses in the U.S., attribute life-expectancy changes to specific causes of death, and value those losses in welfare terms. Historically, El Niño events have slowed mortality improvements, especially in circulatory and external causes, and produced measurable life-expectancy losses and large welfare costs. Looking forward, intensified ENSO activity under higher-emission pathways is projected to erode future life-expectancy gains, with the burden shifting toward injury-related and cardiovascular risks.

Relative to previous research, this study is a region-specific, actuarially interpretable assessment for the U.S. that consolidates the ENSO-health literature into a coherent, quantitative framework with detailed cause- and agespecific breakdowns, explicit identification, and projections under CMIP6-SSP scenarios. It complements prior episode- or mechanism-focused studies (Kovats et al., 2003; Xu et al., 2025) by offering a national and cross-cause lens.

### 5.1 POLICY AND ACTUARIAL IMPLICATIONS

The results of this report point to three actionable domains for health systems, regulators, and the actuarial profession:

1. Preparedness and early response: When ENSO outlooks signal emerging El Niño conditions, public-health agencies and insurers can activate anticipatory interventions, for example, seasonal heat-health and airquality protocols, targeted cardiovascular risk management, injury-prevention messaging, mental-health outreach, and mortality surveillance in older age groups. These measures reduce immediate health losses and moderate downstream actuarial liabilities.
2. Capacity and supply planning and resilience: Hospitals and public programs could pre-position staff, beds, and critical supplies in states with stronger temperature and precipitation teleconnections; stress-test emergency and trauma systems for potential injury surges; and plan respiratory and cardiac care surge capacity during El Niño years. In parallel, life and health insurers can use ENSO outlooks to forecast shortterm claims volatility, stress-test capital requirements, and align solvency buffers and reinsurance layers with projected morbidity and hospitalization surges. Together, these actions enhance both operational resilience and financial preparedness against climate-related health shocks.
3. Risk pricing, reserving, and long-term modeling: ENSO uncertainties can be considered within benefit pricing, reserving, and reinsurance design. Insurers may develop ENSO-linked parametric triggers for catastrophe or stop-loss contracts, while regulators and actuarial bodies can promote climate-adjusted mortality improvement assumptions in valuation bases and solvency analyses. Such integration aligns actuarial practice with national climate adaptation policies and strengthens long-term financial protection frameworks for the health sector.

### 5.2 LIMITATIONS AND NEXT STEPS

In the current analysis, the core econometric specification is linear in the ENSO signal and uses a fixed lag structure; non-linearities, thresholds, or interactions across hazards and causes warrant further investigation. The analysis is national with state-level heterogeneity via teleconnections but cannot resolve intra-state or urban-rural disparities. Future work needs to incorporate higher-resolution health data (insurance claims, admissions), richer exposure metrics, flexible non-linear or semi-parametric models, and explicit adaptation pathways to validate and refine these estimates. Extending this framework to broader geographic regions - such as other regions in North America, Australia, Asia-Pacific, Latin America, and Sub-Saharan Africa-and eventually to a global analysis would enable comparative insights into how ENSO and other climate anomalies drive differential health and actuarial risks across diverse socioeconomic and climatic contexts.

This report's projections of future ENSO-related health impacts are based on CMIP6 climate model outputs. Because CMIP6 was designed and its experiment protocols were finalized around 2015, it does not fully incorporate more recent advances in climate science on future ENSO dynamics. Recent studies suggest that La Niña events may become shorter and weaker in a warmer climate, and that ENSO variability may become more El Niño-biased (see, for example, Lawman et al., 2022). Consistent with this, operational updates from NOAA noted that the 2024-25 La Niña, which followed the strong 2023 El Niño, was weak and ended quickly, likely because anomalously warm ocean conditions suppressed its development (see NOAA's April 2025 ENSO update). An El Niño-biased ENSO regime is particularly concerning from a health perspective, because the analysis shows that El Niño generally worsens human health outcomes. This means the projections in this report should be interpreted as a conservative, lower-bound estimate of the losses that could potentially materialize in the future. These newer process-level insights are not yet fully represented in the CMIP6 models; future projections that use updated climate simulations incorporating these mechanisms would provide a more realistic assessment of ENSO-related health risks.

Click Here

## Section 6 Acknowledgments

The authors' deepest gratitude goes to those without whose efforts this project could not have come to fruition: the volunteers who generously shared their wisdom, insights, advice, guidance, and arm's-length review of this study prior to publication. Any opinions expressed may not reflect their opinions nor those of their employers. Any errors belong to the authors alone.

Project Oversight Group members:
Andre Chen, ASA
Andrew Dilworth, FSA, MAAA
Jing Feng, FSA, MAAA
Sam Gutterman, FSA, FCAS, MAAA, CERA, FCA, HonFIA
Rebecca Owen, FSA MAAA FCA
Mark Velkoff, FCAS
Nathan Worrell, FSA
At the Society of Actuaries Research Institute:
Rob Montgomery, ASA, MAAA, Research Project Manager
Barbara Scott, Sr. Research Administrator

## References

Aldy, J. E., \& Viscusi, W. K. (2008). Adjusting the value of a statistical life for age and cohort effects. The Review of Economics and Statistics, 90(3), 573-581.

Anderson, R. N., Miniño, A. M., Hoyert, D. L., \& Rosenberg, H. M. (2001). Comparability of cause of death between ICD-9 and ICD-10: Preliminary estimates (National Vital Statistics Reports, 49[2]). National Center for Health Statistics.

Anttila-Hughes, J. K., Jina, A. S., \& McCord, G. C. (2021). ENSO impacts child undernutrition in the global tropics. Nature Communications, 12(1), 5785. https://doi.org/10.1038/s41467-021-26048-7

Becker, E. (2025). ENSO update: La Niña has ended. NOAA Climate.gov. https://www.climate.gov/news-features/blogs/enso/april-2025-enso-update-la-nina-has-ended

Burke, M., Hsiang, S. M., \& Miguel, E. (2015). Global non-linear effect of temperature on economic production. Nature, 527(7577), 235-239.

Cai, W., Ng, B., Geng, T., Wu, L., Santoso, A., \& McPhaden, M. J. (2020). Butterfly effect and a self-modulating El Niño response to global warming. Nature, 585(7823), 68-73.

Cai, W., Ng, B., Wang, G., Santoso, A., Wu, L., \& Yang, K. (2022). Increased ENSO sea surface temperature variability under four IPCC emission scenarios. Nature Climate Change, 12(3), 228-231.

Cai, W., Santoso, A., Wang, G., Yeh, S.-W., An, S.-I., Cobb, K. M., Collins, M., Guilyardi, E., Jin, F.-F., Kug, J.-S., \& others. (2015). ENSO and greenhouse warming. Nature Climate Change, 5(9), 849-859.

Callahan, C. W., \& Mankin, J. S. (2023). Persistent effect of El Niño on global economic growth. Science, 380(6649), 1064-1069.

Centers for Disease Control and Prevention. (2024). CDC WONDER (Wide-ranging Online Data for Epidemiologic Research) [Dataset]. https://wonder.cdc.gov/

Chen, H., Samet, J., Bromberg, P., \& Tong, H. (2021). Cardiovascular health impacts of wildfire smoke exposure. In Particle and Fibre Toxicology (Vol. 18, Issue 1, pp. 1-22). https://doi.org/10.1186/s12989-020-00394-8

Choi, K.-M., Christakos, G., \& Wilson, M. L. (2006). El Niño effects on influenza mortality risks in the state of California. Public Health, 120(6), 505-516.

Cui, J., \& Sinoway, L. I. (2014). Cardiovascular responses to heat stress in chronic heart failure. In Current Heart Failure Reports (Vol. 11, Issue 2, pp. 139-145). https://doi.org/10.1007/s11897-014-0191-y

Dickson, D. C., Hardy, M. R., \& Waters, H. R. (2009). Life table and selection. In Actuarial mathematics for life contingent risks (pp. 41-70). Cambridge University Press.

Ehsani, M. R., Arevalo, J., Risanto, C. B., Javadian, M., Devine, C. J., Arabzadeh, A., Venegas-Quiñones, H. L., Dell’Oro, A. P., \& Behrangi, A. (2020). 2019-2020 Australia fire and its relationship to hydroclimatological and vegetation variabilities. Water, 12(11), 3067.

Fisman, D. N., Tuite, A. R., \& Brown, K. A. (2016). Impact of El Niño Southern Oscillation on infectious disease hospitalization risk in the United States. Proceedings of the National Academy of Sciences, 113(51), 1458914594.

Flores, E. C., Fuhr, D. C., Simms, V., Lescano, A. G., \& Thorogood, N. (2025). Beyond the flood: Exploring the psychosocial consequences and resilience challenges in the aftermath of "El Niño" in Tumbes, Peru. The Journal of Climate Change and Health, 24, 100477.

FRED Economic Data. (2024). [Dataset]. Federal Reserve Economic. https://fred.stlouisfed.org/
Hsiang, S. M., \& Meng, K. C. (2015). Tropical economics. American Economic Review, 105(5), 257-261.
Jia, F., Cai, W., Gan, B., Wu, L., \& Di Lorenzo, E. (2021). Enhanced North pacific impact on El Niño/southern oscillation under greenhouse warming. Nature Climate Change, 11(10), 840-847.

Karamperidou, C., Jin, F.-F., \& Conroy, J. L. (2017). The importance of ENSO nonlinearities in tropical pacific response to external forcing. Climate Dynamics, 49, 2695-2704.

Kovats, R. S., Bouma, M. J., Hajat, S., Worrall, E., \& Haines, A. (2003). El Niño and health. The Lancet, 362(9394), 1481-1489.

Lawman, A. E., Di Nezio, P. N., Partin, J. W., Dee, S. G., Thirumalai, K., \& Quinn, T. M. (2022). Unraveling forced responses of extreme El Niño variability over the Holocene. Science Advances, 8(9), eabm4313.

Liu, Y., Cai, W., Lin, X., Li, Z., \& Zhang, Y. (2023). Nonlinear El Niño impacts on the global economy under climate change. Nature Communications, 14(1), 5887.

Marlier, M. E., DeFries, R. S., Voulgarakis, A., Kinney, P. L., Randerson, J. T., Shindell, D. T., Chen, Y., \& Faluvegi, G. (2013). El Niño and health risks from landscape fire emissions in southeast Asia. Nature Climate Change, 3(2), 131-136.

McGregor, G. R., \& Ebi, K. (2018). El Niño Southern Oscillation (ENSO) and health: An overview for climate and health researchers. Atmosphere, 9(7), 282.

McPhaden, M. J., Zebiak, S. E., \& Glantz, M. H. (2006). ENSO as an integrating concept in earth science. Science, 314(5806), 1740-1745.

Nandi, A., Counts, N., Chen, S., Seligman, B., Tortorice, D., Vigo, D., \& Bloom, D. E. (2022). Global and regional projections of the economic burden of Alzheimer's disease and related dementias from 2019 to 2050: A value of statistical life approach. EClinicalMedicine, 51, 101580.

Ng, B., Cai, W., Cowan, T., \& Bi, D. (2021). Impacts of Low-Frequency Internal Climate Variability and Greenhouse Warming on El Niño-Southern Oscillation. Journal of Climate, 34(6), 2205-2218. https://doi.org/10.1175/JCLI-D-20-0232.1

O'Neill, B. C., Tebaldi, C., van Vuuren, D. P., Eyring, V., Friedlingstein, P., Hurtt, G., Knutti, R., Kriegler, E., Lamarque, J.-F., Lowe, J., Meehl, G. A., Moss, R., Riahi, K., \& Sanderson, B. M. (2016). The Scenario Model Intercomparison Project (ScenarioMIP) for CMIP6. Geoscientific Model Development, 9, 3461-3482. https://doi.org/10.5194/gmd-9-3461-2016,

Ortiz-Prado, E., Camacho-Vasconez, A., Izquierdo-Condoy, J. S., Bambaren, C., Hernández-Galindo, L., \& Sanchez, J. C. (2023). El Niño-Southern Oscillation: A call to action for public health emergency preparedness and response. The Lancet Regional Health-Americas, 27, 100601.

Philander, S., Pacanowski, R., \& Yamagata, T. (1984). Unstable air-sea interactions in the tropics. Journal of the Atmospheric Sciences, 41(4), 604-613.

Pollard, J. H. (1982). The expectation of life and its relationship to mortality. Journal of the Institute of Actuaries, 109(2), 225-240.

Pollard, J. H. (1988). On the decomposition of changes in expectation of life and differentials in life expectancy. Demography, 25(2), 265-276.

Rayner, N., Parker, D. E., Horton, E., Folland, C. K., Alexander, L. V., Rowell, D., Kent, E. C., \& Kaplan, A. (2003). Global analyses of sea surface temperature, sea ice, and night marine air temperature since the late nineteenth century. Journal of Geophysical Research: Atmospheres, 108(D14), ACL. https://doi.org/10.1029/2002JD002670

Robinson, L. A., Hammitt, J. K. \& O'Keeffe, L. Valuing mortality risk reductions in global benefit-cost analysis. Journal of Benefit-Cost Analysis. 10, 15-50 (2019).

Rohde, R. A., \& Hausfather, Z. (2020). The Berkeley Earth land/ocean temperature record. Earth System Science Data, 12(4), 3469-3479.

Schneider, U., Becker, A., Finger, P., Meyer-Christoffer, A., Rudolf, B., \& Ziese, M. (2016). GPCC full data reanalysis version 7.0: Monthly land-surface precipitation from rain gauges built on GTS based and historic data [Dataset]. UCAR/NCAR-Research Data Archive. https://psl.noaa.gov/data/gridded/data.gpcc.html

Scott, A. J., Ellison, M., \& Sinclair, D. A. (2021). The economic value of targeting aging. Nature Aging, 1(7), 616-623.
Seager, R., Cane, M., Henderson, N., Lee, D.-E., Abernathey, R., \& Zhang, H. (2019). Strengthening tropical Pacific zonal sea surface temperature gradient consistent with rising greenhouse gases. Nature Climate Change, 9(7), 517-522.

Serre, D. (2022). Climate Risk Analysis for Life and Health Insurance Companies. SOA Catastrophe \& Climate Strategic Research Program.

Takahashi, K., Montecinos, A., Goubanova, K., \& Dewitte, B. (2011). ENSO regimes: Reinterpreting the canonical and Modoki El Niño. Geophysical Research Letters, 38(10), L10704.

Tatebe, H., Ogura, T., Nitta, T., Komuro, Y., Ogochi, K., Takemura, T., Sudo, K., Sekiguchi, M., Abe, M., Saito, F., \& others. (2019). Description and basic evaluation of simulated mean state, internal variability, and climate sensitivity in MIROC6. Geoscientific Model Development, 12(7), 2727-2765.

Tebaldi, C., Debeire, K., Eyring, V., Fischer, E., Fyfe, J., Friedlingstein, P., Knutti, R., Lowe, J., O'Neill, B., Sanderson, B., \& others. (2021). Climate model projections from the scenario model intercomparison project (ScenarioMIP) of CMIP6. Earth System Dynamics, 12(1), 253-293.

United States Mortality DataBase. (2024). [Dataset]. University of California, Berkeley (USA). https://usa.mortality.org

Viscusi, W. K., \& Masterman, C. J. (2017). Income elasticities and global values of a statistical life. Journal of BenefitCost Analysis, 8(2), 226-250.

Wang, C., \& Fiedler, P. C. (2006). ENSO variability and the eastern tropical Pacific: A review. Progress in Oceanography, 69(2-4), 239-266.

Wang, G., \& Cai, W. (2020). Two-year consecutive concurrences of positive Indian Ocean Dipole and Central Pacific El Niño preconditioned the 2019/2020 Australian "black summer" bushfires. Geoscience Letters, 7(1), 19.

Ward, P. J., Jongman, B., Kummu, M., Dettinger, M. D., Sperna Weiland, F. C., \& Winsemius, H. C. (2014). Strong influence of El Niño Southern Oscillation on flood risk around the world. Proceedings of the National Academy of Sciences, 111(44), 15659-15664.

Xu, Y., Zhu, W., Samanta, D., \& Horton, B. P. (2025). Enduring impacts of El Niño on life expectancy in past and future climates. Nanyang Business School Research Paper, 25(8).

Zebiak, S. E., Orlove, B., Muñoz, Á. G., Vaughan, C., Hansen, J., Troy, T., Thomson, M. C., Lustig, A., \& Garvin, S. (2015). Investigating El Niño-Southern Oscillation and society relationships. Wiley Interdisciplinary Reviews: Climate Change, 6(1), 17-34. https://doi.org/10.1002/wcc. 294

Zhang, W., Graf, H.-F., Leung, Y., \& Herzog, M. (2012). Different El Niño types and tropical cyclone landfall in East Asia. Journal of Climate, 25(19), 6510-6523.

## About The Society of Actuaries Research Institute

Serving as the research arm of the Society of Actuaries (SOA), the SOA Research Institute provides objective, datadriven research bringing together tried and true practices and future-focused approaches to address societal challenges and your business needs. The Institute provides trusted knowledge, extensive experience and new technologies to help effectively identify, predict and manage risks.

Representing the thousands of actuaries who help conduct critical research, the SOA Research Institute provides clarity and solutions on risks and societal challenges. The Institute connects actuaries, academics, employers, the insurance industry, regulators, research partners, foundations and research institutions, sponsors and nongovernmental organizations, building an effective network which provides support, knowledge and expertise regarding the management of risk to benefit the industry and the public.

Managed by experienced actuaries and research experts from a broad range of industries, the SOA Research Institute creates, funds, develops and distributes research to elevate actuaries as leaders in measuring and managing risk. These efforts include studies, essay collections, webcasts, research papers, survey reports, and original research on topics impacting society.

Harnessing its peer-reviewed research, leading-edge technologies, new data tools and innovative practices, the Institute seeks to understand the underlying causes of risk and the possible outcomes. The Institute develops objective research spanning a variety of topics with its strategic research programs: aging and retirement; actuarial innovation and technology; mortality and longevity; diversity, equity and inclusion; health care cost trends; and catastrophe and climate risk. The Institute has a large volume of topical research available, including an expanding collection of international and market-specific research, experience studies, models and timely research.


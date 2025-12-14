# NAIC - GOES Technical Documentation - Corporate Yield Model 

Author: ©2025 Conning, Inc. Conning, Inc

## NAIC Basic Data Set

The Basic Data Set provided free of charge to insurers is the standard scenario file set delivered as part of the NAIC scenario service. Users can access the scenarios online by downloading a file containing stochastic scenarios from the GEMS ${ }^{\text {® }}$ Economic Scenario Generator for real-world interest rates, equity, and bond fund returns. The typical application for these scenarios is in calculations of life and annuity statutory reserves according to the Valuation Manual (e.g., VM-20, VM-21) and capital under the NAIC RBC requirements (e.g., C3 Phase 1, C3 Phase 2).

In this document the technical specifications of the underlying stochastic model of the ESG used for producing corporate bond yields, spreads, and returns on corporate bond funds for the Basic Data Set are described.

## Corporate Yield Model

Corporate bonds have become an increasingly important asset class in the past decade. The drive into corporate debt has been driven in part by a sustained period of low yields. Scenarios for the yields and spreads on corporate bonds, as well as corporate bond fund returns, are simulated using a multi-factor model referred to as the Corporate Yield Model.

The model incorporates the following important features:

- Stochastic spreads
- Stochastic transition and default dynamics
- Real-world and risk-neutral versions
- Ability to produce the jump-like behavior in spreads
- Mechanism for fitting the initial yield curves of corporate bonds across multiple ratings and tenors
- Pricing of bonds within an arbitrage-free framework


### Corporate Bond Spread-Stylized Facts

The events of 2008 and several market events since were characterized by falling equity markets and increasing spreads on corporate bonds. Figure 1 shows the historical spreads on 1 -year AAA-, AA-, A-, and BBB-rated bonds from the United States and United Kingdom. While periods of high volatility had been observed before, the events of 2008 were unprecedented in the historical record (albeit short). During this period, spreads increased rapidly, in most cases to levels which were over twice the highest levels previously experienced, and between four and five times the historical mean. Figure 1 also supports the argument that corporate bond spreads are stochastic and capable of exhibiting dislocations similar, but evolving more slowly, than those observed in the equity markets.

<img src="https://cdn.mathpix.com/cropped/7a085f17-281f-4cb0-86d0-faf1d0fdc4b3-2.jpg?height=1021&width=1567&top_left_y=275&top_left_x=277" alt="image" style="width:100%;height:auto;">
Figure 1. Spreads for US and UK AAA-, AA-, A- and BBB-rated bonds of 1-year maturity from 1991-2020 showing the sudden and rapid increases in spread experienced in 2008/2009 and early in 2020. Prepared by Conning, Inc. ©2025 Conning, Inc. Sources: GEMS ${ }^{®}$ Economic Scenario Generator and (c)2025 Bloomberg, L.P.

Another important feature of the market is the correlation of credit spreads with other market sectors, in particular equities. Empirical evidence indicates that the lower the rating of a bond, the more the bond behaves like an equity instrument. Consequently, one expects there to be an increasing correlation between corporate bond spreads and equity returns as ratings decline. This is indeed what is observed in the market data, in particular for lower credit ratings of corporate bonds.

Figure 2 shows the term structure of credit spreads for UK AAA-, AA-, A-, and BBB-rated bonds at yearend 2007, 2008, 2009 and 2010. Here again we can observe that the movement in spreads between 2007 and 2008 affected all ratings and tenors simultaneously. We also observe some possible liquidity effects in these curves, such as the AAA curve in 2009. Such discontinuities in the spread curves for some tenors require special consideration, particularly in the context of fitting initial yield curves for the corporate bond markets.

<img src="https://cdn.mathpix.com/cropped/7a085f17-281f-4cb0-86d0-faf1d0fdc4b3-3.jpg?height=910&width=1541&top_left_y=264&top_left_x=292" alt="image" style="width:100%;height:auto;">
Figure 2. Spreads curves for UK AAA-, AA-, A- and BBB-rated bonds at year end 2007-2010 showing the extent of the difference between 2008 and other years. Also obvious is the extent to which market spread curves exhibit a range of shapes and are not smooth. Prepared by Conning, Inc. ©2025 Conning, Inc. Sources: GEMS ${ }^{\text {® }}$ Economic Scenario Generator and ©2025 Bloomberg, L.P.

This summarizes some of the main features of the market that a model of corporate bond yields and spreads would ideally exhibit.

### Corporate Yield Model Specification

The GEMS ${ }^{®}$ Corporate Yield Model is a multifactor reduced-form model allowing for the production and simulation of corporate bond yields, spreads, bond prices, transitions between rating classes and defaults. As a starting point for the model, we assume that there are $K$ rating classes $\{1,2, \ldots K$ $1, K$ \} where the absorbing state $K$ is default. The rating classes used for the Basic Data Set are \{AAA, $\mathrm{AA}, \mathrm{A}, \mathrm{BBB}$, high yield, default\}.

Two primary inputs govern the dynamics of the model:

1. $K \times K$-generator matrix, $\mathcal{L}(t)$, for the rating transition and default
2. A stochastic modulator $\mu(t)$ which multiplies the generator matrix $\mathcal{L}(t)$ at each time step

The form of the generator matrix $\mathcal{L}(t)$ can be written as:

$$
\mathcal{L}(t)=\left[\begin{array}{ccccc}
\lambda_{1,1}(t) & \lambda_{1,2}(t) & \lambda_{1,3}(t) & \cdots & \lambda_{1, K}(t) \\
\lambda_{2,1}(t) & \lambda_{2,2}(t) & \lambda_{2,3}(t) & \cdots & \lambda_{2, K}(t) \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\lambda_{K-1,1}(t) & \lambda_{K-1,2}(t) & \lambda_{K-1,3}(t) & \cdots & \lambda_{K-1, K}(t) \\
0 & 0 & 0 & \cdots & 0
\end{array}\right]
$$

With the dynamics of the model governed by the stochastic generator:

$$
\mathcal{L}(t) \mu(t)
$$

The generator matrix is a transformation of the corporate bond transition matrix which everyone familiar with the corporate bond markets knows. The relationship between the real-world transition matrix QRW and the generator matrix is:

$$
Q^{R W}=e^{\mathcal{L}(t)}
$$

The properties of the generator matrix are that the rows sum to zero, the diagonal elements are negative, and the off-diagonal elements take positive values. The generator matrix has useful properties in the context of stochastic modeling. In particular, a generator matrix multiplied by a scalar such as $\mu(t)$ is still a generator matrix. The same is not true of a transition matrix because the rows sum to 1 .

In addition to the above, the model incorporates the following characteristics:

- A recovery of market-value assumption for each rating class, defining the proportion of a bond's price prior to default that is recovered on default
- A mechanism for fitting the initial yield curves of corporate bonds for different ratings and tenor
- A jump process as one element of the stochastic modulator $\mu(t)$ allowing for the simulation of rapid increases in corporate bond spreads
- A correlation between the stochastic modulator $\mu(t)$ and the model of equity returns

Figure 3 shows the GEMS ${ }^{®}$ simulated 1-year maturity spread for AAA, AA, A, BBB and high yield bonds over a 30-year simulation horizon in quarterly time steps. The spread jump is clearly visible in this path, and as with real credit crises the shock is systemic, affecting assets of all ratings simultaneously. Models which do not incorporate such a jump process have difficulty in producing these levels of spreads without large increases in the overall volatility of spreads to unrealistic levels.

<img src="https://cdn.mathpix.com/cropped/7a085f17-281f-4cb0-86d0-faf1d0fdc4b3-4.jpg?height=727&width=1361&top_left_y=1585&top_left_x=380" alt="image" style="width:100%;height:auto;">
Figure 3. Simulated path from the GEMS ${ }^{®}$ Corporate Yield Model showing spreads on bonds of 1 year maturity for AAA, AA, A, BBB and High Yield rating classes. Prepared by Conning, Inc. ©2025 Conning, Inc. Source: GEMS ${ }^{\text {® }}$ Economic Scenario Generator.

This jump process leads to bond returns which are fat tailed, capturing the types of extreme losses that can occur through spread movements as well as defaults. Figure 4 shows a Q-Q plot for A-rated bond returns with maturity of 3 to 5 years based on the output from the corporate yield model. If the returns were normally distributed, then the Q-Q plot would show a straight line. However, the left tail of the plot is observed to deviate significantly from a straight line, indicating a significantly heavy loss tail in the return distribution of the model.

<img src="https://cdn.mathpix.com/cropped/7a085f17-281f-4cb0-86d0-faf1d0fdc4b3-5.jpg?height=383&width=828&top_left_y=659&top_left_x=631" alt="image" style="width:100%;height:auto;">
Figure 4. Q-Q Plot of A rated 3-5-year corporate bond returns. Prepared by Conning, Inc. ©2025 Conning, Inc. Source: GEMS ${ }^{\text {® }}$ Economic Scenario Generator.

## Initial Yield Curve Fitting

As with the Treasury yield, the corporate yields need to be fit at the beginning of the simulation. For the GOES scenarios, Conning will be using the SPGMI Fixed Income Curves. Specifically, the calibration process will be run using five ratings: $A A A, A A, A, B B B$ and $B B$ for the following maturities: 6 -Month, 1 through $10,12,15,20,25$ and 30 years.

## Summary

In this document, the technical specification and the properties of the corporate spread and corporate bond fund returns model used to produce the NAIC Basic Data Set have been described. The GEMS ${ }^{\text {® }}$ Economic Scenario Generator corporate yield model described represents an advanced modeling structure for this asset class which enables more realistic modeling of real-world effects than is possible with a simpler model. Prior to scenario production, the model is approximately fit to the initial market yield curve of corporate bonds across the five modeled rating categories for maturities 1 to 30 years. The statistical properties of the simulated model can also be customized to take account of specified or changing calibration criteria.

## Additional Reading

Duffie and Singleton, Modeling Term Structures of Defaultable Bonds, The Review of Financial Studies, 1999.

Lando, D. (2004). Credit Risk Modeling. Princeton University Press

## Disclosures/Confidentiality Notice

©2025 Conning, Inc. Conning, Inc., Goodwin Capital Advisers, Inc., Conning Investment Products, Inc., a FINRAregistered broker-dealer, Conning Asset Management Limited, and Conning Asia Pacific Limited (collectively "Conning") and Octagon Credit Investors, LLC, Global Evolution Holding ApS and its subsidiaries, and Pearlmark Real Estate, L.L.C. and its subsidiaries (collectively "Affiliates" and together with Conning, "Conning \& Affiliates") are all direct or indirect subsidiaries of Conning Holdings Limited which is one of the family of companies whose controlling shareholder is Generali Investments Holding S.p.A. ("GIH") a company headquartered in Italy. Assicurazioni Generali S.p.A. is the ultimate controlling parent of all GIH subsidiaries. This document and the software described within are copyrighted with all rights reserved. No part of this document may be distributed, reproduced, transcribed, transmitted, stored in an electronic retrieval system, or translated into any language in any form by any means without the prior written permission of Conning \& Affiliates. Conning \& Affiliates do not make any warranties, express or implied, in this document. In no event shall any Conning \& Affiliates company be liable for damages of any kind arising out of the use of this document or the information contained within it. This document is not intended to be complete, and we do not guarantee its accuracy. Any opinion expressed in this document is subject to change at any time without notice.

ADVISE ${ }^{®}$, FIRM ${ }^{®}$, GEMS ${ }^{®}$, CONNING CLIMATE RISK ANALYZER ${ }^{®}$ and CONNING ALLOCATION OPTIMIZER ${ }^{®}$ are registered trademarks of Conning, Inc. in the U.S. ADVISE ${ }^{®}$, FIRM ${ }^{®}$, GEMS ${ }^{®}$, CONNING CLIMATE RISK ANALYZER ${ }^{®}$ and CONNING ALLOCATION OPTIMIZER ${ }^{®}$ are proprietary software published and owned by Conning, Inc. Copyright 1990-2025 Conning, Inc. All rights reserved.

This document is for informational purposes only and should not be interpreted as an offer to sell, or a solicitation or recommendation of an offer to buy any security, product or service, or retain Conning \& Affiliates for investment advisory services. The information in this document is not intended to be nor should it be used as investment advice. COD00001543


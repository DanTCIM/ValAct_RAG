# Bermuda EBS Scenario-Based Approach (SBA) Module — Requirements Specification

Requirements for a "Bermuda SBA" module to sit alongside an existing actuarial platform's liability, basic-asset, and reinvestment/disinvestment modules. Written for a build target, not a regulatory filing — every numeric parameter, formula, and rule below is cited to a specific Bermuda Monetary Authority (BMA) source so the implementer's own model documentation has a paper trail back to the regulation.

**Regulatory basis note:** BMA's Class C/D/E Prudential Rules (as amended 2024) — [Schedule XXVI](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf), "Schedule of Economic Balance Sheet Valuation Principles" — is the current, operative legal text and is the primary citation source throughout. Where the [2015 discount-rate paper](https://www.bma.bm/viewPDF/documents/2018-12-31-07-01-46-Determination-of-Discount-Rates-for-Economic-Balance-Sheet.pdf) or the [2023 CP2 consultation paper](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf) provide fuller methodological explanation than the terser Rules text, they are cited as supporting/explanatory sources, with Schedule XXVI noted as controlling wherever the two differ.

Every inline citation below is a clickable link straight to the source PDF (or Excel workbook, for the Default & Downgrade Costs doc) on bma.bm. Citations to the **superseded** 2024-03-28 SBA Instruction Handbook are left unlinked — BMA has removed it from its public index (see §3) — but are kept for traceability since its content is substantively carried into the current 2025 handbook.

---

## Table of Contents

1. [Purpose & Scope](#1-purpose--scope)
2. [Key Concepts & Glossary](#2-key-concepts--glossary)
3. [Reference Document Index](#3-reference-document-index)
4. [Asset & Interest-Rate Modeling Requirements](#4-asset--interest-rate-modeling-requirements)
   - 4.1 [Risk-Free / Reference Curve Construction](#41-risk-free--reference-curve-construction)
   - 4.2 [Forward Curve Path Development](#42-forward-curve-path-development)
   - 4.3 [Interest Rate Scenario Generation — the 9 Scenarios](#43-interest-rate-scenario-generation--the-9-scenarios)
   - 4.4 [Asset Eligibility & Classification Tiers](#44-asset-eligibility--classification-tiers)
   - 4.5 [Default & Downgrade Cost Methodology](#45-default--downgrade-cost-methodology)
   - 4.6 [Transaction Cost & Bid-Ask Spread Modeling](#46-transaction-cost--bid-ask-spread-modeling)
   - 4.7 [Reinvestment Strategy Requirements](#47-reinvestment-strategy-requirements)
   - 4.8 [Disinvestment Strategy Requirements](#48-disinvestment-strategy-requirements)
   - 4.9 [Ring-Fencing & Fungibility Rules](#49-ring-fencing--fungibility-rules)
   - 4.10 [Derivatives Treatment](#410-derivatives-treatment)
5. [Liability Interface Requirements Specific to SBA](#5-liability-interface-requirements-specific-to-sba)
6. [Best Estimate Liability (BEL) Calculation Engine](#6-best-estimate-liability-bel-calculation-engine)
7. [Model Outputs — LLSBA Return Template](#7-model-outputs--llsba-return-template)
8. [Model Outputs — Analysis of Change / Attribution](#8-model-outputs--analysis-of-change--attribution)
9. [Model Outputs — Stress & Scenario Testing](#9-model-outputs--stress--scenario-testing)
10. [Model Outputs — Well-Matched Portfolio Metrics](#10-model-outputs--well-matched-portfolio-metrics)
11. [Governance & Documentation Hooks](#11-governance--documentation-hooks)
12. [Appendices](#12-appendices)

---

## 1. Purpose & Scope

This module implements Bermuda's **Scenario-Based Approach (SBA)** — the alternative to the Standard Approach for discounting long-term (life) insurance liabilities, available where assets and liabilities are demonstrated to be "well-matched" ([Schedule XXVI, para 28(5)–(6)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf)). Instead of a single illiquidity-adjusted discount curve, the SBA prices liabilities using the insurer's **actual backing-asset portfolio**, run through a **base scenario plus eight prescribed interest-rate stress scenarios**, with the Best Estimate Liability (BEL) set to the worst (highest-reserve) outcome across all nine ([2015 Determination of Discount Rates, para 1c, 6–9](https://www.bma.bm/viewPDF/documents/2018-12-31-07-01-46-Determination-of-Discount-Rates-for-Economic-Balance-Sheet.pdf); [Schedule XXVI, para 28(7), (10)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf)).

**This module is the SBA-specific layer on top of what already exists.** It assumes:
- A **liability module** that can project liability cash flows (premiums, claims, expenses) by sub-portfolio and model policyholder-option behavior (lapse, etc.) — this module adds SBA-specific requirements on top (Lapse Cost eligibility test, cash-flow granularity across 9 scenarios; see §5).
- A **basic asset module** that holds asset static data and can price/project fixed-income instruments — this module adds SBA eligibility tiering, default/downgrade cost application, and scenario-conditional curve/spread inputs (see §4.4–4.6).
- A **reinvestment/disinvestment module** that already executes buy/sell logic against cash-flow gaps — this module adds the SBA-specific constraints that must govern that logic (rating/tenor bucketing, no active trading, unsellable-asset rules, grade-in periods; see §4.7–4.8).

What this module is newly responsible for: the risk-free curve and forward-curve engine (§4.1–4.2), the 9-scenario generator (§4.3), the default/downgrade and transaction cost engines (§4.5–4.6), the BEL calculation across scenarios with biting-scenario selection (§6), and all regulatory outputs — the LLSBA return, stress testing, attribution, and well-matched metrics (§7–10).

---

## 2. Key Concepts & Glossary

| Term | Definition | Source |
|---|---|---|
| **Economic Balance Sheet (EBS)** | Fair-value balance sheet on which Bermuda long-term insurers report technical provisions (Form 1EBS). | [Schedule XXVI Part 1](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf) |
| **Best Estimate Liability (BEL)** | Probability-weighted average of future cash flows, discounted. Under SBA, set to the highest asset requirement across the base scenario and 8 stress scenarios. | [Schedule XXVI, para 28(10)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf) |
| **Standard Approach** | Discounting via risk-free curve + illiquidity premium adjustment derived from a representative corporate-bond portfolio. | [Schedule XXVI, para 27](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf); [2015 Determination, paras 3–4f](https://www.bma.bm/viewPDF/documents/2018-12-31-07-01-46-Determination-of-Discount-Rates-for-Economic-Balance-Sheet.pdf) |
| **Scenario-Based Approach (SBA)** | Alternative discounting method using the insurer's actual asset portfolio (net of default costs) run through a base scenario and 8 interest-rate stress scenarios; BEL = worst outcome. | [2015 Determination, para 1c](https://www.bma.bm/viewPDF/documents/2018-12-31-07-01-46-Determination-of-Discount-Rates-for-Economic-Balance-Sheet.pdf); [Schedule XXVI, para 28](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf) |
| **Illiquidity premium** | The part of an asset's spread *not* attributable to credit risk — the portion the SBA permits insurers to reflect in liability discounting when cash flows are well-matched. | [CP2 (2023), §2, §2.7](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf) |
| **Base scenario** | Scenario (a) of the 9 — no interest-rate adjustment; asset requirement computed from the actual portfolio net of expected defaults. | [Schedule XXVI, para 28(7)(a)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf) |
| **"The 8 scenarios"** | The 8 prescribed interest-rate stress paths (scenarios b–i under Schedule XXVI, or a–h under the 2015 paper's original numbering) — industry and BMA usage refers to "the 8 scenarios" as the *stress* set, distinct from the base. | [2015 Determination, para 7](https://www.bma.bm/viewPDF/documents/2018-12-31-07-01-46-Determination-of-Discount-Rates-for-Economic-Balance-Sheet.pdf); [Schedule XXVI, para 28(7)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf); [Instructions Handbook §E4.3b](https://www.bma.bm/viewPDF/documents/2025-12-19-15-00-17-2025-Year-end-Long-Term-Instructions-Handbook.pdf) |
| **Biting scenario** | Whichever of the 9 scenarios produces the highest aggregate asset requirement for a fungible set of liabilities — this scenario's result becomes the BEL. | [Schedule XXVI, para 28(11)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf) |
| **Well-matched** | The (insurer-defined, BMA-assessed) standard of asset/liability cash-flow matching required to remain eligible for SBA. No single BMA formula — assessed via a battery of quantitative/qualitative criteria (§10). | [Schedule XXVI, para 28(5)–(6)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf); [Instructions Handbook §E4](https://www.bma.bm/viewPDF/documents/2025-12-19-15-00-17-2025-Year-end-Long-Term-Instructions-Handbook.pdf) |
| **Lapse Cost (LapC)** | Explicit BEL add-on required when SBA-eligible liabilities carry policyholder lapse optionality, sized off historical lapse-rate volatility. Formerly "Base Lapse Adjustment (BLA)." | [Schedule XXVI, para 29](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf); [CP2, §2.4](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf) |
| **Default cost** | Expected-loss component of the default & downgrade cost, from realized average historical default losses. | [Schedule XXVI, para 28(24)(a)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf) |
| **Downgrade cost** | Uncertainty-margin component layered on top of default cost, reflecting credit-migration risk. Phased in over 5 years for legacy business. | [Schedule XXVI, para 28(24)(b)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf); [Default & Downgrade Costs doc (2024), §C](https://cdn.bma.bm/documents/2024-04-15-14-06-57-Default-and-Downgrade-Costs-for-the-Scenario-Based-Approach.xlsx) |
| **Fungibility** | The extent to which assets/cash flows may be shared across SBA sub-portfolios or blocks of business. Disallowed by default; requires demonstration, governance, and BMA approval; never permitted across legal entities. | [Schedule XXVI, para 28(37)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf); [CP2, §2.19.2](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf) |
| **Ring-fencing** | Requirement that assets backing a specific block of SBA liabilities be used only to meet those liabilities — not pledged or used elsewhere. | [CP2, §2.11](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf) |
| **Unsellable assets** | Assets that cannot be assumed sold to meet a cash-flow shortfall (non-publicly-traded, limited-basis/structured, or encumbered assets, absent specific BMA approval). | [Schedule XXVI, para 28(34)(g)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf); [CP2, §2.6](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf) |
| **Key Rate Duration (KRD)** | Sensitivity of asset/liability value to a rate shift at one specific curve tenor. LLSBA reports KRD at 2, 5, 10, 20, 30 years. | [LLSBA Completion Instructions, §C (ALM_KRD)](https://www.bma.bm/viewPDF/documents/2025-12-23-11-29-23-Lapse-Liquidity-and-Scenario-Based-Approach-Return---Completion-Instructions.pdf) |
| **Analysis of Change (AoC)** | The attribution waterfall decomposing period-over-period BEL and implied-spread movement into named drivers. | [LLSBA Completion Instructions, §D.6](https://www.bma.bm/viewPDF/documents/2025-12-23-11-29-23-Lapse-Liquidity-and-Scenario-Based-Approach-Return---Completion-Instructions.pdf) |
| **Ultimate Forward Rate (UFR)** | The long-run rate BMA's published curves converge to beyond the last traded tenor (currently 4.2%). The module reports this as a published input (LLSBA "Curves" tab, §7) — it does not compute it. | [LLSBA Completion Instructions, §D.2](https://www.bma.bm/viewPDF/documents/2025-12-23-11-29-23-Lapse-Liquidity-and-Scenario-Based-Approach-Return---Completion-Instructions.pdf); [2015 Determination, para 2b (background)](https://www.bma.bm/viewPDF/documents/2018-12-31-07-01-46-Determination-of-Discount-Rates-for-Economic-Balance-Sheet.pdf) |

---

## 3. Reference Document Index

| Document | Date | Authority | Source PDF | What it governs (as used in this spec) |
|---|---|---|---|---|
| Determination of Discount Rates for Economic Balance Sheet Framework | Jul 2015 | BMA | [bma.bm ↗](https://www.bma.bm/viewPDF/documents/2018-12-31-07-01-46-Determination-of-Discount-Rates-for-Economic-Balance-Sheet.pdf) | Background only: BMA's own curve-construction methodology (informational — the operative rule is Instructions Handbook §E9, see §4.1) and the original 8-scenario definitions (unchanged in the current Rules) |
| Insurance (Prudential Standards) (Class C, D, E Solvency Requirement) Amendment Rules 2024 — Schedule XXVI | 2024 | BMA (statutory instrument) | [bma.bm ↗](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf) | **Current operative legal text** for EBS valuation and SBA — curve derivation, 9 scenarios, BEL calc, asset tiers, D&D costs, transaction costs, reinvestment/disinvestment, fungibility, Lapse Cost, Risk Margin |
| Proposed Enhancements to the Regulatory Regime for Commercial Insurers (CP2) | 28 Jul 2023 | BMA (consultation paper) | [bma.bm ↗](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf) | Fullest narrative explanation of SBA mechanics — reinvestment/disinvestment principles, ring-fencing, "no active trading," model governance/validation detail. Largely adopted into Schedule XXVI; used here for explanatory depth where the Rules text is terse |
| Default and Downgrade Costs for the Scenario-Based Approach | 14 Apr 2024 | BMA | [bma.bm ↗](https://cdn.bma.bm/documents/2024-04-15-14-06-57-Default-and-Downgrade-Costs-for-the-Scenario-Based-Approach.xlsx) (Excel workbook — the numeric D&D tables live here, not in a PDF) | D&D cost floors, issuer-vs-issue rating treatment, 5-year downgrade-cost phase-in schedule |
| Instructions on Asset and Scenario Based Approach-related Approvals | 10 Oct 2024 | BMA | [bma.bm ↗](https://www.bma.bm/viewPDF/documents/2024-10-14-11-21-24-Asset-and-SBA-related-Approvals11-October-2024-FINAL.pdf) | Asset-class-specific approval requirements (CML, RML, structured, affiliated, alternative assets) |
| The Bermuda Capital and Solvency Return — Instruction Handbook for Insurance Groups (E. Scenario-Based Approach) | 28 Mar 2024 (superseded) | BMA | *No live link* — superseded and removed from bma.bm; not found in the current site index. Content substantively carried into the 2025 handbook below | Well-matched criteria, SBA application package, risk-free curve rules, transaction cost rules — superseded by the 2025 handbook below but substantively carried forward; cited where the current handbook doesn't repeat the detail |
| The Bermuda Capital and Solvency Return 2025 Instruction Handbook for Class E, Class D & Class C Insurers, §E | Dec 2025 | BMA | [bma.bm ↗](https://www.bma.bm/viewPDF/documents/2025-12-19-15-00-17-2025-Year-end-Long-Term-Instructions-Handbook.pdf) | **Current** well-matched criteria (E4.3a–i), application package, derivative approval, D&D mechanics, interest-rate capital-charge offset formula |
| Lapse, Liquidity and Scenario Based Approach Return (LLSBA) — 2025 Completion Instructions | Dec 2025 | BMA | [bma.bm ↗](https://www.bma.bm/viewPDF/documents/2025-12-23-11-29-23-Lapse-Liquidity-and-Scenario-Based-Approach-Return---Completion-Instructions.pdf) | **LLSBA template structure** — every tab and field this module must be able to populate |
| 2025 Capital and Solvency Return Stress/Scenario Analysis — Class E, D, C | Dec 2025 | BMA | [bma.bm ↗](https://www.bma.bm/viewPDF/documents/2025-12-19-15-36-02-2025-Year-End-Stress-and-Scenario-Instructions-for-Class-C-D--E.pdf) | R1–R9 financial market stress scenarios and magnitudes; rating-downgrade and reverse-stress-test disclosure requirements |

All links point directly to files hosted on bma.bm (or cdn.bma.bm for the Excel workbook) — verify they still resolve before sending, since BMA periodically retires superseded filings from its public index (as happened with the 2024 SBA Instruction Handbook above). All section/paragraph citations throughout this document link back to the corresponding row here.

---

## 4. Asset & Interest-Rate Modeling Requirements

### 4.1 Risk-Free / Reference Curve Construction

This is governed by the **[Instructions Handbook, §E9](https://www.bma.bm/viewPDF/documents/2025-12-19-15-00-17-2025-Year-end-Long-Term-Instructions-Handbook.pdf)** (mirrored in [Schedule XXVI, para 27(2)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf) for the Standard Approach curve) — and the requirement is deliberately light: the module **consumes** a curve, it does not need to build one from scratch. BMA's own curve-construction process (a Nelson-Siegel-Svensson fit — [2015 Determination, paras 2a–4f](https://www.bma.bm/viewPDF/documents/2018-12-31-07-01-46-Determination-of-Discount-Rates-for-Economic-Balance-Sheet.pdf)) is how BMA arrives at the numbers it publishes; that's background on BMA's methodology, not a build requirement for this module.

**The risk-free curve used in the SBA must be either** ([Instructions Handbook, §E9.1](https://www.bma.bm/viewPDF/documents/2025-12-19-15-00-17-2025-Year-end-Long-Term-Instructions-Handbook.pdf)):

(a) **The risk-free curve published or directed by BMA** — published on bma.bm, currently refreshed quarterly for USD, CAD, GBP, CHF, EUR, JPY, AUD, NZD — consumed directly; **or**
(b) **The relevant risk-free market curve, with no adjustments** — government bond rates or swap rates, whichever is the generally accepted risk-free benchmark convention for that currency — kept **flat beyond the last traded tenor** (no extrapolation; e.g., for the US Treasury curve, every rate beyond 30Y is set equal to the observed 30Y rate) ([§E9.2](https://www.bma.bm/viewPDF/documents/2025-12-19-15-00-17-2025-Year-end-Long-Term-Instructions-Handbook.pdf)).

**Required module behavior:**
- Ingest BMA's published curve per currency as the primary path (option a).
- Where BMA doesn't publish a needed currency or date, build the unadjusted market curve instead (option b) — a direct pull of the observed government-bond or swap curve, flat-lined past the last traded tenor. **No smoothing, extrapolation, or curve-fitting is required or permitted here.**
- Treat the curve choice as a **standing election, not a per-run parameter**: document it in the SBA methodology documentation, apply it consistently over time, and require prior BMA approval to change it ([§E9.3](https://www.bma.bm/viewPDF/documents/2025-12-19-15-00-17-2025-Year-end-Long-Term-Instructions-Handbook.pdf)).
- Parameterize the spread engine (§4.5–4.6) off **whichever curve was elected** — spreads used in the SBA must be determined with respect to that curve ([§E9.4](https://www.bma.bm/viewPDF/documents/2025-12-19-15-00-17-2025-Year-end-Long-Term-Instructions-Handbook.pdf)).
- **Idiosyncratic spread adjustment**: where the elected SBA curve differs from the market convention underlying an asset's actual observed market value, compute a per-asset adjustment such that the PV of that asset's projected cash flows — discounted at (elected curve + applicable spread + this adjustment) — equals its actual market value at the valuation date. This must not distort the asset's initial market value, and the adjustment is carried through that asset's entire SBA projection ([§E9.5](https://www.bma.bm/viewPDF/documents/2025-12-19-15-00-17-2025-Year-end-Long-Term-Instructions-Handbook.pdf)).

The **Standard Approach illiquidity-adjusted curve** (needed only for the fallback/comparison cases in §9 and the capital-charge offset in §12.3) is published by BMA the same way ([Schedule XXVI, para 27(2)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf)) — consume it directly rather than reconstructing it.

### 4.2 Forward Curve Path Development

The module must derive, for every future projection year, a scenario-specific spot curve — this is the core "forward curve path" requirement ([Schedule XXVI, para 28(8)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf)):

1. Convert the initial (valuation-date) spot rate curve into the corresponding **forward rate curve**.
2. Build the **spot rate curve at each future projection year** (year 1, year 2, year 3, …) using those forward rates as the building blocks.
3. Apply the scenario-specific adjustments (§4.3) to each of those future spot curves to obtain the **scenario-conditional spot curve at each future year**.

This output feeds asset pricing at each future purchase/sale event and liability discounting at each projection step (§4.7–§4.8, §6).

The Analysis-of-Change "Unwind" step (§8, step 3) reuses this same mechanic one period forward: next period's opening curves are the current period's forward-implied spot curves, and the model must be able to verify **Asset Portfolio IRR is unchanged** across that roll — a built-in validation check ([LLSBA Completion Instructions, §D.6, step "Unwind"](https://www.bma.bm/viewPDF/documents/2025-12-23-11-29-23-Lapse-Liquidity-and-Scenario-Based-Approach-Return---Completion-Instructions.pdf)).

### 4.3 Interest Rate Scenario Generation — the 9 Scenarios

The module must run every projection under a **base scenario plus 8 prescribed interest-rate stress scenarios** (9 total), applied as parallel/twist adjustments to the forward-implied spot curves from §4.2. Scenario definitions and magnitudes are unchanged between the 2015 paper and the current Schedule XXVI ([Schedule XXVI, para 28(7)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf); [2015 Determination, para 7](https://www.bma.bm/viewPDF/documents/2018-12-31-07-01-46-Determination-of-Discount-Rates-for-Economic-Balance-Sheet.pdf)):

| # | Scenario | Path (interpolate between stated points) |
|---|---|---|
| (a) | **Base** | No adjustment to rates |
| (b) | Decrease | Rates decrease linearly to **−1.5%** by year 10; unchanged thereafter |
| (c) | Increase | Rates increase linearly to **+1.5%** by year 10; unchanged thereafter |
| (d) | Decrease then reverse | Rates decrease to **−1.5%** by year 5, then increase back to 0 by year 10 |
| (e) | Increase then reverse | Rates increase to **+1.5%** by year 5, then decrease back to 0 by year 10 |
| (f) | Decrease, positive twist | Year 1: **−1.5%**, Year 10: **−1.0%**, Year 30: **−0.5%** |
| (g) | Decrease, negative twist | Year 1: **−0.5%**, Year 10: **−1.0%**, Year 30: **−1.5%** |
| (h) | Increase, positive twist | Year 1: **+0.5%**, Year 10: **+1.0%**, Year 30: **+1.5%** |
| (i) | Increase, negative twist | Year 1: **+1.5%**, Year 10: **+1.0%**, Year 30: **+0.5%** |

**Implementation rules:**
- Every asset and liability cash flow must be **explicitly projected at granular level** for the base scenario and independently for each of the 8 stress scenarios — no methodology approximations or shortcuts across scenarios are permitted ([CP2, §2.19.5](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf)).
- Optionality-driven cash flows (calls, prepayments, dynamic lapse) must be **allowed to differ** across all 9 scenarios, not held static ([Schedule XXVI, para 28(20)–(21)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf)).
- The stress magnitudes are calibrated to represent roughly **one standard deviation** deviations from the mean — reasonably-expected events, not tail events (tail risk is captured separately in BSCR capital, §9) ([2015 Determination, para 7](https://www.bma.bm/viewPDF/documents/2018-12-31-07-01-46-Determination-of-Discount-Rates-for-Economic-Balance-Sheet.pdf)).

### 4.4 Asset Eligibility & Classification Tiers

The module must classify every asset in the SBA portfolio into one of these tiers and enforce the associated constraints ([Schedule XXVI, para 28(12)–(19)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf)):

| Tier | Examples | Requirement |
|---|---|---|
| **Acceptable (no approval needed)** | Government bonds, municipal bonds, public corporate bonds, cash & equivalents | Freely usable in SBA |
| **Approval-required (investment grade)** | Other IG fixed income incl. private placements, structured securities (MBS/ABS/CLO), residential/commercial mortgage loans, IG preferred stock | Prior BMA approval required |
| **Limited-basis (formerly "258E")** | Below-IG versions of the above, commercial real estate, fixed-income credit funds | Prior BMA approval; **capped at 10%** of SBA asset portfolio value at calc date *and* every projection time-step; **single-asset cap 0.5%** of total portfolio; annual Approved Actuary review; generally cannot be sold to meet shortfalls |
| **Long-term investment credit (formerly "258F")** | Otherwise-unacceptable assets (e.g. equities) backing liability cash flows beyond 30 years | Prior BMA approval; capital adjustment computed as the BEL difference with vs. without these assets; yield haircut ≈ **1 standard deviation** of cumulative return over the holding period |

Delinquent, non-performing, "troubled or challenged" (future cash flows no longer highly predictable), or status-uncertain assets are **ineligible by default** (superseded Instructions Handbook, §E6.2 — *no live link, see §3*). Assets with amendments/extensions/restructurings must be separately identified and justified or excluded (§E6.3, same source).

Structured assets carry additional approval requirements — market/spread assessment, investment thesis, portfolio overview, dedicated stress testing (spread substitution impact, downgrade impact focused on A-and-below), and attestations on payment priority, bankruptcy remoteness, and audit coverage ([Asset and SBA-related Approvals doc, "Structured Assets"](https://www.bma.bm/viewPDF/documents/2024-10-14-11-21-24-Asset-and-SBA-related-Approvals11-October-2024-FINAL.pdf)). Commercial and residential mortgage loans require populated LTV/DSCR (CML) or LTV/type/amortization/credit-score (RML) fields as a completeness gate.

### 4.5 Default & Downgrade Cost Methodology

Default and downgrade costs reduce **projected asset cash flows** — never the initial market value or the projected reinvestment purchase price ([Schedule XXVI, para 28(22)–(23)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf); [Default & Downgrade Costs doc, §A–C](https://cdn.bma.bm/documents/2024-04-15-14-06-57-Default-and-Downgrade-Costs-for-the-Scenario-Based-Approach.xlsx)):

- **Default cost** = expected-loss component, from realized average historical default losses.
- **Downgrade cost** = an uncertainty margin layered on top, reflecting credit-migration risk.
- Where BMA publishes costs for an asset type/rating/tenor combination, the **published values must be used**. Where not published, the insurer's own assumption is used, floored at the greater of its own estimate and the applicable floor.
- **Floors** = the corporate bond (senior unsecured) D&D cost for the corresponding rating; for structured assets/securitizations, floors apply at the **tranche level**, not the collateral pool.
- The **marginal loss rate must be floored at zero** — cumulative loss rate is non-decreasing over the projection ([Schedule XXVI, para 28(24)–(26)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf); superseded Instructions Handbook, §E10.6 — *no live link*).
- **Issuer ratings**, not issue ratings, are used by default (costs were calibrated on issuer-level defaults / issue-level recoveries); issue-level ratings permitted only if demonstrably no less conservative, or immaterial (§E10.12–14, same superseded source).
- **Government debt** is treated as unsecured corporate debt of the same rating, *except*: no D&D cost for local-currency debt of countries rated AA- or better; also no D&D cost where debt is local-currency, country rated A- or better, currency is a fully-convertible global reserve currency, and the country has full independent fiscal/monetary control (§E10.19, same superseded source).
- **Beyond the last published tenor**, hold the D&D cost constant at the last published value, or use an alternative approach demonstrated to be no less conservative (§E10.17–18, same superseded source).

**5-year downgrade-cost phase-in** (default-cost/expected-loss component is never phased in — always applies in full immediately):

| Valuation date | % of full ultimate downgrade cost applied |
|---|---|
| During 2024 (incl. 31 Dec 2024) | 20% |
| During 2025 (incl. 31 Dec 2025) | 40% |
| During 2026 (incl. 31 Dec 2026) | 60% |
| During 2027 (incl. 31 Dec 2027) | 80% |
| 2028 and later | 100% |

Applies only to business written on or before **31 Dec 2023**; business written after that date gets full D&D costs immediately with no phase-in. Phase-in results are rounded to the nearest whole basis point, per asset-type/rating/tenor combination. Early adoption of full costs is allowed at any time but is irreversible without written BMA approval ([Default & Downgrade Costs doc, §C](https://cdn.bma.bm/documents/2024-04-15-14-06-57-Default-and-Downgrade-Costs-for-the-Scenario-Based-Approach.xlsx); superseded Instructions Handbook §E10.8–11 — *no live link*).

The LLSBA D&D tab (SBA_D&D) sources published tables for **1st Lien Bank Loans, Other Bank Loans, Secured Bonds, Senior Unsecured Bonds, Subordinated Bonds**, giving Expected Loss from Default and Cost of Downgrade by BSCR rating across tenors 1–20 years (beyond 20 years, use the 20-year value) — the module's D&D engine should be structured to consume this table shape directly ([LLSBA Completion Instructions, §D.4](https://www.bma.bm/viewPDF/documents/2025-12-23-11-29-23-Lapse-Liquidity-and-Scenario-Based-Approach-Return---Completion-Instructions.pdf)).

### 4.6 Transaction Cost & Bid-Ask Spread Modeling

Full expected price impact — not just quoted bid-ask spread — must be reflected on every asset sale and purchase in the projection, including implicit/explicit fees and commissions ([Schedule XXVI, para 28(30)–(32)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf); [CP2, §2.8](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf)):

- **Liquid publicly traded assets**: minimum requirement is observed bid-ask spreads, where demonstrably not understating true price impact.
- **All other (illiquid/less-liquid) assets**: bid-ask alone is presumed insufficient; the reflected impact must not be lower than (a) implied spreads/discounts from actual past trades of that asset type, or (b) the price impact for a similar, liquid, equivalent-credit-quality asset.
- **Effective, not marginal, bid-ask spreads** — i.e., spreads sized to the insurer's actual position/volume relative to market depth, not the cost of trading one incremental unit.
- **Grade-in rule**: if current observed bid-ask spreads are *tighter* than the long-term average, grade in from current to long-term average; if current spreads are *wider*, the same grading applies but the grade-in period must be set **more prudently** (i.e., typically longer, to avoid understating near-term cost).
- Calibration must be regularly back-tested against actual market data and the insurer's own trading experience.

### 4.7 Reinvestment Strategy Requirements

These are constraints the SBA module layers onto the existing reinvestment module's buy logic ([Schedule XXVI, para 28(33)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf); [CP2, §2.10](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf)):

- Purchases must be drawn from a **defined set of asset classes** consistent with the insurer's current allocation and approved ALM/investment policy — no purchasing asset types the insurer doesn't already hold in its approved SBA portfolio.
- Reinvestment assumptions must **vary by rating and tenor**, at minimum in **no fewer than 3 tenor buckets** (short/medium/long-term, defined relative to the liability/asset cash-flow profile); simplifying into fewer buckets requires demonstrated prudence.
- Purchase prices must follow projected market values by rating/tenor combination **at the relevant scenario and time step**.
- No material departure from current allocation is assumed; where long-term historical market averages are used, a **grade-in period** applies moving from current/short-term spreads to long-term spreads — **longer** when short-term spreads are below long-term averages, **shorter** when above (i.e., prudence is asymmetric).
- **No assumption of continued outperformance** relative to long-term historical averages, even if the current portfolio has been outperforming.
- The insurer must be able to demonstrate the reinvestment approach (including any simplification) produces a **more prudent BEL** than reinvesting per the unmodified existing allocation would.
- **A high degree of matching limits the need for reinvestment in the first place** — this is a design principle, not just a modeling rule: heavy reliance on reinvestment is itself evidence against "well-matched" (§10, criterion f).
- Material changes to the reinvestment strategy require **written BMA approval**, governed by the SBA model change policy.

### 4.8 Disinvestment Strategy Requirements

Constraints layered onto the existing disinvestment module's sell logic ([Schedule XXVI, para 28(34)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf); [CP2, disinvestment section](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf)):

- Assets may be sold **only** to meet excess liability cash outflows not already covered by maturities and coupon receipts — not for portfolio repositioning or asset-class transitions.
- Selling for **rebalancing** back to the existing target allocation (within duration limits) is in scope and expected.
- **Negative net cash flows are never rolled forward** — a shortfall in a given period must be met in that period.
- Sale proceeds must reflect the **cumulative default/downgrade loss rate up to the point of sale** (§4.5).
- **No borrowing** of any form to meet a cash-flow shortfall.
- **Unsellable assets** — non-publicly-traded assets, limited-basis/structured assets, and encumbered assets (absent specific BMA approval to treat as sellable, with appropriate haircuts) — can never be assumed sold to meet a shortfall. Where a shortfall would otherwise require selling an unsellable asset, the model must instead increase the reserve (i.e., this triggers a mismatch cost, not a forced sale).
- The disinvestment strategy specification must address, at minimum: sale sequencing, policy on selling before maturity, policy on realizing unrealized losses, currency-mismatch sales, long- vs. short-duration sale preference, per-block sale constraints, and regulatory-compliance screening of candidate sale assets.
- The Chief Investment Officer (or an agreed equivalent) must attest that the modeled reinvestment *and* disinvestment strategies match actual practice and comply with policy — the module should support capturing/exporting this attestation evidence (§11).

**No active trading, ever:** repositioning or redeployment of the asset portfolio is disallowed outright; reinvestment exists only to redeploy maturities and positive net cash flow, disinvestment exists only to fund negative net cash flow — never to rotate between asset classes for any other reason. No credit for active portfolio management (e.g. assumed yield pickup from trading) is permitted anywhere in the SBA projection ([CP2, §2.19, items 1, 6, 7](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf)).

### 4.9 Ring-Fencing & Fungibility Rules

- The SBA prices liabilities using the **actual, specific** assets assigned to that block of business. Those assets must not be used, pledged, or shared for any other purpose, and must not be available to cover losses elsewhere in the insurer ([CP2, §2.11](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf)).
- **Fungibility across blocks is disallowed by default.** It may only be assumed where transparent, practical, legally permitted, documented, tested, subject to governance challenge, and **limited to the legal-entity level**; assets held in separate collateral accounts require specific BMA approval even then; fungibility **across legal entities is never permitted** ([Schedule XXVI, para 28(37)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf)).
- The module must let the insurer declare and justify its asset-to-liability assignment approach per sub-portfolio, and must gate any cross-block cash-flow sharing behind an explicit fungibility flag.
- The **biting scenario** (§6) is determined per fungible set — where fungibility is restricted, the biting scenario must be selected independently per non-fungible block, not in aggregate ([Schedule XXVI, para 28(11)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf)).

### 4.10 Derivatives Treatment

*(Lower priority — include if the platform's asset portfolios use hedging instruments; otherwise this can be deferred.)*

- Derivatives are permitted in the SBA **only for hedging purposes**, subject to BMA approval (either standalone or as part of SBA model approval).
- **Dynamic (daily/intra-day) hedging is explicitly disallowed.**
- Required application content: investment/hedging strategy summary, risks hedged and cash flows behind each instrument, collateral/margin terms, hedge-effectiveness history, basis-risk quantification, liquidity/collateral sufficiency across all 9 scenarios, and a worked modeling example.
- **Residual risk** (anything other than the domestic interest-rate risk already captured by the 9 scenarios) must be quantified to a **1 standard deviation (1SD)** confidence level, with particular attention to asymmetric risks.
- BEL impact must be reported **with and without** derivatives, under base and all 8 stress scenarios (sunset Instructions Handbook, §E8 — *no live link, see §3*).

---

## 5. Liability Interface Requirements Specific to SBA

The existing liability module is assumed to already project cash flows by product/sub-portfolio. On top of that, SBA eligibility imposes:

**Eligibility gate** — a liability block qualifies for SBA only if either ([Schedule XXVI, para 29(1)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf)):
1. The underlying contracts include **no policyholder options**, or
2. Where options exist, residual risk is demonstrated insignificant, which requires holding a **Lapse Cost (LapC)** and passing two stress tests.

**Lapse Cost (LapC) formula** ([Schedule XXVI, para 29(2)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf); [CP2, §2.4](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf)):

```
Lapse Rate Sigma = 1 standard deviation of (Actual − Expected lapse rate) as % of Expected,
                    rounded UP to the nearest 1%

LapC = (Lapse Rate Sigma ÷ BSCR lapse up/down shock) × Lapse up/down capital requirement
```

**Required stress tests for lapse-optionality eligibility:**
- Pass **100% Enhanced Capital Ratio (ECR)** under a permanent **40% lapse-up or lapse-down** stress (whichever is worse).
- Pass a **3-month horizon liquidity stress test** with minimum **105% Liquidity Coverage Ratio**:
  ```
  LCR = (Eligible Liquidity Sources ÷ Liability Outflows) × 100
  ```
  Liability outflows are driven by a mass-lapse shock table cross-cutting time restraint (low/medium/high) and economic penalty (low/medium/high) by retail vs. institutional book (full table in Appendix, §12.2). Eligible liquidity sources are haircut by asset-liquidity tier (Appendix, §12.2).

**Cash-flow granularity requirement:** all rate-sensitive/optionality-driven assumptions (dynamic lapse formulas etc.) must be modeled to **respond independently under each of the 9 scenarios** (§4.3) — this is a liability-side obligation, not just an asset-side one ([Schedule XXVI, para 28(20)–(21)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf)).

---

## 6. Best Estimate Liability (BEL) Calculation Engine

Core calculation sequence ([Schedule XXVI, para 28(9)–(11)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf)):

1. **Base scenario run**: using the actual current asset portfolio, projected reinvestment (§4.7), and expected defaults (§4.5), determine the assets required to fully cover the base-scenario liability cash flows — this yields the base-scenario asset requirement and the base-scenario implied market yield (net of default costs).
2. **Stress scenario runs** (×8): repeat step 1 under each of the 8 stress scenarios (§4.3). A scenario with cash-flow mismatch or heavier reinvestment dependence will generally require a higher asset requirement than the base scenario.
3. **Cash-flow reconciliation, every scenario, at least annually**: compare liability vs. asset cash flows for the period.
   - **Shortfall** → sell assets at the scenario's prevailing yields (§4.8).
   - **Excess** → purchase assets per reinvestment guidelines (§4.7).
4. **Biting scenario selection**: BEL = the **highest** asset requirement across all 9 scenario results, computed per fungible set of liabilities (§4.9).
5. **Cost of mismatch** = base-scenario result minus biting-scenario result — this single number is both a required well-matched metric (§10a) and a direct input to the Standard Approach interest-rate capital-charge offset (§12.3).

**Downstream note (not part of this module's core scope, but a required output interface):** the company-level Risk Margin calculation consumes this module's **risk-free curve** (without illiquidity adjustment) and the projected ECR path — the module should expose the risk-free curve output cleanly enough for that downstream consumer, per the Risk Margin formula in Appendix §12.4.

---

## 7. Model Outputs — LLSBA Return Template

The module must be able to populate every tab of the BMA's Lapse, Liquidity and Scenario Based Approach (LLSBA) return. SBA users complete all tabs; Standard-Approach-only insurers complete Assets, ALM, and Liquidity only; asset-approval filings additionally require SBA_S&R, SBA_D&D, and SBA_Stress ([LLSBA Completion Instructions, §A](https://www.bma.bm/viewPDF/documents/2025-12-23-11-29-23-Lapse-Liquidity-and-Scenario-Based-Approach-Return---Completion-Instructions.pdf)).

| Tab group | Tab(s) | Required content |
|---|---|---|
| **Assets** | AS_Bonds_Loans, AS_Structured, AS_CML, AS_RML, AS_Other | Per-asset: ID (CUSIP/ISIN/internal), linkage key to Asset Projections, market value, gross market yield, option-adjusted gross market spread, effective duration, weighted average life, coupon type/rate/floating margin, risk-free curve used for spread determination, BSCR rating mapping, SBA sub-portfolio number, D&D table used. Plus: affiliated/related/connected flags, derivative aggregates and open positions, investment/hedging costs, disposed-asset log, asset-related management expenses |
| **ALM** | ALM_KRD | Key Rate Duration at **2, 5, 10, 20, 30 year** tenors — Assets KRD (incl. and excl. derivatives) and Liability KRD, per sub-portfolio, per tenor. Liability duration sourced from Form 4EBS line 27(d) |
| **SBA — Spread & Reinvestment** | SBA_S&R | Reinvestment spread and target-allocation assumptions (§4.7) |
| **SBA — Curves** | (within SBA section) | UFR, risk-free discount factors, reference-rate curves for other instruments (including inflation/LPI curves) — outputs of §4.1–4.2 |
| **SBA — Liability Cashflows** | (within SBA section) | Per sub-portfolio: cash-flow inflow (premiums/fees) and outflow (claims/expenses) amounts, per scenario, per time period, outflows reported positive; **excludes asset cash flows**; total = inflow − outflow. Fungible blocks combinable only with BMA fungibility approval (§4.9) |
| **SBA — Default & Downgrade** | SBA_D&D | Per §4.5 — Expected Loss from Default and Cost of Downgrade by BSCR rating and tenor |
| **SBA — Stress** | SBA_Stress | Per §9 |
| **SBA — Analysis of Change** | SBA_AoC | Per §8 |
| **Asset Projections** | AP_All_Scenarios, AP_All_Scenarios_Others | Full asset cash-flow/market-value projections across all 9 scenarios — the granular projection output required by §4.3 |
| **Liquidity** | Lapse Profile, Liquidity Projections, Liquidity Sources (optional) | Mass-lapse-by-BSCR-category tables; Cashflow Ratio = Gross Outflows ÷ Gross Inflows under slow-moving and fast-moving stress scenario sets; optional liquidity-source haircut/LCR reporting (§12.2 has the haircut tables) |

---

## 8. Model Outputs — Analysis of Change / Attribution

The SBA_AoC tab requires a **waterfall attribution** of period-over-period movement in **(a) SBA BEL for the biting scenario** and **(b) the implied SBA spread relative to the underlying risk-free rate**, run per material sub-portfolio (**maximum 10**, with any remainder aggregated into "Aggregate of all other small portfolios") ([LLSBA Completion Instructions, §D.6, ¶43–47](https://www.bma.bm/viewPDF/documents/2025-12-23-11-29-23-Lapse-Liquidity-and-Scenario-Based-Approach-Return---Completion-Instructions.pdf)).

Each row below must be a genuine model re-run wherever feasible — estimates are permitted only with documented justification, and for the current filing cycle BMA accepts a "best endeavour" standard given tooling maturity ([ibid., ¶49, 54](https://www.bma.bm/viewPDF/documents/2025-12-23-11-29-23-Lapse-Liquidity-and-Scenario-Based-Approach-Return---Completion-Instructions.pdf)).

| Step | What it isolates |
|---|---|
| **Opening: Prior Period (start)** | Prior period's closing BEL, on the prior biting scenario |
| 1. Model Changes | Revalue at prior-period-start using the *current* period's methodology (asset & liability). Assumption changes are included here **unless** any single change is ≥**5% of start-of-period BEL**, in which case it must be itemized separately under "Other" instead |
| 2. Unwind | Roll the valuation date forward one period: recompute curves via the forward rates implied by the start-of-period curves (§4.2), rebase inflation indices, drop off elapsed cash flows, roll asset market values, unwind D&D risk adjustment for elapsed lifetime. **Validation check: Asset Portfolio IRR must be unchanged** across this step |
| 3. Updated Risk Free Rate | Refresh the liability discount curve and the asset valuation/cash-flow-reference RFR curves to end-of-period levels; revalue asset market values accordingly |
| 4. Update Starting Portfolio Asset Spreads | Roll spreads to end-of-period observed levels (index-based for sold/matured assets); revalue market values |
| 5. Update Asset Portfolio | Reflect the actual end-of-period portfolio (market values and cash flows), **excluding new business**; rebalancing impact included; approximation allowed if separating new-business effects from rebalancing is impractical |
| 6. Update to Assumed Target Asset Allocation | Reinvestment strategic-allocation assumption changes |
| 7. Update to Assumed Reinvestment Spreads | Reinvestment spread assumption changes |
| 8. Variation of Liability Cash Flows for In-force | Actual end-of-period liability model-point profile vs. the start-of-period projection — **excludes** lapse/mortality assumption changes (those sit elsewhere) |
| 9. New Business | New liabilities onboarded plus associated asset-portfolio changes; apportionment approximations allowed if stated |
| 10. Change in Biting Scenario from Prior Period | Isolates the impact of the worst-scenario identity changing period over period |
| 11. Other (a)–(e) | Catch-all: itemize any material change (≥**5% of start-of-period BEL**) not captured above. Candidate categories: Asset Assumptions (default assumptions, asset cash-flow projection updates), Liability Assumptions (lapse, mortality/longevity, expense) |
| **Closing: Closing BEL** | **Reconciliation check** — must tie exactly to the period's reported Closing Assets and BEL on the current-period biting scenario |

Each step must output both a running **BEL (after this step)** and a running **Implied SBA Spread** value, so the waterfall attributes both the reserve movement and the spread movement simultaneously.

---

## 9. Model Outputs — Stress & Scenario Testing

Two distinct stress regimes are required, serving different purposes — do not conflate their calibrations.

### 9.1 SBA Application-Package Stresses

Required whenever the module supports an SBA application or ongoing eligibility validation (superseded Instructions Handbook, §E5.6h — *no live link, see §3*; largely mirrored in [CP2 §2.2](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf)):

| Stress | Mechanics |
|---|---|
| **Combined credit-spread + mass-lapse** | Mass lapse shock = higher of **20% flat** (all products) or the product-specific BSCR mass-lapse shock. Simultaneously widen credit spreads per rating (table below); shock applied instantaneously in year 1 only, reverting to base thereafter. All assets stressed (rated/unrated, AFS/HTM, structured/ABS/MBS included); unrated assets assumed **CCC/C**. |
| **One-notch credit downgrade** | Downgrade every SBA asset by one notch; reprice on the resulting (lower) credit curve — no change to spread *levels* themselves, only to which curve applies. If insufficient SBA-eligible assets remain post-downgrade, fall back to the Standard Approach for the shortfall, subject to the **no-splitting-of-liabilities** rule at policyholder-contract/block-product level (if that condition can't be met, Standard Approach applies to the *entire* block). |
| **No reinvestment into limited-basis assets** | Assume reinvestment into limited-basis (formerly "258E") assets is no longer possible; reflect the resulting change in modeled reinvestment strategy (§4.7). |

**Credit spread widening table (application-package stress):**

| Rating | AAA | AA | A | BBB | BB | B | CCC/C |
|---|---|---|---|---|---|---|---|
| Δ bps | 277 | 328 | 444 | 498 | 842 | 1346 | 2346 |

### 9.2 BSCR-Level Financial Market Scenarios (R1–R9)

Required for the SBA asset portfolio's contribution to BSCR-level stress reporting ([2025 Stress/Scenario Instructions, Section A](https://www.bma.bm/viewPDF/documents/2025-12-19-15-36-02-2025-Year-End-Stress-and-Scenario-Instructions-for-Class-C-D--E.pdf)). Stresses apply "immediately upon occurrence"; SBA liabilities are revalued reflecting stressed asset values, subject to the same no-splitting-of-liabilities rule as above.

| # | Scenario | Magnitude |
|---|---|---|
| **R1** | Equity price decline | **−40%** (Black Monday 1987 calibration); hedging effects reported separately |
| **R2** | Alternatives / Real Estate decline | **−40%**; Level 3 assets shocked −40% separately if overlapping |
| **R3** | Yield curve stress | Moderate Widening +1%, Moderate Tightening −1%, Severe Widening +2%, Severe Tightening −2% (all maturities); credit spreads held constant; **no zero floor** on resulting yields; only Moderate Widening feeds the BSCR model |
| **R4** | Credit spread widening | AAA 199.6bp, AA 249.0bp, A 241.5bp, BBB 276.4bp, BB 947.5bp, Below BB 3,113.6bp; unrated assets assumed **Below BB**; CAT bonds excluded |
| **R5** | Combined | R3 (Moderate Widening) + R1 + R2 + R4 simultaneously |
| **R6** | FX shock | EUR/USD 24.9%, JPY/USD 27.6%, GBP/USD 41.0%, CHF/USD 22.4%, AUD/USD 31.8% |
| **R7** | Sovereign risk escalation | 50% face-value haircut: Greece, Italy, Portugal, Argentina, Turkey; 100% haircut: Ukraine, Russia |
| **R8** | Inflation / monetary policy | Moderate: +5% Y1–Y4 (additive); Severe: +10% Y1–Y4; Deflation: replaces (not additive) prevailing inflation with −1.0%, Y4 rate correction, Y5+ reversion; only the most significant scenario feeds the BSCR model |
| **R9** | Long-Term liquidity stress | Haircuts for 1-in-20 and 1-in-200 market moves; liquid assets in 3 tiers, Tier 3 capped at 30%; mass lapse applied to all lapsable policies; **overall post-stress LCR must be ≥105%** |

Also required, where the module supports the fuller BSCR disclosure: **Section C** (qualitative disclosure of a two-notch-or-below-A− rating downgrade's impact on collateral/liquidity) and **Section E** (reverse stress test — either report the scenario that breaches solvency, or calculate the loss size that would breach ECR and its implied return period), both in the [2025 Stress/Scenario Instructions](https://www.bma.bm/viewPDF/documents/2025-12-19-15-36-02-2025-Year-End-Stress-and-Scenario-Instructions-for-Class-C-D--E.pdf). Section B (underwriting-loss scenarios) and Section F (technology risk) are liability/operational-side disclosures, out of scope for this asset-modeling module.

---

## 10. Model Outputs — Well-Matched Portfolio Metrics

There is **no single BMA formula** for "well-matched" — the insurer must define its own standard, document the assessment, and set its own thresholds/tolerances/triggers ([Instructions Handbook, §E4.1](https://www.bma.bm/viewPDF/documents/2025-12-19-15-00-17-2025-Year-end-Long-Term-Instructions-Handbook.pdf)). What the module must be able to compute are the **nine criteria BMA uses to assess that self-defined standard** ([Instructions Handbook, §E4.3a–i](https://www.bma.bm/viewPDF/documents/2025-12-19-15-00-17-2025-Year-end-Long-Term-Instructions-Handbook.pdf)) — these should be modeled as a **configurable metrics/thresholds panel**, not hard-coded regulatory constants:

| # | Metric | Computation |
|---|---|---|
| a | Cost of mismatch | Base-scenario result − biting-scenario result (§6, step 5) |
| b | Scenario dispersion | Spread/dispersion of BEL results across the 8 stress scenarios |
| c | Capital as % of BEL | BSCR capital required for currency, interest rate, lapse, mortality, morbidity, and longevity risk, each as a % of BEL |
| d | Currency matching | Extent assets and liabilities share currency denomination; hedging extent/nature/effectiveness; residual risk |
| e | Asset sales as % of BEL | Total asset sales made to meet cash-flow shortfalls, as a % of BEL |
| f | Reinvestment dependence | Graphical comparison of annual liability cash flows vs. existing-asset cash flows vs. reinvestment-asset cash flows, plus sensitivity of BEL to reinvestment-assumption changes |
| g | Peak cash-flow shortfall | Highest accumulated cash-flow shortfall across all projection years, as a % of BEL |
| h | KRD gap vs. tolerance | ALM position (asset KRD vs. liability KRD, §7 ALM_KRD) vs. internal tolerances, at the 2/5/10/20/30-year key rate points |
| i | Fungibility/encumbrance | Extent to which portfolio assets are fungible or encumbered |

---

## 11. Governance & Documentation Hooks

The regulation attaches heavy process requirements to SBA use — board approval, officer attestations, model change policy, data quality policy, and periodic model validation ([Schedule XXVI, para 28(35)–(41)](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf); superseded Instructions Handbook §E2–E3 — *no live link*; [CP2 §2.12–2.17](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf)). These are organizational, not computational, requirements — full detail is out of scope for this spec — but the module should provide the supporting data plumbing so the human process has something to point to:

- **Assumption/model-change audit trail**: every change to a scenario definition, curve methodology, D&D table, or reinvestment/disinvestment assumption should be logged with who/when/why, sized against the insurer's own major-vs-minor materiality threshold — this is what backs the required **model change log** ([CP2, §2.14](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf)).
- **Versioning**: the ability to reproduce a prior period's exact BEL calculation (curve, scenario set, D&D table, asset portfolio as of that date) — needed both for the AoC "Unwind"/"Model Changes" steps (§8) and for model validation re-runs.
- **Attestation capture**: a place to attach the CIO's reinvestment/disinvestment-strategy attestation (§4.8) and the Chief Actuary/CRO/CIO sign-offs referenced throughout Schedule XXVI, rather than requiring these to live outside the system.
- **Well-matched documentation**: a structured place to record the insurer's own definition of "well-matched" and its thresholds/triggers (§10), since BMA explicitly requires this to be a documented, not just computed, assessment.

---

## 12. Appendices

### 12.1 Full 9-Scenario Formula Reference

See §4.3 for the complete table. Implementation note: scenarios (f)–(i) require interpolation between the three stated anchor points (year 1, year 10, year 30); scenarios (b)–(e) require interpolation to a single anchor point (year 5 or year 10) and are flat thereafter.

### 12.2 Lapse Cost Eligibility — Supporting Tables

**Mass-lapse liability outflow shock (% of liability, by time restraint × economic penalty × book type)** — [CP2, §2.4](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf):

| Economic penalty | Retail, Low restraint | Inst., Low restraint | Retail, Medium restraint | Inst., Medium restraint | Retail, High restraint | Inst., High restraint |
|---|---|---|---|---|---|---|
| Low (no penalty) | 25% | 50% | 12.50% | 25% | 0% | 0% |
| Medium (<20% penalty) | 12.50% | 25% | 6.25% | 12.50% | 0% | 0% |
| High (>20% penalty) | 0% | 1.25% | 0% | 0% | 0% | 0% |

*Time restraint: Low = under 1 week; Medium = 1 week to under 3 months; High = over 3 months (shocked to zero — delay disincentivizes surrender).*

**Eligible liquidity source haircuts** — [CP2, §2.4](https://www.bma.bm/viewPDF/documents/2023-07-28-15-25-26-Consultation-Paper---Proposed-Enhancements-to-the-Regulatory-Regime-and-Fees-for-Commercial-Insurers.pdf):

| Source | Tier | Haircut |
|---|---|---|
| Cash / demand deposits | 1 | 0% |
| Sovereigns rated AA- and above | 1 | 0.70% × WAL |
| Sovereigns rated BBB- and above | 1 | 1.40% × WAL |
| Public Corporates rated AA- and above | 2 | 1.40% × WAL |
| Public Corporates rated BBB- and above | 2 | 1.50% × WAL |
| Publicly traded equity | 3 | 65% |
| Certificates of Deposit | 3 | 60% |
| Undrawn committed lines | 3 | 90% |
| Liquid mutual/money market funds | 3 | 85% |
| Liquid ETFs | 3 | 90% |
| AAA MBS, WAL < 10y | 3 | 1.90% × WAL |
| AAA other structured, WAL < 10y | 3 | 2.20% × WAL |
| All other potential sources | 4 | 100% |

*Tier 3 sources capped at 30% of total liquidity sources for LCR purposes; tiers 2–3 cannot defease "Low" time-restraint (under 1 week) outflows — only Tier 1 counts there.*

### 12.3 Capital-Charge Interaction (Standard Approach Interest Rate Risk Offset)

Where SBA BEL dispersion is available, the Standard Approach interest-rate capital charge may be offset ([Instructions Handbook, "Option 2" formula, D19](https://www.bma.bm/viewPDF/documents/2025-12-19-15-00-17-2025-Year-end-Long-Term-Instructions-Handbook.pdf)):

```
C_Interest = max{ max(Shock_IR,Down, Shock_IR,Up) − OffSet_ScenarioBased,  0 }

OffSet_ScenarioBased = min( 0.5 × (BEL_WorstScenario − BEL_BaseScenario),
                             0.75 × C_Interest_WithoutOffset )
```

This module should expose `BEL_WorstScenario − BEL_BaseScenario` (= §6 step 5, "cost of mismatch") cleanly enough for whatever computes the BSCR capital charge to consume it.

### 12.4 Risk Margin Formula (downstream consumer, for context only)

```
RM = CoC × Σ[t≥0]  ModECR_t / (1 + r_(t+1))^(t+1)
```

Where `CoC` = BMA-prescribed cost-of-capital rate, `ModECR_t` = projected ECR at time t for insurance/credit/operational/non-hedgeable market risk, `r_t` = BMA-prescribed **risk-free** rate (no illiquidity adjustment) for maturity t. This is a company-level calculation outside this module's scope, but it consumes this module's risk-free curve output (§4.1) ([Schedule XXVI, para 36](https://www.bma.bm/viewPDF/documents/2024-03-28-13-20-55-Insurance-Prudential-Standards-Group-Solvency-Requirement-Amendment-Rules-2024.pdf)).

### 12.5 LLSBA Asset Tab Field Reference (Core Fields)

Minimum field set per asset, across the five asset tabs (AS_Bonds_Loans, AS_Structured, AS_CML, AS_RML, AS_Other) — [LLSBA Completion Instructions §B.2](https://www.bma.bm/viewPDF/documents/2025-12-23-11-29-23-Lapse-Liquidity-and-Scenario-Based-Approach-Return---Completion-Instructions.pdf):

- Asset ID (CUSIP/ISIN/Internal) and Asset ID in Asset Projections (linkage key)
- Market Value (mark-to-market or mark-to-model fair value)
- Gross Market Yield; Option-Adjusted Gross Market Spread
- Effective Duration; Weighted Average Life
- Coupon Type / Fixed Coupon / Floating Margin
- Risk-Free Curve Used for Spread Determination
- BSCR Rating Mapping
- SBA Sub-portfolio Number
- Default and Downgrade Table Used
- *(CML-specific)* Loan-to-Value, Debt Service Coverage Ratio
- *(RML-specific)* Loan-to-Value, mortgage type/purpose, amortization status, documentation, credit score

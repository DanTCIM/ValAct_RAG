# BMA 2024 vs 2025 Instruction Comparison — Based on ChatGPT summary

**Use the information at your own risk**

- [Question 1: Compare LLSBA (LAPSE, LIQUIDITY AND SCENARIO-BASED APPROACH RETURN) between 2024 and 2025](#question-1-compare-llsba-lapse-liquidity-and-scenario-based-approach-return-between-2024-and-2025)
- [Question 2: Stress scenarios 2024 vs 2025](#question-2-stress-scenarios-2024-vs-2025)
- [Question 3: Compare Long-term Insurance Handbook 2024 vs. 2025](#question-3-compare-long-term-insurance-handbook-2024-vs-2025)

---

## Question 1: Compare LLSBA (LAPSE, LIQUIDITY AND SCENARIO-BASED APPROACH RETURN) between 2024 and 2025

References

- [2025 LLSBA](https://www.bma.bm/viewPDF/documents/2025-12-23-11-29-23-Lapse-Liquidity-and-Scenario-Based-Approach-Return---Completion-Instructions.pdf)
- [2024 LLSBA](https://www.bma.bm/viewPDF/documents/2025-03-19-11-24-30-Lapse-Liquidity-and-Scenario-Based-Approach-Return---2024-Completion-Instructions.pdf)

**Executive summary**

2025 is a structural re-write, not a minor refresh:

- clearer regulatory intent
- stronger ALM + projection linkage (e.g., asset projections)
- more mandatory flags, identifiers, and consistency checks
- clearer treatment of affiliated / connected assets
- reduced ambiguity around what must be completed by whom

**Key sections covered:**

	1. Structural organization
	2. Regulatory intent
	3. Affiliated / connected assets
	4. Asset taxonomy
	5. Field definitions
	6. ALM, projections, and liquidity

#### 1. Structural organization: major redesign

2025 expects firms to think in systems (assets → projections → liquidity → stress), not just complete tabs.

> *2024 = descriptive reporting framework*  
> *2025 = integrated risk & modeling framework*

**2024 Instructions**

* Organized primarily by:
	* Asset categories (Bonds, Alternatives, Structured Assets, Real Estate, etc.)
	* Then SBA mechanics (curves, cashflows, defaults, lapse, liquidity)
* Heavy emphasis on asset-level descriptive fields
* ALM concepts were present but loosely coupled to assets

**2025 Instructions**

* Reorganized into clear functional sections:
	* Assets
	* ALM
	* SBA
	* Asset Projections (new in 2025)
	* Liquidity
* Explicit separation between:
	* Static asset description
	* Dynamic modeling inputs
* ALM and projections are now first-class sections, not appendices

#### 2. Regulatory Intent

2025 explicitly states that insurers using the standard approach must still complete Assets + ALM + Liquidity, closing a loophole that existed in 2024.

**2024**

* Describes how to complete fields
* Less explicit on why certain data is required
* Some ambiguity around:
	* Standard vs SBA filers
	* Asset approval vs year-end reporting

**2025**

* Very explicit on:
	* Who completes which tabs
	* When SBA vs standard approach applies
	* Which tabs are mandatory vs optional
* Introduces clearer language around:
	* Risk sensitivity
	* Model governance
	* Supervisory review expectations

#### 3. Affiliated / connected assets

2025 requirement materially increases compliance burden for:

* Intra-group structures
* Private credit
* Fund investments with complex ownership chains

**2024**

* Affiliated assets discussed, but embedded across sections
* Approval logic implied rather than operationalized

**2025**

* Dedicated section: “Affiliated, Related and Connected Assets”
* Clear definitions:
	* Affiliated
	* Related
	* Connected
* Explicit look-through requirement
* Mandatory identification flags across multiple asset tabs

#### 4. Asset taxonomy: simplified but more prescriptive

Fewer places to hide ambiguity + Easier for supervisors to run consistency checks

**2024**

* Very granular asset categories
* Multiple overlapping mappings (e.g., loans vs ABS vs alternatives)
* Heavier reliance on narrative explanations

**2025**

* Asset universe streamlined into five core asset sheets:
	* Bonds & Loans
	* Structured Assets
	* Commercial Mortgage Loans
	* Residential Mortgage Loans
	* Other Assets
* Each field now has:
	* Scope
	* Mandatory / conditional status

#### 5. Field definitions: sharper and more enforceable

2025 treats fields as model inputs, not just disclosures.

| Aspect              | 2024        | 2025                               |
|---------------------|-------------|------------------------------------|
| Mandatory flags     | Sparse      | Explicit per field                 |
| Asset IDs           | Basic       | Required linkage to projections    |
| Encumbrance         | Light       | Explicit + conditional fields      |
| Optionality / PIK   | Mentioned   | Mandatory flags + types            |
| Ratings             | Broad       | Expanded agency coverage + logic   |
| SBA linkage         | Conceptual  | Explicit table references          |

#### 6. ALM, projections, and liquidity: biggest conceptual leap

This is the single biggest change in practice.

**2024**

* Liquidity and lapse projections present
* Asset cashflows and liabilities loosely linked
* Asset projections less explicit

**2025**

* New dedicated sections:
	* ALM
	* Asset Projections (new)
	* Liquidity Sources (optional / on request)
* Assets must now:
	* Map cleanly to projection IDs
	* Align with liability sub-portfolios
	* Be consistent across SBA stress, default, and reinvestment tabs

---

## Question 2: Stress scenarios 2024 vs 2025

References

- [2025 Stresses](https://www.bma.bm/viewPDF/documents/2025-12-19-15-36-02-2025-Year-End-Stress-and-Scenario-Instructions-for-Class-C-D--E.pdf)
- [2024 Stresses - download](https://cdn.bma.bm/documents/2024-12-02-16-22-37-2024-Year-End-Stress-and-Scenario-Instructions-for-Class-C-D--E.pdf)

**High-level summary**
- No material quantitative changes to stress calibrations
- Changes focus on clarification, tightening, and consistency

### Key observations
- Balance sheet date rolled forward (1 Jan 2025 → 1 Jan 2026)
- SBA vs Standard Approach language strengthened
	- Explicit quote-style emphasis on “no splitting of liabilities”
	- If SBA eligibility fails under stress → use Standard Approach
	- Partial fallback must be disclosed
- Liquidity stress mechanics unchanged but review for definitions tightening


---

## Question 3: Compare Long-term Insurance Handbook 2024 vs. 2025

References

- [2025 Instruction Handbook](https://www.bma.bm/viewPDF/documents/2025-12-19-15-00-17-2025-Year-end-Long-Term-Instructions-Handbook.pdf)
- [2024 Instruction Handbook](https://www.bma.bm/viewPDF/documents/2024-12-02-12-56-21-2024-Year-end-Long-Term-Instructions-Handbook.pdf)

#### Structure and themes
- Same six-part spine (Sections A–F)
- No re-architecture, but consolidation and normalization
- SBA section (E) becomes more modular and self-contained
- Transitional language reduced
- Submission workflow centralized
- Shift from transitional to steady-state framing
- SBA positioned for deeper supervisory review

> You can safely ignore ~60% of the document if your focus is SBA, stress, liquidity, or asset approval.

#### SBA (Scenario-based Approach)

> *Section E stops being “how to use SBA” and becomes “the rules of engagement for internal models.”*

- Same subsection headings (E1–E12)
- No reordering or new sections

**Major shifts**
- Section E evolves from approval overlay → supervisory framework
- Governance moves from documentation → enforceable control
- SBA approval treated as ongoing, not permanent
- Stress interaction becomes central to eligibility

### Thematic analysis
- **E1:** BMA discretion elevated and ongoing
	- Approval ≠ permanence
	- BMA's discretion can revert SBA to Standard Approach
- **E2–E3:** Attestations and model change policy become accountability gates
	- Emphasis on change triggers, materiality, BMA visibility, pre- vs. post-approval changes
- **E4:** Well-matched portfolios treated as constraints
	- If portfolios stop being well-matched under stress → SBA may fail
- **E5:** Application becomes lifecycle requirement
	- Ongoing completeness standard
- **E6–E8:** Asset approval integrated across portfolios
	- Stronger consistency expectations across: Asset approval, Stress eligibility, Liquidity treatment, Default / downgrade modeling
- **E9–E11:** Curves, defaults, costs treated as model-critical
- **E12:** Supervisory safety valve



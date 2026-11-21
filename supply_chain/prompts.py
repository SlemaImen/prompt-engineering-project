from langchain_core.messages import HumanMessage, SystemMessage

ZERO_SHOT_SYSTEM = """
You are a Senior Supply Chain Risk Analyst at TransGlobal Manufacturing.

### Expected Behavior

- Act as an experienced supply chain risk analyst.
- Base all observations, conclusions, and recommendations solely on the information provided in the input.
- Do not assume, infer, or fabricate facts that are not explicitly supported by the dataset.
- If sufficient evidence is unavailable, clearly indicate that additional operational data is required.
- Maintain a professional, objective, and business-oriented tone.
- Focus on producing accurate, concise, and actionable insights that support executive decision-making.

## Output Requirements

- Present the report using clear section headings.
- Use bullet points wherever appropriate.
- Do not generate a report template.
- Do not include placeholder fields such as Date, Prepared By, Company Name, or Contact Information.
"""

ZERO_SHOT_USER = """
Analyze the following supply chain disruption dataset and prepare a Business Impact Assessment Report.

## Input Data

{business_context}

## Report Structure

1. Executive Summary
2. Identified Disruptions
3. Root Causes
4. Supplier Impact
5. Inventory Impact
6. Production Risk
7. Logistics Risk
8. Financial Implications
9. Recommended Mitigation Strategies
10. Business Continuity Assessment
"""


def zero_shot_messages(business_context: str) -> list:
    return [
        SystemMessage(content=ZERO_SHOT_SYSTEM),
        HumanMessage(content=ZERO_SHOT_USER.format(business_context=business_context)),
    ]


FEW_SHOT_SYSTEM = """
You are a Senior Supply Chain Risk Analyst at TransGlobal Manufacturing.

### Expected Behavior

- Act as an experienced supply chain risk analyst.
- Analyze supply chain disruption data and generate evidence-based business impact assessment reports.
- Learn the expected analytical style, reasoning approach, and response format from the reference examples provided by the user.
- Apply the learned style consistently while analyzing the user's input.
- Base all observations, conclusions, and recommendations solely on the information provided.
- Do not assume, infer, or fabricate facts that are not explicitly supported by the input.
- If sufficient evidence is unavailable, clearly indicate that additional operational data is required.
- Maintain a professional, objective, and business-oriented tone.
- Produce concise, accurate, and actionable insights suitable for executive decision-making.

## Output Requirements

- Present the report using clear section headings.
- Use bullet points wherever appropriate.
- Generate a concise, consistent, and executive-ready business report.
- Do not generate a report template.
- Do not include placeholder fields such as Date, Prepared By, Company Name, or Contact Information.
"""

FEW_SHOT_USER = """
Analyze the following supply chain disruption dataset and prepare a comprehensive Business Impact Assessment Report by following the analytical style, report structure, and level of detail demonstrated in the reference examples.

## Reference Examples

========================================================
### Example 1 – Port Congestion

#### Scenario

A Tier-1 electronics supplier shipping semiconductor chips through the Port of Singapore experienced severe port congestion.

#### Observed Business Impact
- Shipment delayed by 9 days.
- Inventory dropped below the safety stock level.
- Assembly line utilization decreased.
- Logistics costs increased because of expedited air freight.

#### Analysis

**Executive Summary**
Port congestion disrupted inbound material flow, increasing logistics costs and creating moderate production risk.

**Root Causes**
- Port congestion
- Vessel scheduling delays

**Supplier Impact**
The supplier fulfilled the order but experienced significant delivery delays.

**Inventory Impact**
Inventory levels declined below the required safety stock.

**Production Risk**
Production schedules required partial replanning.

**Logistics Risk**
Inbound transportation reliability decreased.

**Financial Implications**
Additional logistics expenses increased operational costs.

**Recommended Mitigation Strategies**
- Diversify shipping ports.
- Increase safety stock for critical components.
- Establish alternate logistics partners.

**Business Continuity Assessment**
Operations continued with manageable disruption.

========================================================
### Example 2 – Supplier Failure

#### Scenario

A Tier-2 supplier manufacturing industrial bearings declared bankruptcy, resulting in an immediate suspension of component deliveries.

#### Observed Business Impact
- Production stopped for two manufacturing lines.
- Inventory exhausted within five days.
- Customer deliveries postponed.
- Revenue at risk increased significantly.

#### Analysis

**Executive Summary**
Supplier failure created a critical supply interruption affecting production continuity.

**Root Causes**
- Supplier insolvency
- Lack of alternate sourcing

**Supplier Impact**
Complete disruption of material supply.

**Inventory Impact**
Critical inventory depletion.

**Production Risk**
High production downtime.

**Logistics Risk**
Alternative sourcing required emergency transportation.

**Financial Implications**
Revenue losses and emergency procurement costs increased substantially.

**Recommended Mitigation Strategies**
- Qualify secondary suppliers.
- Increase supplier financial monitoring.
- Maintain strategic inventory reserves.

**Business Continuity Assessment**
Business continuity is at high risk without immediate intervention.

========================================================
### Example 3 – Geopolitical Disruption

#### Scenario

Trade restrictions between two countries disrupted cross-border transportation of electronic components used in multiple production facilities.

#### Observed Business Impact
- Customs clearance delayed.
- Lead time increased by 14 days.
- Procurement costs increased.
- Manufacturing schedules required revision.

#### Analysis

**Executive Summary**
Geopolitical instability significantly disrupted international material flow.

**Root Causes**
- Border restrictions
- Trade sanctions
- Customs inspections

**Supplier Impact**
International suppliers experienced prolonged delivery delays.

**Inventory Impact**
Material availability declined across multiple facilities.

**Production Risk**
Manufacturing schedules became uncertain.

**Logistics Risk**
International transportation routes were severely affected.

**Financial Implications**
Higher procurement and logistics costs reduced operating margins.

**Recommended Mitigation Strategies**
- Diversify supplier locations.
- Increase regional sourcing.
- Maintain alternate transportation routes.

**Business Continuity Assessment**
Operations continued under elevated supply chain risk.

========================================================

## Input Data

Supply Chain Disruption Dataset

{business_context}

## Report Structure

1. Executive Summary
2. Identified Disruptions
3. Root Causes
4. Supplier Impact
5. Inventory Impact
6. Production Risk
7. Logistics Risk
8. Financial Implications
9. Recommended Mitigation Strategies
10. Business Continuity Assessment
"""


def few_shot_messages(business_context: str) -> list:
    return [
        SystemMessage(content=FEW_SHOT_SYSTEM),
        HumanMessage(content=FEW_SHOT_USER.format(business_context=business_context)),
    ]



COT_SYSTEM = """
You are a Senior Supply Chain Risk Analyst at TransGlobal Manufacturing.

### Expected Behavior

- Act as an experienced supply chain risk analyst.
- Analyze supply chain disruption data and generate evidence-based business impact assessment reports.
- Use a structured reasoning approach to evaluate the available information before generating the final response.
- Base all observations, conclusions, and recommendations solely on the information provided.
- Do not assume, infer, or fabricate facts that are not explicitly supported by the input.
- If sufficient evidence is unavailable, clearly indicate that additional operational data is required.
- Maintain a professional, objective, and business-oriented tone.
- Produce concise, accurate, and actionable insights suitable for executive decision-making.
- Provide only the final report unless the user explicitly requests your reasoning process.

## Output Requirements

- Present the report using clear section headings.
- Use bullet points wherever appropriate.
- Generate a concise, logical, and executive-ready business report.
- Do not generate a report template.
- Do not include placeholder fields such as Date, Prepared By, Company Name, or Contact Information.
"""

COT_USER = """
Analyze the following supply chain disruption dataset and prepare a comprehensive Business Impact Assessment Report.

## Input Data

Supply Chain Disruption Dataset

{business_context}

## Task

Perform a structured analysis of the provided dataset before generating the final report.

## Report Structure

1. Executive Summary
2. Identified Disruptions
3. Root Causes
4. Supplier Impact
5. Inventory Impact
6. Production Risk
7. Logistics Risk
8. Financial Implications
9. Recommended Mitigation Strategies
10. Business Continuity Assessment
"""


def cot_messages(business_context: str) -> list:
    return [
        SystemMessage(content=COT_SYSTEM),
        HumanMessage(content=COT_USER.format(business_context=business_context)),
    ]



TOT_SYSTEM = """
You are a Senior Supply Chain Risk Analyst at TransGlobal Manufacturing.

### Expected Behavior

- Act as an experienced supply chain risk analyst.
- Analyze supply chain disruption data and generate evidence-based Business Impact Assessment Reports.
- Consider multiple plausible solution approaches before selecting the most appropriate recommendation.
- Evaluate alternative mitigation strategies based on business impact, feasibility, implementation effort, cost, and business continuity.
- Compare the strengths and trade-offs of each alternative before arriving at the final recommendation.
- Base all observations, conclusions, and recommendations solely on the information provided.
- Do not assume, infer, or fabricate facts that are not explicitly supported by the input.
- If sufficient evidence is unavailable, clearly indicate that additional operational data is required.
- Maintain a professional, objective, and business-oriented tone.
- Produce concise, accurate, and actionable insights suitable for executive decision-making.
- Provide only the final report unless the user explicitly requests your reasoning process.

## Output Requirements

- Present the report using clear section headings.
- Use bullet points wherever appropriate.
- Generate a concise, logical, and executive-ready business report.
- Do not generate a report template.
- Do not include placeholder fields such as Date, Prepared By, Company Name, or Contact Information.
"""

TOT_USER = """
Analyze the following supply chain disruption dataset and prepare a comprehensive Business Impact Assessment Report.

## Input Data

Supply Chain Disruption Dataset

{business_context}

## Task

Develop mitigation recommendations by considering multiple feasible approaches for each major disruption and recommend the most appropriate strategy based on the available evidence.

## Report Structure

1. Executive Summary
2. Identified Disruptions
3. Root Causes
4. Supplier Impact
5. Inventory Impact
6. Production Risk
7. Logistics Risk
8. Financial Implications
9. Recommended Mitigation Strategies
10. Business Continuity Assessment
"""


def tot_messages(business_context: str) -> list:
    return [
        SystemMessage(content=TOT_SYSTEM),
        HumanMessage(content=TOT_USER.format(business_context=business_context)),
    ]
# Research Notes: AI Development (October 2026 Update)

Research date: 2026-10-04

These notes collect publicly available sources on the state of artificial intelligence (AI) development as of October 2026. They are the basis for the report `report/AI_발전_보고서_v2.docx`. Some figures come from secondary summaries rather than the primary reports, so treat individual numbers as indicative. Where sources disagree, both figures are given.

## 1. Capabilities and frontier models

- AI capability is accelerating, not plateauing. On the SWE-bench coding benchmark, top scores rose from about 60% to nearly 100% within one year. (Stanford AI Index 2026)
- The frontier is "jagged." Models that win gold at the International Mathematical Olympiad read analog clocks correctly only 50.1% of the time. Headline benchmarks are a poor proxy for real-world performance. (Stanford AI Index 2026)
- The performance gap between the United States and China has effectively closed. (Stanford AI Index 2026)
- Release cadence is very fast. Between February and June 2026, major releases included Gemini 3.1 Pro, GPT-5.5, Grok 4.3, Qwen 3.7 Max, DeepSeek V4, GLM-5.2, and Kimi K2.6. In early September 2026, GPT-6 Astra, Claude Fable 5.1, Gemini 3.8 Flash, and Meta Muse Spark 1.3 shipped within two days of each other. (Industry trackers, secondary sources)
- Open-weight models are close to the frontier. DeepSeek V4 (24 April 2026, MIT license) is a 1.6-trillion-parameter mixture-of-experts model with 49B active parameters and a 1M-token context. Four of the top five open-weight models come from Chinese labs. (Industry trackers, secondary sources)
- Model prices keep falling. One tracker reports a 119x price spread among models and a price floor of $0.10 per million tokens in September 2026. (Industry tracker, secondary source)

## 2. AI agents

- AI is moving from chatbots to agents that use tools, browse the web, operate computers, manage files, and do software engineering tasks. (International AI Safety Report 2026)
- Gartner reports that 80% of enterprise applications shipped or updated in Q1 2026 embed at least one AI agent, up from 33% in 2024.
- Adoption figures vary by survey: 65% of enterprises say they already use AI agents (CrewAI survey); 57.3% of professionals report agents in production, up from 51% (other surveys).
- Companies report automating 31% of workflows with agentic AI on average and expect a further 33% increase in 2026.
- The production gap is large: about 88% of agent pilots do not reach production. Top blockers are evaluation gaps (64%), governance friction (57%), and model reliability (51%).

## 3. Investment and infrastructure

- J.P. Morgan estimates hyperscaler capex at $697B in 2026. Another estimate puts Big Four capex at up to $630B, about 62% above the record $388B in 2025.
  - Amazon: about $200B; Meta: $115–135B (up from $72B); Microsoft: $110–120B (up from $90B).
- About 75% of 2026 hyperscaler capex (about $545B) is tied to AI infrastructure. More than 60% of that goes to power, cooling, and data center construction rather than compute hardware.
- Electricity is now the main bottleneck for AI infrastructure.
- 88% of organizations use AI, and generative AI reached 53% population adoption faster than the PC or the internet. (Stanford AI Index 2026)

## 4. Energy demand

- Data centers used about 485 TWh of electricity in 2025. Demand grew 17% in 2025, while demand from AI-focused data centers grew 50%. Global electricity demand grew only about 3%. (IEA)
- The IEA projects data center consumption of about 950 TWh in 2030, roughly double 2025 levels and about 3% of global electricity demand. Consumption by AI-focused data centers is projected to triple over 2025–2030. (IEA)

## 5. Jobs and the economy

- AI skills appear in 2.5% of all U.S. job postings, up 55% year over year and 297% over a decade. (Stanford AI Index 2026)
- PwC's 2026 Global AI Jobs Barometer, based on more than one billion job ads in 27 countries and territories, finds:
  - The average wage premium for AI skills rose to 62% (from 57%). It ranges from 16% in government to 118% in consumer markets.
  - Jobs requiring AI skills grew 69%, almost eight times faster than the overall job market (9%).
  - The most AI-capable companies grew headcount faster (52% vs. 36%) and wages faster (24% vs. 17%) than the least AI-exposed ones.
- Entry-level work is changing the most. 38% of employers moved basic data processing from entry-level staff to AI, and 31% raised experience requirements for entry-level jobs. (ZipRecruiter AI Employer Report 2026)
- AI-exposed entry-level roles are seven times more likely to require senior-level skills such as judgment and leadership. (PwC 2026)
- Overall, reports suggest AI is not eliminating entry-level jobs outright but is raising the skill bar and narrowing the traditional entry path.

## 6. Regulation and policy

### European Union

- The Digital Omnibus package (Regulation (EU) 2026/1744) received final Council approval on 29 June 2026 and has been in force since 27 July 2026.
- Obligations for stand-alone high-risk AI systems (Annex III: employment, credit scoring, education, essential services, and similar) moved from 2 August 2026 to 2 December 2027. Obligations for AI embedded in regulated products (Annex I) moved to 2 August 2028.
- Article 50 transparency obligations (disclosing AI interactions) still apply from 2 August 2026. Only the watermarking requirement for systems already on the market received a grace period to 2 December 2026.

### United States

- The executive order "Ensuring a National Policy Framework for Artificial Intelligence" (11 December 2025) seeks a "minimally burdensome national standard" and federal preemption of state AI laws.
- It created an AI Litigation Task Force to challenge state laws. The Department of Commerce was required to identify burdensome state laws by 11 March 2026.
- An executive order cannot overturn state law on its own; that requires Congress or the courts. State laws remain enforceable for now.

### South Korea

- The AI Basic Act (Framework Act on the Development of AI and the Establishment of a Foundation for Trust) took effect on 22 January 2026. It is described as the first comprehensive AI law in the world to take full effect, since the EU AI Act applies in phases.
- It takes a risk-based approach. High-impact AI in about ten areas (hiring, lending, healthcare, education, transport, and others) faces stricter duties.
- Generative AI must give prior notice to users and label or watermark its outputs.
- The Act also supports industry through R&D funding, AI data centers, and talent programs. The government plans a guidance period of at least one year before full enforcement.

## 7. Safety and risks

- Documented AI incidents rose from 233 to 362 year over year. Only half of U.S. middle and high schools have AI policies. (Stanford AI Index 2026)
- The International AI Safety Report 2026 groups risks into three categories:
  - **Malicious use:** deepfake fraud is rising. In one evaluation, an AI agent found 77% of known vulnerabilities in real software. Only 3% of 375 surveyed biological AI tools have safeguards.
  - **Malfunctions:** hallucinations have become less common, but risk management remains fallible. Pre-deployment testing is harder because models can tell test settings from real deployment.
  - **Systemic risks:** automation of a wide range of cognitive tasks, especially in knowledge work.
- The long-term trajectory is highly uncertain. Plausible 2030 scenarios range from a plateau to dramatic acceleration. (International AI Safety Report 2026)

## 8. South Korea's AI strategy

- South Korea secured a commitment for 260,000 NVIDIA GPUs at APEC 2025 and aims to own 50,000 GPUs domestically by 2028.
- The Sovereign AI Foundation Model project funds elite teams (currently LG, SKT, Upstage, and Motif) with GPUs, data, and talent. The goal is at least 95% of the performance of leading global models.
- Key challenges are power supply (grid connection requests up about eightfold) and debates over how independent the models really are.

## 9. Key takeaways

1. Capability is rising fast but unevenly, and benchmarks overstate real-world reliability.
2. Agents are spreading quickly, but most pilots still fail to reach production.
3. Investment is at record levels, and power has become the binding constraint.
4. AI raises wages and productivity for skilled workers while shrinking the traditional entry-level path.
5. Regulation is diverging: the EU is delaying parts of its rules, the U.S. is pushing federal preemption, and South Korea has put a comprehensive law into effect.
6. Safety practice and policy are lagging behind capability.

## Sources

- Stanford HAI, AI Index Report 2026 (summaries: https://www.starkinsider.com/2026/04/stanford-2026-ai-index-report.html, https://dcthemedian.substack.com/p/20-takeaways-from-stanfords-2026)
- International AI Safety Report 2026: https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026
- IEA, Energy and AI: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
- PwC, 2026 Global AI Jobs Barometer: https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-jobs-barometer.html
- ZipRecruiter, 2026 AI Employer Report: https://www.ziprecruiter-research.org/economic-insights-research/ai-employer-report-2026
- AI agent adoption: https://www.digitalcommerce360.com/2026/02/11/survey-enterprises-ai-agents-crewai-report/, https://www.digitalapplied.com/blog/ai-agent-adoption-2026-enterprise-data-points
- Hyperscaler capex: https://www.jpmorgan.com/insights/banking/capital-markets/financing-ai-infrastructure-data-centers, https://datacenterrichness.substack.com/p/hyperscalers-plan-630-billion-in
- Frontier models: https://www.teamday.ai/blog/best-ai-models-2026, https://neuralwired.com/2026/05/29/best-open-source-ai-models-2026/, https://local-ai-zone.github.io/blog/September_2026_AI_Model_Updates.html
- EU Digital Omnibus: https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes, https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
- U.S. executive order: https://www.hoganlovells.com/en/publications/white-house-issues-executive-order-to-establish-a-federal-ai-policy-and-preempt-state-laws, https://www.ropesgray.com/en/insights/alerts/2026/03/the-white-house-legislative-recommendations-national-policy-framework-for-artificial-intelligence-an
- Korea AI Basic Act: https://kbthink.com/life/daily/ai-basic-act.html, https://www.shinkim.com/kor/media/newsletter/3114
- Korea sovereign AI and GPUs: https://www.hankyung.com/article/202605318606i, https://biz.heraldcorp.com/article/10766420, https://factrace.kr/topics/ai-industry-2026

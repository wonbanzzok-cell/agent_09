# Research Notes: The Development of AI (as of October 2026)

These notes summarize publicly available sources on the state of artificial intelligence (AI) development. Figures are taken from the sources listed under each section; secondary summaries were used where primary reports were not directly accessible, so treat individual numbers as indicative.

## 1. Capabilities and performance

- AI capability is accelerating rather than plateauing. Industry produced more than 90% of notable frontier models in 2025. (Stanford AI Index 2026)
- Several frontier models now meet or exceed human baselines on PhD-level science questions, multimodal reasoning, and competition mathematics. (Stanford AI Index 2026)
- On the SWE-bench Verified coding benchmark, top performance rose from about 60% to nearly 100% within a single year. (Stanford AI Index 2026)
- The U.S.–China performance gap has effectively closed. DeepSeek-R1 briefly matched the top U.S. model in February 2025; as of March 2026 the leading U.S. model (Anthropic) led by only 2.7%. (Stanford AI Index 2026)
- General-purpose AI reaches expert-level performance in law, coding, and science, but performance is "jagged": systems excel at complex tasks and still fail at some simple ones. (International AI Safety Report 2026)

## 2. AI agents

- AI is moving from chatbots to agents that use tools, browse the web, operate computers, manage files, and carry out software engineering tasks. (International AI Safety Report 2026)
- Gartner predicts 40% of enterprise applications will include task-specific AI agents by the end of 2026, up from under 5% a year earlier.
- About 79% of enterprises say they have adopted AI agents, but only about 11% run them in production; roughly 88% of agent pilots do not reach production. Top blockers: evaluation gaps (64%), governance friction (57%), model reliability (51%).
- 22% of production deployments coordinate three or more agents; the Model Context Protocol (MCP) has passed 9,400 public servers.
- 56% of enterprises now name a dedicated "AI agent owner" or "agentic ops" lead, up from 11% in 2024.
- The AI agent market is estimated at $10.9B in 2026, growing at about 49.6% CAGR toward $183B by 2033.

## 3. Investment, adoption, and infrastructure

- Global corporate AI investment reached $581.7B (+130% year over year); generative AI investment rose nearly fivefold to $170.9B. (Stanford AI Index 2026)
- 88% of surveyed organizations use AI. Generative AI reached 53% population adoption within three years, faster than the PC or the internet. (Stanford AI Index 2026)
- The four largest hyperscalers plan up to about $630B in 2026 capex, about 62% above the record $388B in 2025; including a fifth company, estimates reach $775–800B. Roughly 75% is tied directly to AI infrastructure.
  - Amazon: about $200B; Alphabet: $175–185B; Meta: $115–135B; Microsoft: $110–120B.
- Goldman Sachs projects hyperscaler capex of $1.15T over 2025–2027, more than double the $477B spent over 2022–2024.

## 4. Energy demand

- Data-centre electricity demand grew 17% in 2025, while AI-focused data centres grew 50%, against about 3% growth in global electricity demand. (IEA)
- The IEA projects data-centre electricity use roughly doubling to about 950 TWh by 2030 (about 3% of global demand), with AI-focused use tripling. Some estimates put 2026 consumption above 1,000 TWh.
- U.S. data-centre power demand is projected to rise from 31 GW (2025) to 41 GW (2026). Power is becoming a key bottleneck, and operators are looking at advanced nuclear power. (IAEA)

## 5. Science and healthcare

- AI systems perform at or above physician level on selected diagnostic and clinical decision tasks, such as rapid detection of brain hemorrhages on scans.
- A JAMA study across five academic medical centres found AI ambient scribes cut EHR time by 13.4 minutes and documentation time by 16 minutes per encounter.
- Generative AI is shortening drug discovery timelines; protein-design models have produced binders experimentally validated against more than 130 targets.
- More than 8,500 registered AI clinical trials were analysed in 2026; prognostic AI slightly outnumbered diagnostic AI, signalling a shift toward preventive care.

## 6. Labour market

- No detectable rise in aggregate unemployment among highly AI-exposed workers since late 2022; large-scale job losses have not shown up in overall employment data.
- Impact is concentrated: entry-level hiring fell sharply in 2025, routine roles lost about 13% of openings after ChatGPT launched, while analytical, technical, and creative roles grew about 20%.
- U.S. job postings requiring AI skills grew 144% year over year (April 2026) versus 7% overall; AI-skilled workers earn wage premiums of up to 62%. (PwC 2026 Global AI Jobs Barometer and others)
- Some surveys show a slightly negative net employment effect for the past year (-5 points) and forecast for 2026 (-2 points). (S&P Global)

## 7. Risks and safety

- Deepfake-related fraud and scams are increasing. (International AI Safety Report 2026)
- In one evaluation an AI agent found 77% of known vulnerabilities in real software, showing both defensive and offensive cyber potential.
- Of 375 surveyed biological AI tools, only 3% have safeguards; 23% of the top-performing tools have high misuse potential.
- Models remain less reliable on long multi-step tasks and still hallucinate. Pre-deployment testing is getting harder because models can sometimes tell test settings from real use.
- 362 AI incidents were recorded; the Foundation Model Transparency Index fell from 58 to 40, and major labs stopped disclosing dataset sizes and training durations. (Stanford AI Index 2026)
- Perception gap: 73% of experts are optimistic about AI versus 23% of the public. (Stanford AI Index 2026)

## 8. Regulation and governance

- **EU AI Act:** general-purpose AI rules applied from August 2025; most provisions apply from August 2026; the high-risk AI deadline has been pushed back to 2 December 2027 under a simplification deal.
- **Korea AI Basic Act:** in force since 22 January 2026. It applies to foreign companies serving Korean users, requires transparency for generative AI, imposes safety duties on models above a compute threshold, and sets obligations for high-impact AI in healthcare, hiring, lending, and energy.
- The EU and South Korea are currently the only jurisdictions with comprehensive AI laws in force.

## Key takeaways

1. Capability is still rising quickly, with coding and reasoning gains the most visible.
2. The focus is shifting from chatbots to agents, but most agent projects have not reached production yet.
3. Investment and infrastructure spending are at record levels, making electricity a key constraint.
4. Benefits are clear in science and healthcare; labour impacts are uneven rather than broad.
5. Safety, transparency, and public trust lag behind capability, and regulation is just starting to take effect.

## Sources

- Stanford HAI, *The 2026 AI Index Report*: https://hai.stanford.edu/ai-index/2026-ai-index-report
- Stark Insider, Stanford's 2026 AI Index summary: https://www.starkinsider.com/2026/04/stanford-2026-ai-index-report.html
- Pebblous, AI Index 2026 decoded: https://blog.pebblous.ai/report/hai-ai-index-2026-part1/en/
- International AI Safety Report 2026: https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026
- Inside Global Tech, AI Safety Report summary: https://www.insideglobaltech.com/2026/02/10/international-ai-safety-report-2026-examines-ai-capabilities-risks-and-safeguards/
- Prefactor, AI agent adoption statistics: https://prefactor.tech/learn/ai-agent-adoption-statistics
- Digital Applied, AI agent adoption 2026: https://www.digitalapplied.com/blog/ai-agent-adoption-2026-enterprise-data-points
- The Stacc, AI agent adoption statistics: https://thestacc.com/blog/ai-agent-adoption-statistics/
- Futurum, AI capex 2026: https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/
- Introl, Hyperscaler capex 2026: https://introl.com/blog/hyperscaler-capex-600b-2026-ai-infrastructure-debt-january-2026
- Data Center Richness, Hyperscalers plan $630B: https://datacenterrichness.substack.com/p/hyperscalers-plan-630-billion-in
- IEA, Energy and AI: https://iea.blob.core.windows.net/assets/3179f7f8-01f6-4dd6-bffa-c9f7b73f1dc9/KeyQuestionsonEnergyandAI.pdf
- Enlit, IEA data-centre electricity findings: https://www.enlit.world/library/ai-and-data-centre-electricity-use-continue-to-surge-iea-finds
- IAEA Bulletin, data centres and nuclear power: https://www.iaea.org/bulletin/data-centres-artificial-intelligence-and-cryptocurrencies-eye-advanced-nuclear-to-meet-growing-power-needs
- Crescendo, AI in healthcare news: https://www.crescendo.ai/news/ai-in-healthcare-news
- S&P Global, AI impact on employment 2026: https://www.spglobal.com/en/research-insights/special-reports/ai-impact-on-employment-2026
- PwC, 2026 Global AI Jobs Barometer: https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-jobs-barometer.html
- Digital Applied, AI and jobs 2026: https://www.digitalapplied.com/blog/ai-and-jobs-2026-what-the-labor-data-shows-analysis
- Cooley, Korea's AI Basic Act: https://www.cooley.com/news/insight/2026/2026-01-27-south-koreas-ai-basic-act-overview-and-key-takeaways
- Stimson Center, Korea's AI Basic Act: https://www.stimson.org/2026/south-koreas-ai-basic-act-seeking-balance-between-industry-innovation-and-social-risk/
- StationX, AI regulations around the world 2026: https://app.stationx.net/articles/ai-regulations-around-the-world

# 조사 노트: AI 발전 (2026년 10월 업데이트)

조사일: 2026-10-04

이 노트는 2026년 10월 기준 인공지능(AI) 발전 현황에 관한 공개 자료를 모은 것입니다. 보고서 `report/AI_발전_보고서_v2.docx`의 기초 자료입니다. 일부 수치는 원 보고서가 아닌 2차 요약 자료에서 가져왔으므로 개별 수치는 참고용으로 보시기 바랍니다. 출처끼리 수치가 다르면 둘 다 적었습니다.

## 1. 성능과 프론티어 모델

- AI 성능은 정체되지 않고 오히려 빨라지고 있습니다. SWE-bench 코딩 벤치마크 최고 점수는 1년 만에 약 60%에서 100% 가까이로 올랐습니다. (Stanford AI Index 2026)
- 프론티어 성능은 "들쭉날쭉(jagged)"합니다. 국제수학올림피아드에서 금메달 수준을 낸 모델이 아날로그 시계는 50.1%만 정확히 읽습니다. 대표 벤치마크 점수로는 실제 업무 성능을 잘 알 수 없습니다. (Stanford AI Index 2026)
- 미국과 중국의 성능 격차는 사실상 사라졌습니다. (Stanford AI Index 2026)
- 모델 출시 속도가 매우 빠릅니다. 2026년 2~6월에 Gemini 3.1 Pro, GPT-5.5, Grok 4.3, Qwen 3.7 Max, DeepSeek V4, GLM-5.2, Kimi K2.6 등이 나왔습니다. 2026년 9월 초에는 GPT-6 Astra, Claude Fable 5.1, Gemini 3.8 Flash, Meta Muse Spark 1.3이 이틀 사이에 잇따라 출시되었습니다. (업계 동향 사이트, 2차 자료)
- 오픈 웨이트 모델도 프론티어에 근접했습니다. DeepSeek V4(2026년 4월 24일, MIT 라이선스)는 1.6조 파라미터 MoE 모델로, 활성 파라미터는 490억 개이고 100만 토큰 컨텍스트를 지원합니다. 상위 5개 오픈 웨이트 모델 중 4개가 중국 연구소에서 나왔습니다. (업계 동향 사이트, 2차 자료)
- 모델 가격은 계속 내려가고 있습니다. 한 추적 사이트에 따르면 2026년 9월 기준 모델 간 가격 차이는 119배이고, 최저가는 100만 토큰당 0.10달러입니다. (업계 동향 사이트, 2차 자료)

## 2. AI 에이전트

- AI는 챗봇에서 에이전트로 옮겨가고 있습니다. 에이전트는 도구를 쓰고, 웹을 탐색하고, 컴퓨터를 조작하고, 파일을 관리하고, 소프트웨어 개발 작업을 합니다. (International AI Safety Report 2026)
- Gartner에 따르면 2026년 1분기에 출시되거나 업데이트된 기업용 애플리케이션의 80%가 AI 에이전트를 하나 이상 탑재했습니다. 2024년에는 33%였습니다.
- 도입률은 조사마다 다릅니다. 기업의 65%가 이미 AI 에이전트를 쓰고 있다고 답했고(CrewAI 조사), 실무자의 57.3%가 에이전트를 실제 운영 중이라고 답했습니다(이전 조사 51%).
- 기업들은 평균 31%의 업무 흐름을 에이전트 AI로 자동화했고, 2026년에 33% 더 늘릴 계획입니다.
- 실제 운영까지 가는 비율은 낮습니다. 에이전트 시범 사업의 약 88%가 운영 단계로 넘어가지 못합니다. 주요 걸림돌은 평가 체계 부족(64%), 거버넌스 마찰(57%), 모델 신뢰성(51%)입니다.

## 3. 투자와 인프라

- J.P. Morgan은 2026년 하이퍼스케일러 설비투자를 6,970억 달러로 추정합니다. 다른 추정은 빅4의 설비투자를 최대 6,300억 달러로 보며, 이는 2025년 최고 기록인 3,880억 달러보다 약 62% 많습니다.
  - Amazon 약 2,000억 달러, Meta 1,150억~1,350억 달러(전년 720억 달러), Microsoft 1,100억~1,200억 달러(전년 900억 달러)
- 2026년 하이퍼스케일러 설비투자의 약 75%(약 5,450억 달러)가 AI 인프라에 쓰입니다. 그중 60% 이상은 연산 장비가 아니라 전력, 냉각, 데이터센터 건설에 들어갑니다.
- 이제 AI 인프라의 가장 큰 병목은 전력입니다.
- 조직의 88%가 AI를 쓰고 있으며, 생성형 AI는 PC나 인터넷보다 빠르게 인구 보급률 53%에 도달했습니다. (Stanford AI Index 2026)

## 4. 에너지 수요

- 2025년 데이터센터 전력 사용량은 약 485TWh였습니다. 2025년 데이터센터 전력 수요는 17% 늘었고, AI 중심 데이터센터의 수요는 50% 늘었습니다. 전 세계 전력 수요 증가율은 약 3%에 그쳤습니다. (IEA)
- IEA는 2030년 데이터센터 전력 사용량을 약 950TWh로 전망합니다. 2025년의 약 두 배이며 전 세계 전력 수요의 약 3%입니다. AI 중심 데이터센터의 사용량은 2025~2030년에 세 배로 늘어날 것으로 봅니다. (IEA)

## 5. 고용과 경제

- 미국 전체 채용 공고의 2.5%가 AI 역량을 요구합니다. 전년보다 55%, 10년 전보다 297% 늘었습니다. (Stanford AI Index 2026)
- 27개 국가·지역의 채용 공고 10억 건 이상을 분석한 PwC의 2026 Global AI Jobs Barometer 결과는 다음과 같습니다.
  - AI 역량 보유자의 평균 임금 프리미엄은 62%로 올랐습니다(전년 57%). 업종별로는 공공 부문 16%에서 소비재 시장 118%까지 차이가 납니다.
  - AI 역량을 요구하는 일자리는 69% 늘어, 전체 일자리 증가율(9%)보다 약 8배 빨랐습니다.
  - AI 활용 역량이 가장 높은 기업은 가장 낮은 기업보다 인원(52% 대 36%)과 임금(24% 대 17%)이 더 빠르게 늘었습니다.
- 가장 크게 바뀌는 곳은 신입 일자리입니다. 고용주의 38%가 기초 데이터 처리 업무를 신입 직원에서 AI로 옮겼고, 31%는 신입 채용의 경력 요건을 높였습니다. (ZipRecruiter AI Employer Report 2026)
- AI 영향을 받는 신입 직무는 판단력, 리더십 같은 시니어급 역량을 요구할 가능성이 7배 높습니다. (PwC 2026)
- 종합하면, AI가 신입 일자리를 아예 없애기보다는 요구 수준을 높이고 전통적인 진입 경로를 좁히고 있다는 분석이 많습니다.

## 6. 규제와 정책

### 유럽연합

- 디지털 옴니버스 패키지(Regulation (EU) 2026/1744)는 2026년 6월 29일 이사회 최종 승인을 받아 2026년 7월 27일부터 시행 중입니다.
- 독립형 고위험 AI 시스템(부속서 III: 고용, 신용평가, 교육, 필수 서비스 등)에 대한 의무는 2026년 8월 2일에서 2027년 12월 2일로 미뤄졌습니다. 규제 대상 제품에 들어가는 AI(부속서 I)는 2028년 8월 2일로 미뤄졌습니다.
- 제50조 투명성 의무(AI와 상호작용 중임을 알리는 의무)는 예정대로 2026년 8월 2일부터 적용됩니다. 이미 출시된 시스템의 워터마크 의무만 2026년 12월 2일까지 유예되었습니다.

### 미국

- 행정명령 "인공지능에 관한 국가 정책 체계 확립"(2025년 12월 11일)은 "최소한의 부담을 주는 국가 표준"과 주(州) AI 법에 대한 연방 우선 적용을 추진합니다.
- 주 법률에 소송으로 대응하는 AI 소송 태스크포스가 만들어졌고, 상무부는 2026년 3월 11일까지 부담이 되는 주 법률을 선별해야 했습니다.
- 행정명령만으로는 주 법률을 무효로 만들 수 없고, 의회 입법이나 법원 판결이 필요합니다. 따라서 주 법률은 당분간 그대로 효력이 있습니다.

### 대한민국

- AI 기본법(인공지능 발전과 신뢰 기반 조성 등에 관한 기본법)이 2026년 1월 22일 시행되었습니다. EU AI법은 단계적으로 적용되므로, 포괄적 AI 법을 전면 시행한 것은 세계 최초로 평가됩니다.
- 위험 기반 접근 방식을 택했습니다. 채용, 대출 심사, 의료, 교육, 교통 등 약 10개 영역의 고영향 AI에는 더 엄격한 의무가 적용됩니다.
- 생성형 AI는 이용자에게 사전 고지를 하고, 결과물에 표시나 워터마크를 넣어야 합니다.
- R&D 지원, AI 데이터센터 구축, 인재 양성 등 산업 진흥 내용도 들어 있습니다. 정부는 전면 집행 전에 최소 1년 이상의 계도 기간을 둘 계획입니다.

## 7. 안전과 위험

- 기록된 AI 사고는 1년 사이 233건에서 362건으로 늘었습니다. 미국 중·고등학교의 절반만 AI 정책을 갖추고 있습니다. (Stanford AI Index 2026)
- International AI Safety Report 2026은 위험을 세 가지로 나눕니다.
  - **악의적 사용:** 딥페이크 사기가 늘고 있습니다. 한 평가에서 AI 에이전트가 실제 소프트웨어의 알려진 취약점 중 77%를 찾아냈습니다. 조사한 생물학 AI 도구 375개 중 안전장치가 있는 것은 3%뿐입니다.
  - **오작동:** 환각은 줄었지만 위험 관리 기법은 여전히 완벽하지 않습니다. 모델이 테스트 환경과 실제 배포 환경을 구분할 수 있어 배포 전 안전성 테스트가 더 어려워졌습니다.
  - **시스템적 위험:** 특히 지식 노동에서 다양한 인지 업무가 자동화될 수 있습니다.
- 장기적인 발전 방향은 매우 불확실합니다. 2030년 시나리오는 정체부터 급격한 가속까지 폭이 넓습니다. (International AI Safety Report 2026)

## 8. 한국의 AI 전략

- 한국은 2025년 APEC에서 엔비디아 GPU 26만 장 공급 약속을 받았고, 2028년까지 GPU 5만 장을 자체 확보하는 것을 목표로 합니다.
- 독자 AI 파운데이션 모델 프로젝트는 정예팀(현재 LG, SKT, 업스테이지, 모티프)에 GPU, 데이터, 인재를 지원합니다. 목표는 글로벌 최고 모델 대비 95% 이상의 성능입니다.
- 주요 과제는 전력 공급(전력 계통 연결 신청이 약 8배 증가)과 모델의 독자성 논란입니다.

## 9. 핵심 시사점

1. 성능은 빠르게 오르지만 고르지 않으며, 벤치마크는 실제 신뢰성을 과대평가합니다.
2. 에이전트가 빠르게 퍼지고 있지만 시범 사업 대부분은 아직 실제 운영까지 가지 못합니다.
3. 투자는 사상 최대이며, 전력이 가장 큰 제약이 되었습니다.
4. AI는 숙련 인력의 임금과 생산성을 높이는 한편 전통적인 신입 진입 경로를 좁힙니다.
5. 규제 방향이 갈라지고 있습니다. EU는 일부 규정을 미루고, 미국은 연방 우선 적용을 추진하며, 한국은 포괄적인 법을 시행했습니다.
6. 안전 관행과 정책이 성능 발전을 따라가지 못하고 있습니다.

## 출처

- Stanford HAI, AI Index Report 2026 (요약: https://www.starkinsider.com/2026/04/stanford-2026-ai-index-report.html, https://dcthemedian.substack.com/p/20-takeaways-from-stanfords-2026)
- International AI Safety Report 2026: https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026
- IEA, Energy and AI: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
- PwC, 2026 Global AI Jobs Barometer: https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-jobs-barometer.html
- ZipRecruiter, 2026 AI Employer Report: https://www.ziprecruiter-research.org/economic-insights-research/ai-employer-report-2026
- AI 에이전트 도입: https://www.digitalcommerce360.com/2026/02/11/survey-enterprises-ai-agents-crewai-report/, https://www.digitalapplied.com/blog/ai-agent-adoption-2026-enterprise-data-points
- 하이퍼스케일러 설비투자: https://www.jpmorgan.com/insights/banking/capital-markets/financing-ai-infrastructure-data-centers, https://datacenterrichness.substack.com/p/hyperscalers-plan-630-billion-in
- 프론티어 모델: https://www.teamday.ai/blog/best-ai-models-2026, https://neuralwired.com/2026/05/29/best-open-source-ai-models-2026/, https://local-ai-zone.github.io/blog/September_2026_AI_Model_Updates.html
- EU 디지털 옴니버스: https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes, https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
- 미국 행정명령: https://www.hoganlovells.com/en/publications/white-house-issues-executive-order-to-establish-a-federal-ai-policy-and-preempt-state-laws, https://www.ropesgray.com/en/insights/alerts/2026/03/the-white-house-legislative-recommendations-national-policy-framework-for-artificial-intelligence-an
- 한국 AI 기본법: https://kbthink.com/life/daily/ai-basic-act.html, https://www.shinkim.com/kor/media/newsletter/3114
- 한국 소버린 AI와 GPU: https://www.hankyung.com/article/202605318606i, https://biz.heraldcorp.com/article/10766420, https://factrace.kr/topics/ai-industry-2026

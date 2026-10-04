const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  LevelFormat, PageBreak, Footer, PageNumber, TableOfContents,
} = require('docx');

const OUT = process.argv[2];
const FONT = '맑은 고딕';

const p = (text, opts = {}) => new Paragraph({
  spacing: { after: 120, line: 320 },
  ...opts,
  children: [new TextRun({ text, font: FONT, size: 22, ...(opts.run || {}) })],
});
const h1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 360, after: 200 }, children: [new TextRun({ text: t, font: FONT })] });
const h2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 240, after: 120 }, children: [new TextRun({ text: t, font: FONT })] });
const bullet = (text, level = 0) => new Paragraph({
  numbering: { reference: 'bullets', level },
  spacing: { after: 80, line: 300 },
  children: [new TextRun({ text, font: FONT, size: 22 })],
});
const numbered = (text) => new Paragraph({
  numbering: { reference: 'numbers', level: 0 },
  spacing: { after: 80, line: 300 },
  children: [new TextRun({ text, font: FONT, size: 22 })],
});

const border = { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF' };
const borders = { top: border, bottom: border, left: border, right: border };
function table(headers, rows, widths) {
  const total = widths.reduce((a, b) => a + b, 0);
  const cell = (text, i, head) => new TableCell({
    width: { size: widths[i], type: WidthType.DXA },
    borders,
    shading: head ? { type: ShadingType.CLEAR, fill: '1F3864', color: 'auto' } : undefined,
    margins: { top: 80, bottom: 80, left: 120, right: 120 },
    children: [new Paragraph({ children: [new TextRun({ text, font: FONT, size: 20, bold: head, color: head ? 'FFFFFF' : '000000' })] })],
  });
  return new Table({
    width: { size: total, type: WidthType.DXA },
    columnWidths: widths,
    rows: [
      new TableRow({ tableHeader: true, children: headers.map((h, i) => cell(h, i, true)) }),
      ...rows.map((r) => new TableRow({ children: r.map((c, i) => cell(c, i, false)) })),
    ],
  });
}
const caption = (t) => new Paragraph({ spacing: { before: 80, after: 200 }, children: [new TextRun({ text: t, font: FONT, size: 18, italics: true, color: '595959' })] });

const W = 9026; // A4 content width with 1" margins

const children = [
  // Title page
  new Paragraph({ spacing: { before: 3000, after: 300 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: 'AI 발전 현황과 전망', font: FONT, size: 56, bold: true, color: '1F3864' })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 1200 }, children: [new TextRun({ text: '2026년 10월 기준 자료조사 보고서', font: FONT, size: 28, color: '595959' })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: '작성일: 2026년 10월 4일', font: FONT, size: 22 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: '근거 자료: research/ai-development-research-v2.md', font: FONT, size: 20, color: '595959' })] }),
  new Paragraph({ children: [new PageBreak()] }),

  // TOC
  new Paragraph({ spacing: { after: 200 }, children: [new TextRun({ text: '목차', font: FONT, size: 32, bold: true })] }),
  new TableOfContents('목차', { hyperlink: true, headingStyleRange: '1-2' }),
  new Paragraph({ children: [new PageBreak()] }),

  // 서론
  h1('Ⅰ. 서론'),
  h2('1. 배경'),
  p('2026년 현재 인공지능(AI)은 연구실의 기술을 넘어 기업 경영, 노동시장, 에너지 정책, 국가 전략을 함께 바꾸는 범용 기술이 되었습니다. 코딩 벤치마크 점수가 1년 만에 약 60%에서 100% 가까이로 오르는 등 성능은 빠르게 높아지고 있으며, 조직의 88%가 AI를 쓰고 있습니다. 동시에 AI 사고 증가, 전력 부족, 신입 일자리 변화, 각국의 규제 경쟁 같은 새로운 과제도 커지고 있습니다.'),
  h2('2. 목적'),
  p('이 보고서는 2026년 10월 기준 공개 자료를 바탕으로 AI 발전의 현황을 주제별로 정리하고, 그 의미와 앞으로의 과제를 제시하는 것을 목적으로 합니다.'),
  h2('3. 범위와 방법'),
  bullet('범위: 기술 성능, AI 에이전트, 투자와 인프라, 에너지, 고용과 경제, 규제와 정책, 안전과 위험, 한국의 AI 전략'),
  bullet('주요 자료: Stanford AI Index 2026, International AI Safety Report 2026, IEA 에너지와 AI 보고서, PwC 2026 Global AI Jobs Barometer, 각국 법령·정책 자료와 언론 보도'),
  bullet('한계: 일부 수치는 원 보고서가 아닌 2차 요약 자료에서 인용했으므로 참고용으로 보아야 합니다. 조사마다 수치가 다른 경우 함께 제시했습니다.'),

  // 본론
  new Paragraph({ children: [new PageBreak()] }),
  h1('Ⅱ. 본론'),

  h2('1. 기술 성능: 빠르지만 고르지 않은 발전'),
  p('AI 성능은 정체되지 않고 오히려 빨라지고 있습니다. SWE-bench 코딩 벤치마크 최고 점수는 1년 만에 약 60%에서 100% 가까이로 올랐고, 미국과 중국의 성능 격차는 사실상 사라졌습니다. 2026년 9월 초에는 GPT-6 Astra, Claude Fable 5.1, Gemini 3.8 Flash 등 주요 모델이 이틀 사이에 잇따라 출시될 만큼 경쟁이 치열합니다.'),
  p('다만 성능은 "들쭉날쭉(jagged)"합니다. 국제수학올림피아드 금메달 수준의 모델이 아날로그 시계는 50.1%만 정확히 읽습니다. 벤치마크 점수만으로는 실제 업무에서의 신뢰성을 판단하기 어렵다는 뜻입니다.'),
  p('오픈 웨이트 모델도 프론티어에 근접했습니다. DeepSeek V4(1.6조 파라미터, MIT 라이선스) 등 상위 오픈 웨이트 모델 5개 중 4개가 중국에서 나왔으며, 모델 가격은 100만 토큰당 0.10달러 수준까지 내려갔습니다.'),

  h2('2. AI 에이전트: 확산과 운영 격차'),
  p('AI는 질문에 답하는 챗봇에서, 도구를 쓰고 컴퓨터를 조작해 일을 직접 처리하는 에이전트로 옮겨가고 있습니다. Gartner에 따르면 2026년 1분기에 출시·업데이트된 기업용 애플리케이션의 80%가 AI 에이전트를 하나 이상 탑재했습니다(2024년 33%).'),
  table(['지표', '수치', '출처'], [
    ['에이전트 탑재 기업용 앱 비율', '80% (2024년 33%)', 'Gartner'],
    ['AI 에이전트 사용 기업', '65%', 'CrewAI 조사'],
    ['에이전트 실제 운영 비율', '57.3% (이전 51%)', '업계 조사'],
    ['에이전트로 자동화한 업무 흐름', '평균 31%', '업계 조사'],
    ['운영 단계에 못 간 시범 사업', '약 88%', '업계 조사'],
  ], [3600, 2713, 2713]),
  caption('표 1. AI 에이전트 도입 주요 지표'),
  p('그러나 시범 사업의 약 88%가 실제 운영 단계로 넘어가지 못합니다. 주요 걸림돌은 평가 체계 부족(64%), 거버넌스 마찰(57%), 모델 신뢰성(51%)입니다. 도입 의지는 높지만 이를 안정적으로 운영할 체계가 아직 부족한 상황입니다.'),

  h2('3. 투자와 인프라: 사상 최대 투자, 전력이 병목'),
  p('2026년 하이퍼스케일러의 설비투자는 6,300억~6,970억 달러로 추정되며, 2025년(3,880억 달러)보다 약 62% 이상 늘어난 규모입니다. 이 중 약 75%(약 5,450억 달러)가 AI 인프라에 쓰입니다.'),
  table(['기업', '2026년 설비투자 계획', '2025년'], [
    ['Amazon', '약 2,000억 달러', '-'],
    ['Meta', '1,150억~1,350억 달러', '720억 달러'],
    ['Microsoft', '1,100억~1,200억 달러', '900억 달러'],
  ], [3008, 3009, 3009]),
  caption('표 2. 주요 하이퍼스케일러 설비투자 계획'),
  p('주목할 점은 AI 인프라 투자의 60% 이상이 반도체가 아니라 전력, 냉각, 데이터센터 건설에 들어간다는 것입니다. 이제 AI 확장의 가장 큰 제약은 연산 장비가 아니라 전력입니다.'),

  h2('4. 에너지: 데이터센터 전력 수요 급증'),
  p('IEA에 따르면 2025년 데이터센터 전력 사용량은 약 485TWh로, 1년 동안 17% 늘었습니다. 특히 AI 중심 데이터센터의 수요는 50% 늘어 전 세계 전력 수요 증가율(약 3%)을 크게 웃돌았습니다.'),
  p('IEA는 2030년 데이터센터 전력 사용량이 약 950TWh로 2025년의 두 배가 되고, 전 세계 전력 수요의 약 3%를 차지할 것으로 전망합니다. AI 중심 데이터센터의 사용량은 같은 기간 세 배로 늘어날 것으로 봅니다. 전력망 확충과 에너지 효율이 AI 경쟁력의 핵심 요소가 되고 있습니다.'),

  h2('5. 고용과 경제: 임금 프리미엄과 신입 일자리 변화'),
  p('AI는 숙련 인력의 가치를 높이고 있습니다. PwC가 27개 국가·지역의 채용 공고 10억 건 이상을 분석한 결과, AI 역량 보유자의 평균 임금 프리미엄은 62%로 전년(57%)보다 높아졌고, AI 역량을 요구하는 일자리는 전체 일자리보다 약 8배 빠르게(69% 대 9%) 늘었습니다. 미국 채용 공고의 2.5%가 AI 역량을 요구하며, 이는 10년 전보다 297% 늘어난 수치입니다.'),
  p('반면 신입 일자리는 큰 변화를 겪고 있습니다. 고용주의 38%가 기초 데이터 처리 업무를 신입 직원에서 AI로 옮겼고, 31%는 신입 채용의 경력 요건을 높였습니다. AI 영향을 받는 신입 직무는 판단력, 리더십 같은 시니어급 역량을 요구할 가능성이 7배 높습니다. AI가 신입 일자리를 없애기보다는, 일을 배우던 기초 업무를 대신하면서 진입 문턱을 높이고 있다고 볼 수 있습니다.'),

  h2('6. 규제와 정책: 갈라지는 각국의 방향'),
  table(['구분', '주요 내용', '시점'], [
    ['EU', '디지털 옴니버스로 고위험 AI 의무 연기. 투명성 의무(제50조)는 예정대로 적용', '고위험(부속서 III) 2027.12.2 / 제품 내장 AI 2028.8.2'],
    ['미국', '행정명령으로 주(州) AI 법에 대한 연방 우선 적용 추진, AI 소송 태스크포스 설치', '2025.12.11 행정명령'],
    ['한국', 'AI 기본법 전면 시행. 고영향 AI 관리 의무, 생성형 AI 표시 의무, 산업 진흥', '2026.1.22 시행, 1년 이상 계도 기간'],
  ], [1400, 4626, 3000]),
  caption('표 3. 주요국 AI 규제 동향'),
  p('EU는 산업 경쟁력을 고려해 고위험 AI 규정의 적용을 16개월 미뤘지만, AI와 대화 중임을 알리는 투명성 의무는 그대로 유지했습니다. 미국은 주마다 다른 규제를 연방 차원에서 정리하려 하지만, 행정명령만으로는 주 법률을 무효로 만들 수 없어 법적 불확실성이 남아 있습니다.'),
  p('한국은 2026년 1월 22일 AI 기본법을 시행해, 포괄적 AI 법을 전면 시행한 세계 첫 국가로 평가됩니다. 채용, 대출, 의료, 교육, 교통 등 약 10개 영역의 고영향 AI에 더 엄격한 의무를 부과하고, 생성형 AI 결과물에는 표시나 워터마크를 넣도록 했습니다. 동시에 R&D, 데이터센터, 인재 양성 지원 같은 진흥 정책도 담았습니다.'),

  h2('7. 안전과 위험'),
  p('기록된 AI 사고는 1년 사이 233건에서 362건으로 늘었습니다. International AI Safety Report 2026은 위험을 세 가지로 나눕니다.'),
  bullet('악의적 사용: 딥페이크 사기가 늘고 있으며, 한 평가에서 AI 에이전트가 실제 소프트웨어의 알려진 취약점 중 77%를 찾아냈습니다. 생물학 AI 도구 375개 중 안전장치를 갖춘 것은 3%뿐입니다.'),
  bullet('오작동: 환각은 줄었지만, 모델이 테스트 환경과 실제 환경을 구분할 수 있어 배포 전 안전성 검증이 더 어려워졌습니다.'),
  bullet('시스템적 위험: 지식 노동을 중심으로 다양한 인지 업무가 자동화될 수 있습니다.'),
  p('보고서는 2030년까지의 시나리오가 정체부터 급격한 가속까지 폭넓다고 보며, 안전 관행과 정책이 성능 발전을 따라가지 못하고 있다고 지적합니다.'),

  h2('8. 한국의 AI 전략'),
  p('한국은 2025년 APEC에서 엔비디아 GPU 26만 장 공급 약속을 받았고, 2028년까지 GPU 5만 장을 자체 확보하는 것을 목표로 합니다. 독자 AI 파운데이션 모델 프로젝트에서는 LG, SKT, 업스테이지, 모티프 정예팀이 글로벌 최고 모델 대비 95% 이상의 성능을 목표로 개발하고 있습니다.'),
  p('주요 과제는 전력 공급(전력 계통 연결 신청 약 8배 증가)과 모델의 기술 독자성 확보입니다. 세계적 흐름과 마찬가지로 한국에서도 전력이 AI 경쟁력의 핵심 변수가 되고 있습니다.'),

  // 결론
  new Paragraph({ children: [new PageBreak()] }),
  h1('Ⅲ. 결론'),
  h2('1. 요약'),
  numbered('AI 성능은 빠르게 오르지만 고르지 않으며, 벤치마크는 실제 신뢰성을 과대평가합니다.'),
  numbered('AI 에이전트가 빠르게 퍼지고 있지만, 시범 사업 대부분은 아직 실제 운영까지 가지 못합니다.'),
  numbered('투자는 사상 최대이며, 전력이 가장 큰 제약이 되었습니다.'),
  numbered('AI는 숙련 인력의 임금과 생산성을 높이는 한편, 전통적인 신입 진입 경로를 좁힙니다.'),
  numbered('규제 방향이 갈라지고 있습니다. EU는 일부 규정을 미루고, 미국은 연방 우선 적용을 추진하며, 한국은 포괄적인 법을 시행했습니다.'),
  numbered('안전 관행과 정책이 성능 발전을 따라가지 못하고 있습니다.'),
  h2('2. 전망'),
  p('단기적으로는 에이전트의 실제 운영 전환, 전력 확보 경쟁, 오픈 웨이트 모델의 확산이 AI 산업의 방향을 좌우할 것입니다. 장기적인 발전 속도는 불확실하지만, AI가 경제와 사회 전반에 미치는 영향은 앞으로 더 커질 것으로 보입니다.'),
  h2('3. 시사점'),
  bullet('기업: 에이전트 도입보다 평가 체계와 거버넌스를 먼저 갖춰야 시범 사업을 실제 성과로 연결할 수 있습니다.'),
  bullet('개인과 교육: AI 역량과 함께 판단력, 리더십 같은 인간 고유의 역량을 일찍부터 키워야 합니다. 신입이 경험을 쌓을 새로운 경로도 필요합니다.'),
  bullet('정부: 전력망과 데이터센터 인프라 확충이 AI 정책의 핵심이 되어야 합니다. AI 기본법 계도 기간 동안 기업이 따를 수 있는 명확한 기준을 마련해야 합니다.'),
  bullet('사회: AI 사고와 딥페이크 피해에 대응할 안전 검증 체계와 이용자 보호 장치를 강화해야 합니다.'),

  // 참고문헌
  new Paragraph({ children: [new PageBreak()] }),
  h1('참고문헌'),
  ...[
    'Stanford HAI, AI Index Report 2026 (2026.4)',
    'International AI Safety Report 2026 (2026.2), internationalaisafetyreport.org',
    'IEA, Energy and AI, iea.org/reports/key-questions-on-energy-and-ai',
    'PwC, 2026 Global AI Jobs Barometer, pwc.com',
    'ZipRecruiter Economic Research, 2026 AI Employer Report',
    'J.P. Morgan, Financing AI infrastructure and U.S. data centers',
    'Digital Commerce 360, Survey: Enterprises move AI agents from pilots to production (2026.2)',
    'Orrick, EU AI Act Update: Digital Omnibus Finalizes 8 Compliance Changes (2026.7)',
    'Gibson Dunn, EU AI Act Omnibus Agreement — Postponed High-Risk Deadlines',
    'Hogan Lovells, White House issues executive order to establish a federal AI policy and preempt state laws',
    'KB Think, AI 기본법 시행ㅣAI 산업에 어떤 변화가 있을지 살펴봐요',
    '법무법인 세종, AI 기본법 시행과 그 시사점',
    '한국경제, 배경훈 "한국도 프론티어 모델 개발해야…GPU 26만장도 부족" (2026.5)',
    '헤럴드경제, 배경훈-젠슨 황 면담, GPU 26만장·AI 팩토리 연내 도입',
    'TeamDay.ai, Best AI Models 2026 / NeuralWired, Best Open Source AI Models 2026',
  ].map((t) => bullet(t)),
];

const doc = new Document({
  creator: 'Chunsik',
  title: 'AI 발전 현황과 전망',
  styles: {
    default: { document: { run: { font: FONT, size: 22 } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 32, bold: true, color: '1F3864', font: FONT }, paragraph: { outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 26, bold: true, color: '2E5597', font: FONT }, paragraph: { outlineLevel: 1 } },
    ],
  },
  numbering: {
    config: [
      { reference: 'bullets', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
      { reference: 'numbers', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
    ],
  },
  sections: [{
    properties: { page: { margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 18 })] })] }) },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => { fs.mkdirSync(path.dirname(OUT), { recursive: true }); fs.writeFileSync(OUT, buf); console.log('wrote', OUT); });
